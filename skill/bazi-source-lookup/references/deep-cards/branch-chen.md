# DC-BRANCH-CHEN｜辰土 Deep Card

- `version`: 0.3
- `status`: approved
- `review_state`: runtime_approved_by_human_2026-08-10
- `symbol_fact`: 地支辰；五行、月令、节气、藏干、司令、墓库身份及关系事实由 Reader／Structure Core 提供
- `role`: 季春湿土过渡场、戊乙癸复合接口与现实载体候选；不负责重算藏气等级、司令、开库、合局、旺衰或事件
- `structural_authority`: none
- `runtime_contract`: unit_permissions_v0.1
- `branch_manifestation_contract`: field-qi-function-result-v1
- `static_hidden_stems_authority`: Reader
- `static_hidden_stems`: [戊, 乙, 癸]
- `commander_authority`: Reader_month_command_with_source
- `commander_sequence`: [乙9, 癸3, 戊18]
- `commander_does_not_rewrite_hidden_stems`: true

## 1. Core seasonal field

辰是十二月令循环中的**季春湿土过渡场**。《千里命稿》列辰属阳土，为三月，清明起辰月、立夏前结束，静态藏戊、乙、癸；五行方位归土，而春令组又使它处在东方木季的收束端。奇门材料常配东南并称木火分野。这里应分清：土的五行归类、春末季节位置与其他体系的空间配位是不同坐标，不必压成一个方位答案。

辰继承土的“稼穑”：承载、容纳、混合、培育与转化；又保留春木余势与水分，因此优先观察为**含水土体、复合介质、季节换挡与多种材料重新分配的容器**。戊提供土体主接口，乙保留春木路线，癸提供水分／水库接口。湿润可以培育、调和、提取与转化，也可能在过饱和、过热、边界破损或无去处时变成泥泞、混浊、干裂或内部分配竞争。

《子平真诠》明确称辰为杂气，理由不是“杂乱无用”，而是所藏不一、取用须看透干、会支及其有情无情；同书也明确反对“财官入库不冲不发”的机械口诀。因此，“辰为水库”只能作为受 Structure 控制的状态入口，不能自动推出开库、得水、财库、化工、地产或事件。

## 2. Derivation path and fact boundary

```text
土爰稼穑
→ 承载、混合、培育、储存与转化
× 季春木气未尽、水分仍在、夏火将接
→ 含水土介质＋春末复合容器＋季节换挡场
→ 戊／乙／癸逐气核对，不以“杂气”批量激活
→ 场在／气在／用起／果显分别桥接
```

### 静态藏干、等级异表与司令时序必须分开

- `static_hidden_stems`：Reader 当前登记辰藏戊、乙、癸，分别标作本气、中气、余气；本卡运行时继承该事实。
- `commander_sequence`：徐乐吾评注所录辰月司令为乙九日、癸三日、戊十八日；实际值由 Reader 按清明后偏移与表源登记。
- 奇门笔记的本／中／余表列辰为戊／癸／乙；《子平真诠》又以“辰本藏戊、为水库、为乙余气”描述功能层级。两者与当前 Reader 的 qi_rank 不完全相同，须分栏保留，不由 Deep Card 私自改表。
- 乙—癸—戊司令时序不改写静态戊—乙—癸等级；任一气透清或触发，也不自动释放其余两气。

## 3. Seasonal and paired contrasts

| 对照 | 优先观察 | 本卡不允许的简化 |
|---|---|---|
| 卯 → 辰 | 卯是仲春专气木场；辰把木余势、水分与土体带入复合换季容器 | 木进辰便必然入库、受困或转化 |
| 辰 → 巳 | 辰仍在季春含水土场；巳进入孟夏火场与更明显的热、显露 | 立夏一到辰水必干、火必旺 |
| 辰与戊 | 辰是季节／空间／复合容器；戊是其本气接口 | 辰＝戊，可忽略乙癸和水库身份 |
| 辰与丑 | 都可为湿土／储存场；辰偏季春、水库与木余势，丑偏季冬、寒湿与金收藏 | 两者都是“湿土仓库”所以完全同象 |
| 辰与戌 | 都是阳土复合库支，燥湿、季节和内部接口不同 | 未经 Structure 裁决便宣布辰戌冲自动开库 |

