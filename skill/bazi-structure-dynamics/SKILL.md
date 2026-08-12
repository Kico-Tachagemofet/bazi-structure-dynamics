---
name: bazi-structure-dynamics
description: 编排以结构动力、原典证据和十神—干支象核分析四柱八字的分阶段流水线。先校验四柱、司令、十神、藏干与旬空，完成节点、地支裁决、作用边、主问题、路线、结构核、用神太极核、冻结与审计；再以领域太极场组织完整十神关系链，由天干、地支、藏干和柱位具体化为可核对的人事场景，完成家庭、学业、财运、事业及加选专题，真实用户问题另做答案闭环。用于完整原局、旺衰格局、通关制化、取象、岁运、合盘与验证。禁止跳过中间产物，禁止把结构核、问题表、性格画像、建议或字段齐全称为完整断局。
---

# 八字结构动力总编排

把八字视为有方向、有距离、有容量、有竞争和条件开关的结构网络。当前技能只负责编排，不再一口气亲自完成全盘。

本流水线的首要任务不是证明步骤都跑过，而是产出有方向、可证伪、能区分层级的现实断语。必须完整读取并贯穿执行 [八字现实断语合同 v1.0](references/semantic-verdict-contract.md)。结构、来源、Lens、Imagery、Finding、Composition、Render 与 Audit 的局部规则若导致已成立的学历层级、专业性质、技术动作、权责、名声、收入、变动或代价被删除，以现实断语合同为准退回相应上游重做；不得用程序 PASS 覆盖语义失败。

## 断局目标、覆盖账本与真实问题

完整断局的终点不是产物齐全、术语解释、性格画像或改善建议，而是把命盘中有区分度的现实人事场景完整断开：谁与什么事相连，怎样形成，主要落成什么，哪里有优势，代价落在哪里，什么现实门使结果兑现，什么条件令它反转，以及命主可以核对什么。

读者问题剖面的内部检查项进入 coverage ledger，保证家庭、学业、财运、事业及加选专题没有漏面；它们不是用户问题，不得被改写成答题册。只有用户真正提出的具体问题才形成 Reader Answer Contract，至少锁定：

- 求测者真正要知道的中文问题，以及本题涉及的人、事、角色、对象和结果；
- 直接答案及其强度；条件式结论也须先说清当前偏向，不能只列可能性；
- 该答案由哪些冻结 process、十神关系、柱位、藏干状态与现实载体形成；
- 优势怎样成事、代价落在哪里、外部结果还需什么现实门槛；
- 什么条件会加强、减弱、改道、失效或反转；
- 可供命主核对的具体表现与最强替代解释。

完整断局的主要生产单位是十神—干支 scene kernel，不是问题。十神关系链说明功能怎样传递，天干说明显性动作，地支说明场景与根基，藏干说明参与层，柱位限定人事范围；单个十神或单个干支没有独立直断权。性格与行为倾向只能解释已经成立的领域判断；建议只能置于答案之后。完整与详细按象核密度、因果链完整度、领域覆盖与真实问题闭合判定，不按字数、段数、标题数或字段数量判定。

## 核心立场

- 身强身弱是系统状态中的日主承载力，不是开局先验。
- 格局是月令与全局成败救应的组织方式，不是醒目十神或旺衰别名。
- 分开关系存在、实际起效、领域显化和全局净效果。
- 一个节点可同时服务多条路线，但不能被重复满额调用。
- 分开库存、吞吐、蓄积、瓶颈、启动权、控制权和自治子系统。
- 使用强／中／弱与状态词，避免伪精确分数。

## 启动协议

开始完整分析前完整读取 [Pipeline Spec](references/pipeline-spec.md) 与 [八字现实断语合同 v1.0](references/semantic-verdict-contract.md)。

涉及经历合参、校准或验证时另完整读取 [经历映射与流运验证协议](references/validation-protocol.md)。

首次完整原局分析必须先向求测者说明：

