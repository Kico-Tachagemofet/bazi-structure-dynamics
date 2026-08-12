# DC-BRANCH-SHEN｜申金 Deep Card

- `version`: 0.3
- `status`: approved
- `review_state`: runtime_approved_by_human_2026-08-10
- `symbol_fact`: 地支申；五行、月令、节气、藏干、司令及关系事实由 Reader 提供
- `role`: 孟秋复合金场、庚壬戊接口与现实载体候选；不负责重算月令、司令、旺衰、合冲刑害、会局、透干激活或事件
- `structural_authority`: none
- `runtime_contract`: unit_permissions_v0.1
- `branch_manifestation_contract`: field-qi-function-result-v1
- `static_hidden_stems_authority`: Reader
- `static_hidden_stems`: [庚, 壬, 戊]
- `commander_authority`: Reader_month_command_with_source
- `commander_sequence`: [戊己10, 壬3, 庚17]
- `commander_does_not_rewrite_hidden_stems`: true

## 1. Core seasonal field

申是十二月令循环中的**孟秋复合金场**。《千里命稿》列申属阳金、西方、七月，立秋起申月、白露前结束；Reader 静态登记庚、壬、戊。它承接未月成熟整理后的材料，使事物进入收敛、定形、筛选、改制和输出新通道的阶段，但仍是秋季发动端，不等于酉月的专气金场。

申继承金的“从革”：材料能够随加工而改变形态，并通过精炼、裁切、取舍而成器。这里至少要分开：**什么正在被收束／加工、边界怎样建立、哪些部分被筛除、成形后是否获得通道，以及裁切究竟是有用改制还是过度破坏**。课程与奇门所说的肃杀、破坏力，只能在目标、力度和结果均成立时作为状态；不能把申固定成急躁、严肃、凶猛或必有伤灾。

庚提供主要金性接口，壬提供冷却、流通、传递和向冬水过渡的接口，戊提供上游土体、矿料、平台、边界与承载接口。申因此可以成为“材料—加工—流通”的复合场，但三气是否形成这条路线，要逐一检查关系后状态；不能因申中有庚壬戊便预设土生金、金生水已经顺畅完成。

## 2. Derivation path and fact boundary

```text
金曰从革
→ 孟秋开始收束、筛选、改形并建立可执行边界
× 庚金主加工／裁断＋壬水流通／冷却＋戊土材料／平台
→ 戊己—壬—庚司令时序另作月令查询
→ 场在／气在／用起／果显分别桥接
```

### 静态藏干、来源异序、司令与长生说明必须分开

- `static_hidden_stems`：Reader 当前登记申藏庚、壬、戊，依次为本气、中气、余气。
- 《千里命稿》高保真整理的申条写“藏干戊庚壬”，与 Reader 的层级次序不同；奇门表写庚、壬、戊，与 Reader 一致。异表只保留为来源分歧，本卡不私自重排。
- `commander_sequence`：徐乐吾评注所录申月司令为立秋后戊己土十日、壬水三日、庚金十七日；实际值由 Reader 按节气偏移和采用表源登记。戊己并称也不等于申静态同时藏戊己。
- 奇门称“壬水长生于申”可作为季节过渡与壬接口的来源说明；长生、通根、实际可用性由 Reader／Structure 裁决，Deep Card 不执行。
- 庚、壬或戊透出、流年引动，只会让 Structure 重算相应节点的可见性、作用边、通量和去处，不令整支三气同步外显。

## 3. Seasonal and paired contrasts

| 对照 | 优先观察 | 本卡不允许的简化 |
|---|---|---|
| 未 → 申 | 未重余热入土后的熟化收藏；申开始把成熟材料收束、改形并建立秋季边界 | 立秋一到火木全灭、金必能裁断 |
| 申 → 酉 | 申是庚壬戊复合发动场；酉是辛金专气、完成度与精细定形中心 | 申酉都是金所以只分大刀／小刀 |
| 申与庚 | 申是季节／空间／复合容器；庚是主要金性接口 | 申＝庚，可套用全部庚金人格职业 |
| 申与壬 | 壬可提供流通、冷却和水势起点；是否发用看节点与路线 | 见申便水源充足、运输顺畅或申子辰成局 |
| 申与寅 | 孟秋收束改形与孟春伸展发动方向相对 | 未经 Structure 便宣布寅申冲的迁移、手术、事故或离合 |

申的复合性说明场内同时有加工、承载和流通接口，不是性格复杂。材料能否成器，取决于热度、硬度、加工精度、平台和出口；金性过盛或对象错配时才考虑过切、刚折、损伤与淘汰过快。

## 4. Derivation routes and embedded-qi interfaces

### A. 孟秋收束、改形与开路路线｜优先

