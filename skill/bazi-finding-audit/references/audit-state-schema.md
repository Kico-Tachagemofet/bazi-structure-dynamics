# Audit State Schema v2.1

`audit-state.json` 是审计裁决的唯一机器事实源；`audit-report.md` 是人类可读投影。冻结工具只读取并校验 state，不接受命令行手填 verdict。

## Header

- `schema_version: "2.1"`（既有 v2.0 可读取；新审计使用 2.1）
- `audit_id`
- `audit_report_ref`
- `stage`：`structure`／`topic`／`finding`／`composition`／`render`／`timing`／`synastry`／`validation`
- `verdict`：`PASS`／`PASS_WITH_WARNINGS`／`FAIL`
- `findings`
- `repair_propagations`
- `summary`
- `evidence_scan_ref`：finding／composition／render 阶段强制，指向独立程序扫描结果；structure 等阶段可省略

独立 evidence scan 不是审计员自己写的 issue 计数，而是直接从 canonical findings、report-scope、reader 模块、render、receipt 与逐年文件重新枚举缺口。scan 为 FAIL 时，audit state 必须为 FAIL；不能通过“findings 为空”覆盖程序发现的缺失。

## Finding State

每个 finding 含：

- `audit_id`
- `severity`：`BLOCKER`／`WARNING`
- `pattern_id`
- `status`：`open`／`resolved`
- `affected_artifacts`
- `evidence_refs`
- `repair_stage`
- `repair_type`：`patch`／`re-derive`
- `verdict_direction_changed`：修复是否改变原判断方向、主轴、主路线或主 finding
- `discovered_by`：`self-audit`／`user`／`downstream-stage`
- `downstream_impacted`
- `propagation_id`：需要重推时指向 propagation 记录

方向改变者必须 `repair_type: re-derive`。不得补两条边、改一句话后把旧的关系后节点、Topic 或 finding 继续拼接使用。

## Repair Propagation

- `propagation_id`
- `trigger_audit_id`
- `status`：`pending`／`complete`
- `rerun_from_stage`
- `required_artifacts`
- `rerun_artifacts`
- `recheck_refs`

`complete` 时 `rerun_artifacts` 必须覆盖 finding 声明的全部 `downstream_impacted` 与本记录的 `required_artifacts`。

## Summary

以下四个计数由 findings 机械计算并必须完全一致：

- `blocker_total`
- `blocker_open`
- `warning_total`
- `warning_open`

计算 verdict：有 open BLOCKER 为 `FAIL`；否则有 open WARNING 为 `PASS_WITH_WARNINGS`；否则 `PASS`。
