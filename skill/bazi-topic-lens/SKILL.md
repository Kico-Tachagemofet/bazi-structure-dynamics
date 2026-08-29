---
name: bazi-topic-lens
description: 可选的八字专题诊断工具。在用户明确要求查看内容地图、限定专题需要额外拆解，或 fresh report 明显遗漏现实层时，把已确认范围映射到十神链与干支柱位。普通完整报告默认不调用，只产一份 topic-map。
---

# 八字 Topic Lens

本技能用于诊断“某个专题到底还缺什么材料”，不是普通完整报告的前置步骤。

## 使用时机

- 用户明确要求内容地图或分析底稿；
- 只看一个复杂专题，需要把不同现实端点拆开；
- fresh report 已经产生，但某章明显只有泛化性格或遗漏关键层级。

## 输入

- `chart-stage1.yaml`
- `structure-notebook.md`
- `report-scope.yaml`

## 输出

只写一份 `topic-map.md`。每个专题简要说明：太极中心、相关十神链、天干地支藏干柱位锚点、必须判断的现实端点，以及最强竞争解释。

它不预写答案，不规定 finding 数和章节格式，也不自动启动 Imagery、Composition 或 Render。完成诊断后，由调用者决定补 reading pack 还是重新启动 fresh writer。
