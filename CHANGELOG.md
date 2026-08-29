# Changelog

## [2.0.0-rc.2] - 2026-08-29

### Summary

rc.2 是一次以实际断盘质量和运行成本为中心的破坏性瘦身。rc.1 虽然建立了完整的语义门、producer／auditor 隔离和可追溯收据，但真实运行暴露出新的主要问题：大量 token、文件和时间花在证明流程已经完成，最终报告仍可能只有抽象机制、性格画像和防御性保留。

本版删除旧审计屎山，把默认流程重建为：

```text
Reader → Structure → user Scope gate
→ sealed reading pack → fresh-context reader-writer
```

事实与结构仍由上游收束；取象、现实载体比较、结果判断和散文写作重新合并到同一个无历史上下文 writer 中。这样既保留四柱、旺衰、格局和用神的正确性边界，也避免判断在 Topic Lens、scene kernels、findings、Composition 和 pure Render 之间反复压缩。

### Why this release exists

rc.1 的问题不是审计文件本身占多少磁盘，而是审计合同反向塑造了生产过程：

- 每个专题先拆 packet、kernel、finding、coverage 和 receipt，导致模型把注意力用于填字段；
- producer 与 auditor 为每个 topic 重复加载材料，运行时间随专题和年份快速膨胀；
- Render 被限制为纯翻译层，无法在成文时继续进行十神—干支取象和载体比较；
- 中间层压缩后只剩“压力、支持、承载、边界”等抽象词，报告看起来完整，实际仍像性格测试；
- case-specific few-shot 会显著提高同盘文字表现，却破坏盲测有效性；
- Scope 阶段没有真正阻塞，用户只说“看看这个盘”时，Agent 会自行扩展成完整原局、感情、健康和岁运；
- audit PASS、文件数量和字段齐全无法证明最终断语有用。

### Removed — redundant audit pipeline

- 公开 `skill/` 从 **138 个文件降至 68 个文件**。
- 删除默认运行中的 audit state、active artifact manifest、freeze／hash receipt 和多层 activation 状态。
- 删除逐专题 Deep Card runtime packet、material disposition、carrier resolution 与 cross-topic signature。
- 删除 per-topic scene-kernel producer／independent auditor job 目录和相关 schema。
- 删除 finding／judgment／question closure、coverage receipt、Render markers、Reader 分卷与 delivery scan。
- 删除逐年 census／overlay／process 三件套；岁运改为固定结构变化后由 writer 自然成文。
- 删除不再参与运行的 validator、test fixture 和硬编码集合等值检查。
- 删除 active Render 中的同盘 few-shot、negative few-shot 和旧反套话规则；公开包不再携带任何命例样章。
- `bazi-finding-audit` 收窄为显式调用的语义法证工具，不再是普通报告依赖。

这些删除不影响四柱、十神、藏干、司令、合冲刑害、格局与用神的基本正确性检查。

### Changed — scope and routing

- 显式调用 `$bazi-reader` 时，只生成事实产物并停止；“断一下／看看／分析一下”不再自动升级成完整报告。
- 新增真正的用户 Scope gate。命主、本人／代看、专题、岁运范围或必要性别口径不清时，流程必须提问并结束当前 turn。
- 新增高特异度精度提示：用户明确要求尽可能精确还原学历／学位、婚次、职业身份、官职或标志性事件时，入口先说明八字边界；环境可用时建议优先转入 `$ziwei-feixing-core-v2`，八字用于结构与推运补充。
- 用户回答前不得创建 `report-scope.yaml`、Topic Lens、reading notebook、Composition 或报告。
- 禁止仅凭大运顺逆推定性别后直接书写感情和六亲。
- 用户已经把范围说清时直接记录，不重复询问。

### Added — sealed reading pack

- 新增 `reading-pack/`，固定 `handoff.md`、`chart-stage1.yaml`、`structure-notebook.md`、`report-scope.yaml`、`source-notes.md` 和相关 `materials/`。
- pack 只复制本盘实际相关的五行、十神、天干、地支、藏干和岁运材料。
- pack 明确排除旧报告、旧 findings、用户纠错、预期答案、经历材料、Topic Lens、reading notebook、Composition、few-shot、审计文件和其他 case。
- 经用户授权加入经历时必须标为 `non-blind`，不得宣称前向盲断。
- 新增可复用的 fresh-context handoff 提示，要求只传 pack 路径和输出路径，不转发父 session 的对话摘要。

