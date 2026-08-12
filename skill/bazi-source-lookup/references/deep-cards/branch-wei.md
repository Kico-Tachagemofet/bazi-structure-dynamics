# DC-BRANCH-WEI｜未土 Deep Card

- `version`: 0.3
- `status`: approved
- `review_state`: runtime_approved_by_human_2026-08-10
- `symbol_fact`: 地支未；五行、月令、节气、藏干、司令、墓库身份及关系事实由 Reader／Structure Core 提供
- `role`: 季夏燥暖土场、己丁乙接口、成熟收藏机制与现实载体候选；不负责重算月令、司令、旺衰、合冲刑害、会局、开库、透干激活或事件
- `structural_authority`: none
- `runtime_contract`: unit_permissions_v0.1
- `branch_manifestation_contract`: field-qi-function-result-v1
- `static_hidden_stems_authority`: Reader
- `static_hidden_stems`: [己, 丁, 乙]
- `commander_authority`: Reader_month_command_with_source
- `commander_sequence`: [丁9, 乙3, 己18]
- `commander_does_not_rewrite_hidden_stems`: true

## 1. Core seasonal field

未是十二月令循环中的**季夏燥暖土场与成熟收藏容器**。《千里命稿》列未属阴土、六月，小暑起未月、立秋前结束，静态藏己、丁、乙。它承接午月中心火势，把余热带入土体，使生长物进入熟化、形成味道、沉降、整理和换季收藏；它不是一般“土”的重复，也不是火一入未便完全熄灭。

未继承土的“稼穑”，重点在**材料经过热量与时间后成熟、可食／可用、可整理并进入下一阶段**。己提供主要土体、培育与沉降接口；丁保留余热、熟化和干燥接口；乙保留木性材料、植物成果、根气或待时生长接口。合适的水分、温度、通风和出口可令材料熟成、保存或转序；过干可能焦脆，过湿可能黏滞，余热不足或去处不明则可能停在未熟／待整理状态。

未常称木库，但“木库”是受 Structure 控制的身份与状态入口，不是自动结果。《子平真诠》论杂气明确反对“不冲不发”的机械说法：是否收藏、开合、透出、引动、释放哪一气，以及释放后流向何处，都必须按实际关系裁决。未卡只能解释已冻结身份怎样显化，不能自行宣布乙入墓、开库、木被困、财库或争产。

## 2. Derivation path and fact boundary

```text
土爰稼穑
→ 季夏余热进入土体，使生长物熟化、沉降、成味与换季整理
× 己土主容器＋丁火余热＋乙木材料／根气
→ 丁—乙—己司令时序另作月令查询
→ 木库身份由 Structure 冻结，场在／气在／用起／果显分别桥接
```

### 静态藏干、来源异序、司令时序与木库身份必须分开

- `static_hidden_stems`：Reader 当前登记未藏己、丁、乙，依次为本气、中气、余气。
- `commander_sequence`：徐乐吾评注所录未月司令为丁九日、乙三日、己十八日；实际值由 Reader 按小暑后偏移与表源登记。
- 奇门笔记的本／中／余表列未为己、乙、丁，与 Reader 的己、丁、乙不同；它只作为来源分歧保留，不由本卡调换运行层级。
- “未为木库”只开放 `WEI-STORAGE-ROLE-WOOD` 查询；是否入墓、入库、开库、受损、释放及哪一气参与，全部继承 Structure 裁决。
- 丁或乙透干、岁运引动会增加对应气的现实接口并触发重算，但不会让未中三气整体同时外显。

## 3. Seasonal and paired contrasts

| 对照 | 优先观察 | 本卡不允许的简化 |
|---|---|---|
| 午 → 未 | 午重集中火势与持续输出；未把余热带入土体，转向熟化、沉降与整理 | 午未相邻便火全入土、成果自动形成 |
| 未 → 申 | 未是季夏燥暖土与木火余气容器；申进入孟秋金气发动与水土接口 | 立秋一到乙丁全灭、庚金必强 |
| 未与己 | 未是季节／空间／复合容器；己是主要土体接口 | 未＝己，可套用全部己土人格职业 |
| 未与辰丑戌 | 都是复合土支，但季节、燥湿、余气、墓库对象和转化阶段不同 | 四库皆土所以物象、开库法与结果相同 |
| 未与木库 | 木库是关系后身份；乙接口可库存、待时、受护、受困或释放 | 见未即乙入墓、木尽、财库、房产或开库 |

