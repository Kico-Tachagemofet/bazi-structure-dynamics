# 八字 Composition Schema

`composition.md` 是通过审计的 findings 到最终报告／对话之间的总骨架，不是第二次自由断盘。

v4.1 Composition 必须同时遵循 [八字现实断语合同 v1.0](../../bazi-structure-dynamics/references/semantic-verdict-contract.md)、[十神—干支象核 Schema v2](ten-god-stem-branch-kernel-schema.md) 与 [问题—答案闭环 Schema v2](question-answer-closure-schema.md)。claim kernel 是不同现实结果端点的最小保真单位，scene kernel 负责把它们合成现实画面；Reader Answer Contract 只闭合用户真实提出的问题。finding、judgment、process、facet、问题和标题的数量都不要求相等。

v3.1 Composition 必须同时遵循 [五行克应 Composition Schema v3.1](process-composition-schema.md)。它先组织完整五行过程，再组织十神、柱位、物象和领域；symbol resonance 不再是分析脊柱。

`delivery_mode: full-reading` 且未显式选择摘要时，另必须遵循 [完整原局详批 Schema](natal-detailed-reading-schema.md)。生活 topics 之前先核对八个原局 core coverage units，并把它们接入全盘主锚与叙事主线；不能把结构核压缩为“一句话主轴”后直接进入家庭／事业。coverage units 是内部完整性边界，不是八个可见标题。

## 必需部分

### 1. Freeze and Coverage

- case ID 与 structure freeze ID
- report-scope 与 topic-lens-index refs
- 每个 topic 的太极场、coverage facets、axis dispositions 与 scene-kernel handoff
- 真实 Reader Answer Contracts、closure keys、answer targets 与 domain-specific deltas；若没有真实问题则为空
- use-kernel 与各 topic 用神枢纽／关系轴 refs
- `structure-process-handoff.yaml`、全部 `process-compositions.yaml` 与 process freeze／hash refs
- timing／synastry 时逐窗 `process-state-diff` 与 propagation closure refs
- timing／synastry v3.1 的 `natal_route_retention`、`overlay_function_transition`、shared-node competition、structural impact bounds 与 runtime-context policy refs
- delivery mode 与 reading center
- 已审计 topic findings 清单
- imagery source packet 清单
- Deep Card runtime packet、validator PASS receipt、`bazi-scene-kernels.yaml`、领域载体 resolution，以及实际生成的 resonance map 清单／明确 `not-used` 收据
- manifestation mapping 与 evidence validation 是否存在，以及各自边界
- 未覆盖、可供后续追问的象意范围

### 1A. Coverage Receipt

先生成 `coverage-receipt.json`，逐 facet 保存：

- topic／facet ID 与 reader relevance；
- 实际覆盖它的 scene kernel、finding、claim 与 narrative span；
- primary／supporting／cross-ref／not-applicable／source-gap disposition；
- 本领域相对共用结构新增的人、事、载体、条件或结果；
- 是否已保留形成、能成什么、代价、结果门、反转和核验材料。

coverage receipt 只证明没有漏断，不产生直接答案、标题或段落模板。

### 1B. Question Answer Map

只有真实 Reader Answer Contracts 存在时才生成 `question-answer-map.yaml`，逐 `closure_key` 保存：

- exact reader question 与 answer target；
- answer status、direct answer summary 与独立 claim IDs；
- finding／source／process refs；
- formation／advantage／cost／result-gate／switch／verification 六类 obligation refs；
- domain-specific delta、shared mechanism／answer refs、strongest alternative；
- personality 与 advice 的从属角色；
- 唯一 render obligation ID。

`complete／conditional` 条目必须先有直接答案，随后才是性格解释或建议。`not-applicable／source-gap` 必须说明理由，不得伪造结论。不存在真实问题时允许空 map；不得从 coverage facets 反造合同。具体字段和机械门槛见问题—答案闭环 Schema。

### 2. 一句话主轴

用生活语言概括旺衰承载、主压力过程、真实通关、日主成本、剩余问题、回病与相位能动性。不得省去“系统能运行”“日主受益”“日主能启动”“日主能停止”之间的区别。

### 3. 五行克应过程脊柱

先逐 `process_id` 列出：

- 旺衰、司令、实际可用量与日主承载；
- 完整 ordered edge／route／condition；
- 被动、主动、自治、停滞与恢复 phase；
- 日主成本、治疗效果、剩余问题与回病；
- start gate、分配竞争、反转和停机条件；
- timing 时的 before／after 与 expiry。

不得从柱象、十神或 resonance map 重建另一个缩短版本。

### 3A. 十神—干支象核与核心复合画面

引用 `bazi-scene-kernels.yaml` 列出由本盘真实材料形成的复合画面；不设固定数量。每个画面必须引用完整十神链、干支／藏干／柱位组合、relation axes 与 finding IDs，说明：