### Changed — Render becomes Reader-Writer

- `bazi-render` 不再是“只能翻译 Composition”的纯语言层。
- 新 Render 仅在 sealed pack 已存在时运行，并在一个干净上下文中独立完成：
  - 十神主链与竞争路线理解；
  - 天干动作、地支场景、藏干参与和柱位范围组合；
  - 学历、专业性质、技术动作、权责、名声、收入、变动和关系结果判断；
  - 现实载体家族比较与主次排序；
  - 大运流年在保留原局保证下的自然成文；
  - 少标题、连续中文断盘。
- writer 自由决定章节、标题、段落顺序和详略，不使用固定问答、统一段落字段或内部审计语言。
- 父窗口只检查盘面事实、确认范围、排除材料和高风险确定化，不按预期答案重写正文。
- 需要重写时废弃当前稿并启动新的 clean writer，不在原上下文累加长篇纠错。

### Changed — optional diagnostic skills

- `bazi-topic-lens` 改为可选专题诊断，只在用户要求内容地图、复杂限定专题或 fresh report 明显漏层时使用。
- `bazi-imagery-composition` 改为可选推导底稿，用于查看十神—干支组合过程或补充 reading pack。
- 普通完整报告不再默认创建 `topic-map.md`、`reading-notebook.md`、`timing-notebook.md` 或 `composition.md`。
- `bazi-source-lookup` 现在同时服务 Structure 和 reading pack，只提供规则、符号材料和未排名候选，不替 writer 预写生活答案。
- `bazi-structure-core` 只固定技术结构和下游接口，不提前写家庭、学历、职业或婚姻 verdict。

### Interpretation quality

- 保留“十神关系链＋天干动作＋地支场景＋藏干参与＋柱位范围”的核心取象方法。
- 允许 writer 在成文过程中继续摊开、比较、排序和合成现实载体，避免结构材料被过早压平。
- 报告目标仍然是现实层级、领域性质、动作材料、载体家族、结果、代价和反转，而不是只报旺衰或性格标签。
- 陌生合成盘前向测试在无 few-shot、无旧报告、无 Topic Lens／Composition 的条件下，仍能自行形成教育层级、专业资格、职业家族、财富路径、关系权责和创作载体等详细判断。

### Public packaging and privacy

- 所有本机绝对路径替换为仓库相对路径或 `external-source://...` 标识。
- 清除维护者专名、命例 ID、thread ID、case 目录、临时 reading pack 和前向测试产物。
- 公开包不包含出生资料、subject context、用户经历、旧报告或已知答案。

### Validation

- 8/8 Skills 通过 `quick_validate.py`。
- Markdown 本地引用缺失 0。
- 公共包扫描未发现本机盘符、用户命例 ID、thread ID、few-shot 或旧 runtime 文件名。
- 独立 Scope gate 测试确认显式 Reader 只交付事实并询问后续范围。
- 独立 fresh writer 测试使用 `fork_turns="none"`，只读取 sealed pack，并生成完整多专题报告。

### Breaking changes and migration

- rc.1 的 scope、Lens、runtime、scene kernels、findings、Composition、Render receipt 和 delivery artifacts 不再构成 rc.2 的默认完成链。
- `bazi-render` 的职责发生反转：从纯翻译层改为 clean-context reader-writer。
- 旧 case 不应把已有 Composition 或 findings 直接送入新 Render；应重新固定 facts、structure、scope 和 reading pack。
- 没有 fresh-context agent 能力时，完整报告流程停在 reading pack，由用户在新任务中继续。
- 如果外部集成依赖旧 schema 或 validator，需要继续使用 rc.1 分支，或自行迁移到新的七项默认产物。

### Known limitations and positioning

- reading pack 仍需完整读取本盘相关 Deep Cards；上游 Source 阶段是当前主要耗时，后续将在不牺牲报告质量的前提下继续测试压缩空间。
- 八字更适合分析结构性质、成事路线、职业类型与推运；它不保证从原局稳定盲断博士、离婚或精确职业身份等高特异度履历。
- 若主要目标是高精度还原具体人生领域和事件，传统术数使用者可优先使用 `$ziwei-feixing-core-v2`，再以八字补充结构与时间判断。
- 本项目属于传统文化文本研究与解释工具，不是经科学验证的预测系统，也不构成医疗、法律或财务建议。

