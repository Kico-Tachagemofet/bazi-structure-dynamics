# Audit Report Schema

# 八字审计：[case_id] / [stage]

## Coverage

| 项目 | 应有 | 实有 | 状态 |
|---|---:|---:|---|
| 位置节点 |  |  |  |
| 候选关系 |  |  |  |
| 地支关系类别与 negative scan |  |  |  |
| 关系后节点 |  |  |  |
| Edge post-state 引用 |  |  |  |
| 来源查询 |  |  |  |
| 路线 |  |  |  |
| 主问题与路线端点锁 |  |  |  |
| Conditions Matrix |  |  |  |
| Structure Freeze |  |  |  |
| Report Scope／Reading Center |  |  |  |
| 基础四板块／已选专题 |  |  |  |
| Family Blind Calibration Gate |  |  |  |
| 取象单元与逐柱复合 |  |  |  |
| Findings／Composition／Render |  |  |  |

## Findings

每个问题使用：

- audit_id
- severity：BLOCKER／WARNING
- pattern_id
- affected artifact and claim
- evidence
- why it matters
- repair stage
- exact repair
- recheck condition

## Source and Context Integrity

- source receipt verdict
- framework separation verdict
- subject-context isolation verdict
- calibration boundary verdict
- conversational routing verdict

## Verdict

- PASS
- PASS_WITH_WARNINGS
- FAIL

FAIL 时列固定回退顺序，不得由审计器自行改写最终答案后直接通过。

上游产物在审计中被修改时，必须增加 repair propagation 记录：修改内容是否改变语义、受影响的全部下游产物、实际重跑／复验结果。没有该记录不得把修复后的上游与旧下游拼接后通过。

## Structure Freeze Receipt

结构审计 PASS 后另产 `structure-freeze-receipt.yaml`：

- `freeze_id`
- `case_id`
- `audit_report_id` 与 verdict
- 每个结构文件的绝对／案例相对路径、schema version、SHA-256、修改时间
- `commander_fact_ref`
- `problem_state_ref`
- `edge_map_ref`
- `route_map_ref`
- `created_at`
- `invalidates_when`

下游任一结构文件 hash 不符时，Topic、Imagery、Composition 与 Render 全部停止。
