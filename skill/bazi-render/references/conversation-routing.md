# 八字对话路由

## 1. 先识别问题类型

| 类型 | 例子 | 处理 |
|---|---|---|
| report-scope-intake | “结构看完了，接下来完整断盘” | Render Mode 0 确认中心、基础四板块与附加专题，再退回 Topic Lens |
| manifestation-mapping | “这条其实主要在公司发生” | 映射到已有 finding 的领域载体；标 non-evidentiary，不新增 finding |
| validation-intake | “按流运验证一下” | 检查 hypothesis freeze；冻结前退回 validation planning，冻结后只收自由年史 |
| validation-quick-feedback | “整体部分准，2024 不太准” | 保存低负担主观反馈；不计分、不追问，等待用户主动选择是否展开 |
| validation-expand | “展开验证／我想详细说发生了什么” | 启用 detailed opt-in；每次一个时间窗、一句自然问题 |
| validation-scoring | “这些年份能支持多少？” | 引用冻结假设、verbatim response 与固定 rubric；交 audit 复核 |
| clarification | “你说庚戌难用具体是什么意思？” | 直接解释已有 finding |
| comparison | “这是财制枭还是食神制杀？” | 引用已有路线比较；缺路线则退回 Core |
| new-imagery | “丁火在视觉上还能怎么取？” | 同锚点增量 Source + Imagery Composition |
| new-domain | “这个结构放到亲密关系会怎样？” | 新 Topic Lens + 增量 finding |
| verification | “我确实换过专业，这算哪一条？” | 先分流为 manifestation mapping 或 preregistered validation；不倒推结构 |
| counterexample | “但我实际并不懒。” | 检查表达带、条件与替代解释；必要时审计 |
| timing | “28 年会怎样？” | timing diff，不由 Render 猜 |
| synastry | “他来了以后为什么变了？” | 双盘 audit + overlay／关系场 |
| structural-challenge | “你是不是漏了戊癸合绊？” | 退回 structure audit |
| contradiction | “你前后说法相反。” | contradiction audit，先解决再答 |

## 2. qa-route.yaml

至少记录：

- `turn_id`
- `exact_question`
- `intent_type`
- `topic_scope`
- `candidate_anchor_ids`
- `existing_finding_ids`
- `imagery_coverage_state`
- `required_upstream_action`
- `route_verdict`：report-scope-intake／manifestation-mapping／validation-planning／validation-quick-feedback／validation-expand／validation-intake／validation-scoring／direct-render／supplement-imagery／new-topic／timing-diff／synastry-overlay／structure-audit／blocked
- `reason`
- `forbidden_shortcut`

## 3. 直接回答门槛

只有同时满足以下条件才可 `direct-render`：

- 问题所需结构已经冻结；
- 至少一个通过审计的 finding 覆盖问题；
- 所需原始象意单元已加载；
- 没有新时间层、跨盘层或结构争议；
- 答案不会新增上游没有的生活判断。

首次完整原局在没有 `report-scope.yaml` 时不得 direct-render；先走 `report-scope-intake`。完整报告缺基础四板块或已选专题时不得用“已有部分足够”放行。

## 4. 增量取象与结构重算的边界

### 只需补取象

结构中的柱、节点、路线和主问题不变；只是问题换了领域、载体或要求展开某个原象。新增的是 `source unit → composite → finding`。

### 必须重算／重审

问题要求改变或新增：

- 司令、旺衰、合化、支局、冲开库；
- 节点 availability；
- active edge、路线方向或主问题；
- 大运流年覆盖；
- 跨盘临时接口。

新增的是结构事实时，Render 无权处理。

## 5. 对话回答形态

按问题所需选用，不要求每次全套：

1. 直接结论；
2. 当前涉及的干支／十神／柱位复合画面；
3. 全局为什么会加强、堵塞或改道；
4. 基线、受压、良性或反向版本；
5. 现实领域载体；
6. 技术依据与尚未证明的部分。

对话可以短，但不能删掉会改变答案方向的条件。