辰的“杂”是多接口、多用途和竞争可能，不是负面人格标签。若接口分工清楚、温湿与流入流出可控，它可以成为培育、混合、分离、转化和资源中转场；若内部竞争、边界与去处失配，才考虑状态不稳、混浊、积压或反复改换。

## 4. Derivation routes and embedded-qi interfaces

### A. 季春含水土与换挡路线｜优先

湿土、泥水介质、田园、浅滩、土岭、低洼地、培育床与春末过渡空间，是辰场可直接进入的环境候选。问场所、物件或工作介质时，`field_layer` 不要求戊乙癸先逐一透出。

### B. 戊本气接口｜土体与承载

`CHEN-QI-WU-MAIN` 解释戊在辰中的土体、地基、承载、边界和转化接口。戊为本气不等于它必然压制水木或主导全局；可用度、透出、关系后状态和下游承接仍须逐项审计。

### C. 乙中气接口｜春木余势

`CHEN-QI-YI-MIDDLE` 依 Reader 当前口径解释乙在辰中的根气、春木余势、穿行土体与待时生长接口。其他来源称乙为余气，本卡只登记分歧；实际运行不改写 Reader。乙是否能疏土、继续生长或仅作根气，由 Structure 决定。

### D. 癸余气接口｜水分与收藏

`CHEN-QI-GUI-RESIDUAL` 依 Reader 当前口径解释癸的水分、湿润、内部储水、根气或待时接口。水库身份成立也不等于癸直接做功；透出、会局、冲动与岁运触发均须重算实际节点、通量和去处。

### E. 乙—癸—戊司令过渡｜仅限月令查询

`CHEN-COMMANDER-YI-GUI-WU` 只解释辰月内部气序候选。日数“未可执着”，且不能拿司令顺序替代静态 qi_rank。

### F. 水库、混合、分离与提取路线｜受控机制

辰作为水库时，可提供水分被收藏、暂存、混合、过滤、释放或改道的结构入口。课程从癸水与水库进一步联想到提纯、化工；本卡只保留“混合—分层—过滤／提取—转化”的工作性质，具体化工、精油或实验行业必须由材料、工艺、职业轴和现实资格共同桥接。

### G. 龙、土地、身体躯干与巽位路线｜分层候选

龙来自生肖；田园、土地、土岭、浅滩、庄稼地可回接土场；腹部、腰、肩等来自课程身体联想，范围较宽，只作低权重位置候选。航空、网络、思想、风来自辰巳配巽卦，留作 source-only，不由辰支直接推出行业与人格。

## 5. Manifestation and state switches

| layer | 辰卡可解释什么 | 未通过时仍保留什么 |
|---|---|---|
| `field_layer` | 季春、含水土、混合介质、培育床、浅滩、换季与复合容器 | `field-present`；环境／物件题可直接桥接 |
| `qi_layer` | 戊、乙、癸各自的库存、根气、土体、水分、木余势或待时状态 | 逐气保留 stock／root-support／environmental-feed／timing-pending |
| `function_layer` | 获 direct-action gate 的具体藏气、实际边、通量、承接和竞争 | 一气发用不等于三气同步发动或开库 |
| `result_layer` | 场或具体功能是否接到人物、身体、工作、财富、关系或物件结果 | 未接通时只写场、库存、机制或候选 |

