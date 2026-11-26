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


def sync_file(path, products, html=False):
    text = path.read_text(encoding="utf-8")
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
    path.write_text(text, encoding="utf-8")


def sync_manifest(products):
    path = ROOT / "agent-tools.json"
    text = path.read_text(encoding="utf-8")
    document = json.loads(text)
    for name, product in products.items():
        record = document["products"][name]
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
        record["installation"] = installation
    path.write_text(text, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--askovo", type=Path)
    parser.add_argument("--growovo", type=Path)
    parser.add_argument("--verovo", type=Path)
    args = parser.parse_args()
    document = json.loads((ROOT / "versions.json").read_text(encoding="utf-8"))
    if document.get("schema") != "ovo.release-channels/1":
        raise ValueError("unsupported release channel schema")
    products = document["products"]
    for relative in ("start.html", "en-start.html"):
        sync_file(ROOT / relative, products, html=True)
    sync_file(ROOT / "llms.txt", products)
    sync_file(ROOT / "README.md", products)
    sync_manifest(products)
    for product, directory in (
        ("askovo", args.askovo), ("growovo", args.growovo), ("verovo", args.verovo),
    ):
        if directory is None:
            continue
        for name in ("README.md", "README.zh-CN.md", "README.en.md", "llms.txt"):
            path = directory / name
            if path.is_file():
                sync_file(path, {product: products[product]})
    print("synchronized %d products from %s" % (len(products), ROOT / "versions.json"))


if __name__ == "__main__":
    main()
