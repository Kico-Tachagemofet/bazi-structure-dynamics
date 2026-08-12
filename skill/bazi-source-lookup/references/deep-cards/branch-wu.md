# DC-BRANCH-WU｜午火 Deep Card

- `version`: 0.3
- `status`: approved
- `review_state`: runtime_approved_by_human_2026-08-10
- `symbol_fact`: 地支午；五行、月令、节气、藏干、司令及关系事实由 Reader 提供
- `role`: 仲夏火势中心、丁己接口与现实载体候选；不负责重算月令、司令、旺衰、合冲刑害、会局、透干激活或事件
- `structural_authority`: none
- `runtime_contract`: unit_permissions_v0.1
- `branch_manifestation_contract`: field-qi-function-result-v1
- `static_hidden_stems_authority`: Reader
- `static_hidden_stems`: [丁, 己]
- `commander_authority`: Reader_month_command_with_source
- `commander_sequence`: [丙10, 己9, 丁11]
- `commander_does_not_rewrite_hidden_stems`: true

## 1. Core seasonal field

午是十二月令循环中的**仲夏火势中心与转折场**。《千里命稿》列午属火、南方、五月，芒种起午月、小暑前结束，命理操作上作阴支，静态藏丁、己。它把巳月已经发动的升温与显露推到持续照明、集中输出和高温成形的阶段；同时午月包含夏至附近的阴阳转折，所以“达到峰值”与“开始转向”可以同时存在，不能简化成只升不降。

午继承火的“炎上”，但仲夏中心不等于一切结果都强烈。应分别核对：**热量强度、光的覆盖、信号是否集中、对象能否承受、转化产物如何沉降，以及输出是否接到现实用途**。丁提供持续而聚焦的火性接口，己提供土化、承载、灰烬／熟化产物与回收接口；午不是纯丁火，也不是看到己便自动“火生土成功”。

奇门笔记把午称为阳火，而《千里命稿》的八字运行口径作阴支，并解释“子午体阳用阴”。本卡保留这组层次差异：午的季节形态可以盛大、居中、外显，运行取用却按阴支／阴用处理。它们不是谁推翻谁，而是观察坐标不同。

## 2. Derivation path and fact boundary

```text
火曰炎上
→ 仲夏热量、照明与信号进入集中持续阶段
× 夏至附近由盛转变，输出同时产生己土式承载／沉降接口
→ 丁主火性、己主产物与承载；丙只在司令过渡中出现
→ 场在／气在／用起／果显分别桥接
```

### 操作阴阳、体用阴阳、静态藏干与司令必须分开

- 八字运行口径依《千里命稿》把午作阴支；同书体用段说“子午体阳用阴”，可解释外在形态与实际作用的层次差异。
- `static_hidden_stems`：Reader 当前登记午藏丁、己，依次为本气、中气。
- `commander_sequence`：徐乐吾评注所录午月司令为丙十日、己九日、丁十一日；实际值由 Reader 按芒种后偏移与表源登记。
- 丙出现在司令气序，不等于午静态藏丙；丙透干、岁运来到或月内前段用事时，应由 Structure 重算丙节点，不得由本卡补写藏干。
- 奇门“阳火”只作另一体系的形态／气势说明，不能覆盖 Reader 的阴支事实。

## 3. Seasonal and paired contrasts

| 对照 | 优先观察 | 本卡不允许的简化 |
|---|---|---|
| 巳 → 午 | 巳是丙戊庚复合火场与升温发动；午是丁己双接口、集中照明与高温中心 | 巳午都是火所以完全同象 |
| 午 → 未 | 午重持续输出与中心火势；未重余热进入土体后的熟化、沉降与收藏 | 午一到未便火灭、结果自动入库 |
| 午与丁 | 午是季节／空间／高温场；丁是其中主要火性接口 | 午＝丁，可套用全部丁火人格职业 |
| 午与己 | 己是承载／转化产物接口；是否成形、沉积或堵塞看作用后状态 | 火生土便一定产生成果、地产或食伤 |
| 午与子 | 仲夏集中外显与仲冬收敛流动方向相反 | 未经 Structure 便宣布子午冲的事故、离散或情绪波动 |

午的“变”首先来自季节峰值后的转向和火遇不同材料时形态改变，不是固定的“三分钟热度”。只有当持续燃料不足、对象承载不住、输出过度或路线频繁换向时，才考虑状态不稳；若能量、节奏与出口匹配，午也可以表现为持久热源、稳定信号和连续生产。

## 4. Derivation routes and embedded-qi interfaces

### A. 仲夏集中照明与持续输出路线｜优先

持续发热、照亮中心、放大可见度、发出信号、保持反应和把过程推至定形，是午场的直接机制候选。场所／物件题可以由 `field_layer` 进入明亮、炎热、开放、居中或电热环境，不要求丁先透干；人物和事件结论仍须逐层桥接。

