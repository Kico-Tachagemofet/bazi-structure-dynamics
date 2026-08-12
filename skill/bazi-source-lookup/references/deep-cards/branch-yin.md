# DC-BRANCH-YIN｜寅木 Deep Card

- `version`: 0.3
- `status`: approved
- `review_state`: runtime_approved_by_human_2026-08-10
- `symbol_fact`: 地支寅；五行、月令、节气、藏干、司令及关系事实由 Reader 提供
- `role`: 孟春发动场、甲丙戊复合接口与现实载体候选；不负责重算月令、司令、旺衰、合冲刑害、会局或事件
- `structural_authority`: none
- `runtime_contract`: unit_permissions_v0.1
- `branch_manifestation_contract`: field-qi-function-result-v1
- `static_hidden_stems_authority`: Reader
- `static_hidden_stems`: [甲, 丙, 戊]
- `commander_authority`: Reader_month_command_with_source
- `commander_sequence`: [戊7, 丙7, 甲16]
- `commander_does_not_rewrite_hidden_stems`: true

## 1. Core seasonal field

寅是十二月令循环中的**孟春发动木场**。《千里命稿》列寅属阳木、东方、正月，立春起寅月、惊蛰前结束，静态藏甲、丙、戊。它首先表示冬后生机开始取得方向、根基与向外接口的季节场，不是把寅缩写成甲木或“大树”。

寅继承木的“曲直”：生发、伸展、疏通、建立方向，并在阻力与空间之间寻找生长路线。甲本气提供木的主线，丙中气提供温度、显露与后续火势接口，戊余气保留换季地基与承载条件。三者构成的是一个**从旧土承接、经温度启动、到木气主事**的复合春场；是否真的形成这条顺序，仍须逐节点读取司令、透藏、位置、关系后状态与下游承接。

寅的阳木与孟春发动允许“粗壮、向上、发展迅速、资源展开”等候选，但不能冻结成“寅必是大树、命主必高大、必有领导力”。同样，成长需要疏导或输出不等于“没有泄就一定朽木”；只有扩张持续、空间不足、没有修剪与去处时，才考虑拥塞、徒长或内部消耗。

## 2. Derivation path and fact boundary

```text
木曰曲直
→ 冬末条件转向立春后的生发、伸展与定向
→ 寅以甲为主线，内含丙的温度／显露接口与戊的承载余气
→ 旧基础—启动条件—春木发动逐层核对
→ 场在／气在／用起／果显分别桥接
```

### 静态藏干与司令时序必须分开

- `static_hidden_stems`：Reader 当前登记寅藏甲、丙、戊，分别为本气、中气、余气；每一气独立建节点。
- `commander_sequence`：徐乐吾评注所录寅月司令为戊七日、丙七日、甲十六日；具体值由 Reader 按立春后偏移和框架表源登记。
- 戊—丙—甲的司令时序不是静态 qi_rank 的倒排规则，也不表示三气按固定剧本依次产生现实事件。
- 甲、丙或戊之一透清／被触发，只重算该节点及受影响的边；不得把同支三气整体发动。

## 3. Seasonal and paired contrasts

| 对照 | 优先观察 | 本卡不允许的简化 |
|---|---|---|
| 丑 → 寅 | 丑收纳冬水并等待换季；寅使生机开始取得方向、温度与向外通道 | 立春一到所有木都自动有力 |
| 寅 → 卯 | 寅是孟春复合发动场；卯是仲春专气木场，生长更集中于木本身 | 寅只负责开始、卯只负责完成 |
| 寅与甲 | 寅是季节／空间／复合容器；甲是其本气接口 | 寅＝甲，可忽略丙戊和季节场 |
| 寅与申 | 都是复合转场支，内部接口与季节方向不同 | 未经 Structure 裁决便宣布寅申冲的迁移、伤损或成败 |

寅的“发动”描述季节倾向，不等于人物永远主动。路线被保留、受阻、改道、被占用或只有根气支持时，它也可以表现为准备、内部生长、替其他节点供给，或尚未形成外部成果。

## 4. Derivation routes and embedded-qi interfaces

### A. 孟春发动与建立方向路线｜优先

破冬、起步、向上伸展、建立主线、开辟空间与调动资源，是寅场的直接动作候选。环境题可由 `field_layer` 进入春季、林木、起始区、根基地或开发中的空间，不要求甲先透干。

### B. 甲本气接口｜春木主线

