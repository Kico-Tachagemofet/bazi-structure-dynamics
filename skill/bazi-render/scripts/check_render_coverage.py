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
TOPIC_MARKER = re.compile(r"<!--\s*topic_id:\s*([a-z0-9-]+)\s*-->")
BASELINE_TOPICS = (
    "family-home",
    "education-learning",
    "wealth-resource",
    "career-work",
)


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def marked_sections(render_text: str, marker: re.Pattern[str]) -> dict[str, list[str]]:
    matches = list(marker.finditer(render_text))
    result: dict[str, list[str]] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(render_text)
        result.setdefault(match.group(1), []).append(render_text[match.start() : end])
    return result


def scope_values(scope_text: str) -> dict[str, object]:
    """Read the small, deliberately constrained report-scope YAML subset.

    This avoids adding a YAML dependency to the mechanical checker. The schema
    keeps topic lists as top-level scalar lists.
    """
    values: dict[str, object] = {
        "mandatory_sections": [],
        "selected_optional_sections": [],
    }
    active_list: str | None = None
    for raw_line in scope_text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if raw_line == raw_line.lstrip():
            active_list = None
            key, separator, raw_value = raw_line.partition(":")
            if not separator:
                continue
            key = key.strip()
            raw_value = raw_value.strip().strip('"\'')
            if key in ("mandatory_sections", "selected_optional_sections"):
                active_list = key
                if raw_value == "[]":
                    values[key] = []
                    active_list = None
            elif key in ("delivery_mode", "family_calibration_state"):
                values[key] = raw_value
            continue
        stripped = raw_line.strip()
        if active_list and stripped.startswith("- "):
            item = stripped[2:].strip().strip('"\'')
            cast = values[active_list]
            assert isinstance(cast, list)
            cast.append(item)
    return values


def check(
    findings_text: str,
    render_text: str,
    mode: str,
    expected: list[str],
    scope_text: str | None = None,
) -> dict:
    finding_ids = FINDING_HEADING.findall(findings_text)
    rendered = marked_sections(render_text, RENDER_MARKER)
    rendered_topics = marked_sections(render_text, TOPIC_MARKER)
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

    required_topics: list[str] = []
    scope: dict[str, object] = {}
    if scope_text is not None:
        scope = scope_values(scope_text)
        mandatory = scope.get("mandatory_sections", [])
        selected = scope.get("selected_optional_sections", [])
        assert isinstance(mandatory, list)
        assert isinstance(selected, list)
        required_topics = [*mandatory, *selected]

        if scope.get("delivery_mode") == "full-reading":
            missing_baseline_contract = [item for item in BASELINE_TOPICS if item not in mandatory]
            if missing_baseline_contract:
                blockers.append(
                    "Full-reading scope omits mandatory baseline topics: "
                    f"{missing_baseline_contract}"
                )
            calibration_state = scope.get("family_calibration_state")
            if calibration_state not in ("completed", "declined", "uncalibrated", "contaminated"):
                blockers.append(
                    "Full-reading family calibration gate is not closed: "
                    f"{calibration_state or 'missing'}"
                )

        missing_topics = [item for item in required_topics if item not in rendered_topics]
        if missing_topics:
            blockers.append(f"Required report topics are not rendered: {missing_topics}")
        duplicate_topics = [item for item, chunks in rendered_topics.items() if len(chunks) != 1]
        if duplicate_topics:
            blockers.append(f"Topic marker is not one-to-one: {duplicate_topics}")
        unknown_topics = [item for item in rendered_topics if item not in required_topics]
        if mode == "report" and unknown_topics:
            blockers.append(f"Render contains topics outside report scope: {unknown_topics}")

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
        "rendered_topics": list(rendered_topics),
        "required_topics": required_topics,
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
    parser.add_argument("--scope", help="report-scope.yaml for topic and calibration gates")
    args = parser.parse_args()
    scope_text = read(args.scope) if args.scope else None
    result = check(read(args.findings), read(args.render), args.mode, args.expect, scope_text)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["verdict"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