### B. 丁本气接口｜聚焦、维持与信号

`WU-BRANCH-QI-DING-MAIN` 解释丁在午中的根气、环境供给、持续热源、聚焦照明或待时状态。丁为本气不等于微弱、烛火、文艺、漂亮或情绪细腻；在仲夏场中，它也可以承担连续、高密度和中心化输出，具体尺度由全盘与现实载体决定。

### C. 己中气接口｜沉降、熟化产物与承载

`WU-BRANCH-QI-JI-MIDDLE` 解释己所提供的细土、灰烬、熟化／烘干产物、吸收、平台和后续承载。它可能把火输出固定为可保存成果，也可能吸热、积灰、壅塞或令系统需要清理；不能由己直接断食物、地产、胃病或稳定收成。

### D. 丙—己—丁司令过渡｜仅限月令查询

`WU-BRANCH-COMMANDER-BING-JI-DING` 解释午月内部由丙余势、己承接到丁主事的气序候选。丙在司令表出现但不在静态藏干；日数“未可执着”，不能据此重排丁己或机械定强弱。

### E. 峰值与转向路线｜状态而非判词

午月包含夏至附近的由盛转衰，是“输出达到峰值后开始改变方向”的时间象。它可帮助解释阶段节奏、维持成本和何时需要回收／降温，但不能由午直接断反复、热情消退、事业下滑或关系转折。

### F. 明亮空间、电热设备与虚拟显示路线｜受控候选

影院、舞台、灯光场、发电／供能设备、电子显示、计算机与网络界面可以回接照明、信号和能量转换。文学、影像、虚拟空间也多受离卦联想影响，只能在媒介功能、职业轴、资质和其他节点共同支持时进入候选；午单字不能直接选行业。

### G. 马鹿、观赏植物与身体热象路线｜分层候选

马、鹿来自生肖和课程动物象；观赏树、盆景可回接被持续光热塑形的植物场景。眼、心、循环、胸部与热感只作身体专题检索入口；红眼、胸热、高血压等课程例子不得作为诊断或必然结果。

## 5. Manifestation and state switches

| layer | 午卡可解释什么 | 未通过时仍保留什么 |
|---|---|---|
| `field_layer` | 仲夏、高温中心、持续照明、公开可见、峰值与转向环境 | `field-present`；环境／物件题可直接桥接 |
| `qi_layer` | 丁己各自的根气、库存、环境供给、产物或待时状态 | 未透仍保留 stock／root-support／environmental-feed／timing-pending |
| `function_layer` | 获 direct-action gate 的具体藏气、真实作用边、热量／信号通量及承接 | 一气起用不等于丁己同步发动；司令丙不等于藏丙 |
| `result_layer` | 照明、信号、熟化、定形、能耗或损伤是否进入现实领域 | 未接通时只写场、库存、机制或候选 |

- **持续燃料、对象承载与出口匹配**：可形成稳定照明、信号、热加工、熟化与连续输出。
- **热量过强、冷却不足或对象脆弱**：才考虑灼热、干裂、过度曝光、能耗或循环压力；午本身不是病态。
- **燃料／目标不足**：可能只有中心场、可见性需求或间歇信号，不可固定成“三分钟热度”。
- **己土承接合适**：可把热输出沉降为产品、记录、平台或可保存材料；是否有价值看领域体与下游。
- **timing／synastry 激活**：只重算丁、己或外来丙的实际节点、作用边、覆盖范围和 expiry，不回写原局。

## 6. Candidate expressions

### 性质与动作

聚焦、照明、持续加热、发信号、放大可见度、把过程推到峰值、定形并产生可沉降产物。人物锚点稳定成立时，可查询善于把注意力集中到中心、保持输出或让内容被看见；条件失配时才查询过曝、能耗、刺激过强或维持困难，不得固化成热情、冲动、虚荣或三分钟热度。

### 形态、身体与环境

明亮、红暖、居中、开放、高温、灯光和电热感可作形态／场景候选。眼、心、循环、胸部与体热只作身体检索入口，不从午支直接诊断疾病。

### 学习、工作与资源

可查询聚焦重点、公开表达、影像／信号呈现、持续供能、热加工与把输出固定成成果等工作性质。影视、文学、电力、电子、计算机、网络与舞台均须另走领域载体比较。

### 物件、场所与动物

灯具、影院、舞台、明亮大厅、电站／供能设施、电子显示设备、盆景、观赏树、马和鹿可作候选；不因午支直接选中某一场所或物种。

## 7. Topic axes

