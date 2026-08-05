# 八字经历映射与流运验证协议

## 1. 两种不同任务

先判断本轮是在做哪一种事，不得混称：

- **显化映射（manifestation mapping）**：结构与 findings 已审计后，读取经历，判断同一机制主要落在家庭、职场、关系、学习、资源或身体节律等哪个载体。它可以调整呈现顺序、措辞、领域载体和后续问题，但不增加结构置信度。
- **证据验证（evidence validation）**：在读取相关经历前，先形成有时间窗、顺序、机制、领域竞争和失败条件的复杂假设，审计并冻结；读取原始回应后按固定量表计分。只有满足完整流程时才称验证。

完整原局不强制做验证。没有合格验证条件时，交付已审计但未验证的报告，比使用宽泛问题制造命中更合格。

## 2. 默认选择

优先使用跨领域的流运对照预注册。它通常比单独询问原局性格或家庭情景更有区分度，因为时间窗、先后次序和差异年可以提供反证。

只有同时满足下列条件才启动：

- natal 已审计并冻结；
- 出生时间、起运方向和换运边界足以支持所选时间粒度；
- 所选大运／流年／流月 overlay 已完成 before／after diff、审计与冻结；
- 相关年份或事件历史尚未被读取，或已知污染范围能够明确排除／降权；
- 至少能构造两个有真实差异的时间窗，或一个具有明确阶段顺序和失败条件的时间窗。

不满足时选择 `manifestation-mapping` 或 `none`，不得降低标准强行计分。

## 3. 预注册步骤

### 3.1 先建验证计划

产出 `validation-plan.yaml`，至少记录：

- `case_id`、`validation_id`、`validation_mode`；
- natal freeze、timing overlay freeze 与相关 audit IDs；
- 候选时间窗、选择理由和 observation cutoff；
- 已读取经历、旧解读和专题偏好清单；
- 每个已知先验的污染等级：clean／partial-prior／contaminated；
- 明确排除或降权的年份、领域与命题；
- 若无法盲验证，写 `validation_eligibility: ineligible` 并停止。

选择时间窗时只读排盘和岁运事实，不读年史。不得因为已经知道某年发生大事才挑选该年。

### 3.2 写复杂假设

产出 `timing-validation-hypotheses.md`。每条假设至少包含：

1. **窗口或对照**：哪一年／阶段应与哪一年／阶段不同；
2. **事件顺序**：先出现什么机制，后出现什么负担、成果或改道；
3. **路线机制**：引用哪些 natal route、timing diff 和竞争关系；
4. **领域排序**：最多两个 primary carriers，可列 secondary carriers；领域只是载体，不得把所有领域全部罗列；
5. **可辨认表现**：使用复合过程，例如“先共同娱乐／共同做事，再因现实安排增加维护责任”，不能只写“关系有变化”；
6. **失败条件**：什么真实叙述会使假设不成立；
7. **先验处理**：已知领域或既有线索如何降权；
8. **不完整窗口**：注明截至日期，未发生部分保持 prospective，不提前计分。

禁止把“忙、压力、变化、机会、关系波动、说得通”等高基率词单独作为命中点。假设若没有机制顺序或反事实，退回重写。

### 3.3 审计与冻结

调用 `$bazi-finding-audit` 审计：

- 假设是否只引用冻结 natal 和 timing overlay；
- 是否在读取年史前完成；
- 是否存在明确时间差、顺序、机制和失败条件；
- 是否用过多领域制造不可证伪；
- 是否登记全部已知先验并做降权；
- 是否把神煞、单一十神或一个冲合直接写成事件。

PASS 后产出 `timing-hypothesis-freeze-receipt.yaml`，记录假设文件、审计报告和上游 timing imagery／overlay 的 SHA-256。冻结后不得修改措辞来贴合回应；需要新增假设时建立新版本，并与原版本分开计分。

## 4. 两档回应模式

冻结完成后才由 `$bazi-render` 提问，但详细回填必须由用户主动选择，不得作为默认负担。

### 4.1 默认：快速反馈

默认只给一个低负担入口：

> 你可以只回复“准／部分准／不准／记不清”；愿意时补一句最明显或最不对的地方就够了，不需要逐年填事件。若想进一步定位具体年份、先后顺序和实际落在职场、关系、家庭等哪个载体，可以说“展开验证”，我再启用详细模式；这有助于细化命盘，但不启用也不影响报告。

允许用户只评价整体，也允许按假设简短评价。产出 `timing-validation-quick-feedback.md`，记录：