未的“成熟”是过程候选，不等于一切都圆满或已经完成。只有当材料、温度、水分、时间、容器与出口共同合适时，才可从熟化进一步谈成果；若条件不合，仍可能表现为半熟、焦燥、黏滞、积压、返工或等待下一阶段。

## 4. Derivation routes and embedded-qi interfaces

### A. 季夏熟化、沉降与换季整理路线｜优先

培育到成熟、形成味道、烘干／熟化、沉降、归整、保存和把产物送入下一阶段，是未场的直接机制候选。环境／物件题可由 `field_layer` 进入燥暖土、院落、园圃、粮食／食物、干燥储存或加工容器，不要求己丁乙先逐一透出。

### B. 己本气接口｜土体、培育、吸收与归整

`WEI-QI-JI-MAIN` 解释己在未中的土体、承载、细化处理、培育、吸收、边界与沉降接口。己为本气不等于结果稳定、擅长照顾、从事农业或拥有土地；能否承接余热与植物材料，仍看容量、湿度、作用边和出口。

### C. 丁中气接口｜余热、熟化与保存条件

`WEI-QI-DING-MIDDLE` 依 Reader 口径解释丁在未中的余热、干燥、熟化、信号或待时火性接口。其他来源若把丁列余气，本卡只登记分歧。丁是否能把材料熟化、是否过热焦燥或只是残余温度，由 Structure 与状态桥决定。

### D. 乙余气接口｜植物材料、根气与木库库存

`WEI-QI-YI-RESIDUAL` 依 Reader 口径解释乙的植物材料、根气、纤维、成果或待时生长接口。乙藏于未不等于木已经死亡、被困或一定入库；透乙、会局或岁运触发时，只重算乙节点的参与范围和实际去处。

### E. 丁—乙—己司令过渡｜仅限月令查询

`WEI-COMMANDER-DING-YI-JI` 解释未月内部余火、木性材料与土体主事的气序候选。日数“未可执着”，司令顺序也不改写静态己—丁—乙层级。

### F. 木库、收藏与释放路线｜受控机制

`WEI-STORAGE-ROLE-WOOD` 只在 Structure 已确认木库／墓身份、关系后状态和释放范围时调用。它可解释植物性资源被收纳、保护、暂存、压缩、等待时机或经触发进入下游；冲、合、刑、透都不能由本卡预设为“开库”，也不能把争产、财库、房屋或某位六亲直接绑定到未。

### G. 味道、胃、食物与动物路线｜同音／生肖候选

“未—味”“胃”的联想可帮助搜索成熟后的味道、食物、消化承接与腹部容器，但属于文字／同音桥，必须有饮食、身体或物件题才能调用。羊、驴来自生肖与课程动物象；丰满、圆厚是形态候选。均不得直推贪吃、肥胖、胃病、糖尿病、温顺或劳动命。

### H. 院落、果园与公共职责路线｜分级处理

院落、园圃、果园、农作物与干燥储存空间可回接土体、植物成果和成熟收藏。课程把未进一步联想到公务员，但从单支到身份的桥不足，本版只记录为来源缺口／context-only，不建立可晋级 runtime unit。

## 5. Manifestation and state switches

| layer | 未卡可解释什么 | 未通过时仍保留什么 |
|---|---|---|
| `field_layer` | 季夏、燥暖土、熟化、沉降、成味、换季整理与复合容器 | `field-present`；环境／物件题可直接桥接 |
| `qi_layer` | 己丁乙各自的土体、余热、植物材料、根气、库存或待时状态 | 未透仍保留 stock／root-support／environmental-feed／timing-pending |
| `function_layer` | 获 direct-action gate 的具体藏气、木库身份、真实作用边、通量与承接 | 一气起用不等于三气齐发、整体开库或静态等级改变 |
| `result_layer` | 熟化、保存、释放、焦燥、黏滞或积压是否进入现实领域 | 未接通时只写场、库存、机制或候选 |

