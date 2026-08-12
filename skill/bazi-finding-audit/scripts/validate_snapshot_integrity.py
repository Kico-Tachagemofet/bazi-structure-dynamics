#!/usr/bin/env python3
"""Validate freeze hashes and classify every routable downstream artifact."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_routable(relative: Path) -> bool:
    name = relative.name.lower()
    parts = {part.lower() for part in relative.parts}
    if "archive" in parts:
        return False
    if relative.parts and "topic-findings" in parts:
        return relative.suffix.lower() in {".md", ".json", ".yaml", ".yml"}
    if "reader" in parts or "natal-core-findings" in parts or "qa" in parts:
        return relative.suffix.lower() in {".md", ".json", ".yaml", ".yml"}
    prefixes = (
        "report-scope",
        "topic-lens-",
        "topic-lens-index",
        "natal-core-",
        "hidden-manifestation",
        "cross-topic-claim",
        "imagery-source-packet-",
        "imagery-source-read-receipts",
        "imagery-coverage",
        "pillar-composites",
        "axis-scenes",
        "resonance-map",
        "manifestation-map",
        "topic-findings-",
        "composition",
        "timing-activation",
        "overlay-",
        "render-card-receipt",
        "audit-report-findings",
        "audit-state-findings",
        "audit-report-composition",
        "audit-state-composition",
        "audit-report-render",
        "audit-state-render",
        "full-reading",
    )
    return name.startswith(prefixes) and relative.suffix.lower() in {".md", ".json", ".yaml", ".yml"}


def declared_freeze_ids(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    if path.suffix.lower() == ".json":
        try:
            payload = json.loads(text)
            value = payload.get("structure_freeze_id") if isinstance(payload, dict) else None
            if isinstance(value, str):
                return [value]
        except json.JSONDecodeError:
            pass
    patterns = (
        r"<!--\s*structure_freeze_id\s*:\s*([^\s>]+)\s*-->",
        r'^\s*"structure_freeze_id"\s*:\s*"([^"\r\n]+)"',
        r"^\s*structure_freeze_id\s*:\s*['\"]?([^'\"\s\r\n]+)",
        r"^\s*-?\s*`?structure_freeze_id`?\s*[:：]\s*`?([^`\s\r\n]+)",
    )
    found: list[str] = []
    for pattern in patterns:
        found.extend(re.findall(pattern, text, re.MULTILINE))
    return list(dict.fromkeys(found))


def load_json(path: Path, label: str, errors: list[str]) -> dict[str, Any] | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{label} unreadable: {exc}")
        return None


def validate(case_dir: Path, receipt_path: Path, manifest_path: Path) -> list[str]:
    errors: list[str] = []
    receipt = load_json(receipt_path, "freeze receipt", errors)
    manifest = load_json(manifest_path, "active artifact manifest", errors)
    if receipt is None or manifest is None:
        return errors
    if receipt.get("schema_version") != "2.0":
        errors.append("freeze receipt must use schema_version 2.0")
    if manifest.get("schema_version") != "1.0":
        errors.append("active artifact manifest must use schema_version 1.0")
    if manifest.get("case_id") != case_dir.name:
        errors.append("manifest case_id does not match case directory")
    freeze_id = receipt.get("freeze_id")
    if manifest.get("current_structure_freeze_id") != freeze_id:
        errors.append("manifest current freeze does not match receipt")

    receipt_rel_paths: set[str] = set()
    for item in receipt.get("files", []):
        raw = Path(item.get("path", ""))
        path = raw if raw.is_absolute() else case_dir / raw
        if not path.is_file():
            errors.append(f"frozen file missing: {item.get('path')}")
            continue
        if digest(path) != item.get("sha256"):
            errors.append(f"frozen file hash mismatch: {item.get('path')}")
        if not raw.is_absolute():
            receipt_rel_paths.add(raw.as_posix())

    active_items = manifest.get("active_artifacts", [])
    inactive_items = manifest.get("inactive_artifacts", [])
    if not isinstance(active_items, list) or not isinstance(inactive_items, list):
        return errors + ["manifest active_artifacts and inactive_artifacts must be lists"]
    active = {Path(item.get("path", "")).as_posix(): item for item in active_items if isinstance(item, dict)}
    inactive = {Path(item.get("path", "")).as_posix(): item for item in inactive_items if isinstance(item, dict)}
    overlap = sorted(set(active) & set(inactive))
    if overlap:
        errors.append(f"artifacts cannot be both active and inactive: {overlap}")

    discovered = {
        path.relative_to(case_dir).as_posix()
        for path in case_dir.rglob("*")
        if path.is_file() and is_routable(path.relative_to(case_dir))
    }
    unclassified = sorted(discovered - set(active) - set(inactive))
    if unclassified:
        errors.append(f"routable artifacts are unclassified: {unclassified}")

    for relative, item in active.items():
        needed = {"path", "stage", "structure_freeze_id", "dependencies"}
        if not needed.issubset(item):
            errors.append(f"active artifact {relative}: incomplete entry")
            continue
        path = case_dir / relative
        if not path.is_file():
            errors.append(f"active artifact missing: {relative}")
            continue
        if item["structure_freeze_id"] != freeze_id:
            errors.append(f"active artifact {relative}: manifest freeze mismatch")
        declared = declared_freeze_ids(path)
        if not declared:
            errors.append(f"active artifact {relative}: file does not declare structure_freeze_id")
        elif declared != [freeze_id]:
            errors.append(f"active artifact {relative}: stale or mixed freeze refs {declared}")
        for dependency in item["dependencies"]:
            dep = Path(dependency).as_posix()
            dep_path = case_dir / dep
            if dep not in receipt_rel_paths and dep not in active and not dep_path.is_file():
                errors.append(f"active artifact {relative}: missing dependency {dep}")
            if dep in active and active[dep].get("structure_freeze_id") != freeze_id:
                errors.append(f"active dependency {dep}: freeze mismatch")

    for relative, item in inactive.items():
        needed = {"path", "reason", "superseded_by"}
        if not needed.issubset(item):
            errors.append(f"inactive artifact {relative}: incomplete entry")
            continue
        if not (case_dir / relative).is_file():
            errors.append(f"inactive artifact missing: {relative}")
        replacement = item.get("superseded_by")
        if replacement is not None and Path(replacement).as_posix() not in active:
            errors.append(f"inactive artifact {relative}: superseded_by is not active")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Bazi freeze and active artifact graph.")
    parser.add_argument("case_dir")
    parser.add_argument("receipt")
    parser.add_argument("manifest")
    args = parser.parse_args()
    errors = validate(Path(args.case_dir).resolve(), Path(args.receipt).resolve(), Path(args.manifest).resolve())
    result = {"verdict": "PASS" if not errors else "FAIL", "errors": errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