- `feedback_level`：overall／per-hypothesis；
- `fit_state`：accurate／partly-accurate／inaccurate／unclear-memory；
- 用户自愿补充的一句话；
- `non-evidentiary: true`；
- `formal_score_state: not-run`。

快速反馈不进入 0–8 计分，不提高结构或时间假设置信度，也不触发自动追问。它的用途是让用户方便地表达体验、指出最明显的偏差，并决定是否值得继续展开。

### 4.2 可选：详细验证模式

只在用户主动说“展开验证”“详细说说”“继续回填”等明确意图后启用。说明一次价值即可：详细叙述可以帮助区分时间是否命中、事件先后是否吻合、同一结构实际落在哪个领域，以及哪条路线只是可能性。

提问使用一句自然语言，每次只处理一个时间窗，例如：

> 请随意讲讲 2018 和 2020 各自最明显发生了什么；如果记得，带一下先后和主要领域，记不清的年份可以跳过。

禁止默认抛出“1–3 件事／大致时间／发展顺序／所属领域／是否返工”等多项表格。只有用户已经开始叙述、且某个缺口会实质改变评分时，才补一个简短追问；不得为了填满 rubric 反复索取细节。

详细模式优先请求自由叙事：

- 该时间窗实际发生了什么；
- 能记得时说明先发生什么、后来怎样；
- 主要落在哪个领域；
- 没有或记不清可以直接写“没有／记不清”。

不要先把假设拆成关键词清单诱导逐项确认。把用户原话完整写入 `timing-validation-response.md`，与假设文件分离；可以另外做 evidence extraction，但不得改写原始回应。

若用户在启用详细模式前已经看过具体假设或给过快速反馈，记录 `hypothesis_exposure: partial／full`。详细叙述仍可用于领域载体与机制分析，但最终验证强度必须注明提示暴露，不得称完全盲回填。

“不一定明确意识到，但说得通”记为 `indeterminate`；只有通用词重合记为 `non-discriminating`；二者均不加分。缺失或记不清记为 `unscored`，不能按反证扣成零分。

## 5. 固定计分

每条已冻结假设默认满分 8 分：

| 维度 | 分值 | 判定 |
|---|---:|---|
| `window_hit` | 0–2 | 时间窗或对照差异是否出现 |
| `sequence_hit` | 0–2 | 先后次序是否吻合；只有关键词而无顺序计 0，次序不完整／记忆不确定最多 1 |
| `route_mechanism_hit` | 0–2 | 叙述机制是否对应预注册路线，而非事后换解释 |
| `domain_hit` | 0–1 | 是否落在预注册的优先载体；已知领域默认最高 0.5 |
| `counterfactual_survival` | 0–1 | 预设失败条件是否未出现，且反向情形没有更吻合 |

总分解释：0–2 unsupported；3–4 weak；5–6 medium；7–8 strong。若核心历史缺失，标 `unscored`，不把未知包装成 weak 或 unsupported。

产出 `timing-validation-scorecard.md`，逐维引用原始回应证据，列明 miss、uncertainty、prior discount 和 observation cutoff。禁止把多个假设的零散命中拼成一条高分。

随后调用 `$bazi-finding-audit` 产出 `timing-validation-score-audit.md`。审计器只检查计分是否忠于冻结文本与原始回应，不替分析者寻找更好解释。

## 6. 结果用途

- 验证结果可以支持、削弱或保留某条**时间假设**及其领域载体优先级。
- 单次验证不能证明通用命理规则，也不能反向改写 natal node、edge、route、pattern 或司令事实。
- 结构性反例应登记为 `structural-challenge`，另开审计；不得在 scorecard 中圆回。
- 显化映射使用 `manifestation-map.md`；历史兼容文件 `calibration-map.md` 必须显式标注 `non-evidentiary: true`。
- 最终报告分别写明：结构审计状态、经历映射状态、验证状态与验证强度。不得用“已校准”模糊合并三者。

## 7. 最低产物集

若只收快速反馈，只需 `timing-validation-quick-feedback.md`，且不得声称完成正式验证。若声称完成流运验证，必须存在：

- `validation-plan.yaml`
- 受审计并冻结的 timing diff／overlay
- `timing-validation-hypotheses.md`
- `timing-hypothesis-audit-report.md`
- `timing-hypothesis-freeze-receipt.yaml`
- `timing-validation-response.md`
- `timing-validation-scorecard.md`
- `timing-validation-score-audit.md`

任一缺失时只能说“进行了经历讨论”或“完成显化映射”，不得称盲验证、回验通过或验证命中。