- **温度、水分、时间、容器与出口合适**：可培育成熟、成味、干燥保存、分类沉降并转入下一阶段。
- **过干或余热过强**：才考虑焦脆、干裂、营养／弹性下降和保存条件恶化；燥暖本身不等于失衡。
- **过湿、通风不足或出口受阻**：才考虑黏滞、发酵失控、积压和返工；土能承载不等于无限吸收。
- **乙木获通道**：可成为植物成果、纤维材料、根气或下一轮生长接口；是否释放与能否继续生长看完整路线。
- **timing／synastry 激活**：只重算被引动气、木库状态、作用边、释放范围和 expiry，不回写原局或预定事件。

## 6. Candidate expressions

### 性质与动作

培育、熟化、成味、吸收、沉降、归整、收藏、干燥保存和把阶段成果送往下一流程。人物锚点稳定成立时，可查询善于把半成品慢慢处理成熟、维持容器或整理多种材料；条件失配时才查询积压、焦燥、黏滞、返工或舍不得释放，不得固化成温顺、迟钝、贪吃或保守。

### 形态、身体与环境

燥暖、土黄、圆厚、丰满、容器感、院落、园圃、果实与粮食可作形态／场景候选。脾、胃、腹部、消化吸收和代谢只作身体检索入口；“未—胃”有同音成分，必须降权并由多锚点复核。

### 学习、工作与资源

可查询把材料慢慢做熟、整理归档、吸收转化、维护培养、储存与阶段交接等工作性质。农业、食品、园艺、仓储、土地、餐饮和公共服务均须另走领域载体；公务员尤其不能由未单字推出。

### 物件、场所与动物

院落、果园、园圃、田地、粮仓／干燥容器、成熟食物、果实、羊和驴可作候选。房子、产权、争产的用神仍按实际六亲／财产体确定；未、官杀或比劫只能解释被冻结的关系与过程，不能替换财产体。

## 7. Topic axes

| axis | coverage | 领域候选与状态桥 |
|---|---|---|
| `behavior_personality` | `derived_candidate` | 稳定人物锚点下，可查询耐心熟化、整理材料、维护容器和阶段交接；湿热、边界或出口失配时才考虑积压、返工、焦燥或难释放。不得固定成温顺、迟钝、贪吃、肥胖或公务员性格。 |
| `appearance_body` | `derived_candidate` | 可查询圆厚、丰满、燥暖、腹部、脾胃、消化吸收与代谢；同音桥须降权，具体体貌与疾病须身体专题。 |
| `learning_cognition` | `derived_candidate` | 可查询把生材料逐步做熟、吸收沉降、分类归整和阶段复盘；未不直接决定记忆、学历、迟缓或农业知识。 |
| `career_work` | `supported_candidate` | 可查询培育、熟化、食品／材料处理、归整、储存和流程交接性质；农业、食品、园艺、仓储、土地、公务等具体岗位另走领域模块。 |
| `wealth_resource` | `derived_candidate` | 财／资源轴成立时，可查询成熟度、保存成本、库存、释放条件和阶段性兑现；未为木库不等于财库、房产、争产或资源已取得。 |
| `family_relationship` | `derived_candidate` | 六亲身份锁定后，可查询谁在培养、容纳、整理、保存或不愿释放；争产仍以财产体为用，不能把比劫等忌神改成用神，也不能由未指定六亲。 |
| `object_place` | `supported_candidate` | 可查询院落、果园、园圃、田地、粮仓、干燥容器、成熟食物、羊驴；按介质、功能和位置选载体。 |

## 8. Bridge requirements

每次调用至少记录 Reader 中未、己丁乙 qi_rank、未月司令和表源；本题使用的是季夏土场、余热熟化、植物材料、木库、味道／同音还是容器维度；对应藏气处于 field／qi／function／result 哪一层；若用木库，必须引用 Structure 的身份、开合／受损、释放范围、before／after 通量和下游；再比较食品、园艺、储存、土地、身体、动物等载体。具体财产题先锁定财产体和用忌，不得由场景象替换。

## 9. Runtime unit map

