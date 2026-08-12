#!/usr/bin/env python3
"""Self-test the Deep Card runtime compilation firewall."""

from __future__ import annotations

from copy import deepcopy

from validate_deep_card_runtime_packet import validate_packet


def valid_packet():
    return {
        "schema_version": "1.1",
        "case_id": "fixture",
        "topic_id": "career-work",
        "structure_freeze_id": "FRZ-1",
        "topic_lens_ref": "topic-lens-career-work.json",
        "source_packet_ref": "imagery-source-packet-career-work.md",
        "raw_card_access": "source-lookup-only",
        "composition_access": "compiled-units-only",
        "render_access": "none",
        "raw_card_forwarded": False,
        "context_only_payload_forwarded": False,
        "query_receipts": [{
            "query_id": "DCQ-JIA",
            "card_id": "DC-STEM-JIA",
            "full_read_receipt_ref": "imagery-source-packet-career-work.md#READ-JIA",
            "requested_unit_classes": ["semantic_core"],
            "selection_purpose": "explain work initiation property",
            "selection_basis_refs": ["TPA-1", "PROC-1"],
            "topic_claim_ceiling": "mechanism",
            "selected_unit_ids": ["DCQ-JIA::JIA-WORK-GROWTH"],
            "context_only_unit_ids": ["JIA-ORDINAL-FIRST"],
            "forbidden_unit_ids": ["JIA-CROSS-QIMEN"],
            "source_gap_unit_ids": [],
            "excluded_unit_ids": ["JIA-SHAPE-LONG", "JIA-MATERIAL-WOOD"],
            "raw_card_text_forwarded": False,
        }],
        "selected_units": [{
            "runtime_unit_id": "DCQ-JIA::JIA-WORK-GROWTH",
            "authoring_unit_id": "JIA-WORK-GROWTH",
            "query_ref": "DCQ-JIA",
            "card_id": "DC-STEM-JIA",
            "unit_class": "semantic_core",
            "topic_axis": "career_work",
            "semantic_payload": "发起、培育、建立主线和推动成长的工作性质。",
            "derivation_path": "曲直与生气发动在相关职业轴上的过程投影",
            "state_switches": ["有根且路线可持续时才形成长期推动"],
            "activation_requirements": ["甲参与已冻结职业轴"],
            "activation_basis_refs": ["TPA-1", "PROC-1"],
            "allowed_topics": ["career_work", "learning_cognition"],
            "claim_ceiling": "mechanism",
            "forbidden_promotions": ["teacher", "leader", "specific_job"],
            "source_layer": "current_synthesis",
            "source_receipt_refs": ["READ-JIA"],
            "candidate_carriers": [],
            "alternative_carriers": [],
            "mechanism_trace": "只解释冻结路线怎样表现为发起与培育，不生成职业结论。",
        }],
        "candidate_palette": [{
            "palette_item_id": "PAL-TECH-NATURE",
            "judgment_dimension_refs": ["occupational-nature"],
            "specificity_level": "L2-domain-nature",
            "nature_action_material_or_family": "培育、建立主线与长期推动",
            "contributing_selected_unit_refs": ["DCQ-JIA::JIA-WORK-GROWTH"],
            "activation_anchor_refs": ["TPA-1", "PROC-1"],
            "post_relation_state_refs": ["post-node-01"],
            "ten_god_chain_contribution": "把已冻结职业轴的发动功能具体化",
            "compatible_carrier_families": ["education", "project-development"],
            "competing_palette_item_ids": [],
            "claim_ceiling": "candidate",
            "not_a_finding": True,
        }],
        "domain_carrier_leads": [],
    }


def main() -> None:
    packet = valid_packet()
    assert validate_packet(packet) == []

    broken = deepcopy(packet)
    broken["raw_card_forwarded"] = True
    assert any("raw_card_forwarded must be false" in error for error in validate_packet(broken))

    broken = deepcopy(packet)
    broken["selected_units"][0]["context_only_payload"] = "领导、教育"
    assert any("forbidden field" in error for error in validate_packet(broken))

    broken = deepcopy(packet)
    broken["selected_units"][0]["unit_class"] = "composite_domain_carrier"
    assert any("cannot be forwarded" in error for error in validate_packet(broken))

    broken = deepcopy(packet)
    broken["selected_units"][0]["claim_strength"] = "supported"
    assert any("forbidden field" in error for error in validate_packet(broken))

    broken = deepcopy(packet)
    broken["query_receipts"][0]["context_only_unit_ids"].append("DCQ-JIA::JIA-WORK-GROWTH")
    assert any("permission buckets overlap" in error for error in validate_packet(broken))

    with_lead = deepcopy(packet)
    with_lead["domain_carrier_leads"] = [{
        "lead_id": "DCL-EDUCATION",
        "domain_request_ref": "DCR-1",
        "label": "教育／培养类工作",
        "carrier_family": "career",
        "contributing_selected_unit_refs": ["DCQ-JIA::JIA-WORK-GROWTH"],
        "source_receipt_refs": ["READ-JIA"],
        "source_support_scope": "candidate lead only; needs relation, position, route and result gates",
        "claim_ceiling": "candidate",
        "not_a_finding": True,
    }]
    assert validate_packet(with_lead) == []

    print("PASS: Deep Card runtime packet preserves an open candidate palette while reserving ranking for Composition")


if __name__ == "__main__":
    main()