- 哪个 process／phase 以及哪些柱共同构成；
- 它的基线、受压和良性版本；
- 哪些条件使它改道；
- 哪些材料互相加强、具体化、承载、限制、改道、竞争或矛盾；
- 哪些领域只是同一结构的不同载体；
- 同一用神在不同领域体上为什么形成不同结果，或为什么只能交叉引用而不应重复。

### 3B. Symbol／Carrier Context

resonance map 降为可选的措辞／载体收据。若使用，逐 finding 引用 `resonance_map_id`，保留每个干支、十神、柱位、藏干和状态对已锁定 process 场景的具体贡献。另列：

- activated units 与实际进入结论的路径；
- excluded/context-only unit IDs 与排除理由；不得包含其语义正文；
- 未采用的竞争载体及淘汰原因；
- 具体职业、岗位、身份或事件通过的复合 gates；不得由单张符号卡升格。

### 4. Topic Coverage and Narrative Order

每个 topic 记录：

- coverage facets 的处置与 scene-kernel／finding／narrative-span refs；
- mandatory judgment dimensions 的处置、claim-kernel refs、specificity verdicts 与唯一完整展开位置；
- 真实 Reader Answer Contract 顺序、每个问题的 direct answer claim 与最终闭环位置；若无则为空；
- finding 顺序；
- 它在 reader narrative spine 中归入哪条全盘主线，前后承接什么；
- relation axes 怎样聚合进 scene kernels；
- process ref、phase focus、route closure 与本领域 process composition；
- 开场 hook；
- 必须展开的原始象意；
- 不得丢失的条件、代价和反证；
- 交叉引用位置；
- 可见成果需要的额外现实条件。
- 涉及地支时，场在／气在／用起／果显分别由哪个 receipt 支持，以及没有外部结果时仍保留哪种表达。
- timing／synastry 时，原局 process、matched activation interface、propagation closure、process before／after、持续方式与 expiry 分别由哪个 receipt 支持；不得把 overlay 语句合并进原局基线。
- coverage profile 的每个必查 facet 在何处以 primary／supporting／cross-ref／not-applicable／source-gap 被处置；
- 形成、能成什么、代价、结果门、反转与核验材料在哪个 scene kernel／finding 完整保留；
- 主场景、次场景与切换场景。

full-reading 的 Topic Order 必须先核对：

1. family-home
2. education-learning
3. wealth-resource
4. career-work
5. report-scope 中全部 selected optional topics

coverage 清单不得缺项，也不得把四个基础 topic 合并为 general；reader narrative order 可以为叙事调整、让多个 topic 相邻共用一个主线标题，但必须在正文保留每个 topic 的独立人事范围、载体与结果。只有真实问题需要 question marker。

facet、十神、finding 与解释职责的数量不决定可见标题数量。Composition 必须先把它们合成数条因果连续的主论证，再交 Render；不得把内部覆盖表直接交给读者。

`detailed-natal` 在 Topic Order 前另核对八个 `core_section_id`、`natal-core-findings`、`hidden-manifestation-matrix.yaml` 与 `cross-topic-claim-registry.yaml`。每个独立生活主张的 judgment ID 必须进入 Render Contract；不设每个 finding 的固定数量。

### 5. 张力与反向表现

不得只写优势。把同一结构的：

- 自然倾向；
- 被环境倒逼的表现；
- 有支援时的高质量表现；
- 过量、阻塞或改道后的代价

分开列出。

### 6. 领域载体地图

先写性质，再写例子。职业类必须区分行业、岗位、任务、组织环境、收入机制、可见度和实际变现；健康与神秘学必须保留证据边界。

### 7. Render Contract

逐 finding 写内部 handoff；这些字段不直接构成读者版模板：

- reader block ID；不是可见 section 标题配额
- verifiable judgments
- 每条 judgment 的稳定 ID 与唯一完整展开位置
- topic body／use pivot／relation axis
- scene kernel ID、完整十神链、干支柱位组合与 material-spread receipt
- process ID／process composition／phase focus／route closure
- main scene／secondary scene／switch scene
- strength → elemental action → phase／agency → ten-god relation → carrier → result expansion order
- daymaster cost／therapeutic effect／residual problem／bypass and rebound
- mandatory imagery
- mandatory condition and cost
- technical trace refs；完整进入 marker／receipt，读者版可低干扰呈现或按需展开
- prohibited compression
- confidence tone
- `render_use_envelope`：locked claims、runtime packet ref、selected unit IDs、领域载体 resolution refs、已物化的允许语言展开、禁止新增结论与 render-gap 回退路径
- `high_contrast_explanation_required`、signal refs、读者必须分辨的关系；仅在确实提高清晰度时建议矩阵／清单／before-after
- `coverage_obligation`：facet refs、scene-kernel／finding refs 与 narrative span target
- `reader_answer_obligation`：仅真实问题使用；contract ID、closure key、原样问题、direct answer claim IDs、解释职责 refs、domain-specific delta、唯一正文 marker 与 receipt target

