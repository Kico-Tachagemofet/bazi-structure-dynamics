# 五行克应 Composition Schema v4.0

本文件定义 Structure Process 到领域 finding 的组合规则。Composition 的主单位是完整五行克应过程，不是符号共振、逐柱词条或任意 edge 子集。

## 1. 输入优先级

严格按以下顺序读取并锁定：

1. `structure-process-handoff.yaml`；
2. timing／synastry 时的 `process-state-diff`；
3. Topic Lens 的 `process_ref` 与 `phase_focus`；
4. post-branch handoff、十神关系、柱位与藏干状态；
5. imagery source、Deep Cards 与候选现实载体。

后层只能解释、着色和桥接前层，不得修改旺衰、通量、路线、成本、通关效果、相位或日主能动性。

`therapeutic_effect` 只回答相对 primary problem 的病药方向，不能代替 `objective_output_capacity` 或 `social_realization_channels`。若一条路线加重日主负担却提高客观产出、事业成果或收入机会，Composition 必须把两个方向同时保留。

## 2. process-compositions.yaml

每条 `process_composition` 至少含：

- `process_composition_id`
- `topic_id`
- `topic_process_axis_id`
- `process_ref`
- `process_hash_or_freeze_ref`
- `scope`：natal／timing／synastry
- `timing_process_diff_ref`：非 timing 可为空
- `natal_route_retention_ref`：v3.1 timing／synastry 必填
- `overlay_function_transition_refs`：v3.1 timing／synastry 必填
- `shared_node_competition_ref`：v3.1 timing／synastry 必填
- `phase_focus_refs`
- `strength_and_bearing_snapshot`
- `complete_edge_closure`
- `route_condition_refs`
- `elemental_response_sequence`
- `phase_and_agency_sequence`
- `ten_god_relation_meaning`
- `pillar_and_hidden_state_coloring`
- `therapeutic_effect`
- `daymaster_cost`
- `life_effect_matrix`：继承日主承载、客观产出、社会兑现、持续代价四面裁决
- `topic_realization_verdicts`：只在本 topic 对允许通道作方向判断，不改写结构事实
- `residual_problem`
- `bypass_and_rebound`
- `switch_and_failure`
- `domain_carrier_bridge`
- `external_result_gate`
- `reader_question_facet_refs`
- `explanatory_obligations`
- `structural_impact_bounds`：v3.1 timing／synastry 必填
- `runtime_context_branches`：v3.1 timing／synastry 必填；只改载体与 agency，不改 process state
- `do_not_infer`
- `technical_refs`、`source_refs`、`confidence`

### elemental_response_sequence

逐 phase 写清：

- 谁是 source、谁是 target；
- 发生生／克／泄／耗／制／化／通关／改道中的哪一种；
- 该 edge 当前通量；
- 它处理了什么、消耗了什么；
- 下游是继续通关、分叉、停滞还是回病。

不得用“有利有弊”“压力与资源并存”替代过程。

### phase_and_agency_sequence

逐 phase 继承：

- passive／active／autonomous／stalled；
- start gate；
- can-start／can-carry／can-redirect／can-stop；
- 前一 phase 未完成时后续 phase 是否仍可自治运行；
- 恢复或反转条件。

若日主供能失败但地支库存仍在，必须同时写“日主不能主动调用”与“库存／环境供给可能仍存在”，不得二选一。

## 3. 十神、柱位与物象的权限

- 十神解释每条 elemental action 相对日主和领域体的关系，不决定 edge 是否成立；
- 柱位说明过程落在哪一层关系、时间或生活职责，不改变通量；
- 藏干说明库存、根气、环境供给、直接功能或待时接口，不自动等于外部结果；
- 干支物象与 Deep Cards 只补动作形态、质感、场所和候选载体；
- resonance map 可保留为措辞与载体比较收据，但不得成为 finding 的机制事实源。

`pillar-composites.yaml` 降为 `pillar_and_hidden_state_coloring` 的可读投影。它可以帮助解释同柱画面，不能独立支持 route、process、用神或 timing 结论。

## 4. Topic Finding Handoff

每条 primary finding 必须含：

- `process_composition_ref`
- `process_ref`
- `phase_focus_refs`
- `route_closure_receipt_ref`
- `strength_and_bearing_snapshot_ref`
- `timing_process_diff_ref`：岁运必填
- `complete_edge_ids`：必须与 process closure 相等，不得自由删选
- `daymaster_cost`
- `therapeutic_effect`
- `residual_problem`
- `agency_transition`
- `switch_and_failure`

原有 `anchor set` 只作索引投影，不再是人工选择事实源。若 edge／route 列表与 process closure 不同，以 process closure 为准并判 finding FAIL。

## 5. Composition 主骨架

`composition.md` 先按 process 建立全盘脊柱，再组织领域：

1. 旺衰与承载基线；
2. 主压力过程；
3. 通关／救应过程及实际吞吐；
4. 成本、剩余问题与回病；
5. 日主在各 phase 的启动、承载、改道与停机；
6. 同一 process 在不同领域体上的十神与柱位落法；
7. 物象、载体和表达层。

不得先按符号、柱或领域写完若干段，再用一句“旺衰路线修正”补救。

## 6. timing Composition

岁运 finding 先比较 natal process 与本窗 before／after，再映射领域。顺序固定为：

```text
natal baseline
→ external trigger and requalified relation
→ shared-node competition
→ retained natal route and backup route
→ temporary relation function
→ topic-specific carrier candidates
→ runtime role/context branches
→ structural impact bounds and result gate
→ expiry
```

至少写：

- 哪个外来节点改变了哪一 phase；
- start gate、throughput、allocation、cost、therapeutic effect、rebound 与 agency 的变化；
- 哪些 natal phase 仍原样运行；
- 外来关系是否占用原局主路的共享节点，原局路线还剩多少；
- 原局 hidden／latent／timing-only 节点只取得 root-support、direct-function 还是 visible-interface；
- 该临时功能在本领域可能落成哪些不同角色，以及命主当时位置如何改变载体与可控范围；
- 受影响路线的核心度、overlay 层级／持续、剩余主路和备用路线共同支持哪个结构影响带；
- 哪些变化是外部逼迫，哪些部分日主能控制；
- 覆盖到期后撤销什么。

不得用相同的 natal anchor 模板覆盖所有年份；不得从“流年出现某十神”直接跳到生活结论。“原局有保护”必须落到仍成立的 edge／phase、剩余通量和备用路线；不能作安慰性空话。现实位置只能改载体与 agency branch，不能回头改五行 diff。

## 7. 兼容边界

- v2 `pillar-composites／axis-scenes／resonance-map` 只读兼容；
- 新 finding 与 composition 使用 v4.0 composition fields 与 v4 process refs；
- v2 与 v3 不得混合进入同一 composition freeze；
- 旧命例迁移必须从已冻结 Structure Core 重新生成 process handoff，再重做 Topic／Composition；不得只补字段。
