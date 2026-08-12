# DC-BRANCH-HAI｜亥水 Deep Card

- `version`: 0.3
- `status`: approved
- `review_state`: runtime_approved_by_human_2026-08-10
- `symbol_fact`: 地支亥；五行、月令、节气、藏干、司令及关系事实由 Reader 提供
- `role`: 孟冬入水场、壬甲复合接口与现实载体候选；不负责重算月令、司令、旺衰、合冲刑害、会局或事件
- `structural_authority`: none
- `runtime_contract`: unit_permissions_v0.1
- `branch_manifestation_contract`: field-qi-function-result-v1
- `static_hidden_stems_authority`: Reader
- `static_hidden_stems`: [壬, 甲]
- `commander_authority`: Reader_month_command_with_source
- `commander_sequence`: [戊7, 甲5, 壬18]
- `commander_does_not_rewrite_hidden_stems`: true

## 1. Core seasonal field

亥是十二月令循环中的**孟冬入水场**。《千里命稿》列亥属水、在命理作用分类中作阳、配北方、为十月，立冬起亥月、大雪前结束，静态藏壬、甲。它不是“壬水的另一个写法”，而是冬令开始时由季节、方位、温度、流路与内部人元共同构成的复合场。

亥继承水的“润下”：汇集、流通、渗入、趋向可行低处并滋养。相对子月的仲冬集中，亥更适合先观察为**冷气与水势进入、不同水路归集、开放连接以及水中保存下一阶段生长条件**。壬是 Reader 当前登记的本气接口，甲是中气接口；“水中有木”说明容器内保留生长的可能性，不等于甲已出地发动，也不等于见亥便形成水生木的现实成果。

亥的阴阳须分太极点。《千里命稿》的地支表把亥作阳，后文解释为“亥本属阴，因藏壬而体阴用阳，故作阳论”；八字课程和奇门笔记则直接称亥为阴水，更接近季节支体或阴寒环境的描述。本卡不把它们硬合成一个标签：**季节／支体可偏阴寒，藏气与实际作用分类可用阳水方式表达**，具体主动性与外显程度仍看结构。

## 2. Derivation path and fact boundary

```text
水曰润下
→ 立冬后的冷、水、低位、归集与流通条件进入
→ 亥居孟冬入口，水场开放而内含壬、甲两条接口
→ 水势怎样进入／汇合，与水中生机是否获得出口分别核对
→ 场在／气在／用起／果显逐层桥接
```

### 静态藏干与司令时序必须分开

- `static_hidden_stems`：Reader 当前登记亥藏壬、甲，分别为本气、中气；每一气都有独立节点和 runtime interface。
- `commander_sequence`：徐乐吾评注所录亥月司令为戊七日、甲五日、壬十八日；具体命盘采用何值，须由 Reader 按立冬后的实际偏移与表源登记。
- 戊在亥月前段司令，不等于亥的静态藏干中另有戊；司令时序也不把壬甲改排成戊甲壬。
- 壬或甲之一透清、成势或被岁运激活，只重算实际命中的节点、边与承接，不把另一气自动一并发动。

## 3. Seasonal and paired contrasts

| 对照 | 优先观察 | 本卡不允许的简化 |
|---|---|---|
| 戌 → 亥 | 戌仍带季秋收敛与燥土条件；亥打开孟冬水场，冷与流通开始成为主要环境 | 戌一过便所有水木自动有力 |
| 亥 → 子 | 亥是冬令入口、复合而较开放；子是仲冬中心、藏气更专、趋于集中 | 亥一定奔腾、子一定静止 |
| 亥 → 丑 | 亥让水势进入并归集；丑把冬水纳入寒湿土介质，收束并等待换季 | 亥只流通、丑只阻塞 |
| 亥与壬 | 亥是季节／空间／复合容器；壬是其中一条人元接口 | 亥＝壬，可忽略甲与季节场 |
| 亥与巳 | 都是体用阴阳层次复杂的四生／转场支 | 未经 Structure 裁决便宣布巳亥冲的破坏、迁移或吉凶 |

亥的“开放”不等于无边界，也不等于永远流动。水源、边界、温度、出口和下游承接合适时，它可以建立连续流路；未接入实际路线时，也可以只保留为季节背景、内部库存、根气或待时条件。

## 4. Derivation routes and embedded-qi interfaces

### A. 孟冬入水与归集路线｜优先

立冬、北方水季、冷气入口、开放水面、上游来水与不同流路归集，是亥的直接场景候选。问环境、迁移通道、作息、物件或工作介质时，`field_layer` 可以直接进入载体，不要求壬先透干。

