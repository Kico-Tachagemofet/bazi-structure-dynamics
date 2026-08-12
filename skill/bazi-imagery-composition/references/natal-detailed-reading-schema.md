# 完整原局详批 Schema

`delivery_mode: full-reading` 默认等于 `report_depth: detailed-natal`。它不是“若干生活专题的合集”，而是先把原局本身完整讲清，再进入家庭、学业、财运、事业与加选专题。只有用户明确要求摘要时才可使用 `report_depth: summary`，且标题与交付说明不得称“详批”。

## 1. 固定原局核心覆盖单元

完整原局必须建立以下稳定 `core_section_id`，每项各有 lens／coverage／finding／composition／render handoff，或明确的 `not-applicable` 收据：

1. `natal-facts-boundaries`：四柱、日主、月令、司令、旬空、真太阳时、起运边界、候选盘与不确定性。
2. `natal-system-engine`：季节环境、节点库存、实际吞吐、蓄积、主堵点、自治子系统、日主承载／启动／改道／停止权。
3. `natal-four-pillars`：年、月、日、时逐柱复合；每柱天干、十神、柱位、地支场、全部藏干、同柱双向着色与关系后修正。
4. `natal-hidden-manifestation`：所有重要 hidden／latent／timing-only 节点的显化矩阵，尤其是会改变主问题、路线、格局、日主承载或已选专题的节点。
5. `natal-relation-network`：天干生克合、同柱、六合、六冲、刑、自刑、害、破、方会、三合、半合、重复支、共享节点竞争、残余功能与 negative scan。
6. `natal-ten-god-functions`：十神库存、实际功能边、当前通量、对主问题净效果、代价／旁路、竞争用途、反证和反转条件；禁止用名称替代功能。
7. `natal-pattern-use-agency`：格局候选、成败救应、结构主问题、格局用神、病药／制化、扶身、调候、当前可用度、备用路线与日主能动性。
8. `natal-synthesis-tensions`：全盘最特殊结构、2–5 个复合画面、至少 2 个真实张力或明确不足数量的收据、跨专题共通／差异、证据缺口与 Q&A 入口。

`core_section_id` 是原局核心覆盖单元，不得冒充普通生活 topic。四个基础生活 topic 与已选专题仍按 report scope 另行生产。这里的“单元”约束上游 lens／finding／composition／handoff 的完整性，不规定 Render 必须给每项一个可见标题。

## 2. 重要藏干显化矩阵

产出 `hidden-manifestation-matrix.yaml`。每个重要节点至少含：

- `node_id`、柱位、地支、藏干、十神与气序；
- `natal_visibility`；
- `field_layer`、`qi_layer`、`root_support`、`environmental_feed`、`direct_action_gate`、`pattern_eligibility` 分栏；
- 当前可做什么、不能做什么、实际容量与竞争分配；
- 同一字在不同支位的状态比较，禁止聚合为一个“某木／某火”；
- `activation_interfaces` 按 trigger type 分栏：`stem_exposure`、`branch_reinforcement`、`directional_completion`、`void_fill`、`relationship_field`；
- 每类 trigger 命中后从哪个阶段重算，以及 affected branch／node／edge／route refs；
- `unexposed_expression`：原局未透时仍成立的场、根、供给、内部功能或低容量直接功能；
- `overlay_interface_expression`：外来同字或支场如何提供临时可见接口；不得改写 natal visibility；
- `external_result_requirements`、`strongest_counterconditions`、`expiry_rule`；
- 至少 3 条可核对判断或 `not-reader-facing` 理由。

“不透”“有气”“能做功”“透出”“形成现实结果”是五个不同状态，不得合并成一个开关。外来同字透出表示覆盖层出现临时接口，不表示原局藏干永久变成明干。

## 3. 原局核心 Finding

产出 `natal-core-findings/<core-section-id>.md`。每条 finding 除通用 Finding Schema 外，必须：

- 引用一个稳定 `core_section_id`；
- 引用至少一个 `bazi-scene-kernel`，或在纯事实边界 section 记录 `scene_kernel_not_applicable` 与理由；
- 标出它回答的原局技术问题，而不是借生活 topic 绕写；
- 保留完整结构链和最强反证；
- 每条独立生活主张有稳定 `judgment_id`，格式 `J-<FINDING-ID>-NN`；不设固定数量，也不得为凑数拆成重复性格句；
- 对高对比结构列 `signal_count`、逐信号 refs、读者必须分辨的来源／方向／竞争／结果，以及仅在有助理解时采用的呈现建议；
- 对藏干、用神、格局和能动性说明当前态与条件态，不把未来候选写成现在。

一个原局核心 finding 可以被多个生活 topic 引用，但不能被它们取代。相同判断完整展开一次，其他位置通过 `cross_topic_claim_registry` 交叉引用。

## 4. Composition 固定内容角色与叙事骨架

完整原局 Composition 在 per-topic 覆盖之前先落实以下八类内容角色：

1. 命盘事实与边界；
2. 全盘一句话主轴；
3. 最特殊结构／paradox 主锚；无明显主锚时列前三个主要结构特征；
4. 四柱与藏干显化主线；
5. 格局、用神、路线与日主能动性；
6. 各生活 topic 主线；
7. 跨 topic 张力、共振和现实载体竞争；
8. 整体生命形态、source gaps、Render 与 Q&A handoff。

八类内容角色可以在 composition 中分项登记，供审计逐项核对；Render 则按全盘主锚、关键人生主线、张力与跨 topic 回扣重排成连贯叙事，不要求八段、八章或八个标题。不得为了叙事流畅把任一核心内容压进一句“先说结论”，也不得为了覆盖审计把八个内部字段原样暴露给读者。

## 5. 完整性门槛

- `detailed-natal` 缺任一 core section：BLOCKER。
- 重要藏干缺显化矩阵，或只写“藏而未显”：BLOCKER。
- 四柱没有逐柱展开，或任一相关支漏藏干：BLOCKER。
- 原局关系只列名称，未说明关系后节点、边和路线变化：BLOCKER。
- 十神章节从名称直接给吉凶／能力／事件：BLOCKER。
- 只有 Structure Kernel 或生活 topics，却把交付称为完整原局详批：BLOCKER。
- `summary` 模式可以缩短，但不得复用 `detailed-natal` 合格标识、标题或 audit verdict。

## 6. Reader 输出

建议分文件生成并逐件审计：

- `reader/00-natal-core.md`
- `reader/01-four-pillars.md`
- `reader/02-hidden-manifestation.md`
- `reader/03-relations-pattern-use.md`
- `reader/10-<topic>.md`
- `reader/90-timing-overview.md` 与 `reader/timing/<year>.md`（若请求岁运）

这些文件名是生产与逐件审计边界，不是最终报告目录。最终汇总报告按 composition 的 reader narrative spine 排列已经通过审计的正文块，每块只出现一次，不得在编译时重新压缩、重断或把文件名机械转成标题。
