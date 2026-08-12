---
name: bazi-imagery-composition
description: 将已经通过结构审计的四柱八字转成可追溯、可验证的断局材料：先保真继承旺衰承载、完整五行克应 process、日主成本、回病旁路和相位条件，再强制建立十神关系链，以天干、地支、藏干与柱位逐层限定其现实场景，合成主象、次象和反转象，最后生成领域 findings 与散文 composition。完整原局覆盖家庭、学业、财运、事业及加选专题；只有用户真实提出的问题才另做答案闭环。不得凭经历倒推结构，不得让性格画像、建议、单个十神或单个干支代替断命。
---

# 八字取象与组合

把“结构上成立什么”加工成“它在具体生命领域里可能怎样表现”。本技能不重算旺衰、格局或作用路线；它只在冻结的结构核上完成分层取象、finding 生产和跨 finding 组合。

## 启动门槛

首次运行前完整读取：

- [八字现实断语合同 v1.0](../bazi-structure-dynamics/references/semantic-verdict-contract.md)
- [取象 Finding Schema](references/imagery-finding-schema.md)
- [Composition Schema](references/composition-schema.md)
- [问题—答案闭环 Schema v2](references/question-answer-closure-schema.md)
- [Coverage Receipt Schema v1](references/coverage-receipt-schema.md)
- [五行克应 Composition Schema v4](references/process-composition-schema.md)
- [五行克应过程 Handoff Schema v4](../bazi-structure-core/references/five-element-process-handoff-schema.md)
- [十神—干支象核 Schema v2.0](references/ten-god-stem-branch-kernel-schema.md)
- [象核 Agent 隔离生产协议 v1.0](references/scene-kernel-agent-protocol.md)
- [完整原局详批 Schema](references/natal-detailed-reading-schema.md)
- [领域载体推导](references/domain-carrier-schema.md)
- [读者问题剖面](../bazi-topic-lens/references/reader-question-profiles.md)
- [Deep Card Schema](../bazi-source-lookup/references/deep-card-schema.md)
- [Source Packet Schema](../bazi-source-lookup/references/source-packet-schema.md)

必需输入：

- `chart-stage1.yaml`
- `post-branch-node-ledger.yaml`
- `qualified-edge-map.yaml`
- `problem-state.yaml`
- `route-candidates.yaml`
- `conditions-matrix.md`
- `structure-kernel.md`
- `use-kernel.md`
- `structure-process-handoff.yaml`
- `structure-freeze-receipt.yaml`
- 通过的 structure audit
- `report-scope.yaml`
- `topic-lens-index.yaml` 与本轮全部 canonical `topic-lens-*.json`；Markdown 只作可读投影
- 本 topic 的完整 `imagery-source-packet-<topic>.md`
- 通过 `validate_deep_card_runtime_packet.py` 的 `deep-card-runtime-packet-<topic>.json`
- timing／synastry topic 另需对应 diff／overlay artifacts、审计报告与 overlay freeze receipt

任一结构文件晚于 freeze receipt，或 hash／版本不一致时停止并退回结构审计。不得读取 `subject-context.md`，直到相关 blind findings 通过审计；若要做流运验证，还须等 hypotheses 审计并冻结后才能读取对应年史。

岁运或合盘 finding 必须同时引用冻结 natal process 与受审计 `process-state-diff`；另须引用 matched activation interface、受影响边和 process 的传播闭合收据、覆盖范围与失效条件。overlay 只能描述本轮新增接口和状态差分，不得把它写成本命永久属性。

## 固定分段流程

### 复杂象核的 Agent 执行边界

进入 Mode B2 前，先按 [象核 Agent 隔离生产协议 v1.0](references/scene-kernel-agent-protocol.md) 计算复杂度。`full-reading／detailed-natal`、一次两个以上 kernels、多 process／多判断维度、路线竞争、L4 载体比较、timing／synastry／歧义、runtime selected units 超过 12、当前上下文已知经历／预期答案，或准备以脚本批量生成断语时，必须调用全新上下文 producer agent；主 session 只能产无答案 job packet、调度、合并已审计产物和传播状态。

producer 必须使用最小 allowed-input packet；支持时固定 `fork_turns: none`，不得继承总 session 历史。另调用一个全新上下文 auditor 独立验收；生产者、编排者和审计者不得共享预写答案源。不能创建干净 agent 时标 `AGENT_ISOLATION_UNAVAILABLE` 并停止，不得由主 session、批量脚本或旧报告改写替代。