### B. 开放连接、持续流动与广域容纳路线｜当前归纳

亥水可以对应江河湖海、泉流、液体网络或跨节点连接，但“大海”只是高匹配载体，不是固定尺度。边界、去处和控制通道清楚时，可表现为汇流、输送、交换和资源连接；通道过多、没有稳定落点或方向条件不足时，才可能出现无边界联想、频繁改道或缺乏方向感。

### C. 壬本气接口｜逐节点调用

`HAI-QI-REN-MAIN` 解释壬在亥中的库存、根气、环境供给、待时或已审计直接功能。即使壬为本气，也须同时看月令、司令、位置、透出、关系后状态、竞争占用与下游去处；不能由“亥水旺”替代实际通量判断。

### D. 甲中气接口｜水中生机

`HAI-QI-JIA-MIDDLE` 解释甲木在水场中的保存、根气、受生条件与未来发动接口。它可以成为“种子／核、潜在生长、下一阶段主线”的来源之一，但只有木节点获得可用度、温度、位置、承接与出口后，才能进入实际生长或输出；不得从亥中藏甲直推教育、领导、子女或植物事件。

### E. 戊—甲—壬司令过渡｜仅限月令查询

`HAI-COMMANDER-WU-JIA-REN` 只解释亥月内部气序候选。徐乐吾对司令日数明言“未可执着”，所以出生时点、节气边界或框架口径不明时，本单元只能登记 source context，不能替 Reader 选司令。

### F. 收敛外观与奔流功能的状态反差｜受控候选

奇门笔记用“其性好静、其势奔腾”描述亥。本卡只取其中可回接水场的状态反差：没有现实接口时，水可作为背景或内部库存；一旦获得通道、坡度、来源和去处，流量可能持续展开。它不是固定人格，更不意味着“参与必出成绩”。

### G. 江河湖海、水类场所、惊骇与寺院路线｜分层候选

江河湖海、溪泉、液体加工、盐、水浴与排水场所来自八字课程，可回接水体、流通、提炼或清洗功能；“惊骇”来自谐音，“寺院”来自课程以“佛法无量—大海”建立的文化联想，权重更低。后两者只有明确语言／宗教／场所问题及额外锚点时才可进入候选，不能反推人格、信仰或事件。

## 5. Manifestation and state switches

### 四层收据

| layer | 亥卡可解释什么 | 未通过时仍保留什么 |
|---|---|---|
| `field_layer` | 孟冬、北方水季、冷气入口、开放水面、归集、连接与复合容器 | `field-present`；环境／物件题可直接桥接 |
| `qi_layer` | 壬、甲各自的库存、根气、环境供给、受生条件、格局候选或待时状态 | 分别保留 stock／root-support／environmental-feed／timing-pending |
| `function_layer` | 获 direct-action gate 的具体藏气、实际边、通量、承接与竞争 | 一气发用不等于另一气同步发动 |
| `result_layer` | 水场／壬功能／甲功能是否接到本题人物、身体、工作、财富、关系或物件结果 | 未接通时，只写场、库存、机制或候选 |

### 状态切换

- **来源、边界、通道与去处合适**：可归集、连接、输送、交换，并持续为下游提供水源或信息资源。
- **水中甲木获得温度与承接**：潜在生长条件可以被转成主线、输出或具体培育过程；没有这些条件时只保留生机库存。
- **无稳定落点、边界不足或同时开启过多流路**：才考虑改道、分散、无边界联想或缺乏方向感；流动、迁移和多线连接本身并不构成失衡。
- **过寒、缺少温度或出口受阻**：可表现为冷滞、积水、内部蓄积或水木均难外展；不能直接写成情绪低落或疾病。
- **获得适当容器或调节节点**：开放流动可以转成可管理的供给、储备、运输、研究或滋养过程。
- **关系后 retained／concentrated／redirected／damaged**：只继承 Structure Core；本卡不自行判寅亥合、亥卯未局、巳亥冲、申亥害或亥亥自刑。
- **岁运／合盘触发**：只按 activation interface 重算实际命中的壬或甲、相关边、范围与 expiry，不把临时显性回写原局。

## 6. Candidate expressions

### 性质与动作

进入、归集、连接、流通、输送、交换、广域容纳，以及在水中保存下一阶段生长条件。以人为体且反复稳定时，可表现为能接入多来源信息、连接不同节点、容纳较大范围材料，并为后续生长留接口；条件失配时才考虑无边界联想、方向感不足、反复改道或内部蓄积。

### 形态、身体与环境

