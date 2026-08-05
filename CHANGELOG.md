# Changelog

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
