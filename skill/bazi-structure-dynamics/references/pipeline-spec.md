# 八字 Fresh Reading Pipeline

## 默认路径

| 阶段 | 负责什么 | 产物／停止点 |
|---|---|---|
| Reader | 核对盘面事实 | `case-manifest.yaml`、`chart-stage1.yaml` |
| Structure | 收束旺衰、格局、十神链与用神 | `source-notes.md`、`structure-notebook.md` |
| Scope gate | 向用户确认命主、专题与时间范围 | 信息不足时停止并等待 |
| Seal | 把允许材料固定为独立输入 | `report-scope.yaml`、`reading-pack/` |
| Fresh writer | 在无历史上下文中取象并成文 | `full-reading.md` |

普通报告到此结束。Topic Lens、reading notebook、composition 和独立审计只在诊断、研究或用户明确要求时使用。

## 入口语义

- 显式 `$bazi-reader` 默认只做事实阶段。
- “断一下／看看／分析一下”不是完整范围授权。
- “完整原局”可确认核心原局范围，但感情、六亲、子女与岁运仍按用户原话和必要口径处理。
- 用户明确列出专题、年份和命主信息时，无需重复提问。

## 回退

- 盘面事实错，回 Reader。
- 旺衰、格局、关系或用神错，回 Structure。
- 范围不清，停在 Scope gate。
- reading pack 缺材料，补 pack 后重新启动 fresh writer。
- writer 文风不理想但事实与范围完整，不用审计链修饰；需要重写时换一个干净 writer。

## 完成标准

报告覆盖用户确认范围，能够从固定结构与取象材料形成现实判断，并保持自然完整的断盘行文。中间文件数量、字段齐全、标题格式和审计痕迹不属于完成标准。