开放水面、连续水路、深广、寒湿、向低处汇流、入口与上游来水可作形态／环境候选。身体题可检索肾、泌尿、体液、血液循环和水液代谢；课程中的血液病、痰湿等只作为检索线索，不得由亥直接诊断。

### 学习、工作与资源

可查询多源材料汇集、跨节点连接、流动信息处理、资源输送、水／液体相关流程、保存潜在生长条件并等待启动等性质。航运、水务、饮品／发酵、盐业、洗浴、卫生排水、研究或网络连接均只是领域载体线索。

### 物件、场所与文化联想

江河湖海、溪泉、水池、液体容器、水路、港口、浴场、盐水／发酵场所、排水与卫生空间可作候选。“惊骇”“寺院”是低权重语言／文化联想，必须有本题明确入口和额外共振，默认不加载。

## 7. Topic axes

| axis | coverage | 领域候选与状态桥 |
|---|---|---|
| `behavior_personality` | `derived_candidate` | 以明确人物为体，且归集、连接、容纳多来源与为下一阶段留接口的动作反复稳定时，可表现为视野开放、能连接不同材料并维持流通；边界、落点或方向条件不足时才考虑无边界联想、反复改道与方向感不足。不得固定成安静、奔放、聪明、欲望强或容易受惊。 |
| `appearance_body` | `supported_candidate` | 可查询深广、连续、寒湿、向低处汇流的形态，以及肾、泌尿、体液、血液循环和水液代谢；肤色黑、血液病、痰湿等课程例子不得由单支直断。 |
| `learning_cognition` | `derived_candidate` | 可查询多源信息汇集、跨主题连接、保持开放接口、先广泛吸收再寻找流向的认知方式；缺落点时再考虑联想无边界或难以收束。亥不直接决定智力、学历与宗教悟性。 |
| `career_work` | `supported_candidate` | 可查询连接、输送、流动处理、液体／水路、跨节点网络、资源归集与潜在项目孵化等工作性质；具体水务、航运、酒盐、洗浴、研究或互联网岗位必须另由领域载体模块比较。 |
| `wealth_resource` | `derived_candidate` | 财／资源轴已成立时，可查询多来源汇入、流动性、跨节点调配、广域资源池与为后续生长保留资本；无边界、泄漏或积压须有结构状态支持。亥本身不等于大财、流动财或破财。 |
| `family_relationship` | `derived_candidate` | 六亲身份锁定后，可查询谁在连接不同成员、承接多方信息、提供资源流或保存尚未发动的生长接口；亥中甲不能直接指定子女、父母、领导或教育者。 |
| `object_place` | `supported_candidate` | 可查询江河湖海、溪泉、水池、水路、港口、液体容器、浴场、盐水／发酵场所及卫生排水空间；惊骇／寺院只在明确语言文化题中低权重调用。 |

## 8. Bridge requirements

每次把亥卡写入 finding，至少记录：

1. `fact_receipt`：Reader 中的亥支位置、月令身份、壬甲节点及 qi_rank、司令状态与表源；
2. `field_layer`：本题实际调用孟冬、冷气入口、开放水面、归集、连接还是复合容器；
3. `qi_layer`：壬、甲分别处于库存、根气、供给、受生、待时或其他状态中的哪一种；
4. `function_layer`：若声称壬或甲直接做功，逐气引用 gate、实际 edge、通量、承接与竞争；
5. `result_layer`：人物体、领域轴、现实载体与结果条件是否另行通过；
6. `growth_bridge`：若使用种子／生长象，说明甲节点、温度、位置、去处和现实生长载体怎样接通；
7. `carrier_comparison`：江海、溪泉、网络、液体流程、资源流、潜在生长或文化联想为何当前一个更匹配；
8. `timing_boundary`：后天触发命中壬还是甲，重算哪些边、持续到何时。

## 9. Runtime unit map