只有协议列出的全部窄题条件同时成立时，主 session 才可直接生成一个增量 kernel；仍须全量 unit disposition ledger 和独立审计。任何不确定按必须调用 agent 处理。

### Mode A：象意覆盖账本

先根据 Topic Lens 建立 `imagery-coverage.yaml`：

- 本轮问题涉及的柱、干、支、十神、藏干、关系和路线；
- 每个相关柱必须读取的完整取象单元；
- 已加载、缺失、暂不相关的象意范围；
- 被排除但容易误取的符号及排除理由；
- 后续追问可以增量加载的未穷尽范围。
- 每条 `topic_process_axis` 的实际控制者／承载者、两端、去处、日主关系与适用治疗枢纽所需象意。
- 每个 coverage facet 计划由哪些 axes／scene kernels／findings 覆盖，以及形成、能成什么、代价、结果门、反转和核验材料的证据或缺口。
- 只有 `explicit_reader_questions` 中的真实 Reader Answer Contract 才登记 `question_source_coverage`。

“本轮没展开”不得写成“此字没有该象”。缺完整来源时标 `SOURCE_GAP`，不得用一句口诀补齐。

不得读取任何 Deep Card 母卡、source-only manifest 的候选正文或 runtime packet 未选择的单元。只读取 runtime packet 的 `selected_units` 与本题 `domain_carrier_leads`；Source Lookup 已把避免断章取义所需的配对、状态、推导路径和限定编译进单元 payload。若 payload 不足以组合，登记 source gap 并退回 Source Lookup，不自行开母卡补齐。

取象先区分三类：

- `core-process／mechanism-bearing`：气、质、刚柔、方向、形态或动作确实说明已审计作用怎样发生；必须保留，但只能解释现有 node／edge／route，不能反向造边。
- `candidate-carrier`：人物外形、物件或场所候选可以在桥接后进入 finding；具体职业、岗位、正式身份、疾病或事件必须另过 Domain Carrier Resolver。
- `unsupported-fixed-verdict`：没有结构、状态和问题中心桥接，就从一个符号宣布唯一人物、外形、行业或事件；不得进入 finding。

阻止的是无桥接定案，不是阻止候选本身。若甲木与身体题锚点、状态和全盘形态一致，“更可能高挑挺拔”可以直接进入 finding；若只看到甲字而没有这些桥接，才退回候选。若来源的比喻承担机制说明，须写出 `mechanism_trace`。

full-reading 先建立总 `imagery-coverage-index.yaml`：逐项列出 family-home、education-learning、wealth-resource、career-work 和所有 selected optional topics 的 lens、source packet、pillar coverage 与状态。任一基础 topic 缺失时停止，不得先写其他章节后补。

`report_depth: detailed-natal` 时，还必须先建立 `natal-core-coverage-index.yaml`，覆盖 `natal-facts-boundaries`、`natal-system-engine`、`natal-four-pillars`、`natal-hidden-manifestation`、`natal-relation-network`、`natal-ten-god-functions`、`natal-pattern-use-agency`、`natal-synthesis-tensions` 八个原局核心覆盖单元。它们是生活 topics 的上游解释层，不能用四个基础 topic 的 finding 数冒充覆盖；覆盖单元名称不构成 Render 可见标题要求。

### Mode B：五行克应过程复合

先按 [五行克应 Composition Schema v4](references/process-composition-schema.md) 产出 `process-compositions.yaml`。这是八字 Composition 的主要事实脊柱；不得先做符号、柱象或领域故事，再以“旺衰路线修正”补在末尾。

每条 Topic Process Axis 必须先锁定一个完整 `process_ref`，并按以下顺序处理：

1. 继承司令、季节、五行库存、实际可用量与日主承载；
2. 展开 process 的完整 ordered edges、route closure 与 conditions；
3. 逐 phase 说明被动承受、主动发动、主动改道、自治流动、停滞或恢复；
4. 分开日主成本、对主问题的治疗效果、仍未解决的问题与回病旁路；
5. 分开 can-start／can-carry／can-redirect／can-stop；
6. timing／synastry 时用 process before／after 改写当前 phase，再比较 `shared_node_competition → natal_route_retention → overlay_function_transition`；不用符号出现直接推事件；
7. 最后才加入十神关系、柱位、藏干状态、干支物象与现实载体。

十神在这里解释已经成立的五行作用相对日主与领域体意味着什么，不决定 edge 是否成立。若日主供能失败而地支库存／自治供给仍在，两个事实必须同时保留。

### Mode B1：逐柱与藏干着色