## [2.0.0-rc.1] - 2026-08-12

### Summary

2.0 RC 把流水线的验收中心从“步骤和字段是否齐全”改为“是否真正回答现实断局问题”。结构层仍负责可追溯的旺衰、格局、节点、关系、作用边和五行过程；Topic、Imagery 与 Composition 则必须继续完成完整十神关系链、天干地支藏干柱位合成、现实结果分层、载体竞争与反转。Render 只负责把这些已冻结内容写成少标题、因果连续的散文，不能自行补象。

本版同时引入复杂象核的 fresh-context producer／independent auditor 隔离。已经知道命主经历、预期答案或用户纠错的主 session 不再具有盲产资格；缺少干净 agent 时，复杂象核会明确停止，而不是继续生成看似完整的报告。

该版本标记为 RC，是因为新协议、schema、validator 和回归门已经完成，但仍需更多未讨论命例的首次前向盲测，才能证明泛化表现。

### Why this release exists

1.2.0 虽然已经分开 Structure、Use Kernel、Topic Lens、Composition 和 Render，但实盘仍暴露出系统性缺陷：

- 上游只给每个专题一个宽泛问题，Render 只能扩写成更长的性格测试；
- 十神、天干、地支和柱位名义上都被读取，实际生产时只剩旺衰强弱与通用断语；
- 学历、专业技术、权责、名声、收入、变动和代价被合成一句，丢失方向差异；
- timing 的不同年份可以复用同一套八维结论和同一载体排名；
- coverage receipt 字段齐全，却可能让所有 facet 指向同一条 judgment；
- 主 session 已经知道修复目标后仍直接生产，导致回归样章不能作为盲测证据；
- Render 被内部标题、答题模板和审计字段框住，正文不像连续断盘散文。

2.0 RC 针对这些失败重建了从语义目标到独立交付扫描的整条链。

### Added — semantic objective and report scope

- 新增《八字现实断语合同 v1.0》，把终点明确为可区分、可证伪的现实判断，而不是术语解释、性格画像、建议或 artifact 齐全。
- 为每条重要判断要求形成：对象与事件、方向、形成链、优势、代价、结果门、反转、核验表现与替代解释。
- 区分 coverage facets 与真实用户问题：前者只保证完整断局不漏面，后者才建立 Reader Answer Contract、direct answer 和独立 answer receipt。
- `full-reading` 默认固定为 `detailed-natal`；新增原局八章的 Lens、coverage、findings 和 cross-topic registry，生活专题不能替代原局详批。
- 完整原局固定保留家庭、学业、财运、事业，并允许感情、健康、神秘学／直觉、创作、人际、子女及自定义专题。

### Added — structure-to-composition process spine

- 新增／强化 `structure-process-handoff`，把冻结路线无损交给 Topic 与 Composition。
- 每条 process 分开日主承载、客观产出、社会兑现、持续代价，避免把“对主问题有治疗作用”误写成“外部成就一定更高”。
- process handoff 显式保留 start gate、完整 edge／route closure、phase、共享节点分配、日主成本、治疗效果、残余问题、回病旁路和 agency。
- timing overlay 增加逐窗 process-state diff、传播闭包、natal route retention、overlay function transition、shared-node allocation 与 expiry／no-backwrite 收据。
- 用户要求逐年时，每年必须有独立 scope atom、关系 census、overlay diff、process diff、finding 和正文。

### Added — Topic Lens v4.1

- Topic Lens 改为“专题太极点 + mandatory judgment dimensions + process + 十神链计划 + 干支柱位锚点 + 开放载体候选池”。
- mandatory dimensions 必须逐项登记 `pending-directional-verdict`、`not-applicable` 或 `source-gap`，不得静默合并学历、专业性质、权责、名声、收入、变动等结果端点。
- Lens 不得填写方向答案、预定 finding 数或 preferred carrier；问题表不再承担正文结构。
- 新增 natal-core lens／coverage index、hidden manifestation matrix、cross-topic claim registry 和逐专题 scene-kernel handoff。
- timing／synastry 先生成最小 scope seed，Structure overlay 冻结后再回到 Topic Lens 生成正式 typed state，防止 Lens 预造岁运过程。

### Added — Deep Cards and topic runtime compilation