- **温湿、边界、流入流出合适**：可培育、混合、分层、储存、过滤和把材料送往下一阶段。
- **水分过多或出口不足**：才考虑泥泞、混浊、积压和边界模糊；湿土本身不是失衡。
- **受热、失水或容器破损**：可转为干裂、沉积、快速释放或原有培育条件下降；不能仅见火便断水尽。
- **乙木有根并获通道**：可疏导、穿行、继续生长或把土水转成植被；实际成本与成果看完整路线。
- **墓库／合冲会刑介入**：只读 Structure 的身份、占用、释放范围与 before／after 通量；冲不自动开库，会不自动把戊乙癸全部化水。
- **timing／synastry**：只重算命中的藏气、作用边、覆盖范围和 expiry，不回写原局。

## 6. Candidate expressions

### 性质与动作

承载、混合、培育、储存、分层、过滤、提取、中转与季节换挡。人物锚点和稳定重复成立时，可表现为能处理多种材料、维持复杂容器并在条件成熟后重新分配；边界、温湿或接口竞争失配时才考虑状态反复、混浊、积压和难以定向。

### 形态、身体与环境

湿润、厚实、泥水混合、低洼、浅滩、田地、土岭、夹层与库容感可作候选。腹部、腰、肩、消化承接、水液储存和躯干支撑属于身体检索入口，具体部位与疾病必须另有多锚点。

### 学习、工作与资源

可查询把不同材料放入同一框架、分类沉淀、混合试验、过滤提取、维护库存、从春季生长切换到下一流程等性质。农业、土地、地产、仓储、化工、实验提纯、供应链、网络或航空均只是需另行比较的领域线索。

### 物件、场所与动物

田园、庄稼地、湿地、浅滩、土岭、水库、蓄水池、混合／过滤容器、地下或夹层空间及龙类生肖意象可作候选。地产不等于房子用神，水库也不等于财库。

## 7. Topic axes

| axis | coverage | 领域候选与状态桥 |
|---|---|---|
| `behavior_personality` | `derived_candidate` | 人物锚点与稳定重复成立时，可查询承接复杂材料、混合分层、维护容器和在换挡期重新分配；边界或接口竞争失配时才考虑状态反复、混浊、积压与方向未明。不得固定成善变、悲观、城府深或会管理。 |
| `appearance_body` | `derived_candidate` | 可查询厚实、含水、层叠、库容感，以及腹部、腰、肩、消化承接、水液储存与躯干支撑；具体体貌疾病须身体专题。 |
| `learning_cognition` | `derived_candidate` | 可查询把异质材料归入框架、分层沉淀、过滤提取与阶段转换；接口竞争时再考虑信息混杂和难以下结论。辰不直接决定理工、化学或网络能力。 |
| `career_work` | `supported_candidate` | 可查询承载、混合、培育、库存、过滤、提取、中转和流程切换性质；农业、地产、化工、实验、供应链、航空／网络等具体载体另走领域模块。 |
| `wealth_resource` | `derived_candidate` | 财／资源轴成立时，可查询入库、混合资产、流动性、维护成本、释放条件和资源再分配；辰为水库不等于财库、房产或钱已取得。 |
| `family_relationship` | `derived_candidate` | 六亲身份锁定后，可查询谁在承接多方事务、保存资源、调节边界或让问题停在内部容器；争产仍以财产体为用，辰只解释场与过程。 |
| `object_place` | `supported_candidate` | 可查询田园湿地、浅滩土岭、水库蓄水池、混合过滤容器、夹层空间及龙类意象；须按介质、功能和共振选载体。 |

## 8. Bridge requirements

每次调用至少记录 Reader 中辰、戊乙癸 qi_rank、司令与表源；本题使用的季春／湿土／水库／换挡维度；戊乙癸逐气参与层；直接功能的 gate、边、通量和承接；若使用水库，引用 Structure 的墓库身份、开合、受损、释放与结果去处；再比较土地、水体、容器、提取流程、身体位置和生肖等载体。异表只留 source receipt，不改运行事实。

## 9. Runtime unit map