产出 `pillar-composites.yaml`，作为 `process-compositions.yaml` 的着色投影。对 Topic Lens 涉及的每一柱，按以下顺序处理：

1. 该柱承载哪些 process／phase；
2. 天干原始物象与气质；
3. 已成立五行作用对应的十神关系；
4. 年／月／日／时柱位职责；
5. 地支场景、季节、动静及全部藏干关系后状态；
6. 天干怎样染色地支，地支怎样提供场景、根基、阻力或去处；
7. 基线、受压、良性、停滞与反向 phase 在本柱怎样表达。

同柱双向着色是 `composition-only`，不是新的生克边，也不是五五对称。它不得独立支持 route、process、用神或 timing 结论；权重须引用显隐、司令、季节、位置、通量和关系后状态。

每个藏干都要列出，但必须区分：库存、根气、环境供给、直接做功、格用资格和岁运待引动。不得因“藏在库中”自动判可用，也不得因“不透”自动判无效。

timing／synastry topic 对每个相关藏干再分开 `natal_visibility` 与 `overlay_visibility`：前者原样引用冻结原局，后者只继承 overlay 重算结果。若接口只是 registered／matched-pending，不得在柱象中写成已发用；若为 active-overlay，仍须说明它在本时间窗持续、间歇、短促或仅关系内成立，以及何时失效。

每个涉及地支的柱另须读取 `post-branch-node-ledger.branch_manifestation_handoffs` 与 Source Packet 的 `branch_manifestation_receipt`，按 `场在／气在／用起／果显` 四层复合。前三层继承冻结结构；`果显`由本技能结合 Topic Lens、载体桥接与现实结果条件裁定。四层不是机械串联：地支场可直接成为环境载体，藏干也可只经根气／环境供给间接影响另一节点。

未达到外部结果门槛时，必须明确保留实际成立的 `field-background／stock-root-support／environmental-feed／internal-latent／direct-function／timing-pending`，不能只写“未显”；反过来，已有 direct-function 也不能省略现实载体和结果条件，直接宣布事情已兑现。

### Mode B2：十神—干支象核合成（强制）

在 process composition 与逐柱着色之后，必须按 [十神—干支象核 Schema v2.0](references/ten-god-stem-branch-kernel-schema.md) 产出 `bazi-scene-kernels.yaml`。这是八字从结构进入断命的核心分析层；不得以 axis scene、问题答案表或 Render 自由发挥替代。

每个 topic 依次完成五步，前三步不得合并成一个 `main_scene`：

1. **spread 材料全摊开**：把相关完整 process、四面 `life_effect_matrix`、十神链各环、透干、四支场、重要藏干、柱位、形成期大运、同柱与跨柱组合、竞争路线、runtime candidate palette 全部列齐，并保留来源与 relation-after-state。
2. **intersect 关系交会**：逐项标明加强、具体化、承载、限制、改道、竞争、矛盾或 context-only；回答十神链怎样传递、流到哪里、由谁承担、怎样反馈，以及候选象为何获得或失去资格。
3. **differentiate 结果拆分**：按 mandatory judgment dimensions 和不同现实端点建立独立 `claim_kernels`。学历层级、专业性质、技术动作、资格／权责、名声、收入、变动、冲突与代价即使共享 process，也不得先压成一个职业大场景。
4. **rank 五级裁决**：L1–L3 有组合支持时必须给方向；L4 比较最多三个载体家族；L5 具体身份可以 `not-claimed`。不得因 L5 不足而删除 L1–L3。
5. **synthesize 场景合成**：在独立 claim kernels 已成立后，才给出主场景、次场景、切换场景、未显化层、最强替代解释与禁止渲染项；说明这些结果怎样同时落在一个人的现实生活中。

Mode B2 的 directional verdict 只能由隔离 producer 在完成 unit disposition ledger 后产生。禁止在 Python／PowerShell／模板字典中预写 `TOPIC_CLAIMS`、`TIMING_CLAIMS`、preferred carrier 或 finding 正文，再按数组位置映射到 mandatory dimensions；脚本只可做路径、hash、集合、schema、ID 和确定性合并，不得生成命理判断文本。

`material_spread_receipt.selected_unit_ids` 必须与 runtime packet 的全部 selected units 集合严格相等。每个 unit 必须唯一标记 `used／counterevidence／context-only／excluded-with-reason` 并保存 claim 回链或具体理由；不得截前 N 项，不得由 producer 手填 `all_chain_links_covered: true` 自证覆盖。每条 directional claim 另须列实际 `support_unit_refs` 与 `counterevidence_unit_refs`，审计须检查引用材料对正文的语义蕴含。

