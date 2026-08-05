#!/usr/bin/env python3
"""Run anonymous regression fixtures against the deterministic enumerator."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path


def load_enumerator():
    script = (
        Path(__file__).resolve().parents[2]
        / "bazi-reader"
        / "scripts"
        / "bazi_fact_enumerator.py"
    )
    spec = importlib.util.spec_from_file_location("bazi_fact_enumerator", script)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load enumerator: {script}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def relation_exists(payload: dict, relation_type: str, branches: set[str]) -> bool:
    return any(
        relation.get("type") == relation_type
        and set(relation.get("branches", [])) == branches
        for relation in payload["branch_candidates"]["pair_relations"]
    )


def repeated_exists(payload: dict, branch: str) -> bool:
    return any(
        item["branch"] == branch and item["count"] >= 2
        for item in payload["branch_candidates"]["repeated_branches"]
    )


def fixture_k(module) -> list[str]:
    payload = module.enumerate_chart(["戊寅", "丙辰", "壬寅", "庚戌"])
    failures: list[str] = []
    if not repeated_exists(payload, "寅"):
        failures.append("K: repeated 寅 missing")
    if not relation_exists(payload, "clash", {"辰", "戌"}):
        failures.append("K: 辰戌 clash missing")
    if any(
        item["type"] == "self_punishment"
        for item in payload["branch_candidates"]["pair_relations"]
    ):
        failures.append("K: false self-punishment reported")
    if set(payload["void_branches"]) != {"辰", "巳"}:
        failures.append("K: void branches should be 辰巳")
    if payload["coverage_audit"]["verdict"] != "PASS":
        failures.append("K: coverage audit failed")
    return failures


def fixture_a(module) -> list[str]:
    payload = module.enumerate_chart(["癸卯", "戊午", "戊午", "庚申"])
    failures: list[str] = []
    if not repeated_exists(payload, "午"):
        failures.append("A: repeated 午 missing")
    if not relation_exists(payload, "self_punishment", {"午"}):
        failures.append("A: 午午 self-punishment missing")
    combinations = payload["visible_stem_combinations"]
    if len(combinations) != 2:
        failures.append("A: two 戊癸 combination candidates were not enumerated")
    shared = payload["shared_stem_combination_candidates"]
    if not any(
        item["node_id"] == "year.stem" and len(item["candidate_relations"]) == 2
        for item in shared
    ):
        failures.append("A: shared 癸 node in two 戊癸 candidates was not flagged")
    rooted_pair = any(
        set(pair["nodes"]) == {"hour.stem", "hour.branch.hidden.1"}
        and pair["same_polarity"]
        and pair["position_distance"] == 0
        for pair in payload["same_element_candidate_pairs"]
    )
    if not rooted_pair:
        failures.append("A: same-pillar 庚申 root candidate missing")
    if set(payload["void_branches"]) != {"子", "丑"}:
        failures.append("A: void branches should be 子丑")
    if payload["coverage_audit"]["verdict"] != "PASS":
        failures.append("A: coverage audit failed")
    return failures


def fixture_edge_punishment_group(module) -> list[str]:
    payload = module.enumerate_chart(["甲寅", "己巳", "丙申", "戊子"])
    failures: list[str] = []
    complete = any(
        item.get("type") == "three_punishment_group"
        and item.get("subtype") == "ungrateful"
        and item.get("completeness") == "complete"
        for item in payload["branch_candidates"]["group_candidates"]
    )
    if not complete:
        failures.append("E: complete 寅巳申 punishment group missing")
    return failures


def main() -> int:
    module = load_enumerator()
    failures = fixture_k(module) + fixture_a(module) + fixture_edge_punishment_group(module)
    result = {
        "verdict": "PASS" if not failures else "FAIL",
        "fixtures": ["K", "A", "E-punishment-group"],
        "failures": failures,
        "boundary": "These tests verify enumeration, not strength or interpretation.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