- 扩展五行、十天干、十二地支、地支共通层和十神 Deep Cards，并增加逐 card runtime units。
- Source Lookup 必须按命盘和专题编译 selected units、context-only／forbidden units、开放 candidate palette 与 carrier leads；通用十神包不能冒充所有专题材料。
- 新增 material disposition：producer 必须对每个 selected runtime unit 标记 `used`、`counterevidence`、`context-only` 或 `excluded-with-reason`，四类并集必须严格等于输入集合。
- 外部跨体系材料只能作为共同符号候选，去除另一术数专属组件后才可进入 source-only 层，不能决定八字结构或事件。

### Added — scene-kernel production and agent isolation

- 新增 `scene-kernel-agent-protocol.md`，定义何时强制 fresh producer 与 independent auditor。
- 隔离触发包括：完整报告、复杂专题、timing／synastry、L4 载体竞争、批量 kernels，或当前上下文已经知道经历／预期答案／纠错方向。
- 总编排 session 只允许生成不含答案的 job packet；producer 每次只处理一个 topic，不能用 follow-up 连续生产下一题。
- auditor 与 producer、orchestrator 分离，只读 job packet、允许输入、producer output 和审计规则；FAIL 后必须废弃输出并另开 producer。
- 新增 producer／auditor 固定任务说明、actual read set、hash、forbidden inputs、prior exposure、script-generated judgment 和 isolation receipt。
- 环境无 fresh-context agent 时新增 `AGENT_ISOLATION_UNAVAILABLE` 停止状态，不允许主 session 代写复杂象核。
- Scene Kernel schema 新增：完整十神链、干支柱位组合、selected-unit disposition、spread/intersect/differentiate/rank/synthesize、主象／次象／反转象、现实载体竞争、claim strength 和 agent provenance。
- Scene Kernel validator 新增集合等值、每 unit 处置、复杂度触发、角色分离、禁止预写方向、禁止脚本／模板生成 judgment text 等检查。

### Changed — imagery and findings

- Imagery Composition 固定采用 `spread → intersect → differentiate → rank → synthesize`。
- `spread` 必须先摊开 process、十神、天干、地支、藏干、柱位和所有 selected runtime units；不得截取最顺眼的前几项。
- `intersect` 只在完整关系链交会处形成现实候选；单个十神或干支不再拥有独立直断权。
- `differentiate` 先拆开学历、训练路径、技术动作、权责、名声、收入、变动与代价，再允许在散文中合写。
- `rank` 使用多级 specificity：具体身份保持高门槛，但已受组合支持的教育层级、专业性质、技术工作、权责和收入方向不得退回性格或流程套话。
- 每个 primary finding 必须携带逐 process handoff、phase、closure、strength snapshot、cost、treatment、residual problem、agency、switch／failure，以及 timing diff（若适用）。
- Formation、advantage、cost、result gate、switch 和 verification 不再允许用一段全盘通用背景替代专题主张。
- Domain carrier resolution 必须逐专题／逐时间窗比较，不能所有年份复制同一 L4 排名和 comparison reason。

### Changed — composition and render

- Composition 负责全盘主锚、关键人生主线、跨专题张力、独立 judgments、coverage mapping 和自足 render-use envelope；Render 不再从卡片或字段猜答案。
- Render 入口必须读取合格详批散文 few-shot 与失败问答 negative few-shot。
- 正文改为主场景驱动的连续散文：标题只按读者真正需要辨认的主线设置，不按 finding、facet、问题、十神或内部字段机械起标题。
- 覆盖与判断清单留在不可见 receipts；内部维度不再渲染成答题册。
- 多个判断可以在少量段落中合成，但每个已冻结方向必须实质出现；不能只剩“综合能力”“压力—资源—输出”等抽象流程。
- Render 只读审计后的 process compositions、scene kernels、findings 与 envelopes；禁止打开 raw Deep Cards、runtime packet 或 Source manifest。
- 新增 detailed-natal prose few-shot、negative question-ledger few-shot、anti-cliche 规则和 reader／full-reading 同文归一化要求。
- 最终交付增加 render-card receipt、coverage-render receipt、按需 reader-answer receipt、独立 delivery scan 和 Render audit。

### Changed — audit and freeze