筛选、裁断、清障、改制、建立边界、让成熟材料进入器用或运输通道，是申场的直接机制候选。物件／场所题可以从 `field_layer` 进入金属、机械、道路、关口和加工空间，不要求庚先透干；人物身份和事件结果仍须另过桥。

### B. 庚本气接口｜裁断、执行与结构改制

`SHEN-QI-GENG-MAIN` 解释庚在申中的根气、环境供给、硬质材料、裁切、执行或待时状态。庚为本气不等于一定锋利、能克木、军警司法或手术成功；对象、权限、力度和下游用途必须由冻结结构提供。

### C. 壬中气接口｜冷却、流通与传递

`SHEN-QI-REN-MIDDLE` 解释壬的水源、冷却液、信息／物资流、道路传递、库存或待时接口。壬在申得长生的说法不能替代实际通根与可用性审计；道路、传送、物流和水务是现实载体候选，不是申的固定行业。

### D. 戊余气接口｜矿料、平台与边界承载

`SHEN-QI-WU-RESIDUAL` 解释戊的土石材料、矿料来源、平台、关口、边界或待时承载。戊是否生金、埋金、挡水或提供收费／检查空间，须看土金水的实际位置、体量和通道；不能由申字形直接定收费站、保安或关口。

### E. 戊己—壬—庚司令过渡｜仅限月令查询

`SHEN-COMMANDER-EARTH-REN-GENG` 只解释申月内部气序候选。戊己土十日是评注表的合并写法，日数“未可执着”；司令不增删静态藏干，也不重排 Reader 的庚—壬—戊。

### F. 刀剑、机械、道路与关口路线｜受控载体

刀剑铁器、机械、手术刀、道路、传送、关卡、收费／检查空间可回接裁切、开路、流通和边界检查。司法、军警、医生、保安、交通等身份必须另有权责／医疗／职业轴、资格、位置和持续接口；不能因载体相似直接选人。

### G. 肺牙、猴与猛兽路线｜分层候选

肺、牙齿、骨架及收敛／切割功能来自金类与课程身体象，只作身体检索入口。猴为生肖载体；虎、狮等猛兽是课程由“能伤人”所作低权重联想。动物题可正常使用候选，但不得把凶猛、机灵、好动或攻击性回填成人格。

## 5. Manifestation and state switches

| layer | 申卡可解释什么 | 未通过时仍保留什么 |
|---|---|---|
| `field_layer` | 孟秋、收束、定形、加工、开路、关口与金水过渡环境 | `field-present`；环境／物件题可直接桥接 |
| `qi_layer` | 庚壬戊各自的根气、库存、材料、供给或待时状态 | 未透仍保留 stock／root-support／environmental-feed／timing-pending |
| `function_layer` | 获 direct-action gate 的具体藏气、真实作用边、加工／流通通量与承接 | 一气起用不等于三气同步发动或关系已顺生 |
| `result_layer` | 裁切、改制、传递、成器、损伤是否进入现实人物、身体、工作与物件 | 未接通时只写场、库存、机制或候选 |

- **材料、加工力度、平台和出口匹配**：可完成筛选、改形、成器、开路与传递。
- **金性过强、对象脆弱或裁切无度**：才考虑过切、刚折、损伤、淘汰过快或关系边界过硬；肃杀不是固定凶象。
- **壬水形成有效出口**：可冷却、清洗、传送并让加工结果流动；水无界、无承接时也可能使成形松散或结果流失。
- **戊土合适承载**：可供矿料、平台和边界；土过厚、位置不当时才考虑埋压或通道阻塞。
- **timing／synastry 激活**：只重算被引动藏气的可见性、作用边、范围与 expiry，不回写原局或整体启动申中三气。

## 6. Candidate expressions

### 性质与动作

收束、筛选、裁断、改制、清障、建立边界、开路、传递和把成熟材料转成器用。人物锚点稳定成立时，可查询善于做取舍、执行标准、处理硬问题或打通路径；对象和力度失配时才查询过切、急于淘汰、刚硬对抗，不得固定成急躁、严肃、凶狠或军人性格。

### 形态、身体与环境

硬直、棱角、骨架、金属感、机械结构、道路节点和关口形态可作候选。肺、牙齿、骨骼与切割／收敛功能只作身体检索入口，不从申支直接诊断疾病或手术。

### 学习、工作与资源

可查询拆解筛选、执行标准、把材料改制成器、建立流程关口、冷却清洗和传递输出等性质。司法、军警、医疗、机械、交通、物流和安保必须另走领域载体比较。

### 物件、场所与动物

刀剑铁器、机械、手术刀、道路、关口、收费／检查空间、猴及大型猛兽可作候选；按材料、功能、尺度、位置和题目共振选载体。

## 7. Topic axes

