# Bazi Structure Dynamics

一套面向 Codex 的四柱八字多 Skill 工作流。它先把四柱事实、旺衰承载、格局、十神竞争和用神路线收束清楚，再把固定材料交给无历史上下文的独立 reader-writer，由它在同一个写作过程里完成取象、现实判断和中文断盘。

当前版本：**2.0.0-rc.2**

本版是一次大幅瘦身重构。旧版把大量精力消耗在 audit state、freeze、hash、coverage receipt、runtime packet、scene-kernel job、逐专题 producer／auditor 和 Render validator 上，运行时间很长，最后的正文却仍可能像性格测试。rc.2 删除了这套冗余审计屎山，把重点重新放回两件事：结构算对，以及报告真的能断出人生层级、现实载体、结果、代价和岁运变化。

## 默认流程

```text
Reader
  核对四柱、十神、藏干、司令、旬空和时间边界
        ↓
Structure
  收束旺衰、格局、十神主链、竞争路线与用神
        ↓
Scope gate
  向用户确认命主、专题、性别口径和岁运范围
        ↓
Sealed reading pack
  固定事实、结构、范围、来源笔记和相关 Deep Cards
        ↓
Fresh reader-writer
  在无历史上下文中独立取象并写 full-reading.md
```

普通完整报告不再默认经过：

```text
Topic Lens → per-topic runtime packets → scene kernels
→ findings → coverage receipts → Composition → pure Render
→ delivery scan
```

Topic Lens、Imagery Composition 和 Finding Audit 仍然保留，但只用于明确请求的诊断、分析底稿、污染检查或 benchmark，不再绑架普通断盘。

## 为什么改成 Fresh Reader-Writer

八字的现实判断高度依赖十神链、天干动作、地支场景、藏干参与和柱位范围在写作过程中的持续交叉。旧版把取象、finding、composition 和 Render 分给多层文件后，真正有用的关系容易在中间被压平，Render 最后只能把几条抽象结论扩写得更长。

rc.2 让下游 writer 同时承担：

- 理解已固定的旺衰格局和用神；
- 比较十神的主路线与竞争路线；
- 组合天干、地支、藏干和柱位；
- 判断学历、职业性质、技术动作、权责、名声、收入、关系与变动；
- 比较现实载体家族并决定主次；
- 把这些内容写成自然完整的中文断盘。

writer 可以自由决定章节、标题、段落顺序和详略。Skill 不要求固定问答、统一段落模板、judgment ID 或内部审计措辞。

## Scope gate：先问清楚看什么

本版修复了“用户只说看看这个盘，AI 就自行扩成完整报告”的问题。

- 显式调用 `$bazi-reader` 时，默认只交付事实，不自动进入旺衰或报告。
- “断一下”“看看”“分析一下”不等于已经授权完整原局、感情、健康或岁运。
- 范围不明确时，结构完成后必须询问并等待：
  - 命主本人还是代看；
  - 完整原局还是指定专题；
  - 是否包含大运和哪些流年；
  - 感情、六亲、子女需要的性别口径。
- 用户回答前不创建 `report-scope.yaml`、Topic Lens、reading notebook、Composition 或报告。
- 若用户明确追求精确还原具体学历／学位、离婚婚次、职业身份／机构、官职或标志性事件，入口会先说明八字的能力边界；环境已安装紫微飞星 Skills 时，建议优先使用 `$ziwei-feixing-core-v2`，原始紫微盘面先经 `$ziwei-reader`，再以八字补充结构与推运。

用户已经把范围说清时，不重复确认。

## Sealed reading pack

范围确认后，上游创建一份固定的 `reading-pack/`：

```text
reading-pack/
├── handoff.md
├── chart-stage1.yaml
├── structure-notebook.md
├── report-scope.yaml
├── source-notes.md
└── materials/
```

`materials/` 只包含本盘实际出现并参与结构的五行、十神、天干、地支、重要藏干和用户要求的岁运材料。

reading pack 不包含旧报告、旧 findings、用户纠错、预期答案、经历材料、Topic Lens、reading notebook、Composition、few-shot、审计文件或其他命例。用户明确允许经历合参时，handoff 必须标为 `non-blind`。

在支持 sub-agent 的 Codex 环境中，总编排使用 `fork_turns="none"` 启动 fresh writer。没有 fresh-context 能力时，流程停在 reading pack，并让使用者在新任务中继续，不在已经加载大量上游规则的长 session 中冒充干净写作。

## 快速开始

1. 克隆本仓库。
2. 把 `skill/` 下八个目录全部复制到 Codex 的个人 Skills 目录。
3. 重启 Codex。
4. 从总入口开始：

