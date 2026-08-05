# 八字取象 Finding Schema

## 目录

1. Imagery Coverage
2. Pillar Composite
3. Topic Finding
4. Full-chart Sweep
5. Experience and Validation Maps

## 1. Imagery Coverage

`imagery-coverage.yaml` 至少包含：

- `case_id`
- `topic_id`
- `exact_question`
- `structure_freeze_id`
- `report_scope_ref`
- `topic_lens_ref`
- `taiji_center`
- `baseline_required`：true／false
- `required_anchors`：柱、节点、边、路线
- `required_imagery_units`：干、支、十神、柱位、藏干、关系、领域
- `loaded_units`
- `missing_units`
- `deferred_units`：本轮不相关但可供追问加载
- `tempting_but_excluded`
- `coverage_verdict`

本账本记录本轮覆盖，不宣称穷尽一个字的全部象意。

## 2. Pillar Composite

`pillar-composites.yaml` 每个相关柱至少含：

- `pillar_id` 与 `position_role`
- `stem_node_id`
- `stem_raw_imagery` 与 source unit IDs
- `stem_ten_god_function`
- `branch_position_id`
- `branch_raw_imagery` 与 source unit IDs
- `hidden_stems`：逐节点列 node ID、十神、气序、关系后状态、参与层、可用条件、不可越界项
- `stem_colors_branch`：天干怎样改变该支场景的呈现
- `branch_colors_stem`：地支怎样给天干提供根基、环境、阻力、去处或存储
- `coloring_asymmetry`：哪一面占主导及理由
- `season_and_commander_modifier`
- `branch_relation_modifier`
- `problem_state_role`
- `route_roles`
- `baseline_expression`
- `pressure_expression`
- `healthy_expression`
- `counterexpression_or_nonmanifestation`
- `technical_refs`
- `source_refs`
- `confidence`

### 同柱互染边界

- 互染描述组合画面，不自动生成生、克、合、制或通关边。
- 天干坐支不等于能调用支中全部藏干。
- 地支藏财库不等于资源已到账；必须读取 visibility、participation scope、route 和 trigger。
- 同柱双方都要解释，但力度可以明显不对称。

## 3. Topic Finding

每条 finding 使用独立小节，标题包含稳定 ID，例如 `## F-CAREER-001`。至少填写：

### Identity

- `finding_id`
- `topic_id`
- `exact_question_part`
- `confidence`
- `scope`：natal／timing／synastry／relationship-field
- `taiji_center`
- `report_section_slug`
- `baseline_required`

### Anchor Set

- pillar IDs
- node IDs
- edge IDs
- route IDs
- problem-state claim IDs
- source unit IDs
- pillar composite IDs

### Composition Trace

按顺序说明：

1. 干或支的本象；
2. 十神赋予的功能；
3. 柱位赋予的生活层；
4. 同柱双向着色；
5. 藏干内部结构；
6. 旺衰、关系后状态和路线如何修正；
7. 以上内容怎样收束成一个可验证判断。

### Full-chart Sweep

- `reinforcing_facts`
- `weakening_facts`
- `reversing_facts`
- `competing_routes`
- `checked_but_irrelevant`
- `net_effect`

### Expression Bands

- `baseline`
- `under_pressure`
- `when_supported_or_well_routed`
- `counterexpression`
- `nonmanifestation_condition`

### Manifestation Layers

- `internal_mechanism`
- `domain_carrier`
- `external_result_requirement`
- `timing_or_field_condition`
- `counter_cost`

### Verifiable Judgments

列出 2 至 6 条命主可核对的具体判断。不要把术语改写成同义术语；每条应包含机制、条件或竞争载体，避免只有“忙、压力、变化、敏感”等高基率词。静态判断即使可回答“是／否／有条件”，也不自动具备证据验证资格。

### Boundaries

- `strongest_alternative`
- `do_not_render`
- `source_gap`
- `not_proven`

### Render Obligations

列出最终文字不可删除的：核心画面、条件、代价、反证、技术依据与需要交叉引用的其他 finding。

每条 blind finding 另加：

- `blind_generation: true`
- `subject_context_read_before_audit: false`
- `manifestation_mapping_eligible_after_audit: true`
- `validation_candidate`：true／false
- `validation_discriminators`：若为 true，列时间差／顺序／竞争载体／失败条件中已具备的部分
- `known_prior_exposure`：none／partial／contaminated

## 4. Full-chart Sweep

Full-chart sweep 不是重断全盘，而是防止局部象遮住全局。至少检查：

- 同一十神在其他位置是否有不同状态；
- 同一节点是否被竞争路线占用；
- 主问题会放大、压制或倒逼该象；
- 救应路线是否改变表达质量；
- 显而易见的相反证据；
- 内部能力、现实载体与外部成果是否被错误等同。

## 5. Experience and Validation Maps

`manifestation-map.md` 逐 finding 记录：

- `finding_id`
- `context_item_id`
- `mapping_state`：matched／conditional／carrier-shift／disconfirmed／new-question／structural-challenge
- `affected_expression_band`
- `allowed_change`：priority／wording／domain carrier／next question
- `forbidden_change`：node／edge／route／pattern／universal rule
- `non-evidentiary: true`
- `next_action`

经历不能填补 source gap，也不能把低通量路线改成高通量或提高结构 confidence。历史兼容文件 `calibration-map.md` 只有在显式写入 `non-evidentiary: true` 时才可继续使用。

流运验证不写入 manifestation map，按 [Validation Protocol](../../bazi-structure-dynamics/references/validation-protocol.md) 单独产出并冻结。至少记录：

- `validation_plan_ref`
- `timing_overlay_freeze_ref`
- `hypothesis_freeze_ref`
- `verbatim_response_ref`
- `scorecard_ref`
- `score_audit_ref`
- `validation_state`：scored／unscored／declined／contaminated