| unit_id | unit_class | 对应内容 | allowed_topics | activation requirements | claim ceiling／forbidden promotions | source_layer |
|---|---|---|---|---|---|---|
| `WEI-FIELD-LATESUMMER-EARTH` | `semantic_core` | 季夏、燥暖土、余热入土、熟化、成味、沉降与换季整理 | 全部相关 topic | Reader 确认未节点；query 需要季节／场机制 | 只解释机制；不得重算旺衰、调候、墓库或吉凶 | `bazi_primary＋current_synthesis` |
| `WEI-ACTION-RIPEN-SETTLE-STORE` | `semantic_core` | 培育成熟、成味、吸收、归整、收藏、保存与阶段交接 | behavior_personality／learning_cognition／career_work／wealth_resource／family_relationship／object_place | 领域体、材料、时间、容器和出口成立 | 不得直推温顺、农业、食品、仓储、公务、房产或成熟结果 | `bazi_course＋current_synthesis` |
| `WEI-STATE-MANIFESTATION` | `state_modifier` | 四层显化及成熟／焦燥／黏滞／积压／待时状态 | 全部相关 topic | 引用 branch_manifestation_handoff | 不得自行判开库、三气齐发、成果或事件 | `current_synthesis` |
| `WEI-QI-JI-MAIN` | `state_modifier` | 己本气的土体、培育、吸收、边界、沉降与承载接口 | 全部相关 topic | Reader 己节点及 Structure gate／边／通量 | 本气不等于土地、稳定、照顾、农业或自动得用 | `bazi_primary＋current_synthesis` |
| `WEI-QI-DING-MIDDLE` | `state_modifier` | 依 Reader 口径的丁中气：余热、熟化、干燥与待时火性接口 | 全部相关 topic | Reader 丁节点及 Structure 可用度／去处 | 不因异表改称 residual，不得直推火库、食品成熟或焦燥 | `bazi_primary＋current_synthesis` |
| `WEI-QI-YI-RESIDUAL` | `state_modifier` | 依 Reader 口径的乙余气：植物材料、根气、纤维、成果与待时接口 | 全部相关 topic | Reader 乙节点及 Structure 墓库／可用度／去处 | 不因异表改称 middle，不得直推乙入墓、木死、园艺或财库 | `bazi_primary＋current_synthesis` |
| `WEI-COMMANDER-DING-YI-JI` | `state_modifier` | 未月丁九、乙三、己十八司令过渡 | 月令解释／timing | Reader month_command 有节气偏移与表源 | 不改写 static qi_rank，不按日数机械定命 | `bazi_commentary` |
| `WEI-STORAGE-ROLE-WOOD` | `state_modifier` | 未作木墓／库时的收藏、保护、暂存、压缩、释放与改道机制 | career_work／wealth_resource／family_relationship／object_place | Structure 确认墓库身份、关系后状态、节点与释放范围 | 只到 mechanism；不得直推开库、木死、财库、房产、争产或事件 | `bazi_primary＋bazi_commentary＋current_synthesis` |
| `WEI-SHAPE-DRY-WARM-CONTAINER` | `symbol_carrier` | 燥暖、土黄、圆厚、丰满、院落、园圃、粮食与干燥容器 | appearance_body／object_place／career_work | 形态／介质／场所锚点及竞争载体支持 | 最高 candidate；不得直断体型、土地、房屋、农业或仓储职业 | `bazi_course＋current_synthesis` |
| `WEI-WORDPLAY-TASTE-STOMACH` | `symbol_carrier` | “未—味—胃”的同音桥：成熟味道、食物、胃与腹部容器 | appearance_body／object_place／career_work | 明确饮食／身体／物件题且至少一个独立锚点 | 必须降权；不得单凭同音诊断胃病、贪吃、食品业或事件 | `bazi_course＋cross_system_common_symbol` |
| `WEI-OBJECT-COURTYARD-ORCHARD` | `symbol_carrier` | 院落、果园、园圃、田地、粮仓、成熟食物与果实 | object_place／career_work／wealth_resource | 场所／材料／产品功能及位置共振 | 最高 candidate；不得直推房产、土地所有权、农业或餐饮职业 | `bazi_course＋current_synthesis` |
| `WEI-ANIMAL-SHEEP-DONKEY` | `symbol_carrier` | 羊、驴及相关动物／物件候选 | object_place／family_relationship | 明确动物／生肖题和场景锚点 | 不得类比出温顺、劳碌、固执、肥胖或六亲身份 | `bazi_course` |
| `WEI-BODY-SPLEEN-STOMACH-METABOLISM` | `symbol_carrier` | 脾、胃、腹部、消化吸收与代谢候选 | appearance_body | 身体专题、位置与多锚点；同音只作辅助 | 不得诊断胃炎、糖尿病、脾胃病、肥胖或固定体质 | `bazi_course＋current_synthesis` |
| `WEI-CROSS-QIMEN` | `cross_system_context` | 己乙丁异序、季夏成熟成味及状态随关系变化等线索 | 仅明确需要的相关 topic | 去除宫卦、奇门关系和断验后仍可回接共同符号 | source-only context；不得改写 Reader、木库、结构、职业或人格 | `cross_system_common_symbol` |

