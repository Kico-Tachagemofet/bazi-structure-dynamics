#!/usr/bin/env python3
"""Validate the Deep Card compilation firewall without interpreting imagery."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


UNIT_CLASSES = {
    "semantic_core", "state_modifier", "symbol_carrier", "relational_carrier",
    "composite_domain_carrier", "cross_system_context",
}
SELECTABLE_CLASSES = {"semantic_core", "state_modifier", "symbol_carrier", "relational_carrier"}
CLAIM_CEILINGS = {"mechanism", "candidate"}
PALETTE_LEVELS = {"L2-domain-nature", "L3-action-material", "L4-carrier-family"}
FORBIDDEN_RUNTIME_KEYS = {
    "card_path", "raw_card_path", "raw_card_text", "full_card_text", "full_card_content",
    "context_only_payload", "forbidden_payload", "bridge_status", "claim_strength", "carrier_rank",
}


def _need(obj: dict[str, Any], fields: set[str], label: str, errors: list[str]) -> None:
    missing = sorted(fields - set(obj))
    if missing:
        errors.append(f"{label}: missing {', '.join(missing)}")


def _scan_forbidden_keys(value: Any, path: str, errors: list[str]) -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            child = f"{path}.{key}" if path else key
            if key in FORBIDDEN_RUNTIME_KEYS:
                errors.append(f"runtime packet: forbidden field {child}")
            _scan_forbidden_keys(item, child, errors)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _scan_forbidden_keys(item, f"{path}[{index}]", errors)


def _nonempty_list(value: Any) -> bool:
    return isinstance(value, list) and bool(value)


def validate_packet(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = {
        "schema_version", "case_id", "topic_id", "structure_freeze_id", "topic_lens_ref",
        "source_packet_ref", "raw_card_access", "composition_access", "render_access",
        "raw_card_forwarded", "context_only_payload_forwarded", "query_receipts",
        "selected_units", "candidate_palette", "domain_carrier_leads",
    }
    _need(payload, required, "packet", errors)
    if errors:
        return errors

    if payload.get("schema_version") != "1.1":
        errors.append("packet: schema_version must be 1.1")
    if payload.get("raw_card_access") != "source-lookup-only":
        errors.append("packet: raw_card_access must be source-lookup-only")
    if payload.get("composition_access") != "compiled-units-only":
        errors.append("packet: composition_access must be compiled-units-only")
    if payload.get("render_access") != "none":
        errors.append("packet: render_access must be none")
    if payload.get("raw_card_forwarded") is not False:
        errors.append("packet: raw_card_forwarded must be false")
    if payload.get("context_only_payload_forwarded") is not False:
        errors.append("packet: context_only_payload_forwarded must be false")

    _scan_forbidden_keys(payload, "", errors)

    receipts = payload.get("query_receipts")
    if not isinstance(receipts, list) or not receipts:
        errors.append("query_receipts: must be a non-empty list")
        receipts = []
    receipt_by_query: dict[str, dict[str, Any]] = {}
    selected_ids_from_receipts: set[str] = set()
    for receipt in receipts:
        if not isinstance(receipt, dict):
            errors.append("query_receipts: each receipt must be an object")
            continue
        _need(
            receipt,
            {
                "query_id", "card_id", "full_read_receipt_ref", "requested_unit_classes",
                "selection_purpose", "selection_basis_refs", "topic_claim_ceiling",
                "selected_unit_ids", "context_only_unit_ids", "forbidden_unit_ids",
                "source_gap_unit_ids", "excluded_unit_ids", "raw_card_text_forwarded",
            },
            "query_receipt",
            errors,
        )
        query_id = receipt.get("query_id")
        if not isinstance(query_id, str) or not query_id:
            errors.append("query_receipt: query_id must be a non-empty string")
            continue
        if query_id in receipt_by_query:
            errors.append(f"query_receipts: duplicate query_id {query_id}")
        receipt_by_query[query_id] = receipt
        requested = receipt.get("requested_unit_classes")
        if not _nonempty_list(requested):
            errors.append(f"query_receipt {query_id}: requested_unit_classes must be non-empty")
        else:
            unknown = sorted(set(requested) - UNIT_CLASSES)
            if unknown:
                errors.append(f"query_receipt {query_id}: unknown unit classes {unknown}")
        if not receipt.get("selection_purpose") or not _nonempty_list(receipt.get("selection_basis_refs")):
            errors.append(f"query_receipt {query_id}: selection purpose and basis refs are required")
        if receipt.get("topic_claim_ceiling") not in CLAIM_CEILINGS:
            errors.append(f"query_receipt {query_id}: invalid topic_claim_ceiling")
        if receipt.get("raw_card_text_forwarded") is not False:
            errors.append(f"query_receipt {query_id}: raw_card_text_forwarded must be false")
        buckets: list[set[str]] = []
        for field in {
            "selected_unit_ids", "context_only_unit_ids", "forbidden_unit_ids",
            "source_gap_unit_ids", "excluded_unit_ids",
        }:
            value = receipt.get(field)
            if not isinstance(value, list):
                errors.append(f"query_receipt {query_id}: {field} must be a list")
                value = []
            bucket = set(value)
            if len(bucket) != len(value):
                errors.append(f"query_receipt {query_id}: {field} contains duplicates")
            for previous in buckets:
                overlap = sorted(bucket & previous)
                if overlap:
                    errors.append(f"query_receipt {query_id}: unit permission buckets overlap {overlap}")
            buckets.append(bucket)
            if field == "selected_unit_ids":
                selected_ids_from_receipts |= bucket

    units = payload.get("selected_units")
    if not isinstance(units, list):
        errors.append("selected_units: must be a list")
        units = []
    unit_ids: set[str] = set()
    required_unit_fields = {
        "runtime_unit_id", "authoring_unit_id", "query_ref", "card_id", "unit_class", "topic_axis", "semantic_payload",
        "derivation_path", "state_switches", "activation_requirements", "activation_basis_refs",
        "allowed_topics", "claim_ceiling", "forbidden_promotions", "source_layer",
        "source_receipt_refs", "candidate_carriers", "alternative_carriers", "mechanism_trace",
    }
    for unit in units:
        if not isinstance(unit, dict):
            errors.append("selected_units: each unit must be an object")
            continue
        _need(unit, required_unit_fields, "selected_unit", errors)
        unit_id = unit.get("runtime_unit_id")
        if not isinstance(unit_id, str) or not unit_id:
            errors.append("selected_unit: runtime_unit_id must be a non-empty string")
            continue
        if unit_id in unit_ids:
            errors.append(f"selected_units: duplicate unit_id {unit_id}")
        unit_ids.add(unit_id)
        if not isinstance(unit.get("authoring_unit_id"), str) or not unit.get("authoring_unit_id"):
            errors.append(f"selected_unit {unit_id}: authoring_unit_id must be a non-empty string")
        query_ref = unit.get("query_ref")
        receipt = receipt_by_query.get(query_ref)
        if receipt is None:
            errors.append(f"selected_unit {unit_id}: unknown query_ref {query_ref}")
        else:
            if unit_id not in set(receipt.get("selected_unit_ids", [])):
                errors.append(f"selected_unit {unit_id}: missing from query receipt selected_unit_ids")
            if unit.get("card_id") != receipt.get("card_id"):
                errors.append(f"selected_unit {unit_id}: card_id differs from query receipt")
            if unit.get("unit_class") not in set(receipt.get("requested_unit_classes", [])):
                errors.append(f"selected_unit {unit_id}: unit_class was not requested")
        unit_class = unit.get("unit_class")
        if unit_class not in SELECTABLE_CLASSES:
            errors.append(f"selected_unit {unit_id}: unit_class {unit_class} cannot be forwarded")
        ceiling = unit.get("claim_ceiling")
        if ceiling not in CLAIM_CEILINGS:
            errors.append(f"selected_unit {unit_id}: claim_ceiling must be mechanism or candidate")
        if unit_class in {"semantic_core", "state_modifier"} and ceiling != "mechanism":
            errors.append(f"selected_unit {unit_id}: {unit_class} ceiling must be mechanism")
        if unit_class in {"symbol_carrier", "relational_carrier"} and ceiling != "candidate":
            errors.append(f"selected_unit {unit_id}: {unit_class} ceiling must be candidate")
        semantic_payload = unit.get("semantic_payload")
        if semantic_payload is None or semantic_payload == "" or semantic_payload == [] or semantic_payload == {}:
            errors.append(f"selected_unit {unit_id}: semantic_payload cannot be empty")
        for field in {
            "activation_requirements", "activation_basis_refs", "allowed_topics",
            "forbidden_promotions", "source_receipt_refs",
        }:
            if not _nonempty_list(unit.get(field)):
                errors.append(f"selected_unit {unit_id}: {field} must be a non-empty list")
        for field in {"candidate_carriers", "alternative_carriers"}:
            if not isinstance(unit.get(field), list):
                errors.append(f"selected_unit {unit_id}: {field} must be a list")
        if not unit.get("derivation_path") or not unit.get("mechanism_trace"):
            errors.append(f"selected_unit {unit_id}: derivation_path and mechanism_trace are required")

    if unit_ids != selected_ids_from_receipts:
        missing = sorted(selected_ids_from_receipts - unit_ids)
        extra = sorted(unit_ids - selected_ids_from_receipts)
        errors.append(f"selected_units: receipt mismatch missing={missing} extra={extra}")

    palette = payload.get("candidate_palette")
    if not isinstance(palette, list) or not palette:
        errors.append("candidate_palette: must be a non-empty list in v1.1")
        palette = []
    palette_ids: set[str] = set()
    for item in palette:
        if not isinstance(item, dict):
            errors.append("candidate_palette: each item must be an object")
            continue
        _need(
            item,
            {
                "palette_item_id", "judgment_dimension_refs", "specificity_level",
                "nature_action_material_or_family", "contributing_selected_unit_refs",
                "activation_anchor_refs", "post_relation_state_refs",
                "ten_god_chain_contribution", "compatible_carrier_families",
                "competing_palette_item_ids", "claim_ceiling", "not_a_finding",
            },
            "candidate_palette_item",
            errors,
        )
        palette_id = item.get("palette_item_id")
        if not isinstance(palette_id, str) or not palette_id or palette_id in palette_ids:
            errors.append("candidate_palette_item.palette_item_id: must be non-empty and unique")
            continue
        palette_ids.add(palette_id)
        if item.get("specificity_level") not in PALETTE_LEVELS:
            errors.append(f"candidate_palette_item {palette_id}: invalid specificity_level")
        for field in {
            "judgment_dimension_refs", "contributing_selected_unit_refs",
            "activation_anchor_refs", "post_relation_state_refs",
        }:
            if not _nonempty_list(item.get(field)):
                errors.append(f"candidate_palette_item {palette_id}: {field} must be non-empty")
        unknown = sorted(set(item.get("contributing_selected_unit_refs", [])) - unit_ids)
        if unknown:
            errors.append(f"candidate_palette_item {palette_id}: unknown selected unit refs {unknown}")
        for field in {"compatible_carrier_families", "competing_palette_item_ids"}:
            if not isinstance(item.get(field), list):
                errors.append(f"candidate_palette_item {palette_id}: {field} must be a list")
        if not item.get("nature_action_material_or_family") or not item.get("ten_god_chain_contribution"):
            errors.append(f"candidate_palette_item {palette_id}: semantic contribution cannot be empty")
        if item.get("claim_ceiling") != "candidate" or item.get("not_a_finding") is not True:
            errors.append(f"candidate_palette_item {palette_id}: must remain candidate and not_a_finding")

    for item in palette:
        if not isinstance(item, dict):
            continue
        unknown_competitors = sorted(set(item.get("competing_palette_item_ids", [])) - palette_ids)
        if unknown_competitors:
            errors.append(f"candidate_palette_item {item.get('palette_item_id')}: unknown competitors {unknown_competitors}")

    leads = payload.get("domain_carrier_leads")
    if not isinstance(leads, list):
        errors.append("domain_carrier_leads: must be a list")
        leads = []
    lead_ids: set[str] = set()
    for lead in leads:
        if not isinstance(lead, dict):
            errors.append("domain_carrier_leads: each lead must be an object")
            continue
        _need(
            lead,
            {
                "lead_id", "domain_request_ref", "label", "carrier_family",
                "contributing_selected_unit_refs", "source_receipt_refs", "source_support_scope",
                "claim_ceiling", "not_a_finding",
            },
            "domain_carrier_lead",
            errors,
        )
        lead_id = lead.get("lead_id")
        if not isinstance(lead_id, str) or not lead_id:
            errors.append("domain_carrier_lead: lead_id must be a non-empty string")
            continue
        if lead_id in lead_ids:
            errors.append(f"domain_carrier_leads: duplicate lead_id {lead_id}")
        lead_ids.add(lead_id)
        if not lead.get("domain_request_ref") or not lead.get("label") or not lead.get("carrier_family"):
            errors.append(f"domain_carrier_lead {lead_id}: request, label, and family are required")
        contributions = lead.get("contributing_selected_unit_refs")
        if not _nonempty_list(contributions):
            errors.append(f"domain_carrier_lead {lead_id}: contributing_selected_unit_refs must be non-empty")
        else:
            unknown = sorted(set(contributions) - unit_ids)
            if unknown:
                errors.append(f"domain_carrier_lead {lead_id}: unknown selected unit refs {unknown}")
        if not _nonempty_list(lead.get("source_receipt_refs")):
            errors.append(f"domain_carrier_lead {lead_id}: source_receipt_refs must be non-empty")
        if lead.get("claim_ceiling") != "candidate":
            errors.append(f"domain_carrier_lead {lead_id}: claim_ceiling must be candidate")
        if lead.get("not_a_finding") is not True:
            errors.append(f"domain_carrier_lead {lead_id}: not_a_finding must be true")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a compiled Deep Card runtime packet.")
    parser.add_argument("packet")
    args = parser.parse_args()
    path = Path(args.packet)
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        errors = validate_packet(payload)
    except (OSError, json.JSONDecodeError) as exc:
        errors = [f"packet unreadable: {exc}"]
    result = {
        "verdict": "PASS" if not errors else "FAIL",
        "packet": str(path),
        "errors": errors,
        "boundary": "Compilation and access validation only; imagery meaning and carrier ranking remain analytical judgments.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
