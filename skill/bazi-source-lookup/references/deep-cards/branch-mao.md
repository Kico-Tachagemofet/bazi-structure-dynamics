# DC-BRANCH-MAO｜卯木 Deep Card

- `version`: 0.3
- `status`: approved
- `review_state`: runtime_approved_by_human_2026-08-10
- `symbol_fact`: 地支卯；五行、月令、节气、藏干、司令及关系事实由 Reader 提供
- `role`: 仲春专气木场、乙木接口与现实载体候选；不负责重算月令、司令、旺衰、合冲刑害、会局或事件
- `structural_authority`: none
- `runtime_contract`: unit_permissions_v0.1
- `branch_manifestation_contract`: field-qi-function-result-v1
- `static_hidden_stems_authority`: Reader
- `static_hidden_stems`: [乙]
- `commander_authority`: Reader_month_command_with_source
- `commander_sequence`: [甲10, 乙20]
- `commander_does_not_rewrite_hidden_stems`: true

## 1. Core seasonal field

卯是十二月令循环中的**仲春专气木场**。《千里命稿》列卯属阴木、东方、二月，惊蛰起卯月、清明前结束，静态只藏乙。相较寅的复合起步，卯更接近木气进入集中生长、破土舒展、分枝铺开并形成连续绿意的季节中心；它不是乙木天干的同义词，也不只有花草一种物象。

卯继承木的“曲直”，但阴木与仲春环境使其优先呈现为**柔韧伸展、分布式生长、穿越缝隙、编织连接和持续繁衍**。单一藏气说明接口相对集中，不代表卯必然清纯、柔弱、漂亮或没有其他现实载体；关系后状态、位置与领域轴仍会把同一木场改写成植被、道路边界、门户、药材、快速移动的生物或其他承载。

课程把大树优先归给甲木，把卯多取花草、竹子、农作物和灌木。本卡保留这种**优先级**，但不写成“大树禁止项”：若全盘形态、同柱材料、空间体量和其他木节点共同支持，大型林木仍可成为现实载体，只是不能由一个卯字独立选中。

## 2. Derivation path and fact boundary

```text
木曰曲直
→ 仲春温度与空间支持木气集中生长
→ 阴木优先沿可行路径柔韧伸展、分枝、编织与覆盖
→ 专气接口由乙承担，甲只出现在月内司令过渡
→ 场在／气在／用起／果显分别桥接
```

### 静态藏干与司令时序必须分开

- `static_hidden_stems`：Reader 当前登记卯只藏乙，乙为本气。
- `commander_sequence`：徐乐吾评注所录卯月司令为甲十日、乙二十日；实际值由 Reader 按惊蛰后偏移与表源登记。
- 甲在卯月前段司令，不等于“卯静态藏甲乙”；也不能据此把卯解释为甲乙同时等量发用。
- 专气支只有一个藏气接口，但 `field_layer`、乙的根气支持、直接功能与现实结果仍是不同层次。

## 3. Seasonal and paired contrasts

| 对照 | 优先观察 | 本卡不允许的简化 |
|---|---|---|
| 寅 → 卯 | 寅是孟春复合发动；卯是仲春木气集中、破土与铺展 | 寅只粗壮、卯只细弱 |
| 卯 → 辰 | 卯集中于木的生长；辰进入季春湿土与木水土混合过渡 | 卯一到辰便必然入库或受困 |
| 卯与乙 | 卯是季节／空间／专气场；乙是其中的人元接口 | 卯＝乙，可直接套用全部乙木职业人格 |
| 卯与酉 | 都是专气与门户候选，季节和材料方向相反 | 未经 Structure 裁决便宣布卯酉冲的伤损、分离或迁移 |

卯的“专”只说明静态藏气集中。木场仍可能因水源、温度、修剪、空间、金土关系与现实用途不同，表现为茂密、柔韧、修整、攀附、被切割、移植或停在根气层。

## 4. Derivation routes and embedded-qi interfaces

### A. 仲春生长、破土与覆盖路线｜优先

持续生长、破土、分枝、覆盖、更新和形成连续植被，是卯场的直接候选。环境题可由 `field_layer` 进入草地、园圃、街道绿带、农作物区或门户边界，不要求乙先透干。