- 先盲跑盘面事实、全盘结构、刑冲合害、旺衰格局、主问题与制化路线；该阶段不使用个人经历倒推；
- 结构审计并冻结后，才确认本次以谁／哪件事为中心以及报告范围；
- 完整原局的基础交付固定包含家庭、学业、财运、事业，爱情、健康、神秘学、创作等由求测者后置加选；
- `full-reading` 默认是 `detailed-natal`：生活专题之前必须先交付原局八章（事实边界、系统发动机、四柱、藏干显化、关系网络、十神功能、格局／用神／能动性、整体张力）。四个基础专题和加选专题不能反过来冒充原局详批；只有用户明确要求摘要时才能使用 summary。
- 领域 findings 先在经历隔离状态下完成并审计；经历合参默认只作显化映射，若要称为验证则优先采用先审计冻结、后读取年史的跨领域流运预注册。

不得在启动说明时提前索取可能参与本轮验证的详细经历或专项故事。Reader 只确认命盘主人、本人／代看关系与必要排盘资料。

根据请求进入：

- 新盘或原局：从 $bazi-reader 开始。
- 旧解读审计：仍先用 $bazi-reader 重建事实，再逐条审 claim。
- 原典或流派问题：Reader 最小事实层后调用 $bazi-source-lookup。
- 已有合格 Stage 1：检查产物后继续，不重复已完成阶段。
- 岁运：先完成并锁定 natal。
- 合盘：双方 natal 分别通过审计后再建跨盘临时接口。

## 固定流水线

1. $bazi-reader
   产出 case-manifest、chart-stage1、audit、subject-context。Reader 后必须停止判断。

2. $bazi-source-lookup
   读取本轮真正需要的完整原典、评注或课程，产出 source-packet。

3. $bazi-structure-core
   严格按 Node Ledger → Interaction Census → Branch Relation Census → Branch Arbitration → Post-Branch Node Ledger → Edge Qualification → System State → Primary Problem → Pattern／Structured Routes → Conditions Matrix → Structure Kernel → Use-God Kernel → Five-Element Process Handoff 执行。每一阶段写入独立产物。地支关系必须写回全部节点；hidden／latent／timing-only 节点还须预登记 activation interface 与命中后的重算范围。Edge Qualification 只能读取关系后节点状态。路线只能引用 Edge Map 的 edge ID，实际通量、对主问题的净作用和治疗优先级必须分栏。最后产出 `use-kernel.md`，再把旺衰承载、完整五行链、通关、成本、回病、phase 与日主启动／停机组织为 `structure-process-handoff.yaml`。每条 process 还必须分开 `effect_on_daymaster_capacity／objective_output_capacity／social_realization_channels／sustainability_and_cost`；治疗方向不得代替外部成就方向。该 handoff 是下游唯一过程级事实源。

4. $bazi-finding-audit
   检查覆盖、逻辑、来源和 context 隔离，先产机器事实源 `audit-state.json`，再生成报告投影。出现 BLOCKER 必须退回对应阶段；方向改变必须 re-derive 并完成下游传播。通过后生成 `structure-freeze-receipt.yaml`，冻结 structure inputs、audit state 与 hashes，并初始化 `active-artifact-manifest.json`。

5. $bazi-render — Report Scope Intake
   审计和冻结通过后，先以用户语言确认命盘主人、需要围绕的具体人／关系／事件、时间范围和附加板块，产出 `report-scope.yaml`。完整原局固定使用 `report_depth: detailed-natal`，并保留原局八章、家庭、学业、财运、事业四个基础板块；Render 此时只收问题范围，不让求测者自选技术用神，也不产断语。只有用户明确说“摘要／简版”才可降为 summary，且交付名称必须同步改为摘要，不能称详批。

