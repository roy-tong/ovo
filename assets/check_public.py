"""Check the complete Pages source tree, including untracked assets.

正本。`python3 assets/check_public.py <站点目录>`，失败退 1。
检查三件事：公开文件清单没有多也没有少、页内链接都指向站内已存在的文件、
锚点都落在目标页的 id 上。
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import posixpath
import sys

root = Path(sys.argv[1]).resolve()
products = ("askovo", "growovo", "verovo")
pages = (
    {"index.html", "en.html"}
    | {p + n + ".html" for p in ("", "en-") for n in ("cases", "journal", "start")}
    | {product + "/" + page for product in products for page in ("index.html", "en.html")}
)
allowed = pages | {
    ".nojekyll", "LICENSE", "README.md", "llms.txt", "robots.txt", "sitemap.xml",
    # 发版口径与 Agent 清单：站点自己发布，必须在清单里
    "versions.json", "agent-tools.json", "assets/sync_versions.py", "assets/check_public.py",
    "assets/styles.css", "assets/app.js", "assets/social-preview.png",
    "assets/askovo.webp", "assets/growovo.webp", "assets/verovo.webp",
    "assets/fonts/Geist-Variable.woff2", "assets/fonts/GeistMono-Variable.woff2",
}
present = {p.relative_to(root).as_posix() for p in root.rglob("*")
           if not {".git", ".github"} & set(p.relative_to(root).parts)
           and (p.is_file() or p.is_symlink())}
if present != allowed:
    raise SystemExit("Unexpected: %s, missing: %s" % (sorted(present - allowed), sorted(allowed - present)))


def local_target(page, raw):
    """Map an href/src onto a repo-relative file path, or None when it is external."""
    ref = urlsplit(raw)
    if ref.scheme or ref.netloc:
        return None, None
    path = ref.path
    if path.startswith("/"):
        # Pages serves this repo under /ovo/; absolute links carry that prefix.
        rest = path[len("/ovo/"):] if path.startswith("/ovo/") else path[1:]
        base = ""
    else:
        rest = path
        base = posixpath.dirname(page)
    if rest in ("", "."):
        return page, ref.fragment
    if rest.endswith("/"):
        rest += "index.html"
    return posixpath.normpath(posixpath.join(base, rest) if base else rest), ref.fragment


class Page(HTMLParser):
    def __init__(self, name):
        super().__init__()
        self.ids = set()
        self.refs = []
        self.feed((root / name).read_text())
    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if "id" in values:
            assert values["id"] not in self.ids, values["id"]
            self.ids.add(values["id"])
        for key in ("href", "src"):
            if key in values:
                self.refs.append(values[key])

docs = {p: Page(p) for p in pages}
for p, doc in docs.items():
    for raw in doc.refs:
        target, fragment = local_target(p, raw)
        if target is None:
            continue
        assert target in allowed, (p, raw, target)
        if fragment:
            assert target in docs, (p, raw, target)
            assert fragment in docs[target].ids, (p, raw, fragment)
for name in present:
    assert not (root / name).is_symlink(), name
print("Verified %d pages, local links and fragments, %d public files." % (len(pages), len(present)))