十神与干支的权限固定：

- 十神关系链回答“人与事怎样连接、功能怎样传递、结果被谁接走”；
- 天干回答这条链显性采取什么动作、方式和姿态；
- 地支回答它在哪种场、根基、持续性、阻力和去处中运行；
- 藏干回答未透但已参与的是库存、根气、环境供给、直接功能还是待触发接口；
- 柱位限定人事范围、时间层与生活位置；
- 同柱／跨柱组合只负责相互限定，不能制造冻结结构中不存在的 edge。

任何人物、职业、身份、疾病或事件必须由“完整十神链 + 至少一组干支／柱位组合 + 现实结果门”共同推出。单个十神、单个干支、一个同柱标签或一个通用五行机制都没有独立直断权。相反，若组合已充分支持具体载体，不得因怕贴标签而退回纯性格或抽象机制。

scene kernel 不与 axis 一一对应：多个轴可以共享同一现实场景，一条轴也可产生多个结果端点或相反分支。kernel 数不由 coverage facet、问题或十神数决定，但凡判断对象、现实结果端点、specificity level、载体家族、timing switch 或“外部成就／日主代价”方向不同，必须先拆出独立 claim kernel；之后才允许在同一 scene synthesis 中合写。

### Mode B2.2：Topic Axis 材料投影

逐条处理 Topic Lens 的 primary／supporting Topic Process Axes，产出兼容投影 `axis-scenes.yaml`。事实脊柱仍是 `process-compositions.yaml`，现实断局主单位则是 `bazi-scene-kernels.yaml`；axis scene 只负责把轴材料送入一个或多个 kernels，不得自由重列 edge／route 子集，也不得直接写成报告段落。

每次只处理一条关系轴：

1. 读取 `process_ref`、完整 edge closure、route conditions 与 phase focus；
2. 读取领域体、实际控制者／承载者与适用治疗枢纽；
3. 继承旺衰承载、五行作用、日主成本、治疗效果、剩余问题与回病；
4. 展开相位先后与主动／被动／自治／停滞切换；
5. 再用十神、柱位、相关地支与全部藏干解释本领域关系；
6. 合成基线、被触发、被改道、失败／反转场景；
7. 比较候选载体并记录 `bridge_status`；
8. 指明进入哪些 scene kernel、与哪些其他轴合成；
9. 写明不能从本轴单独推出什么。

每个 axis scene 须回链 coverage facets 与 mandatory judgment dimensions；只在真实问题存在时回链 `reader_answer_contract`。上游必须给足形成、能成什么、代价、结果门、反转和核验材料。不得一 facet 一 finding、一问题一 finding或一十神一 finding，但也不得以“自然闭合”为名，用一条泛化 finding 吞掉不同结果端点。

同一节点的两种方向必须分别成 phase／branch。例如“制病”和“生出回病旁路”不能糊成一条“既好又坏”。八字不使用紫微式全库词条共振，但必须做本盘相关材料的完整摊开与语义合成；完整五行克应过程先于十神链，十神链又先于干支柱位的现实具体化。

### Mode B2.5：原局核心场景与藏干显化矩阵

在详细原局中，于普通 topic finding 前按 [完整原局详批 Schema](references/natal-detailed-reading-schema.md) 产出：

- `hidden-manifestation-matrix.yaml`：逐位置比较重要藏干的原局未透表现、直接功能资格、各类触发接口、重算路径、外部结果门与反条件；
- `natal-core-scenes.yaml`：八个 core sections 的主场景、反向场景、结构张力与禁止推论；
- `cross-topic-claim-registry.yaml`：登记完整展开位置、引用位置和 judgment IDs，防止重复泛化。

同字多处藏干不得合并。`stem_exposure`、`branch_reinforcement`、`directional_completion` 与 `void_fill` 必须分开说明；外来同字提供 overlay 接口时，不得写成原局藏干永久透出。

### Mode B3：象核图与复合载体竞争

`bazi-scene-kernels.yaml` 已是强制主产物；若一个 kernel 使用多组载体竞争，可另产 `resonance-map.yaml` 作为可读投影与竞争收据，保留：

- 每个天干、地支、十神、柱位、藏干和状态分别贡献什么；
- 哪些贡献互相加强、着色、承载、限制或改道；
- 哪些 unit ID 被 Source 排除或只作 context-only；这里只保存排除收据，不读取对应语义正文；
- 主场景、次场景和切换场景怎样由十神链与干支组合共同组成；
- 本题竞争的现实载体，以及各自通过／未通过哪些结构与现实 gate。

