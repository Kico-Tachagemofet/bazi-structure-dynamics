#!/usr/bin/env python3
"""Extract DOCX paragraphs and tables to Markdown without summarizing them."""

from __future__ import annotations

import argparse
from pathlib import Path

from docx import Document
from docx.document import Document as DocumentObject
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P


def blocks(parent: DocumentObject):
    for child in parent.element.body.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)


def esc(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", "<br>")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_docx", type=Path)
    parser.add_argument("output_md", type=Path)
    parser.add_argument("--title", required=True)
    args = parser.parse_args()

    doc = Document(args.input_docx)
    lines = [
        f"# {args.title}",
        "",
        f"> 来源文件：`{args.input_docx}`",
        "> 本文件按 Word 正文顺序机械抽取；不删节、不摘要。原段落序号用于回查。",
        "",
    ]
    paragraph_no = 0
    table_no = 0
    for block in blocks(doc):
        if isinstance(block, Paragraph):
            paragraph_no += 1
            text = block.text.rstrip()
            style = block.style.name if block.style is not None else ""
            lines.append(f"<!-- paragraph {paragraph_no}; style: {style} -->")
            if style.lower().startswith("heading"):
                try:
                    level = min(max(int(style.split()[-1]), 1), 6)
                except ValueError:
                    level = 2
                lines.extend([f"{'#' * level} {text}", ""])
            else:
                lines.extend([text, ""])
        else:
            table_no += 1
            lines.extend([f"<!-- table {table_no} -->", ""])
            rows = [[esc(cell.text) for cell in row.cells] for row in block.rows]
            if rows:
                width = max(len(row) for row in rows)
                rows = [row + [""] * (width - len(row)) for row in rows]
                lines.append("| " + " | ".join(rows[0]) + " |")
                lines.append("| " + " | ".join(["---"] * width) + " |")
                for row in rows[1:]:
                    lines.append("| " + " | ".join(row) + " |")
            lines.append("")

    args.output_md.parent.mkdir(parents=True, exist_ok=True)
    args.output_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
