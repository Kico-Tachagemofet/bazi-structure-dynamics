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
from typing import Any


FINDING_HEADING = re.compile(r"^##\s+(F-[A-Z0-9-]+)\b", re.MULTILINE)
FINDING_FIELD = re.compile(r"^-\s*finding_id:\s*(F-[A-Z0-9-]+)\s*$", re.MULTILINE)
RENDER_MARKER = re.compile(r"<!--\s*finding_id:\s*(F-[A-Z0-9-]+)\s*-->")
JUDGMENT_ID = re.compile(r"\b(J-F-[A-Z0-9-]+-\d{2})\b")
JUDGMENT_MARKER = re.compile(r"<!--\s*judgment_id:\s*(J-F-[A-Z0-9-]+-\d{2})\s*-->")
TOPIC_MARKER = re.compile(r"<!--\s*topic_id:\s*([a-z0-9-]+)\s*-->")
CORE_MARKER = re.compile(r"<!--\s*core_section_id:\s*([a-z0-9-]+)\s*-->")
TIMING_YEAR_MARKER = re.compile(r"<!--\s*timing_year:\s*(\d{4})\s*-->")
LUCK_PERIOD_MARKER = re.compile(r"<!--\s*luck_period_id:\s*([A-Z0-9-]+)\s*-->")
BASELINE_TOPICS = (
    "family-home",
    "education-learning",
    "wealth-resource",
    "career-work",
)
NATAL_CORE_SECTIONS = (
    "natal-facts-boundaries",
    "natal-system-engine",
    "natal-four-pillars",
    "natal-hidden-manifestation",
    "natal-relation-network",
    "natal-ten-god-functions",
    "natal-pattern-use-agency",
    "natal-synthesis-tensions",
)


def read(path: str | Path) -> str:
    return Path(path).read_text(encoding="utf-8")


def read_canonical_findings(path_value: str | Path) -> tuple[str, list[str]]:
    """Read canonical finding files while excluding ID-only aggregation indexes."""
    path = Path(path_value)
    if path.is_file():
        return read(path), [str(path)]
    if not path.is_dir():
        raise OSError(f"findings path does not exist: {path}")
    files: list[Path] = []
    for candidate in path.rglob("*.md"):
        lowered_parts = {part.lower() for part in candidate.parts}
        if "archive" in lowered_parts:
            continue
        name = candidate.name.lower()
        if name == "topic-findings-all.md":
            continue
        if (
            name.startswith("topic-findings-")
            or "natal-core-findings" in lowered_parts
            or "topic-findings" in lowered_parts
            or "timing-findings" in lowered_parts
        ):
            files.append(candidate)
    files = sorted(set(files))
    if not files:
        raise OSError(f"no canonical finding files found under: {path}")
    return "\n\n".join(read(item) for item in files), [str(item) for item in files]


def marked_sections(render_text: str, marker: re.Pattern[str]) -> dict[str, list[str]]:
    matches = list(marker.finditer(render_text))
    result: dict[str, list[str]] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(render_text)
        result.setdefault(match.group(1), []).append(render_text[match.start() : end])
    return result


def finding_sections(findings_text: str) -> dict[str, list[str]]:
    headings = list(FINDING_HEADING.finditer(findings_text))
    heading_ids = {match.group(1) for match in headings}
    # Canonical findings may be prose-led topic files with ``## F-*`` headings
    # or compact natal-core records whose stable ID is a top-level field.  Keep
    # one boundary per finding without forcing either authoring shape.
    matches = [
        *headings,
        *(match for match in FINDING_FIELD.finditer(findings_text) if match.group(1) not in heading_ids),
    ]
    matches.sort(key=lambda match: match.start())
    result: dict[str, list[str]] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(findings_text)
        result.setdefault(match.group(1), []).append(findings_text[match.start() : end])
    return result


def _scalar(raw: str) -> Any:
    value = raw.strip().strip('"\'')
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if value.lower() in {"null", "none", "~"}:
        return None
    if value.startswith("[") and value.endswith("]"):
        body = value[1:-1].strip()
        return [] if not body else [_scalar(item) for item in body.split(",")]
    if re.fullmatch(r"\d+", value):
        return int(value)
    return value


