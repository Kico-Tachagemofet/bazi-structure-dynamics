# DC-BRANCH-XU｜戌土 Deep Card

- `version`: 0.3
- `status`: approved
- `review_state`: runtime_approved_by_human_2026-08-10
- `symbol_fact`: 地支戌；五行、月令、节气、藏干、司令、墓库身份及关系事实由 Reader／Structure Core 提供
- `role`: 季秋燥土收尾场、戊辛丁接口、火库机制与现实载体候选；不负责重算月令、司令、旺衰、合冲刑害、会局、开库、透干激活或事件
- `structural_authority`: none
- `runtime_contract`: unit_permissions_v0.1
- `branch_manifestation_contract`: field-qi-function-result-v1
- `static_hidden_stems_authority`: Reader
- `static_hidden_stems`: [戊, 辛, 丁]
- `commander_authority`: Reader_month_command_with_source
- `commander_sequence`: [辛9, 丁3, 戊18]
- `commander_does_not_rewrite_hidden_stems`: true

## 1. Core seasonal field

戌是十二月令循环中的**季秋燥土收尾场与火性收藏容器**。《千里命稿》列戌属阳土、九月，寒露起戌月、立冬前结束，静态藏戊、辛、丁。它承接酉月金气成形后的收束，把秋金余势、逐渐下降的温度与残存火种纳入燥土，进入封边、归整、干燥保存、清理旧物和向冬季移交的阶段。

戌继承土的“稼穑”，但其季秋位置使重点不在继续培育，而在**承接已经完成或正在衰退的材料，划定边界、干燥固结、封存火种、处理残余并腾出下一周期的空间**。奇门生长序列把戌说成“万物的消亡”，本卡只迁移生命周期的收尾、凋落、归藏与分解候选，不把戌直接等同死亡、失败、衰败人格或现实灾祸。

戊提供主要燥土、边界和封存接口；辛保留秋金的修整、残余器物和精细清理接口；丁保留火种、余温、照明／文化材料和待时释放接口。合适的水分、温度、容器和出口可使材料得到保存、归档或安全交接；过燥可能焦脆、开裂，受水过度可能松散、泥化或令封存失效。

## 2. Derivation path and fact boundary

```text
土爰稼穑
→ 季秋把成熟后的材料、金性余势与残火带入收尾容器
→ 戊主边界／封存＋辛主修整／残余金气＋丁主火种／余温
→ 辛—丁—戊司令时序另作月令查询
→ 火库身份由 Structure 冻结，场在／气在／用起／果显分别桥接
```

### 静态藏干、来源异序、司令与火库身份必须分开

- `static_hidden_stems`：Reader 当前登记戌藏戊、辛、丁，依次为本气、中气、余气；《千里命稿》整理表与此一致。
- 奇门笔记的本／中／余表列戌为戊、丁、辛，与 Reader 的戊、辛、丁不同；徐乐吾评注又称戌为金之余气。异表只保留在来源层，本卡不越权换位。
- `commander_sequence`：徐乐吾评注所录戌月司令为辛九日、丁三日、戊十八日；实际值由 Reader 按寒露后偏移与表源登记。
- “戌为火库”只开放 `XU-STORAGE-ROLE-FIRE` 查询；丙丁是否通根、收藏、受护、受困、透出或释放，由 Structure 裁决。
- 辛或丁透干、岁运引动，只触发相应节点重算；不表示戌被整体打开，也不使戊辛丁同步外显。

## 3. Seasonal and paired contrasts

| 对照 | 优先观察 | 本卡不允许的简化 |
|---|---|---|
| 酉 → 戌 | 酉重专气金的精炼完成；戌把金余势、丁火种与戊土带入季秋收尾容器 | 金进戌便完全入库、器物必埋 |
| 戌 → 亥 | 戌重燥土封存与周期收尾；亥进入孟冬水场、汇流与种子／潜在生机 | 立冬一到戌火必灭、土必被水冲散 |
| 戌与戊 | 戌是季节／空间／复合容器；戊是主要土体接口 | 戌＝戊，可套用全部戊土人格职业 |
| 戌与火库 | 火库是关系后身份；丁接口可收藏、待时、受护、受困或释放 | 见戌即火灭、火库开、文化玄学或能源事件 |
| 戌与辰丑未 | 都是复合土支，但季节、燥湿、余气、墓库对象和收尾阶段不同 | 四库同法，逢冲皆开且结果相同 |

戌的“收尾”并不等于只能终止。清理残余、保存火种和建立边界也可以为下一周期留下接口；若封存与释放条件不匹配，才可能表现为积压、僵结、过度干燥、旧物不清或火热闷在内部。