### B. 乙本气接口｜柔韧与分布式伸展

`MAO-QI-YI-MAIN` 解释乙在卯中的根气、库存、环境供给、待时或已审计直接功能。乙为本气不等于人物必然温柔、善变或从事花艺；它怎样表达仍取决于支撑物、空间、修剪、连接对象和下游去处。

### C. 甲—乙司令过渡｜仅限月令查询

`MAO-COMMANDER-JIA-YI` 解释卯月内部由甲余势向乙专气过渡的来源候选，不改写静态藏干。出生时点不明或框架有争议时只作 source context。

### D. 门户、通道与边界路线｜受控候选

奇门笔记把卯酉称为门户之地，八字课程又给出大街、街道与草坪。可迁移的共同部分是：生长从内部穿出、形成出入口、边界带或连续通道。是否真是门、路、平台或关系入口，须由物件／场所题、柱位与功能锚点决定。

### E. 快速动物与震动路线｜低权重候选

兔、松鼠、羊、鹿、狐狸等来自课程以震卦“跑得快”所作联想；风、雷电也依赖震卦。动物可以在明确动物／生肖题中作为候选，风雷震动则保留跨体系 source-only；均不得直接推成急性子、迁移快或突发事件。

### F. 植物、药材与柔韧材料路线｜现实载体

花草、竹子、农作物、灌木、藤条、纤维、编织物和中药材可回接阴木的生长形态与植物材料。它们是候选族，不是卯的唯一物象；大型树木也不是绝对排除，只需更多体量与形态锚点。

## 5. Manifestation and state switches

| layer | 卯卡可解释什么 | 未通过时仍保留什么 |
|---|---|---|
| `field_layer` | 仲春、东方木季、破土、生长、覆盖、门户／边界与连续绿地 | `field-present`；环境题可直接桥接 |
| `qi_layer` | 乙的库存、根气、环境供给、格局候选或待时范围 | stock／root-support／environmental-feed／timing-pending |
| `function_layer` | 乙节点获准参与的实际边、通量、承接与竞争 | gate 未通过时不删除木场与根气 |
| `result_layer` | 木场或乙功能是否接到人物、身体、工作、财富、关系或物件结果 | 未接通时只写机制或候选 |

- **水源、温度、空间与支撑合适**：可持续生长、分枝、覆盖、连接并形成柔韧结构。
- **修剪与边界合适**：分布式生长可转为精细组织、园艺、编织、路径设计或稳定协作。
- **空间不足、依附点过多或缺少主线**：才考虑缠绕、分散、难以定向或彼此争夺资源；柔韧不等于无原则。
- **过度切割、移植或失去水源**：可表现为生长中断、形态受限或只能保留根气；具体关系由 Structure 给出。
- **关系后与 overlay**：只继承已裁定状态，不自行判木局、东方会局、门户开启、冲刑害或事件。

## 6. Candidate expressions

### 性质与动作

破土、伸展、分枝、覆盖、编织、连接、适应支撑、更新与繁衍。人物锚点和稳定重复成立时，可表现为善于从缝隙寻找路径、连接细节、持续维护关系或让系统长成网络；边界和主线不足时才考虑分散、缠绕与难以收束。

### 形态、身体与环境

细长、柔韧、分枝、成片、绿色、纤维和编织感可作形态候选。肝胆、筋腱、四肢伸展、头发和植物性材料可作身体／物件查询；具体外貌与疾病必须另有多锚点。

### 学习、工作与资源

可查询逐步吸收、连接细节、建立网络、反复修订、栽培维护、柔性协调与分布式增长等性质。园艺、农业、药材、纺织、设计、道路绿化或网络协作只是领域载体线索。

### 物件、场所与动物

花草、竹子、作物、灌木、藤条、纤维、编织物、中药材、草坪、绿带、街道边界、门与出入口可作候选；兔及其他快速动物须有动物／生肖题入口。

## 7. Topic axes

