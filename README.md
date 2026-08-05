# Bazi Structure Dynamics

一套以结构动力、原典证据和阶段审计分析四柱八字的 Codex skills。

它不要求模型在一次生成里同时完成排盘校验、旺衰、格局、刑冲合害、通关、取象和成文。相反，它把分析拆成八个职责独立的 skill，每一阶段产生可检查的中间产物；下游只能引用已经通过审计的上游结论。

这套流水线同时区分“技术结构已经分析完”和“面向求测者的断盘已经交付完”。Structure Freeze 只是生活断局的起点；完整原局还必须确认求测中心，分别完成家庭、学业、财运、事业四个基础板块，并把用户另选的专题逐题生产、审计和呈现。

当前版本：**1.0.0**

## 为什么要拆成流水线

八字判断的困难不只在于规则多，而在于很多规则会争夺同一个字：

- 同一藏干既可能提供根气，也可能参与制化，但两种作用不是同一层；
- 同一个寅可能参与方会、三合、冲刑与食神路线，不能被每条路线重复满额使用；
- 五行有箭头不等于通关，图上成环也不等于真实周流；
- 实际通量最大的路线，可能正在加重主问题，而不是救应；
- 系统能够自行运转，不等于日主能够主动启动、停止或改道；
- 已发生经历能校准显化方式，却不能倒推格局或替代原典规则。

单次长回答很容易漏掉其中一层，然后在后文用贴切故事掩盖结构缺口。1.0.0 的核心变化，就是把这些判断变成必须逐阶段完成、能够退回修复的工作流。

## 总体架构

```mermaid
flowchart TD
    A["Stage 0<br/>Case Manifest"] --> B["Stage 1<br/>Reader"]
    B --> C["Stage 1.2<br/>Source Packet"]
    C --> D["Stage 1.5–3<br/>Structure Core"]
    D --> E["Stage 3.5<br/>Audit + Freeze"]
    E --> F["Stage 3.6<br/>Report Scope Intake"]
    F --> G["Stage 4A<br/>Topic Index + Per-topic Lens"]
    G --> H{"Timing / Synastry?"}
    H -- "是" --> I["Diff / Overlay + Audit"]
    H -- "否" --> J["Per-topic Imagery Source"]
    I --> J
    J --> K["Topic Findings + Audit"]
    K --> L["Stage 4.6<br/>Family Blind Calibration"]
    L --> M["Composition + Audit"]
    M --> N["Render + Delivery Audit"]
    N -- "新取象或新领域" --> G
    N -- "结构争议" --> D
```

### 阶段与硬门槛

| 阶段 | 负责 skill | 主要产物 | 不能跳过的门槛 |
|---|---|---|---|
| 0 | `bazi-structure-dynamics` | `case-manifest` | 明确问题、模式、流派和允许范围 |
| 1 | `bazi-reader` | `chart-stage1`、事实审计、`subject-context` | 四柱、十神、藏干、司令、旬空与时间边界通过校验 |
| 1.2 | `bazi-source-lookup` | `source-packet` | 记录实际读取的完整章节、来源身份、冲突与证据缺口 |
| 1.5 | `bazi-structure-core` | `node-ledger`、`interaction-census` | 所有天干和逐位置藏干覆盖 100%，关系先枚举后裁决 |
| 2 | `bazi-structure-core` | 地支关系专表、`branch-state`、关系后节点、`qualified-edge-map`、系统与主问题 | 地支竞争已写回每个节点；作用边只能从关系后状态起算 |
| 3 | `bazi-structure-core` | 格局候选、路线、端点锁、条件矩阵、`structure-kernel` | 通量、净作用和治疗优先级分开；路线端点与 Edge Map 一致 |
| 3.5 | `bazi-finding-audit` | 审计报告、`structure-freeze-receipt` | BLOCKER 必须返工；通过 hash 冻结结构 |
| 3.6 | `bazi-render` scope intake | `report-scope.yaml` | 确认命盘主人、求测者角色、太极中心、报告模式、四个基础板块与附加专题；不产断语 |
| 4A | `bazi-topic-lens` | `topic-lens-index`、逐题 Lens | 每个板块单独定太极；full-reading 强制家庭、学业、财运、事业四镜头 |
| 4B–4D | Core timing／synastry、`bazi-source-lookup`、`bazi-imagery-composition` | diff／overlay、逐题完整取象包、逐柱复合、topic findings | 只映射冻结结构，不在取象阶段重算旺衰和格局；每个 topic 独立覆盖 |
| 4.5 | `bazi-finding-audit` | finding audit | finding 通过后才可进入事实校准 |
| 4.6 | `bazi-render` family calibration | 家庭盲校准题与回应状态 | 先生成并审计家庭判断，后读取家庭经历；污染、拒答或未答必须如实标记 |
| 5–5.5 | `bazi-imagery-composition`、`bazi-finding-audit` | calibration map、composition 与审计 | 同柱互染不伪造作用边；经历只校准已有分支，不得反写结构 |
| 6–6.5 | `bazi-render`、`bazi-finding-audit` | 报告或对话回答 | 每个必选和已选 topic 恰好覆盖一次；Render 不得新增 finding |

