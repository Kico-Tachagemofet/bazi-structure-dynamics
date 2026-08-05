# Stage 1 盘面事实 Schema

## 目录

1. Case Manifest
2. Chart Stage 1
3. Audit
4. Subject Context

## 1. Case Manifest

case-manifest.yaml 至少记录：

- case_id：匿名、稳定的案例标识。
- mode：pillars-confirmed／birth-data／uncertain-time／timing／synastry。
- question_scope：本轮用户真正询问的范围。
- framework_lock：韦千里／沈孝瞻／徐乐吾／课程／其他；允许多选但不得混写。
- input_source：用户文字、排盘软件、截图、出生数据或旧档案。
- uncertainty：日期、时间、地点、节气、真太阳时、司令和起运口径的不确定项。
- permitted_claims：natal-only／timing-enabled／synastry-enabled。
- subject_context_isolated：true／false。

## 2. Chart Stage 1

chart-stage1.yaml 使用以下层次。

### chart

- year_pillar
- month_pillar
- day_pillar
- hour_pillar
- day_master
- month_branch
- month_command：结构化对象，见下
- seasonal_node
- void_branches
- known_calendar_method

`month_command` 至少包含：

- `value`：具体司令干；未知时为 null
- `status`：known／unknown-insufficient-input／disputed-framework／pending-calculation
- `framework`
- `provenance`：user-supplied／calculated／chart-export／source-table
- `solar_term_boundary`
- `offset_from_term`：节后日数或小时数；未知原因
- `calculation_or_table_source`
- `alternative_values`：流派分歧时列出
- `downstream_confidence_cap`

若出生日期时间足够计算，或用户明确提供司令，`status` 不得停留在 `unknown-insufficient-input`。任何司令更正必须令全部结构下游失效。

### pillars

每柱分别记录：

- position：year／month／day／hour
- stem
- stem_element
- stem_yinyang
- stem_ten_god
- branch
- branch_element
- branch_void：true／false
- hidden_stems：依本气、中气、余气顺序

每个藏干必须有独立 ID，例如 month.branch.hidden.2，不得只保存“辰藏戊乙癸”字符串。

藏干字段：

- id
- stem
- qi_rank：main／middle／residual
- element
- yinyang
- ten_god
- table_source

### deterministic candidates

允许 Reader 机械列出，但不得裁权重：

- repeated branches
- stem combinations
- branch combinations
- clashes
- punishments and self-punishments
- harms
- breaks
- three-harmony candidates
- directional-meeting candidates
- adjacency and distance

### timing

只有资料足够时记录：

- luck direction and rule
- luck start and rule
- active major luck
- year／month overlay
- timing_verdict

## 3. Audit

chart-stage1-audit.md 至少检查：

- 四柱完整性；
- 日主与十神重算一致性；
- 每支藏干覆盖；
- 重复支是否保留位置；
- 旬空计算或来源；
- 月令、司令和节气边界；
- 司令是否具有可追溯来源，已知事实是否被错误保留为 unknown；
- 真太阳时、夏令时、历史时区；
- timing 资料是否足够；
- synastry 是否双方分盘；
- subject context 是否隔离。

Verdict：

- PASS：事实足够，可进入完整结构分析。
- PARTIAL：可做限定范围分析；列明锁定的断语。
- FAIL：事实冲突或关键输入缺失，停止。

## 4. Subject Context

subject-context.md 可保存：

- 已发生经历；
- 旧解读；
- 用户自我理解；
- 杯、卦、灵体反馈；
- 健康与现实背景。

文件头必须写明：

> Structure Core 在盲结构阶段禁止读取。本文件只允许在结构审计通过后的 calibration 或 render 阶段使用。

任何个人背景都不得复制进通用 Skill reference 或测试期望。