| axis | coverage | 领域候选与状态桥 |
|---|---|---|
| `behavior_personality` | `derived_candidate` | 稳定人物锚点下，可查询筛选取舍、执行边界、处理硬问题与打通路径；力度或对象失配时才考虑过切、急于淘汰和刚硬对抗。不得固定成急躁、严肃、凶狠、军警型或机灵好动。 |
| `appearance_body` | `derived_candidate` | 可查询骨架、棱角、硬直、金属／机械感，以及肺、牙齿、骨骼与收敛功能；具体体貌、疾病和手术须身体专题。 |
| `learning_cognition` | `derived_candidate` | 可查询拆解问题、筛除干扰、建立标准、形成流程关口并把结果输出；申不直接决定理工、法律、医学能力或判断力。 |
| `career_work` | `supported_candidate` | 可查询裁断执行、机械加工、道路传送、关口检查、风险处置和冷却流通等工作性质；司法、军警、医生、交通、物流、安保等具体岗位另走领域模块。 |
| `wealth_resource` | `derived_candidate` | 财／资源轴成立时，可查询材料改制、设备、通道、清理配置、运输成本和成器价值；申不等于金融、矿产、收费获利或破财。 |
| `family_relationship` | `derived_candidate` | 六亲身份锁定后，可查询谁在设边界、做取舍、开路、传递或承担检查；不能由申指定父亲、丈夫、军人、医生或冲突离合事件。 |
| `object_place` | `supported_candidate` | 可查询刀剑铁器、机械、道路、关口、收费／检查空间、猴和猛兽；按功能、尺度与场景选载体。 |

## 8. Bridge requirements

每次调用至少记录 Reader 中申、庚壬戊 qi_rank、申月司令和表源；本题使用的是孟秋金场、裁切改制、流通冷却、土石平台、关口还是动物／身体维度；对应藏气处于 field／qi／function／result 哪一层；direct-action gate、对象、力度、通量、承接和出口；再比较工具、机械、道路、司法／医疗空间、动物等载体。使用长生说时必须引用 Reader／Structure 结论，不由卡片自行裁根。

## 9. Runtime unit map

| unit_id | unit_class | 对应内容 | allowed_topics | activation requirements | claim ceiling／forbidden promotions | source_layer |
|---|---|---|---|---|---|---|
| `SHEN-FIELD-EARLYAUTUMN-METAL` | `semantic_core` | 孟秋、收束发动、改形、定界、开路及金水过渡复合场 | 全部相关 topic | Reader 确认申节点；query 需要季节／场机制 | 只解释机制；不得重算旺衰、调候、关系、长生或吉凶 | `bazi_primary＋current_synthesis` |
| `SHEN-ACTION-CULL-REFORM-CHANNEL` | `semantic_core` | 筛选、裁断、改制、清障、建立边界、开路与输出 | behavior_personality／learning_cognition／career_work／wealth_resource／family_relationship／object_place | 领域体、对象、权限／工具和出口成立 | 不得直推急躁、肃杀、司法、军警、医生、机械、交通或事故 | `bazi_course＋current_synthesis` |
| `SHEN-STATE-MANIFESTATION` | `state_modifier` | 四层显化及成器／过切／刚折／受埋／流失／待时状态 | 全部相关 topic | 引用 branch_manifestation_handoff | 不得自行判旺衰、三气顺生、长生得用或现实结果 | `current_synthesis` |
| `SHEN-QI-GENG-MAIN` | `state_modifier` | 庚本气的硬质材料、裁断、执行、改制与根气接口 | 全部相关 topic | Reader 庚节点及 Structure gate／边／通量 | 本气不等于刀剑、克木成功、军警司法或自动得用 | `bazi_primary＋current_synthesis` |
| `SHEN-QI-REN-MIDDLE` | `state_modifier` | 壬中气的水源、冷却、清洗、传递、流通与待时接口 | 全部相关 topic | Reader 壬节点及 Structure 长生／可用度／去处 | 不得因“壬长生申”直推有根有用、水局、物流或成绩 | `bazi_primary＋current_synthesis` |
| `SHEN-QI-WU-RESIDUAL` | `state_modifier` | 戊余气的土石／矿料、平台、边界、关口与承载接口 | 全部相关 topic | Reader 戊节点及 Structure 可用度／体量／去处 | 不因异表改称 main，不得直推生金、埋金、收费站或土地 | `bazi_primary＋current_synthesis` |
| `SHEN-COMMANDER-EARTH-REN-GENG` | `state_modifier` | 申月戊己土十、壬三、庚十七司令过渡 | 月令解释／timing | Reader month_command 有节气偏移、戊己口径与表源 | 不把己补进静态藏干，不改 qi_rank，不按日数机械定命 | `bazi_commentary` |
| `SHEN-OBJECT-BLADE-ROAD-GATE` | `symbol_carrier` | 刀剑铁器、机械、手术刀、道路、关口与收费／检查空间 | object_place／career_work／wealth_resource | 工具／通道／边界功能、尺度和位置共振 | 最高 candidate；不得直推手术、司法、军警、交通、安保职业或事故 | `bazi_course＋current_synthesis` |
| `SHEN-BODY-LUNG-TEETH-BONE` | `symbol_carrier` | 肺、牙齿、骨骼与收敛／切割功能候选 | appearance_body | 身体专题、位置与多锚点 | 不得诊断肺病、牙病、骨伤或预定手术 | `bazi_course` |
| `SHEN-ANIMAL-MONKEY-PREDATOR` | `symbol_carrier` | 猴及虎、狮等大型猛兽候选 | object_place／family_relationship | 明确动物／生肖题和场景锚点 | 不得类比出机灵、好动、凶猛、攻击性或人物身份 | `bazi_course＋current_synthesis` |
| `SHEN-CROSS-QIMEN` | `cross_system_context` | 壬水长生、水神、坤宫、顽钝耐磨、肃杀破坏等跨体系线索 | 仅明确需要的相关 topic | 去除宫卦、奇门关系、旺衰和断验后仍可回接共同符号 | source-only context；不得改写 Reader、结构、人格、职业或事件 | `cross_system_common_symbol` |

