# 结构状态词

统一状态词，防止“有关系”被悄悄改写成“已经起效”。

## Node State

- available：节点当前可参与其他路线。
- limited：有气但容量有限。
- occupied：被合、局或竞争关系明显占用。
- suppressed：受季节、克制或调候环境压制。
- latent：藏而未显或需岁运触发。
- unavailable：本轮结构中无法形成有效输出。

## Edge State

- candidate：仅由五行或组合规则识别。
- active：条件充分，正在传递。
- weak：存在实际作用但容量低。
- blocked：被中间节点、环境或对手阻断。
- occupied：上游或下游被其他关系占用。
- redirected：力量被导向另一目标。
- conditional：需透出、补根、冲合或岁运条件。
- inactive：当前不参与主结构。

## Process Phase State

- passive-reception：当前主要承受上游作用，日主或本 phase 控制者尚未发动下游。
- active-initiation：启动门已通过，控制者正在提供本 phase 所需上游容量。
- active-redirection：已有通量被主动导向治疗、出口或另一目标。
- autonomous-flow：子系统依库存／环境供给运行，不等于日主主动调用。
- recovery：支援先恢复承载，后续 phase 是否开启仍另过 start gate。
- stalled：路线或库存可能仍存在，但本 phase 因供能、分配、承接或条件不足无法继续。

每个 phase 另分开 `start_gate: open／conditional／blocked`、`throughput_band: high／medium／low／conditional／none` 与 `agency_state: can-start／can-carry／can-redirect／can-stop`。不得用一个 active／inactive 开关代替。

## Timing Process Delta

- strengthened：同一 process 的实际吞吐或治疗效果提高；须说明成本与回病是否同时改变。
- weakened：吞吐、承载或控制下降但未完全停止。
- blocked：start gate 或关键 phase 关闭。
- reopened：原先 blocked／stalled 的 phase 恢复到 conditional／active。
- redirected：共享节点分配或主要去向改变。
- unchanged：经依赖传播检查后明确无影响；必须有继承收据。

## Effect Dimensions

- relation form：关系形式优先按克、合、并存或未决，不代表已经产生全部效果。
- target material effect：目标形质或库存的实质损伤。
- target functional effect：目标做功被压制、羁绊、占用或改道。
- third-party protective effect：另一节点是否因该作用而减压或得到保护。

四维分别使用 `none／low／medium／high／conditional／unknown` 并列证据。形式上作合可以仍有剩余做功或功能制约；对目标实损低也可以对第三方有保护效果。禁止从其中一维自动推导其余三维。

## Branch Relation State

- complete：形式齐全且通过裁决。
- partial：半合、半会或缺关键支。
- candidate：只存在组合可能。
- damaged：被冲、刑、空亡或共享支削弱。
- competing：与其他组合争用节点，未裁决。
- dormant：原局不主导，待岁运引动。

## Post-Branch Change State

- retained：关系裁决后保留原身份和主要功能。
- strengthened：同类聚拢或成势后可用度提高，但未必转化。
- concentrated：力量被聚到某一五行／中神，独立用途减少。
- bound：被六合、争合或合绊占用，独立起边能力下降。
- redirected：仍有库存，但主要输出方向改变。
- destabilized：受冲、刑、害、破或空亡影响，兑现不稳。
- damaged：根、库存或功能被实质削弱。
- transformed：只在流派条件完整且证据充分时使用。
- latent：保留为库存／根气，原局不允许直接做功。
- unchanged：完成检查但无关系造成的状态变化。

`clash-throughput`、`hidden-stem availability`、`storage-opening doctrine` 必须分别记录；不得用其中一个替代另外两个。

## Branch Manifestation Layer

- `field-present`：地支位置作为季节、空间、场景或容器仍在；场的质量可以 strengthened／concentrated／redirected／damaged，但不因藏干未透而被删除。
- `qi-participating`：逐藏干在 stock／root-support／environmental-feed／pattern-eligible／timing-only 中至少有一项经证据保留；不等于可以直接起边。
- `direct-function`：节点的 direct-action gate 与实际 edge／capacity 均通过；不等于已有现实载体或外部结果。
- `result-handoff`：只列可供 Topic Lens／Composition 继续桥接的 route、condition 与未决开关；Structure Core 不使用 `externalized-result` 裁生活结果。

visibility 与 manifestation 正交：`visible／hidden／latent` 只回答接口显隐；`stock／support／direct-action／external result` 分别回答参与方式、功能资格和现实兑现。禁止使用 `透＝用＝显` 或 `不透＝无` 的连锁映射。

取象层可使用以下非互斥模式：`field-background`、`stock-root-support`、`environmental-feed`、`internal-latent`、`direct-function`、`timing-pending`、`externalized-result`。前三层状态必须引用 Core；最后一项还须通过 topic carrier 与结果条件。

## Activation Interface State

- `registered-unmatched`：原局已登记可重算的待时接口，但本轮没有触发匹配。
- `matched-pending-requalification`：外来节点与接口签名匹配，正等待支局、节点与作用边重新裁决。
- `active-overlay`：只在本轮覆盖范围内通过重算；不改变原局身份。
- `blocked-overlay`：触发形式存在，但受制、占用、竞争、无承接或问题中心不调用而未放行。
- `expired-overlay`：时间窗或关系场结束，临时差分失效；原局接口仍为 registered-unmatched 或其冻结原态。

`natal_visibility` 是原局冻结事实，`overlay_visibility` 是当前时间／关系场的临时接口状态。后者可为 `activated-visible／activated-latent／unchanged`，不得反写前者。持续方式另记 `persistent-in-window／intermittent／pulse／relationship-bound`，不得把“激活”预设为渐进或突发。

## Edge Layer

- direct-action：节点对另一节点实际生、克、制、泄、合绊或改道。
- root-support：为天干或同类节点提供根气、同党和承载，不等于直接输出。
- environmental-feed：季节、方局、同气场或聚拢关系持续提供背景供给。
- branch-relation：合冲刑害破及会局造成的状态变换。
- composition-only：只说明同支组成／层级，禁止当作持续生克边。

同一条路线可以混合多种 edge layer，但必须逐段标明。删除 direct-action 不得自动删除 root-support 或 environmental-feed。

## System State

- stock：库存与根源。
- throughput：实际传输量。
- accumulation：力量聚集处。
- bottleneck：限制全路线的弱环。
- controller：能启动、改道或停止路线的节点。
- autonomous subsystem：不依赖日主直接驱动也可维持的链。
- feedback：输出回到上游并增强或削弱原状态。

禁止自创“百分之多少成局”等伪精确分数。使用高／中／低并列出证据。
