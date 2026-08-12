---
name: bazi-topic-lens
description: 在八字结构、用神太极核与五行克应过程冻结后，为完整原局或限定专题选择领域太极点，建立覆盖账本，并按真实命盘关系组织 process、十神链和干支柱位锚点；只有用户真正提出的具体问题才建立 Reader Answer Contract。用于从技术结构进入家庭、学业、财运、事业、关系、健康、神秘学、创作、岁运或合盘，避免先编问题再预填答案、领域重复泛化、性格画像代替断命。本技能不重算原局、不产生活结论，也不得自由挑选路线 edge 子集。
---

# 八字 Topic Lens

本技能先建立本轮的**领域太极场**：要看哪些人事范围，冻结 process 在这个领域的哪些阶段起作用，哪些十神构成关系链，哪些天干、地支、藏干和柱位能够把关系链具体化。它不预写断语，也不把内部覆盖项伪装成用户提问。

只有用户在当前轮次真正提出、且可以单独回答的自然语言问题才建立 Reader Answer Contract。完整原局中的“收入接口、家庭边界、学习输出”等是 `coverage_facets`，用于保证没有漏断，不得改写成几十个假问题，更不得在 Lens 中写 `external_result_target`、直接答案或倾向性结论。合同字段齐全仍不等于答案成立；下游须用冻结结构、取象材料与 scene kernel 实际完成。

完整专题必须完整读取 [八字现实断语合同 v1.0](../bazi-structure-dynamics/references/semantic-verdict-contract.md)、[读者问题剖面](references/reader-question-profiles.md) 和 [太极场 Lens Schema v4.1](references/taiji-field-lens-schema.md)。前两者规定“最后必须判断什么”，后者规定“怎样组织命盘信号”；它们都不得变成预制答案表，但不得因防止预写答案而删除必须判断的现实端点。

## 必需输入

- `case-manifest.yaml`
- `chart-stage1.yaml`
- `structure-kernel.md`
- `use-kernel.md`
- `problem-state.yaml`、`route-candidates.yaml`、`conditions-matrix.md`
- `structure-process-handoff.yaml`
- `structure-freeze-receipt.yaml`
- 已通过的 structure audit
- `report-scope.yaml` 或用户的限定具体问题

缺少 `use-kernel.md`、`structure-process-handoff.yaml`、结构冻结或审计未通过时停止。若本轮结构文件晚于 freeze receipt，退回结构审计。

## 四层中心必须分开

- **领域体／问题中心**：求测者究竟在问谁、哪件事、哪一种结果。由 `report-scope.yaml` 和当前问题确定。
- **常规符号候选**：传统上与该题有关的十神、柱位或节点，只是检索候选，不自动成为主轴。
- **实际控制者／承载者**：关系后状态里真正组织、占用、改道或承接本题过程的节点、场或路线；它可能不是常规对应星。
- **治疗枢纽**：只在问题询问救应、改善、通关或条件切换时，从冻结的 `use-kernel.md` 选择；描述性、能力性或结果性问题允许记 `not-applicable`。

求测者不需要自选十神、柱位或喜用神。Render 只收自然语言问题；本技能完成技术锁定。

## 固定工作流

### Step 0：建立冻结事实快照

在切 topic 前，用五项短句记录并逐项引用冻结上游：

1. 月支本气、当前司令、季节阶段分别是什么；三者不得合并重复计权；
2. 透干有哪些；
3. 最强地支场是什么，若未决则保留候选；
4. 日主根源与可调用性分别如何；
5. 本题常规对应星的关系后状态、占用和最终去处。

另列与本题候选中心相关的 `process_id`、完整 route closure、日主成本、治疗效果、剩余问题、回病与 phase agency；这一栏只引用冻结 handoff，不重新裁边。

这五项是防断章取义的快照，不是固定打分表。无法从冻结产物确定时写 `undetermined`，不得凭 topic 名称补齐。

### Step 1：建立覆盖账本，并只登记真实问题

先从读者问题剖面建立 `coverage_profile`，并从现实断语合同建立 `mandatory_judgment_dimensions`。例如事业仍须检查职业专业性质、核心技术动作、组织权责、资质、名声、收入、变动、冲突和持续性。它们不是 `question_slice`，不要求报告逐项用“关于……结论是……”作答；但每一维必须在 finding 阶段得到 `directional-verdict／not-applicable／source-gap`，不能仅因共用一条 process 而静默合并。