具体职业、岗位、正式身份、疾病或事件属于 `composite_domain_carrier`。先按 [领域载体推导](references/domain-carrier-schema.md) 产出并校验 `domain-carrier-resolution-<topic>.json`；不得由单一天干、地支或十神卡升到 `supported`。至少检查领域轴、完整十神链、干支／藏干／柱位组合、可见接口、完整做功路线、日主承载／调用、持续性、去处、现实结果条件与替代载体。十神链决定载体必须完成什么关系功能，干支组合决定它更像哪种动作、场所、材料、角色和落地方式；两者共同参与筛选，而不是等载体定案后才做装饰。

随后为每条 finding 产出 `render_use_envelope`：

- `locked_claims` 与 claim strength；
- `deep_card_runtime_packet_ref`、`selected_unit_ids` 与可选 `domain_carrier_resolution_refs`；
- `excluded_unit_receipts`：只含 context-only／forbidden／source-gap unit IDs 与原因；
- `allowed_linguistic_expansions`：Composition 已从 selected units 明确写出的过程、比喻、配对、状态和共振解释；Render 不再回卡补写；
- `forbidden_new_claims`：不得新增的载体、人物、职业、事件、结构与强度；
- `render_gap_route`：出现上游未组合的新象时回退到哪个 Topic／Source／Imagery 环节。

### Mode C：象核驱动领域 Finding

产出 `topic-findings/<slug>.md`。每条 primary finding 必须对应一个已完成的 scene kernel，并继承它引用的全部 `topic_process_axes`、process compositions 与干支材料；不得强制一轴一 finding。supporting axis 可以进入同一场景的修正层，但不能在未合成时被省略。每条 finding 必须完成：

- `scene kernel handoff`：kernel ID、主场景、次场景、切换场景、十神链、干支柱位组合、独特细节、最强替代与禁止渲染项；
- `answer contract handoff` 仅在真实显式问题存在时建立：contract ID、closure key、原样自然语言问题、answer target、answer status、直接答案 claim 与本领域相对共享机制的新增信息；

- `process handoff`：process ref、phase focus、route closure、完整 edge set、旺衰承载、日主成本、治疗效果、剩余问题、回病与 agency transition；
- `anchor set`：由 process closure 自动投影柱、节点、边、路线和来源单元，不得自由删边；
- `full-chart sweep`：检查其他柱和竞争路线是加强、改写、反转还是无关；
- `composition trace`：旺衰承载、五行克应、route／phase、十神链、天干显性动作、地支场景、藏干层级、柱位人事与现实载体如何依权限逐层合成；
- `use relation`：领域体、用神枢纽、处理对象、支持／损用、去处和日主能动性；
- `expression bands`：基线／受压／条件良好／反向或未显化；
- `manifestation layers`：涉及地支时先引用场在／气在／用起收据，再分内部机制／领域载体／外部结果／时间条件／反向代价；
- timing／synastry 另保留 activation interface → trigger match → edge／route propagation closure → process before／after → overlay manifestation 的链，不得从“原局可能被激活”直跳事件；
- timing／synastry 在 process before／after 后必须另保留共享节点分配、原局主路剩余、临时功能资格、领域关系功能、runtime role branches 与结构影响带；
- 1–30 岁形成期须比较普通在校、供给／带薪教育、单位培养、军校、实习／临床／学徒、边学边做、资格训练与正式任职等兼容场景；财、官杀、印或食伤运不得被机械翻译成“离校／就业／只读书”三选一；
- 足以让命主核对场景是否存在、落在哪类人事、怎样成事、何时转坏的具体生活判断；数量由场景复杂度决定，不得为凑数把同一机制改写成多条性格句；
- 每条独立生活主张分配稳定 `judgment_id`，格式 `J-<FINDING-ID>-NN`，并进入 `render obligations`；
- `interpretive kernel ref`：直接引用 `bazi-scene-kernels.yaml`，不得在 finding 临时重写一份较薄象核；
- `render_use_envelope`，以及实际使用物象／载体竞争时的可选 `resonance map ref`；
- 最强替代解释与禁止渲染项。

一个 finding 可以覆盖多个 coverage facets，也可以服务多个真实 Reader Answer Contracts。每个真实 contract 须分别留下 `direct_answer_claim_id` 和解释职责收据；coverage facets 则留到独立 coverage receipt。finding 数量、judgment 数量或同一 process 被完整解释，都不能自动算作真实问题已经回答。若只写“命主容易如何感受／处理”而没有交代本题的人、事、角色、载体与结果，不能视为合格断局。

