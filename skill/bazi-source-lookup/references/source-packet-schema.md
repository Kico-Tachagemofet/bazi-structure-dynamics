# Source Packet Schema

source-packet.md 是本轮分析的读书收据，不是书目清单。

## Header

- case_id
- framework_lock
- question_scope
- packet_date
- source_coverage：complete／partial／blocked
- packet_role：structure／imagery／supplemental-imagery
- structure_freeze_id：imagery packet 必填
- report_scope_ref：full-reading imagery packet 必填
- topic_slug
- topic_lens_ref
- taiji_center
- topic_body_refs
- use_kernel_ref
- use_pivot_ids
- relation_axis_ids
- baseline_required：true／false

## Source Queries

每个 query 单独编号：

| 字段 | 说明 |
|---|---|
| query_id | SQ-01 等 |
| trigger | 来自哪个盘面事实或待裁决关系 |
| decision_needed | 需要判断什么 |
| framework | 采用哪个来源口径 |
| search_terms | 仅用于定位 |
| full_section_required | 必须读取的完整章节 |

## Read Receipt

每个实际读取段落记录：

- source_id
- 文件路径
- 书名、作者、原典／评注／课程身份
- 章节或课程时间段
- 是否完整读取
- OCR 或断句疑点
- 可支持的规则
- 不可越界的推论

## Decision Rules

只摘录本轮真正会进入结构裁决的规则。每条必须带：

- rule_id
- source_id
- 原意转述
- 适用条件
- 反例或限制
- 与其他来源是否冲突

避免大段复制原文；需要取象时保留完整展开的结构与层次，不压缩成一句口诀。

## Imagery Units

仅 imagery／supplemental-imagery packet 使用。每个单元至少含：

- `imagery_unit_id`
- `symbol_type`：stem／branch／ten-god／pillar-position／hidden-stem／relation／body／place／action／domain
- `symbol`
- `source_id` 与完整读取范围
- `expanded_imagery`：保留原材料的分项层次，不缩成标签
- `functional_meaning`
- `positive_or_supported_expression`
- `pressured_or_distorted_expression`
- `conditions_and_limits`
- `examples_in_source`
- `prohibited_generalization`
- `provenance_layer`
- `ocr_or_transcription_risk`

同柱干支组合、十神相对功能与全局改写由 Imagery Composition 完成，Source Packet 不替命局裁决。

## Coverage Registry

- 本轮 Topic Lens 要求的 imagery units
- 逐条 relation axis 已覆盖的两端、支持／损用／去处／日主关系 units
- 已完整加载的 units
- missing units
- deferred units：首次未展开、后续追问可增量加载
- 不相关或明确排除的 units 及理由

## Conflict Matrix

| 议题 | 来源 A | 来源 B | 本轮处理 |
|---|---|---|---|
| 合化条件 | 规则与适用域 | 规则与适用域 | 分流，不混用 |

## Gaps

每个缺口标：

- gap_id
- missing material
- affected claim
- confidence cap
- fallback allowed

没有证据包的判断不能在后续被写成“原书明确说”。
