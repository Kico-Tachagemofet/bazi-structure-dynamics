# Timing／Synastry Scope Seed Schema v1.0

`timing-scope-seed.yaml`／`synastry-scope-seed.yaml` 是 report-scope 与 overlay 之间的最小无结论入口。它只回答“这轮要重算哪些时间／关系 atom、围绕什么自然语言问题、检查哪些原局 activation interface”，不回答哪条 process 成为正式 topic 轴，也不产 finding 或人物载体。

## 顶层字段

- `schema_version: "1.0"`
- `seed_id`
- `seed_type`：`timing`／`synastry`
- `report_scope_ref`
- `natal_structure_freeze_ref`
- `question_center`：自然语言问题中心，不得写十神人物等式或事件结论
- `domain_scope`：待分析领域 slug 列表
- `scope_atoms`：逐时间窗／关系场独立登记
- `canonical_axes_forbidden: true`
- `finding_handoff_forbidden: true`
- `domain_carrier_verdict_forbidden: true`
- `overlay_status: pending`

不得出现 `topic_process_axes`、`primary_axes`、`expected_primary_findings`、`finding_handoff`、`deep_card_queries`、`domain_carrier_resolution`、`candidate_carriers_ranked` 或 `canonical_topic_lens_ref`。这些字段都依赖尚未完成的 overlay diff／freeze。

## Scope atom

每个 atom 至少含：

- `atom_id`
- `atom_type`：`timing-luck-cycle`／`timing-annual`／`timing-monthly`／`synastry-field`
- `scope_start`、`scope_end`
- `external_node_refs`：本层新加入的干支／关系节点
- `activation_interface_refs`：本轮需要匹配的原局接口；若全量扫描则显式写 `scan-all-natal-interfaces`
- `question_slice_refs`
- `parent_atom_ref`：无则为 `null`

逐年请求中，每一年必须有一个独立 `timing-annual` atom 与独立 `atom_id`，不得用 `2021-2034` 一个 sequence atom 代替。大运 atom 可以是年度 atom 的 parent，但不能替代年度重算。

## 边界

- seed 不读取 overlay、Deep Card、经历或 runtime position；
- seed 不选择正式 process／route／phase，不判断共享节点怎样分配；
- seed 不把 trigger match 写成已激活；
- seed 不把劫财、官杀等关系写成同事、上司或事件；
- Structure Core 完成 overlay、Audit PASS 并 freeze 后，Topic Lens 才能建立 canonical timing／synastry v3.1 state。

运行 `scripts/validate_timing_scope_seed.py <seed.json-or-yaml>`。新 seed 必须 PASS 后才能交 Structure Core。
