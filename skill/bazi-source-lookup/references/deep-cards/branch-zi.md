# DC-BRANCH-ZI｜子水 Deep Card

- `version`: 0.3
- `status`: approved
- `review_state`: runtime_approved_by_human_2026-08-10
- `symbol_fact`: 地支子；五行、月令、节气、藏干、司令及关系事实由 Reader 提供
- `role`: 仲冬水场、单一藏气接口与现实载体候选；不负责重算月令、司令、旺衰、合冲刑害或事件
- `structural_authority`: none
- `runtime_contract`: unit_permissions_v0.1
- `branch_manifestation_contract`: field-qi-function-result-v1
- `static_hidden_stems_authority`: Reader
- `static_hidden_stems`: [癸]
- `commander_authority`: Reader_month_command_with_source
- `commander_sequence`: [壬10, 癸20]
- `commander_does_not_rewrite_hidden_stems`: true

## 1. Core seasonal field

子是十二月令循环中的**仲冬水场**。在《千里命稿》的事实表中，子属水、配北方、为十一月，大雪起子月，小寒前结束；它处在亥—子—丑冬令组的中心位置。这里首先描述的是一个时间、方位、温度、流动与容纳条件构成的场，不是把子缩写成一枚癸水天干。

子继承水的“润下”：水向可行的低处汇集、渗入、流通并滋养。仲冬使这一过程更偏向**集中、潜藏、低位运行、内部蓄积与等待转机**。冬至落在子月，又提供“一阳来复”的季节转折入口：外部仍寒，内部的新一轮生机可以开始萌动。它不是“见子便朝气蓬勃”的人格断语，只有相关生长路线、承接与人物锚点成立时，才可解释为在收束环境中酝酿新的发动。

“子作阴”与“冬至一阳生”并不矛盾。《千里命稿》在命理分类中把子列作阴支，又用“子午本属阳，因子中藏癸，体阳而用阴”解释其体用层次。本卡保留这两个太极点：**支体／季节转机**与**藏气／实际发用方式**不能被一个“阴”或“阳”字抹平。

## 2. Derivation path and fact boundary

```text
水曰润下
→ 北方冬令的寒、藏、低位与汇集条件
→ 子居仲冬中心，水场较纯、外收而内聚
→ 场在／气在／用起／果显分别核对
→ 再按 Topic Lens 选择人物、身体、工作、关系或物件载体
```

### 静态藏干与司令时序必须分开

- `static_hidden_stems`：Reader 当前登记子藏癸一气，且癸为本气；这是单支内部接口事实。
- `commander_sequence`：徐乐吾评注所录司令表为大雪后壬十日、癸二十日；具体命盘采用何值，须由 Reader 按节气偏移与来源写入 `month_command`。
- 壬在子月前段司令，不等于“子又静态藏壬”，也不能由 Deep Card 把 Reader 的子藏癸改成壬癸二气。
- 子只藏一气，说明内部接口相对集中；不等于癸必然直接做功、必然清纯、必然力量大，也不等于所有现实表现只有一种。

## 3. Seasonal and paired contrasts

| 对照 | 优先观察 | 本卡不允许的简化 |
|---|---|---|
| 亥 → 子 | 亥是孟冬入口与复合水场；子是仲冬中心，水气更集中、接口更纯 | 亥一定动、子一定静 |
| 子 → 丑 | 子以集中水场为主；丑转入寒湿土容器，开始混合、收纳与换季 | 子只有流动、丑只有阻塞 |
| 子与癸 | 子是季节／空间／容器场；癸是子中实际登记的人元接口 | 子＝癸，二者可互换 |
| 子与午 | 二者都是二至转换的中心场，方向与温度相反 | 未经 Structure 裁决就宣布子午冲的结果 |

子“纯”指静态藏干接口单一，不是价值判断。关系后被聚拢、改道、受损、受制或获得出口时，同一子场仍可表现为集中供给、内部循环、低位通道、寒湿积存或待时资源。

