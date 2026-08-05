# Topic Lens Packet Schema

`topic-lens-<slug>.md` 至少包含以下部分。

## 1. Scope

- `case_id`
- `topic_id`／`topic_type`
- `exact_question`
- `question_slices`
- `natal／timing／synastry scope`
- `framework_lock`
- `structure_freeze_id`
- `use_kernel_ref`
- `report_scope_ref`
- `delivery_mode`
- `subject_context_available_to_finding: false`

## 2. Topic Body／领域体

每个 question slice 分别记录：

- `question_slice_id`
- `user_language_center`
- `center_type`
- `relation_to_chart_subject`
- `body_anchor_refs`：pillar／ten-god／node／edge／route
- `why_this_body`
- `alternative_body_anchor`
- `internal_mechanism_target`
- `domain_carrier_target`
- `external_result_target`
- `body_confidence`

领域体只说明“看什么”，不承担“怎样解决”。

## 3. Use Pivot Lock／用神枢纽锁

- `primary_use_pivot_id`
- `framework_role`
- `why_relevant_to_this_topic`
- `current_availability`
- `daymaster_access`
- `auxiliary_use_pivots`
- `alternative_use_pivots`
- `excluded_use_readings`
- `use_kernel_evidence_refs`

不得在本文件新定用神；全部 ID 必须存在于 `use-kernel.md`。

## 4. Body-Use Relation Axes

每条实际关系轴至少含：

- `axis_id`
- `question_slice_id`
- `axis_role`：primary／supporting／contrast／deferred
- `focal_question`
- `topic_body_refs`
- `use_pivot_ref`
- `source_endpoint`／`target_endpoint`
- `node_refs`／`edge_refs`／`route_refs`
- `mechanism`
- `base_state`
- `supporting_factors`
- `damage_diversion_or_occupation`
- `destination_and_feedback`
- `daymaster_agency_relation`
- `competing_allocation`
- `switch_conditions`
- `failure_or_reversal`
- `strongest_alternative`
- `finding_disposition`：required／deferred／source-gap

一条轴只回答一个主过程。不同方向、不同端点或不同结果必须拆轴。

## 5. Imagery Source Needs

逐 axis 记录：

- `required_full_imagery_units`
- `relevant_pillar_full_anatomy`
- `hidden_stems_required`
- `stem-on-branch and branch-on-stem coloring_pairs`
- `relation／domain imagery units`
- `source_query_ids`
- `missing_imagery_evidence`
- `deferred_imagery`
- `confidence_cap`

## 6. Full-Chart and Boundary Notes

- reinforcing／weakening／reversing axes
- same node competing allocation
- same ten-god elsewhere
- tempting but excluded anchors
- internal mechanism versus external result checks
- allowed claims
- forbidden overreach
- real-world conditions required

## 7. Finding Handoff

- `primary_axis_ids`
- `supporting_axis_ids`
- `expected_primary_findings`：与 primary axis 一一对应
- `cross_topic_refs`
- `axes_requiring_timing_or_synastry_overlay`
- `unresolved_source_gaps`

不设统一最低 finding 数。主轴若未产 finding，必须有明确 `deferred／source-gap` 收据。

## Full-reading Index

`topic-lens-index.yaml` 至少含：

- `case_id`
- `structure_freeze_id`
- `use_kernel_ref`
- `report_scope_ref`
- `mandatory_topics`
- `selected_optional_topics`
- `produced_lenses`
- `topic_body_summary`
- `use_pivot_summary`
- `primary_axis_count_by_topic`
- `missing_lenses`
- `omitted_baseline_sections`
- `completeness_verdict`