## 4. Derivation routes and embedded-qi interfaces

### A. 季秋归整、干燥与移交路线｜优先

收束、清理、固结、干燥保存、封边、归档、处理残余和为下一阶段腾出空间，是戌场的直接机制候选。环境／物件题可由 `field_layer` 进入燥土、围墙／边界、干燥储存、炉灰、燃料／火种容器和季末清理空间，不要求戊辛丁先逐一透出。

### B. 戊本气接口｜燥土、主边界与封存容器

`XU-QI-WU-MAIN` 解释戊的土石、平台、围护、固结、主边界、封存与待时承载。戊为本气不等于可靠、固执、房地产、城墙或能镇水；干湿、体量、开合方式与下游用途仍须逐项检查。

### C. 辛中气接口｜秋金余势、精整与残余器物

`XU-QI-XIN-MIDDLE` 依 Reader 口径解释辛的金属细件、锋芒、修整、质量检查、残余器物或待时接口。其他来源若把辛列余气，本卡只登记分歧。辛是否被土埋、获得保护、继续精炼或成为清理工具，取决于实际关系与出口。

### D. 丁余气接口｜火种、余温与待时照明

`XU-QI-DING-RESIDUAL` 依 Reader 口径解释丁的余温、火种、灯火、热加工、文化／仪式媒介或待时接口。丁藏于火库不等于火已熄灭或一定能保存；透丁、会火或岁运触发时，只重算丁节点的实际参与和去处。

### E. 辛—丁—戊司令过渡｜仅限月令查询

`XU-COMMANDER-XIN-DING-WU` 解释戌月内部金余势、火库气与土体主事的气序候选。日数“未可执着”，司令不重排静态戊—辛—丁，也不预定哪一气成为本盘功能。

### F. 火库、保存与释放路线｜受控机制

`XU-STORAGE-ROLE-FIRE` 只在 Structure 已确认火墓／库身份、节点、关系后状态与释放范围时调用。它可解释热量、燃料、灯火、文化／仪式媒介被收纳、保护、闷存、等待、受损或经触发进入下游；冲、合、刑、透都不能由本卡预设为“开库”。

### G. 炉窑、燃料、寺庙与工业路线｜分级载体

炉窑、炉灰、燃料／火种容器、围护场和干燥加工空间可以回接燥土与火库。寺庙／香火、化工、石油、冶炼、军工等课程载体需要宗教仪式、材料工艺、职业权责和现实场所的独立锚点；戌卡最多提供火种封存、耐热容器和收尾处理的 candidate lead。

### H. 狗狼、皮肤与干燥路线｜分层候选

狗是生肖载体，豺狼来自课程“像狗”的动物联想。皮肤、体液边界、燥裂、炎热闷存只作身体专题检索入口；不得直接诊断皮肤病、虚弱或炎症，也不得由动物类比推出忠诚、凶狠、群体性或社会身份。

### I. 虚拟媒介协作路线｜不得由“戌—虚”启动

课程从“戌／虚”延伸到虚拟、玄学、虚伪、狡诈、互联网与编辑部，但两字并非严格同音，从谐音直接推人格、行业或媒介的桥接过长，本版不采用这种启动方式。虚拟媒介的显像、光影、界面和信息可见性应先由离火／火性显化、信息或实际媒介轴独立成立。

若该轴已经成立，戌可以作为**协作节点**解释媒介背后的载体、实质内容、规则边界、存续／归档、基础设施和结项清理；它不是“虚拟外壳”，也不能单独证明互联网、编辑、平台或玄学职业。`XU-MEDIA-CARRIER-GOVERNANCE` 只能在上游媒介轴已冻结后按需开放。

## 5. Manifestation and state switches

| layer | 戌卡可解释什么 | 未通过时仍保留什么 |
|---|---|---|
| `field_layer` | 季秋、燥土、收尾、固结、封边、干燥保存、残余处理与火库容器 | `field-present`；环境／物件题可直接桥接 |
| `qi_layer` | 戊辛丁各自的土体、金余势、火种、材料、库存或待时状态 | 未透仍保留 stock／root-support／environmental-feed／timing-pending |
| `function_layer` | 获 direct-action gate 的具体藏气、火库身份、真实作用边、通量与承接 | 一气起用不等于三气齐发、整体开库或静态等级改变 |
| `result_layer` | 保存、释放、清理、固结、焦裂、闷热或积压是否进入现实领域 | 未接通时只写场、库存、机制或候选 |

