---
name: bazi-structure-core
description: 分阶段建立四柱八字的结构动力模型：逐位置评估天干与藏干，完整枚举生克合冲刑害方会合局，裁决地支状态和节点占用，限定作用边通量，再锁定主问题、实际吞吐、日主承载、自治子系统、格局候选、端点一致的结构化路线、条件矩阵、结构核、后置用神太极核与可供 Composition 无损消费的五行克应过程。用户询问旺衰、通关、格局、用神、藏干起效、合化、墓库、路线、岁运过程变化或既有结构遗漏时使用。必须接收 Reader 和 Source Packet，不直接写生活故事。
---

# 八字 Structure Core

本技能是分析引擎，不是一次性解盘器。严格按模式产出中间文件；每个模式完成后停止或显式进入下一模式。

## 必需输入

- case-manifest.yaml
- chart-stage1.yaml
- chart-stage1-audit.md
- source-packet.md

Stage 1 为 FAIL 时停止。Source Packet 有缺口时，允许枚举事实，但不得对缺证据事项给高置信度裁决。

## 固定执行顺序

详细字段见 [Core artifact schemas](references/core-artifact-schemas.md)，用神太极核见 [Use Kernel Schema](references/use-kernel-schema.md)，状态词见 [State vocabulary](references/state-vocabulary.md)；另须完整读取 [八字现实断语合同 v1.0](../bazi-structure-dynamics/references/semantic-verdict-contract.md)。结构到下游的过程事实按 [五行克应过程 Handoff Schema v4](references/five-element-process-handoff-schema.md) 交付，岁运／合盘在冻结原局之上另按 [Activation Overlay Schema](references/timing-synastry-activation-overlay-schema.md) 建临时覆盖层。

### Mode A：Node Ledger

逐一记录四个天干和每个地支藏干。不得先聚合重复支或同五行。

产出 node-ledger.yaml，至少含：得令、根型、透藏、来源、克泄耗、位置、空亡、调候环境、支局候选、当前占用与反证。

### Mode B：Interaction Census

先全枚举，后谈权重。检查：

- 天干生克合与相邻／隔柱；
- 同柱干支；
- 六合、六冲、刑、自刑、害、破；
- 三合、半合、方会及共享支竞争；
- 重复支；
- 藏干候选关系；
- 中间节点阻断和岁运待补条件。

必须以 Reader 的确定性枚举结果初始化 `interaction-census.yaml`，把它作为关系候选的事实基线，而不是只作提示。Structure 可以裁关系形式、竞争、通量与残余功能，但不得凭记忆另增一个 Reader 未枚举的合、冲、刑、自刑、害、破、重复支或方会／三合候选；若确有来源争议，先登记 source gap 并回到 Reader／规则包。重复支与自刑是两个不同事实：重复的卯、寅、子等只登记 `repeated_branch`；本链采用的自刑成员为辰、午、酉、亥，同支重复时才另登记 `self_punishment`。岁运加入临时支后须把原局支与临时支一起重新枚举，再进入关系裁决，不能手写 overlay 关系清单。

规则卡在本阶段只可按 `propose` hook 为候选关系补充来源标签；不得提前裁关系主形式、通量或四维效果。待审卡只能生成 source query，不得写结构候选。

### Mode C1：Branch Relation Census

从 Interaction Census 单独抽取并重新核对所有地支关系：三会、三合、半合／拱合、六合、六冲、刑、自刑、害、破、重复支及共享支。每一类别无命中时也必须留下 negative scan；不得让地支关系淹没在大量五行候选边中。

产出 branch-relation-census.yaml。覆盖未通过时不得进入 Mode C2。

### Mode C2：Branch Arbitration

对每组地支关系分别判断完整度、旺支、紧贴、月令、空亡、冲刑破损、共享节点和流派优先级。

分开记录：

1. 形式上的支局状态；
2. 成局后仍保留的本气和功能边；
3. 同一节点被多条关系占用的比例性限制；
4. 原局潜伏与岁运引动。

每张裁决卡必须说明该关系如何改变成员支与逐个藏干，而不只描述关系本身。分别裁定：形式成立度、实际通量、合绊／集中／改道／冲动／受损／转化、残余功能，以及旬空和“不自动开库”这两个独立条件。

产出 branch-state.md。有未解决共享节点竞争时不得进入 Mode C3。

### Mode C3：Post-Branch Node Ledger

把 Mode C2 的裁决逐节点写回，产出 post-branch-node-ledger.yaml。必须覆盖原 Node Ledger 的全部天干和逐位置藏干；没有受到地支关系影响的节点也要显式标记 retained／unchanged。