## Structure Core 具体做什么

Structure Core 是 1.0.0 的核心。它不是“算完旺衰再套格局”，而是依次建立一张有位置、有容量和有条件的网络。

### 1. Node Ledger：先保留每个位置

四个天干和每一枚藏干分别建账。两个寅中的甲、两个午中的丁不能先合并，因为它们的柱位、距离、冲合、根型和可作用对象不同。

每个节点记录得令、根气、透藏、受生、受克泄耗、旬空、燥湿、关系候选、当前占用及最强反证。这个阶段只说明“有什么”，不抢先宣布哪条路线已经成立。

### 2. Interaction Census：关系必须全枚举

先检查天干生克合、同柱干支、六合、六冲、刑、自刑、害、破、三合、半合、方会、重复支、共享支和藏干候选关系。没有命中的类别也保留 negative scan，防止模型只看到最醒目的一个合局。

### 3. Branch Arbitration：地支关系必须改写成员

地支关系不能停留在“有辰戌冲”或“有寅午戌”。每组关系都要裁定：

- 形式成立度与实际通量；
- 合绊、集中、改道、冲动、受损或转化；
- 共享支被多条关系占用时的容量限制；
- 每个成员支和逐枚藏干的关系后状态；
- 旬空降低兑现度与“冲不自动开库”两个独立问题；
- 原局潜伏与岁运补齐后的不同状态。

裁决结果写入 `post-branch-node-ledger`。没有被关系改变的节点也要明确标记 retained，而不是从账上消失。

### 4. Edge Qualification：有关系不等于能起效

作用边只能从关系后节点建立，并区分：

- `direct-action`：能够直接参与生克制化；
- `root-support`：提供根气或承载；
- `environmental-feed`：维持某个接收端的环境供给；
- `branch-relation`：由地支关系产生的集中、合绊或改道；
- `composition-only`：只用于取象组合，不能倒灌为结构作用。

每条边检查上游容量、距离、先后、中间阻断、下游承接、竞争路线和回病旁路。由此避免“有根就是畅通”“同支藏干自动互生”“被冲就全部出库”等常见跳步。

### 5. System State：旺衰只是系统的一项

节点和边稳定后，才聚合五行与十神库存、真实吞吐、蓄积点、最弱环、日主承载力、启动权、控制权、停机能力、自治子系统和正负反馈。

因此“身弱”不会自动抹掉已经发生的食神制杀，“五行齐全”也不会自动得到闭环。系统可以有一条很响的木火土通道，同时金水救援仍然低通量。

### 6. Primary Problem：先锁病，再谈药

在比较用神、救应和出口前，单独生成 `problem-state`，列出主问题、次问题、非问题、维持主问题的反馈、最强反证与改判条件。

之后每条路线必须回答它对这个主问题究竟是：

- 缓解；
- 加重；
- 混合；
- 只提供条件；
- 或者与本题无关。

这一步防止把“最强通道”误叫成“最佳用神”。

### 7. Structured Routes：端点锁定，路线不许手改

