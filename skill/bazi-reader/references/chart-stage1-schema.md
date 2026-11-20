# Stage 1 盘面事实 Schema

## 目录

1. Case Manifest
2. Chart Stage 1
3. Built-in Fact Check
4. Subject Context

## 1. Case Manifest

`case-manifest.yaml` 至少记录：

- `case_id`：匿名、稳定的案例标识。
- `mode`：`pillars-confirmed`／`birth-data`／`uncertain-time`／`timing`／`synastry`。
- `delivery_mode`：`full-reading`／`structure-only`／`limited-topic`（Scope Gate 确认前仅记录用户原始请求，不得擅自扩充）。
- `chart_owner`：命盘主人匿名标识；不得与求测者自动视为同一人。
- `querent_role`：`self`／`proxy`／`unknown`；`proxy` 时记录与命盘主人的关系，但不把代问者经历写进盘主事实。
- `default_reading_center`：通常为 `chart-owner`。
- `question_scope`：本轮用户真正询问的原始范围。
- `framework_lock`：韦千里／沈孝瞻／徐乐吾／课程／其他；允许多选但不得混写。
- `input_source`：用户文字、排盘软件、截图、出生数据或旧档案。
- `uncertainty`：日期、时间、地点、节气、真太阳时、司令和起运口径的不确定项。
- `permitted_claims`：`natal-only`／`timing-enabled`／`synastry-enabled`。
- `subject_context_isolated`：`true`／`false`。

## 2. Chart Stage 1

`chart-stage1.yaml` 使用以下层次。

### chart

- `year_pillar`、`month_pillar`、`day_pillar`、`hour_pillar`
- `day_master`、`month_branch`
- `month_command`：结构化对象，至少包含：
  - `value`：具体司令干；未知时为 `null`
  - `status`：`known`／`unknown-insufficient-input`／`disputed-framework`／`pending-calculation`
  - `framework`、`provenance`、`solar_term_boundary`、`offset_from_term`、`calculation_or_table_source`、`alternative_values`、`downstream_confidence_cap`
- `seasonal_node`、`void_branches`、`known_calendar_method`

若出生日期时间足够计算，或用户明确提供司令，`status` 不得停留在 `unknown-insufficient-input`。任何司令更正必须令下游结构结论重算。

### pillars

每柱分别记录：`position`（`year`/`month`/`day`/`hour`）、`stem`、`stem_element`、`stem_yinyang`、`stem_ten_god`、`branch`、`branch_element`、`branch_void`、`hidden_stems`（依本气、中气、余气顺序）。

每个藏干必须有独立 ID（例如 `month.branch.hidden.2`），包含 `id`、`stem`、`qi_rank`（`main`/`middle`/`residual`）、`element`、`yinyang`、`ten_god`、`table_source`。

### deterministic_candidates

允许 Reader 调用 `scripts/bazi_fact_enumerator.py` 机械列出，但不得裁权重：重复地支、天干五合、地支六合/六冲/刑/害/破（注明“破”在《子平真诠》《千里命稿》中无专门定义）、三合/方会候选及柱位距离。

### timing

只有资料足够时记录：起运顺逆与规则、起运岁数、大运序列、当前大运及用户指定的流年／流月接口、`timing_verdict`。

## 3. Built-in Fact Check

`chart-stage1.yaml` 末尾自带简短 `fact_check` 对象（不另建独立 `chart-stage1-audit.md`）：

- `verdict`：`PASS`（事实完整，可进入结构分析）／`PARTIAL`（限定范围可用，须列明受限项）／`FAIL`（关键事实冲突或缺失，停止）。
- `checks`：核对四柱干支合法性、日主十神重算、每支藏干覆盖、重复支分柱保留、旬空、月令司令与节气边界、真太阳时/时区边界、起运资料及经历隔离。
- `limitations`：记录未独立历算或待确认口径（如性别由运序推定、未提供精确出生秒数等）。

## 4. Subject Context

确有污染材料（已发生经历、旧解读、用户自述、其他术数反馈等）时，隔离写入 `subject-context.md`，文件头标明：

> 盲结构阶段与 fresh writer 禁止读取本文件；仅允许在用户明确要求非盲合参或事后校准时使用。

任何个人背景都不得复制进通用 Skill reference 或测试期望。
