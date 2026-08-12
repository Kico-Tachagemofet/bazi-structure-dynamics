#!/usr/bin/env python3
"""Detect generic Bazi runtime packets reused across several topics."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def _unit_id(item: Any) -> str:
    if isinstance(item, str):
        return item
    if isinstance(item, dict):
        for key in ("unit_id", "imagery_unit_id", "id"):
            if item.get(key):
                return str(item[key])
    return ""


def _ids(payload: dict[str, Any], key: str) -> tuple[str, ...]:
    values = payload.get(key, [])
    if not isinstance(values, list):
        return ()
    return tuple(sorted(item_id for item in values if (item_id := _unit_id(item))))


def packet_signature(payload: dict[str, Any]) -> tuple[tuple[str, ...], tuple[str, ...]]:
    selected = payload.get("selected_units", payload.get("activated_units", []))
    if not isinstance(selected, list):
        selected = []
    unit_ids = tuple(sorted(item_id for item in selected if (item_id := _unit_id(item))))
    carrier_ids = _ids(payload, "domain_carrier_leads")
    return unit_ids, carrier_ids


def validate_packets(packets: list[tuple[str, dict[str, Any]]]) -> list[str]:
    errors: list[str] = []
    if len(packets) < 2:
        return ["at least two topic packets are required"]
    groups: dict[tuple[tuple[str, ...], tuple[str, ...]], list[tuple[str, dict[str, Any]]]] = {}
    for name, payload in packets:
        signature = packet_signature(payload)
        if not signature[0]:
            errors.append(f"{name}: selected/activated unit list is empty")
        groups.setdefault(signature, []).append((name, payload))
    for signature, members in groups.items():
        if len(members) < 2:
            continue
        undocumented = []
        for name, payload in members:
            delta = payload.get("cross_topic_delta") or payload.get("topic_specific_compilation")
            chain_tasks = payload.get("ten_god_chain_contribution_tasks")
            if not delta or not chain_tasks:
                undocumented.append(name)
        if undocumented:
            errors.append(
                "identical topic packet signature without both cross-topic delta and ten-god-chain tasks: "
                + ", ".join(undocumented)
                + f"; units={len(signature[0])}, carrier_leads={len(signature[1])}"
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packets", nargs="+", type=Path)
    args = parser.parse_args()
    loaded: list[tuple[str, dict[str, Any]]] = []
    try:
        for path in args.packets:
            payload = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(payload, dict):
                raise ValueError(f"{path}: root must be an object")
            loaded.append((str(path), payload))
        errors = validate_packets(loaded)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "FAIL", "errors": [str(exc)]}, ensure_ascii=False, indent=2))
        return 2
    print(json.dumps({"status": "PASS" if not errors else "FAIL", "errors": errors}, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