`YIN-QI-JIA-MAIN` 解释甲在寅中的根气、库存、环境供给、待时或已审计直接功能。甲为本气不等于必然领起全局；若位置、温度、空间、透出与去处不足，它也可能只作根基、内部主线或潜在发展条件。

### C. 丙中气接口｜温度与显露

`YIN-QI-BING-MIDDLE` 解释丙火在孟春场中的温度、照明、显露、表达或后续火路线接口。它可能帮助木获得生长环境，也可能在实际通量过大时泄木；必须回读完整边和承载，不能固定成“寅中有丙所以一定暖、一定出名”。

### D. 戊余气接口｜旧土与承载

`YIN-QI-WU-RESIDUAL` 解释冬春转换中保留的土体、地基、容器或资源承载。戊可以提供落点，也可能形成阻力或被木疏导；其作用由 Structure 裁决，不能从“余气”直接等同弱、无用或阻碍。

### E. 戊—丙—甲司令过渡｜仅限月令查询

`YIN-COMMANDER-WU-BING-JIA` 只解释寅月内部气序候选。出生时点或采用口径不明时，只登记 source context；评注所录日数本身“未可执着”。

### F. 体量、根基、发展与输出路线｜当前归纳

奇门笔记强调寅木实体、体量与快速发展，又提醒能量需要释放。本卡将其拆成条件模型：资源、空间、温度、修剪与输出合适时，生长可形成稳定主干与供给；只扩张而无边界、无去处或内部竞争严重时，才考虑徒长、拥塞、资源耗散或方向过多。

### G. 腿、头发、肝胆、虎猫与艮位联想｜分层候选

腿来自字形联想，头发与肝胆来自木类身体取象，虎／猫来自动物与生肖，艮的阻隔、厚土和“鬼门”属于跨体系方位联想。前四类可按身体、动物或物件题低权重调用；艮卦和鬼门只留 source-only，不进入八字结构或固定事件。

## 5. Manifestation and state switches

| layer | 寅卡可解释什么 | 未通过时仍保留什么 |
|---|---|---|
| `field_layer` | 孟春、东方木季、起步、伸展、开辟、根基与复合发动场 | `field-present`；环境／物件题可直接桥接 |
| `qi_layer` | 甲、丙、戊各自的库存、根气、温度／供给、承载或待时范围 | 逐气保留 stock／root-support／environmental-feed／timing-pending |
| `function_layer` | 获 direct-action gate 的具体藏气、实际边、通量、承接与竞争 | 一气发用不等于三气同步发动 |
| `result_layer` | 春木场或具体藏气是否接到人物、身体、工作、财富、关系或物件结果 | 未接通时只写场、机制或候选 |

- **空间、温度、根基与出口合适**：可起步、定向、伸展、建立主线并持续供给下游。
- **有生长但缺修剪／去处**：才考虑徒长、拥塞、资源摊薄或多线并进而难以集中；生长本身不是失衡。
- **温度不足或地基不承**：发动可能延迟、停在内部准备，或依赖后天条件；不等于寅木不存在。
- **丙火得到通道**：可增温、照明、表达或泄木；究竟帮助还是耗散由通量与本题端点决定。
- **戊土成为落点或阻力**：可承载、固定、提供现实接口，也可能被木疏导或占用；不预设吉凶。
- **关系后状态与 timing overlay**：只继承 Structure 的 retained／redirected／damaged 和重算结果，不自行判合冲刑害、火局或东方会局。

## 6. Candidate expressions

### 性质与动作

起步、定向、伸展、建立主线、开辟空间、调动资源、扎根并向外发展。以人为体且反复稳定时，可表现为愿意先建立方向、推动事物开始并扩充承载；空间与边界失配时才考虑急于铺开、线头过多、徒长或难以修剪。

### 形态、身体与环境

向上、粗直、根系、主干、起始坡地、林木与发展中空间可作候选。腿、头发、肝胆属于身体查询入口；具体体型、伤病和部位必须另有柱位、结构与身体专题。

### 学习、工作与资源

可查询建立框架、先定主线、启动项目、开发资源、培养早期能力、从地基到显露逐步推进等性质。管理、教育、林业、建筑、创业或项目负责人只是需要领域模块比较的载体，不是寅的直接结论。

### 物件、场所与动物

树林、木材、梁柱、根基地、开发区、起始节点、腿形／支撑物、虎猫等可作候选。鬼门、艮卦阻隔和具体灵异事件不进入可选八字 runtime 内容。

## 7. Topic axes

