#!/usr/bin/env python3
"""Independently scan a Bazi reader delivery against scope and canonical findings."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from types import ModuleType


def load_render_checker() -> ModuleType:
    path = Path(__file__).resolve().parents[2] / "bazi-render" / "scripts" / "check_render_coverage.py"
    spec = importlib.util.spec_from_file_location("bazi_render_coverage", path)
    if spec is None or spec.loader is None:
        raise OSError(f"cannot load render checker: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _has_core_markers(reader_dir: Path, checker: ModuleType) -> tuple[set[str], list[str]]:
    texts: list[str] = []
    sources: list[str] = []
    if reader_dir.is_dir():
        for path in sorted(reader_dir.rglob("*.md")):
            texts.append(path.read_text(encoding="utf-8"))
            sources.append(str(path))
    markers = set(checker.CORE_MARKER.findall("\n".join(texts)))
    return markers, sources


def _first_existing(case_dir: Path, candidates: list[str]) -> tuple[Path, str]:
    """Resolve the active-v3 layout first while retaining legacy read compatibility."""
    for relative in candidates:
        candidate = case_dir / relative
        if candidate.is_file():
            return candidate, relative
    return case_dir / candidates[0], candidates[0]


def scan(case_dir: Path, scope_path: Path, render_path: Path, receipt_path: Path) -> dict[str, object]:
    checker = load_render_checker()
    blockers: list[str] = []
    warnings: list[str] = []
    try:
        scope_text = scope_path.read_text(encoding="utf-8")
        render_text = render_path.read_text(encoding="utf-8")
        receipt_text = receipt_path.read_text(encoding="utf-8")
        build_root = (
            render_path.parent.parent
            if render_path.parent.name in {"render", "delivery"}
            else case_dir
        )
        # Let the canonical reader discover both the current sibling layout
        # (natal-core-findings/ + topic-findings/) and legacy nested layouts.
        # Starting at the active build root avoids silently falling through to
        # another version under the wider case directory.
        findings_root = build_root
        findings_text, finding_sources = checker.read_canonical_findings(findings_root)
    except OSError as exc:
        return {"verdict": "FAIL", "blockers": [str(exc)], "warnings": [], "case_dir": str(case_dir)}

    render_scan = checker.check(
        findings_text,
        render_text,
        "report",
        [],
        scope_text,
        receipt_text,
    )
    blockers.extend(f"render-coverage: {item}" for item in render_scan["blockers"])
    warnings.extend(f"render-coverage: {item}" for item in render_scan["warnings"])

    scope = checker.scope_values(scope_text)
    detailed = scope.get("delivery_mode") == "full-reading" and scope.get("report_depth") != "summary"
    required_upstream: list[str] = []
    reader_sources: list[str] = []
    if detailed:
        local_upstream = [
            [
                build_root / "topic-lenses" / "natal-core.yaml",
                build_root / "natal-core-lens-index.yaml",
                case_dir / "v3" / "natal-core-lens-index.yaml",
                case_dir / "natal-core-lens-index.yaml",
            ],
            [
                build_root / "composition" / "natal-core-coverage-index.yaml",
                build_root / "natal-core-coverage-index.yaml",
                case_dir / "v3" / "natal-core-coverage-index.yaml",
                case_dir / "natal-core-coverage-index.yaml",
            ],
            [
                build_root / "composition" / "hidden-manifestation-matrix.yaml",
                build_root / "findings" / "hidden-manifestation-matrix.json",
                case_dir / "v3" / "findings" / "hidden-manifestation-matrix.yaml",
                case_dir / "hidden-manifestation-matrix.yaml",
            ],
            [
                build_root / "composition" / "cross-topic-claim-registry.yaml",
                build_root / "findings" / "cross-topic-claim-registry.json",
                case_dir / "v3" / "findings" / "cross-topic-claim-registry.yaml",
                case_dir / "cross-topic-claim-registry.yaml",
            ],
            [
                build_root / "composition" / "composition.md",
                build_root / "findings" / "composition.md",
                case_dir / "v3" / "composition" / "composition.md",
                case_dir / "composition.md",
            ],
        ]
        for candidates in local_upstream:
            resolved = next((item for item in candidates if item.is_file()), candidates[0])
            try:
                relative = str(resolved.relative_to(case_dir))
            except ValueError:
                relative = str(resolved)
            required_upstream.append(relative)
            if not resolved.is_file():
                blockers.append(f"detailed-natal upstream artifact missing: {relative}")
        required_upstream.append(str(receipt_path.relative_to(case_dir)))
        if not receipt_path.is_file():
            blockers.append(f"detailed-natal upstream artifact missing: {receipt_path}")
        delivery_reader = render_path.parent / "reader"
        reader_dir = delivery_reader if delivery_reader.is_dir() else case_dir / "reader"
        markers, reader_sources = _has_core_markers(reader_dir, checker)
        if not reader_dir.is_dir():
            blockers.append("detailed-natal reader/ directory is missing")
        missing_reader_core = [item for item in checker.NATAL_CORE_SECTIONS if item not in markers]
        if missing_reader_core:
            blockers.append(f"reader modules omit natal core sections: {missing_reader_core}")

    annual_years: list[int] = []
    luck_period_ids: list[str] = []
    if scope.get("requested") is True:
        raw_luck_periods = scope.get("luck_periods", [])
        if isinstance(raw_luck_periods, list):
            luck_period_ids = [
                str(item.get("luck_period_id")) if isinstance(item, dict) else str(item)
                for item in raw_luck_periods
                if (isinstance(item, dict) and item.get("luck_period_id"))
                or (not isinstance(item, dict) and str(item))
            ]
        timing_root = build_root / "structure" / "timing"
        for luck_period_id in luck_period_ids:
            file_stem = luck_period_id.replace("LP-", "LP", 1)
            for suffix in (
                "interaction-census.yaml",
                "activation-overlay.yaml",
                "process-state-diff.yaml",
            ):
                artifact = timing_root / f"{file_stem}-{suffix}"
                if not artifact.is_file():
                    blockers.append(
                        f"requested major-luck period {luck_period_id} lacks {suffix}: "
                        f"{artifact.relative_to(case_dir)}"
                    )
        raw_years = scope.get("annual_years", [])
        if isinstance(raw_years, list):
            annual_years = [int(item) for item in raw_years if isinstance(item, int) or str(item).isdigit()]
        for year in annual_years:
            timing_roots = [build_root / "structure" / "timing", case_dir / "timing"]
            census_candidates = [
                root / f"year-{year}-interaction-census.yaml" for root in timing_roots
            ]
            diff_candidates = [
                root / f"year-{year}-overlay-diff.yaml" for root in timing_roots
            ]
            census = next((item for item in census_candidates if item.is_file()), census_candidates[0])
            diff = next((item for item in diff_candidates if item.is_file()), diff_candidates[0])
            if not census.is_file():
                blockers.append(f"requested year {year} lacks independent interaction census: {census.relative_to(case_dir)}")
            if not diff.is_file():
                blockers.append(f"requested year {year} lacks independent overlay diff: {diff.relative_to(case_dir)}")

    verdict = "FAIL" if blockers else ("PASS_WITH_WARNINGS" if warnings else "PASS")
    return {
        "schema_version": "1.0",
        "verdict": verdict,
        "case_dir": str(case_dir),
        "scope": str(scope_path),
        "render": str(render_path),
        "receipt": str(receipt_path),
        "detailed_natal": detailed,
        "finding_sources": finding_sources,
        "reader_sources": reader_sources,
        "required_upstream": required_upstream,
        "annual_years": annual_years,
        "luck_period_ids": luck_period_ids,
        "render_scan": render_scan,
        "blockers": blockers,
        "warnings": warnings,
        "boundary": "Independent delivery-shape scan; semantic audit remains separately required.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Independently scan a Bazi reader delivery.")
    parser.add_argument("case_dir")
    parser.add_argument("--scope", required=True)
    parser.add_argument("--render", required=True)
    parser.add_argument("--receipt", required=True)
    parser.add_argument("--output", help="Optional JSON evidence-scan output path")
    args = parser.parse_args()
    result = scan(
        Path(args.case_dir).resolve(),
        Path(args.scope).resolve(),
        Path(args.render).resolve(),
        Path(args.receipt).resolve(),
    )
    payload = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(payload + "\n", encoding="utf-8")
    print(payload)
    return 1 if result["verdict"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