表达强度须与 bridge 对齐：`candidate` 只列可能载体，`supported` 可自然写“更可能／偏向”，`preferred` 可置于主判断，`assertable` 才直接定案。没有实际竞争锚点、状态切换、来源冲突或 source gap 时，不要为了显得谨慎机械追加“但是／也不一定”；把真正的转折集中写在 switch scene。

不能只从十神标签跳故事，也不能只讲干支本象而漏掉十神和全局。A 带 B 的特性时，同时检查 B 如何承载或限制 A；但两者权重不要求相等。

full-reading 的四个基础 topic 必须分别拥有独立 finding 文件和稳定 topic ID：

- `family-home`：家庭系统、父母／家庭资源压力、家庭角色、居住和生活环境维持；不自动代替爱情或子女。
- `education-learning`：学习输入、理解与输出、考试资格、专业和教育路径。
- `wealth-resource`：资源、收入、积累、支出、流动性、可见度与变现。
- `career-work`：任务、岗位、组织环境、责任压力、职业发展与成果。

相同结构可跨 topic 引用，但必须说明领域体或体—用关系怎样改变了场景；若完全相同则交叉引用，不复制泛化段落。不得用一条“综合性格 finding”代替四个领域。每个 selected optional topic 也必须有独立 finding。

`detailed-natal` 另必须产出 `natal-core-findings/<core-section-id>.md`。八个 core sections 缺一项，或没有 `hidden-manifestation-matrix.yaml`，不得进入 Composition。

### Mode D：Finding 审计、显化映射与验证接口

先调用 `$bazi-finding-audit` 的 imagery-finding 模式。FAIL 必须退回对应 finding 或 source packet。

完整读取 [经历映射与流运验证协议](../bazi-structure-dynamics/references/validation-protocol.md)，再选择：

1. **不合参**：记录 `manifestation_mapping_state: none` 与 `validation_state: none`，直接进入 composition；
2. **显化映射**：审计后读取经历，产出 `manifestation-map.md`。可记录 matched／conditional／carrier-shift／disconfirmed／new-question／structural-challenge，但必须标 `non-evidentiary: true`；
3. **流运验证**：在读取相关年史前，基于冻结 natal、受审计 timing overlay 与 timing imagery 形成复杂假设，交 `$bazi-finding-audit` 审计并冻结。之后由 `$bazi-render` 收集 verbatim response，再按固定 rubric 生成 scorecard 并重审。

显化映射可以调优先级、语气和领域载体，不能创造新的结构、路线或普遍规则，也不能增加 confidence。验证结果只能评价冻结的时间假设，不反写 natal。

若用户拒绝或没有可回忆材料，记录 `declined`／`unscored` 并继续；不得补写“根据反馈验证”。若详细经历在 blind finding 或 timing hypothesis 冻结前已经进入生成上下文，须在 validation plan 排除／降权；无法隔离时记录 `contaminated` 并放弃验证资格，但可做显化映射。若仍把既有事实写入 finding 或声称盲验证，退回 `$bazi-finding-audit`。

### Mode E：Composition

只使用通过审计的 findings 与可选 manifestation map 产出 `composition.md`；没有 subject context 时明确记录“未做经历映射”，不得虚构验证结果。它负责：

- 先建立 `coverage-receipt.json`：逐 coverage facet 指向实际 scene kernels、findings 与将进入正文的 narrative span；它证明没有漏断，但不规定标题、段落或问答顺序；
- 若本轮存在真实 Reader Answer Contracts，再产出 `question-answer-map.yaml`：逐 `closure_key` 锁定原问题、answer target、直接答案、finding／claim refs、解释职责、领域特有增量、最强替代与最终 Render obligation；不存在真实问题时允许空 map，不得从 coverage facets 反造问题；
- 全盘主锚与若干贯穿人生领域的 storyline；
- 先按五行克应 process 建立旺衰承载、主压力、通关、成本、剩余问题、回病与相位能动性的全盘脊柱；
- 主问题、主要救应与日主能动性的生活化总框架；
- 将十神链—干支象核编织成可连续阅读的主场景，而不是按内部字段依次翻译；
- 各 topic 的 finding 进入哪条 storyline、何处展开、何处回扣；
- 同一十神链在不同柱位与领域体中怎样改变人物、事情、载体和结果；
- 同一结构跨领域的共通点与差异；
- 必须保留的条件、代价、反证和 source gap；
- 后续追问可以继续展开的象意索引；
- 每条 finding 的 process composition、runtime packet／domain resolver refs 与自足 render-use envelope；实际使用物象／载体竞争时再附 resonance map。Render 只消费这些已组合材料，不回读卡片。

