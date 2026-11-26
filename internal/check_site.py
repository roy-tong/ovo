from html.parser import HTMLParser
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
FILES = ["index.html", "en.html", "cases.html", "en-cases.html", "journal.html", "en-journal.html", "start.html", "en-start.html"]
REQUIRED = {
    "index.html": ["data-product-target=\"askovo\"", "data-product-target=\"growovo\"", "data-product-target=\"verovo\"", "journal.html", "start.html",
                   "href=\"https://roy-tong.github.io/Askovo/first-look.html\"",
                   "href=\"https://roy-tong.github.io/Growovo/examples/controlled-run.html\"",
                   "href=\"https://roy-tong.github.io/Verovo/first-look.html\""],
    "en.html": ["href=\"https://roy-tong.github.io/Askovo/en/first-look.html\"",
                "href=\"https://roy-tong.github.io/Growovo/examples/controlled-run.en.html\"",
                "href=\"https://roy-tong.github.io/Verovo/first-look.html\""],
    "cases.html": ["data-filter-group=\"cases\"", "109,429", "73 → 0", "110+ / 65+"],
    "journal.html": ["data-filter-group=\"journal\"", "01-askovo-a-research-database-needs-transactions", "02-growovo-exactly-once-is-the-wrong-goal", "03-verovo-deterministic-replay-with-unknowns", "ai-spend-optimization"],
    "start.html": ["assets/bp/ovo-agent-native-bp-20261126.pdf", "assets/bp/ovo-agent-native-bp-20261126.pptx", "2.25.1rc1", "0.23.1rc2", "0.20.1rc1"],
    "en-start.html": ["assets/bp/ovo-agent-native-bp-20261126.pdf", "assets/bp/ovo-agent-native-bp-20261126.pptx", "2.25.1rc1", "0.23.1rc2", "0.20.1rc1"],
}


class Audit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.images = []
        self.buttons = []
        self.main = 0
        self.h1 = 0
        self.lang = ""

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get("id"):
            self.ids.append(values["id"])
        if tag == "a" and values.get("href"):
            self.links.append(values["href"])
        if tag == "img":
            self.images.append(values)
        if tag == "button":
            self.buttons.append(values)
        if tag == "main":
            self.main += 1
        if tag == "h1":
            self.h1 += 1
        if tag == "html":
            self.lang = values.get("lang", "")


def local_target(source, value):
    value = value.split("#", 1)[0].split("?", 1)[0]
    if not value or value.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
        return None
    return source.parent / value.lstrip("/")


errors = []
for name in FILES:
    path = ROOT / name
    text = path.read_text(encoding="utf-8")
    parser = Audit()
    parser.feed(text)
    if not parser.lang:
        errors.append(f"{name}: missing html lang")
    if parser.main != 1:
        errors.append(f"{name}: expected one main")
    if parser.h1 < 1 and name != "index.html":
        errors.append(f"{name}: missing page heading")
    duplicates = sorted({value for value in parser.ids if parser.ids.count(value) > 1})
    if duplicates:
        errors.append(f"{name}: duplicate ids {duplicates}")
    for image in parser.images:
        if "alt" not in image:
            errors.append(f"{name}: image without alt {image.get('src')}")
    for button in parser.buttons:
        if button.get("type") != "button":
            errors.append(f"{name}: button without explicit type")
    for value in parser.links:
        target = local_target(path, value)
        if target is not None and not target.exists():
            errors.append(f"{name}: broken local link {value} -> {target}")
    for required in REQUIRED.get(name, []):
        if required not in text:
            errors.append(f"{name}: missing {required}")

for name in ("en.html", "en-cases.html", "en-journal.html", "en-start.html"):
    text = (ROOT / name).read_text(encoding="utf-8")
    if 'hreflang="zh-CN"' not in text:
        errors.append(f"{name}: missing Chinese alternate")

sitemap = ET.parse(ROOT / "sitemap.xml")
for node in sitemap.getroot():
    url = node.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc").text
    relative = url.split("/ovo/", 1)[1]
    if relative and not (ROOT / relative).is_file():
        errors.append(f"sitemap: missing local page {relative}")

if errors:
    raise SystemExit("\n".join(errors))
print("unified site structure, accessibility basics and local links: PASS")