格局与制化路线只能引用 `qualified-edge-map` 中已经存在的 edge ID。每条路线分别记录：

- actual throughput：原局实际能跑多少；
- net effect：对主问题的净作用；
- therapeutic priority：若要解决主问题，理论上优先补哪一段；
- 最弱环、代价、旁路、反馈和触发条件。

例如食神制杀与食神生财再生杀可以同时存在，但必须说明它们争夺的是哪一枚甲木、各自能分到多少，以及哪条会把药重新导回病处。

### 8. Conditions、Kernel 与 Freeze

`conditions-matrix` 保存每条路线的成立先后、必要条件、反转节点及岁运接口；它不是预测本身。`structure-kernel` 只收束主组织、有效支援、瓶颈、出口、反馈、控制权和关键开关。

独立审计通过后，`structure-freeze-receipt` 对结构输入生成 hash。后续职业、关系、健康、神秘学、岁运和合盘只能引用这份冻结结构；任何结构文件改变，都必须重新审计。

## 从结构分析到合格断盘

Structure Core 回答的是：命局里有哪些节点，关系裁决后哪些作用边真的能跑，主问题是什么，哪些路线缓解、加重或只是提供条件。它不会自动回答这些结构在家庭、求学、挣钱、工作或某个特殊问题中怎样落地。因此，`structure-kernel` 再完整，也只能称“原局结构分析”，不能单独称为“完整断局”。

本项目把交付分成三种模式：

- `full-reading`：结构冻结后继续执行 Stage 3.6–6.5；固定包含家庭、学业、财运、事业，并覆盖求测者选择的全部附加专题；
- `structure-only`：止于 Stage 3.5，只交付技术结构、主问题、路线和条件，不冒充完整断盘；
- `limited-topic`：只为约定专题生产 finding 和报告，必须明确哪些基础板块没有覆盖。

完整断盘的关键不是把同一个结构核扩写四遍，而是每个生活板块都重新确定太极中心和现实载体。求测者只需用自然语言说明“看谁、看什么关系或看什么事”；`report-scope.yaml` 保存范围合同，`bazi-topic-lens` 再把它转换为技术中心，并为每个 topic 建立独立 Lens、Source Packet、finding 和报告小节。四个基础板块可以互相引用，但不能被一段泛化的“综合性格”替代。

家庭板块另设盲校准门：先在未读取详细家庭经历的上下文中生成并审计 2–6 条可核判断，再询问求测者确认、补条件或否认。反馈只能调节已有表达分支的置信度与排序；不能反向创造节点、作用边或格局。用户拒绝或尚未回应时继续交付并标记 `declined`／`uncalibrated`；上下文已经污染且无法隔离时标记 `contaminated`，不得宣称完成了盲验证。

最终报告必须让 `report-scope.yaml` 中的每个必选和已选 topic 恰好出现一次，并与通过审计的 findings 一一对应。缺了基础板块、漏了用户选题、没有逐题 Lens，或把结构核直接改写成生活故事，都不满足完整断局的完成条件。

## 取象、事实校准与对话

结构回答“什么力量能够怎样运行”，取象回答“它在当前领域可能表现成什么”。两层不得互相替代。

- `bazi-render` 先收集报告范围和自然语言太极中心，不让求测者替模型选择十神或柱位；
- `bazi-topic-lens` 为每个板块分别确定需要哪些柱、节点、路线和完整象义单元；
- `bazi-source-lookup` 读取完整展开版本，不用一句口诀补故事；
- `bazi-imagery-composition` 组合天干本象、地支本象、十神功能、柱位、藏干和全局修正；
- `bazi-finding-audit` 检查反向表现、非显化条件、现实载体和证据边界；
- `bazi-render` 只把通过审计的 findings 写成人能读懂的报告，并机械核对范围覆盖。

用户经历在盲结构与盲 finding 通过后才进入 calibration。家庭校准遵循更严格的先问后读隔离；其他领域也只能提高某个表达分支的置信度，不能修改 node、edge、route 或格局。

对话追问也有路由：