每个 facet 只登记：

- `facet_id`、需要检查的人事范围与结果层；
- 可能由哪些 topic axis／scene kernel／finding 覆盖；
- `primary`、`supporting`、`cross-ref`、`not-applicable` 或 `source-gap`；
- 本领域相对共用结构新增的对象、载体、结果或成立条件；
- 最终 coverage receipt 应在哪里闭合。

不得为了凑闭合率，把 facet slug、专题名、“完整回答某项”或模型自行扩写的问题注册为用户问题。多个 facets 可以由一条完整场景链共同覆盖；一条复杂 scene kernel 也可以同时照亮多个 topic axes。coverage 数量不得决定 axis 或 finding 数量。

另建立 `explicit_reader_questions`，只收录用户在当前 scope 中确实提出的具体问题。每个真实问题可建立 `reader_answer_contract`：

- `contract_id` 与跨下游唯一 `closure_key`；
- 原样或忠实转述的 `exact_reader_question`；
- `answer_target`：`subject_or_role`、`matter_or_domain_object`、`result_or_outcome`；
- `direct_answer_required: true`；
- `allowed_answer_statuses`：complete／conditional／not-applicable／source-gap；
- `prohibited_answer_substitutes`：personality-only／advice-only／generic-cross-topic-summary／technical-label-only；
- `topic_specificity_required: true`。

Lens 只登记回答义务，不得出现直接答案、偏向性摘要、预选现实载体或下游应复制的结论。完整断局可以没有逐 facet 的 Reader Answer Contract，但不能没有 coverage ledger。

### Step 2：定义领域体

为每个真实专题太极场写 `topic_body`；只有 explicit reader question 存在时，才额外记录该问题的局部焦点：

- 求测者自然语言中心；
- 可能承载该问题的柱位、十神、节点或路线；
- 为什么选这些锚点；
- 最强替代锚点；
- 内部机制、领域载体和外部结果分别指什么。

领域体只是“要看的对象”，不自动等于用神，也不自动等于某个十神。

### Step 3：裁定常规星资格与三类技术中心

先列常规符号候选，再逐个裁定 `star_eligibility`：

- `qualified`
- `diverted`
- `absorbed-by`
- `suppressed-by`
- `not-applicable`
- `undetermined`

裁定必须引用 post-branch state、edge／route、去处和最强替代中心。允许结论为“该星不成主轴；本题主要表现为它被改道、被接管或被压制”。

随后锁定实际控制者／承载者。只有本题意图为 `therapeutic`，或确实需要解释改善条件时，才从 `use-kernel.md` 选择治疗枢纽：

- 主用是否直接处理本题；
- 辅用是否只负责承载／启动；
- 备用路线是否在本题比主用更直接；
- 调候需要是否只改质量而不产结果；
- 哪些看似相关的用神口径必须排除。

记录三类中心之间的比较，不得把“传统上相关”写成“本盘实际主导”，也不得在 Topic 阶段重新发明用神。

### Step 3B：能力桥

题目涉及“有无能力、是否强项、能否产出或形成外部结果”时，逐项检查：

- potential：相关节点／机制是否存在；
- daymaster_access：日主能否启动、承载、改道或停止；
- visibility：是否透出或有现实接口；
- sustainability：是否能持续而非一次性触发；
- destination：做功后流向哪里，是否被财、官杀或其他系统接管；
- external_result：是否具备形成外部成果的现实条件。

不同问题可声明不同必需 gate；“外部结果强”默认六项都须支持，“内部潜能”不机械要求外显。任一必需 gate 未决或受阻时，只能给条件式结论或不主张，不能把节点有气直接写成命主强项。

### Step 4：从冻结 Process 裁切 Topic Process Axes

只列本题真实存在的过程轴。可以围绕实际控制者／承载者，也可以在治疗问题中裁切 `use-kernel.md` 的关系轴：

- 用神自身状态；
- 用神怎样处理主问题；
- 谁生用／助用；
- 谁损用、占用或把用改道；
- 用神做功后流向哪里；
- 用神与日主承载、启动、控制的关系；
- 备用路线如何接力、竞争或反转。