- **干燥程度、容器、边界和出口合适**：可收尾、清理、固结、保存火种并完成阶段移交。
- **过燥或余热闷存**：才考虑焦脆、开裂、内部热压和材料失去弹性；燥土本身不等于病。
- **水分适中且有排出路径**：可能调节燥烈、帮助清理或使容器保持可用；水过多、冲刷强或边界破损时也可能松散失封。
- **辛金获得通路**：可进行精整、筛除残余或形成器具；土厚无出口时才考虑埋金与清理困难。
- **timing／synastry 激活**：只重算被引动气、火库状态、作用边、释放范围和 expiry，不回写原局或预定事件。

## 6. Candidate expressions

### 性质与动作

收束、清理、固结、封边、干燥保存、处理残余、保留火种和阶段移交。人物锚点稳定成立时，可查询善于结束流程、守住边界、整理遗留并保留下一步资源；条件失配时才查询过度封闭、积压、焦燥或旧物难清，不得固定成虚伪、狡诈、悲观、虚弱或黑社会人格。

### 形态、身体与环境

燥暖、土石、围护、封闭、干燥、灰烬、炉火余温和容器感可作形态／场景候选。皮肤、体液边界、干燥与热量闷存只作身体检索入口，不直接诊断疾病。

### 学习、工作与资源

可查询结项、归档、清理遗留、质量收尾、保存关键火种／知识和把材料移交下一流程等性质。仓储、档案、炉窑、能源、化工、冶炼、宗教空间等具体载体须另走领域模块。虚拟、玄学、互联网不由戌卡提供入口；媒介轴已由离火／信息节点成立时，戌才可补充其载体、内容存续、规则和归档机制。

### 物件、场所与动物

干燥土石、墙垣围护、炉窑、灰烬、燃料／火种容器、干燥储存空间、狗及豺狼可作候选。寺庙／香火须有独立宗教与仪式锚点；房产、土地、能源库存也须先锁定领域体。

## 7. Topic axes

| axis | coverage | 领域候选与状态桥 |
|---|---|---|
| `behavior_personality` | `derived_candidate` | 稳定人物锚点下，可查询结项清理、守住边界、处理遗留和保存下一步资源；干湿、开合或出口失配时才考虑封闭、积压、焦燥与难以放下。不得固定成虚伪、狡诈、虚弱、凶狠、乞丐或黑社会人格。 |
| `appearance_body` | `derived_candidate` | 可查询燥暖、土石／围护感、皮肤、体液边界、干燥与热量闷存；具体体貌和疾病须身体专题及多锚点。 |
| `learning_cognition` | `derived_candidate` | 可查询结项、归档、清理冗余、保存核心材料和完成阶段交接；戌不直接决定玄学、虚拟思维或编辑能力。媒介轴另已成立时，才补充内容存续、规则边界与归档。 |
| `career_work` | `supported_candidate` | 可查询结项清理、边界维护、干燥保存、耐热容器、残余处理和阶段移交性质；仓储、档案、炉窑、能源、化工、冶炼、宗教等具体岗位另走领域模块。虚拟媒介须由离火／信息轴启动，戌只协作承载其实质、规则与存续。 |
| `wealth_resource` | `derived_candidate` | 财／资源轴成立时，可查询库存封存、维护成本、残余清理、释放条件和资源移交；戌为火库不等于财库、能源资产、房产或收益已取得。 |
| `family_relationship` | `derived_candidate` | 六亲身份锁定后，可查询谁在守边界、收尾遗留、保存共同资源或不愿释放；不能由戌指定伴侣、长辈、宗教人物、争产者或离合事件。 |
| `object_place` | `supported_candidate` | 可查询墙垣围护、炉窑灰烬、燃料／火种容器、干燥储存空间、狗及豺狼；寺庙须独立仪式锚点，按功能和位置选载体。 |

## 8. Bridge requirements

每次调用至少记录 Reader 中戌、戊辛丁 qi_rank、戌月司令和表源；本题使用的是季秋燥土、收尾封边、辛金余势、丁火种、火库、干燥／身体还是物件维度；对应藏气处于 field／qi／function／result 哪一层；若用火库，必须引用 Structure 的身份、开合／受损、释放范围、before／after 通量和下游；再比较围护、储存、炉窑、能源、宗教空间与动物等载体。不得调用“戌—虚”谐音补充虚拟、玄学、互联网或人格故事；若调用媒介协作路线，必须另有已经冻结的离火／信息／媒介轴，并把戌限定为载体、实质、规则、存续或归档。

## 9. Runtime unit map