- Audit 以独立检察官模式运行；生产者自报 PASS、字段齐全、字数、标题数或 judgment 数均不构成通过证据。
- 新增机器 `audit-state` 作为事实源，Markdown audit 只作投影；verdict、计数和 propagation 必须一致。
- 任何方向性修复都要从首次改变的上游重推，更新依赖 hash 和 active manifest；禁止只 patch 最终报告。
- 增加 Lens 预写答案、跨专题通用包、process spine 压缩、L4 排名复用、coverage 错绑、经历污染、脚本硬编码答案和 Render 越权检查。
- Structure、timing、imagery、composition、render 分别冻结；下游必须引用同一 active freeze，旧报告和旧 findings 不得混入。

### Fixed

- 修复“十神都出现了，但实际只在报强弱和一般断语”的假取象。
- 修复把学业判断写成开放写作、抽象表达等通用能力画像，而没有从印、食伤、官杀、财及干支场景判断具体训练方式和考核适配。
- 修复高印／长训练结构因防御性措辞被统一下调为“学习不差但学历未必高”。
- 修复职业专题只写责任感、流程、交付和收尾，没有区分专业技术、制度资格、权责、名声、收入和变动。
- 修复把一个十神直接等同于同事、上司、配偶、医生、某种疾病或具体事件；现在必须结合原局关系后状态、流运触发、柱位与命主当时位置。
- 修复流运临时合、冲、刑或比劫触发被写回原局，或因原局保护存在就删除临时阻碍。
- 修复普通重复支被误报为自刑；自刑仍限定辰、午、酉、亥的同支重复并经关系枚举器裁定。
- 修复 timing 八个维度实际只复制三四句、不同年份载体排序完全相同的问题。
- 修复 coverage receipt 把一个专题全部 facets 指向第一条 judgment，导致真实 judgments 未被追踪。
- 修复回答问题式目录把完整断局压成 42／78 个短答，Render 看似全覆盖却没有围绕太极点铺开。
- 修复内部“生活判断／条件与代价／技术依据”固定栏位直接泄漏到读者正文。
- 修复旧报告、known facts、用户纠错或父／本人命例串案后仍声称盲测通过。

### Breaking changes and migration

- 完整／复杂象核现在要求 fresh producer + independent auditor；不支持干净 agent 的运行环境会在 Imagery 前停止。
- Topic Lens v4.1、process handoff、scene-kernel schema、coverage receipts 和 agent receipts 均与 1.2.0 不兼容；旧 artifacts 不能原地补字段后继续。
- 旧 `output-contract.md`、旧 `topic-lens-schema.md` 和过期 roadmap 已从公开 skill 包删除；当前合同由现实断语合同、Topic Lens v4.1 和各阶段 schema 共同定义。
- Deep Card curation 状态从维护者专名迁移为角色化状态：`draft_pending_human_review`、`pending_human_review`、`runtime_approved_by_human_*`。
- 未随仓库分发的来源从 Windows 绝对路径迁移为 `external-source://...` ID；validator 同时接受现有绝对本地文件或外部来源 URI。
- 从 1.2 升级的命例应把旧 active report、findings、composition、Lens 与 scope 归档为 inactive，从新版 report scope 开始重建；Structure Freeze 只有在 hash 和 schema 仍兼容时才可复核后继续。

### Privacy and portability

- 公开包删除本机盘符、私有目录、命例路径、thread ID、known facts 和维护者个人名状态。
- 外部课程／笔记只保留稳定来源 ID、portable scope 与 excluded scope；原文件不随仓库提交。
- `.gitignore` 继续隔离 forward tests、case artifacts、private、subject context 和本地覆盖文件。
- 发布扫描明确检查维护者本机目录、命例 ID、临时截图、AppData、blind-run answers、`__pycache__` 与 `.pyc`。

### Validation and release status

- 八个 skills 均纳入 `quick_validate.py`。
- 新增／扩展 Reader 枚举、route endpoint、process handoff、Deep Card index、runtime diversity、Topic Lens、carrier resolution、scene-kernel、coverage、question closure、Render coverage 和 delivery artifact 测试。
- Scene Kernel validator tests 覆盖 selected-unit 等值、遗漏 unit、伪造全覆盖、agent provenance 和脚本生成判断文本等失败样本。
- 2.0.0-rc.1 不把已知命例上的修复样章宣称为盲测成果；正式 2.0.0 仍以全新命例、全新 producer、独立 auditor 和解封后对照为发布条件。

## [1.2.0] - 2026-08-05

### Summary