| unit_id | unit_class | 对应内容 | allowed_topics | activation requirements | claim ceiling／forbidden promotions | source_layer |
|---|---|---|---|---|---|---|
| `HAI-FIELD-EARLYWINTER-WATER` | `semantic_core` | 孟冬、北方水季、冷气入口、归集、开放连接与复合水场 | 全部相关 topic | Reader 确认亥节点；query 明确需要场、季节、通道或容器 | 只解释机制；不得重算月令、旺衰、调候、关系或吉凶 | `bazi_primary＋current_synthesis` |
| `HAI-POLARITY-BODY-USE` | `semantic_core` | 季节／支体偏阴寒，藏壬与命理作用分类呈“体阴用阳”的层次 | behavior_personality／learning_cognition／career_work／family_relationship | 查询确实涉及隐显、收束／流动或发动方式，且有相应人物／领域体 | 只说明太极层次；不得从阴阳标签推出性别、性格、主动被动或事件 | `bazi_primary＋bazi_course＋current_synthesis` |
| `HAI-STATE-MANIFESTATION` | `state_modifier` | 场在、逐气在、用起、果显及 retained／concentrated／redirected／damaged 的表达切换 | 全部相关 topic | 引用 branch_manifestation_handoff 与 post-relation state | 只继承状态；不得自行判合冲刑害、木局、水方或结果兑现 | `current_synthesis` |
| `HAI-QI-REN-MAIN` | `state_modifier` | 壬本气的库存、根气、环境供给、待时与已审计流通接口 | 全部相关 topic | Reader 的壬节点存在；Structure 给出 gate、边、通量与承接 | 只解释已裁功能；本气不等于自动强旺、得用、奔腾或外显 | `bazi_primary＋current_synthesis` |
| `HAI-QI-JIA-MIDDLE` | `state_modifier` | 甲中气作为生长库存、根气、受生条件与未来发动接口 | 全部相关 topic | Reader 的甲节点存在；Structure 给出温度、可用度、透出／触发、位置与承接 | 只解释已裁功能；不得直推领导、教育、子女、植物或现实成长成果 | `bazi_primary＋current_synthesis` |
| `HAI-COMMANDER-WU-JIA-REN` | `state_modifier` | 亥月戊七、甲五、壬十八的司令过渡 | 结构冻结后的月令解释／timing | Reader 的 month_command 有节气偏移、来源与采用口径 | 只解释已选司令；不得把戊补进静态藏干、改写 qi_rank 或机械按日数定命 | `bazi_commentary` |
| `HAI-ACTION-GATHER-CONNECT` | `semantic_core` | 多源归集、开放连接、持续流通、输送、交换与广域容纳 | behavior_personality／learning_cognition／career_work／wealth_resource／family_relationship | 相应人物／领域体、有效通道、边界、落点与持续路线成立 | 只说明过程；不得直推聪明、奔放、无边界人格、物流／网络／水务岗位 | `bazi_course＋cross_system_common_symbol＋current_synthesis` |
| `HAI-PROCESS-WATER-HOLDS-GROWTH` | `semantic_core` | 水场保存甲木生机，待温度、位置、出口与承接后进入下一阶段 | learning_cognition／career_work／wealth_resource／family_relationship／object_place | 甲节点相关且 growth_bridge 的温度、去处与现实载体均有收据 | 只到 mechanism；不得直推怀孕、子女、教育、领导、创业或项目成功 | `bazi_primary＋cross_system_common_symbol＋current_synthesis` |
| `HAI-SHAPE-OPEN-WATERWAY` | `symbol_carrier` | 江河湖海、溪泉、开放水面、入口、连续水路、港口与液体容器 | appearance_body／object_place／career_work／wealth_resource | 水体／通道功能、位置环境与竞争载体共同支持 | 最高 candidate；不得由一个亥字直断大海、港口、远行、航运、水务或住宅 | `bazi_course＋cross_system_common_symbol＋current_synthesis` |
| `HAI-BODY-WATER-CIRCULATION` | `symbol_carrier` | 肾、泌尿、体液、血液循环及水液代谢查询 | appearance_body | 身体专题、对应位置、关系后状态与多重锚点 | 最高 candidate；不得诊断肤色、血液病、痰湿、肾病或泌尿疾病 | `bazi_course＋current_synthesis` |
| `HAI-WORDPLAY-SHOCK-TEMPLE` | `symbol_carrier` | “亥／骇”惊骇谐音及“海量—佛法—寺院”文化联想 | object_place／family_relationship | 明确语言、宗教或场所问题，且有至少一项独立场景／柱位锚点 | 最高 candidate、默认不加载；不得直推胆小、事故、信佛、出家或寺院事件 | `bazi_course` |
| `HAI-CROSS-QIMEN` | `cross_system_context` | 种子／核、五湖归聚、冷气入口、静态背景与奔流功能反差等跨体系线索 | 仅明确需要的相关 topic | 去除宫星门神、关系技法和断验后，仍能回接季节、水形或壬甲容器 | source-only context；不得转发为 selected unit、进入八字结构或具体断验 | `cross_system_common_symbol` |