| axis | coverage | 领域候选与状态桥 |
|---|---|---|
| `behavior_personality` | `derived_candidate` | 稳定人物锚点下，可查询柔韧伸展、连接细节、适应支撑、持续维护与网络化生长；主线不足或依附点过多时才考虑分散、缠绕和难收束。不得固定成温柔、善变、胆小或跑得快。 |
| `appearance_body` | `supported_candidate` | 可查询细长、柔韧、分枝、纤维、筋腱、四肢伸展、头发与肝胆；疾病和具体体貌须身体专题。 |
| `learning_cognition` | `derived_candidate` | 可查询从细节连接成网、逐步吸收、反复修订和沿可行路径扩展；卯不直接决定文科、记忆、学历或聪明。 |
| `career_work` | `supported_candidate` | 可查询栽培、维护、协调、编织、设计、网络化增长与植物材料性质；具体园艺、农业、药材、纺织、道路或设计岗位另走领域模块。 |
| `wealth_resource` | `derived_candidate` | 财／资源轴成立时，可查询小单位持续增长、分布式来源、维护成本、网络资源与修剪配置；卯不等于小财、稳定增值或投资农业。 |
| `family_relationship` | `derived_candidate` | 六亲身份锁定后，可查询连接成员、维护日常、适应关系支撑或形成边界／入口；不能由卯直接指定女性、子女、伴侣或合作事件。 |
| `object_place` | `supported_candidate` | 可查询花草竹木、作物、纤维编织物、药材、草坪绿带、街道边界、门户及快速动物；按功能和共振选载体。 |

## 8. Bridge requirements

每次调用至少记录 Reader 中卯、乙与司令事实；本题使用的仲春／木场／门户维度；乙的参与层与 direct-action gate；现实领域和结果条件；植被、材料、门户、道路、动物等竞争载体。使用人格路线须有人物锚点与稳定重复；使用大树时须另有体量、主干和空间证据，不能由卯单字决定。

## 9. Runtime unit map

| unit_id | unit_class | 对应内容 | allowed_topics | activation requirements | claim ceiling／forbidden promotions | source_layer |
|---|---|---|---|---|---|---|
| `MAO-FIELD-MIDSPRING-WOOD` | `semantic_core` | 仲春、东方木季、专气生长、破土、覆盖与连续木场 | 全部相关 topic | Reader 确认卯节点；query 需要季节／场机制 | 只解释机制；不得重算旺衰、关系或吉凶 | `bazi_primary＋current_synthesis` |
| `MAO-ACTION-EMERGE-WEAVE` | `semantic_core` | 伸展、分枝、编织、连接、适应支撑、更新与繁衍 | behavior_personality／learning_cognition／career_work／wealth_resource／family_relationship | 人物／领域体与持续路线成立 | 不得直推温柔、女性、设计师、园艺、药师或网络职业 | `bazi_course＋current_synthesis` |
| `MAO-STATE-MANIFESTATION` | `state_modifier` | 四层显化及茂密／修整／缠绕／中断状态 | 全部相关 topic | 引用 branch_manifestation_handoff | 不得自行判关系、成局、门户开启或结果 | `current_synthesis` |
| `MAO-QI-YI-MAIN` | `state_modifier` | 乙本气的根气、供给、待时与已审计功能 | 全部相关 topic | Reader 乙节点及 Structure gate／边／通量 | 本气不等于柔弱、漂亮、花草或自动得用 | `bazi_primary＋current_synthesis` |
| `MAO-COMMANDER-JIA-YI` | `state_modifier` | 卯月甲十、乙二十司令过渡 | 月令解释／timing | Reader month_command 有节气偏移与表源 | 不把甲补进静态藏干，不按日数机械定命 | `bazi_commentary` |
| `MAO-SHAPE-FLEXIBLE-VEGETATION` | `symbol_carrier` | 细长、柔韧、分枝、花草、竹子、作物、灌木、藤纤维与编织物 | appearance_body／object_place／career_work | 形态／材料／场所锚点及竞争载体支持 | 最高 candidate；大树非优先但非禁项，不得直断体貌或行业 | `bazi_course＋current_synthesis` |
| `MAO-OBJECT-GATEWAY-GREENWAY` | `symbol_carrier` | 门户、出入口、街道边界、草坪、绿带与连续通道 | object_place／career_work／family_relationship | 明确入口／边界／通道功能及位置共振 | 不得直推住宅门户、道路、迁移、合作或开放事件 | `bazi_course＋cross_system_common_symbol` |
| `MAO-BODY-WOOD-FLEXION` | `symbol_carrier` | 肝胆、筋腱、四肢伸展、头发与纤维功能 | appearance_body | 身体专题、位置和多锚点 | 不得诊断肝胆、筋伤、脱发或固定体型 | `bazi_course＋current_synthesis` |
| `MAO-ANIMAL-FAST` | `symbol_carrier` | 兔、松鼠、羊、鹿、狐狸等快速动物候选 | object_place／family_relationship | 明确动物／生肖题和场景锚点 | 不得由动物类比推出胆小、机敏、迁移或急躁人格 | `bazi_course` |
| `MAO-CROSS-QIMEN` | `cross_system_context` | 门户、震动、风、雷电、破土等跨体系线索 | 仅明确需要的相关 topic | 去除卦宫与奇门断验后仍可回接共同形态者 | source-only context；不得进入结构或突发事件判断 | `cross_system_common_symbol` |