每个节点至少写明：pre-state 引用、关系引用、关系后身份与可用度、根型变化、透藏／显隐状态、允许参与的功能范围、direct-action gate、显化依据束、分配上限、反证与置信度。显化依据束必须并看司令／气序、透出接口、位置、关系后支局、占用竞争、承接与去处；任一单项不得自动放行。

对当前为 hidden／latent 或仅保留 `timing-only` 的节点，另登记 `activation_interfaces`：当前原局状态、可识别的触发类别与签名、若命中应从哪个阶段重算、可能受影响的 branch／node／edge／route condition，以及最强反条件。接口只预登记重算入口，不裁哪一年、哪一个人必然触发，也不把未来候选写成当前事实。

藏干存在、提供库存／根气、环境供给、直接做功和成为格用是不同层级。冲不负责把藏干“释放”为明干；同支藏干也不得仅凭五行相生克自动获得 active direct-action gate。

但“不透”本身也不是把藏干一律降为 conditional／weak／forbidden 的充分理由。有原典人元规则、得令本气、位置近、同气透出、重复根群或成势支持时，藏干仍可获得 allowed direct-action gate；其实际容量留到 Mode D 裁决。即使 direct-action gate 不成立，root-support／environmental-feed 仍须单独保留，不能因删除伪直接边而抹去。

逐节点回写后，按每个地支位置另建 `branch_manifestation_handoffs`，分开记录 `field_layer`、逐藏干 `qi_layer`、`function_layer`、`activation_interface_refs` 及留给 Topic Lens／Composition 的 `result_handoff`。Structure Core 只裁场、气和功能的结构资格，不裁现实载体或外部结果；四层是分栏，不是必须依次串联的单一路径。

覆盖不足、共享节点未分配、或任一变化没有回链到 branch-state 时，不得进入 Mode D。

### Mode D：Edge Qualification

只允许从 post-branch-node-ledger.yaml 起边。原 node-ledger.yaml 仅用于追溯 pre-state，不得作为 availability 的当前事实源。

每条边标记为 candidate、active、weak、blocked、occupied、redirected、conditional 或 inactive。Stage 2B 内部固定按以下顺序执行，不得以书页顺序、卡号顺序或生成便利改序：

1. `2B.0 edge-candidate`：从 Interaction Census 与 Post-Branch Node Ledger 建立候选边；
2. `2B.1 relation-form`：只裁克／合／并存／未决等关系主形式；
3. `2B.2 competition-arbitration`：比较距离、位置、先后、中介与共用节点的竞争；
4. `2B.3 allocation`：写入节点占用和分配上限；
5. `2B.4 residual-capacity`：在竞争与占用之后裁剩余做功能力；
6. `2B.5 effect-dimensions`：分别裁目标形质实损、目标功能制抑与第三方保护候选；
7. `2B.6 finalize`：完成状态、容量、最弱条件和反证，才产出最终 Edge Map。

只允许使用 Source Packet 已登记、状态为 `approved`、hook 与依赖均匹配的规则卡参与 `decide`。每条边必须保留阶段 trace 和 rule application receipt。`pending_human_review` 卡只能触发回读或 SOURCE_GAP，不得改变任何结构字段。

分别检查：

- 上游可用量；
- 连接距离和先后；
- 中间是否受合、冲、制、泄；
- 调候与环境；
- 下游承接能力；
- 与其他路线的竞争；
- 是否把药重新导回病处。
- source／target 的 post-branch state 引用；
- edge layer：direct-action／root-support／environmental-feed／branch-relation／composition-only；
- direct-action gate 是否允许该层级节点起边；
- branch-state 已判 suppressed／occupied／redirected／conditional 的变化是否被继承。
- 关系形式、目标形质实损、目标功能制抑和第三方保护是否分栏；“作合论”不自动清零后两者，“能制”也不自动等于把目标克掉。
- 规则卡是否只在声明的 hook 写入允许字段；`depends_on` 是否已经完成，`may_not_decide` 是否未越界。

“有根”“有箭头”“五行齐”都不能直接判畅通。产出 qualified-edge-map.yaml。

若完成 `2B.0–2B.6` 后仍存在会改变路线或 topic 关系轴的克合争议，不得凭生活经历现场选边。产出 `structural-ambiguity-register.yaml`，逐项记录 ambiguity ID、共享节点、候选 relation-form、各自 edge refs、已穷尽的来源／位置／力量证据、仍未决原因、分支后果、可辨别条件和禁止回写范围。无真正分支差异时不得登记争议。

### Mode E：System State

在节点和边审计完成后，才聚合为：

- 五行／十神库存；
- 实际吞吐；
- 蓄积点；
- 最弱环与主堵点；
- 日主承载力；
- 启动权、控制权和停机能力；
- 自治子系统；
- 正反馈、负反馈和旁路；
- 调候状态。

产出 system-state.md。身强身弱只是其中一项。