农业、食品、餐饮、园艺、仓储、土地、公务及任何财库／房产／争产／疾病事件均须另走领域载体或事件审计，不由未卡独立晋级。

## 10. Cannot decide

本卡不能单独决定未是否旺、己丁乙谁主事、异表层级取舍、未是否作为木墓／库及怎样开合释放、午未合／丑未冲／丑未戌刑／亥卯未局是否成立，也不能决定人格、职业、体貌、疾病、食物、房产、财库、争产与事件。

## 11. Source receipts

### S0｜共同底座
- 文件：`skill/bazi-source-lookup/references/deep-cards/five-elements-core.md`；`skill/bazi-source-lookup/references/deep-cards/earthly-branches-core.md`
- 支持：土爰稼穑；四层显化、逐藏气接口与墓库受控调用
- provenance：`current_synthesis`

### S1｜《千里命稿》原典
- 文件：`external-source://qianli-minggao-pdf`；`skill/bazi-structure-dynamics/references/qianli-minggao-fidelity-full.md`
- 核读：地支篇未条、人元问答与力量分析
- 支持：未属阴土、六月、小暑至立秋、藏己丁乙；人元有层级
- 边界：合冲刑害、木局、开库与实际作用进入 Structure；静态顺序由 Reader 继承
- provenance：`bazi_primary`

### S2｜《子平真诠》原本与徐乐吾评注
- 文件：`skill/bazi-structure-dynamics/references/ziping-zhenquan-original-full.md`；`skill/bazi-structure-dynamics/references/ziping-zhenquan-commentary-full.md`
- 核读：论杂气、未月实例、透干会支、反对机械冲库及司令表
- 支持：杂气须按透干会支与路线取用，不能“不冲不发”；未月司令丁九、乙三、己十八
- 边界：墓库身份、开合、释放范围与格局由 Structure 裁决；日数未可执着
- provenance：`bazi_primary＋bazi_commentary`

### S3｜若境清课程
- 文件：`skill/bazi-structure-dynamics/references/ruojing-qianli-01-full.md`
- 可迁移：丰满形态、食物／胃同音、羊驴、院落果园、脾胃与代谢等候选
- 降权／排除：胃炎、糖尿病不作诊断；公务员推导桥不足，仅记 source gap，不设 runtime unit
- provenance：`bazi_course`

### S4｜奇门共同符号材料
- 文件：`external-source://qimen-note-03-five-elements`；`external-source://qimen-note-05-earthly-branches`
- 可迁移：稼穑、季夏、火势下降、成熟成味及土场随湿热条件改变
- 来源分歧：奇门表列己乙丁，与 Reader 己丁乙不同；只登记，不迁移为运行事实
- 不迁移：宫卦、奇门关系、旺衰、固定人格与断验
- provenance：`cross_system_common_symbol`

### S5｜当前架构归纳
- 内容：把未整理为余热进入土体后的熟化收藏场，分开己丁乙静态接口、丁乙己司令与 Structure 控制的木库身份
- provenance：`current_synthesis`

## 12. Forward-test questions

1. 模型能否区分未场与己天干，并把成熟理解为条件过程而非既成好结果？
2. 能否继承 Reader 己丁乙，同时把奇门己乙丁异序留在来源层？
3. 能否区分静态藏干、丁乙己司令、木库身份和岁运透干激活？
4. 面对冲合透干时，能否只重算实际节点与释放范围，不整体开库或断乙木死亡？
5. 能否使用食物、胃、院落、果园、羊驴等候选而不直推疾病、职业、房产或争产？
