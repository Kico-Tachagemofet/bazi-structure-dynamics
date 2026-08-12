#!/usr/bin/env python3
"""Validate the project-specific Deep Card index without third-party YAML packages."""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path


ALLOWED_STATUS = {"planned", "draft_pending_human_review", "approved", "rejected"}
EXPECTED_FAMILIES = {
    "foundation": 1,
    "heavenly_stem": 10,
    "earthly_branch": 12,
    "relational_operator": 1,
}
REQUIRED_TOPIC_AXES = {
    "behavior_personality",
    "appearance_body",
    "learning_cognition",
    "career_work",
    "wealth_resource",
    "family_relationship",
    "object_place",
}
ALLOWED_UNIT_CLASSES = {
    "semantic_core",
    "state_modifier",
    "symbol_carrier",
    "relational_carrier",
    "cross_system_context",
}
BRANCH_CONTRACT_DECLARATIONS = {
    "`branch_manifestation_contract`: field-qi-function-result-v1",
    "`static_hidden_stems_authority`: Reader",
    "`commander_authority`: Reader_month_command_with_source",
    "`commander_does_not_rewrite_hidden_stems`: true",
}
BRANCH_MANIFESTATION_LAYERS = {
    "field_layer",
    "qi_layer",
    "function_layer",
    "result_layer",
}
STEM_UNIT_TOKEN = {
    "甲": "JIA",
    "乙": "YI",
    "丙": "BING",
    "丁": "DING",
    "戊": "WU",
    "己": "JI",
    "庚": "GENG",
    "辛": "XIN",
    "壬": "REN",
    "癸": "GUI",
}
STATIC_HIDDEN_STEMS_DECLARATION = re.compile(
    r"^- `static_hidden_stems`: \[(?P<stems>[甲乙丙丁戊己庚辛壬癸](?:, [甲乙丙丁戊己庚辛壬癸])*)\]$",
    re.MULTILINE,
)
COMMANDER_SEQUENCE_DECLARATION = re.compile(
    r"^- `commander_sequence`: \[(?P<sequence>[^\]]+)\]$",
    re.MULTILINE,
)
UNIT_ROW = re.compile(
    r"^\| `(?P<unit_id>[A-Z][A-Z0-9-]+)` \| `(?P<unit_class>[a-z_]+)` \|"
)


def _value(line: str) -> str:
    value = line.split(":", 1)[1].strip()
    if value == "null":
        return ""
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def _parse_index(path: Path) -> tuple[list[dict[str, str]], list[str], list[dict[str, str]]]:
    cards: list[dict[str, str]] = []
    source_paths: list[str] = []
    shared_layers: list[dict[str, str]] = []
    section = ""
    current: dict[str, str] | None = None

    for line in path.read_text(encoding="utf-8").splitlines():
        if line == "shared_layers:":
            section = "shared"
            current = None
            continue
        if line == "cross_system_source_pool:":
            section = "sources"
            current = None
            continue
        if line == "cards:":
            section = "cards"
            current = None
            continue
        if line == "review_sequence:":
            section = "review"
            current = None
            continue

        stripped = line.strip()
        if section == "shared":
            if stripped.startswith("- layer_id:"):
                current = {"layer_id": _value(stripped)}
                shared_layers.append(current)
            elif current is not None and any(
                stripped.startswith(f"{key}:") for key in ("scope", "status", "path")
            ):
                key = stripped.split(":", 1)[0]
                current[key] = _value(stripped)
        elif section == "sources" and stripped.startswith("path:"):
            source_paths.append(_value(stripped))
        elif section == "cards":
            if stripped.startswith("- card_id:"):
                current = {"card_id": _value(stripped)}
                cards.append(current)
            elif current is not None and any(
                stripped.startswith(f"{key}:") for key in ("family", "symbol", "status", "path")
            ):
                key = stripped.split(":", 1)[0]
                current[key] = _value(stripped)

    return cards, source_paths, shared_layers


def _parse_indented_list(text: str, key: str) -> list[str]:
    """Read a simple YAML list under an exact key without accepting nested spillover."""
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.strip() != f"{key}:":
            continue
        base_indent = len(line) - len(line.lstrip())
        values: list[str] = []
        for child in lines[index + 1 :]:
            if not child.strip():
                continue
            child_indent = len(child) - len(child.lstrip())
            if child_indent <= base_indent:
                break
            stripped = child.strip()
            if stripped.startswith("- "):
                values.append(stripped[2:].strip().strip("'\""))
        return values
    return []