十神在本阶段先作为日主相对关系标签与库存索引，不携带固定吉凶。每个实际功能必须引用已限定的 node／edge：同一十神可同时泄身、生助、制约、通关、改道或经旁路回病，也可因占用、距离和承接不同而不起该功能。不得从“伤官／印／财／官杀”等名称直接宣布它是药、病、能力或事件。

### Mode E2：Primary Problem Arbitration

在比较救应和出口前，先产出 `problem-state.yaml`，锁定本轮的首要矛盾。至少列：主问题、次问题和非问题，受影响的核心节点，直接压力边与维持反馈，日主承载与系统自治的关系，判定证据、最强反证、置信度，以及什么变化会令主问题改判。

后续所有路线必须评价“对该主问题的净作用”。没有 problem state 时，不得使用“救应、出口、药、病、优先”这些词。

十神功能的利弊只在主问题锁定后裁决。同一十神至少保留：当前功能边、实际通量、对主问题的净效果、代价／旁路、最强反证和反转条件；不得用“某十神通常怎样”覆盖本盘路线。

### Mode F：Pattern and Structured Route Matrix

按不同来源分别列格局候选，不静默混派。检查格局的成、败、救应、太过、不及、清杂、变化、相神和生克先后。

同时枚举所有竞争路线，不只写熟悉的格局术语。路线文件只引用 `qualified-edge-map.yaml` 的 edge ID，不得手抄或改写端点。每条路线分开记录实际通量、对主问题的净作用、治疗优先级、现实成立度、代价、旁路、反馈和成立条件。

产出：

- pattern-candidates.md
- route-candidates.yaml
- route-edge-endpoint-map.yaml：由审计脚本根据 Edge Map 展开，只作校验视图
- conditions-matrix.md

`conditions-matrix.md` 对每条主路线列原局状态、必要条件、最弱环、可触发的外部节点、反转节点和成立先后。新增岁运节点只是条件接口，不是本阶段预测。

实际通量最大不等于最能解决主问题。加重主问题的路线必须标 `aggravating`，不得进入 rescue／outlet 排名；混合路线必须分别写收益和回病旁路。

证据不足时保留多候选，禁止强行给唯一格名。

已登记结构争议必须为每个分支分别建立 route／condition refs；不得用一条混合路线把“合主”和“克主”压成模糊结论。Structure Kernel 与 Use-God Kernel 可保留条件分支，但不得提前读取经历选边。

### Mode G：Structure Kernel

只收束技术结构：

1. 主组织／主压力；
2. 有效支援；
3. 主要瓶颈；
4. 可用出口；
5. 关键反馈；
6. 启动与控制；
7. 条件开关和最强反证。

每项须引用 `problem-state`、node、edge、route 和 source rule ID。产出 structure-kernel.md；此时技术结构已收束，但尚未完成后置用神太极锁定。

### Mode H：Use-God Kernel／用神太极核

读取 `problem-state.yaml`、`pattern-candidates.md`、`route-candidates.yaml`、`conditions-matrix.md` 与 `structure-kernel.md`，按 [Use Kernel Schema](references/use-kernel-schema.md) 产出 `use-kernel.md`。

本模式必须：

1. 分开格局用神、病药／制化主用、扶身辅用和调候需要；不静默混派；
2. 先按主问题确定“最需要解决什么”，再判断主用当前是否真能起效；
3. 分开主用、辅用、备用路线与损用／占用／改道因素；
4. 把主用与病神、生用、损用、去处、日主能动性及备用路线之间的**实际关系轴**逐条列出；
5. 同一节点的竞争用途分别成轴，记录分配冲突，不用一句“有利有弊”代替；
6. 只引用冻结前的 node、edge、route 与 condition，不新增生活故事或行业结论。

用神太极核是后续 Topic Lens 的结构中心，不是最后一句“喜某五行”。完成后调用 `$bazi-finding-audit`；`use-kernel.md` 必须与其他结构文件一起审计并冻结。

### Mode H2：五行克应过程 Handoff

读取 `system-state.md`、`problem-state.yaml`、`qualified-edge-map.yaml`、`route-candidates.yaml`、`conditions-matrix.md`、`structure-kernel.md` 与 `use-kernel.md`，按 [五行克应过程 Handoff Schema v4](references/five-element-process-handoff-schema.md) 产出 `structure-process-handoff.yaml`。

本模式不新增作用关系，只把冻结候选中的完整过程闭合交付给下游。每个 process 必须先写旺衰与承载背景，再写完整有序 edge、路线条件、被动／主动／自治／停滞 phase、日主成本、通关效果、剩余问题与回病旁路。随后分开记录它对日主承载、客观产出、社会兑现和持续代价四面的影响。`therapeutic／aggravating` 只裁相对主问题的方向，不得被下游误读为学历、事业、财富或社会成就的高低。十神只记录各 edge 相对日主的实际关系，不得取代五行作用或决定吉凶。