完成后再次调用 `$bazi-finding-audit` 的 composition 模式。Render 不得绕过该审计。

full-reading 的 `composition.md` 必须按照 `report-scope.yaml` 建立基础四板块和全部已选专题的 coverage ledger，并另给出服从全盘主线的 reader narrative order、跨专题回扣与自然过渡；二者不得机械等同。缺任一 topic 覆盖不得进入 Render，但 coverage facet 不自动获得可见标题或独立段落。

`detailed-natal` 的 Composition 还必须先按完整原局详批 Schema 建立八类原局内容的 coverage map，再以全盘主锚、关键人生主线和张力关系组织 reader narrative spine；“一句话主轴”只能作入口，不能替代四柱、藏干显化、关系网络、十神、格局用神与能动性的实质内容。八类 coverage 不等于八个可见标题。

每个专题的 reader narrative 由 scene kernels 与全盘 storyline 组织：先选本题最有区分度的一至数条十神—干支因果链，再把 supporting／cross-ref facets 沿主链插入。可见标题只服务读者定位与真正的内容转场，不得为 facet、十神、finding、judgment 或内部解释职责各建一标题。

Composition 允许合并标题和共享结构说明，但不得合并真实 Reader Answer Contracts。每个真实 `closure_key` 都必须能沿 `question-answer-map.yaml` 追到一条直接答案 claim、解释职责材料及唯一 Render obligation。`personality_role` 只能是 explanatory-only／not-used，`advice_role` 只能是 after-answer／not-used；性格画像、建议、技术标签或“这一主题仍由同一主链控制”都不能填入直接答案栏。coverage facets 只沿 `coverage-receipt.json` 验收，不得因没有对应问答条目而失败。

## 职业与行业推导

不得从一个十神直接报行业名称。先按 [领域载体推导](references/domain-carrier-schema.md) 写工作性质，再给行业例子，并分开：

- 行业；
- 岗位／角色；
- 实际工作内容；
- 组织环境；
- 收入机制；
- 可见度、名声和真正变现。

例子只是性质的现实载体，不是命局唯一答案。

## 硬门槛