| axis | coverage | 领域候选与状态桥 |
|---|---|---|
| `behavior_personality` | `derived_candidate` | 人物锚点与稳定重复成立时，可查询起步、定向、开拓、建立主线和扩充承载；空间不足、无修剪或多线竞争时才考虑急于铺开、徒长和难以集中。不得固定成勇敢、领导型、固执或脾气大。 |
| `appearance_body` | `supported_candidate` | 可查询向上、粗直、根基、腿部支撑、头发、肝胆及木性伸展；外貌、损伤与疾病须身体专题和多锚点。 |
| `learning_cognition` | `derived_candidate` | 可查询先确定主线、搭框架、从基础向外扩展并把知识转成可发展的路径；分支过多时再考虑难以修剪。寅不直接决定聪明与成绩。 |
| `career_work` | `supported_candidate` | 可查询启动、开发、建设主线、资源供给、早期培育与扩张性质；具体管理、教育、林业、建设或创业岗位另走领域载体模块。 |
| `wealth_resource` | `derived_candidate` | 财／资源轴成立时，可查询种子资源、早期投入、基础建设、扩张成本与后续产出通道；寅本身不等于会创业、资产增长或花钱快。 |
| `family_relationship` | `derived_candidate` | 六亲身份锁定后，可查询谁在发起、建立方向、提供成长空间或承担早期建设；不能由寅中甲丙戊直接指定父母、子女、领导或伴侣。 |
| `object_place` | `supported_candidate` | 可查询树林、木材、梁柱、根基地、开发中空间、起始节点、支撑物、虎猫及春季东方环境；须以功能、位置与共振选载体。 |

## 8. Bridge requirements

每次调用至少记录 Reader 事实；`field_layer` 所用季节／动作；甲丙戊逐气的 `qi_layer`；声称直接作用时的 gate、边、通量与承接；现实领域与 `result_layer`；候选载体比较；若由岁运／合盘触发，注明命中节点、重算范围与 expiry。使用“发展／主线”时还须说明空间、温度、修剪与去处，不能只凭寅字。

## 9. Runtime unit map

| unit_id | unit_class | 对应内容 | allowed_topics | activation requirements | claim ceiling／forbidden promotions | source_layer |
|---|---|---|---|---|---|---|
| `YIN-FIELD-EARLYSPRING-WOOD` | `semantic_core` | 孟春、东方木季、起步、伸展、定向与复合发动场 | 全部相关 topic | Reader 确认寅节点；query 需要季节／场／起步机制 | 只解释机制；不得重算旺衰、调候、关系或吉凶 | `bazi_primary＋current_synthesis` |
| `YIN-ACTION-INITIATE-EXPAND` | `semantic_core` | 启动、开辟、建立主线、扎根、扩展与资源调动 | behavior_personality／learning_cognition／career_work／wealth_resource／family_relationship | 人物／领域体及持续路线成立，空间、边界与去处有收据 | 不得直推领导、教育、创业、管理或固定人格 | `bazi_course＋current_synthesis` |
| `YIN-STATE-MANIFESTATION` | `state_modifier` | 四层显化及发动／停滞／徒长／改道状态 | 全部相关 topic | 引用 branch_manifestation_handoff | 不得自行判关系、成局或结果兑现 | `current_synthesis` |
| `YIN-QI-JIA-MAIN` | `state_modifier` | 甲本气的根气、主线、供给、待时或直接功能 | 全部相关 topic | Reader 甲节点及 Structure gate／边／通量 | 本气不等于自动主事、领导或大树 | `bazi_primary＋current_synthesis` |
| `YIN-QI-BING-MIDDLE` | `state_modifier` | 丙中气的温度、显露、表达与后续火接口 | 全部相关 topic | Reader 丙节点及 Structure 的温度、去处和通量收据 | 不得直推温暖、出名、文化行业或成果 | `bazi_primary＋current_synthesis` |
| `YIN-QI-WU-RESIDUAL` | `state_modifier` | 戊余气的旧土、地基、承载与阻力接口 | 全部相关 topic | Reader 戊节点及 Structure 可用度／承接 | 余气不等于弱、无用或必然阻碍 | `bazi_primary＋current_synthesis` |
| `YIN-COMMANDER-WU-BING-JIA` | `state_modifier` | 寅月戊七、丙七、甲十六司令过渡 | 月令解释／timing | Reader month_command 有节气偏移与表源 | 不改写 static qi_rank，不按日数机械定命 | `bazi_commentary` |
| `YIN-SHAPE-ROOTED-UPWARD` | `symbol_carrier` | 向上、粗直、根系、主干、林木、梁柱与发展中空间 | appearance_body／object_place／career_work | 形态／场所锚点及竞争载体支持 | 最高 candidate；不得直断高大、大树、建筑或林业 | `bazi_course＋cross_system_common_symbol＋current_synthesis` |
| `YIN-BODY-LEG-HAIR-LIVER` | `symbol_carrier` | 腿部支撑、头发、肝胆与木性伸展功能 | appearance_body | 身体专题、位置与多锚点 | 不得诊断腿伤、脱发、肝胆疾病或体型 | `bazi_course` |
| `YIN-ANIMAL-TIGER-CAT` | `symbol_carrier` | 虎、猫及相关动物／生肖场景 | object_place／family_relationship | 明确动物／生肖题并有场景锚点 | 不得类比出凶猛、威权或猫科人格 | `bazi_course` |
| `YIN-CROSS-QIMEN` | `cross_system_context` | 艮位、厚土阻隔、鬼门、快速发展和需释放等跨体系线索 | 仅明确需要的相关 topic | 去除宫卦断验后仍可回接季节／形态者才保留 | source-only context；不得进入结构、灵异结论或固定断验 | `cross_system_common_symbol` |