def scope_values(scope_text: str) -> dict[str, object]:
    """Read the constrained report-scope YAML subset, including object lists."""
    try:
        document = json.loads(scope_text)
    except json.JSONDecodeError:
        document = None
    if isinstance(document, dict):
        values = dict(document)
        values["mandatory_sections"] = list(
            values.get("mandatory_sections", values.get("mandatory_topics", []))
        )
        raw_optional = list(
            values.get("selected_optional_sections", values.get("selected_optional_topics", []))
        )
        values["selected_optional_sections"] = [
            item.get("topic_slug") if isinstance(item, dict) else item
            for item in raw_optional
            if not isinstance(item, dict) or item.get("topic_slug")
        ]
        values["natal_core_sections"] = list(values.get("natal_core_sections", []))
        timing = values.get("timing_scope", {})
        if isinstance(timing, dict):
            values["requested"] = timing.get("requested", False)
            values["annual_years"] = list(timing.get("annual_years", timing.get("years", [])))
            values["luck_periods"] = list(timing.get("luck_periods", []))
        else:
            values["requested"] = False
            values["annual_years"] = []
            values["luck_periods"] = []
        return values

    values: dict[str, object] = {
        "mandatory_sections": [],
        "selected_optional_sections": [],
        "natal_core_sections": [],
        "annual_years": [],
        "luck_periods": [],
    }
    active_top: str | None = None
    active_list: str | None = None
    for raw_line in scope_text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        stripped = raw_line.strip()
        if indent == 0:
            active_top = None
            active_list = None
            key, separator, raw_value = stripped.partition(":")
            if not separator:
                continue
            key = key.strip()
            raw_value = raw_value.strip()
            if key in {"mandatory_sections", "selected_optional_sections", "natal_core_sections"}:
                active_list = key
                parsed = _scalar(raw_value) if raw_value else []
                values[key] = parsed if isinstance(parsed, list) else []
                if raw_value and raw_value != "[]":
                    active_list = None
            elif key == "timing_scope":
                active_top = key
            else:
                values[key] = _scalar(raw_value)
            continue

        if active_list and stripped.startswith("- "):
            item = stripped[2:].strip().strip('"\'')
            cast = values[active_list]
            assert isinstance(cast, list)
            if active_list == "selected_optional_sections" and item.startswith("topic_slug:"):
                cast.append(_scalar(item.partition(":")[2]))
            elif ":" not in item:
                cast.append(_scalar(item))
            continue

        if active_top == "timing_scope":
            key, separator, raw_value = stripped.partition(":")
            if separator and key.strip() in {"requested", "annual_years", "luck_periods"}:
                parsed_key = key.strip()
                values[parsed_key] = _scalar(raw_value)
                active_list = parsed_key if parsed_key in {"annual_years", "luck_periods"} and not raw_value.strip() else None
            elif active_list in {"annual_years", "luck_periods"} and stripped.startswith("- "):
                target = values[active_list]
                assert isinstance(target, list)
                target.append(_scalar(stripped[2:]))
    return values


def _reader_facing_text(chunk: str) -> str:
    """Return prose content while ignoring markers and technical-only scaffolding."""
    clean = re.sub(r"<!--.*?-->", "", chunk, flags=re.DOTALL)
    kept: list[str] = []
    for raw_line in clean.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or re.fullmatch(r"-{3,}", line):
            continue
        if re.match(r"^(?:技术依据|命理依据|audit trail)\s*[:：]", line, flags=re.IGNORECASE):
            continue
        line = re.sub(r"^[>\-*+\d.、)）\s]+", "", line)
        line = re.sub(r"[*_`\[\]()（）]", "", line)
        kept.append(line)
    return re.sub(r"\s+", "", "".join(kept))


def _judgment_body(chunk: str, judgment_id: str) -> str:
    """Return reader-facing prose between one judgment marker and the next."""
    matches = list(JUDGMENT_MARKER.finditer(chunk))
    for index, match in enumerate(matches):
        if match.group(1) != judgment_id:
            continue
        boundary_starts = [
            candidate.start()
            for pattern in (JUDGMENT_MARKER, TOPIC_MARKER, CORE_MARKER, TIMING_YEAR_MARKER)
            for candidate in pattern.finditer(chunk, match.end())
        ]
        end = min(boundary_starts) if boundary_starts else len(chunk)
        return _reader_facing_text(chunk[match.end() : end])
    return ""


