#!/usr/bin/env python3
"""Validate the deterministic enumeration artifact before model judgment."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def load_payload(path: str) -> dict:
    if path == "-":
        return json.load(sys.stdin)
    return json.loads(Path(path).read_text(encoding="utf-8"))


def check(payload: dict) -> dict:
    blockers: list[str] = []
    warnings: list[str] = []
    pillars = payload.get("pillars", {})
    nodes = payload.get("nodes", [])
    branch_data = payload.get("branch_candidates", {})
    coverage = payload.get("coverage_audit", {})

    if set(pillars) != {"year", "month", "day", "hour"}:
        blockers.append("Four positioned pillars are not present.")
    node_ids = [node.get("node_id") for node in nodes]
    if len(node_ids) != len(set(node_ids)):
        blockers.append("Node IDs are not unique.")
    if not coverage.get("all_nodes_present"):
        blockers.append("Visible and hidden node coverage is incomplete.")
    if len(payload.get("visible_stem_pair_checks", [])) != 6:
        blockers.append("All six visible stem position pairs were not checked.")
    if len(branch_data.get("pair_checks", [])) != 6:
        blockers.append("All six branch position pairs were not checked.")
    if not coverage.get("self_punishment_scan_completed"):
        blockers.append("Self-punishment scan is missing.")
    if not coverage.get("punishment_group_scan_completed"):
        blockers.append("Three-punishment group scan is missing.")
    if not coverage.get("group_scan_completed"):
        blockers.append("Three-harmony or directional-meeting scan is missing.")
    if not coverage.get("shared_node_scan_completed"):
        blockers.append("Shared-node competition scan is missing.")
    if payload.get("scope") != "facts_and_candidates_only":
        warnings.append("Artifact scope is not explicitly facts-and-candidates only.")
    if not payload.get("prohibited_inferences"):
        warnings.append("Prohibited inference boundary is missing.")

    verdict = "FAIL" if blockers else ("PASS_WITH_WARNINGS" if warnings else "PASS")
    return {
        "verdict": verdict,
        "blockers": blockers,
        "warnings": warnings,
        "counts": {
            "nodes": len(nodes),
            "visible_stem_pair_checks": len(payload.get("visible_stem_pair_checks", [])),
            "branch_pair_checks": len(branch_data.get("pair_checks", [])),
            "branch_relations": len(branch_data.get("pair_relations", [])),
            "branch_group_candidates": len(branch_data.get("group_candidates", [])),
            "elemental_candidate_edges": len(payload.get("elemental_candidate_edges", [])),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit a Bazi fact enumeration JSON artifact.")
    parser.add_argument("artifact", nargs="?", default="-", help="JSON file or - for stdin")
    args = parser.parse_args()
    result = check(load_payload(args.artifact))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["verdict"] != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