## 4. Derivation routes and embedded-qi interfaces

### A. 仲冬水场路线｜优先

季节、夜半、北方、寒水、低位与汇集，是子的直接场景候选。问环境、作息、工作场景或物件时，`field_layer` 可以直接接入领域载体，不要求癸先透干。

### B. 集中、潜藏与内部酝酿路线｜当前归纳

仲冬并非“完全停止”，而是外部收束、资源向内部集中。若后续有木的承接、火的温度或现实出口，可解释为积累后萌发；若长期无出口、过寒或边界失配，才可能表现为内部循环、寒湿积聚或方向尚未形成。

### C. 癸本气接口｜逐节点调用

`ZI-QI-GUI-MAIN` 只在 Reader 已登记相应隐藏节点，并由 Structure handoff 给出其关系后状态时调用。它可能只作库存、根气、环境供给或待时接口，也可能在透清、得令、同气成势、位置接近与下游承接共同支持时获得 direct-action gate。是否发用不能由“本气”一词单独决定。

### D. 壬癸司令过渡｜仅限月令查询

`ZI-COMMANDER-REN-GUI` 只解释子月内部气序，不改写藏干表。出生时点不明或 Reader 将司令标作 disputed／pending 时，本单元只能作为来源上下文，不能替命盘选择壬或癸。

### E. 夜半、鼠与“子”字路线｜低权重载体

半夜与鼠来自课程中的时辰／生肖取象，可作为作息、动物、形态或场景候选；“孩子”来自字义联想，只能在明确的子女／六亲问题中，与十神、宫位、柱位和实际路线共同桥接。它们都不能反推固定性格、职业或家庭事件。

## 5. Manifestation and state switches

### 四层收据

| layer | 子卡可解释什么 | 未通过时仍保留什么 |
|---|---|---|
| `field_layer` | 仲冬、北方、夜半、寒水、低位、集中、潜藏及环境容器 | `field-present`；环境题可直接桥接 |
| `qi_layer` | 子中癸的库存、根气、环境供给、格局候选或待时范围 | stock／root-support／environmental-feed／timing-pending |
| `function_layer` | 癸节点已获准参与的实际边、通量、承接与竞争 | direct gate 未通过时，不删除其场与库存 |
| `result_layer` | 已成立场／功能是否接到本题人物、身体、工作、关系或物件结果 | 未接到现实结果时，只写机制或候选 |

### 状态切换

- **得时、来源稳定且边界合适**：可集中、供给、蓄积、维持内部循环，或为下一阶段提供水源。
- **有出口与承接**：水场可向生长、表达、运输、滋养或资源周转转化；具体去处由完整路线决定。
- **过寒、缺少温度或长期无出口**：才考虑凝滞、寒湿积存、内部反复或发动延迟；不能把“仲冬”直接写成消沉人格。
- **边界不足或流路过多**：可能分散、改道或难以集中；流动本身不等于失衡。
- **关系后 retained／concentrated／redirected／damaged**：只继承 Structure Core 的裁决；本卡不自行判合化、冲散、刑害或水局成立。
- **岁运／合盘触发**：只读 activation interface 重算后的范围和期限，不把临时透清回写成原局常态。

## 6. Candidate expressions

### 性质与动作

汇集、下行、低位流通、内部蓄积、潜藏、等待转机和在收束环境中酝酿。以人为体且长期稳定时，可表现为善于在低调位置收集信息、保存资源、感受细微变化或等待合适时机；无方向与出口时，才可能形成内部循环、方向感不足或无边界联想。

### 形态、身体与环境

低处、凹处、暗处、夜间、寒凉、湿润、连续水路与内部水循环可作形态／环境候选。身体题可检索体液、水液代谢、泌尿与下部通道，但疾病和部位结论必须另有身体专题、多锚点与医学核验。

### 学习、工作与资源

