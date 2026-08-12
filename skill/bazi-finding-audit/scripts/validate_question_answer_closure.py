#!/usr/bin/env python3
"""Mechanically validate Bazi Reader Answer Contract closure artifacts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


SCHEMA_VERSIONS = {"1.0", "2.0"}
ANSWER_STATUSES = {"complete", "conditional", "not-applicable", "source-gap"}
OBLIGATION_ROLES = {"formation", "advantage", "cost", "result-gate", "switch", "verification"}
PERSONALITY_ROLES = {"explanatory-only", "not-used"}
ADVICE_ROLES = {"after-answer", "not-used"}
QUESTION_SOURCES = {"user-verbatim", "scope-confirmed", "faithful-restatement"}
ADVICE_PREFIXES = ("建议", "应当", "应该", "最好", "需要", "请", "可以考虑")
QUESTION_PLACEHOLDER_PREFIXES = ("完整回答", "完整交付")
QUESTION_MARKER = re.compile(r"<!--\s*question_id:\s*([^\s>]+)\s*-->")
CJK = re.compile(r"[\u3400-\u9fff]")


def _need(obj: dict[str, Any], fields: set[str], label: str, errors: list[str]) -> None:
    missing = sorted(fields - set(obj))
    if missing:
        errors.append(f"{label}: missing {', '.join(missing)}")


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _nonempty_list(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(_nonempty_string(item) for item in value)


def _natural_question(value: Any, facet_id: Any) -> bool:
    if not _nonempty_string(value):
        return False
    question = value.strip()
    if len(question) < 8 or not CJK.search(question) or not question.endswith(("？", "?")):
        return False
    if question.startswith(QUESTION_PLACEHOLDER_PREFIXES) or question == str(facet_id or "").strip():
        return False
    return True


def _normalized_text(value: str) -> str:
    return re.sub(r"[\s，。；：、,.!?！？:;‘’“”\-—]", "", value)


def _visible_body(value: str) -> str:
    value = re.sub(r"<!--.*?-->", "", value, flags=re.S)
    value = re.sub(r"[#>*_`\[\](){}]", "", value)
    return value.strip()


def validate_closure(
    payload: dict[str, Any],
    report_text: str | None = None,
    receipt: dict[str, Any] | None = None,
) -> list[str]:
    errors: list[str] = []
    header = {
        "schema_version", "case_id", "structure_freeze_id", "report_scope_ref",
        "topic_lens_index_ref", "question_answers",
    }
    _need(payload, header, "question-answer-map", errors)
    schema_version = str(payload.get("schema_version"))
    if schema_version not in SCHEMA_VERSIONS:
        errors.append("question-answer-map: schema_version must be 1.0 or 2.0")
    if errors and not isinstance(payload.get("question_answers"), list):
        return errors

    answers = payload.get("question_answers")
    if not isinstance(answers, list):
        errors.append("question-answer-map: question_answers must be a list")
        return errors
    if not answers:
        if schema_version == "1.0":
            errors.append("question-answer-map: v1.0 question_answers must be a non-empty list")
        if report_text is not None and QUESTION_MARKER.search(report_text):
            errors.append("report: question markers exist but v2.0 has no genuine question contracts")
        return errors

    closure_keys: set[str] = set()
    contract_ids: set[str] = set()
    render_obligations: set[str] = set()
    answers_by_key: dict[str, dict[str, Any]] = {}
    summary_owners: dict[str, list[dict[str, Any]]] = {}
    required_fields = {
        "closure_key", "contract_id", "topic_id", "question_slice_id", "facet_id",
        "exact_reader_question", "answer_status", "answer_target", "direct_answer_summary",
        "direct_answer_claim_ids", "finding_refs", "source_coverage_refs", "process_refs",
        "obligation_refs", "domain_specific_delta", "shared_mechanism_refs", "shared_answer_ref",
        "strongest_alternative", "personality_role", "advice_role", "advice_substitutes_answer",
        "render_obligation_id", "gap_or_na_reason",
    }
    if schema_version == "2.0":
        required_fields -= {"question_slice_id", "facet_id"}
        required_fields |= {"explicit_question_id", "source_kind", "source_ref"}

    for index, item in enumerate(answers, start=1):
        label = f"question_answers[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{label}: must be an object")
            continue
        _need(item, required_fields, label, errors)
        closure_key = item.get("closure_key")
        contract_id = item.get("contract_id")
        render_obligation_id = item.get("render_obligation_id")
        for value, seen, field in (
            (closure_key, closure_keys, "closure_key"),
            (contract_id, contract_ids, "contract_id"),
            (render_obligation_id, render_obligations, "render_obligation_id"),
        ):
            if not _nonempty_string(value):
                errors.append(f"{label}: {field} must be a non-empty string")
            elif value in seen:
                errors.append(f"{label}: duplicate {field} {value}")
            else:
                seen.add(value)
        if _nonempty_string(closure_key):
            answers_by_key[closure_key] = item

        if schema_version == "2.0":
            if item.get("source_kind") not in QUESTION_SOURCES:
                errors.append(f"{label}: source_kind must prove genuine user/scope provenance")
            if not _nonempty_string(item.get("source_ref")):
                errors.append(f"{label}: source_ref cannot be empty")

        if not _natural_question(item.get("exact_reader_question"), item.get("facet_id")):
            errors.append(f"{label}: exact_reader_question must be a concrete natural-Chinese question")
        answer_target = item.get("answer_target")
        target_fields = {"subject_or_role", "matter_or_domain_object", "result_or_outcome"}
        if not isinstance(answer_target, dict) or set(answer_target) != target_fields:
            errors.append(f"{label}: answer_target must contain exactly the three reader target fields")
        elif any(not _nonempty_string(answer_target.get(field)) for field in target_fields):
            errors.append(f"{label}: every answer_target field must be non-empty")

        status = item.get("answer_status")
        if status not in ANSWER_STATUSES:
            errors.append(f"{label}: invalid answer_status")
        if item.get("personality_role") not in PERSONALITY_ROLES:
            errors.append(f"{label}: personality_role must be explanatory-only or not-used")
        if item.get("advice_role") not in ADVICE_ROLES:
            errors.append(f"{label}: advice_role must be after-answer or not-used")
        if item.get("advice_substitutes_answer") is not False:
            errors.append(f"{label}: advice_substitutes_answer must be false")

        if status in {"complete", "conditional"}:
            summary = item.get("direct_answer_summary")
            if not _nonempty_string(summary) or len(summary.strip()) < 12 or not CJK.search(summary):
                errors.append(f"{label}: complete/conditional needs a concrete Chinese direct_answer_summary")
            elif summary.strip().startswith(ADVICE_PREFIXES):
                errors.append(f"{label}: direct_answer_summary cannot be advice-first")
            else:
                summary_owners.setdefault(_normalized_text(summary), []).append(item)
            for field in {"direct_answer_claim_ids", "finding_refs", "source_coverage_refs", "process_refs"}:
                if not _nonempty_list(item.get(field)):
                    errors.append(f"{label}: {field} must be a non-empty list for complete/conditional")
            obligations = item.get("obligation_refs")
            if not isinstance(obligations, dict) or set(obligations) != OBLIGATION_ROLES:
                errors.append(f"{label}: obligation_refs must contain exactly the six explanatory roles")
            else:
                for role in OBLIGATION_ROLES:
                    if not _nonempty_list(obligations.get(role)):
                        errors.append(f"{label}: obligation_refs.{role} cannot be empty")
            for field in {"domain_specific_delta", "strongest_alternative", "render_obligation_id"}:
                if not _nonempty_string(item.get(field)):
                    errors.append(f"{label}: {field} is required for complete/conditional")
        elif status in {"not-applicable", "source-gap"}:
            if not _nonempty_string(item.get("gap_or_na_reason")):
                errors.append(f"{label}: {status} needs gap_or_na_reason")

    for owners in summary_owners.values():
        topics = {item.get("topic_id") for item in owners}
        if len(owners) < 2 or len(topics) < 2:
            continue
        shared_refs = {item.get("shared_answer_ref") for item in owners}
        deltas = [item.get("domain_specific_delta", "").strip() for item in owners]
        if None in shared_refs or "" in shared_refs or len(shared_refs) != 1 or any(not delta for delta in deltas) or len(set(deltas)) != len(deltas):
            errors.append(
                "question-answer-map: identical direct answers across topics need one shared_answer_ref and distinct domain_specific_delta values"
            )

    if report_text is not None:
        matches = list(QUESTION_MARKER.finditer(report_text))
        marker_counts: dict[str, int] = {}
        for match in matches:
            marker_counts[match.group(1)] = marker_counts.get(match.group(1), 0) + 1
        unknown = set(marker_counts) - closure_keys
        if unknown:
            errors.append(f"report: unknown question markers {sorted(unknown)}")
        for closure_key in closure_keys:
            count = marker_counts.get(closure_key, 0)
            if count != 1:
                errors.append(f"report: question marker {closure_key} must appear exactly once, found {count}")
        for index, match in enumerate(matches):
            closure_key = match.group(1)
            item = answers_by_key.get(closure_key)
            if item is None:
                continue
            end = matches[index + 1].start() if index + 1 < len(matches) else len(report_text)
            body = _visible_body(report_text[match.end():end])
            minimum = 24 if item.get("answer_status") in {"complete", "conditional"} else 8
            if len(body) < minimum:
                errors.append(f"report: question {closure_key} has no substantive answer body")
            if item.get("answer_status") in {"complete", "conditional"} and body.startswith(ADVICE_PREFIXES):
                errors.append(f"report: question {closure_key} starts with advice instead of a direct answer")

    if receipt is not None:
        _need(receipt, {"schema_version", "case_id", "report_ref", "question_answer_receipts"}, "reader-answer-receipt", errors)
        if str(receipt.get("schema_version")) not in SCHEMA_VERSIONS:
            errors.append("reader-answer-receipt: schema_version must be 1.0 or 2.0")
        receipt_items = receipt.get("question_answer_receipts")
        if not isinstance(receipt_items, list):
            errors.append("reader-answer-receipt: question_answer_receipts must be a list")
        else:
            seen: set[str] = set()
            for index, entry in enumerate(receipt_items, start=1):
                label = f"reader-answer-receipt[{index}]"
                required = {
                    "closure_key", "contract_id", "render_obligation_id", "marker_count",
                    "direct_answer_present", "answer_before_advice", "body_ref", "audit_status",
                }
                if not isinstance(entry, dict):
                    errors.append(f"{label}: must be an object")
                    continue
                _need(entry, required, label, errors)
                closure_key = entry.get("closure_key")
                if closure_key in seen:
                    errors.append(f"{label}: duplicate closure_key {closure_key}")
                seen.add(closure_key)
                answer = answers_by_key.get(closure_key)
                if answer is None:
                    errors.append(f"{label}: unknown closure_key {closure_key}")
                    continue
                if entry.get("contract_id") != answer.get("contract_id"):
                    errors.append(f"{label}: contract_id does not match question-answer map")
                if entry.get("render_obligation_id") != answer.get("render_obligation_id"):
                    errors.append(f"{label}: render_obligation_id does not match question-answer map")
                if entry.get("marker_count") != 1:
                    errors.append(f"{label}: marker_count must be 1")
                if answer.get("answer_status") in {"complete", "conditional"}:
                    if entry.get("direct_answer_present") is not True:
                        errors.append(f"{label}: direct_answer_present must be true")
                    if entry.get("answer_before_advice") is not True:
                        errors.append(f"{label}: answer_before_advice must be true")
                if not _nonempty_string(entry.get("body_ref")):
                    errors.append(f"{label}: body_ref cannot be empty")
                if entry.get("audit_status") != "pending-independent-audit":
                    errors.append(f"{label}: audit_status must remain pending-independent-audit; Render cannot self-pass")
            if seen != closure_keys:
                errors.append("reader-answer-receipt: must cover every closure_key exactly once")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Bazi question-answer closure artifacts.")
    parser.add_argument("question_answer_map")
    parser.add_argument("--report")
    parser.add_argument("--reader-receipt")
    args = parser.parse_args()
    try:
        payload = json.loads(Path(args.question_answer_map).read_text(encoding="utf-8"))
        report_text = Path(args.report).read_text(encoding="utf-8") if args.report else None
        receipt = json.loads(Path(args.reader_receipt).read_text(encoding="utf-8")) if args.reader_receipt else None
        errors = validate_closure(payload, report_text, receipt)
    except (OSError, json.JSONDecodeError) as exc:
        errors = [f"artifacts unreadable: {exc}"]
    result = {
        "verdict": "PASS" if not errors else "FAIL",
        "question_answer_map": args.question_answer_map,
        "report": args.report,
        "reader_receipt": args.reader_receipt,
        "errors": errors,
        "boundary": "Mechanical closure scan only; independent semantic audit must still decide whether the prose truly answers the reader question.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
