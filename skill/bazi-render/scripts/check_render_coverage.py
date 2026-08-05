#!/usr/bin/env python3
"""Mechanically check Bazi finding-to-render coverage.

Semantic fidelity remains the responsibility of bazi-finding-audit.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


FINDING_HEADING = re.compile(r"^##\s+(F-[A-Z0-9-]+)\b", re.MULTILINE)
RENDER_MARKER = re.compile(r"<!--\s*finding_id:\s*(F-[A-Z0-9-]+)\s*-->")


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def sections(render_text: str) -> dict[str, list[str]]:
    matches = list(RENDER_MARKER.finditer(render_text))
    result: dict[str, list[str]] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(render_text)
        result.setdefault(match.group(1), []).append(render_text[match.start() : end])
    return result


def check(findings_text: str, render_text: str, mode: str, expected: list[str]) -> dict:
    finding_ids = FINDING_HEADING.findall(findings_text)
    rendered = sections(render_text)
    blockers: list[str] = []
    warnings: list[str] = []

    duplicates = [item for item, chunks in rendered.items() if len(chunks) != 1]
    if duplicates:
        blockers.append(f"Render marker is not one-to-one: {duplicates}")

    required = expected or (finding_ids if mode == "report" else list(rendered))
    missing = [item for item in required if item not in rendered]
    if missing:
        blockers.append(f"Required findings are not rendered: {missing}")

    if mode == "report":
        extras = [item for item in rendered if item not in finding_ids]
        if extras:
            blockers.append(f"Render contains unknown finding IDs: {extras}")

    for finding_id in required:
        chunks = rendered.get(finding_id, [])
        if not chunks:
            continue
        chunk = chunks[0]
        for label in ("生活判断：", "条件与代价：", "技术依据："):
            if label not in chunk:
                blockers.append(f"{finding_id} missing required label: {label}")
        if "source gap" in chunk.lower() and "不确定" not in chunk and "缺" not in chunk:
            warnings.append(f"{finding_id} mentions a source gap without reader-facing uncertainty.")

    verdict = "FAIL" if blockers else ("PASS_WITH_WARNINGS" if warnings else "PASS")
    return {
        "verdict": verdict,
        "mode": mode,
        "finding_count": len(finding_ids),
        "rendered_ids": list(rendered),
        "required_ids": required,
        "blockers": blockers,
        "warnings": warnings,
        "boundary": "Mechanical coverage only; run bazi-finding-audit for semantic fidelity.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Bazi render coverage.")
    parser.add_argument("findings")
    parser.add_argument("render")
    parser.add_argument("--mode", choices=("report", "qa"), default="report")
    parser.add_argument("--expect", action="append", default=[])
    args = parser.parse_args()
    result = check(read(args.findings), read(args.render), args.mode, args.expect)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["verdict"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