每条 `topic_process_axis` 必须引用一个冻结 `process_ref`、其 `route_closure_receipt_ref` 与一个或多个 `phase_focus_refs`，再写 `domain_focus`、实际控制者／承载者、基线状态、竞争分配和条件开关。只有轴直接服务于真实用户问题时才另写 `explicit_question_refs`。edge／route 只能由 process closure 自动投影，不得人工删选。`therapeutic_pivot_ref` 可以为空；若同一 process 既制病又经旁路生病，按 phase／branch 拆轴，但仍共享完整 process closure。

每条轴另须显式引用：旺衰／承载快照、`daymaster_cost`、`therapeutic_effect`、`residual_problem`、`bypass_and_rebound` 与 can-start／carry／redirect／stop。若日主不能供能但库存或自治子系统仍可运行，必须分别记录，不能合并为“有／无能力”。

每条轴还必须生成两份下游分析计划：

- `ten_god_chain_plan`：领域体、链条起点、各十神在关系后状态中的功能、传递方向、实际终点、回流、竞争、命主能动性与反转条件；不能只列“财官印食”等星名。
- `stem_branch_anchor_plan`：相关透干、地支场、藏干、柱位、同柱与跨柱组合，分别准备用来限定显性动作、场景根基、潜层参与和人事范围；不得在 Lens 中把任何组合预写成职业、人物或事件。

八字不照搬紫微的全库词条压力，但也不能只剩一条抽象五行 process。首要思考单位仍是冻结的五行克应过程；进入现实断局前，必须把该过程转写成完整十神关系链，再由天干、地支、藏干和柱位共同具体化。单个十神、单个字或同柱标签都没有独立直断权。

不设统一最低轴数。轴数由本盘真实关系决定；但每条已列主轴必须在下游进入至少一个 scene kernel 与 finding，或明确记录 `deferred／source-gap`，不得静默消失。多个轴可以共同形成一个 finding。常规对应星若资格不是 `qualified`，不得仅凭题目名称成为 primary axis。

不按问题数或十神数规定统一 axis／finding 数，但对现实端点设硬覆盖门槛。每个 topic 必须列出 coverage facets、`mandatory_judgment_dimensions`、实际关系轴、准备进入的 claim endpoints，以及 `not-applicable／source-gap` 收据。若宽泛 topic 只剩一条轴或一个预定大 kernel，必须回查学历层级、专业性质、技术动作、权责、名声、收入、变动、冲突等不同端点是否被提前压缩。共享 process 可以共用事实脊柱，但不同现实端点必须分别送入 Imagery 的 `differentiate` 阶段。

每个 primary axis 另登记 `explanatory_obligations`：形成、能成什么、附带代价、结果门、反转条件和可核验判断。它是上游材料密度合同，不是 Render 的六段模板，也不要求一轴一段。

full-reading 的覆盖下限使用分 scope 判断维度，不用用户问题或统一 finding 数：

- family-home：家庭资源／责任、家庭角色／边界、居住／生活维持至少逐项检查；
- education-learning：输入吸收、理解／输出、考试、学历／认证层级、专业训练深度、学习连续性及形成期运势至少逐项检查；
- wealth-resource：收入接口、积累／支出、流动性／变现至少逐项检查；
- career-work：职业性质、核心动作／材料、组织／资格／权责、成果／科名、收入接口、单位／岗位变动、冲突与代价至少逐项检查；
- optional topic：按用户 exact question 加领域专属 slices，不得只复用一个 general mechanism；
- 任一项目没有独立结构时写 `not-applicable` 或 cross-ref，不得静默不查。

`expected_scene_kernels` 由可区分的十神链、干支组合和场景反转决定，不等于 facet、axis 或问题数量。多个 axes 可以在同一 scene kernel 中合成；一个 axis 若包含两个互相竞争、结果方向不同的干支组合，也可形成多个 kernels。逐年 scope 中每个独立流年仍至少须有一个自己的 kernel 或明确的“背景态／未外显”kernel。

真实 Reader Answer Contract 数也不等于 finding 数。多个真实问题可共享一条完整 finding，但后续 `question-answer-map.yaml` 必须分别闭合；coverage facets 则进入独立 `coverage-receipt.json`，不能冒充问答。