| unit_id | unit_class | 对应内容 | allowed_topics | activation requirements | claim ceiling／forbidden promotions | source_layer |
|---|---|---|---|---|---|---|
| `XU-FIELD-LATEAUTUMN-EARTH` | `semantic_core` | 季秋、燥土、收尾、固结、封边、干燥保存与周期移交 | 全部相关 topic | Reader 确认戌节点；query 需要季节／场机制 | 只解释机制；不得重算旺衰、调候、墓库、死亡或吉凶 | `bazi_primary＋current_synthesis` |
| `XU-ACTION-CLOSE-CLEAR-PRESERVE` | `semantic_core` | 收束、清理、固结、封边、处理残余、保存火种与阶段移交 | behavior_personality／learning_cognition／career_work／wealth_resource／family_relationship／object_place | 领域体、材料、容器、边界和出口成立 | 不得直推虚伪、玄学、虚拟、仓储、化工、宗教职业或终止事件 | `bazi_course＋current_synthesis` |
| `XU-STATE-MANIFESTATION` | `state_modifier` | 四层显化及保存／焦裂／闷热／松散／积压／待时状态 | 全部相关 topic | 引用 branch_manifestation_handoff | 不得自行判开库、三气齐发、死亡、成果或事件 | `current_synthesis` |
| `XU-QI-WU-MAIN` | `state_modifier` | 戊本气的燥土、土石、主边界、固结、封存与承载接口 | 全部相关 topic | Reader 戊节点及 Structure gate／边／通量 | 本气不等于城墙、可靠、固执、房地产或能镇水 | `bazi_primary＋current_synthesis` |
| `XU-QI-XIN-MIDDLE` | `state_modifier` | 依 Reader 口径的辛中气：秋金余势、精整、残余器物与待时接口 | 全部相关 topic | Reader 辛节点及 Structure 可用度／去处 | 不因异表改称 residual，不得直推金被埋、刀具、档案或清理成果 | `bazi_primary＋current_synthesis` |
| `XU-QI-DING-RESIDUAL` | `state_modifier` | 依 Reader 口径的丁余气：火种、余温、灯火、热加工与待时接口 | 全部相关 topic | Reader 丁节点及 Structure 墓库／可用度／去处 | 不因异表改称 middle，不得直推火灭、文化、寺庙、能源或玄学 | `bazi_primary＋current_synthesis` |
| `XU-COMMANDER-XIN-DING-WU` | `state_modifier` | 戌月辛九、丁三、戊十八司令过渡 | 月令解释／timing | Reader month_command 有节气偏移与表源 | 不改写 static qi_rank，不按日数机械定命 | `bazi_commentary` |
| `XU-STORAGE-ROLE-FIRE` | `state_modifier` | 戌作火墓／库时的收藏、保护、闷存、待时、释放与改道机制 | career_work／wealth_resource／family_relationship／object_place | Structure 确认墓库身份、关系后状态、节点与释放范围 | 只到 mechanism；不得直推开库、火灭、能源、寺庙、文化、财库或事件 | `bazi_primary＋bazi_commentary＋current_synthesis` |
| `XU-OBJECT-DRY-ENCLOSURE-FIRESTORE` | `symbol_carrier` | 墙垣围护、干燥储存、炉窑、灰烬及燃料／火种容器 | object_place／career_work／wealth_resource | 场所／介质／耐热／封存功能及位置共振 | 最高 candidate；不得直推房产、仓储、化工、冶炼、军工、寺庙或能源职业 | `bazi_course＋current_synthesis` |
| `XU-MEDIA-CARRIER-GOVERNANCE` | `relational_carrier` | 已成立虚拟／媒介轴背后的载体、实质内容、规则边界、存续、归档与结项机制 | learning_cognition／career_work／object_place | 离火／信息／媒介轴已独立冻结，戌节点实际参与其承载、规则或保存路线 | 只到 mechanism／candidate；不得由戌或谐音启动虚拟、互联网、编辑、平台、玄学职业或界面显像 | `current_synthesis` |
| `XU-BODY-SKIN-DRY-HEAT` | `symbol_carrier` | 皮肤、体液边界、干燥、燥裂与热量闷存候选 | appearance_body | 身体专题、位置、干湿热状态与多锚点 | 不得诊断皮肤病、炎症、虚弱、脱水或固定体质 | `bazi_course＋current_synthesis` |
| `XU-ANIMAL-DOG-CANID` | `symbol_carrier` | 狗、豺、狼等犬科动物候选 | object_place／family_relationship | 明确动物／生肖题和场景锚点 | 不得类比出忠诚、凶狠、群居、贫困、犯罪或人物身份 | `bazi_course` |
| `XU-CROSS-QIMEN` | `cross_system_context` | 万物收尾／凋落、燥烈、水调燥及戊丁辛异序等线索 | 仅明确需要的相关 topic | 去除宫卦、奇门关系、旺衰、断验和“戌—虚”谐音后仍可回接共同符号 | source-only context；不得改写 Reader、结构、人格、虚拟／玄学职业或事件 | `cross_system_common_symbol` |

