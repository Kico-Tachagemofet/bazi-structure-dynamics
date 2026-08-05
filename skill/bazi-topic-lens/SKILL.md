---
name: bazi-topic-lens
description: 在八字结构与用神太极核冻结后，把求测者的具体问题转换为领域体、适用用神枢纽和逐条体—用关系轴：完整原局分别处理家庭、学业、财运、事业，再处理关系、健康、神秘学、创作、岁运或合盘。用户需要从技术结构进入正常断局、避免四个领域重复同一段泛化机制，或追问首次报告未展开的象意时使用。本技能不重算原局，不产生活断语。
---

# 八字 Topic Lens

本技能负责回答三件事：本题在看什么、用哪一个功能枢纽观察、两者之间有哪些真实关系。它不靠固定板块清单凑 finding，也不从十神标签直接跳生活故事。

## 必需输入

- `case-manifest.yaml`
- `chart-stage1.yaml`
- `structure-kernel.md`
- `use-kernel.md`
- `problem-state.yaml`、`route-candidates.yaml`、`conditions-matrix.md`
- `structure-freeze-receipt.yaml`
- 已通过的 structure audit
- `report-scope.yaml` 或用户的限定具体问题

缺少 `use-kernel.md`、结构冻结或审计未通过时停止。若本轮结构文件晚于 freeze receipt，退回结构审计。

## 两种中心必须分开

- **领域体／问题中心**：求测者究竟在问谁、哪件事、哪一种结果。由 `report-scope.yaml` 和当前问题确定。
- **用神枢纽／技术太极**：盘中哪条主用、辅用或备用路线负责处理这个问题。只能从冻结的 `use-kernel.md` 选择。

求测者不需要自选十神、柱位或喜用神。Render 只收自然语言问题；本技能完成技术锁定。

## 固定工作流

### Step 1：切出具体问题片段

把宽泛领域拆成能够单独回答的 `question_slice`。例如“事业”可能实际问任务性质、组织压力、成果形成或收入接口；只有盘中结构确实提供不同关系时才拆，不按固定目录机械穷举。

一个 question slice 只保留一个主要现实问题。不能把“父母、家庭资源、居住、生活维持”装进同一个问题，再期待下游一句话同时断完。

### Step 2：定义领域体

为每个 question slice 写 `topic_body`：

- 求测者自然语言中心；
- 可能承载该问题的柱位、十神、节点或路线；
- 为什么选这些锚点；
- 最强替代锚点；
- 内部机制、领域载体和外部结果分别指什么。

领域体只是“要看的对象”，不自动等于用神，也不自动等于某个十神。

### Step 3：锁定适用用神枢纽

从 `use-kernel.md` 选择：

- 主用是否直接处理本题；
- 辅用是否只负责承载／启动；
- 备用路线是否在本题比主用更直接；
- 调候需要是否只改质量而不产结果；
- 哪些看似相关的用神口径必须排除。

记录 `use_pivot_lock`，不得在 Topic 阶段重新发明用神。

### Step 4：建立实际体—用关系轴

只列本题真实存在的轴。可从 `use-kernel.md` 的以下方向选择或裁切：

- 用神自身状态；
- 用神怎样处理主问题；
- 谁生用／助用；
- 谁损用、占用或把用改道；
- 用神做功后流向哪里；
- 用神与日主承载、启动、控制的关系；
- 备用路线如何接力、竞争或反转。

每条 `body_use_axis` 必须有一个 `focal_question`、一组明确端点、引用的 edge／route、基线状态、竞争分配和条件开关。若同一节点既制病又经旁路生病，拆成两条轴。

**八字不照搬紫微的“词条全列 → 语义交叉”。** 八字的思考单位是完整的体—用关系轴；后续直接把轴两端的干支、十神、柱位、藏干和结构条件合成场景。

不设统一最低轴数。轴数由本盘真实关系决定；但每条已列主轴必须在下游形成一条 primary finding，或明确记录 `deferred／source-gap`，不得静默消失。

### Step 5：建立取象请求

每条轴分别列：

- 两端相关柱的天干、地支、十神、柱位；
- 相关支的全部藏干及关系后状态；
- 同柱双向着色对；
- 主问题、竞争路线、用神去处和条件开关；
- 需要加载的完整 imagery units；
- 可能的领域载体类型与外部结果所需现实条件；
- 首次未展开、可供后续追问加载的范围。

## 完整原局

`delivery_mode: full-reading` 时，先产 `topic-lens-index.yaml`，再分别建立：

- `family-home`
- `education-learning`
- `wealth-resource`
- `career-work`
- `selected_optional_sections` 中的每个专题

四个基础 topic 可以引用同一个用神枢纽，但必须通过不同的领域体或不同关系轴回答各自问题。若两个 topic 只有完全相同的轴和生活过程，保留一个完整展开，在另一个 topic 建交叉引用；不得复制同一段泛化断语。

limited-topic 只建立约定镜头，同时记录未覆盖基础板块和“不得称完整断局”。

## 岁运与合盘

- 岁运：锁定原局用神核后读取 timing diff，记录哪条关系轴被补齐、占用、改道或反转；不重写 natal 用神核。
- 合盘：双方 natal 分别审计；跨盘节点只作临时接口。可新增 relationship-field 关系轴，但不把对方节点写成本命永久根。
- 直接叠盘必须是 case-manifest 的显式模式。

## 输出

按 [Topic Lens Packet Schema](references/topic-lens-schema.md) 产出 `topic-lens-<slug>.md`，并维护 `topic-lens-index.yaml`。输出后交 `$bazi-source-lookup` 与 `$bazi-imagery-composition`。

本技能不得：

- 重算旺衰、合化、开库、路线或用神；
- 把领域体直接当喜忌；
- 只写“压力、资源、支持、输出”而没有明确端点和过程；
- 产生活断语；
- 用固定轴数替代实际结构。

