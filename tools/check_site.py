"""Check source-to-figure integrity and the static files that Pages will serve."""
from pathlib import Path
import hashlib
import json
import re
import struct
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
from decision_content import validate_decision, weighted_score, market_estimates

site = Path(__file__).resolve().parent.parent
dist = site / "dist"
source = (site / "content/research.md").read_text(encoding="utf-8")
decision = json.loads((site / "content/decision.json").read_text(encoding="utf-8"))
validate_decision(decision)
assert decision == json.loads((dist / "data/decision.json").read_text(encoding="utf-8"))
platforms_by_id = {item["id"]: item for item in decision["score"]["platforms"]}
assert set(platforms_by_id) == {"carplay", "android-auto", "aaos", "gas", "siri", "gemini", "atoto-s84g209p"}
assert weighted_score(platforms_by_id["siri"]["voice"]["scores"], [30, 30, 10, 20, 10]) == 88
assert weighted_score(platforms_by_id["gemini"]["voice"]["scores"], [30, 30, 10, 20, 10]) == 70
assert weighted_score(platforms_by_id["carplay"]["panel"]["scores"], [20, 20, 25, 20, 15]) == 74
assert weighted_score(platforms_by_id["gas"]["voice"]["scores"], [30, 30, 10, 20, 10]) is None
base, gap, sam, annual = market_estimates(decision["market"], {"gap": 10, "compatible": 50, "purchase": 1})
assert abs(annual - 112127.725374) < 0.001
assert market_estimates(decision["market"], {"gap": 0, "compatible": 50, "purchase": 1})[-1] == 0
blocks = [match.group(1).strip() + "\n" for match in re.finditer(r"```mermaid\s*\n([\s\S]*?)```", source)]
manifest = json.loads((dist / "diagrams/manifest.json").read_text(encoding="utf-8"))
assert len(blocks) == len(manifest["diagrams"]) == 13
assert len({hashlib.sha256(code.encode()).hexdigest() for code in blocks}) == 13
for code, item in zip(blocks, manifest["diagrams"]):
    digest = hashlib.sha256(code.encode()).hexdigest()
    assert digest == item["sourceHash"] == item["renderedSourceHash"], item["id"]
    folder = dist / "diagrams"
    assert (folder / (item["id"] + ".mmd")).read_text(encoding="utf-8") == code
    svg = ET.parse(folder / (item["id"] + ".svg")).getroot()
    assert svg.tag.endswith("svg") and len(svg.findall(".//{http://www.w3.org/2000/svg}text")) > 0
    assert "Syntax error" not in "".join(svg.itertext())
    payload = (folder / (item["id"] + ".png")).read_bytes()
    assert payload[:8] == b"\x89PNG\r\n\x1a\n"
    width, height = struct.unpack(">II", payload[16:24])
    assert width >= item["width"] and height >= item["height"]

