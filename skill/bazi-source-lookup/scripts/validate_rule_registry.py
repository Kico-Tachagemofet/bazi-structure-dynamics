#!/usr/bin/env python3
"""Validate conditional Bazi rule cards without making metaphysical judgments."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


VALID_RULE_TYPES = {
    "conditional-principle",
    "interaction-arbitration",
    "mechanism-with-examples",
    "mechanism-bearing-imagery",
    "fixed-label-prohibition",
}
VALID_CURATION = {"pending_human_review", "approved", "rejected"}
VALID_CONFIDENCE = {"low", "medium", "high"}
VALID_HOOK_ROLES = {"route", "propose", "decide", "guard", "audit"}
HOOK_ORDER = {
    "stage-1.2-source-route": 12,
    "stage-1.5B-interaction-census": 15,
    "stage-1.5C-post-branch-node-ledger": 18,
    "stage-2B.1-relation-form": 21,
    "stage-2B.2-competition-arbitration": 22,
    "stage-2B.3-allocation": 23,
    "stage-2B.4-residual-capacity": 24,
    "stage-2B.5-effect-dimensions": 25,
    "stage-2D-problem-state": 27,
    "stage-3.5-structure-audit": 35,
    "stage-4B-timing-synastry-overlay": 42,
    "stage-4B.5-overlay-audit": 42.5,
    "stage-4C-imagery-source": 43,
    "stage-4D-imagery-composition": 44,
    "stage-4.5-finding-audit": 45,
}
ABSOLUTE_TERMS = ("一律", "绝不", "必然", "无条件", "百分之百")
INTERACTION_TYPES = {
    "conditional-principle",
    "interaction-arbitration",
    "mechanism-with-examples",
}
EFFECT_DIMENSIONS = {
    "material_damage",
    "functional_restraint",
    "protective_effect",
    "relation_form",
}


def source_span_text(path: Path, start: int, end: int) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    if start < 1 or end < start or end > len(lines):
        raise ValueError(f"invalid source span {start}-{end}; file has {len(lines)} lines")
    return "\n".join(lines[start - 1 : end]) + "\n"


def validate_registry(registry_path: Path, project_root: Path) -> list[str]:
    errors: list[str] = []
    try:
        payload = json.loads(registry_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"registry unreadable: {exc}"]

    for field in ("schema_version", "registry_id", "release_state", "source_policy", "cards"):
        if field not in payload:
            errors.append(f"registry missing {field}")
    cards = payload.get("cards")
    if not isinstance(cards, list) or not cards:
        errors.append("registry cards must be a non-empty list")
        return errors

    ids = [card.get("rule_id") for card in cards if isinstance(card, dict)]
    if len(ids) != len(set(ids)):
        errors.append("rule_id values must be unique")
    known_ids = set(ids)

    required = {
        "rule_id",
        "title",
        "rule_type",
        "source",
        "taiji_of_source",
        "applicable_taiji",
        "question_answered",
        "questions_not_answered",
        "rule_summary",
        "preserved_qualifiers",
        "conditions",
        "prohibited_shortcuts",
        "cross_refs",
        "pipeline_hooks",
        "curation",
        "auto_application",
    }
    for index, card in enumerate(cards, start=1):
        if not isinstance(card, dict):
            errors.append(f"card #{index} must be an object")
            continue
        rule_id = card.get("rule_id", f"card#{index}")
        missing = sorted(required - set(card))
        if missing:
            errors.append(f"{rule_id}: missing fields {', '.join(missing)}")
            continue

        rule_type = card["rule_type"]
        if rule_type not in VALID_RULE_TYPES:
            errors.append(f"{rule_id}: invalid rule_type {rule_type}")
        if not card["taiji_of_source"] or not card["applicable_taiji"]:
            errors.append(f"{rule_id}: source and applicable taiji must be explicit")
        if not isinstance(card["questions_not_answered"], list) or not card["questions_not_answered"]:
            errors.append(f"{rule_id}: questions_not_answered must be non-empty")
        if not isinstance(card["preserved_qualifiers"], list):
            errors.append(f"{rule_id}: preserved_qualifiers must be a list")
        if card["preserved_qualifiers"] and any(term in card["rule_summary"] for term in ABSOLUTE_TERMS):
            errors.append(f"{rule_id}: qualified source was rewritten with an absolute term")

        source = card["source"]
        source_required = {"file", "line_start", "line_end", "excerpt_sha256", "provenance_layer", "framework"}
        if not isinstance(source, dict) or not source_required.issubset(source):
            errors.append(f"{rule_id}: incomplete source receipt")
        else:
            source_path = project_root / source["file"]
            try:
                span = source_span_text(source_path, int(source["line_start"]), int(source["line_end"]))
                actual = hashlib.sha256(span.encode("utf-8")).hexdigest()
                if actual != source["excerpt_sha256"]:
                    errors.append(f"{rule_id}: source excerpt hash mismatch; actual={actual}")
            except (OSError, TypeError, ValueError) as exc:
                errors.append(f"{rule_id}: source receipt invalid: {exc}")

        conditions = card["conditions"]
        condition_fields = {
            "required_state_refs",
            "applicability_conditions",
            "override_conditions",
            "failure_conditions",
        }
        if not isinstance(conditions, dict) or not condition_fields.issubset(conditions):
            errors.append(f"{rule_id}: incomplete conditions")
        elif not conditions["override_conditions"] or not conditions["failure_conditions"]:
            errors.append(f"{rule_id}: override and failure conditions must be non-empty")

        if rule_type in INTERACTION_TYPES:
            dimensions = card.get("effect_dimensions")
            if not isinstance(dimensions, dict) or set(dimensions) != EFFECT_DIMENSIONS:
                errors.append(f"{rule_id}: interaction rule must separate all four effect dimensions")

        unknown_refs = sorted(set(card["cross_refs"]) - known_ids)
        if unknown_refs:
            errors.append(f"{rule_id}: unknown cross_refs {', '.join(unknown_refs)}")

        pipeline = card["pipeline_hooks"]
        pipeline_fields = {"hooks", "depends_on", "may_not_decide"}
        if not isinstance(pipeline, dict) or not pipeline_fields.issubset(pipeline):
            errors.append(f"{rule_id}: incomplete pipeline_hooks")
        else:
            hooks = pipeline["hooks"]
            dependencies = pipeline["depends_on"]
            forbidden_decisions = pipeline["may_not_decide"]
            if not isinstance(hooks, list) or not hooks:
                errors.append(f"{rule_id}: pipeline hooks must be a non-empty list")
            else:
                previous_order = -1
                for hook_index, hook_spec in enumerate(hooks, start=1):
                    hook_fields = {"hook", "role", "reads", "writes"}
                    if not isinstance(hook_spec, dict) or not hook_fields.issubset(hook_spec):
                        errors.append(f"{rule_id}: incomplete pipeline hook #{hook_index}")
                        continue
                    hook = hook_spec["hook"]
                    role = hook_spec["role"]
                    reads = hook_spec["reads"]
                    writes = hook_spec["writes"]
                    if hook not in HOOK_ORDER:
                        errors.append(f"{rule_id}: unknown pipeline hook {hook}")
                    elif HOOK_ORDER[hook] < previous_order:
                        errors.append(f"{rule_id}: pipeline hooks are not in runtime order")
                    else:
                        previous_order = HOOK_ORDER[hook]
                    if role not in VALID_HOOK_ROLES:
                        errors.append(f"{rule_id}: invalid hook role {role}")
                    if not isinstance(reads, list) or not reads:
                        errors.append(f"{rule_id}: hook {hook} needs non-empty reads")
                    if not isinstance(writes, list) or not writes:
                        errors.append(f"{rule_id}: hook {hook} needs non-empty writes")
                    if isinstance(reads, list) and isinstance(writes, list):
                        overlap = sorted(set(reads) & set(writes))
                        if overlap:
                            errors.append(
                                f"{rule_id}: hook {hook} reads and writes the same target {', '.join(overlap)}"
                            )
            if not isinstance(dependencies, list):
                errors.append(f"{rule_id}: depends_on must be a list")
            else:
                unknown_dependencies = sorted(set(dependencies) - known_ids)
                if unknown_dependencies:
                    errors.append(
                        f"{rule_id}: unknown pipeline dependencies {', '.join(unknown_dependencies)}"
                    )
                if rule_id in dependencies:
                    errors.append(f"{rule_id}: pipeline cannot depend on itself")
            if not isinstance(forbidden_decisions, list) or not forbidden_decisions:
                errors.append(f"{rule_id}: may_not_decide must be non-empty")

        curation = card["curation"]
        if not isinstance(curation, dict):
            errors.append(f"{rule_id}: curation must be an object")
            continue
        status = curation.get("status")
        cap = curation.get("confidence_cap")
        if status not in VALID_CURATION:
            errors.append(f"{rule_id}: invalid curation status {status}")
        if cap not in VALID_CONFIDENCE:
            errors.append(f"{rule_id}: invalid confidence cap {cap}")
        if card["auto_application"] is not False:
            errors.append(f"{rule_id}: interpretive rule cards cannot auto-apply")
        if status == "pending_human_review":
            if cap == "high":
                errors.append(f"{rule_id}: pending card cannot have high confidence cap")
        if status == "approved" and (not curation.get("reviewed_by") or not curation.get("reviewed_at")):
            errors.append(f"{rule_id}: approved card needs reviewer and review time")

    dependency_map = {
        card["rule_id"]: card.get("pipeline_hooks", {}).get("depends_on", [])
        for card in cards
        if isinstance(card, dict) and card.get("rule_id")
    }
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(rule_id: str, trail: list[str]) -> None:
        if rule_id in visiting:
            cycle_start = trail.index(rule_id) if rule_id in trail else 0
            errors.append(f"pipeline dependency cycle: {' -> '.join(trail[cycle_start:] + [rule_id])}")
            return
        if rule_id in visited:
            return
        visiting.add(rule_id)
        for dependency in dependency_map.get(rule_id, []):
            if dependency in dependency_map:
                visit(dependency, trail + [rule_id])
        visiting.remove(rule_id)
        visited.add(rule_id)

    for current_rule_id in dependency_map:
        visit(current_rule_id, [])

    statuses = {
        card.get("curation", {}).get("status")
        for card in cards
        if isinstance(card, dict)
    }
    if "approved" in statuses and "pending_human_review" in statuses:
        if payload.get("release_state") != "reviewed_partial":
            errors.append("mixed approved/pending registry must use release_state reviewed_partial")

    return errors


def main() -> int:
    default_registry = Path(__file__).resolve().parents[1] / "references" / "rule-registry-qianli-high-risk.json"
    default_root = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser(description="Validate conditional Bazi rule registry.")
    parser.add_argument("registry", nargs="?", default=str(default_registry))
    parser.add_argument("--project-root", default=str(default_root))
    args = parser.parse_args()

    errors = validate_registry(Path(args.registry), Path(args.project_root))
    result: dict[str, Any] = {
        "verdict": "PASS" if not errors else "FAIL",
        "registry": str(Path(args.registry)),
        "errors": errors,
        "boundary": "Schema/source validation only; no chart judgment is automated.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