6. $bazi-topic-lens
   根据 `report-scope.yaml` 先建立 `natal-core-lens-index.yaml`，再为四个基础板块和已选专项建立 Topic Lens v4.1 太极场与 coverage ledger。每个 topic 从冻结 process 与 phase 形成 chart-driven axes，并为每轴登记 `ten_god_chain_plan` 与 `stem_branch_anchor_plan`；coverage facets 只保证不漏查，不生成用户问题、答案或预定 finding 数。Lens 另须按现实断语合同登记该专题的 `mandatory_judgment_dimensions`，逐项标记 `pending-directional-verdict／not-applicable／source-gap`，不得静默合并。只有用户真实提出的具体问题才进入 `explicit_reader_questions` 与 Reader Answer Contract。Lens 不得填写实际答案或载体排名，但必须向 Source 请求开放候选象池，不得用泛化商业载体提前收窄职业、教育或人物候选。

   岁运／合盘在此阶段只按 `$bazi-topic-lens` 的 Timing／Synastry Scope Seed Schema v1.0 产最小 `timing-scope-seed.yaml` 或 `synastry-scope-seed.yaml`，并先通过 seed validator：列大运／流年／关系 atoms、自然语言问题、领域范围和待查 activation interfaces，不在 overlay 前伪造 canonical timing process axes。

7. Timing／Synastry conditional stage
   按 scope seed，由 Structure Core 在冻结 natal 上匹配 `activation_interfaces` 与本轮临时干支。命中只进入重算队列；须从接口登记的最早受影响阶段重新裁 branch state、node state、竞争分配、edge 与 route conditions，并沿 `structure-process-handoff.yaml` 传播到同 process 的全部下游 edge、condition 与 phase。逐年另产 `timing/year-YYYY-process-state-diff.yaml`，交付 start gate、throughput、allocation、daymaster cost、therapeutic effect、residual problem、rebound 与 agency 的 before／after；未改变下游须有 no-impact 收据。每个受影响 process 另产 `natal_route_retention`，比较原局主路剩余通量、共享节点占用和备用路线；每个 matched node 产 `overlay_function_transition`，分开原局功能、临时显化资格与载体 claim ceiling。逐年请求必须逐年输出全量 interaction census、overlay diff 和 process diff；大运综述不能替代年份。四个以上同五行节点、多组冲刑并发或共享节点多重占用时强制交付 high-contrast structure。合盘还须双方 natal 分别冻结并证明跨盘关系与本题有关。本阶段不得回写 natal。

   Overlay 经 `$bazi-finding-audit` 审计并冻结后，必须回到 `$bazi-topic-lens` 生成正式 timing／synastry v3.1 typed state：每个 atom 建独立 axis，分开原局剩余主路、临时功能、领域关系功能、现实载体候选、影响边界、命主当时位置与到期撤销。当时位置只能调整载体分支和可控范围，不得改写结构 diff。

8. $bazi-source-lookup → $bazi-imagery-composition
   full-reading 先按 natal chart-card inventory 完整读取本盘相关十神总卡、透干、四支和重要藏干卡，再为各 topic 编译不同的 runtime units、开放 candidate palette 与 carrier leads；通用五行／十神包不能冒充专题材料。随后按 `$bazi-imagery-composition` 的 Agent 隔离协议判断：完整报告、复杂专题、timing／synastry、L4 载体竞争、批量 kernels 或当前上下文已知经历／预期答案时，主 session 只能生成无答案 job packet，必须由全新上下文 producer 逐 topic 生产，再由另一个全新上下文 auditor 验收；没有干净 agent 就停止。Composition 固定执行：过程覆盖 → `process-compositions.yaml` → 逐柱／藏干着色 → **spread 材料全摊开** → **intersect 关系交会** → **differentiate 按现实端点拆 claim kernels** → **rank 五级断语** → `bazi-scene-kernels.yaml` → kernel-driven topic findings → **synthesize 合成现实画面** → render-use envelope → finding audit → coverage／answer receipts → composition audit。共享 process 不能成为合并学历、技术、权责、名声、收入、变动和代价的理由；它们可在散文中合写，但必须先各自形成有方向的主张。具体身份走 L5 高门槛，L1–L3 已获组合支持时不得因不敢断身份而退回性格或流程描述。