可查询持续收集、内部消化、低位连接、夜间／周期性运行、液体或信息流通、积累后再发动等工作性质。研究、物流、水务、夜班、数据系统等只是领域载体线索，不能由一个子支直接推出行业。

### 物件、场所与关系

北方、夜间空间、低洼处、井渠、水道、排水／供水通道、冷湿空间、内部循环系统可作候选。鼠是生肖／动物候选；“孩子”只有在子女轴已由六亲规则锁定后才能辅助着色，不得代替用神与六亲判定。

## 7. Topic axes

| axis | coverage | 领域候选与状态桥 |
|---|---|---|
| `behavior_personality` | `derived_candidate` | 以明确人物为体，且集中、潜藏、收集、等待时机或低位流通的动作反复稳定时，可表现为感受环境变化、保存信息资源、在幕后酝酿后发动；缺方向、边界或出口时才考虑无边界联想、内部循环与方向感不足。不得由子直接定为聪明、心细、神秘、内向或多变。 |
| `appearance_body` | `supported_candidate` | 可查询低位、含蓄、湿润、寒凉、连续水路感，以及体液、水液代谢、泌尿和下部通道；外貌与疾病须身体专题、柱位和多重锚点。 |
| `learning_cognition` | `derived_candidate` | 可查询收集材料、内部消化、保持线索、等待条件成熟再输出的认知方式；无出口时再考虑思路在内部反复或方向未定。子不直接决定智力、学历或研究能力。 |
| `career_work` | `derived_candidate` | 可查询持续流通、内部调度、夜间／周期运行、信息或液体通道、资源蓄积后启动等工作性质；具体行业与岗位必须交给领域载体模块比较。 |
| `wealth_resource` | `derived_candidate` | 财／资源轴已成立时，可查询资源汇集、低位归集、流动性、储备与等待投放；阻塞、渗漏或分散必须有结构状态支持。子本身不等于暗财、现金流好或破财。 |
| `family_relationship` | `derived_candidate` | 六亲身份锁定后，可查询谁在保存信息、承接情绪、维持内部流通或等待时机；“子＝孩子”只作低权重字义候选，不能替代妻财／官鬼／印等实际六亲用神。 |
| `object_place` | `supported_candidate` | 可查询北方、夜间空间、低洼处、井渠、水道、排水／供水通道、冷湿空间、内部循环系统及鼠类；须按季节、位置、功能和同柱共振竞争选载体。 |

## 8. Bridge requirements

每次把子卡写入 finding，至少记录：

1. `fact_receipt`：Reader 中的子支位置、月令身份、癸隐藏节点、司令状态与表源；
2. `field_layer`：本题实际调用仲冬、北方、夜半、低位、水场还是容器中的哪一项；
3. `qi_layer`：癸当前只作库存／根气／供给／待时，还是另有资格；
4. `function_layer`：若声称癸直接做功，引用 direct-action gate、实际 edge、通量、承接与竞争；
5. `result_layer`：现实载体、人物体、领域轴与结果条件是否另行通过；
6. `carrier_comparison`：水道、内部系统、资源流、作息场景、动物／字义等候选为何当前一个更匹配；
7. `timing_boundary`：若由岁运／他人激活，注明 overlay 范围、expiry 及重算内容。

## 9. Runtime unit map

