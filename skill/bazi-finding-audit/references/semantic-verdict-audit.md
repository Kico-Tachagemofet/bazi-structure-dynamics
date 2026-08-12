# 现实断语语义审计 v1.0

本审计先问“到底断出了什么”，再问“字段是否齐全”。程序完整不能挽救语义空洞。

## P0：专题是否真正完成

逐 Topic Lens 的 `mandatory_judgment_dimensions` 检查：

- 每一维是否唯一处置为 `directional-verdict／not-applicable／source-gap`；
- directional verdict 是否说明主要方向、相对强弱、现实结果和反转条件；
- not-applicable／source-gap 是否有具体盘面或来源缺口，而非“谨慎”“具体职业无法判断”；
- 每一维是否有独立 claim kernel、judgment ID 与正文 span；可以共用根因说明，但不能被综合句替代；
- 是否分开日主承载、客观产出、社会兑现和持续代价。

任一 required dimension 静默缺失，P0 FAIL；后续字段再齐也不得 PASS。

## 学业正向检查

必须能够直接回答：

- 学习能力怎样；
- 正规学历／认证达到较高、中等还是偏弱层级；
- 专业训练是长期深入还是短期实用；
- 考试、论文、实践输出怎样影响最终学历；
- 1–30 岁大运使其继续学习、转轨、边学边做还是中断。

只写“会自学、重实践、学习方式不同”而不判断学历和专业训练：FAIL。

出现财、食伤或官杀运时，若未比较供给／带薪教育、军校／单位培养、实习／临床／学徒、边学边做和正式就业，便直接判离校或学历受限：FAIL。

## 事业正向检查

必须能够直接回答：

- 靠什么专业功能吃饭；
- 核心动作和材料是什么；
- 技术、制度、经营、研究、管理等性质何者为主；
- 资格、机构、授权、职级和实际责任怎样；
- 名声／科名、收入与职位是否同路；
- 单位／岗位／地点是否易变；
- 冲突和代价从哪条链产生。

只写“流程、交付、维护、收尾、承担责任”而无上述判断：FAIL。

## 五级断语检查

- L1–L3 有组合支持却因 L5 具体身份不确定而全部降为 candidate／不判断：FAIL。
- L4 未比较相容载体家族，或只返回 Lens 预选的泛化家族：FAIL。
- L5 未断具体职业不构成失败；L5 由单一符号或已知经历直接定案才是失败。
- exact identity 未过门时，正文仍须完整保留 L1–L4。

## 反模板与独立性

- 不按预定句子、禁词、字数、固定 finding 数或 case-specific answer key 判定生产物合格。
- 父亲或其他已知案例事实只可放在生产完成后的隔离 scorecard 中，不可进入 producer、Lens、Source、Composition 或 validator。
- 独立审计员先读匿名产物与通用 rubric，再在需要评估现实命中时由隔离评估层读取已知事实。
- 同一候选 skill 必须通过反例盘；若所有盘都被抬成高学历、技术权威或正式官职，视为方向膨胀。

## 最终裁决

P0 语义检查优先于 A／B／C 程序检查。P0 FAIL 时，修复阶段应指向最早丢失该现实端点的层：

- process 四面裁决缺失 → Structure Core；
- judgment dimension 缺失 → Topic Lens；
- activated 候选丢失 → Source Lookup；
- 未拆 claim kernel／未排序 → Imagery Composition；
- finding 已有而正文丢失 → Composition／Render。