9. Optional Ambiguity Discrimination／Manifestation Mapping／Validation Gate
   不强制家庭校准。若结构冻结含真实 ambiguity register，先为各分支分别完成 Topic／Imagery／blind findings 与审计冻结；用户主动同意后，只问一个不含分支术语的自由叙述问题，产出 case ambiguity overlay，绝不回写 natal 或规则卡。普通经历只写 `manifestation-map.md`，不增加结构置信度。默认反馈仍为“准／部分准／不准／记不清”，不自动追问、不计作证据；用户主动说“展开验证”后才进入详细流运验证。正式流运验证在读取相关年史前完成 timing diff／overlay、复杂假设、独立审计和 hash 冻结，再收集自由叙事、固定计分并审计 scorecard。流程与产物严格遵循 [经历映射与流运验证协议](references/validation-protocol.md)。没有合格条件时记 `validation_mode: none`，继续报告。

10. $bazi-render
   先完整读取合格散文 few-shot 与失败问答台账反例，再把原局八章和各 topic 写成 `reader/` 覆盖单元，最后按 `composition.md` 的全盘主锚、关键人生主线、scene kernels、跨专题张力与回扣关系无损编译完整报告。reader 文件、coverage facets、问题数和上游 artifact 数都不决定可见标题或段落。Render 只读已审计 process compositions、scene kernels、findings 与自足 envelope，不得打开 Deep Card 母卡、runtime packet 或 Source manifest，不得重新取象。正文围绕主场景连续铺开十神链与干支具体化，性格只能作从属解释；coverage receipts 在后台证明没有漏断，只有真实问题用 question marker 与 reader-answer receipt 闭合。所有独立 judgments 必须有稳定 ID 和实质正文，但不设每 finding 固定数量。`render-card-receipt.yaml`、`coverage-render-receipt.json`、按需 reader-answer receipt、独立交付扫描与 render audit 均为硬门槛。

## 原典资料路由

基础结构必须按需读取：

- [力量模型](references/strength-model.md)
- [格局与功能角色](references/pattern-functional-roles.md)
- [作用网络与刑冲合害](references/interaction-network.md)

查《千里命稿》或流派术语：

- [原典索引](references/source-index.md)

使用《子平真诠》：

- [资料路由](references/ziping-zhenquan-source-map.md)
- [模型笔记](references/ziping-zhenquan-model-notes.md)
- 按路由加载原本全文与徐乐吾评注全文；两者不得混署。

需要完整干支、十神、身体、职业、场所、动作或事件取象：

- [课程资料路由](references/ruojing-course-source-map.md)
- 按路由加载课程完整时间段。
- 读取 [资料摄取与取象保真规范](references/source-ingestion-fidelity.md)。
- 没有完整取象卡时，不得用缩略口诀补写展开。

## 硬门槛