具体航运、水务、饮品／发酵、盐业、洗浴、卫生排水、研究、互联网、宗教身份、寺院事件和任何“项目孵化成功”，不设为亥卡可独立激活的复合载体。它们必须由领域载体模块结合十神功能、柱位、完整路线、现实接口、承载与竞争候选另行晋级。

## 10. Cannot decide

本卡不能单独决定亥是否旺、是否需火、壬甲谁实际主事、戊甲壬何者司令、寅亥是否合、亥卯未是否成局、巳亥冲或亥亥自刑结果、某人是否安静奔放、是否从事水务航运、是否信佛出家，或任何疾病与事件。上述判断分别返回 Reader、Structure Core、Topic Lens、领域载体与身体专题。

## 11. Source receipts

### S0｜五行与地支共同底座

- 文件：`skill/bazi-source-lookup/references/deep-cards/five-elements-core.md`；`skill/bazi-source-lookup/references/deep-cards/earthly-branches-core.md`
- 支持：水曰润下；地支作为季节场与复合容器；场在、气在、用起、果显四层显化
- provenance：`current_synthesis`（五行核心回溯《尚书·洪范》与本项目已核来源）

### S1｜《千里命稿》原典

- PDF：`external-source://qianli-minggao-pdf`
- 高保真整理：`skill/bazi-structure-dynamics/references/qianli-minggao-fidelity-full.md`
- 本轮核读：源 PDF 地支篇亥条、人元问答与阴阳体用段；整理版对应第 900—908、1544—1565、4469—4479 行
- 支持：亥属水、作用分类作阳、北方、十月、立冬至大雪、藏壬甲；同书解释亥本属阴而因藏壬“体阴用阳，故作阳论”
- 边界：合冲刑害、三合方合只进入 Structure；体用阴阳不能直接推出人格、主动性或外部成果
- provenance：`bazi_primary`

### S2｜《子平真诠》原本与徐乐吾评注

- 文件：`skill/bazi-structure-dynamics/references/ziping-zhenquan-original-full.md`；`ziping-zhenquan-commentary-full.md`
- 本轮核读：原本论阴阳生死、地支作用、人元与通根；评注人元司令表及“本静待用、透出显用”的完整上下文
- 支持：亥可提供壬甲人元与通根接口；亥月司令表为戊七、甲五、壬十八；藏气发用须结合透出、得令与全局
- 边界：司令日数“未可执着”；戊司令不改写静态藏干，透出亦不自动等于本盘得用或结果已显
- provenance：`bazi_primary＋bazi_commentary`

### S3｜若境清八字课程

- 文件：`skill/bazi-structure-dynamics/references/ruojing-qianli-01-full.md`；`ruojing-qianli-02-full.md`
- 本轮核读：地支段亥条及藏干／根气示例完整上下文
- 可迁移：课程称亥为阴水；江河湖海、溪泉、水类场所、肾泌尿、液体与提炼／清洗场景，以及惊骇、寺院的低权重联想
- 降权／排除：肤色黑不作固定外貌；血液病、痰湿不作诊断；酒厂、盐场、澡堂、寺院等不作固定职业／信仰；关系结论由 Structure 裁决
- provenance：`bazi_course`

### S4｜奇门共同符号材料

- 文件：`external-source://qimen-note-03-five-elements`；`external-source://qimen-note-05-earthly-branches`
- 可迁移：润下、孟冬、种子／核、五湖归聚、冷气入口、阴水环境、壬甲容器与静态背景／奔流功能的状态反差
- 不迁移：“参与必出成绩”、固定欲望／自刑人格、宫星门神、六合无合化、三合三会、击刑和奇门断验
- provenance：`cross_system_common_symbol`

### S5｜当前架构归纳

- 内容：把亥整理为孟冬入水、归集连接与水中保存生机的复合场；分开支体／作用阴阳、壬甲静态接口与戊甲壬司令；建立冬令三支对照、四层显化、七轴与 runtime units
- provenance：`current_synthesis`

## 12. Forward-test questions

1. 模型能否把亥作为孟冬复合水场处理，而不把它缩写成壬水、大海或固定奔流？
2. 模型能否保留“支体／季节偏阴”和“藏壬、作用分类作阳”的不同太极点，而不强行选一个标签？
3. 模型能否区分亥藏壬甲与亥月戊甲壬司令，不把戊补进静态藏干？
4. 壬或甲被透清／触发时，模型能否只重算实际命中的节点与边，不把两气整体发动？
5. 模型能否把“水中有生机”保留为待温度、位置和出口的机制，不直推教育、领导、子女或项目成功？
6. 模型能否正常使用江河湖海、水类场所、惊骇和寺院等候选，同时维持正确权重与领域桥接？
