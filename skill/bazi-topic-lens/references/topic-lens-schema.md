# Topic Lens Packet Schema

topic-lens.md 至少包含以下部分。

## Scope

- case_id
- topic_type
- exact_question
- natal／timing／synastry scope
- framework lock
- request_mode：initial-report／follow-up
- follow_up_type：clarification／new-imagery／new-domain／verification／counterexample／timing／synastry／structural-challenge／contradiction
- structure_freeze_id
- report_scope_id／report-scope path
- delivery_mode：full-reading／limited-topic
- baseline_required：true／false

## Taiji Center

- chart_subject
- default_center
- user_language_center
- center_type：self／person／relationship／family-system／event／organization／object
- relation_to_chart_subject
- technical_anchor：pillar／node／edge／route refs
- why_this_center
- alternative_center
- center_confidence

## Structural Index

只引用已审计产物：

- relevant node IDs
- relevant edge IDs
- relevant route IDs
- structure-kernel sections
- excluded but tempting signals

## Manifestation Layers

分别填写：

- internal mechanism
- domain carrier
- external result
- timing condition
- counter-cost

## Source Needs

- required full imagery units：stem／branch／ten-god／pillar-position／hidden-stem／relation／domain
- relevant pillar full-anatomy requirement
- stem-on-branch and branch-on-stem coloring pairs
- source query IDs
- missing imagery evidence
- deferred imagery that may be loaded in later Q&A
- confidence cap

## Full-chart Sweep Request

- reinforcing nodes／edges／routes
- weakening or reversing nodes／edges／routes
- competing allocation
- same ten-god elsewhere
- tempting but excluded anchors
- internal mechanism versus external result checks

## Boundaries

- allowed claims
- forbidden overreach
- strongest alternative explanation
- real-world verification needed

## Full-reading Index

`topic-lens-index.yaml` 至少包含：

- `case_id`
- `structure_freeze_id`
- `report_scope_ref`
- `mandatory_topics`：family-home／education-learning／wealth-resource／career-work
- `selected_optional_topics`
- `produced_lenses`
- `missing_lenses`
- `omitted_baseline_sections`
- `completeness_verdict`

每个 lens 另含：

- `subject_context_available_to_finding: false`
- `manifestation_mapping_allowed_after_audit: true`
- `validation_role`：none／primary-carrier／secondary-carrier／excluded-prior
- `validation_plan_ref`（若存在）
- `known_prior_discount`（若存在）

timing validation lens 还含：

- `contrast_window`
- `observation_cutoff`
- `expected_sequence_slots`
- `candidate_route_mechanisms`
- `carrier_priority`
- `counterfactual_requirements`

这些字段只为后续预注册提供结构索引，不在 Topic Lens 阶段产事件假设或读取年史。家庭镜头没有默认验证特权。

Topic Lens 不得重算旺衰、成局或格局。发现上游缺失时退回 Structure Core。

Topic Lens 也不得直接产生活断语；“需要读取某象”与“该象最终成立”必须分开。