| unit_id | unit_class | 对应内容 | allowed_topics | activation requirements | claim ceiling／forbidden promotions | source_layer |
|---|---|---|---|---|---|---|
| `CHEN-FIELD-LATESPRING-EARTH` | `semantic_core` | 季春、含水土、木季收束、换挡、混合介质与复合容器 | 全部相关 topic | Reader 确认辰节点；query 需要场／季节／介质 | 只解释机制；不得重算旺衰、调候、关系或吉凶 | `bazi_primary＋current_synthesis` |
| `CHEN-ACTION-MIX-SEPARATE-TRANSITION` | `semantic_core` | 承载、混合、培育、分层、过滤、提取、中转和流程换挡 | behavior_personality／learning_cognition／career_work／wealth_resource／family_relationship | 人物／领域体、材料流入流出与持续路线成立 | 不得直推管理、化工、地产、实验、供应链或网络职业 | `bazi_course＋current_synthesis` |
| `CHEN-STATE-MANIFESTATION` | `state_modifier` | 四层显化及湿润／泥泞／干裂／沉积／释放状态 | 全部相关 topic | 引用 branch_manifestation_handoff | 不得自行判合冲刑、开库、成局或结果 | `current_synthesis` |
| `CHEN-QI-WU-MAIN` | `state_modifier` | 戊本气的土体、边界、承载与转化接口 | 全部相关 topic | Reader 戊节点及 Structure gate／边／通量 | 本气不等于独占整支、压水木或自动得用 | `bazi_primary＋current_synthesis` |
| `CHEN-QI-YI-MIDDLE` | `state_modifier` | 依 Reader 口径的乙中气：春木余势、根气与穿行接口 | 全部相关 topic | Reader 乙节点及 Structure 可用度／去处 | 不得因异表私改 residual，也不得直推植物、疏土或成长成果 | `bazi_primary＋current_synthesis` |
| `CHEN-QI-GUI-RESIDUAL` | `state_modifier` | 依 Reader 口径的癸余气：水分、储水、根气与待时接口 | 全部相关 topic | Reader 癸节点及 Structure 墓库／可用度／承接 | 不得因异表私改 middle，不得自动开库、得水或发财 | `bazi_primary＋current_synthesis` |
| `CHEN-COMMANDER-YI-GUI-WU` | `state_modifier` | 辰月乙九、癸三、戊十八司令过渡 | 月令解释／timing | Reader month_command 有节气偏移与表源 | 不改写 static qi_rank，不按日数机械定命 | `bazi_commentary` |
| `CHEN-STORAGE-ROLE-WATER` | `state_modifier` | 辰作为水墓／库时的收藏、暂存、释放与改道机制 | career_work／wealth_resource／object_place | Structure 确认墓库身份、关系后状态、节点与释放范围 | 只到 mechanism；不得直推开库、财库、水务、化工或事件 | `bazi_primary＋bazi_commentary＋current_synthesis` |
| `CHEN-SHAPE-MOIST-LAND-CONTAINER` | `symbol_carrier` | 湿土、田园、浅滩、土岭、低洼地、蓄水和混合过滤容器 | appearance_body／object_place／career_work | 介质／形态／场所锚点与竞争载体支持 | 最高 candidate；不得直断房产、农地、水库、化工场所或体型 | `bazi_course＋cross_system_common_symbol＋current_synthesis` |
| `CHEN-BODY-TRUNK-STORAGE` | `symbol_carrier` | 腹部、腰、肩、消化承接、水液储存和躯干支撑候选 | appearance_body | 身体专题、位置与多锚点 | 不得诊断腹腰肩疾病、湿病、消化或水液问题 | `bazi_course` |
| `CHEN-ZODIAC-DRAGON` | `symbol_carrier` | 龙及生肖／图形场景 | object_place／family_relationship | 明确动物／生肖／物件题并有额外锚点 | 不得类比出权贵、神秘、飞腾、成功或固定人格 | `bazi_course` |
| `CHEN-CROSS-QIMEN` | `cross_system_context` | 东南／巽、木火分野、风、航空、网络及戊癸乙异表线索 | 仅明确需要的相关 topic | 只作追溯；去除宫卦与断验后仍能回接共同符号 | source-only context；不得改写 Reader、进入结构或职业断验 | `cross_system_common_symbol` |