仓储、档案、能源、化工、石油、冶炼、军工、寺庙／宗教及任何死亡／疾病／房产事件均须另走领域载体或事件审计。虚拟、玄学、互联网、编辑部不作为戌卡的直接 runtime lead；只有上游媒介轴已成立时，才允许 `XU-MEDIA-CARRIER-GOVERNANCE` 解释其落地承载和规则存续。

## 10. Cannot decide

本卡不能单独决定戌是否旺、戊辛丁谁主事、异表层级、戌是否作为火墓／库及怎样开合释放、卯戌合／辰戌冲／丑未戌刑／酉戌害／火局与西方会是否成立，也不能决定虚拟、玄学、人格、职业、体貌、疾病、房产、能源、宗教、死亡与事件。

## 11. Source receipts

### S0｜共同底座
- 文件：`skill/bazi-source-lookup/references/deep-cards/five-elements-core.md`；`skill/bazi-source-lookup/references/deep-cards/earthly-branches-core.md`
- 支持：土爰稼穑；四层显化、逐藏气接口与墓库受控调用
- provenance：`current_synthesis`

### S1｜《千里命稿》原典
- 文件：`external-source://qianli-minggao-pdf`；`skill/bazi-structure-dynamics/references/qianli-minggao-fidelity-full.md`
- 核读：地支篇戌条、人元问答与力量分析
- 支持：戌属阳土、九月、寒露起月、藏戊辛丁；人元有层级
- 边界：合冲刑害、火局、开库与实际作用进入 Structure；静态顺序由 Reader 继承
- provenance：`bazi_primary`

### S2｜《子平真诠》原本与徐乐吾评注
- 文件：`skill/bazi-structure-dynamics/references/ziping-zhenquan-original-full.md`；`skill/bazi-structure-dynamics/references/ziping-zhenquan-commentary-full.md`
- 核读：论杂气、阳干逢库通根、反对机械冲库、戌月命例与司令表
- 支持：戌为火库，杂气须按透干会支与实际路线取用，不需见冲才发；司令辛九、丁三、戊十八
- 边界：墓库身份、开合、释放范围与格局由 Structure 裁决；日数未可执着
- provenance：`bazi_primary＋bazi_commentary`

### S3｜若境清课程
- 文件：`skill/bazi-structure-dynamics/references/ruojing-qianli-01-full.md`
- 可迁移：燥土、皮肤干燥检索、狗及犬科、火库、炉火／加工／香火类场所等候选
- 复合桥：化工、石油、冶炼、军工、寺庙须另有材料／职业／仪式锚点
- 不采用：“戌—虚”并非严格同音，从谐音推虚拟、玄学、虚伪、狡诈、互联网、编辑部证据不足；黑社会、强盗、乞丐等固定身份亦排除
- 架构转译：虚拟媒介若由离火／信息轴独立成立，戌仅可协作解释载体、实质、规则、存续与归档；这不是课程谐音说的延续
- provenance：`bazi_course`

### S4｜奇门共同符号材料
- 文件：`external-source://qimen-note-05-earthly-branches`
- 可迁移：季秋、生命周期收尾、燥烈、适量水分调节、火库及状态随条件改变
- 来源分歧：奇门表列戊丁辛，与 Reader 戊辛丁不同；只登记，不迁移为运行事实
- 不迁移：宫卦、奇门关系、旺衰、固定人格、死亡断验与具体事件
- provenance：`cross_system_common_symbol`

### S5｜当前架构归纳
- 内容：把戌整理为季秋燥土收尾与火种收藏场，分开戊辛丁静态层级、辛丁戊司令及 Structure 控制的火库身份；移除“戌—虚”直达弱桥，仅保留上游媒介轴成立后的载体／实质／规则协作
- provenance：`current_synthesis`

## 12. Forward-test questions

1. 模型能否区分戌场与戊天干，并把收尾理解为条件过程而非死亡／失败判词？
2. 能否继承 Reader 戊辛丁，同时把奇门戊丁辛异序留在来源层？
3. 能否区分静态藏干、辛丁戊司令、火库身份和岁运透干激活？
4. 面对冲合透干时，能否只重算实际节点与释放范围，不整体开库或断火灭？
5. 能否不从“戌—虚”推虚拟、玄学、虚伪、互联网或编辑职业，同时在离火／媒介轴已成立时只让戌解释载体、实质、规则和存续？