- 已有 finding 的澄清：直接 Render；
- 同一结构的新取象：增量 Source + Imagery；
- 新生活领域：新 Topic Lens；
- 新流年／大运：Timing diff；
- 合盘或直接叠盘：双方 natal 通过后建立 overlay；
- 对合化、开库、司令或作用边的质疑：退回 Structure Core 与 Audit。

## 八个 skills 的职责

| Skill | 职责 |
|---|---|
| `bazi-structure-dynamics` | 总编排、恢复顺序、报告模式与完整断局完成标准 |
| `bazi-reader` | 事实结构化、司令与十神校验、context 隔离 |
| `bazi-source-lookup` | 原典、评注、课程与取象材料的完整来源包 |
| `bazi-structure-core` | 节点、地支裁决、作用边、系统状态、主问题、格局与路线 |
| `bazi-finding-audit` | 结构、逐题 finding、composition、范围覆盖、render 与对话边界审计 |
| `bazi-topic-lens` | 把每个自然语言专题分别映射到冻结结构，并维护 Topic Lens Index |
| `bazi-imagery-composition` | 按 topic 完成逐柱复合、领域载体、finding、校准与 composition |
| `bazi-render` | Report Scope Intake、家庭盲校准、范围完整性检查、报告和受约束的 Q&A 呈现 |

## 仓库结构

```text
skill/
├── bazi-structure-dynamics/   # orchestrator
├── bazi-reader/
├── bazi-source-lookup/
├── bazi-structure-core/
├── bazi-finding-audit/
├── bazi-topic-lens/
├── bazi-imagery-composition/
└── bazi-render/
```

每个 skill 包含自己的 `SKILL.md`、`agents/openai.yaml`，以及按需加载的 `references/` 和确定性 `scripts/`。

## 安装

1. 克隆本仓库。
2. 将 `skill/` 下的 **八个目录全部复制** 到 Codex 的个人 skills 目录。
3. 重启 Codex。

不要只安装 orchestrator：1.0.0 的总 skill 会显式调用七个 sibling skills。

仓库继续保存现有的原典路由、整理文本与课程转写，供 Source Lookup 使用。新增私人书籍或课程时，应使用摄取脚本生成本地 Source Pack；不要把出生资料、`subject-context`、盲测产物或本机绝对路径提交到仓库。

## 使用示例

```text
Use $bazi-structure-dynamics to analyze this 八字. Complete the audited natal structure before imagery or timing.
```

完整断盘会先盲跑并冻结结构，再向求测者确认报告中心和附加专题；家庭、学业、财运、事业是默认不可省略的四个基础板块。若只需要技术结构，请明确要求 `structure-only`。

```text
用 $bazi-structure-dynamics 审计这份旧解读，逐条检查它是否漏了地支关系、共享节点、回病路线或主问题。
```

```text
继续追问这个命局的神秘学取象。先判断是已有 finding、增量取象，还是需要退回结构审计。
```

完整原局至少需要年月日时四柱。涉及真太阳时、月令司令、大运或应期时，还需核对出生地、节气和起运资料。

## 验证

仓库提供：

- Stage 1 确定性事实枚举器；
- 关系枚举覆盖检查；
- 路线端点完整性检查；
- Structure Freeze hash 生成与测试；
- `report-scope.yaml`、四个基础板块、已选专题和家庭校准状态检查；
- Render finding 与报告小节一一覆盖检查；
- 回归预期与测试入口。

发布前应对八个 skill 运行 `quick_validate.py`，再运行自带脚本测试和敏感路径扫描。

## 边界

- 本项目用于传统命理文本研究与结构化分析，不构成医疗、法律、财务或其他专业建议。
- 八字象义可以描述传统模型中的体验和领域载体，不能单独证明超自然来源或替代现实诊断。
- 原文、评注、课程观点和当前结构模型必须分层引用，不得互相冒名。
- 课程转录存在听写待核内容；关键干支、术语、命例与断语应回听原始材料。
- 本仓库未授予统一的开源许可证；来源材料的权利归各自作者或权利人所有。详见 [NOTICE.md](NOTICE.md)。

## 版本记录

参见 [CHANGELOG.md](CHANGELOG.md)。
