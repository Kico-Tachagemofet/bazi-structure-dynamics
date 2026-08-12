#!/usr/bin/env python3
"""Validate Bazi scene-kernel structure and runtime-unit disposition closure."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterable


RELATIONS = {"reinforces", "specifies", "carries", "limits", "diverts", "competes", "contradicts", "context-only"}
RAW_KEYS = {"raw_card", "raw_card_text", "mother_card_text", "full_card_payload", "context_only_payload"}
SPECIFICITY_LEVELS = {"L1-outcome-level", "L2-domain-nature", "L3-action-material", "L4-carrier-family", "L5-exact-identity-event"}
DISPOSITIONS = {"directional-verdict", "not-applicable", "source-gap", "not-claimed"}
UNIT_DISPOSITIONS = {"used", "counterevidence", "context-only", "excluded-with-reason"}


def _need(obj: Any, fields: Iterable[str], label: str, errors: list[str]) -> None:
    if not isinstance(obj, dict):
        errors.append(f"{label}: must be an object")
        return
    missing = [field for field in fields if field not in obj]
    if missing:
        errors.append(f"{label}: missing {', '.join(missing)}")


def _walk(value: Any, path: str = "$"):
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            yield child_path, key, child
            yield from _walk(child, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from _walk(child, f"{path}[{index}]")


def _text(value: Any) -> bool:
    return isinstance(value, str) and len(value.strip()) >= 6


def _list(value: Any) -> bool:
    return isinstance(value, list) and bool(value)


def _runtime_unit_ids(packet: Any, label: str, errors: list[str]) -> list[str]:
    if not isinstance(packet, dict) or not isinstance(packet.get("selected_units"), list):
        errors.append(f"{label}: runtime packet needs selected_units")
        return []
    result: list[str] = []
    for index, unit in enumerate(packet["selected_units"]):
        if not isinstance(unit, dict):
            errors.append(f"{label}.selected_units[{index}]: must be an object")
            continue
        unit_id = unit.get("runtime_unit_id") or unit.get("unit_id")
        if not isinstance(unit_id, str) or not unit_id.strip():
            errors.append(f"{label}.selected_units[{index}]: missing runtime_unit_id/unit_id")
            continue
        result.append(unit_id.strip())
    if len(result) != len(set(result)):
        errors.append(f"{label}.selected_units: unit IDs must be unique")
    return result


def _resolve_runtime_packet(ref: str, kernel_path: Path, runtime_root: Path | None) -> Path | None:
    clean_ref = ref.split("#", 1)[0]
    direct = Path(clean_ref)
    candidates: list[Path] = []
    if direct.is_absolute():
        candidates.append(direct)
    else:
        candidates.append((kernel_path.parent / direct).resolve())
        if runtime_root is not None:
            candidates.append((runtime_root / direct).resolve())
            if direct.name:
                matches = list(runtime_root.rglob(direct.name))
                if len(matches) == 1:
                    candidates.append(matches[0].resolve())
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return None


def validate(payload: Any, kernel_path: Path, runtime_root: Path | None = None) -> tuple[list[str], list[dict[str, Any]]]:
    errors: list[str] = []
    coverage_results: list[dict[str, Any]] = []
    if isinstance(payload, dict) and "kernels" in payload:
        kernels = payload["kernels"]
    elif isinstance(payload, list):
        kernels = payload
    else:
        errors.append("root: must be a kernel list or an object with kernels")
        return errors, coverage_results
    if not isinstance(kernels, list) or not kernels:
        errors.append("kernels: must be a non-empty list")
        return errors, coverage_results

    kernel_ids: set[str] = set()
    for index, kernel in enumerate(kernels):
        label = f"kernels[{index}]"
        _need(
            kernel,
            {
                "kernel_id", "topic_id", "taiji_center", "process_refs", "phase_focus_refs",
                "topic_process_axis_refs", "ten_god_chain", "stem_branch_composition",
                "material_spread_receipt", "composition_relations",
                "mandatory_judgment_dimension_refs", "claim_kernels", "main_scene",
                "secondary_scene", "switch_scene", "nonmanifestation_scene",
                "distinctive_detail_palette", "candidate_carriers_ranked",
                "strongest_alternative", "do_not_render", "confidence",
            },
            label,
            errors,
        )
        if not isinstance(kernel, dict):
            continue
        kernel_id = str(kernel.get("kernel_id", "")).strip()
        if not kernel_id or kernel_id in kernel_ids:
            errors.append(f"{label}.kernel_id: must be non-empty and unique")
        kernel_ids.add(kernel_id)
        for key in ("process_refs", "phase_focus_refs", "topic_process_axis_refs"):
            if not _list(kernel.get(key)):
                errors.append(f"{label}.{key}: must be a non-empty list")
        if not _text(kernel.get("taiji_center")):
            errors.append(f"{label}.taiji_center: must name a real person/matter/result field")

        chain = kernel.get("ten_god_chain")
        _need(
            chain,
            {
                "body_or_subject", "start_node_and_agency", "ordered_relation_functions",
                "result_endpoint", "feedback_to_daymaster", "competing_uses",
                "agency", "reversal_gate",
            },
            f"{label}.ten_god_chain",
            errors,
        )
        if isinstance(chain, dict):
            if not _text(chain.get("body_or_subject")):
                errors.append(f"{label}.ten_god_chain.body_or_subject: cannot be generic or empty")
            if not _list(chain.get("ordered_relation_functions")):
                errors.append(f"{label}.ten_god_chain.ordered_relation_functions: cannot be empty")
            for key in ("start_node_and_agency", "result_endpoint", "feedback_to_daymaster", "reversal_gate"):
                if not chain.get(key):
                    errors.append(f"{label}.ten_god_chain.{key}: cannot be empty")
            agency = chain.get("agency")
            _need(agency, {"can_start", "can_carry", "can_redirect", "can_stop"}, f"{label}.ten_god_chain.agency", errors)

        composition = kernel.get("stem_branch_composition")
        _need(
            composition,
            {
                "exposed_stems", "branch_fields", "hidden_stem_layers", "pillar_roles",
                "same_pillar_coloring", "cross_pillar_transfer",
            },
            f"{label}.stem_branch_composition",
            errors,
        )
        if isinstance(composition, dict):
            if not _list(composition.get("branch_fields")):
                errors.append(f"{label}.stem_branch_composition.branch_fields: cannot be empty")
            if not (_list(composition.get("exposed_stems")) or _list(composition.get("hidden_stem_layers"))):
                errors.append(f"{label}.stem_branch_composition: needs stem participation")
            if not _list(composition.get("pillar_roles")):
                errors.append(f"{label}.stem_branch_composition.pillar_roles: cannot be empty")

        receipt = kernel.get("material_spread_receipt")
        _need(
            receipt,
            {
                "runtime_packet_ref", "selected_unit_ids", "unit_dispositions", "source_refs",
                "excluded_unit_receipts", "coverage_validator_receipt_ref",
            },
            f"{label}.material_spread_receipt",
            errors,
        )
        if isinstance(receipt, dict):
            if not _list(receipt.get("selected_unit_ids")) or not _list(receipt.get("source_refs")):
                errors.append(f"{label}.material_spread_receipt: selected units and source refs cannot be empty")
            if "all_chain_links_covered" in receipt:
                errors.append(f"{label}.material_spread_receipt.all_chain_links_covered: producer self-attestation is prohibited")
            if not _text(receipt.get("coverage_validator_receipt_ref")):
                errors.append(f"{label}.material_spread_receipt.coverage_validator_receipt_ref: required")

        relations = kernel.get("composition_relations")
        if not isinstance(relations, list) or not relations:
            errors.append(f"{label}.composition_relations: must be a non-empty list")
        else:
            for relation_index, relation in enumerate(relations):
                if not isinstance(relation, dict):
                    errors.append(f"{label}.composition_relations[{relation_index}]: must be an object")
                    continue
                _need(relation, {"from_ref", "to_ref", "interaction_type", "chain_position", "effect"}, f"{label}.composition_relations[{relation_index}]", errors)
                if relation.get("interaction_type") not in RELATIONS:
                    errors.append(f"{label}.composition_relations[{relation_index}].interaction_type: invalid")

        dimension_refs = kernel.get("mandatory_judgment_dimension_refs")
        if not _list(dimension_refs) or len(set(dimension_refs)) != len(dimension_refs):
            errors.append(f"{label}.mandatory_judgment_dimension_refs: must be a non-empty unique list")
            dimension_refs = []
        claims = kernel.get("claim_kernels")
        if not isinstance(claims, list) or not claims:
            errors.append(f"{label}.claim_kernels: must be a non-empty list")
            claims = []
        claim_ids: set[str] = set()
        covered_dimensions: set[str] = set()
        for claim_index, claim in enumerate(claims):
            claim_label = f"{label}.claim_kernels[{claim_index}]"
            _need(
                claim,
                {
                    "claim_kernel_id", "judgment_dimension_ref", "claim_endpoint_id",
                    "specificity_level", "disposition", "directional_verdict", "claim_strength",
                    "support_refs", "counterevidence_refs", "result_gate", "reversal_condition",
                    "daymaster_cost_ref", "competing_claim_or_carrier_refs", "support_unit_refs",
                    "counterevidence_unit_refs", "counterevidence_check",
                },
                claim_label,
                errors,
            )
            if not isinstance(claim, dict):
                continue
            claim_id = claim.get("claim_kernel_id")
            if not isinstance(claim_id, str) or not claim_id or claim_id in claim_ids:
                errors.append(f"{claim_label}.claim_kernel_id: must be non-empty and unique")
            claim_ids.add(claim_id)
            dimension_ref = claim.get("judgment_dimension_ref")
            if dimension_ref not in dimension_refs:
                errors.append(f"{claim_label}.judgment_dimension_ref: unknown dimension")
            else:
                covered_dimensions.add(dimension_ref)
            if claim.get("specificity_level") not in SPECIFICITY_LEVELS:
                errors.append(f"{claim_label}.specificity_level: invalid")
            disposition = claim.get("disposition")
            if disposition not in DISPOSITIONS:
                errors.append(f"{claim_label}.disposition: invalid")
            if disposition == "directional-verdict":
                if not _text(claim.get("directional_verdict")) or not claim.get("claim_strength"):
                    errors.append(f"{claim_label}: directional verdict needs substantive text and strength")
                if not _list(claim.get("support_refs")):
                    errors.append(f"{claim_label}.support_refs: directional verdict needs support")
                if not _list(claim.get("support_unit_refs")):
                    errors.append(f"{claim_label}.support_unit_refs: directional verdict needs runtime-unit support")
                if not isinstance(claim.get("counterevidence_unit_refs"), list):
                    errors.append(f"{claim_label}.counterevidence_unit_refs: must be a list")
                if not _text(claim.get("counterevidence_check")):
                    errors.append(f"{claim_label}.counterevidence_check: must record the opposing-material check")
            elif not _text(claim.get("directional_verdict")):
                errors.append(f"{claim_label}: non-directional disposition needs a concrete reason")
        missing_dimensions = sorted(set(dimension_refs) - covered_dimensions)
        if missing_dimensions:
            errors.append(f"{label}.claim_kernels: dimensions lack claims {missing_dimensions}")

        if isinstance(receipt, dict):
            runtime_ref = receipt.get("runtime_packet_ref")
            runtime_path = _resolve_runtime_packet(runtime_ref, kernel_path, runtime_root) if isinstance(runtime_ref, str) else None
            runtime_ids: list[str] = []
            if runtime_path is None:
                errors.append(f"{label}.material_spread_receipt.runtime_packet_ref: cannot resolve {runtime_ref!r}")
            else:
                try:
                    runtime_ids = _runtime_unit_ids(_load(runtime_path), str(runtime_path), errors)
                except (OSError, ValueError, json.JSONDecodeError) as exc:
                    errors.append(f"{label}.material_spread_receipt.runtime_packet_ref: {exc}")

            selected_ids = receipt.get("selected_unit_ids") if isinstance(receipt.get("selected_unit_ids"), list) else []
            if len(selected_ids) != len(set(selected_ids)):
                errors.append(f"{label}.material_spread_receipt.selected_unit_ids: duplicates are prohibited")
            if runtime_ids and set(selected_ids) != set(runtime_ids):
                missing = sorted(set(runtime_ids) - set(selected_ids))
                extra = sorted(set(selected_ids) - set(runtime_ids))
                errors.append(f"{label}.material_spread_receipt: runtime set mismatch missing={missing} extra={extra}")

            rows = receipt.get("unit_dispositions")
            disposition_by_id: dict[str, dict[str, Any]] = {}
            if not isinstance(rows, list) or not rows:
                errors.append(f"{label}.material_spread_receipt.unit_dispositions: must be a non-empty list")
                rows = []
            for row_index, row in enumerate(rows):
                row_label = f"{label}.material_spread_receipt.unit_dispositions[{row_index}]"
                _need(row, {"unit_id", "disposition", "claim_kernel_refs", "reason"}, row_label, errors)
                if not isinstance(row, dict):
                    continue
                unit_id = row.get("unit_id")
                if not isinstance(unit_id, str) or not unit_id:
                    errors.append(f"{row_label}.unit_id: required")
                    continue
                if unit_id in disposition_by_id:
                    errors.append(f"{row_label}.unit_id: duplicate disposition for {unit_id}")
                disposition_by_id[unit_id] = row
                disposition = row.get("disposition")
                if disposition not in UNIT_DISPOSITIONS:
                    errors.append(f"{row_label}.disposition: invalid")
                refs = row.get("claim_kernel_refs")
                if not isinstance(refs, list):
                    errors.append(f"{row_label}.claim_kernel_refs: must be a list")
                    refs = []
                unknown_claims = sorted(set(refs) - claim_ids)
                if unknown_claims:
                    errors.append(f"{row_label}.claim_kernel_refs: unknown claims {unknown_claims}")
                if disposition in {"used", "counterevidence"} and not refs:
                    errors.append(f"{row_label}: used/counterevidence units must link claims")
                if disposition in {"context-only", "excluded-with-reason"} and not _text(row.get("reason")):
                    errors.append(f"{row_label}.reason: context/excluded disposition needs a concrete reason")

            if runtime_ids and set(disposition_by_id) != set(runtime_ids):
                missing = sorted(set(runtime_ids) - set(disposition_by_id))
                extra = sorted(set(disposition_by_id) - set(runtime_ids))
                errors.append(f"{label}.material_spread_receipt.unit_dispositions: runtime set mismatch missing={missing} extra={extra}")

            for claim_index, claim in enumerate(claims):
                if not isinstance(claim, dict):
                    continue
                claim_id = claim.get("claim_kernel_id")
                support_units = claim.get("support_unit_refs") if isinstance(claim.get("support_unit_refs"), list) else []
                counter_units = claim.get("counterevidence_unit_refs") if isinstance(claim.get("counterevidence_unit_refs"), list) else []
                for unit_id in support_units:
                    row = disposition_by_id.get(unit_id)
                    if row is None or row.get("disposition") != "used" or claim_id not in row.get("claim_kernel_refs", []):
                        errors.append(f"{label}.claim_kernels[{claim_index}].support_unit_refs: {unit_id} lacks matching used disposition")
                for unit_id in counter_units:
                    row = disposition_by_id.get(unit_id)
                    if row is None or row.get("disposition") != "counterevidence" or claim_id not in row.get("claim_kernel_refs", []):
                        errors.append(f"{label}.claim_kernels[{claim_index}].counterevidence_unit_refs: {unit_id} lacks matching counterevidence disposition")

            coverage_results.append({
                "kernel_id": kernel_id,
                "runtime_packet": str(runtime_path) if runtime_path else None,
                "runtime_unit_count": len(runtime_ids),
                "selected_unit_count": len(selected_ids),
                "disposition_count": len(disposition_by_id),
                "runtime_set_equal": bool(runtime_ids) and set(runtime_ids) == set(selected_ids) == set(disposition_by_id),
            })

        for key in ("main_scene", "secondary_scene", "switch_scene", "nonmanifestation_scene", "strongest_alternative"):
            if not _text(kernel.get(key)):
                errors.append(f"{label}.{key}: must be a concrete scene, not an empty label")
        if not _list(kernel.get("distinctive_detail_palette")):
            errors.append(f"{label}.distinctive_detail_palette: needs chart-specific details")
        if not isinstance(kernel.get("do_not_render"), list):
            errors.append(f"{label}.do_not_render: must be a list")

        for path, key, _ in _walk(kernel, label):
            if key in RAW_KEYS:
                errors.append(f"{path}: raw/context-only card payload is prohibited")

    return errors, coverage_results


def _load(path: Path) -> Any:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    try:
        import yaml  # type: ignore
    except ImportError as exc:
        raise ValueError("YAML input requires PyYAML; use JSON or install PyYAML") from exc
    return yaml.safe_load(text)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--runtime-root", type=Path)
    parser.add_argument("--receipt-out", type=Path)
    args = parser.parse_args()
    try:
        errors, coverage_results = validate(_load(args.path), args.path.resolve(), args.runtime_root.resolve() if args.runtime_root else None)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "FAIL", "errors": [str(exc)]}, ensure_ascii=False, indent=2))
        return 2
    result = {"status": "PASS" if not errors else "FAIL", "errors": errors, "coverage_results": coverage_results}
    if args.receipt_out:
        args.receipt_out.parent.mkdir(parents=True, exist_ok=True)
        args.receipt_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