```text
Use $bazi-structure-dynamics to verify this chart, confirm the reading scope with me,
seal the structure materials, and hand them to a fresh reader-writer.
```

只想先核盘时：

```text
Use $bazi-reader to extract and verify only the chart facts, then stop.
```

已有 sealed pack、只需新窗口写报告时：

```text
Use $bazi-render to read this sealed reading-pack and independently write the report.
```

## 八个 Skills

| Skill | 默认职责 |
|---|---|
| `bazi-structure-dynamics` | 总编排、Scope gate、reading pack 与 fresh-context handoff |
| `bazi-reader` | 四柱事实、十神、藏干、司令、旬空与时间边界；显式调用后停止 |
| `bazi-source-lookup` | 结构规则、原典依据、相关 Deep Cards 与候选取象材料 |
| `bazi-structure-core` | 旺衰、格局、关系、十神竞争、用神与失败路线；不预写生活答案 |
| `bazi-render` | 从 sealed pack 独立取象、判断并写完整报告 |
| `bazi-topic-lens` | 可选的专题材料缺口诊断 |
| `bazi-imagery-composition` | 可选的取象推导底稿与专题深拆 |
| `bazi-finding-audit` | 仅在显式要求时进行法证式语义复核 |

八个目录应一并安装。后面三个虽然不属于普通主线，仍用于追问、诊断与正式测试。

## 默认产物

普通完整报告只需要：

1. `case-manifest.yaml`
2. `chart-stage1.yaml`
3. `source-notes.md`
4. `structure-notebook.md`
5. `report-scope.yaml`
6. `reading-pack/`
7. `full-reading.md`

不再默认生成 audit state、active manifest、freeze receipt、coverage registry、逐专题 packet、逐年三件套、scene-kernel jobs、reader 分卷、Render receipt 或 delivery scan。

## 岁运

大运和流年先继承原局仍在运行的结构，再判断外来干支实际改变了哪些关系、路线和角色。上游只固定结构变化，不预写事件；fresh writer 在报告中自然展开用户指定的大运和独立流年。

流运不能回写原局，合不自动化，冲不自动开库，重复支不自动等于自刑。临时出现的比劫、官杀、印、财或食伤，需要结合原局保证、命主当时位置和现实载体判断。

## 这个项目适合什么

从当前前向测试看，八字更稳定的长处是：

- 判断一个命局的结构性质与主要矛盾；
- 区分技术型、制度型、研究型、经营型或输出型等职业性质；
- 判断能力怎样转成权责、收入和代价；
- 分析大运流年何时改变原局路线；
- 对已知现实方向做结构和时间上的交叉验证。

它不保证从原局盲断中稳定恢复博士、离婚、精确职业身份等高特异度履历。若主要目标是高精度还原具体人生领域和事件，传统术数使用者可以优先使用 `$ziwei-feixing-core-v2`，再以八字补充结构与推运。两者都属于传统文化解释体系，不是经科学验证的预测工具。

本项目不构成医疗、法律、财务或其他专业建议。

## 来源与隐私

公开包使用仓库相对路径和 `external-source://...` 标识，不包含维护者本机绝对路径。出生资料、命例、旧报告、subject context、盲测答案、用户经历和临时 reading packs 均不应提交。

Deep Cards 是取象候选材料，不决定旺衰、格局或事件。其他术数材料只能提供可回接阴阳五行、季节与形态的共同符号层。

权利与来源说明见 [NOTICE](NOTICE.md)。仓库目前没有统一开源许可证；除非文件另有许可，不应假定可以复制、再发布或商用全部内容。

## 验证

rc.2 已完成：

- 8/8 `quick_validate.py`；
- Skill Markdown 引用检查；
- 本机路径、命例 ID、thread ID 与 few-shot 扫描；
- 显式 Reader 范围门前向测试；
- 无历史上下文 sealed-pack writer 前向测试。

静态 validator 只能证明 Skill 结构与引用有效，不能证明命理判断为客观事实。后续仍应使用未讨论的新命例测试实际报告质量。

## 从 rc.1 升级

rc.2 是破坏性工作流变更：

- 旧的 Topic Lens、runtime packets、scene kernels、findings、Composition 和 Render receipts 不再是默认输入；
- 旧报告不能冒充 sealed-pack fresh reading；
- 显式 Reader 调用不再自动进入完整流水线；
- `bazi-render` 从纯翻译层改为 fresh reader-writer；
- 同盘 few-shot 已从公开运行时删除；
- 旧 case 建议保留归档，按新版事实、结构、scope 和 reading pack 重建。

完整变更见 [CHANGELOG](CHANGELOG.md)。