### Step 5：建立取象请求

完整原局先建立一次 `natal_chart_card_inventory`：列出命盘全部透干、四支、重要藏干及其卡片 ID，并记录哪些只作 context、哪些进入一个或多个 topic axis。它保证 Source 真正读过本盘相关干支材料，又避免每个专题重复把同一套卡伪装成专题差异。

每条轴分别列：

- 两端相关柱的天干、地支、十神、柱位；
- 相关支的全部藏干及关系后状态；
- 同柱双向着色对；
- 主问题、竞争路线、用神去处和条件开关；
- process ref、完整 route closure、phase focus、日主成本、治疗效果、剩余问题、回病与能动状态；
- 需要加载的完整 imagery units，以及它们在十神链中的具体贡献任务；
- 可能的领域载体类型与外部结果所需现实条件；
- 首次未展开、可供后续追问加载的范围。

同时生成 `deep_card_queries`，但本技能只提出查询，不读取或解释卡片：

- 每个 topic 可引用已加载的 `DC-FIVE-ELEMENTS-CORE` 共同语义底座，不得用它独立支撑具体人物、职业或结果；
- 按关系轴端点、相关柱和全部需要展开的藏干，逐项请求对应天干／地支卡；完整原局不得遗漏 chart inventory 中任何实际参与主链或竞争链的字；
- 需要从十神功能进入人物、物件、领域载体或六亲时，请求 `DC-TEN-GODS-CORE`；
- 每项记录 query ID、axis ID、symbol family、symbol／card ID、请求原因、topic axis 与所需来源层；v3 另记录 `requested_unit_classes`、`activation_basis_refs`、`requested_carrier_scope`、`claim_ceiling`、`selection_purpose`、`excluded_unit_classes`、`excluded_uses` 与 `raw_card_access_requested: false`；未请求的 unit class 默认拒绝；
- 不相关的字不因“全库完整”而加载；卡为 `planned` 或缺失时交 Source Lookup 标 `SOURCE_GAP`，不得由 Topic Lens 用模型记忆补齐。

Deep Card query 不能改变常规星资格、实际控制者、治疗枢纽或关系轴。若发现需要在结构冻结前借象意才能选主轴，退回检查 Topic Lens 是否越权。

默认请求当前题需要的 `semantic_core／state_modifier／symbol_carrier`。涉及六亲、同侪、组织关系或具体物件时，`relational_carrier` 不是可选装饰，须引用已经锁定的 topic body、关系口径和参与节点。`deep_card_queries` 不得申请 `composite_domain_carrier`，也不得申请母卡全文进入下游。

职业、岗位、正式身份、疾病或事件另写 `domain_carrier_requests`，但请求必须是开放候选象池：指定领域端点、允许的 specificity levels、process、十神链功能、实际控制者／承载者、位置／可见接口与所需贡献类型，不得先用“流程执行、项目交付、管理”等泛化家族收窄搜索。Source 应返回所有已激活且与这些接口相容的动作／材料象和载体家族；Topic 不预选最终答案，Composition 再比较排序。具体身份资料不足只限制 L5，不得要求下游退回纯机制层。

## 完整原局

`delivery_mode: full-reading` 时，先产 `topic-lens-index.yaml`，再分别建立：

- `natal-core-lens-index.yaml`：按 [完整原局详批 Schema](../bazi-imagery-composition/references/natal-detailed-reading-schema.md) 建立八个 core sections；
- `family-home`
- `education-learning`
- `wealth-resource`
- `career-work`
- `selected_optional_sections` 中的每个专题

四个基础 topic 可以引用同一个实际控制者或治疗枢纽，但必须通过不同的领域体或不同关系轴回答各自问题，并在 index 记录共用的结构原因。若两个 topic 只有完全相同的轴和生活过程，保留一个完整展开，在另一个 topic 建交叉引用；不得复制同一段泛化断语。

八个原局 core sections 不属于可选专题。它们分别解释命盘事实、系统动力、四柱、藏干显化、关系网络、十神功能、格局用神能动性和整体张力；不得用生活 topic 的 finding 反向冒充。