| unit_id | unit_class | 对应内容 | allowed_topics | activation requirements | claim ceiling／forbidden promotions | source_layer |
|---|---|---|---|---|---|---|
| `ZI-FIELD-MIDWINTER-WATER` | `semantic_core` | 仲冬、北方、寒水、低位、集中、潜藏与等待转机的季节场 | 全部相关 topic | Reader 确认子节点；query 明确需要场、季节或容器 | 只解释机制；不得重算月令、旺衰、调候、关系或吉凶 | `bazi_primary＋current_synthesis` |
| `ZI-POLARITY-BODY-USE` | `semantic_core` | 命理分类作阴，同时保留“体阳用阴”与冬至转机的不同太极点 | behavior_personality／learning_cognition／career_work／family_relationship | 查询确实涉及隐显、收束与发动方式，且有相应人物／领域体 | 只说明层次；不得由阴阳标签推出性别、性格、主动被动或事件 | `bazi_primary＋cross_system_common_symbol＋current_synthesis` |
| `ZI-STATE-MANIFESTATION` | `state_modifier` | 场在、气在、用起、果显及 retained／concentrated／redirected／damaged 的表达切换 | 全部相关 topic | 引用 branch_manifestation_handoff 与 post-relation state | 只继承状态；不得自行判透清、合冲刑害、水局或结果兑现 | `current_synthesis` |
| `ZI-QI-GUI-MAIN` | `state_modifier` | 子中癸本气的库存、根气、环境供给、待时或 direct-action 接口 | 全部相关 topic | Reader 隐藏节点存在；Structure 给出逐节点 gate、边、通量与承接 | 只解释已裁功能；本气不等于必然发用，不得把子与癸互换 | `bazi_primary＋current_synthesis` |
| `ZI-COMMANDER-REN-GUI` | `state_modifier` | 子月壬十、癸二十的司令过渡 | 结构冻结后的月令解释／timing | Reader 的 month_command 有节气偏移、来源与采用口径 | 只解释已选司令；不得把壬写入静态藏干或机械按日数定命 | `bazi_commentary` |
| `ZI-ACTION-GATHER-GERMINATE` | `semantic_core` | 收集、内部蓄积、等待条件、在收束中酝酿下一轮发动 | behavior_personality／learning_cognition／career_work／wealth_resource／family_relationship | person／topic anchor 与 repeated-and-stable 或持续路线成立 | 只说明过程；不得直推聪明、心细、隐秘、消沉、研究或管理身份 | `cross_system_common_symbol＋current_synthesis` |
| `ZI-SHAPE-WATER-NIGHT` | `symbol_carrier` | 夜半、北方、低处、暗处、寒凉、湿润、连续水路与内部循环形态 | appearance_body／object_place／career_work | 形态／环境题、位置功能及竞争载体共同支持 | 最高 candidate；不得由一个子字直断外貌、住宅、夜班、水务或疾病 | `bazi_primary＋bazi_course＋current_synthesis` |
| `ZI-BODY-FLUID-LOWER-PATH` | `symbol_carrier` | 体液、水液代谢、泌尿及下部通道查询 | appearance_body | 身体专题、对应位置、关系后状态及多重锚点 | 最高 candidate；不得诊断泌尿、肾脏、寒湿或生殖疾病 | `bazi_course＋current_synthesis` |
| `ZI-RELATION-CHILD-WORD` | `relational_carrier` | “子”字的孩子联想 | family_relationship | 明确子女题；六亲用神、宫位／柱位、相关节点与路线先锁定 | 最高 candidate；不得以子支替代子女用神或断子女数量、性别、事件 | `bazi_course` |
| `ZI-ZODIAC-RAT` | `symbol_carrier` | 鼠类、夜行动物及生肖场景候选 | object_place／family_relationship | 问题确涉及动物／生肖／物件，且有额外形态或场景锚点 | 最高 candidate；不得从鼠类比推出心细、机警、偷盗或固定人格 | `bazi_course` |
| `ZI-CROSS-QIMEN` | `cross_system_context` | 阳气始萌、植物萌芽与坎位等跨体系检索线索 | 仅明确需要的相关 topic | 去除奇门宫星门神及关系技法后，仍能回接季节或共同符号 | source-only context；不得转发为 selected unit、进入八字结构或具体断验 | `cross_system_common_symbol` |

具体研究、物流、水务、夜班、数据系统、儿童身份及家庭事件，不设为子卡可独立激活的复合载体。它们必须由领域载体模块结合十神功能、柱位、结构路线、现实接口、持续性和竞争场景另行晋级。

