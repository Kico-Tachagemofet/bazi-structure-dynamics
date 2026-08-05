---
name: bazi-structure-dynamics
description: 编排以结构动力和原典证据分析四柱八字的分阶段流水线：先校验四柱、司令、十神、藏干与旬空，完成节点、地支裁决、作用边、主问题、端点锁定路线、条件矩阵、结构核、后置用神太极核、结构冻结与审计，再由求测者确认自然语言问题中心和报告范围，按体—用关系轴完成家庭、学业、财运、事业及加选专题。用户询问完整原局、旺衰、格局、通关制化、刑冲合害、用神、藏干、具体取象、职业关系健康神秘学、合盘、经历校准或验证时使用。禁止一口气跳过中间产物，也禁止把只有结构核的分析称为完整断局。
---

# 八字结构动力总编排

把八字视为有方向、有距离、有容量、有竞争和条件开关的结构网络。当前技能只负责编排，不再一口气亲自完成全盘。

## 核心立场

- 身强身弱是系统状态中的日主承载力，不是开局先验。
- 格局是月令与全局成败救应的组织方式，不是醒目十神或旺衰别名。
- 分开关系存在、实际起效、领域显化和全局净效果。
- 一个节点可同时服务多条路线，但不能被重复满额调用。
- 分开库存、吞吐、蓄积、瓶颈、启动权、控制权和自治子系统。
- 使用强／中／弱与状态词，避免伪精确分数。

## 启动协议

开始完整分析前读取 [Pipeline Spec](references/pipeline-spec.md)。

涉及经历合参、校准或验证时另完整读取 [经历映射与流运验证协议](references/validation-protocol.md)。

首次完整原局分析必须先向求测者说明：

- 先盲跑盘面事实、全盘结构、刑冲合害、旺衰格局、主问题与制化路线；该阶段不使用个人经历倒推；
- 结构审计并冻结后，才确认本次以谁／哪件事为中心以及报告范围；
- 完整原局的基础交付固定包含家庭、学业、财运、事业，爱情、健康、神秘学、创作等由求测者后置加选；
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
   严格按 Node Ledger → Interaction Census → Branch Relation Census → Branch Arbitration → Post-Branch Node Ledger → Edge Qualification → System State → Primary Problem → Pattern／Structured Routes → Conditions Matrix → Structure Kernel → Use-God Kernel 执行。每一阶段写入独立产物。地支关系必须写回全部节点；Edge Qualification 只能读取关系后节点状态。路线只能引用 Edge Map 的 edge ID，实际通量、对主问题的净作用和治疗优先级必须分栏。最后把格局用神、病药／制化主用、扶身辅用、调候需要和备用路线分开，产出后置 `use-kernel.md` 与实际用神关系轴。

4. $bazi-finding-audit
   检查覆盖、逻辑、来源和 context 隔离。出现 BLOCKER 必须退回对应阶段，修复后重审。通过后生成 `structure-freeze-receipt.yaml`，冻结 structure inputs 与 hashes。

5. $bazi-render — Report Scope Intake
   审计和冻结通过后，先以用户语言确认命盘主人、需要围绕的具体人／关系／事件、时间范围和附加板块，产出 `report-scope.yaml`。完整原局固定保留家庭、学业、财运、事业四个基础板块；Render 此时只收问题范围，不让求测者自选技术用神，也不产断语。

6. $bazi-topic-lens
   根据 `report-scope.yaml` 为四个基础板块和已选专项分别确定“本题在看什么”的领域体，再从冻结的 `use-kernel.md` 选择相关主用／辅用／备用枢纽，建立具体的体—用关系轴。每条轴只承载一个主过程，并列出必须展开的干支、十神、柱位、藏干与取象单元。限定问题模式可以只建相关镜头，但必须明确不称完整断局。

7. Timing／Synastry conditional stage
   若 Topic Lens 属于岁运或合盘，先由 Structure Core 在冻结 natal 上建立 diff／overlay，完成对应审计；普通 natal topic 跳过。本阶段不得回写 natal。

