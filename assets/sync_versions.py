#!/usr/bin/env python3
"""Synchronize marked install blocks from versions.json; never edits other content."""
from __future__ import annotations

import argparse
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
