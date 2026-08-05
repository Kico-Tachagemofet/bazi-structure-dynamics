#!/usr/bin/env python3
"""Self-test route integrity validator, including deliberate endpoint drift."""

from validate_route_integrity import validate


EDGE_MAP = """
qualified_edges:
  - edge_id: "E1"
    source_node: "A"
    target_node: "B"
    action: "生"
    edge_layer: "direct-action"
    distance_and_order: "near"
  - edge_id: "E2"
    source_node: "B"
    target_node: "C"
    action: "生"
    edge_layer: "direct-action"
    distance_and_order: "near"
"""

GOOD = """
routes:
  - route_id: "R1"
    edge_refs: ["E1", "E2"]
    topology: "chain"
    net_effect_on_primary_problem: "therapeutic"
    therapeutic_priority: "1"
    outlet_eligible: true
"""

BAD_DRIFT = """
routes:
  - route_id: "R2"
    edge_refs: ["E1", "E2"]
    topology: "chain"
    source_node: "WRONG"
    net_effect_on_primary_problem: "aggravating"
    therapeutic_priority: "1"
    outlet_eligible: true
"""


def main() -> None:
    good = validate(EDGE_MAP, GOOD)
    bad = validate(EDGE_MAP, BAD_DRIFT)
    assert good["verdict"] == "PASS", good
    assert bad["verdict"] == "FAIL", bad
    assert any("duplicates endpoint" in item for item in bad["blockers"]), bad
    assert any("cannot be an outlet" in item for item in bad["blockers"]), bad
    assert any("cannot have therapeutic priority" in item for item in bad["blockers"]), bad
    print("PASS: route integrity accepts locked refs and rejects endpoint/priority drift")


if __name__ == "__main__":
    main()
