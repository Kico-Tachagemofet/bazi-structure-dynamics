#!/usr/bin/env python3
"""Extract an EPUB's readable body into ordered Markdown without summarizing it."""

from __future__ import annotations

import argparse
import posixpath
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

from lxml import html


def ordered_documents(book: zipfile.ZipFile) -> list[str]:
    container = ET.fromstring(book.read("META-INF/container.xml"))
    rootfile = container.find(".//{*}rootfile")
    if rootfile is None:
        raise ValueError("EPUB container.xml has no rootfile")
    opf_name = rootfile.attrib["full-path"]
    opf = ET.fromstring(book.read(opf_name))
    opf_dir = posixpath.dirname(opf_name)
    manifest = {
        item.attrib["id"]: posixpath.normpath(posixpath.join(opf_dir, item.attrib["href"]))
        for item in opf.findall(".//{*}manifest/{*}item")
        if "id" in item.attrib and "href" in item.attrib
    }
    result: list[str] = []
    for itemref in opf.findall(".//{*}spine/{*}itemref"):
        href = manifest.get(itemref.attrib.get("idref", ""))
        if href and href.lower().endswith((".html", ".xhtml", ".htm")):
            result.append(href)
    return result


def clean_text(value: str) -> str:
    value = value.replace("\u3000", " ").replace("\xa0", " ")
    value = re.sub(r"[ \t]+", " ", value)
    return value.strip()


def render_document(raw: bytes, entry_name: str) -> list[str]:
    document = html.fromstring(raw)
    body = document.find("body")
    if body is None:
        return []

    output = [f"<!-- EPUB entry: {entry_name} -->"]
    for node in body.iter():
        tag = node.tag.split("}")[-1].lower() if isinstance(node.tag, str) else ""
        if tag not in {"h1", "h2", "h3", "h4", "p", "li", "blockquote"}:
            continue
        # Do not emit nested paragraph/list text twice.
        if any(
            isinstance(parent.tag, str)
            and parent.tag.split("}")[-1].lower() in {"p", "li", "blockquote"}
            for parent in node.iterancestors()
        ):
            continue
        text = clean_text("".join(node.itertext()))
        if not text:
            continue
        if tag.startswith("h"):
            level = min(int(tag[1]), 6)
            output.extend(["", f"{'#' * level} {text}", ""])
        elif tag == "li":
            output.append(f"- {text}")
        elif tag == "blockquote":
            output.extend([f"> {line}" for line in text.splitlines()])
            output.append("")
        else:
            output.extend([text, ""])
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_epub", type=Path)
    parser.add_argument("output_md", type=Path)
    parser.add_argument("--title", default=None)
    args = parser.parse_args()

    with zipfile.ZipFile(args.input_epub) as book:
        documents = ordered_documents(book)
        lines = [
            f"# {args.title or args.input_epub.stem}",
            "",
            f"> 来源文件：`{args.input_epub}`",
            "> 本文件为机械全文抽取，不是摘要；章节次序按 EPUB spine 保留。",
            "",
        ]
        for name in documents:
            lines.extend(render_document(book.read(name), name))

    args.output_md.parent.mkdir(parents=True, exist_ok=True)
    args.output_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
