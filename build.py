"""Build detailed static pages from the published research Markdown.

--prepare writes Mermaid sources and manifest. Render them with tools/render-diagrams.mjs,
then run this script without --prepare to require and insert the rendered figures.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

import markdown
from bs4 import BeautifulSoup, Comment
from tools.decision_content import render_scores, render_market, validate_decision

SITE = Path(__file__).resolve().parent
DIST = SITE / "dist"
CONTENT = SITE / "content"
VERSION = "hardware-interfaces-20261106"
CHAPTER_IDS = dict(zip("一二三四五六七", ["roadmap", "platforms", "products", "starter", "business", "next", "sources"]))


def version_url(url: str) -> str:
    parts = urlsplit(url)
    if parts.scheme or parts.netloc or not parts.path.endswith((".html", ".css", ".js", ".json", ".svg", ".png")):
        return url
    query = dict(parse_qsl(parts.query))
    query["v"] = VERSION
    return urlunsplit(("", "", parts.path, urlencode(query), parts.fragment))


def chapters_from(text: str) -> tuple[str, dict[str, str]]:
    parts = re.split(r"(?m)(?=^# [一二三四五六七]、)", text)
    chapters = {re.match(r"# ([一二三四五六七])、", part).group(1): part for part in parts[1:]}
    if set(chapters) != set(CHAPTER_IDS):
        raise ValueError("Expected all seven research chapters")
    return parts[0], chapters


def source_blocks(text: str) -> list[dict]:
    result = []
    chapter = ""
    for match in re.finditer(r"(?m)^# ([一二三四五六七])、[^\n]+|```mermaid\s*\n([\s\S]*?)```", text):
        if match.group(1):
            chapter = match.group(1)
            continue
        source = match.group(2).strip() + "\n"
        title_match = re.search(r"(?m)^%% title:\s*(.+)$", source)
        title = title_match.group(1).strip() if title_match else f"第{chapter}章关系图"
        result.append({"id": f"fig-{len(result) + 1:02d}", "chapter": chapter, "title": title, "code": source})
    return result


def prepare_diagrams(blocks: list[dict]) -> dict:
    out = DIST / "diagrams"
    out.mkdir(exist_ok=True)
    path = out / "manifest.json"
    old = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"diagrams": []}
    previous = {item["id"]: item for item in old["diagrams"]}
    manifest = {"engine": "Mermaid 10.9.3", "version": VERSION, "diagrams": []}
    for block in blocks:
        (out / (block["id"] + ".mmd")).write_text(block["code"], encoding="utf-8")
        item = {key: block[key] for key in ["id", "chapter", "title"]}
        item.update({key: value for key, value in previous.get(block["id"], {}).items() if key not in item})
        item["sourceHash"] = hashlib.sha256(block["code"].encode()).hexdigest()
        manifest["diagrams"].append(item)
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def formula_images(text: str) -> list[dict]:
    result = []
    for expression in re.findall(r"\$\$([\s\S]*?)\$\$", text):
        identity = "equation-" + hashlib.sha256(expression.encode()).hexdigest()[:10]
        result.append({"expression": expression, "id": identity})
    return result


def formula_mathml(expression: str) -> str:
    plain = re.sub(r"\\mathrm\{([^}]+)\}", r"\1", expression.strip())
    nodes = []
    for token in re.split(r"([=+\-])", plain):
        if token in ["=", "+", "-"]:
            nodes.append("<mo>" + ("−" if token == "-" else token) + "</mo>")
            continue
        variable = re.fullmatch(r"([A-Za-z]+)(?:_\{([A-Za-z]+)\})?", token.strip())
        if not variable:
            raise ValueError("Unsupported formula: " + token)
        name, subscript = variable.groups()
        node = "<mi>" + html.escape(name) + "</mi>"
        if subscript:
            node = "<msub>" + node + "<mtext>" + subscript + "</mtext></msub>"
        nodes.append(node)
    return '<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow>' + "".join(nodes) + '</mrow><annotation encoding="application/x-tex">' + html.escape(expression) + '</annotation></semantics></math>'


def diagram_figure(item: dict, number: int) -> str:
    svg = version_url("diagrams/" + item["id"] + ".svg")
    png = version_url("diagrams/" + item["id"] + ".png")
    source = "diagrams/" + item["id"] + ".mmd"
    title = f"图 {number} · {item['title']}"
    width = min(item["width"], 1100)
    return f'''<figure class="research-diagram" id="{item['id']}">
<div class="diagram-scroll" style="--diagram-min:{width}px;--diagram-width:{item['width']}px"><picture><source srcset="{svg}" type="image/svg+xml"><img src="{png}" width="{item['width']}" height="{item['height']}" alt="{html.escape(title)}。本研究分析示意。" loading="lazy"></picture></div>
<figcaption><strong>{html.escape(title)}</strong><span>分析示意，关系与适用条件见本节正文。可横向滚动或放大阅读。</span></figcaption>
<div class="diagram-actions"><button class="detail-button" data-diagram-src="{svg}" data-diagram-title="{html.escape(title)}">放大查看 ↗</button><a href="{svg}" target="_blank" rel="noopener noreferrer">SVG 大图</a><a href="{png}" download>PNG 下载</a><a href="{source}" download>Mermaid 图源</a></div></figure>'''


def local_link(url: str) -> str:
    if url.startswith(("http://", "https://", "#")):
        return url
    if url.endswith(".mmd"):
        return url
    if "车载智能化 产品样本" in url:
        return "data/products.json"
    if "车载智能化 评分与市场" in url:
        return "data/decision.json"
    if "来源索引" in url:
        return "references.html"
    if "通用调研大纲" in url:
        return "outline.html"
    if "燃油车端侧 AI" in url:
        return "advanced.html"
    if "车载智能化 通用调研" in url:
        return "research.html"
    return url


def platform_comparison(soup: BeautifulSoup) -> None:
    """Build platform cards from the two research tables, preserving one fact source."""
    marker = soup.find(string=lambda node: isinstance(node, Comment) and node.strip() == "platform-comparison-cards")
    if marker is None:
        return
    tables = list(reversed(marker.find_all_previous("table", limit=2)))
    if len(tables) != 2:
        raise ValueError("Platform comparison requires usage and access tables")
    usage = [row.find_all("td", recursive=False) for row in tables[0].select("tbody > tr")]
    access = [row.find_all("td", recursive=False) for row in tables[1].select("tbody > tr")]
    if len(usage) != 7 or len(access) != 7 or any(len(row) != 5 for row in usage + access):
        raise ValueError("Expected seven named platforms and five comparable fields per table")
    cards = []
    for index, (user, developer) in enumerate(zip(usage, access), 1):
        if user[0].get_text(strip=True) != developer[0].get_text(strip=True):
            raise ValueError("Platform rows must use the same order and labels")
        parts = user[0].get_text("|", strip=True).split("|")
        name, category = parts[0], parts[-1]
        company_link = user[0].find_all("a")[1]
        fields = [("执行位置", user[2]), ("手机与屏幕", user[3])]
        details = [("离线范围", user[4]), ("应用与硬件接入", developer[1]), ("车辆权限边界", developer[2]), ("费用与交付责任", developer[3]), ("我们的切入判断", developer[4])]
        def field_list(items: list) -> str:
            return "<dl>" + "".join("<div><dt>" + label + "</dt><dd>" + cell.decode_contents() + "</dd></div>" for label, cell in items) + "</dl>"
        card_class = "platform-card platform-service" if category == "服务层与集成体验" else "platform-card"
        cards.append('<article class="' + card_class + '"><p class="platform-category">' + f"{index:02d} / " + html.escape(category) + '</p><h4>' + html.escape(name) + '</h4><p class="platform-company">公司：' + str(company_link) + '</p><p class="platform-purpose">' + user[1].decode_contents() + '</p>' + field_list(fields) + '<details><summary>查看离线、接入与切入点</summary>' + field_list(details) + '<p class="platform-card-source">依据：' + str(user[0].find("a")) + '</p></details></article>')
    markup = '<section class="platform-overview" aria-label="七类现有平台速览"><h4>按平台展开查看</h4><div class="platform-grid">' + "".join(cards) + '</div></section>'
    marker.replace_with(BeautifulSoup(markup, "html.parser"))
    tables[0].insert_before(BeautifulSoup('<nav class="platform-jumps" aria-label="平台对照表"><a href="#platform-usage-table">使用能力对比 ↓</a><a href="#platform-access-table">开发与商业条件对比 ↓</a><a href="#platform-choice">产品切入判断 ↓</a></nav><p class="matrix-hint">两张表使用相同的七个对象；窄屏可横向滑动，平台名称列固定显示。</p>', "html.parser"))
    for table, identity in zip(tables, ["platform-usage-table", "platform-access-table"]):
        table["id"] = identity
        table["class"] = ["platform-matrix"]
        table["aria-label"] = "现有平台使用能力对比" if identity == "platform-usage-table" else "现有平台开发与商业条件对比"


def wrap_research_sections(soup: BeautifulSoup) -> None:
    sections = [
        ("carplay-focus", "carplay-focus", "CarPlay接入重点与Android Auto对照"),
        ("hardware-access", "hardware-access", "独立硬件与原车接口选择"),
        ("lumi-reference", "lumi-case", "LUMI产品参照与证据边界"),
        ("integration-references", "integration-references", "独立硬件与接口补充资料"),
    ]
    for identity, class_name, label in sections:
        start = soup.find(string=lambda node: isinstance(node, Comment) and node.strip() == identity + ":start")
        end = soup.find(string=lambda node: isinstance(node, Comment) and node.strip() == identity + ":end")
        if start is None and end is None:
            continue
        if start is None or end is None or start.parent is not end.parent:
            raise ValueError("Paired section markers required: " + identity)
        section = soup.new_tag("section", attrs={"id": identity, "class": class_name, "aria-label": label})
        start.insert_before(section)
        node = start.next_sibling
        while node is not None and node is not end:
            following = node.next_sibling
            section.append(node)
            node = following
        start.extract()
        end.extract()


def fold_platform_evidence(soup: BeautifulSoup) -> None:
    heading = soup.find("h2", string=re.compile("现有平台横向对比"))
    if heading is None:
        return
    details = soup.new_tag("details", attrs={"class": "research-evidence", "id": "platform-evidence"})
    summary = soup.new_tag("summary")
    summary.string = "展开完整平台对照、七张详情卡片与依据"
    details.append(summary)
    heading.insert_before(details)
    node = heading
    while node is not None:
        if node is not heading and getattr(node, "name", None) == "h2":
            break
        following = node.next_sibling
        details.append(node)
        node = following


def attach_decisions(soup: BeautifulSoup, decision: dict) -> None:
    if soup.find(id="carplay-focus"):
        soup.head.append(soup.new_tag("link", rel="stylesheet", href=version_url("carplay.css")))
    if not soup.find(id="platform-scores") and not soup.find(id="market-size"):
        return
    payload = soup.new_tag("script", type="application/json", id="decision-data")
    payload.string = json.dumps(decision, ensure_ascii=False).replace("<", "\\u003c")
    soup.body.append(payload)
    soup.head.append(soup.new_tag("script", src=version_url("decision.js"), defer=True))
    soup.head.append(soup.new_tag("link", rel="stylesheet", href=version_url("decision.css")))
    soup.body.append(BeautifulSoup('<dialog id="score-dialog" aria-labelledby="score-detail-title"><div class="dialog-bar"><h2 id="score-detail-title">评分依据</h2><button id="score-close" class="diagram-close" aria-label="关闭评分详情">×</button></div><div id="score-detail-content"></div></dialog>', "html.parser"))


def render_markdown(text: str, blocks: list[dict], manifest: dict, equations: list[dict], decision: dict) -> str:
    text = re.sub(r"<!-- score-summary:start -->[\s\S]*?<!-- score-summary:end -->", lambda _: render_scores(decision), text)
    text = re.sub(r"<!-- market-summary:start -->[\s\S]*?<!-- market-summary:end -->", lambda _: render_market(decision), text)
    lookup = {block["code"].strip(): index for index, block in enumerate(blocks)}
    def replace_diagram(match: re.Match) -> str:
        index = lookup[match.group(1).strip()]
        return "\n\n" + diagram_figure(manifest["diagrams"][index], index + 1) + "\n\n"
    text = re.sub(r"```mermaid\s*\n([\s\S]*?)```", replace_diagram, text)
    for equation in equations:
        markup = '<div class="formula-image">' + formula_mathml(equation["expression"]) + '</div>'
        text = text.replace("$$" + equation["expression"] + "$$", markup)
    def inline_math(match: re.Match) -> str:
        expression = re.sub(r"\\mathrm\{([^}]+)\}", r"\1", match.group(1))
        expression = re.sub(r"_\{([^}]+)\}", r"<sub>\1</sub>", expression)
        return '<span class="inline-math">' + expression + "</span>"
    text = re.sub(r"\$([A-Za-z][^$\n]*?)\$", inline_math, text)
    rendered = markdown.markdown(text, extensions=["tables", "fenced_code"])
    soup = BeautifulSoup(rendered, "html.parser")
    wrap_research_sections(soup)
    platform_comparison(soup)
    fold_platform_evidence(soup)
    for table in list(soup.find_all("table")):
        if "score-table" in table.get("class", []):
            continue
        attributes = {"class": "table-wrap"}
        if "platform-matrix" in table.get("class", []):
            attributes.update({"tabindex": "0", "role": "region", "aria-label": table["aria-label"] + "，可横向滚动"})
        table.wrap(soup.new_tag("div", attrs=attributes))
    for link in soup.find_all("a", href=True):
        link["href"] = version_url(local_link(link["href"]))
        if link["href"].startswith("http"):
            link["target"] = "_blank"
            link["rel"] = "noopener noreferrer"
    return str(soup)


def viewer_markup() -> str:
    return '''<dialog id="diagram-dialog" class="diagram-dialog" aria-labelledby="diagram-view-title"><div class="dialog-bar"><h2 id="diagram-view-title">关系图</h2><button class="diagram-close" aria-label="关闭关系图">×</button></div><div class="diagram-view-tools"><button data-diagram-zoom="out" aria-label="缩小关系图">−</button><button data-diagram-zoom="reset">适合宽度</button><button data-diagram-zoom="in" aria-label="放大关系图">＋</button><span id="diagram-zoom-label">100%</span><a id="diagram-original" target="_blank" rel="noopener noreferrer">打开 SVG ↗</a></div><div class="diagram-view-scroll"><img id="diagram-view-image" alt="放大的关系图"></div></dialog>'''


def standalone(body: str, title: str, decision: dict) -> str:
    soup = BeautifulSoup(body, "html.parser")
    for heading in soup.find_all(re.compile("^h[1-5]$")):
        heading.name = "h" + str(min(int(heading.name[1]) + 1, 6))
    page = BeautifulSoup(f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · 车载智能化研究</title><link rel="stylesheet" href="{version_url('style.css')}"><link rel="stylesheet" href="{version_url('report.css')}"><script src="{version_url('diagrams.js')}" defer></script></head><body><header class="topbar"><a class="brand" href="{version_url('index.html')}"><span class="brand-symbol"></span><b>DreamSoul</b><span>RESEARCH</span></a><a href="{version_url('index.html')}">返回研究主页 ↗</a></header><main class="research-content"><p class="eyebrow">IN-VEHICLE PRODUCTS / RESEARCH</p><h1>{title}</h1>{soup}</main>{viewer_markup()}</body></html>''', "html.parser")
    attach_decisions(page, decision)
    return str(page)


def build(args: argparse.Namespace) -> None:
    CONTENT.mkdir(exist_ok=True)
    for source, name in [(args.source, "research.md"), (args.outline, "outline.md"), (args.decision, "decision.json")]:
        if source:
            target = CONTENT / name
            if Path(source).resolve() != target.resolve():
                shutil.copy2(source, target)
    text = (CONTENT / "research.md").read_text(encoding="utf-8")
    decision = json.loads((CONTENT / "decision.json").read_text(encoding="utf-8"))
    validate_decision(decision)
    (DIST / "data/decision.json").write_text(json.dumps(decision, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    intro, chapters = chapters_from(text)
    blocks = source_blocks(text)
    manifest = prepare_diagrams(blocks)
    equations = formula_images(text)
    if args.prepare:
        print(json.dumps({"prepared": len(blocks), "formulas": len(equations)}))
        return
    for block, item in zip(blocks, manifest["diagrams"]):
        if item.get("renderedSourceHash") != item["sourceHash"]:
            raise ValueError("Render current Mermaid source first: " + item["id"])
        for suffix in ["svg", "png", "mmd"]:
            if not (DIST / "diagrams" / (item["id"] + "." + suffix)).exists():
                raise FileNotFoundError(item["id"] + "." + suffix)
    template = BeautifulSoup((CONTENT / "index.template.html").read_text(encoding="utf-8"), "html.parser")
    for number, identity in CHAPTER_IDS.items():
        section = template.find("section", id=identity)
        if number == "七":
            # Existing source metadata and methods remain visible after the report's reference table.
            section.find("div", class_="report-body").clear()
        content = re.sub(r"^# [^\n]+\n", "", chapters[number], count=1)
        body = BeautifulSoup(render_markdown(content, blocks, manifest, equations, decision), "html.parser")
        for heading in body.find_all(re.compile("^h[2-5]$")):
            heading.name = "h" + str(min(int(heading.name[1]) + 1, 6))
        target = section.find("div", class_="report-body")
        target.clear()
        target.append(body)
    for tag in template.find_all(["a", "link", "script", "img", "source"]):
        for attr in ["href", "src", "srcset"]:
            if tag.get(attr):
                tag[attr] = version_url(tag[attr])
    if not template.find("script", src=re.compile("^diagrams.js")):
        template.head.append(template.new_tag("script", src=version_url("diagrams.js"), defer=True))
    if not template.find("link", href=re.compile("^report.css")):
        template.head.append(template.new_tag("link", rel="stylesheet", href=version_url("report.css")))
    if not template.find(id="diagram-dialog"):
        template.body.append(BeautifulSoup(viewer_markup(), "html.parser"))
    attach_decisions(template, decision)
    (DIST / "index.html").write_text(str(template), encoding="utf-8")
    full = render_markdown(intro, blocks, manifest, equations, decision)
    for number in CHAPTER_IDS:
        full += render_markdown(chapters[number], blocks, manifest, equations, decision)
    (DIST / "research.html").write_text(standalone(full, "车载智能化 产品与阶段路线", decision), encoding="utf-8")
    outline = (CONTENT / "outline.md").read_text(encoding="utf-8")
    (DIST / "outline.html").write_text(standalone(render_markdown(outline, blocks, manifest, equations, decision), "车载智能化 调研大纲", decision), encoding="utf-8")
    # Keep the dedicated reference page aligned with the new report evidence.
    references_path = DIST / "references.html"
    references = BeautifulSoup(references_path.read_text(encoding="utf-8"), "html.parser")
    update = BeautifulSoup(full, "html.parser").find(id="integration-references")
    previous = references.find(id="integration-references")
    if update is not None:
        if previous is not None:
            previous.replace_with(update)
        else:
            references.main.find("p", class_=None).insert_after(update)
        for tag in references.find_all(["a", "link", "script"]):
            for attribute in ["href", "src"]:
                if tag.get(attribute):
                    tag[attribute] = version_url(tag[attribute])
        references_path.write_text(str(references), encoding="utf-8")
    # The data shape did not change. Version the request with the page assets.
    app = DIST / "app.js"
    script = app.read_text(encoding="utf-8")
    script = re.sub(r'fetch\("data/products\.json(?:\?v=[^"]*)?"\)', f'fetch("data/products.json?v={VERSION}")', script)
    app.write_text(script, encoding="utf-8")
    coverage = {}
    for number, identity in CHAPTER_IDS.items():
        section = template.find("section", id=identity)
        coverage[identity] = {"textCharacters": len(section.get_text(" ", strip=True)), "diagrams": len(section.find_all("figure", class_="research-diagram")), "tables": len(section.find_all("table"))}
    (CONTENT / "coverage.json").write_text(json.dumps(coverage, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"renderedMermaid": len(blocks), "coverage": coverage}, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source")
    parser.add_argument("--outline")
    parser.add_argument("--decision")
    parser.add_argument("--prepare", action="store_true")
    build(parser.parse_args())