8. $bazi-source-lookup → $bazi-imagery-composition
   为本 topic 加载完整取象资料，按用神关系轴执行象意覆盖 → 逐柱复合 → axis scene → topic findings → finding audit → composition → composition audit。每条主关系轴至少形成一条能回答具体问题的 finding；不得把数条轴压成“有压力但可借助资源”之类总括句。经历显化映射是可选层，不是 finding 成立的门槛；取象组合不得伪造成新的结构作用边。

9. Optional Manifestation Mapping／Validation Gate
   不强制家庭校准。默认只提供“准／部分准／不准／记不清”的快速反馈入口，不自动追问，也不计作证据；用户主动说“展开验证”后才进入详细模式。若只需把已审计 finding 对应到现实载体，读取经历后写 `manifestation-map.md`，明确其不增加结构置信度。若要正式验证，优先运行跨领域流运对照：在读取相关年史前完成 timing diff／overlay、复杂假设、独立审计和 hash 冻结，再收集自由叙事、固定计分并审计 scorecard。流程与产物严格遵循 [经历映射与流运验证协议](references/validation-protocol.md)。没有合格条件时记 `validation_mode: none`，继续报告。

10. $bazi-render
   生成完整报告，或以对话模式承接追问。已有 finding 可直接解释；首次未展开的象意允许增量回到 Topic／Source／Imagery 生产新 finding；涉及新岁运、合盘或结构争议时必须退回相应上游。Render 自身不得添加 finding。

## 原典资料路由

基础结构必须按需读取：

- [力量模型](references/strength-model.md)
- [格局与功能角色](references/pattern-functional-roles.md)
- [作用网络与刑冲合害](references/interaction-network.md)
- [旧版输出模板](references/output-contract.md)

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
- Branch Relation Census 未单独覆盖三会、三合、半合、六合、六冲、刑、自刑、害、破、重复支及 negative scan：停止。
- Branch State 有未决竞争：停止。
- Post-Branch Node Ledger 未覆盖全部原始节点，或没有把地支裁决逐节点写回：停止。
- Edge Map 直接引用原始 Node Ledger 的 availability，而未引用 post-branch state：停止。
- Source Packet 未加载相关原文：相关结论不得标高置信度。
- Structure audit FAIL：不得进入 Topic、Timing、Synastry 或 Render。
- `use-kernel.md` 缺失、未区分用神框架，或没有逐条实际关系轴：不得冻结结构或进入 Topic。
- Structure 未冻结或下游引用的结构版本与 freeze receipt 不一致：停止。
- 完整原局缺少 `report-scope.yaml`、自然语言问题中心、per-topic 用神枢纽／关系轴或四个基础板块中的任一项：停止；不得改称完整报告后继续。
- 用户经历在 blind findings 或预注册假设审计冻结前参与生成，或已污染仍声称盲验证：FAIL；须明确列出已知先验并排除／降权，无法隔离则标 `contaminated` 并放弃验证资格，但可继续做非证据性的显化映射。
- 路线端点与 qualified-edge-map 不一致、把实际通量排名当治疗优先级、或把加重主问题的路线叫出口：FAIL。
- 取象 finding 漏掉相关柱的天干、地支、藏干、同柱互染或 full-chart sweep：FAIL。
- Render 出现上游没有的新判断：退回 composition；若属合理新追问，则新开增量 Topic／Source／Imagery 回合。

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
- `report-scope.yaml`、命主／求测者／自然语言问题中心、per-topic 用神枢纽／关系轴与完整／限定分析模式；
- 完整原局必须附家庭、学业、财运、事业四个基础 Topic Lens、完整取象 Source Packet、逐柱复合、topic findings、经历映射／验证状态、composition 与不越界 Render；未做验证不影响完整断局，但不得声称已经回验；
- 求测者加选的专项必须同样经过 Topic／Source／Imagery／Audit；岁运／合盘先附受审计 diff／overlay。

只有技术结构而未进入基础四板块时，只能称“结构分析完成”，不能称“完整断局”。限定问题模式只交付约定范围，并须显式列出未覆盖板块。
