#!/usr/bin/env python3
"""Validate route edge references against the qualified edge map.

The parser intentionally supports the narrow YAML subset required by the Bazi
schemas: list records with scalar fields and inline scalar lists. Keeping that
subset narrow makes endpoint validation deterministic without a YAML package.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


RECORD_START = re.compile(r"^(?P<indent>\s*)-\s+(?P<key>[A-Za-z_][\w-]*):\s*(?P<value>.*)$")
FIELD = re.compile(r"^(?P<indent>\s+)(?P<key>[A-Za-z_][\w-]*):\s*(?P<value>.*)$")


def scalar(value: str):
    value = value.strip()
    if not value:
        return ""
    if value in {"true", "false"}:
        return value == "true"
    if value in {"null", "~"}:
        return None
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [scalar(item) for item in inner.split(",")]
    return value


def records(text: str, identity_key: str) -> list[dict]:
    output: list[dict] = []
    current: dict | None = None
    base_indent = 0
    for line in text.splitlines():
        start = RECORD_START.match(line)
        if start and start.group("key") == identity_key:
            if current is not None:
                output.append(current)
            base_indent = len(start.group("indent"))
            current = {identity_key: scalar(start.group("value"))}
            continue
        if current is None:
            continue
        if start and len(start.group("indent")) <= base_indent:
            output.append(current)
            current = None
            continue
        field = FIELD.match(line)
        if field and len(field.group("indent")) > base_indent:
            current[field.group("key")] = scalar(field.group("value"))
    if current is not None:
        output.append(current)
    return output


def validate(edge_text: str, route_text: str) -> dict:
    edge_records = records(edge_text, "edge_id")
    route_records = records(route_text, "route_id")
    edges = {item.get("edge_id"): item for item in edge_records}
    blockers: list[str] = []
    warnings: list[str] = []
    endpoint_map: dict[str, list[dict]] = {}

    if len(edges) != len(edge_records):
        blockers.append("Edge IDs are missing or duplicated.")
    if not route_records:
        blockers.append("No structured route records found.")

    for route in route_records:
        route_id = str(route.get("route_id", "<missing>"))
        refs = route.get("edge_refs", [])
        if not isinstance(refs, list) or not refs:
            blockers.append(f"{route_id}: edge_refs must be a non-empty inline list.")
            continue
        expanded: list[dict] = []
        for edge_id in refs:
            edge = edges.get(edge_id)
            if edge is None:
                blockers.append(f"{route_id}: unknown edge ref {edge_id}.")
                continue
            expanded.append(
                {
                    "edge_id": edge_id,
                    "source_node": edge.get("source_node"),
                    "target_node": edge.get("target_node"),
                    "action": edge.get("action"),
                    "edge_layer": edge.get("edge_layer"),
                    "distance_and_order": edge.get("distance_and_order"),
                }
            )
        endpoint_map[route_id] = expanded

        topology = route.get("topology", "chain")
        if topology == "chain":
            for left, right in zip(expanded, expanded[1:]):
                if left["target_node"] != right["source_node"]:
                    blockers.append(
                        f"{route_id}: discontinuity {left['edge_id']}->{right['edge_id']} "
                        f"({left['target_node']} != {right['source_node']})."
                    )
        elif topology == "mixed" and not route.get("continuity_notes"):
            blockers.append(f"{route_id}: mixed topology requires continuity_notes.")
        elif topology not in {"chain", "parallel", "mixed"}:
            blockers.append(f"{route_id}: invalid topology {topology}.")

        effect = route.get("net_effect_on_primary_problem")
        outlet = route.get("outlet_eligible")
        priority = route.get("therapeutic_priority")
        if effect == "aggravating" and outlet is True:
            blockers.append(f"{route_id}: aggravating route cannot be an outlet.")
        if effect == "aggravating" and priority not in {None, "", "not-applicable"}:
            blockers.append(f"{route_id}: aggravating route cannot have therapeutic priority.")
        if effect in {"therapeutic", "mixed"} and priority in {None, ""}:
            warnings.append(f"{route_id}: therapeutic route has no therapeutic_priority.")

        forbidden = {
            "ordered_nodes",
            "ordered_edges",
            "ordered_nodes_and_edges",
            "source_node",
            "target_node",
        }
        drift_fields = sorted(forbidden.intersection(route))
        if drift_fields:
            blockers.append(f"{route_id}: route duplicates endpoint fields {drift_fields}.")

    verdict = "FAIL" if blockers else ("PASS_WITH_WARNINGS" if warnings else "PASS")
    return {
        "verdict": verdict,
        "edge_count": len(edges),
        "route_count": len(route_records),
        "blockers": blockers,
        "warnings": warnings,
        "route_edge_endpoint_map": endpoint_map,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Bazi route endpoint integrity.")
    parser.add_argument("edge_map")
    parser.add_argument("routes")
    parser.add_argument("--write-map")
    args = parser.parse_args()
    result = validate(
        Path(args.edge_map).read_text(encoding="utf-8"),
        Path(args.routes).read_text(encoding="utf-8"),
    )
    if args.write_map:
        Path(args.write_map).write_text(
            json.dumps(result["route_edge_endpoint_map"], ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["verdict"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