任一 process 引用 route 却遗漏其起始、成本、通关或回病 edge，或只写“系统可运行”而未分开日主受益、启动、改道和停机时，不得冻结。`structure-process-handoff.yaml` 与其他结构文件一起进入 Structure Audit 和 freeze。

### Conditional Mode I：Timing／Synastry Activation Overlay

只在原局已审计冻结，且 Topic Lens 从 `report-scope.yaml` 产出最小 `timing-scope-seed.yaml` 或 `synastry-scope-seed.yaml` 后运行。scope seed 只锁时间／关系 atom、自然语言题目中心、领域范围与待查 interface，不包含正式 process axis 或 finding handoff。读取原局 `activation_interfaces` 与本轮外来干支，按 [Activation Overlay Schema v3.1](references/timing-synastry-activation-overlay-schema.md) 匹配触发接口，并把受影响的 Branch Arbitration、Post-Branch Node Ledger、Edge Qualification 与 route conditions 作为差分重算。

用户要求逐年时，每一个流年必须先在 scope seed 成为独立 `timing-annual` atom，再分别产出全量 interaction census、overlay diff 与 `timing/year-YYYY-process-state-diff.yaml`。大运综合结构只负责说明十年背景，不能替代任何年度重算；不得把多个年份压进一条 sequence axis 或一个 finding。年度重算必须保留仍成立的原局关系，同时完整枚举大运、流年新加入的关系与共享节点竞争。只要上游 availability、allocation、residual capacity 或 start gate 变化，必须沿 `structure-process-handoff.yaml` 传播到同 process 的全部下游 edge、route condition 与 phase；未改变者须有逐项继承收据。出现四个以上同五行节点、多组冲刑并发或一个节点多重占用时，强制输出 `high_contrast_structure`，并向 Composition 交付旧结构、外部逼迫、命主能动、非命主可控结果四栏。

每个受影响 process 另必须产出 `natal_route_retention`：实际比较原局主路 before／after 通量、共享节点分配、仍成立 phase 和备用路线。每个 matched natal node 产出 `overlay_function_transition`：分开原局参与层、本窗口临时功能资格和向 Topic 交付的 claim ceiling。禁止用“原局总能压住”或“岁运一来必冲掉”代替重算。

匹配接口不等于激活完成；激活完成也不等于现实事件已经发生。另一人的干支只有在双方 natal 已分别冻结、跨盘关系成立且本题确实调用该关系场时，才可作为临时 trigger node。产出 overlay、审计并冻结后，才回到 Topic Lens 产正式 timing／synastry typed state，然后交 Source／Imagery；覆盖期结束只撤销临时差分，不回写原局显隐、根气或永久边。

## 不可跨越的边界

- 不把关系存在等同于力量足够。
- 不把图上成环等同于真实流通。
- 不把冲等同于开库，不把合等同于化。
- 不把所有藏干同等引动。
- 不让 Edge Map 绕过 Branch Arbitration 回读原始节点。
- 不在 route 中重写 edge 的 source／target／action；Edge Map 是端点唯一事实源。
- 不把 actual throughput 排名当 therapeutic priority，也不把加重主问题的通道叫出口。
- 不把格局用神、病药用神、扶抑喜神与调候需要静默合并为一个“喜用”。
- 不在用神太极核里直接写领域故事；用神关系轴只写结构过程，生活显化留给 Topic Lens 与 Imagery Composition。
- 不把同支藏干的组成关系自动改写成持续发生的生克边。
- 不把“删除伪直接边”扩大成“所有藏干只剩库存”；混合路线必须同时保留可证的根气与环境供给层。
- 不把“待时接口”写成“当前已经激活”，也不把匹配触发直接写成 active edge；受影响边必须重新裁决。
- 不把 overlay visibility 回写成 natal visibility，不把对方盘的同字／同五行自动写成本命永久根或永久显化。
- 不把系统能运行等同于日主能主动控制。
- 不把 process／route 的存在等同于 start gate 已打开；不把节点库存或自治流动等同于日主主动供能。
- 不允许上游容量改变后只重算该 edge 而跳过同 process 的下游 edge、condition 与 phase。
- 不允许 Composition 从 route 中自由挑选 edge 子集；五行克应过程的完整闭合只由 `structure-process-handoff.yaml` 交付。
- 不把十神身份等同于固定功能或固定吉凶；不以“伤官见官”“枭神夺食”“财多身弱”等名称替代节点、作用边、主问题和反转条件。
- 不提前读取 subject context 以寻找“命中故事”。
- 不用杯卦、灵体反馈或已发生事件证明普遍命理规则。