- 结构未冻结或审计未过：停止。
- full-reading 缺 report-scope、topic-lens-index、基础四镜头或任一已选专题镜头：FAIL。
- detailed-natal 缺任一原局 core section、原局 core finding 或 `hidden-manifestation-matrix.yaml`：FAIL。
- use-kernel 缺失、Topic Lens 未锁定用神枢纽，或 primary axis 没有 axis scene、scene-kernel／finding 去向或 deferred 收据：FAIL。
- 缺 `bazi-scene-kernels.yaml`，或任一 primary finding 没有有效 scene kernel ref：FAIL。
- scene kernel 缺完整十神链、干支／藏干／柱位组合、材料全摊开收据、关系合成、主／次／切换场景、最强替代或禁止渲染项：FAIL。
- 命中 Agent 隔离协议任一强制触发项，却由主 session 直接写 directional verdict／finding，或没有 fresh producer receipt 与独立 auditor PASS：FAIL。
- 复杂象核环境缺干净 agent 却继续生产，producer 继承总 session 历史，或 producer／auditor 读取旧报告、经历、用户纠错、预期答案：FAIL；该结果不得称 blind。
- runtime selected units 与 material disposition ledger 集合不相等、任一 unit 未处置／重复处置／无理由排除、截前 N 项后声称全覆盖，或 producer 写入 `all_chain_links_covered` 自证覆盖：FAIL；覆盖状态只能来自独立 validator receipt。
- directional verdict 来自预写答案字典、批量模板、数组位置映射，或判断文本先于材料 ledger 生成：FAIL。
- scene kernel 由 coverage facet 数、问题数或十神数机械生成，或一轴一 finding 只是字段翻译而未做跨轴合成：FAIL。
- 相关柱漏一天干、地支或任一藏干：FAIL。
- 同柱互染被当成 active edge：FAIL。
- 地支 finding 缺 `branch_manifestation_receipt`，或把 visibility、参与层、direct-function 与 externalized-result 压成同一状态：FAIL。
- timing／synastry finding 缺 matched interface、edge requalification、natal／overlay visibility、scope／expiry 任一收据，或把临时激活写成原局永久属性：FAIL。
- 缺 `structure-process-handoff.yaml`，或 primary finding 缺 process composition／route closure／phase agency：FAIL。
- process 引用 route 却遗漏起始、成本、通关或回病 edge，或 anchor set 与 process closure 不相等：FAIL。
- 上游容量改变但 timing process diff 未传播至同 process 下游 edge／condition／phase：FAIL。
- timing process diff 只有 `reallocated／re-evaluated` 等标签，没有 start gate、throughput、cost、therapeutic effect、rebound 与 agency before／after：FAIL。
- timing／synastry 缺 `natal_route_retention`、`overlay_function_transition`、共享节点分配、结构影响带或 runtime context 分支：FAIL。
- 把临时比劫、官杀、财印功能直接定为同事、上司、客户或导师，而没有领域、位置、可见接口和 runtime role 候选比较：FAIL。
- pillar composite、resonance map、十神或 Deep Card 改写 process state：FAIL。
- 只因对方盘有同字／同五行便写成激活，或接口命中后未重算受影响结构便写 direct-function：FAIL。
- 只写“藏而未显”却删除已经成立的场景、根气、环境供给或内部功能，或把直接做功直接写成外部成果：FAIL。
- 只列符号、不做组合：FAIL。
- 只讲五行 process 而没有十神链，或只列十神再用单个干支贴一个人物／职业／事件：FAIL。
- 打开 Deep Card 母卡、使用 runtime packet 未选择的 unit，或从 context-only／forbidden 排除收据创造、扩大 finding：FAIL。
- 具体职业、岗位、正式身份、疾病或事件没有有效 `domain-carrier-resolution`，或 Resolver 把单张符号卡当充分理由：FAIL。
- 具体职业、岗位、正式身份或事件只由单张天干／地支／十神卡升为 `supported`：FAIL。
- primary finding 缺完整 process composition 或自足 render-use envelope，导致 Render 只能面对压缩结论或需要回卡发挥：FAIL；只有实际使用了物象／载体竞争却未保存 resonance map 时，才因缺图 FAIL。
- finding 的独立可核对生活主张缺稳定 judgment ID，或为凑数量把同一机制拆成重复性格句：FAIL。
- 只讲局部而未做 full-chart sweep：FAIL。
- 把多条用神关系轴压成一条泛化机制 finding：FAIL。
- 宽泛 topic 未建 coverage profile，必查 facets 没有 coverage receipt，或反过来为每个 facet／问题／十神机械建 finding：FAIL。
- 任一真实 Reader Answer Contract 缺用户／scope 来源、自然语言问题、answer target、直接答案 claim、解释职责收据或领域特有增量：FAIL。
- 为内部 coverage facet 自造 Reader Answer Contract，或把 Lens 中的预写答案复制成 finding：BLOCKER。
- 用性格、建议、技术标签、泛化跨专题总结或同一机制复述代替人／事／角色／对象／结果答案：FAIL。
- supporting／cross-ref 没有 `domain_specific_delta`，或复制与其他 topic 相同的直接答案且没有合格共享 closure 引用：FAIL。
- 完整取象来源缺失却写高置信生活故事：FAIL。
- 把有来源且桥接成立的形态、物件或行业候选当作“固定标签”一并删除：至少 WARNING；改变 finding 方向时 FAIL。
- 只因看到一个物象例子便写成命主唯一外形、职业或事件，没有 bridge receipt：FAIL。
- 没有真实竞争证据却用重复“但是／也可能不是”冲淡已支持判断：WARNING；使结论无法核验时 FAIL。
- 用户经历创造新 finding：FAIL。
- 经历在 blind findings 审计前参与生成，或年史在 timing hypotheses 冻结前参与验证命题：FAIL。
- 用一条 general finding 代替家庭、学业、财运、事业任一基础板块：FAIL。
- 行业名先于工作性质：退回改写。
- composition 压掉 finding 的条件、代价或反证：FAIL。
- composition 压掉 process 的 phase 顺序、日主成本、治疗效果、剩余问题、回病或启动／停机状态：FAIL。
- composition 缺 `coverage-receipt.json`，或任一 required facet 无 scene kernel／finding／narrative span 收据：FAIL。
- 存在真实 Reader Answer Contracts 时 composition 缺 `question-answer-map.yaml`，其 closure key 未唯一覆盖全部真实 contracts，或任一 complete／conditional 条目无法追到独立直接答案 claim 与 Render obligation：FAIL；没有真实问题时不得以空问答 map 为由阻断。

## 输出边界

本技能产出可供 Render 使用的分析材料，不直接替用户写最终报告。后续追问若进入新领域，允许增量重跑 Mode A 至 E；不得把首次报告误当成穷尽全部天干地支象意。
