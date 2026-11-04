"""Check source-to-figure integrity and the static files that Pages will serve."""
from pathlib import Path
import hashlib
import json
import re
import struct
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup

site = Path(__file__).resolve().parent.parent
dist = site / "dist"
source = (site / "content/research.md").read_text(encoding="utf-8")
blocks = [match.group(1).strip() + "\n" for match in re.finditer(r"```mermaid\s*\n([\s\S]*?)```", source)]
manifest = json.loads((dist / "diagrams/manifest.json").read_text(encoding="utf-8"))
assert len(blocks) == len(manifest["diagrams"]) == 9
assert len({hashlib.sha256(code.encode()).hexdigest() for code in blocks}) == 9
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
    assert len(figures) == 9, name
    for item in manifest["diagrams"]:
        figure = soup.find("figure", id=item["id"])
        assert figure and figure.find("source", type="image/svg+xml")
        assert int(figure.img["width"]) == item["width"]
        assert int(figure.img["height"]) == item["height"]
        assert figure.find("button", attrs={"data-diagram-src": True})
        assert len(figure.find_all("a")) == 3
    assert soup.find("math"), name
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
assert len(homepage.select("#platforms figure.research-diagram")) == 4
assert len(homepage.select("#starter figure.research-diagram")) == 2
assert len(homepage.select("#platforms .report-body .table-wrap")) == 5
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
assert len(data["products"]) == 23
assert sum(p["phase"] in ["voice", "panel"] for p in data["products"]) == 16
canonical = site.parent / "车载智能化 通用调研.md"
if canonical.exists():
    assert canonical.read_text(encoding="utf-8") == source
print(json.dumps({"mermaidSources": 9, "svg": 9, "png": 9, "platformFigures": 4, "platformMatrices": 2, "platformCards": 7, "localLinks": checked_links, "sourceHashesMatch": True}))