司法、军警、医生、手术、机械、交通、物流、安保、收费及任何事故／迁移事件均须另走领域载体或事件审计，不由申卡独立晋级。

## 10. Cannot decide

本卡不能单独决定申是否旺、庚壬戊谁主事、异表层级、戊己司令具体取值、壬水是否真正得长生之用、巳申合／寅申冲／寅巳申刑／申亥害／水局与西方会是否成立，也不能决定人格、职业、体貌、疾病、手术、迁移与事件。

## 11. Source receipts

### S0｜共同底座
- 文件：`skill/bazi-source-lookup/references/deep-cards/five-elements-core.md`；`skill/bazi-source-lookup/references/deep-cards/earthly-branches-core.md`
- 支持：金曰从革；四层显化、逐藏气接口与受控载体
- provenance：`current_synthesis`

### S1｜《千里命稿》原典
- 文件：`external-source://qianli-minggao-pdf`；`skill/bazi-structure-dynamics/references/qianli-minggao-fidelity-full.md`
- 核读：地支篇申条、人元问答与力量分析
- 支持：申属阳金、西方、七月、立秋起月、藏戊庚壬；人元有层级
- 来源分歧：整理表顺序戊庚壬，Reader 采用庚壬戊；本卡只登记，不改运行事实
- provenance：`bazi_primary`

### S2｜《子平真诠》原本与徐乐吾评注
- 文件：`skill/bazi-structure-dynamics/references/ziping-zhenquan-original-full.md`；`skill/bazi-structure-dynamics/references/ziping-zhenquan-commentary-full.md`
- 核读：申月用神变化、支中人元静待透用、通根与司令表
- 支持：申中复合人元须按透干、会支、配合与路线取用；司令为戊己十、壬三、庚十七
- 边界：司令日数未可执着；长生、格局变化、三合与实际路线不由 Deep Card 执行
- provenance：`bazi_primary＋bazi_commentary`

### S3｜若境清课程
- 文件：`skill/bazi-structure-dynamics/references/ruojing-qianli-01-full.md`
- 可迁移：刀剑铁器、道路传送、肺牙、手术刀、关口收费空间及猛兽等候选
- 降权／排除：急躁严肃不作固定人格；司法、军警、医生、保安等须领域桥，课程关系口诀不迁入裁决
- provenance：`bazi_course`

### S4｜奇门共同符号材料
- 文件：`external-source://qimen-note-05-earthly-branches`
- 可迁移：孟秋、万物成形、金水过渡、庚壬戊接口及材料耐磨／肃杀状态候选
- 边界：壬水长生、水神、坤宫、破坏力只作来源上下文；不迁移宫卦、旺衰、关系与断验
- provenance：`cross_system_common_symbol`

### S5｜当前架构归纳
- 内容：把申整理为材料—加工—流通的孟秋复合金场，分开庚壬戊静态层级、戊己壬庚司令和长生说明
- provenance：`current_synthesis`

## 12. Forward-test questions

1. 模型能否区分申场与庚天干，并保留壬、戊接口而不预设顺生完成？
2. 能否继承 Reader 庚壬戊，同时把《千里命稿》戊庚壬异序留在来源层？
3. 能否区分静态藏干、戊己壬庚司令和壬水长生，不把己补进藏干？
4. 面对刀具、道路、关口时，能否按功能和题轴选载体而不直推军警、医生或事故？
5. 岁运透出壬、庚或戊时，能否只重算对应接口而不整体启动申中三气？