### 8. Q&A Expansion Index

为后续聊天建立索引：

- 已可直接解释的问题；
- 需要补充 imagery source 的领域；
- 需要新 Topic Lens 的问题；
- 必须退回 timing／synastry／structure audit 的问题；
- 已知 source gap 与争议。

## 审计规则

- composition 中每个实质判断必须至少引用一个 finding ID。
- `coverage-receipt.json` 必须覆盖每个 required facet，并指向 scene kernel、finding 与正文位置。
- 存在真实 Reader Answer Contract 时，`question-answer-map.yaml` 必须唯一覆盖每个 contract；每个 complete／conditional 条目必须有非空 direct answer、独立 claim ID、解释职责 refs 与唯一 Render obligation。没有真实问题时不得因空 map 失败。
- 性格、感受、建议、技术标签或跨专题泛化总结不得填入 direct answer；它们只能解释已给出的答案或置于答案之后。
- supporting／cross-ref 未保留领域特有增量，或多个 topic 复制相同 direct answer 而没有共享 closure 与不同 delta 时不得进入 Render。
- composition 中每个主 finding 必须引用一个完整 process composition；process closure 与 finding edge／route 投影必须一致。
- composition 中每个主 finding 必须引用完整 process composition 与 render-use envelope；不能只给 Render 压缩结论，也不能把整卡无门禁交给 Render。只有 finding 实际使用物象／载体竞争时才必须引用 resonance map；未使用时写 `resonance_map_status: not-used`，不得为满足格式虚构符号主轴。
- composition 中每个主 finding 必须引用通过校验的 scene kernel；缺十神链、干支组合或 material-spread receipt 不得进入 Render。
- runtime packet 未选择的单元不得成为新判断、载体升格或 confidence 提升的依据；Composition 不得打开 Deep Card 母卡。
- 不得以“为了整体流畅”为由合并掉独立 finding 的实质内容；多个 finding 可以共享一个可见标题，但各自 marker、judgment 与 claim body 必须完整。
- 不得以“共享同一 process／scene”为由合并掉学历层级、专业性质、技术动作、权责、名声、收入、变动、冲突或代价；它们可以共用根因说明，但每个现实端点仍须有有方向的正文。
- L5 具体身份未达到门槛时，Composition 必须保留已经通过的 L1–L4，不得把整题降为抽象机制。
- 不得只保留结论而删除它的形成层次。
- 不得把五行克应脊柱降成“符号共振后的旺衰修正”；十神、柱位、物象与 Deep Cards 不得改写 process state。
- manifestation mapping 只能改变呈现顺序、语气、领域载体或后续问题，必须标 `non-evidentiary`，不得改变结构方向或 confidence。
- evidence validation 必须引用冻结 timing hypotheses、verbatim response、scorecard 与 score audit；其 verdict 与 structure audit 分栏，不得混成“已校准所以结构正确”。
- timing／synastry composition 缺 overlay audit／freeze、把 projected activation 写成当前事实，或把临时状态回写 natal 时不得进入 Render。
- timing／synastry composition 缺 process state diff／propagation closure，或上游变化未传播至同 process 下游时不得进入 Render。
- timing／synastry composition 缺原局主路剩余、临时功能资格、共享节点分配、结构影响带或 runtime role branches 时不得进入 Render。
- 宽 topic 只有一个泛化机制、必查 facets 未处置，或为每个 facet／问题／十神机械建 finding 时不得进入 Render。
- 宽 topic 的 mandatory judgment dimensions 未逐项 `directional-verdict／not-applicable／source-gap`，或只回答“怎么做事”而未回答“达到什么层级、靠什么性质与动作、形成什么现实结果”时不得进入 Render。
- 任一 process 的 phase 顺序、日主成本、治疗效果、剩余问题、回病或启动／停机状态被压掉时不得进入 Render。
- 经历提前进入 blind finding，或年史提前进入 timing hypothesis 时属于污染，不得由 composition 自行圆回。
- full-reading 缺基础四板块、太极中心或已选专题时不得进入 Render。
- detailed-natal 缺任一原局 core section、藏干显化矩阵或 judgment coverage registry 时不得进入 Render。
- 岁运 finding 缺 `external_forcing／subject_agency／non_controlled_outcome`，或用“主动调整”掩盖外部推动时不得进入 Render。
- 后续追问可以新增经审计 finding；首次 composition 不代表全盘象意已经穷尽。