def check(
    findings_text: str,
    render_text: str,
    mode: str,
    expected: list[str],
    scope_text: str | None = None,
    receipt_text: str | None = None,
) -> dict[str, object]:
    canonical = finding_sections(findings_text)
    finding_ids = list(canonical)
    rendered = marked_sections(render_text, RENDER_MARKER)
    rendered_topics = marked_sections(render_text, TOPIC_MARKER)
    blockers: list[str] = []
    warnings: list[str] = []

    duplicate_findings = [item for item, chunks in canonical.items() if len(chunks) != 1]
    if duplicate_findings:
        blockers.append(f"Canonical finding IDs are duplicated: {duplicate_findings}")
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

    scope: dict[str, object] = {}
    required_topics: list[str] = []
    detailed = False
    required_core: list[str] = []
    annual_years: list[int] = []
    luck_period_ids: list[str] = []
    if mode == "report" and scope_text is None:
        blockers.append("Formal report coverage requires report-scope.yaml")
    if scope_text is not None:
        scope = scope_values(scope_text)
        mandatory = scope.get("mandatory_sections", [])
        selected = scope.get("selected_optional_sections", [])
        if not isinstance(mandatory, list) or not isinstance(selected, list):
            blockers.append("Scope topic lists are malformed")
            mandatory, selected = [], []
        required_topics = [str(item) for item in [*mandatory, *selected]]
        luck_periods = scope.get("luck_periods", [])
        if scope.get("requested") is True and isinstance(luck_periods, list) and luck_periods:
            if "formative-major-luck" not in required_topics:
                required_topics.append("formative-major-luck")
        detailed = scope.get("delivery_mode") == "full-reading" and scope.get("report_depth") != "summary"

        if scope.get("delivery_mode") == "full-reading":
            missing_baseline_contract = [item for item in BASELINE_TOPICS if item not in mandatory]
            if missing_baseline_contract:
                blockers.append(
                    "Full-reading scope omits mandatory baseline topics: "
                    f"{missing_baseline_contract}"
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
        for topic_id in required_topics:
            chunks = rendered_topics.get(topic_id, [])
            if chunks and len(_reader_facing_text(chunks[0])) < 12:
                blockers.append(f"Report topic {topic_id} lacks substantive reader-facing prose")

        if detailed:
            declared_core = scope.get("natal_core_sections", [])
            if not isinstance(declared_core, list):
                declared_core = []
            required_core = list(NATAL_CORE_SECTIONS)
            missing_core_contract = [item for item in required_core if item not in declared_core]
            if missing_core_contract:
                blockers.append(f"Detailed-natal scope omits core sections: {missing_core_contract}")
            rendered_core = marked_sections(render_text, CORE_MARKER)
            missing_core = [item for item in required_core if item not in rendered_core]
            if missing_core:
                blockers.append(f"Detailed-natal report omits core sections: {missing_core}")
            duplicate_core = [item for item, chunks in rendered_core.items() if len(chunks) != 1]
            if duplicate_core:
                blockers.append(f"Core section marker is not one-to-one: {duplicate_core}")
            for core_id in required_core:
                chunks = rendered_core.get(core_id, [])
                if chunks and len(_reader_facing_text(chunks[0])) < 12:
                    blockers.append(f"Core section {core_id} lacks substantive reader-facing prose")
            if scope.get("feedback_offer_state") not in {"offered", "declined"}:
                blockers.append("Delivered report requires feedback_offer_state: offered or declined")

        if scope.get("requested") is True:
            raw_luck_periods = scope.get("luck_periods", [])
            if isinstance(raw_luck_periods, list):
                luck_period_ids = [
                    str(item.get("luck_period_id")) if isinstance(item, dict) else str(item)
                    for item in raw_luck_periods
                    if (isinstance(item, dict) and item.get("luck_period_id"))
                    or (not isinstance(item, dict) and str(item))
                ]
            rendered_luck_periods = marked_sections(render_text, LUCK_PERIOD_MARKER)
            missing_luck_periods = [
                item for item in luck_period_ids if item not in rendered_luck_periods
            ]
            if missing_luck_periods:
                blockers.append(
                    "Requested major-luck periods lack independent render markers: "
                    f"{missing_luck_periods}"
                )
            duplicate_luck_periods = [
                item for item, chunks in rendered_luck_periods.items() if len(chunks) != 1
            ]
            if duplicate_luck_periods:
                blockers.append(
                    "Major-luck marker is not one-to-one: "
                    f"{duplicate_luck_periods}"
                )
            for luck_period_id in luck_period_ids:
                chunks = rendered_luck_periods.get(luck_period_id, [])
                if chunks and len(_reader_facing_text(chunks[0])) < 12:
                    blockers.append(
                        f"Major-luck period {luck_period_id} lacks substantive reader-facing prose"
                    )
            raw_years = scope.get("annual_years", [])
            if isinstance(raw_years, list):
                annual_years = [int(item) for item in raw_years if isinstance(item, int) or str(item).isdigit()]
            rendered_years = marked_sections(render_text, TIMING_YEAR_MARKER)
            missing_years = [year for year in annual_years if str(year) not in rendered_years]
            if missing_years:
                blockers.append(f"Requested annual years lack independent render markers: {missing_years}")
            duplicate_years = [item for item, chunks in rendered_years.items() if len(chunks) != 1]
            if duplicate_years:
                blockers.append(f"Timing year marker is not one-to-one: {duplicate_years}")
            for year in annual_years:
                chunks = rendered_years.get(str(year), [])
                if chunks and len(_reader_facing_text(chunks[0])) < 12:
                    blockers.append(f"Timing year {year} lacks substantive reader-facing prose")

    canonical_judgments: dict[str, list[str]] = {}
    for finding_id, chunks in canonical.items():
        ids = JUDGMENT_ID.findall(chunks[0]) if chunks else []
        canonical_judgments[finding_id] = list(dict.fromkeys(ids))
        if detailed and not canonical_judgments[finding_id]:
            blockers.append(
                f"{finding_id} must expose at least one stable judgment ID"
            )

    all_known_judgments = {item for ids in canonical_judgments.values() for item in ids}
    rendered_judgment_markers = JUDGMENT_MARKER.findall(render_text)
    unknown_judgments = sorted(set(rendered_judgment_markers) - all_known_judgments)
    if unknown_judgments:
        blockers.append(f"Render contains unknown judgment IDs: {unknown_judgments}")

    for finding_id in required:
        chunks = rendered.get(finding_id, [])
        if not chunks:
            continue
        chunk = chunks[0]
        if len(_reader_facing_text(chunk)) < 12:
            blockers.append(f"{finding_id} lacks substantive reader-facing prose")
        if detailed:
            for judgment_id in canonical_judgments.get(finding_id, []):
                count = len(re.findall(rf"<!--\s*judgment_id:\s*{re.escape(judgment_id)}\s*-->", chunk))
                if count != 1:
                    blockers.append(f"{finding_id} judgment marker {judgment_id} occurs {count} times")
                elif len(_judgment_body(chunk, judgment_id)) < 12:
                    blockers.append(
                        f"{finding_id} judgment {judgment_id} lacks substantive reader-facing prose"
                    )
        if "source gap" in chunk.lower() and "不确定" not in chunk and "缺" not in chunk:
            warnings.append(f"{finding_id} mentions a source gap without reader-facing uncertainty.")

    if detailed:
        if receipt_text is None:
            blockers.append("Detailed-natal report requires render-card-receipt.yaml")
        else:
            required_receipt_guards = {
                "raw_card_access: forbidden",
                "render_input_mode: audited-envelopes-only",
                "raw_card_read: false",
            }
            missing_guards = sorted(item for item in required_receipt_guards if item not in receipt_text)
            if missing_guards:
                blockers.append(f"Render receipt lacks raw-card firewall guards: {missing_guards}")
            for finding_id in required:
                if finding_id not in receipt_text:
                    blockers.append(f"Render receipt omits finding {finding_id}")
            for judgment_id in sorted(all_known_judgments):
                if judgment_id not in receipt_text:
                    blockers.append(f"Render receipt omits judgment {judgment_id}")

    verdict = "FAIL" if blockers else ("PASS_WITH_WARNINGS" if warnings else "PASS")
    return {
        "verdict": verdict,
        "mode": mode,
        "detailed_natal": detailed,
        "finding_count": len(finding_ids),
        "rendered_ids": list(rendered),
        "required_ids": required,
        "rendered_topics": list(rendered_topics),
        "required_topics": required_topics,
        "judgment_count": sum(len(items) for items in canonical_judgments.values()),
        "required_core_sections": required_core,
        "required_annual_years": annual_years,
        "required_luck_periods": luck_period_ids,
        "blockers": blockers,
        "warnings": warnings,
        "boundary": "Mechanical coverage only; run bazi-finding-audit for semantic fidelity.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Bazi render coverage.")
    parser.add_argument("findings", help="Canonical findings file, findings directory, or case directory")
    parser.add_argument("render")
    parser.add_argument("--mode", choices=("report", "qa"), default="report")
    parser.add_argument("--expect", action="append", default=[])
    parser.add_argument("--scope", help="report-scope.yaml")
    parser.add_argument("--receipt", help="render-card-receipt.yaml")
    args = parser.parse_args()
    try:
        findings_text, finding_sources = read_canonical_findings(args.findings)
        result = check(
            findings_text,
            read(args.render),
            args.mode,
            args.expect,
            read(args.scope) if args.scope else None,
            read(args.receipt) if args.receipt else None,
        )
        result["finding_sources"] = finding_sources
    except OSError as exc:
        result = {"verdict": "FAIL", "blockers": [str(exc)], "warnings": []}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["verdict"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