在冻结全盘结构之后新增独立的“用神太极核”，再由每个生活领域建立“领域体—用神枢纽—实际关系轴”，逐轴生产场景和 finding。Render 不再把结构核直接扩写成宽泛断语，也不再依赖增加审计门来弥补内容颗粒度不足。

### Added

- 新增 `use-kernel.md` schema：锁定主用、辅用、备用、病药关系、扶抑／调候／通关分工、可用条件与失败条件。
- 新增领域关系轴：每个 topic 必须说明领域体如何接入用神，哪些柱、藏干、路线和现实载体共同组成这一轴。
- 新增 `axis-scenes`：按关系轴组合天干、地支、十神、柱位、藏干和全局修正，先形成完整场景，再收束为 finding。
- 新增 source packet 的 `required_imagery_units` 与 `axis_id` 覆盖，确保取象材料围绕实际关系轴加载。

### Changed

- Structure Freeze 现在同时冻结 `structure-kernel` 与 `use-kernel`；任一缺失或变化都必须重新审计。
- Report Scope Intake 只接收自然语言问题中心，不要求求测者自行挑十神或柱位。
- Topic Lens 从信号清单改为“领域体 + 用神枢纽 + 实际关系轴”，不再对所有词条做无差别枚举。
- Imagery Composition 改为逐轴分段生产；一个 finding 必须有可复核的机制、场景展开、正反表现、条件、代价与现实载体。
- Render 只压缩已经审计的 axis scene 和 finding，不得用一句抽象标签替代机制到生活事件的中间层。

### Fixed

- 修复完整报告虽然覆盖很多板块，却每条都只有宽泛概括、无法算作实际断局的问题。
- 修复把“用神”仅当作结构阶段的喜忌标签，未用于后置太极选择和领域展开的问题。
- 修复自由聊天能结合柱位与藏干展开，而正式 Render 反而因固定模板丢失颗粒度的问题。
- 修复继续增加门控和审计项目却没有告诉模型“正确展开长什么样”的结构性缺陷。

## [1.1.0] - 2026-08-05

### Summary

将家庭专属、逐条问答式的强制校准门改为可选的跨领域经历协议。默认只收“准／部分准／不准／记不清”的低负担反馈；只有求测者主动要求“展开验证”时，才进入受冻结、反事实和固定计分约束的详细流运验证。经历显化映射与证据验证不再混称。

### Added

- 新增 `validation-protocol.md`，定义 validation plan、timing overlay／hypothesis freeze、verbatim response、固定 0–8 计分和 score audit。
- 新增 `manifestation-map.md`：只记录表达带和家庭／职场／关系等现实载体，固定标记 `non-evidentiary`。
- 新增 quick feedback：允许整体或逐条回复 `accurate／partly-accurate／inaccurate／unclear-memory`，不自动追问、不进入正式计分。
- 新增 opt-in 详细验证：每次只用一个自然问题处理一个时间窗，用户可随时跳过或回答记不清。
- 新增验证审计模式：检查年史泄漏、缺少反事实、宽泛词计分、已知先验未降权、回应被重写、不完整窗口超前计分和强制详细回填。

### Changed

- 家庭不再承担默认或强制校准锚点；家庭、职场、学业、关系、资源和健康均作为竞争领域载体。
- 完整断局可以在 `manifestation_mapping_state: none`、`validation_state: none` 下完成；未验证不降低结构审计结论，但不得声称已经回验。
- 默认交互从多字段年份问卷改为低负担 quick feedback；只有用户主动说“展开验证”后才收详细年史。
- “说得通”、忙、压力、变化等高基率表述不增加置信度；记不清记为 `unscored`，不作为反证。
- 已知经历必须在 validation plan 中登记、排除或降权；假设冻结后不得换机制、扩领域或改措辞贴合回应。
- `calibration-map.md` 作为历史兼容文件继续可读，但必须标记 `non-evidentiary: true`；新产物优先使用 `manifestation-map.md`。

### Fixed

- 修复家庭 finding 缺少家庭场景时被误判，而同一机制在职场等其他载体中明显显化的问题。
- 修复逐条“符合／有条件／不符合”过于宽泛，既增加用户负担又无法提供区分性证据的问题。
- 修复为了填满评分维度一次性要求事件数量、月份、顺序、领域和返工情况，导致验证体验像填写问卷的问题。
- 修复普通经历合参被表述为证据验证，以及宽泛认同被计入命中分的问题。