## 10. Cannot decide

本卡不能单独决定子是否旺、寒水是否需火、癸是否直接发用、壬癸何者司令、子丑是否合化、申子辰是否成局、子午冲结果、某人是否聪明心细、是否有子女、是否从事水务物流，或任何疾病与事件。上述判断分别返回 Reader、Structure Core、Topic Lens、领域载体与身体专题。

## 11. Source receipts

### S0｜五行与地支共同底座

- 文件：`skill/bazi-source-lookup/references/deep-cards/five-elements-core.md`；`skill/bazi-source-lookup/references/deep-cards/earthly-branches-core.md`
- 支持：水曰润下；地支作为季节场与复合容器；场在、气在、用起、果显四层显化
- provenance：`current_synthesis`（五行核心回溯《尚书·洪范》与本项目已核来源）

### S1｜《千里命稿》原典

- PDF：`external-source://qianli-minggao-pdf`
- 高保真整理：`skill/bazi-structure-dynamics/references/qianli-minggao-fidelity-full.md`
- 本轮核读：源 PDF 第 17、33—34、178 页；整理版地支篇子条、人元问答与体用段
- 支持：子属水、作阴、北方、十一月、大雪至小寒、藏癸；同书解释“子午本属阳……体阳而用阴”
- 边界：生克合刑冲害与三合方合只进入 Structure；不能从阴阳、藏癸或关系表直接推出现实事件
- provenance：`bazi_primary`

### S2｜《子平真诠》原本与徐乐吾评注

- 文件：`ziping-zhenquan-original-full.md`；`ziping-zhenquan-commentary-full.md`
- 本轮核读：原本论阴阳生死、地支作用、支中人元与杂气取用；评注人元司令表及“本静待用、透出显用”的完整上下文
- 支持：地支承载月令与根气；子月司令表为壬十、癸二十；藏气发用须结合透出、得令与全局
- 边界：司令日数“未可执着”；透出提高显用资格，不等于自动得用或结果已显
- provenance：`bazi_primary＋bazi_commentary`

### S3｜若境清八字课程

- 文件：`skill/bazi-structure-dynamics/references/ruojing-qianli-01-full.md`
- 本轮核读：地支段子条完整上下文
- 可迁移：子属水、北方、藏癸、四正气较纯、半夜、鼠与“孩子”联想的候选入口
- 降权／排除：心细不作固定人格；子女联想不替代六亲用神；课程中的合刑冲害结论不由 Deep Card 迁移
- provenance：`bazi_course`

### S4｜奇门共同符号材料

- 文件：`external-source://qimen-note-03-five-elements`；`external-source://qimen-note-05-earthly-branches`
- 可迁移：润下、仲冬、北方、阳气始萌、消长循环与地支作为季节容器的检索线索
- 不迁移：坎宫断验、宫星门神、击刑、六合无合化、奇门三会与固定人格吉凶
- provenance：`cross_system_common_symbol`

### S5｜当前架构归纳

- 内容：把子整理为仲冬集中水场；分开支体／季节转机、癸本气与壬癸司令；建立四层显化、七轴与 runtime units
- provenance：`current_synthesis`

## 12. Forward-test questions

1. 模型能否把子作为仲冬水场处理，而不把它缩写成一枚癸水天干？
2. 模型能否同时保留“命理作阴”“体阳用阴”和冬至转机，而不拿一个标签覆盖全部层次？
3. 模型能否区分子藏癸与子月壬癸司令，不把壬补进静态藏干？
4. 癸不透时，模型能否保留场、库存、根气与待时接口，同时不虚构 direct-action edge？
5. 模型能否把“半夜、鼠、孩子”保留为可用候选，又不升级成固定人格、子女用神或事件？
6. 出现流年／他人触发时，模型能否重算相关功能与期限，而不把临时显性写回原局？