limited-topic 只建立约定镜头，同时记录未覆盖基础板块和“不得称完整断局”。

## 岁运与合盘

- 岁运先按 [Timing／Synastry Scope Seed Schema v1.0](references/timing-scope-seed-schema.md) 从 `report-scope.yaml` 产出最小 `timing-scope-seed.yaml`，运行 `scripts/validate_timing_scope_seed.py`；它只含时间 atom、自然语言题目、领域范围和应读的原局 activation interfaces，不建 process axis、不产 finding handoff。先交 Structure Core 生成并冻结 overlay，然后才产正式 timing Topic Lens。不得用尚未存在的 canonical timing lens 反过来作 overlay 的前置输入。
- 正式岁运 Lens 锁定原局用神核与 `structure-process-handoff.yaml` 后，读取已冻结 timing edge／route diff 及 `timing/year-YYYY-process-state-diff.yaml`，记录哪个 process／phase 的 start gate、throughput、allocation、cost、therapeutic effect、rebound 或 agency 改变；不重写 natal 用神核。
- 每个 timing axis 必须再做 `timing_manifestation_adjudication`：分开原局节点基线、本窗口临时功能、共享节点竞争、原局主路剩余通量、题目中的关系功能、现实载体候选、影响边界与到期撤销。不得用“流年透出某十神”直接跳人物或事件。
- 命主当时职位、角色和组织场景只进入 `runtime_context_policy`：可以改变“同事／同级合作者／竞争者／资源分配参与者”等载体分支及命主可控范围，不能改写结构 diff 或提高结构置信度。位置未知时保留条件分支，不偷猜。
- 用户要求逐年时，每个流年是独立 `scope_atom`：必须有自己的 interaction census、overlay diff、至少一条 primary axis 和至少一条 finding。大运综合 axis 可以总结阶段，但不得替代年度 atoms。若某年只有背景变化，仍产“背景态／未外显”的 finding，不编事件。
- 合盘：双方 natal 分别审计；跨盘节点只作临时接口。可新增 relationship-field 关系轴，但不把对方节点写成本命永久根。
- 直接叠盘必须是 case-manifest 的显式模式。

## 输出

按 [太极场 Lens Schema v4.1](references/taiji-field-lens-schema.md) 产出机器事实源 `topic-lens-<slug>.json`，运行 `scripts/validate_taiji_field_lens.py`，再按需生成 `topic-lens-<slug>.md` 人类可读投影，并维护 `topic-lens-index.yaml`。旧 v2.0–v3.2 产物只读兼容；新产物使用 v4.1，不得与旧状态混合冻结。输出后交 `$bazi-source-lookup` 与 `$bazi-imagery-composition`。

本技能不得：

- 重算旺衰、合化、开库、路线或用神；
- 把领域体直接当喜忌；
- 把月支本气、十二长生或禄地写成当前司令；
- 把题目常规对应星强制设为主轴；
- 把节点强度直接等同于命主可调用、可持续或可外显的能力；
- 只写“压力、资源、支持、输出”而没有明确端点和过程；
- 自由挑选 edge／route 子集，遗漏 process 的启动、成本、通关或回病边；
- 把 route 存在写成 start gate 已开启，或把库存／自治流动写成日主主动调用；
- timing 轴缺 process before／after 与 propagation closure；
- timing 轴缺原局剩余主路、共享节点竞争、影响边界或 runtime context 分支；
- 把“原局永远大于岁运”或“岁运必然覆盖原局”当通则；
- 产生活断语；
- 把 coverage facet 改写成模型自问自答的 Reader Answer Contract；
- 在 Lens 中写直接答案、倾向性结论、预选现实载体或供下游复制的结果字段；
- 用问题数或 facet 数决定 axis、scene kernel 或 finding 数；
- 只列十神名称而不规划关系链，或只列干支而不说明它在链条中的限定作用；
- 读取 Deep Card 内容、替 Source Lookup 生成象意，或让卡片候选反向改变冻结主轴；
- 用固定轴数替代实际结构。
- 用英文 facet、专题名或“完整回答某项”冒充读者问题；
- 真实用户问题存在，却不登记 Reader Answer Contract 与下游闭合键；
- 把性格画像、行为偏好、改善建议、技术标签或跨专题总括设为最终答案目标；