具体领导、教师、创业者、林业、建筑、开发行业及灵异事件均须另走领域载体或相应专题，不由寅卡独立晋级。

## 10. Cannot decide

本卡不能单独决定寅是否旺、甲丙戊谁主事、司令值、寅亥合／寅申冲／寅巳刑害／火局是否成立，也不能决定领导力、职业、体型、肝胆疾病、迁移或事件。

## 11. Source receipts

### S0｜共同底座
- 文件：`skill/bazi-source-lookup/references/deep-cards/five-elements-core.md`；`skill/bazi-source-lookup/references/deep-cards/earthly-branches-core.md`
- 支持：木曰曲直；四层显化与逐藏气接口
- provenance：`current_synthesis`

### S1｜《千里命稿》原典
- 文件：`external-source://qianli-minggao-pdf`；`skill/bazi-structure-dynamics/references/qianli-minggao-fidelity-full.md`
- 核读：地支篇寅条、人元问答及人元力量分析
- 支持：寅属阳木、东方、正月、立春至惊蛰、藏甲丙戊；月支人元有层级
- 边界：合冲刑害会局进入 Structure；藏气不等量、亦不自动外显
- provenance：`bazi_primary`

### S2｜《子平真诠》原本与徐乐吾评注
- 文件：`skill/bazi-structure-dynamics/references/ziping-zhenquan-original-full.md`；`skill/bazi-structure-dynamics/references/ziping-zhenquan-commentary-full.md`
- 核读：原本论寅中甲为本主、丙戊接口及月令变化；评注人元司令表与透藏上下文
- 支持：寅的复合人元须按透出／会支与全局变化判断；司令为戊七、丙七、甲十六
- 边界：司令日数未可执着；原本格局变化规则不迁入象意卡裁决
- provenance：`bazi_primary＋bazi_commentary`

### S3｜若境清课程
- 文件：`skill/bazi-structure-dynamics/references/ruojing-qianli-01-full.md`
- 可迁移：腿、虎猫、头发、肝胆、木性与根基候选
- 降权／排除：艮、鬼门与三合中神说不进入八字取象裁决；身体与动物例子不升固定人格／事件
- provenance：`bazi_course`

### S4｜奇门共同符号材料
- 文件：`external-source://qimen-note-03-five-elements`；`external-source://qimen-note-05-earthly-branches`
- 可迁移：孟春生长、戊—丙—甲气序、实体根基、体量与发展／输出条件
- 不迁移：宫卦、奇门关系、旺衰、固定人格和断验
- provenance：`cross_system_common_symbol`

### S5｜当前架构归纳
- 内容：把寅整理为孟春发动复合场，建立甲丙戊逐气接口、冬春过渡与七轴 runtime units
- provenance：`current_synthesis`

## 12. Forward-test questions

1. 模型能否把寅作为复合春场，而不等同甲木、大树或领导？
2. 能否区分甲丙戊静态等级与戊丙甲司令时序？
3. 一气透出时能否只重算相关节点，不整体发动三气？
4. 能否正常使用腿、头发、肝胆、虎猫、树林等候选而不直断？
5. 能否把生长过量写成有条件的徒长／拥塞，而非“木旺必坏”？