### Migration notes

- 旧 `family_calibration_*` 字段迁移为 `manifestation_mapping_*` 与 `validation_*` 两组状态。
- 只需要用户体验反馈时使用 quick feedback；需要正式验证时才建立完整 timing validation 产物集。
- 已有冻结假设可继续使用，但必须保留原始 hash；若补建 validation plan，需要标记为行政性重建且不得改动窗口或假设。

## [1.0.0] - 2026-08-05

### Summary

将 0.1.0 的单体断盘流程重构为八个 sibling skills 组成的可审计流水线。新版要求事实、来源、节点、地支裁决、作用边、主问题、路线、结构冻结、报告范围、逐题取象、校准和渲染分别落盘，禁止模型在一次生成中跳过中间裁决。Structure Freeze 现在明确只是技术结构完成，不等同于面向求测者的完整断局。

### Added

- 新增 `bazi-reader`：确定性枚举四柱、十神、藏干、旬空与关系候选，记录带来源和节气偏移的司令事实，并隔离 `subject-context`。
- 新增 `bazi-source-lookup`：按问题生成结构或取象 Source Packet，记录完整读取范围、来源层、流派冲突、OCR 风险与禁止越界。
- 新增 `bazi-structure-core`：实现 Node Ledger、Interaction Census、Branch Relation Census、Branch Arbitration、Post-Branch Node Ledger、Edge Qualification、System State、Primary Problem、Structured Routes、Conditions Matrix 和 Structure Kernel。
- 新增 `bazi-finding-audit`：审计结构、端点、取象、composition、render 和对话路由；BLOCKER 必须返工，禁止 force pass。
- 新增 `bazi-topic-lens`：将职业、关系、健康、神秘学、创作、岁运和合盘问题映射到冻结结构。
- 新增 `bazi-imagery-composition`：保存完整象义覆盖、逐柱双向着色、领域载体、full-chart sweep、表达带、校准图和 composition。
- 新增 `bazi-render`：只把审计后的 findings 翻译为报告或 Q&A，并对新取象、新领域、岁运、合盘和结构争议执行不同回退路线。
- 新增 Structure Freeze hash、路线端点完整性、枚举覆盖、Render 覆盖与回归测试脚本。
- 新增详细 Pipeline Spec、artifact schemas、状态词表、审计清单、领域载体和对话路由规范。
- 新增 Stage 3.6 Report Scope Intake 与 `report-scope.yaml`，记录命盘主人、求测者关系、默认太极中心、报告模式、四个基础板块和附加专题。
- 新增 `topic-lens-index.yaml` 与逐题 Lens 契约；完整原局强制分别处理 `family-home`、`education-learning`、`wealth-resource`、`career-work`。
- 新增家庭盲校准门：家庭判断先生产、先审计，随后才向求测者展示 2–6 条可核判断并读取回应；支持 `completed`、`declined`、`uncalibrated` 与 `contaminated` 状态。
- 扩展 Render 覆盖检查器，支持 `--scope report-scope.yaml`，机械核对基础板块、已选专题、finding／小节一一映射及校准门状态。

### Changed

- `bazi-structure-dynamics` 从一口气执行全盘的单体 skill 改为总编排器。
- 完整原局必须先通过 Structure Audit 并生成 `structure-freeze-receipt`，之后才能进入具体取象、岁运或合盘。
- 重复地支和同五行藏干按位置保留独立节点，不再提前聚合。
- 三会、三合、半合、六合、六冲、刑、自刑、害、破、重复支和共享支改为独立关系专表，并要求无命中类别保留 negative scan。
- 地支裁决必须逐节点写回；`qualified-edge-map` 只能引用关系后状态，不能绕回原始节点。
- 藏干的存在、根气、环境供给、直接做功和格用资格分层记录；不透不自动等于无效，冲也不自动等于开库。
- 作用边新增 `direct-action`、`root-support`、`environmental-feed`、`branch-relation` 和 `composition-only` 分层。
- 在比较救应前新增 `problem-state`；路线分别记录 actual throughput、net effect 和 therapeutic priority。
- 路线只能引用 Edge Map 的 edge ID，并由端点展开脚本检查 source、target、action、layer 与 distance 漂移。
- 系统库存、实际吞吐、蓄积、瓶颈、启动权、控制权、停机能力和自治子系统分开，不再用“身强／身弱”一项覆盖。
- 经历、旧解读、杯卦或其他反馈只能在盲结构与盲 finding 通过后用于 calibration，不能改写节点、边、路线或普遍规则。
- 取象必须读取完整展开材料，并逐层组合天干、地支、十神、柱位、藏干与全局修正；同柱互染不得伪造成结构 active edge。
- 行业、名声、资源、可见度和收入改为不同现实载体，不再由单一十神标签直接等同。
- 将 natal 交付显式分为 `full-reading`、`structure-only` 和 `limited-topic`：只有 full-reading 走完 Stage 0–6.5 才可称完整断局。
- 结构冻结后先确认自然语言求测中心，再由 Topic Lens 为每个生活板块独立选择技术太极；不要求求测者自行选择十神、柱位或作用边。
- Source Lookup、Imagery Composition、Finding Audit 与 Render 改为逐 topic 落盘；四个基础板块可互相引用，但不得合并为泛化的“综合性格”。
- calibration 从一般性的后置事实校准细化为可审计门状态；家庭经历不得在家庭 blind findings 审计通过前进入上下文。