具体农业、地产、仓储、化工、实验提纯、供应链、航空、互联网及房产／财库事件均须另走领域载体，不由辰卡独立晋级。

## 10. Cannot decide

本卡不能单独决定辰是否旺、戊乙癸谁主事、qi_rank 异表取舍、司令值、水库是否开、申子辰局、辰酉合、辰戌冲、卯辰害或自刑结果，也不能决定地产化工职业、房产财富、人格、体貌、疾病与事件。

## 11. Source receipts

### S0｜共同底座
- 文件：`skill/bazi-source-lookup/references/deep-cards/five-elements-core.md`；`skill/bazi-source-lookup/references/deep-cards/earthly-branches-core.md`
- 支持：土爰稼穑；四层显化、逐藏气接口与墓库受控调用
- provenance：`current_synthesis`

### S1｜《千里命稿》原典
- 文件：`external-source://qianli-minggao-pdf`；`skill/bazi-structure-dynamics/references/qianli-minggao-fidelity-full.md`
- 核读：地支篇辰条、人元问答与力量分析
- 支持：辰属阳土、三月、清明至立夏、藏戊乙癸；人元有层级
- 边界：合冲刑害、水局与开库进入 Structure；表中藏序由 Reader 继承
- provenance：`bazi_primary`

### S2｜《子平真诠》原本与徐乐吾评注
- 文件：`skill/bazi-structure-dynamics/references/ziping-zhenquan-original-full.md`；`skill/bazi-structure-dynamics/references/ziping-zhenquan-commentary-full.md`
- 核读：论杂气如何取用、通根、透干会支及反对机械冲库；评注司令表
- 支持：辰本藏戊、为水库、又有乙余气；杂气须按透干会支与有情无情；司令为乙九、癸三、戊十八
- 来源差异：原本称乙余气，当前 Reader 依《千里命稿》次序标乙 middle、癸 residual；卡片不越权重排
- provenance：`bazi_primary＋bazi_commentary`

### S3｜若境清课程
- 文件：`skill/bazi-structure-dynamics/references/ruojing-qianli-01-full.md`
- 可迁移：腹腰肩、龙、田园土地、土岭、浅滩、庄稼地、水库、混合提取等候选
- 降权／排除：化工、地产不作固定职业；航空、网络来自巽卦旁支；身体例子不作诊断
- provenance：`bazi_course`

### S4｜奇门共同符号材料
- 文件：`external-source://qimen-note-03-five-elements`；`external-source://qimen-note-05-earthly-branches`
- 可迁移：季春、湿土、水库、木火过渡、培育、舒展与乙—癸—戊气序
- 来源分歧：本／中／余表列戊／癸／乙，与 Reader 戊／乙／癸不同；仅登记，不迁移为事实
- 不迁移：宫卦、奇门关系、旺衰、固定人格与断验
- provenance：`cross_system_common_symbol`

### S5｜当前架构归纳
- 内容：把辰整理为季春含水土复合容器，分开静态 qi_rank、司令与水库身份，并建立七轴 runtime units
- provenance：`current_synthesis`

## 12. Forward-test questions

1. 模型能否把辰作为季春复合土场，而不直接等同戊土、水库或地产？
2. 能否继承 Reader 戊乙癸，同时把原本／奇门的等级差异留在来源层？
3. 能否区分静态藏气、乙癸戊司令和水库关系后身份？
4. 一气透出或冲会触发时，能否只重算实际节点而不整体开库？
5. 能否使用土地、浅滩、化工提取、龙、身体位置等候选而不直断？