| axis | coverage | 领域候选与状态桥 |
|---|---|---|
| `behavior_personality` | `derived_candidate` | 稳定人物锚点下，可查询聚焦中心、持续输出、提高可见度和推动定形；承载或节奏失配时才考虑过曝、刺激过强与维持困难。不得固定成热情、冲动、虚荣或三分钟热度。 |
| `appearance_body` | `derived_candidate` | 可查询明亮、红暖、居中及眼、心、循环、胸部和热感；体貌与疾病须身体专题及多锚点。 |
| `learning_cognition` | `derived_candidate` | 可查询聚焦重点、用图像／信号呈现、公开表达和把内容推到成品；午不直接决定文学、计算机能力、聪明或注意力。 |
| `career_work` | `supported_candidate` | 可查询照明、供能、信号、展示、热加工和持续生产性质；影视、电力、电子、网络、舞台等具体岗位另走领域模块。 |
| `wealth_resource` | `derived_candidate` | 财／资源轴成立时，可查询曝光价值、能源投入、持续成本、热加工与成品沉降；午不等于大财、火行业、资源耗尽或收益见顶。 |
| `family_relationship` | `derived_candidate` | 六亲身份锁定后，可查询谁处于注意力中心、持续供能、要求公开或承接输出；不能由午指定母女、伴侣、冲突或离合事件。 |
| `object_place` | `supported_candidate` | 可查询灯光、影院舞台、明亮空间、电热／供能设备、电子显示、盆景、马鹿；按功能和共振选载体。 |

## 8. Bridge requirements

每次调用至少记录 Reader 中午、丁己 qi_rank、午月司令和表源；本题使用的是热量、照明、信号、中心性、峰值转向还是产物沉降；丁己处于 field／qi／function／result 哪一层；direct-action gate、作用边、持续输入、对象承载、冷却与出口；再比较明亮空间、电热设备、显示媒介、观赏植物、马鹿和身体位置等竞争载体。使用丙司令必须明确它不是午的静态藏干。

## 9. Runtime unit map

| unit_id | unit_class | 对应内容 | allowed_topics | activation requirements | claim ceiling／forbidden promotions | source_layer |
|---|---|---|---|---|---|---|
| `WU-BRANCH-FIELD-MIDSUMMER-FIRE` | `semantic_core` | 仲夏、高温中心、集中照明、持续输出及峰值转向 | 全部相关 topic | Reader 确认午节点；query 需要季节／场机制 | 只解释机制；不得重算旺衰、调候、关系或吉凶 | `bazi_primary＋current_synthesis` |
| `WU-BRANCH-POLARITY-BODY-USE` | `state_modifier` | 命理操作作阴支；体阳用阴的另一层描述 | 全部相关 topic | query 明确涉及阴阳表达；同时引用 Reader 口径 | 不得用体用说或奇门阳火改写运行阴阳与藏干 | `bazi_primary` |
| `WU-BRANCH-ACTION-FOCUS-ILLUMINATE-SIGNAL` | `semantic_core` | 聚焦、照明、发信号、持续供能、热加工与定形 | behavior_personality／learning_cognition／career_work／wealth_resource／object_place | 领域体、能量输入、承载对象和出口成立 | 不得直推热情、出名、影视、电力、电子、网络职业或转折事件 | `bazi_course＋current_synthesis` |
| `WU-BRANCH-STATE-MANIFESTATION` | `state_modifier` | 四层显化及持续／过曝／不足／峰值转向状态 | 全部相关 topic | 引用 branch_manifestation_handoff | 不得自行判旺衰、阴阳转折结果、丁己齐发或现实事件 | `current_synthesis` |
| `WU-BRANCH-QI-DING-MAIN` | `state_modifier` | 丁本气的持续热源、聚焦照明、信号与待时接口 | 全部相关 topic | Reader 丁节点及 Structure gate／边／通量 | 本气不等于烛火、微弱、文艺、漂亮或火已得用 | `bazi_primary＋current_synthesis` |
| `WU-BRANCH-QI-JI-MIDDLE` | `state_modifier` | 己中气的细土、灰烬／熟化产物、吸收与承载接口 | 全部相关 topic | Reader 己节点及 Structure 可用度／去处 | 不得直推食物、地产、胃病、食伤或稳定成果 | `bazi_primary＋current_synthesis` |
| `WU-BRANCH-COMMANDER-BING-JI-DING` | `state_modifier` | 午月丙十、己九、丁十一司令过渡 | 月令解释／timing | Reader month_command 有节气偏移与表源 | 不把丙补进静态藏干，不按日数机械定命 | `bazi_commentary` |
| `WU-BRANCH-SHAPE-BRIGHT-CENTER` | `symbol_carrier` | 明亮、红暖、居中、开放、高温、灯光与可见焦点 | appearance_body／object_place／career_work | 形态／场所／媒介锚点及竞争载体支持 | 最高 candidate；不得直断外貌、中心人物、名气或行业 | `bazi_course＋current_synthesis` |
| `WU-BRANCH-BODY-EYE-HEART-CIRCULATION` | `symbol_carrier` | 眼、心、循环、胸部与热感候选 | appearance_body | 身体专题、位置与多锚点 | 不得诊断红眼、胸热、高血压、心血管或固定体质 | `bazi_course` |
| `WU-BRANCH-ANIMAL-HORSE-DEER` | `symbol_carrier` | 马、鹿及奔行／观赏动物候选 | object_place／family_relationship | 明确动物／生肖题和场景锚点 | 不得类比出奔波、成功、速度、驯服或人格 | `bazi_course` |
| `WU-BRANCH-OBJECT-BRIGHT-ELECTRIC` | `symbol_carrier` | 影院、舞台、灯具、供能设施、电子显示、盆景与观赏树 | object_place／career_work／learning_cognition | 明确场所／设备／媒介／植物题并有功能锚点 | 最高 candidate；不得直推具体行业、住所或事件 | `bazi_course＋current_synthesis` |
| `WU-BRANCH-CROSS-QIMEN` | `cross_system_context` | 阳火称谓、离宫、文学、虚拟、计算机／网络等跨体系线索 | 仅明确需要的相关 topic | 去除宫卦、奇门关系和断验后仍可回接共同符号 | source-only context；不得改写 Reader、结构、能力或职业 | `cross_system_common_symbol` |