### Fixed

- 修复已知司令仍被重复写成 unknown、或司令修正后只改最终断语而不重跑下游的问题。
- 修复只检查醒目合局而遗漏自刑、共享支、重复支及其他地支关系的问题。
- 修复“旬空所以不算开库”“冲则藏干全部释放”和同支藏干自动生克等层级混淆。
- 修复有根、有箭头、五行齐全或图上闭环被误判为真实流通。
- 修复把实际通量最大的加重路线误叫成救应或出口。
- 修复把系统能够自行运行误写成日主能够主动调用和停止。
- 修复路线端点在 Kernel 中漂移，例如局部土→金接口被扩写为远距离全局通关。
- 修复结构 finding 被经历污染，以及贴切故事反向决定格局、用神和作用边。
- 修复 Render 压缩掉条件、代价、反证，或在聊天追问中自由新增上游没有的判断。
- 修复把完整的 Structure Kernel 直接标成“完整断局”，导致家庭、学业、财运或事业没有实际展开的问题。
- 修复只围绕一个醒目专题写报告、漏掉基础板块或用户已选专题，却仍声称全盘交付完成的问题。
- 修复用一段泛化性格替代多个生活领域，以及同一 finding 被重复塞进多个小节的问题。
- 修复先读取家庭经历再生成所谓“盲断”，或在污染上下文中错误宣称完成盲校准的问题。

### Breaking changes

- 1.0.0 必须安装 `skill/` 下全部八个目录；只安装 `bazi-structure-dynamics` 将无法运行完整流程。
- 0.1.0 的一次性输出不等同于 1.0.0 的阶段产物，不能直接伪装为已经通过 Structure Freeze。
- 岁运与合盘必须建立在审计通过的 natal 上；直接叠盘需要在 case manifest 中显式声明。
- `full-reading` 在 Structure Freeze 后必须生成 `report-scope.yaml`，并分别完成家庭、学业、财运、事业四个基础 topic；旧的 structure-only 产物不能再标为完整原局报告。
- `limited-topic` 可以只交付约定专题，但必须明确未覆盖范围；省略基础四板块时不得使用“完整断盘”或同义完成声明。

### Source compatibility

- 保留 0.1.0 已公开的原典、评注、课程路由和完整材料。
- 本地全文头部的绝对路径不覆盖远端脱敏版本。
- 新增 Source Packet 与完整取象包的证据收据要求，不改变各来源的署名和权利边界。

## [0.1.0] - 2026-08-03

### Added

- 首次公开发布 `bazi-structure-dynamics` skill。
- 建立天干、藏干、月令与位置分账的结构动力工作流。
- 建立月令格局、格神／功能用神／相神及竞争制化路线的分析框架。
- 加入《千里命稿》《子平真诠》原本与评注、若境清课程的来源路由和完整证据材料。
- 加入 DOCX、EPUB、纯文本和本地媒体的资料摄取脚本。
- 加入输出契约、来源保真规范与既有解读审计要求。

### Publication notes

- 将《千里命稿》高保真整理版纳入 skill，移除对发布者本机绝对路径的依赖。
- 清除资料头部的本机目录信息，保留可公开理解的来源文件名与来源层级。