- Chart audit FAIL：停止。
- Node Ledger 未覆盖全部位置节点：停止。
- Interaction Census 未检查自刑、共享支或重复支：停止。
- Interaction Census 没有以 Reader 确定性枚举为事实基线、出现 Reader 未枚举的关系，或把普通重复支误升为自刑：停止。重复支只说明同字节点增加；自刑另限辰、午、酉、亥的同支重复。
- Branch Relation Census 未单独覆盖三会、三合、半合、六合、六冲、刑、自刑、害、破、重复支及 negative scan：停止。
- Branch State 有未决竞争：停止。
- Post-Branch Node Ledger 未覆盖全部原始节点，或没有把地支裁决逐节点写回：停止。
- 岁运／合盘题涉及 hidden／latent／timing-only 节点却无 activation interface，或 trigger match 后未重算受影响作用边：停止。
- Edge Map 直接引用原始 Node Ledger 的 availability，而未引用 post-branch state：停止。
- Source Packet 未加载相关原文：相关结论不得标高置信度。
- Structure audit FAIL：不得进入 Topic、Timing、Synastry 或 Render。
- overlay 把临时显性回写为 natal visibility、把对方节点写成本命永久根，或缺 scope／expiry／overlay audit／freeze：停止。
- `use-kernel.md` 缺失、未区分用神框架，或没有逐条实际关系轴：不得冻结结构或进入 Topic。
- `structure-process-handoff.yaml` 缺失、process route closure 不完整，或未分开日主成本、治疗效果、剩余问题、回病与 phase agency：不得冻结结构或进入 Topic。
- `structure-process-handoff.yaml` 把对主问题的治疗方向当成学业、事业、财富的外部结果方向，或缺少日主承载／客观产出／社会兑现／持续代价四面裁决：不得进入 Topic。
- Structure 未冻结或下游引用的结构版本与 freeze receipt 不一致：停止。
- `audit-state.json` 与报告 verdict／计数不一致、方向改变却只 patch、或 propagation 未完成：停止。
- 可路由下游文件未在 active artifact manifest 中归类，或 active 文件混用 freeze：停止。
- 完整原局缺少 `report-scope.yaml`、领域太极场、per-topic 用神枢纽／关系轴、coverage ledger 或四个基础板块中的任一项：停止；不得改称完整报告后继续。
- Topic Lens v4.1 缺 mandatory judgment dimensions、十神链计划、干支锚点、scene-kernel handoff，出现预写答案／载体排序，或把 coverage facet 冒充真实用户问题：停止。
- Topic Lens 没有逐项登记该 scope 的 mandatory judgment dimensions，或用 `axis 可合并` 静默删去学历、专业性质、权责、名声、收入、变动等结果端点：停止。
- `full-reading` 缺原局八章、`natal-core-lens-index.yaml`、`natal-core-coverage-index.yaml`、`hidden-manifestation-matrix.yaml` 或 `cross-topic-claim-registry.yaml`：停止；生活专题不能替代这些原局产物。
- 用户要求逐年但任一年度没有独立 scope atom、interaction census、overlay diff、primary axis 或 finding：停止；不得以大运总述或多年 sequence finding 代替。
- 用户要求逐年但任一年度没有独立 process state diff／propagation closure，或上游变化未传播到同 process 下游：停止。
- Topic 把本气／禄地当司令重复计权、因题目强制常规星为主轴，或把节点有气直接写成命主能力：停止并退回 Topic Lens。
- 用户经历在 blind findings 或预注册假设审计冻结前参与生成，或已污染仍声称盲验证：FAIL；须明确列出已知先验并排除／降权，无法隔离则标 `contaminated` 并放弃验证资格，但可继续做非证据性的显化映射。
- 路线端点与 qualified-edge-map 不一致、把实际通量排名当治疗优先级、或把加重主问题的路线叫出口：FAIL。
- 取象 finding 漏掉相关柱的天干、地支、藏干、同柱互染或 full-chart sweep：FAIL。
- 取象 finding 缺完整 process composition，anchor 漏掉 process 起始／成本／通关／回病 edge，或符号／十神层改写 process state：FAIL。
- 缺 `bazi-scene-kernels.yaml`，kernel 缺完整十神链、干支柱位组合、材料摊开与关系合成，或由问题／facet 数机械生成：FAIL。
- 命中 `$bazi-imagery-composition` Agent 隔离协议的复杂象核由总编排 session 直接生产、缺无答案 job packet／fresh producer／独立 auditor，或环境无 agent 仍继续：FAIL。
- 主 session、生成脚本或模板先写断语再挂 process／十神／干支证据，runtime units 被固定截断、数组映射或自报全覆盖：FAIL。
- 宽专题没有按 L1–L4 检查现实层级、领域性质、动作材料和候选载体，或因 L5 具体身份证据不足而一并删除 L1–L3：FAIL。
- finding／composition 缺 `coverage-receipt.json`；存在真实问题时缺 `question-answer-map.yaml` 或任一真实问题没有直接答案 claim 与解释职责收据；以性格画像／建议代替领域结论：FAIL。
- imagery packet 缺 Deep Card manifest、primary finding 缺 process composition／render-use envelope、实际使用物象／载体竞争却缺 resonance map，或 Render 无 render-card receipt：FAIL。
- Render 没有保留独立 judgment IDs、任一主张 marker 后缺实质正文、把 coverage 写成问答台账、高反差结构未让来源／方向／竞争／结果可分辨、可见排版暴露审计脚手架并切碎全盘主线、缺 quick-feedback offer 状态，或未通过独立交付扫描：FAIL。不得仅因没有固定三段、固定标签、独立 finding 标题或表格而判 FAIL。
- context-only／forbidden 单元被升格，或单张天干／地支／十神卡直接支持具体职业、岗位、身份或事件：FAIL。
- Render 出现上游没有的新判断：退回 composition；若属合理新追问，则新开增量 Topic／Source／Imagery 回合。
- Render 缺 coverage-render receipt；存在真实问题时缺 reader-answer receipt 或任一问题没有唯一正文闭合位置；同一泛化答案跨专题复制而没有领域新增对象／载体／结果／条件：FAIL。