for name in ["index.html", "research.html"]:
    soup = BeautifulSoup((dist / name).read_text(encoding="utf-8"), "html.parser")
    figures = soup.select("figure.research-diagram")
    assert len(figures) == 13, name
    for item in manifest["diagrams"]:
        figure = soup.find("figure", id=item["id"])
        assert figure and figure.find("source", type="image/svg+xml")
        assert int(figure.img["width"]) == item["width"]
        assert int(figure.img["height"]) == item["height"]
        assert figure.find("button", attrs={"data-diagram-src": True})
        assert len(figure.find_all("a")) == 3
    assert soup.find("math"), name
    focus = soup.find(id="carplay-focus")
    assert focus and len(focus.select(".cp-route")) == 3, name
    assert len(focus.select("figure.research-diagram")) == 3, name
    assert len(soup.select("#hardware-access table tbody > tr")) == 5, name
    assert len(soup.select("#lumi-reference figure.research-diagram")) == 1, name
    assert len(focus.select("details.cp-detail")) == 2, name
    assert "iOS26.4" in focus.get_text() and "通用对话类别未列" in focus.get_text()
    assert "新增软件" in focus.get_text() and "已有CarPlay" in focus.get_text()
    for link in focus.select('a[href^="#"]'):
        assert soup.find(id=link["href"][1:]), link["href"]
    assert soup.select_one("#platform-scores .cp-scope-note a")["href"] == "#carplay-focus"
    assert soup.find(id="platform-scores") and soup.find(id="market-size"), name
    assert soup.find(id="platform-evidence").name == "details" and not soup.find(id="platform-evidence").has_attr("open")
    assert json.loads(soup.find(id="decision-data").string) == decision
    assert len(soup.select("#score-rows > tr")) == 7
    for row in soup.select("#score-rows > tr"):
        assert all(len(cell.get_text(strip=True)) <= 9 for cell in row.select("td")), row.get_text()
        item = platforms_by_id[row.find("button")["data-score-platform"]]
        company = row.select_one(".score-company a")
        assert company.get_text() == item["company"] and company["href"] == item["companyUrl"]
    assert not re.search(r"自有\s*(?:伴随\s*)?App|自有手机|自有语音|companion-app|phone-assistant|aftermarket-android", str(soup), re.I), name
    assert soup.select_one("#market-annual-result").get_text() == "11.2万台/年"
    assert soup.select_one("#channel-result").get_text() == "渠道真实参数待填"
    platform_tables = soup.select("table.platform-matrix")
    assert len(platform_tables) == 2, name
    cards = soup.select("article.platform-card")
    assert len(cards) == 7 and len(soup.select("article.platform-service")) == 1, name
    assert all(len(table.select("tbody > tr")) == 7 for table in platform_tables)
    for card, usage, access in zip(cards, platform_tables[0].select("tbody > tr"), platform_tables[1].select("tbody > tr")):
        usage_cells, access_cells = usage.find_all("td"), access.find_all("td")
        title = card.find(["h4", "h5"])
        assert title.get_text(strip=True) == usage_cells[0].find("a").get_text(strip=True)
        card_text = card.get_text(" ", strip=True)
        for cell in usage_cells[1:] + access_cells[1:]:
            assert cell.get_text(" ", strip=True) in card_text, title.get_text()
        assert card.find("details").find("summary")
    for link in soup.select(".platform-jumps a"):
        assert soup.find(id=link["href"][1:]), link["href"]
    assert "产品扩展分析示意：语音助手与智能面板可以积累" not in soup.get_text()
homepage = BeautifulSoup((dist / "index.html").read_text(encoding="utf-8"), "html.parser")
assert len(homepage.select("#platforms figure.research-diagram")) == 7
assert len(homepage.select("#starter figure.research-diagram")) == 2
assert len(homepage.select("#platforms .report-body .table-wrap")) == 8
assert all(homepage.select_one("#" + identity + " .report-body") for identity in ["roadmap", "platforms", "products", "starter", "business", "next", "sources"])
assert "手机麦克风" in homepage.select_one("#platforms").get_text()
assert "P" in homepage.find("math").get_text()

checked_links = 0
for path in dist.glob("*.html"):
    text = path.read_text(encoding="utf-8")
    assert "\ufffd" not in text
    soup = BeautifulSoup(text, "html.parser")
    for tag in soup.find_all(["a", "link", "script", "img", "source"]):
        url = tag.get("href") or tag.get("src") or tag.get("srcset")
        if not url:
            continue
        parts = urlsplit(url)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        target = dist / unquote(parts.path)
        assert target.exists(), (path.name, parts.path)
        checked_links += 1
    assert not re.search(r"github_pat_|ghp_[A-Za-z0-9]|Bearer [A-Za-z0-9]|[CD]:\\|THg8dKsQ|diaoenmao@gmail", text)
data = json.loads((dist / "data/products.json").read_text(encoding="utf-8"))
assert len(data["products"]) == 24
assert sum(p["phase"] in ["voice", "panel"] for p in data["products"]) == 17
assert len({item["id"] for item in data["products"]}) == len(data["products"])
assert BeautifulSoup((dist / "references.html").read_text(encoding="utf-8"), "html.parser").find(id="integration-references")
canonical_products = site.parent / "车载智能化 产品样本.json"
if canonical_products.exists():
    normalized = json.loads(json.dumps(data))
    for product in normalized["products"]:
        if product.get("image"):
            product["image"].pop("local", None)
    assert normalized == json.loads(canonical_products.read_text(encoding="utf-8"))
canonical = site.parent / "车载智能化 通用调研.md"
if canonical.exists():
    assert canonical.read_text(encoding="utf-8") == source
canonical_decision = site.parent / "车载智能化 评分与市场.json"
if canonical_decision.exists():
    assert decision == json.loads(canonical_decision.read_text(encoding="utf-8"))
print(json.dumps({"mermaidSources": 13, "carplayFocusRoutes": 3, "carplayFocusDiagrams": 3, "platformRatings": 6, "serviceLayersUnrated": 1, "marketAnnualExample": round(annual), "localLinks": checked_links, "sourceHashesMatch": True}))
