#!/usr/bin/env python3
"""Self-test the conditional rule registry validator."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

from validate_rule_registry import validate_registry


def main() -> None:
    skill_root = Path(__file__).resolve().parents[1]
    project_root = Path(__file__).resolve().parents[3]
    registry = skill_root / "references" / "rule-registry-qianli-high-risk.json"

    assert validate_registry(registry, project_root) == []

    payload = json.loads(registry.read_text(encoding="utf-8"))
    payload["cards"][0]["rule_summary"] = "阳干绝不克阴干。"
    payload["cards"][0]["auto_application"] = True
    with tempfile.TemporaryDirectory() as temp:
        broken = Path(temp) / "broken.json"
        broken.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        errors = validate_registry(broken, project_root)
    assert any("absolute term" in error for error in errors)
    assert any("interpretive rule cards cannot auto-apply" in error for error in errors)

    print("PASS: rule registry preserves qualifiers, taiji boundaries, source spans, and review gates")


if __name__ == "__main__":
    main()