## 已知禁止捷径

- 年干七杀不直接等于七杀格。
- 藏干不透不等于完全无效。
- 有根不等于畅通。
- 相生箭头不等于通关完成。
- 五行齐全或图上成环不等于真实周流。
- 合不自动化，冲不自动开库，刑害不独立定性。
- 被冲藏干不能同等释放。
- 地支关系裁决不得停在说明层；必须先改写节点状态，再允许下游起边。
- 旬空只裁关系与节点的兑现度，不得被用作“不自动开库”的原因；两项必须分别判断。
- 同支藏干不得仅凭五行关系自动生成 active 边；须有来源规则与 post-branch direct-action gate。
- 藏干未透不自动等于 weak／conditional／forbidden；须把 direct action、root support 和 environmental feed 分层。禁止伪直接边不得反向抹掉有来源的人元作用或根气供给。
- 当前不透不等于今后永不透清；但登记 activation interface 也不等于当前已激活。触发匹配后必须重裁受影响支局、节点和作用边，不能只把状态开关改成 active。
- 合盘中对方有同字／同五行不自动激活本命节点；跨盘节点只在已声明的关系场和覆盖期内有效。
- 系统能自行运行不等于日主能主动调用或停止。
- 显化映射不能冒充证据验证；验证必须先冻结复杂假设，包含时间窗、顺序、路线机制、领域竞争和失败条件。
- “说得通”、宽泛关键词或单一领域命中不得增加置信度；记不清为 `unscored`，不得按反证处理。
- 经历不能用来倒推格局、路线或通用规则。
- 同柱互染属于 composition-only，不得反向生成结构 active edge。
- 行业必须先由工作性质推导，再给例子；名声、资源、可见度和收入不得自动合并。
- 杯卦、灵体反馈或其他术数只能提示待检假设，不能代替八字原典和结构证据。

## 完成标准

完整分析必须交付：

- 盘面事实与审计；
- 本轮来源收据；
- 原始节点、关系全枚举、地支关系专表、支局裁决、关系后节点和边状态；
- 系统库存、吞吐、瓶颈和控制权；
- 主问题、路线端点锁、实际通量／净作用／治疗优先级、conditions matrix、Structure Kernel、Use-God Kernel 与 structure freeze；
- 分流派格局候选与竞争路线；
- Structure Kernel 与后置用神太极核；
- 独立 audit verdict；
- `report-scope.yaml`、命主／求测者／领域太极场、coverage ledger、per-topic process／phase／用神枢纽／十神链计划／干支锚点与完整／限定分析模式；
- 完整原局必须附家庭、学业、财运、事业四个基础 Topic Lens、natal chart-card inventory、完整取象 Source Packet、Deep Card manifest、process compositions、逐柱着色、axis scenes、`bazi-scene-kernels.yaml`、载体竞争／按需 resonance maps、topic findings、render-use envelopes、coverage receipt、经历映射／验证状态、composition、render receipts 与不越界散文 Render；真实问题存在时另附 question-answer map 与 reader-answer receipt。未做验证不影响完整断局，但不得声称已经回验；
- 求测者加选的专项必须同样经过 Topic／Source／Imagery／Audit；岁运／合盘先附 matched activation interface 收据、受审计 diff／overlay、范围与失效条件。

只有技术结构而未进入基础四板块时，只能称“结构分析完成”，不能称“完整断局”。限定问题模式只交付约定范围，并须显式列出未覆盖板块。
