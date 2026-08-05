---
name: bazi-topic-lens
description: 把首次或追问中的具体八字问题限定到已审计并冻结的结构载体：为职业、学习、财务、关系、健康、神秘学、创作、岁运或合盘选择相关柱、节点、作用链、领域载体、时间层，并列出必须加载的完整干支十神藏干取象单元、同柱双向着色和 full-chart sweep。用户需要避免从十神标签直接跳故事，或后续聊天要判断该直接解释、补取象还是退回结构层时使用。本技能不重算原局，也不产生活断语。
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
- 用户的具体问题

缺少结构核、结构冻结或审计未通过时停止。若本轮结构文件版本晚于 freeze receipt，先退回结构审计。

## 镜头类型

- career-learning
- money-resource
- relationship
- health-body
- occult-perception
- creation-expression
- timing
- synastry
- general

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
