#!/usr/bin/env python3
"""Deterministically enumerate Bazi chart facts and relation candidates.

The script deliberately does not decide strength, transformation, pattern,
auspiciousness, or event imagery. It exists to prevent omission before model
judgment.
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from collections import Counter, defaultdict


STEMS = list("甲乙丙丁戊己庚辛壬癸")
BRANCHES = list("子丑寅卯辰巳午未申酉戌亥")
POSITIONS = ("year", "month", "day", "hour")

STEM_META = {
    "甲": ("wood", "yang"), "乙": ("wood", "yin"),
    "丙": ("fire", "yang"), "丁": ("fire", "yin"),
    "戊": ("earth", "yang"), "己": ("earth", "yin"),
    "庚": ("metal", "yang"), "辛": ("metal", "yin"),
    "壬": ("water", "yang"), "癸": ("water", "yin"),
}

BRANCH_ELEMENT = {
    "子": "water", "丑": "earth", "寅": "wood", "卯": "wood",
    "辰": "earth", "巳": "fire", "午": "fire", "未": "earth",
    "申": "metal", "酉": "metal", "戌": "earth", "亥": "water",
}

HIDDEN_STEMS = {
    "子": ["癸"],
    "丑": ["己", "癸", "辛"],
    "寅": ["甲", "丙", "戊"],
    "卯": ["乙"],
    "辰": ["戊", "乙", "癸"],
    "巳": ["丙", "戊", "庚"],
    "午": ["丁", "己"],
    "未": ["己", "丁", "乙"],
    "申": ["庚", "壬", "戊"],
    "酉": ["辛"],
    "戌": ["戊", "辛", "丁"],
    "亥": ["壬", "甲"],
}

GENERATES = {
    "wood": "fire", "fire": "earth", "earth": "metal",
    "metal": "water", "water": "wood",
}
CONTROLS = {
    "wood": "earth", "earth": "water", "water": "fire",
    "fire": "metal", "metal": "wood",
}

STEM_COMBINATIONS = {
    frozenset(("甲", "己")): "earth",
    frozenset(("乙", "庚")): "metal",
    frozenset(("丙", "辛")): "water",
    frozenset(("丁", "壬")): "wood",
    frozenset(("戊", "癸")): "fire",
}

BRANCH_COMBINATIONS = {
    frozenset(("子", "丑")): "earth",
    frozenset(("寅", "亥")): "wood",
    frozenset(("卯", "戌")): "fire",
    frozenset(("辰", "酉")): "metal",
    frozenset(("巳", "申")): "water",
    frozenset(("午", "未")): "earth",
}
BRANCH_CLASHES = {
    frozenset(("子", "午")), frozenset(("丑", "未")),
    frozenset(("寅", "申")), frozenset(("卯", "酉")),
    frozenset(("辰", "戌")), frozenset(("巳", "亥")),
}
BRANCH_HARMS = {
    frozenset(("子", "未")), frozenset(("丑", "午")),
    frozenset(("寅", "巳")), frozenset(("卯", "辰")),
    frozenset(("申", "亥")), frozenset(("酉", "戌")),
}
BRANCH_BREAKS = {
    frozenset(("子", "酉")), frozenset(("丑", "辰")),
    frozenset(("寅", "亥")), frozenset(("卯", "午")),
    frozenset(("巳", "申")), frozenset(("未", "戌")),
}

PUNISHMENT_PAIRS = {
    ("寅", "巳"): "ungrateful", ("巳", "申"): "ungrateful",
    ("申", "寅"): "ungrateful",
    ("丑", "戌"): "power", ("戌", "未"): "power",
    ("未", "丑"): "power",
    ("子", "卯"): "discourteous", ("卯", "子"): "discourteous",
}
PUNISHMENT_GROUPS = {
    "ungrateful": set("寅巳申"),
    "power": set("丑戌未"),
}
SELF_PUNISH_BRANCHES = set("辰午酉亥")

THREE_HARMONY = {
    "water": set("申子辰"),
    "wood": set("亥卯未"),
    "fire": set("寅午戌"),
    "metal": set("巳酉丑"),
}
DIRECTIONAL_MEETINGS = {
    "water": set("亥子丑"),
    "wood": set("寅卯辰"),
    "fire": set("巳午未"),
    "metal": set("申酉戌"),
}

QI_RANKS = ("main", "middle", "residual")


def ten_god(day_stem: str, other_stem: str) -> str:
    day_element, day_polarity = STEM_META[day_stem]
    other_element, other_polarity = STEM_META[other_stem]
    same_polarity = day_polarity == other_polarity
    if day_element == other_element:
        return "比肩" if same_polarity else "劫财"
    if GENERATES[day_element] == other_element:
        return "食神" if same_polarity else "伤官"
    if CONTROLS[day_element] == other_element:
        return "偏财" if same_polarity else "正财"
    if CONTROLS[other_element] == day_element:
        return "七杀" if same_polarity else "正官"
    if GENERATES[other_element] == day_element:
        return "偏印" if same_polarity else "正印"
    raise ValueError(f"Cannot determine ten god: {day_stem}, {other_stem}")


def xun_void(day_pillar: str) -> list[str]:
    stem, branch = day_pillar
    index = next(
        (i for i in range(60) if STEMS[i % 10] == stem and BRANCHES[i % 12] == branch),
        None,
    )
    if index is None:
        raise ValueError(f"Invalid sexagenary day pillar: {day_pillar}")
    void_by_xun = [
        ["戌", "亥"], ["申", "酉"], ["午", "未"],
        ["辰", "巳"], ["寅", "卯"], ["子", "丑"],
    ]
    return void_by_xun[index // 10]


def validate_pillars(pillars: list[str]) -> None:
    if len(pillars) != 4:
        raise ValueError("Exactly four pillars are required")
    for pillar in pillars:
        if len(pillar) != 2 or pillar[0] not in STEMS or pillar[1] not in BRANCHES:
            raise ValueError(f"Invalid pillar: {pillar}")
        if not any(
            STEMS[i % 10] == pillar[0] and BRANCHES[i % 12] == pillar[1]
            for i in range(60)
        ):
            raise ValueError(f"Stem-branch parity is invalid: {pillar}")


def position_distance(a: str, b: str) -> int:
    return abs(POSITIONS.index(a) - POSITIONS.index(b))


def make_nodes(pillars: list[str], void_branches: list[str]) -> list[dict]:
    day_master = pillars[2][0]
    nodes: list[dict] = []
    for position, pillar in zip(POSITIONS, pillars):
        stem, branch = pillar
        element, polarity = STEM_META[stem]
        nodes.append({
            "node_id": f"{position}.stem",
            "position": position,
            "layer": "visible_stem",
            "stem": stem,
            "element": element,
            "polarity": polarity,
            "ten_god": "日主" if position == "day" else ten_god(day_master, stem),
        })
        for idx, hidden in enumerate(HIDDEN_STEMS[branch]):
            hidden_element, hidden_polarity = STEM_META[hidden]
            nodes.append({
                "node_id": f"{position}.branch.hidden.{idx + 1}",
                "position": position,
                "layer": f"hidden_{QI_RANKS[idx]}",
                "branch": branch,
                "branch_void": branch in void_branches,
                "stem": hidden,
                "element": hidden_element,
                "polarity": hidden_polarity,
                "ten_god": ten_god(day_master, hidden),
                "qi_rank": QI_RANKS[idx],
            })
    return nodes


def node_edges(nodes: list[dict]) -> tuple[list[dict], list[dict]]:
    directed: list[dict] = []
    peers: list[dict] = []
    for source, target in itertools.permutations(nodes, 2):
        relation = None
        if GENERATES[source["element"]] == target["element"]:
            relation = "sheng"
        elif CONTROLS[source["element"]] == target["element"]:
            relation = "ke"
        if relation:
            directed.append({
                "edge_id": f"E{len(directed) + 1:03d}",
                "source": source["node_id"],
                "target": target["node_id"],
                "relation": relation,
                "position_distance": position_distance(source["position"], target["position"]),
                "same_pillar": source["position"] == target["position"],
                "status": "candidate",
            })
    for left, right in itertools.combinations(nodes, 2):
        if left["element"] == right["element"]:
            peers.append({
                "pair_id": f"P{len(peers) + 1:03d}",
                "nodes": [left["node_id"], right["node_id"]],
                "relation": "same_element",
                "same_polarity": left["polarity"] == right["polarity"],
                "position_distance": position_distance(left["position"], right["position"]),
                "status": "candidate",
            })
    return directed, peers


def visible_stem_pair_checks(pillars: list[str]) -> list[dict]:
    visible = [
        {
            "node_id": f"{position}.stem",
            "position": position,
            "stem": pillar[0],
            "element": STEM_META[pillar[0]][0],
        }
        for position, pillar in zip(POSITIONS, pillars)
    ]
    checks: list[dict] = []
    for left, right in itertools.combinations(visible, 2):
        if left["element"] == right["element"]:
            relation = "same_element"
            direction = None
        elif GENERATES[left["element"]] == right["element"]:
            relation = "sheng"
            direction = [left["node_id"], right["node_id"]]
        elif GENERATES[right["element"]] == left["element"]:
            relation = "sheng"
            direction = [right["node_id"], left["node_id"]]
        elif CONTROLS[left["element"]] == right["element"]:
            relation = "ke"
            direction = [left["node_id"], right["node_id"]]
        else:
            relation = "ke"
            direction = [right["node_id"], left["node_id"]]
        checks.append({
            "nodes": [left["node_id"], right["node_id"]],
            "stems": [left["stem"], right["stem"]],
            "relation": relation,
            "direction": direction,
            "distance": position_distance(left["position"], right["position"]),
            "adjacent": position_distance(left["position"], right["position"]) == 1,
        })
    return checks


def stem_candidates(pillars: list[str]) -> tuple[list[dict], list[dict]]:
    candidates: list[dict] = []
    participation: dict[str, list[str]] = defaultdict(list)
    visible = [(position, pillar[0]) for position, pillar in zip(POSITIONS, pillars)]
    for (pos_a, stem_a), (pos_b, stem_b) in itertools.combinations(visible, 2):
        result = STEM_COMBINATIONS.get(frozenset((stem_a, stem_b)))
        if result:
            relation_id = f"SC{len(candidates) + 1:02d}"
            candidates.append({
                "interaction_id": relation_id,
                "type": "stem_combination",
                "participants": [f"{pos_a}.stem", f"{pos_b}.stem"],
                "stems": [stem_a, stem_b],
                "transformation_element": result,
                "distance": position_distance(pos_a, pos_b),
                "adjacent": position_distance(pos_a, pos_b) == 1,
                "status": "candidate_not_transformation",
            })
            participation[f"{pos_a}.stem"].append(relation_id)
            participation[f"{pos_b}.stem"].append(relation_id)
    shared = [
        {"node_id": node_id, "candidate_relations": relation_ids}
        for node_id, relation_ids in participation.items()
        if len(relation_ids) > 1
    ]
    return candidates, shared


def branch_candidates(pillars: list[str]) -> dict:
    branch_nodes = [
        {"node_id": f"{position}.branch", "position": position, "branch": pillar[1]}
        for position, pillar in zip(POSITIONS, pillars)
    ]
    pair_checks: list[dict] = []
    relations: list[dict] = []
    participation: dict[str, list[str]] = defaultdict(list)

    for left, right in itertools.combinations(branch_nodes, 2):
        pair = frozenset((left["branch"], right["branch"]))
        distance = position_distance(left["position"], right["position"])
        pair_checks.append({
            "nodes": [left["node_id"], right["node_id"]],
            "branches": [left["branch"], right["branch"]],
            "distance": distance,
            "adjacent": distance == 1,
        })
        found: list[tuple[str, str | None]] = []
        if left["branch"] == right["branch"]:
            found.append(("repeated_branch", None))
        if pair in BRANCH_COMBINATIONS:
            found.append(("six_combination", BRANCH_COMBINATIONS[pair]))
        if pair in BRANCH_CLASHES:
            found.append(("clash", None))
        if pair in BRANCH_HARMS:
            found.append(("harm", None))
        if pair in BRANCH_BREAKS:
            found.append(("break", None))
        punishment = PUNISHMENT_PAIRS.get((left["branch"], right["branch"]))
        reverse_punishment = PUNISHMENT_PAIRS.get((right["branch"], left["branch"]))
        if punishment or reverse_punishment:
            found.append(("punishment", punishment or reverse_punishment))
        if left["branch"] == right["branch"] and left["branch"] in SELF_PUNISH_BRANCHES:
            found.append(("self_punishment", None))

        for relation_type, result in found:
            relation_id = f"BR{len(relations) + 1:02d}"
            item = {
                "interaction_id": relation_id,
                "type": relation_type,
                "participants": [left["node_id"], right["node_id"]],
                "branches": [left["branch"], right["branch"]],
                "distance": distance,
                "adjacent": distance == 1,
                "status": "candidate",
            }
            if result:
                item["result_or_subtype"] = result
            relations.append(item)
            participation[left["node_id"]].append(relation_id)
            participation[right["node_id"]].append(relation_id)

    distinct_present = set(node["branch"] for node in branch_nodes)
    group_candidates: list[dict] = []
    for group_type, groups in (
        ("three_harmony", THREE_HARMONY),
        ("directional_meeting", DIRECTIONAL_MEETINGS),
    ):
        for element, members in groups.items():
            present = sorted(distinct_present & members, key=BRANCHES.index)
            if len(present) >= 2:
                member_nodes = [
                    node["node_id"] for node in branch_nodes if node["branch"] in members
                ]
                relation_id = f"BG{len(group_candidates) + 1:02d}"
                item = {
                    "interaction_id": relation_id,
                    "type": group_type,
                    "element": element,
                    "members_required": sorted(members, key=BRANCHES.index),
                    "members_present": present,
                    "member_nodes": member_nodes,
                    "completeness": "complete" if members <= distinct_present else "partial",
                    "missing": sorted(members - distinct_present, key=BRANCHES.index),
                    "status": "candidate",
                }
                group_candidates.append(item)
                for node_id in member_nodes:
                    participation[node_id].append(relation_id)

    for subtype, members in PUNISHMENT_GROUPS.items():
        present = sorted(distinct_present & members, key=BRANCHES.index)
        if len(present) >= 2:
            member_nodes = [
                node["node_id"] for node in branch_nodes if node["branch"] in members
            ]
            relation_id = f"BG{len(group_candidates) + 1:02d}"
            group_candidates.append({
                "interaction_id": relation_id,
                "type": "three_punishment_group",
                "subtype": subtype,
                "members_required": sorted(members, key=BRANCHES.index),
                "members_present": present,
                "member_nodes": member_nodes,
                "completeness": "complete" if members <= distinct_present else "partial",
                "missing": sorted(members - distinct_present, key=BRANCHES.index),
                "status": "candidate",
            })
            for node_id in member_nodes:
                participation[node_id].append(relation_id)

    shared = [
        {"node_id": node_id, "candidate_relations": relation_ids}
        for node_id, relation_ids in participation.items()
        if len(relation_ids) > 1
    ]
    counts = Counter(node["branch"] for node in branch_nodes)
    repeated = [
        {
            "branch": branch,
            "count": count,
            "nodes": [node["node_id"] for node in branch_nodes if node["branch"] == branch],
        }
        for branch, count in counts.items()
        if count > 1
    ]
    return {
        "pair_checks": pair_checks,
        "pair_relations": relations,
        "group_candidates": group_candidates,
        "shared_branch_candidates": shared,
        "repeated_branches": repeated,
    }


def enumerate_chart(pillars: list[str]) -> dict:
    validate_pillars(pillars)
    void_branches = xun_void(pillars[2])
    nodes = make_nodes(pillars, void_branches)
    elemental_edges, same_element_pairs = node_edges(nodes)
    stem_pair_checks = visible_stem_pair_checks(pillars)
    stem_combinations, shared_stem_combinations = stem_candidates(pillars)
    branches = branch_candidates(pillars)
    return {
        "schema_version": "1.0",
        "scope": "facts_and_candidates_only",
        "pillars": dict(zip(POSITIONS, pillars)),
        "day_master": pillars[2][0],
        "month_branch": pillars[1][1],
        "void_branches": void_branches,
        "nodes": nodes,
        "visible_stem_pair_checks": stem_pair_checks,
        "visible_stem_combinations": stem_combinations,
        "shared_stem_combination_candidates": shared_stem_combinations,
        "elemental_candidate_edges": elemental_edges,
        "same_element_candidate_pairs": same_element_pairs,
        "branch_candidates": branches,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Enumerate Bazi facts and relation candidates without interpretation."
    )
    parser.add_argument("pillars", nargs=4, help="Four pillars, for example 戊寅 丙辰 壬寅 庚戌")
    parser.add_argument("--compact", action="store_true", help="Emit compact JSON")
    args = parser.parse_args()
    try:
        result = enumerate_chart(args.pillars)
    except ValueError as exc:
        print(json.dumps({"verdict": "FAIL", "error": str(exc)}, ensure_ascii=False))
        return 2
    indent = None if args.compact else 2
    print(json.dumps(result, ensure_ascii=False, indent=indent))
    return 0


if __name__ == "__main__":
    sys.exit(main())
