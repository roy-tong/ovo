#!/usr/bin/env python3
"""Synchronize marked install blocks, copy commands and the agent manifest."""
from __future__ import annotations

import argparse
import html as html_module
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_block(text, tag, replacement):
    pattern = re.compile(
        r"<!--(?:OVO|VERSION):" + re.escape(tag) + r"-->.*?<!--/(?:OVO|VERSION):" + re.escape(tag) + r"-->",
        re.DOTALL,
    )
    style = "OVO" if ("<!--OVO:%s-->" % tag) in text else "VERSION"
    opening = "<!--%s:%s-->" % (style, tag)
    closing = "<!--/%s:%s-->" % (style, tag)
    updated, count = pattern.subn(opening + replacement + closing, text)
    if count != 1:
        raise ValueError("expected one marked block for %s, found %d" % (tag, count))
    return updated


def install_block(product, channel, html=False):
    version = product[channel]
    command = "pipx install %s==%s\n%s" % (product["package"], version, product["demo"])
    return "<pre><code>%s</code></pre>" % command if html else command


def render(text, products, html=False):
    """Return the text with every install block and copy command brought up to date."""
    for name, product in products.items():
        for channel in ("stable", "preview"):
            tag = "%s-%s" % (name, channel)
            replacement = install_block(product, channel, html=html)
            if ("<!--OVO:%s-->" % tag) in text or ("<!--VERSION:%s-->" % tag) in text:
                text = replace_block(text, tag, replacement)
            elif replacement in text:
                style = "VERSION" if html else "OVO"
                text = text.replace(
                    replacement,
                    "<!--%s:%s-->%s<!--/%s:%s-->" % (style, tag, replacement, style, tag),
                    1,
                )
            if html:
                command = "pipx install %s==%s\n%s" % (
                    product["package"], product[channel], product["demo"])
                escaped = html_module.escape(command, quote=True).replace("\n", "&#10;")
                pattern = re.compile(
                    r'(<!--/VERSION:' + re.escape(tag) +
                    r'-->\s*<button\b[^>]*\bdata-copy=")pipx install ' +
                    re.escape(product["package"]) + r'==[^"]*(")')
                text = pattern.sub(lambda match: match.group(1) + escaped + match.group(2), text)
    return text


def sync_file(path, products, html=False):
    """Rewrite one file in place. Returns True when it was out of date."""
    original = path.read_text(encoding="utf-8")
    updated = render(original, products, html=html)
    if updated == original:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def render_manifest(text, products):
    for name, product in products.items():
        record = json.loads(text)["products"][name]
        previous = json.dumps(record["installation"], ensure_ascii=False)
        installation = {
            channel: "pipx install %s==%s" % (product["package"], product[channel])
            for channel in ("stable", "preview")
        }
        replacement = json.dumps(installation, ensure_ascii=False)
        text, count = re.subn(
            r'"installation": ' + re.escape(previous),
            '"installation": ' + replacement.replace("\\", "\\\\"), text, count=1)
        if count != 1:
            raise ValueError("expected one installation manifest for %s" % name)
    return text


def sync_manifest(products):
    path = ROOT / "agent-tools.json"
    original = path.read_text(encoding="utf-8")
    updated = render_manifest(original, products)
    if updated == original:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def targets(args):
    """Every file that carries an install block, as (path, product-or-None).

    The three product subpages are listed here on purpose: they carry the same
    markers as the landing pages, and leaving them out is how the site ended up
    advertising a preview version two RCs behind versions.json.
    """
    files = [(ROOT / "start.html", None), (ROOT / "en-start.html", None)]
    for name in ("askovo", "growovo", "verovo"):
        for page in ("index.html", "en.html"):
            files.append((ROOT / name / page, name))
    for relative in ("llms.txt", "README.md"):
        files.append((ROOT / relative, None))
    for name, directory in (
        ("askovo", args.askovo), ("growovo", args.growovo), ("verovo", args.verovo),
    ):
        if directory is None:
            continue
        for filename in ("README.md", "README.zh-CN.md", "README.en.md", "llms.txt"):
            path = directory / filename
            if path.is_file():
                files.append((path, name))
    return files


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--askovo", type=Path)
    parser.add_argument("--growovo", type=Path)
    parser.add_argument("--verovo", type=Path)
    parser.add_argument("--check", action="store_true",
                        help="只比对不写入；与 versions.json 不一致就退 1")
    args = parser.parse_args()
    document = json.loads((ROOT / "versions.json").read_text(encoding="utf-8"))
    if document.get("schema") != "ovo.release-channels/1":
        raise ValueError("unsupported release channel schema")
    products = document["products"]
    stale = []
    for path, product in targets(args):
        if not path.is_file():
            continue
        scoped = products if product is None else {product: products[product]}
        original = path.read_text(encoding="utf-8")
        if render(original, scoped, html=path.suffix == ".html") != original:
            stale.append(path)
            if not args.check:
                sync_file(path, scoped, html=path.suffix == ".html")
    manifest = ROOT / "agent-tools.json"
    if render_manifest(manifest.read_text(encoding="utf-8"), products) != manifest.read_text(encoding="utf-8"):
        stale.append(manifest)
        if not args.check:
            sync_manifest(products)
    if args.check:
        if stale:
            for path in stale:
                print("out of sync with versions.json: %s" % path.relative_to(ROOT))
            print("运行 python3 assets/sync_versions.py 后重新提交")
            return 1
        print("所有安装块与 %s 一致（%d 个产品）" % (
            (ROOT / "versions.json").relative_to(ROOT), len(products)))
        return 0
    for path in stale:
        print("updated %s" % path.relative_to(ROOT))
    print("synchronized %d products from %s（改动 %d 个文件）" % (
        len(products), (ROOT / "versions.json").relative_to(ROOT), len(stale)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