园艺、农业、药材、纺织、设计、道路绿化、网络协作及任何门户／迁移事件均须另走领域载体，不由卯卡独立晋级。

## 10. Cannot decide

本卡不能单独决定卯是否旺、乙是否得用、甲乙何者司令、卯戌合／卯酉冲／子卯刑／卯辰害／木局是否成立，也不能决定人格、职业、体貌、疾病、门户或迁移事件。

## 11. Source receipts

### S0｜共同底座
- 文件：`skill/bazi-source-lookup/references/deep-cards/five-elements-core.md`；`skill/bazi-source-lookup/references/deep-cards/earthly-branches-core.md`
- 支持：木曰曲直；四层显化与专气接口
- provenance：`current_synthesis`

### S1｜《千里命稿》原典
- 文件：`external-source://qianli-minggao-pdf`；`skill/bazi-structure-dynamics/references/qianli-minggao-fidelity-full.md`
- 核读：地支篇卯条、人元问答与阴阳体用段
- 支持：卯属阴木、东方、二月、惊蛰至清明、藏乙
- 边界：合冲刑害与会局进入 Structure；专气不等于自动外显或唯一物象
- provenance：`bazi_primary`

### S2｜《子平真诠》原本与徐乐吾评注
- 文件：`skill/bazi-structure-dynamics/references/ziping-zhenquan-original-full.md`；`skill/bazi-structure-dynamics/references/ziping-zhenquan-commentary-full.md`
- 核读：原本论通根、专气月令与地支关系；评注司令表及透藏上下文
- 支持：卯可为木根；司令为甲十、乙二十
- 边界：司令日数未可执着；格局与关系规则不由 Deep Card 执行
- provenance：`bazi_primary＋bazi_commentary`

### S3｜若境清课程
- 文件：`skill/bazi-structure-dynamics/references/ruojing-qianli-01-full.md`
- 可迁移：快速动物、花草竹木、农作物、灌木、街道、草坪、中药等候选
- 降权／排除：震卦风雷不作八字结构；“不能是大树”改写为优先级而非绝对禁令
- provenance：`bazi_course`

### S4｜奇门共同符号材料
- 文件：`external-source://qimen-note-03-five-elements`；`external-source://qimen-note-05-earthly-branches`
- 可迁移：仲春、破土、门户、欣欣向荣、专气及甲—乙气序
- 不迁移：卦宫、关系、旺衰、固定人格与断验
- provenance：`cross_system_common_symbol`

### S5｜当前架构归纳
- 内容：把卯整理为仲春专气木场，保留植物／门户／通道候选并建立七轴与 runtime units
- provenance：`current_synthesis`

## 12. Forward-test questions

1. 模型能否区分卯场与乙天干，不直接套用乙木人格职业？
2. 能否区分卯藏乙与甲乙司令，不把甲补进静态藏干？
3. 能否把花草竹木作为优先候选而非排除大型林木的死规则？
4. 能否使用门户、街道、动物、中药等候选而不直断事件与职业？
5. 能否在不外显时保留木场、根气与待时接口？
