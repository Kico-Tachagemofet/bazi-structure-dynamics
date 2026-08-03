#!/usr/bin/env python3
"""Import a text source as UTF-8 Markdown without semantic compression."""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_text", type=Path)
    parser.add_argument("output_md", type=Path)
    parser.add_argument("--encoding", default="gb18030")
    parser.add_argument("--title", required=True)
    args = parser.parse_args()

    body = args.input_text.read_text(encoding=args.encoding)
    body = body.replace("\r\n", "\n").replace("\r", "\n")
    prefix = (
        f"# {args.title}\n\n"
        f"> 来源文件：`{args.input_text}`\n"
        "> 本文件只做编码与换行规范化，不删节、不摘要、不合并原文与评注。\n\n"
    )
    args.output_md.parent.mkdir(parents=True, exist_ok=True)
    args.output_md.write_text(prefix + body.rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
