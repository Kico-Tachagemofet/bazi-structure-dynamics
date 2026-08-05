---
name: bazi-topic-lens
description: 把完整原局报告范围或追问中的具体八字问题限定到已审计并冻结的结构载体：读取 report-scope，把求测者自然语言中的中心转换为逐专题太极点，完整原局至少为家庭、学业、财运、事业建立四个独立镜头，再为关系、健康、神秘学、创作、岁运或合盘选择相关柱、节点、作用链、领域载体、时间层与完整取象单元。用户需要从结构进入正常断局、避免从十神标签直接跳故事，或后续聊天要判断该直接解释、补取象还是退回结构层时使用。本技能不重算原局，也不产生活断语。
---

# 八字 Topic Lens

把“用户问什么”转换为“需要读取哪些已审计结构”，不在本阶段重新断盘。

## 必需输入

- case-manifest.yaml
- chart-stage1.yaml
- structure-kernel.md
- problem-state.yaml、route-candidates.yaml、conditions-matrix.md
- structure-freeze-receipt.yaml
- 已通过的 bazi-finding-audit
- `report-scope.yaml` 或用户的限定具体问题

缺少结构核、结构冻结或审计未通过时停止。若本轮结构文件版本晚于 freeze receipt，先退回结构审计。

## 镜头类型

- family-home
- education-learning
- wealth-resource
- career-work
- love-relationship
- health-body
- occult-perception
- creation-expression
- social-collaboration
- children-parenting
- timing
- synastry
- general

## 太极中心转换

每个 topic 都必须有独立 `taiji_center`，至少记录：

- `chart_subject`：命盘主人；
- `user_language_center`：求测者所说的具体人、关系、事件或组织；
- `center_type`：self／person／relationship／family-system／event／organization／object；
- `relation_to_chart_subject`；
- `technical_anchor`：本 topic 实际采用的柱位、十神功能、节点与路线；
- `why_this_center` 与替代中心。

完整原局默认以命主本人为总中心，但四个基础领域仍分别建立领域中心。不要要求求测者自己选择十神或柱位；技术太极由本技能依据冻结结构完成。

## 完整原局批量镜头

当 `delivery_mode: full-reading` 时：

1. 先产出 `topic-lens-index.yaml`，列明全部 mandatory 与 selected topics；
2. 分别产出 `topic-lens-family-home.md`、`topic-lens-education-learning.md`、`topic-lens-wealth-resource.md`、`topic-lens-career-work.md`；
3. 再为 `selected_optional_sections` 逐项建独立 lens；
4. 四个基础板块可以共享结构锚点，但不得合并成一个 general lens；
5. 家庭镜头必须预先声明 `blind_calibration_anchor: true`，且 `family_context_available_to_finding: false`。

limited-topic 只建立约定镜头，同时记录未覆盖基础板块和“不得称完整断局”。

## 强制区分

每个问题都要分别标注：

1. **内部机制**：能力、倾向、身体或心理的运作方式；
2. **领域载体**：现实中由什么任务、关系、制度或媒介承载；
3. **外部结果**：是否真的形成职位、收入、名声、事件或可见成果；
4. **时间条件**：原局常态、岁运激发还是关系场限定；
5. **反向代价**：同一节点在其他路线中的不利作用。

同时建立 **取象覆盖请求**：

- 相关柱的天干、地支、十神与柱位；
- 每个相关支的全部藏干；
- 需要合成的同柱双向着色对；
- 改写基础象的主问题、作用边、竞争路线与条件开关；
- 本轮必须读取的完整 imagery units；
- 首次未展开、可供后续追问增量加载的范围。

例如，财制枭在职业学习领域显为知识现实化，不会自动把财升级为全局唯一喜神；神秘学感知也不能只由偏印标签直接推出。

## 岁运镜头

- 锁定原局后再叠加大运、流年、流月。
- 输出前后差分：新增根、补齐关系、加强或阻断哪条边、激活何种潜伏路线。
- 时间层负责触发与改道，不反过来改写原局事实。

## 合盘镜头

- 双方原局必须各自审计通过。
- 跨盘干支只作临时接口，不自动成为对方本命之根。
- 直接叠盘是显式案例模式，不是普遍子平规则。
- 分开内部关系场和外部职业社会场；后者需要现实载体，置信度通常更低。

## 输出

按 [Topic Lens Packet schema](references/topic-lens-schema.md) 产出 topic-lens.md，至少列：

- 太极点／问题范围；
- 相关节点和已审计路线 ID；
- 领域载体；
- 必须加载的完整取象来源；
- 时间或合盘层；
- 禁止越界的结论；
- 最强替代解释。
- 问题属于首次报告、已有 finding 澄清、同结构新取象、新 topic、timing、synastry 还是 structural challenge。

输出后交给 `$bazi-source-lookup` 加载 imagery source，再由 `$bazi-imagery-composition` 生产 finding。本技能不得新增上游不存在的结构判断或生活断语。