def _read_reader_hidden_stems(script_path: Path) -> dict[str, list[str]]:
    """Load the deterministic Reader table without importing or executing the script."""
    tree = ast.parse(script_path.read_text(encoding="utf-8"), filename=str(script_path))
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(isinstance(target, ast.Name) and target.id == "HIDDEN_STEMS" for target in node.targets):
            value = ast.literal_eval(node.value)
            if isinstance(value, dict):
                return value
    raise ValueError("Reader HIDDEN_STEMS table not found")


def validate(index_path: Path) -> list[str]:
    errors: list[str] = []
    index_text = index_path.read_text(encoding="utf-8")
    cards, source_paths, shared_layers = _parse_index(index_path)
    reference_root = index_path.parent
    unit_owners: dict[str, str] = {}
    runtime_card_ids: set[str] = set()
    reader_script = index_path.resolve().parents[2] / "bazi-reader" / "scripts" / "bazi_fact_enumerator.py"
    try:
        reader_hidden_stems = _read_reader_hidden_stems(reader_script)
    except (OSError, SyntaxError, ValueError) as exc:
        reader_hidden_stems = {}
        errors.append(f"Reader hidden-stem authority unavailable: {exc}")

    required_runtime_policy = {
        'schema_version: "0.4"',
        "authoring_master_access: source_lookup_only",
        "composition_access: compiled_units_only",
        "render_access: none",
        "default_deny_unrequested_units: true",
    }
    missing_policy = sorted(item for item in required_runtime_policy if item not in index_text)
    if missing_policy:
        errors.append(f"runtime_policy: missing firewall declarations {missing_policy}")
    required_runtime_enablement = {
        "status: production_enabled",
        "reviewed_by: human_maintainer",
        "approved_scope: all_indexed_deep_cards_and_earthly_branch_shared_layer",
        "client_finding_use: allowed_after_structure_freeze_topic_query_runtime_compilation_and_audit",
    }
    missing_enablement = sorted(
        item for item in required_runtime_enablement if item not in index_text
    )
    if missing_enablement:
        errors.append(
            f"runtime_enablement: missing production approval declarations {missing_enablement}"
        )
    for forbidden in {
        "render_reads_manifest_cards_after_claim_lock",
        "render_may_read_manifest_cards_but_must_follow_render_use_envelope",
    }:
        if forbidden in index_text:
            errors.append(f"runtime_policy: legacy raw-card permission remains: {forbidden}")

    if len(cards) != 24:
        errors.append(f"cards: expected 24, got {len(cards)}")

    ids = [card.get("card_id", "") for card in cards]
    if len(ids) != len(set(ids)):
        errors.append("cards: duplicate card_id")

    for family, expected in EXPECTED_FAMILIES.items():
        actual = sum(card.get("family") == family for card in cards)
        if actual != expected:
            errors.append(f"family {family}: expected {expected}, got {actual}")

    for card in cards:
        card_id = card.get("card_id", "<missing>")
        status = card.get("status")
        relative_path = card.get("path", "")
        if status not in ALLOWED_STATUS:
            errors.append(f"{card_id}: invalid status {status}")
        if status == "planned" and relative_path:
            errors.append(f"{card_id}: planned card must have null path")
        if status != "planned":
            if not relative_path:
                errors.append(f"{card_id}: non-planned card needs a path")
                continue
            card_path = reference_root / relative_path
            if not card_path.is_file():
                errors.append(f"{card_id}: missing file {relative_path}")
                continue
            card_text = card_path.read_text(encoding="utf-8")
            first_line = card_text.splitlines()[0]
            if card_id not in first_line:
                errors.append(f"{card_id}: first heading does not identify the card")
            if f"- `status`: {status}" not in card_text:
                errors.append(f"{card_id}: index status {status} does not match card declaration")
            if status == "approved" and "- `review_state`: runtime_approved_by_human_" not in card_text:
                errors.append(f"{card_id}: approved card missing human runtime approval receipt")
            if "`version`: 0.3" in card_text:
                runtime_card_ids.add(card_id)
                if "`runtime_contract`: unit_permissions_v0.1" not in card_text:
                    errors.append(f"{card_id}: v0.3 card missing runtime_contract")
                if "Runtime unit map" not in card_text:
                    errors.append(f"{card_id}: v0.3 card missing Runtime unit map")
                unit_rows = [
                    match
                    for line in card_text.splitlines()
                    if (match := UNIT_ROW.match(line)) is not None
                ]
                if not unit_rows:
                    errors.append(f"{card_id}: v0.3 card has no parseable runtime units")
                for match in unit_rows:
                    unit_id = match.group("unit_id")
                    unit_class = match.group("unit_class")
                    if unit_class not in ALLOWED_UNIT_CLASSES:
                        errors.append(f"{card_id}: {unit_id} has invalid class {unit_class}")
                    previous_owner = unit_owners.get(unit_id)
                    if previous_owner is not None:
                        errors.append(
                            f"{card_id}: duplicate runtime unit {unit_id}; already owned by {previous_owner}"
                        )
                    else:
                        unit_owners[unit_id] = card_id
                    if unit_class == "cross_system_context" and "source-only" not in match.string:
                        errors.append(f"{card_id}: {unit_id} cross-system unit is not source-only")
                if card.get("family") == "earthly_branch":
                    missing_declarations = sorted(
                        declaration
                        for declaration in BRANCH_CONTRACT_DECLARATIONS
                        if declaration not in card_text
                    )
                    if missing_declarations:
                        errors.append(
                            f"{card_id}: missing branch contract declarations {missing_declarations}"
                        )
                    missing_layers = sorted(
                        layer for layer in BRANCH_MANIFESTATION_LAYERS if layer not in card_text
                    )
                    if missing_layers:
                        errors.append(
                            f"{card_id}: missing branch manifestation layers {missing_layers}"
                        )
                    branch_prefix = f"{card_id.rsplit('-', 1)[-1]}-"
                    branch_unit_ids = [match.group("unit_id") for match in unit_rows]
                    wrong_prefixes = sorted(
                        unit_id for unit_id in branch_unit_ids if not unit_id.startswith(branch_prefix)
                    )
                    if wrong_prefixes:
                        errors.append(
                            f"{card_id}: runtime units use a foreign prefix {wrong_prefixes}"
                        )
                    if not any("-QI-" in unit_id for unit_id in branch_unit_ids):
                        errors.append(f"{card_id}: no per-hidden-qi runtime interface")
                    if not any("-COMMANDER-" in unit_id for unit_id in branch_unit_ids):
                        errors.append(f"{card_id}: no separate commander runtime unit")
                    hidden_match = STATIC_HIDDEN_STEMS_DECLARATION.search(card_text)
                    if hidden_match is None:
                        errors.append(f"{card_id}: missing parseable static_hidden_stems declaration")
                    else:
                        hidden_stems = hidden_match.group("stems").split(", ")
                        expected_hidden_stems = reader_hidden_stems.get(card.get("symbol", ""))
                        if expected_hidden_stems is None:
                            errors.append(
                                f"{card_id}: symbol {card.get('symbol', '')} missing from Reader HIDDEN_STEMS"
                            )
                        elif hidden_stems != expected_hidden_stems:
                            errors.append(
                                f"{card_id}: static_hidden_stems {hidden_stems} do not match Reader "
                                f"{expected_hidden_stems}"
                            )
                        for stem in hidden_stems:
                            qi_token = f"-QI-{STEM_UNIT_TOKEN[stem]}-"
                            matches = [unit_id for unit_id in branch_unit_ids if qi_token in unit_id]
                            if len(matches) != 1:
                                errors.append(
                                    f"{card_id}: hidden stem {stem} needs exactly one runtime interface; "
                                    f"got {matches}"
                                )
                    if COMMANDER_SEQUENCE_DECLARATION.search(card_text) is None:
                        errors.append(f"{card_id}: missing parseable commander_sequence declaration")
            if card.get("family") in {"heavenly_stem", "earthly_branch"}:
                if "## 7. Topic axes" not in card_text:
                    errors.append(f"{card_id}: missing standardized Topic axes section")
                missing_axes = sorted(axis for axis in REQUIRED_TOPIC_AXES if f"`{axis}`" not in card_text)
                if missing_axes:
                    errors.append(f"{card_id}: missing Topic axes {', '.join(missing_axes)}")

    compiled_cards = set(_parse_indented_list(index_text, "compiled_pilot"))
    legacy_cards = set(_parse_indented_list(index_text, "legacy_authoring_only_until_unitized"))
    planned_cards = set(_parse_indented_list(index_text, "planned_on_new_runtime_contract"))
    indexed_planned_cards = {
        card.get("card_id", "") for card in cards if card.get("status") == "planned"
    }
    missing_compiled = sorted(runtime_card_ids - compiled_cards)
    stale_compiled = sorted(compiled_cards - runtime_card_ids)
    stale_legacy = sorted(runtime_card_ids & legacy_cards)
    if missing_compiled:
        errors.append(f"runtime_migration: v0.3 cards missing from compiled_pilot {missing_compiled}")
    if stale_compiled:
        errors.append(f"runtime_migration: compiled_pilot contains non-v0.3 cards {stale_compiled}")
    if stale_legacy:
        errors.append(f"runtime_migration: v0.3 cards remain legacy-only {stale_legacy}")
    missing_planned_registry = sorted(indexed_planned_cards - planned_cards)
    stale_planned_registry = sorted(planned_cards - indexed_planned_cards)
    if missing_planned_registry:
        errors.append(
            "runtime_migration: planned cards missing from planned_on_new_runtime_contract "
            f"{missing_planned_registry}"
        )
    if stale_planned_registry:
        errors.append(
            "runtime_migration: planned_on_new_runtime_contract contains non-planned cards "
            f"{stale_planned_registry}"
        )

    if len(source_paths) != 3:
        errors.append(f"cross_system_source_pool: expected 3 paths, got {len(source_paths)}")
    for source_path in source_paths:
        if source_path.startswith("external-source://"):
            continue
        candidate = Path(source_path)
        if not candidate.is_absolute() or not candidate.is_file():
            errors.append(
                "cross-system source must be an existing absolute path or a portable "
                f"external-source URI: {source_path}"
            )

    branch_core = next(
        (layer for layer in shared_layers if layer.get("layer_id") == "DC-EARTHLY-BRANCHES-CORE"),
        None,
    )
    if branch_core is None:
        errors.append("shared_layers: missing DC-EARTHLY-BRANCHES-CORE")
    else:
        status = branch_core.get("status")
        relative_path = branch_core.get("path", "")
        if status not in ALLOWED_STATUS:
            errors.append(f"DC-EARTHLY-BRANCHES-CORE: invalid status {status}")
        if not relative_path:
            errors.append("DC-EARTHLY-BRANCHES-CORE: missing path")
        else:
            layer_path = reference_root / relative_path
            if not layer_path.is_file():
                errors.append(f"DC-EARTHLY-BRANCHES-CORE: missing file {relative_path}")
            else:
                layer_text = layer_path.read_text(encoding="utf-8")
                if "DC-EARTHLY-BRANCHES-CORE" not in layer_text.splitlines()[0]:
                    errors.append("DC-EARTHLY-BRANCHES-CORE: first heading does not identify the layer")
                if f"- `status`: {status}" not in layer_text:
                    errors.append(
                        "DC-EARTHLY-BRANCHES-CORE: index status does not match layer declaration"
                    )
                if status == "approved" and "- `review_state`: runtime_approved_by_human_" not in layer_text:
                    errors.append(
                        "DC-EARTHLY-BRANCHES-CORE: approved layer missing human runtime approval receipt"
                    )

    return errors


def main() -> int:
    index_path = Path(__file__).resolve().parents[1] / "references" / "deep-card-index.yaml"
    errors = validate(index_path)
    result = {
        "verdict": "PASS" if not errors else "FAIL",
        "index": str(index_path),
        "errors": errors,
        "boundary": "Index, runtime firewall, migration registry, runtime-unit uniqueness/class, branch manifestation contract, Reader hidden-stem parity, hidden-qi/commander separation, shared-layer, file, portable source reference, status, family-count, and Topic-axis presence validation only; no imagery judgment.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