影视、文学、电力、电子、计算机、网络、舞台及任何出名／转折／疾病事件均须另走领域载体或事件审计，不由午卡独立晋级。

## 10. Cannot decide

本卡不能单独决定午是否旺、丁己谁主事、司令丙是否实质参与、运行阴支与奇门阳火谁覆盖谁、丁己相生是否形成结果、午未合／子午冲／午午自刑／火局是否成立，也不能决定人格、职业、体貌、疾病、名声、关系与转折事件。

## 11. Source receipts

### S0｜共同底座
- 文件：`skill/bazi-source-lookup/references/deep-cards/five-elements-core.md`；`skill/bazi-source-lookup/references/deep-cards/earthly-branches-core.md`
- 支持：火曰炎上；四层显化、逐藏气接口与受控载体
- provenance：`current_synthesis`

### S1｜《千里命稿》原典
- 文件：`external-source://qianli-minggao-pdf`；`skill/bazi-structure-dynamics/references/qianli-minggao-fidelity-full.md`
- 核读：地支篇午条、人元问答、力量分析与阴阳体用段
- 支持：午属火、南方、五月、芒种至小暑、藏丁己；运行作阴，体阳用阴
- 边界：体用阴阳不改写运行口径；合冲刑害与实际作用进入 Structure
- provenance：`bazi_primary`

### S2｜《子平真诠》原本与徐乐吾评注
- 文件：`skill/bazi-structure-dynamics/references/ziping-zhenquan-original-full.md`；`skill/bazi-structure-dynamics/references/ziping-zhenquan-commentary-full.md`
- 核读：午中己土、通根透藏、月令用事与司令表
- 支持：藏气须按实际透藏与路线取用；午月司令丙十、己九、丁十一
- 边界：丙司令不等于午藏丙；日数未可执着；格局、调候与制化不由 Deep Card 执行
- provenance：`bazi_primary＋bazi_commentary`

### S3｜若境清课程
- 文件：`skill/bazi-structure-dynamics/references/ruojing-qianli-01-full.md`
- 可迁移：马鹿、盆景观赏树、影院、明亮场所、电站、电子显示及身体热象候选
- 降权／排除：离卦文学／虚拟／网络须额外桥；红眼、胸热、高血压等例子不作诊断
- provenance：`bazi_course`

### S4｜奇门共同符号材料
- 文件：`external-source://qimen-note-03-five-elements`；`external-source://qimen-note-05-earthly-branches`
- 可迁移：炎上、仲夏、阴阳交融、盛极转向、火随材料改变形态
- 来源分歧：奇门称午阳火；只保留为形态／体系坐标，不改 Reader 的阴支及丁己
- 不迁移：宫卦、奇门关系、旺衰、固定人格与断验
- provenance：`cross_system_common_symbol`

### S5｜当前架构归纳
- 内容：把午拆为热量、照明、信号、持续输出、峰值转向和产物沉降，分开丁己静态接口与丙己丁司令
- provenance：`current_synthesis`

## 12. Forward-test questions

1. 模型能否区分午场与丁天干，也不把午和巳都压成“火旺”？
2. 能否同时保留运行作阴、体阳用阴及奇门阳火的不同坐标而不混表？
3. 能否记住午静态只藏丁己，丙仅在司令／外来节点中出现？
4. 能否把峰值转向理解为条件节奏，而非固定的三分钟热度或事业下滑？
5. 能否使用影院、电热、网络、马鹿、眼心循环等候选而不直推职业、人格或疾病？
