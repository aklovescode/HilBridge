---
name: fs-dev-doc
description: >-
  Creates or updates project specifications under spec/ using concise
  capability intentions inside Vision, detailed UI Surface notes for visible
  behavior, PlantUML Flow notes for behavior through time, Modules for program
  design, and optional Contracts or cross-domain notes for durable shared
  knowledge. Also documents conversational-agent surfaces, MCP/tool flows,
  widgets, and derived agent skills without making host packaging a source of
  product truth. Use for documentation-first work, documentation graph
  maintenance, UI-to-implementation traceability, explicitly requested
  cross-layer review slices, technical flows without a UI, verification
  mapping, or when the user invokes fs-dev-doc.
---

# Vision-first Spec Documentation

Keep the documentation easy for a human to review against the original intent
and precise enough for an agent to deliver without inventing behavior.

## Project Context

Read the target project's root `AGENTS.md` and any applicable path-local
`AGENTS.md` before applying this workflow. Take the technology stack, domain
invariants, state ownership, repository layout, reuse catalogs, discovery tools,
validation commands, and temporary migration rules from that project context.
Do not infer them from the repository where this skill is installed.

The paths below describe the default Vision-first documentation layout. Follow
project-declared equivalents for documentation and task artifacts. Read existing
conventions when present; do not bootstrap missing layers, tools, or validators
unless the request requires them. If project guidance is absent, use the current
request and repository evidence, and record material gaps rather than importing
another project's assumptions. Run applicable available checks and report any
missing validation.

## Boundary

- Default to one requested documentation layer under `spec/`. When the user
  explicitly names a connected cross-layer review slice, author exactly those
  layers in authority order and stop at the last named layer. Do not infer
  Contracts, Modules, scenarios, operations, or implementation merely to make
  the slice appear complete.
- Do not modify application code. Edit documentation tooling or this skill only
  when the user explicitly requests that maintenance.
- Inspect nearby specs and source code when needed for accuracy. Source code is
  evidence of the implementation, not authority for intended product behavior.
- Keep capability intent in `spec/Vision.md`. Do not create a standalone
  capability note unless the user explicitly requests one.
- Run non-destructive validation after edits.
- Ask only when a missing decision would materially change human intent,
  ownership, or the documentation graph.

## Documentation Graph

Capabilities are concise sections inside `spec/Vision.md`, not a separate
mandatory note layer.

```text
User-visible capability:
Vision capability intent -> UI Surface -> Flow -> Module -> Code

Capability without a UI:
Vision capability intent -> Technical Flow -> Module -> Code

Conversational-agent capability:
Vision capability intent -> Agent UI Surface -> User Flow
User Flow -> Tool Technical Flow -> Contract/Module -> Code

Durable boundary when useful:
Flow/Module -> Contract -> Code

Shared knowledge:
Any note or subsection -> Cross-domain note or subsection
```

These are navigation paths, not one-to-one hierarchies. A surface can support
several capabilities and flows; a flow can cross several surfaces and modules.
An Agent UI Surface is still a UI Surface: it owns the conversation, embedded
views, confirmations, and visible host degradation a person experiences. A
Tool Technical Flow owns the host-to-tool sequence through time, not the
tool's durable schema. Use direct relative Markdown links, including heading
fragments, to express the actual many-to-many graph.

Cross-domain notes contain shared domain models, non-functional requirements,
technical architecture, security, sync, or other knowledge that should not be
owned by one capability. Link them from any relevant note or subsection. They
may contain higher-level PlantUML diagrams such as context, component, data
ownership, or state diagrams. Do not route all cross-domain knowledge through a
single hub merely to satisfy the graph.

Operations remain a related graph for deployment facts and procedures:
`Deployment Architecture -> Environments -> Runbooks -> Operational Facts`.

Core locations are `spec/Vision.md`, `spec/UI/`, `spec/flows/`,
`spec/modules/`, `spec/contracts/`, `spec/architecture_notes/`,
`spec/operations/`, `spec/test_scenarios/`, `spec/conventions/`, and
`spec/doc_issues.md`. Add a more focused cross-domain directory only when the
reviewed information warrants it; the semantic responsibility matters more
than the folder name.

## Human Authority And Derived Guidance

Every product/spec note has two authority bands:

1. The upper human part states the intent or design a human should review.
2. `## Derived Delivery Guidance` follows it and translates that human part
   into instructions useful to an agent.

In `Vision.md`, all product and capability content above
`## Derived Delivery Guidance` is the human part. Every other product/spec note
starts with `## Human View` and places `## Derived Delivery Guidance` below the
complete human part.

The human part is authoritative. Apply these derivation rules:

- Derive each delivery instruction from a specific statement or heading in the
  same human part. The human part may adopt a directly linked authoritative
  Vision, cross-domain, or Contract statement, but it must say which linked
  requirement applies; the delivery section cannot silently import it.
- Use links to exact headings for traceability. Add short stable identifiers
  only when headings are not precise enough.
- Delivery guidance may specify boundaries, prohibited approaches, state or
  data ownership, implementation mapping, verification, and stopping points.
  It must not add a visible behavior, business rule, outcome, or exception.
- If guidance cannot be traced to human intent, first add or clarify the human
  statement and stop for review. Do not hide a product decision in agent
  instructions.
- When implementation and human intent differ, preserve the human intent and
  record the drift in `spec/doc_issues.md`.
- Prefer links over repeated generic rules. A linked cross-domain statement is
  still a valid derivation source.
- Treat executable agent skills, host manifests, tool descriptions, and widget
  bundles as derived delivery artifacts. They may summarize or package
  reviewed intent, semantics, and workflows, but they must not become the only
  authority for a product meaning or user-visible guarantee.

## Note Responsibilities

### Vision And Capability Intent

Keep `spec/Vision.md` concise enough to read as one connected product story.
Each capability subsection should state only:

- the human outcome or need;
- the minimum durable domain or product constraints needed to preserve its
  meaning;
- links to its UI surfaces, or directly to technical flows when it has no UI;
- links to relevant cross-domain notes or contracts.

Do not use a standard scope/non-scope template. Do not put screen layout,
interaction sequences, implementation design, stopping rules, or test
inventories in a capability subsection. Add a non-goal only when omitting it
would make the intended outcome materially ambiguous.

### UI Surface

A UI Surface describes behavior in place: the concrete product surface a human
sees and reviews. Its human part may be intentionally detailed.

Describe the surface in visible order, using sections and subsections that match
the interface. State, where relevant:

- the purpose and entry points;
- each visible section, subsection, control, label, value, and explanatory
  content;
- what actions are available and the immediate visible response;
- navigation affordances and the context handed to another surface;
- loading, empty, error, offline, permission, and disabled states that are
  specific to this surface;
- visible privacy, accessibility, localization, and responsive behavior.

Keep cross-surface sequences in Flow notes, durable metric/data semantics in
Contracts or cross-domain notes, and widget/provider/file ownership in Modules.
Link the surface to the capability headings it realizes, its flows, and its
implementing modules.

For an Agent UI Surface:

- describe the visible conversation before host-specific chrome;
- state what context, evidence, uncertainty, explanation, proposed action, and
  confirmation the person sees;
- document an inline widget or other rich response as part of the visible
  surface, while leaving its resource protocol and code ownership to a
  Contract or Module;
- define an equivalent useful text/structured fallback when a supported host
  cannot render the rich response;
- keep common behavior host-neutral and add host subsections or separate
  surfaces only for material visible differences;
- keep model reasoning, prompt internals, tool schemas, and host packaging out
  of the human-visible sequence.

### Flow

A Flow describes behavior through time. Use a user flow for behavior a person
initiates or observes, and a technical flow for non-UI behavior such as
database synchronization.

The human part states the trigger, meaningful progression, outcomes, and
human-relevant failure or recovery behavior. Include a concise PlantUML
activity/flow diagram. A capability without a UI must link directly from its
Vision subsection to a technical Flow note with this diagram.

Use sequence or state diagrams only when they communicate the human-approved
behavior more clearly; a technical component design belongs in a cross-domain
technical architecture note or Module, not in the human journey.

For agent integrations, use a user Flow for the person's investigation,
explanation, correction, or confirmation journey. Use a separate Tool
Technical Flow when reviewers need to see authentication, tool selection,
authorized query execution, structured results, optional rendering, preview,
confirmation, and mutation through time. Do not prescribe hidden chain of
thought. Document observable requests, decisions, results, and recovery.

Flows own behavioral verification:

- state whether SIT/integration is sufficient, E2E is required, both are
  useful, or verification is not applicable;
- link exact runnable evidence or mark the missing coverage `Backlog`;
- keep detailed multi-flow E2E journeys in `spec/test_scenarios/` with
  bidirectional links to every exercised flow.

### Module

A Module connects the approved behavior to program design. Its human part
explains the responsibility boundary, collaborators, owned state/data, and
important inputs and outputs in terms a technical human can review.

Derived guidance may identify providers, widgets, queries, services, files,
implementation constraints, and exact unit/widget/server-unit evidence.
Modules that own implementation traceability list repo-relative paths under
`## Code`. Link each module back to the surfaces and flows it implements.

For agent integrations, Modules own MCP gateways, semantic-query execution,
widget resources, host packaging, and executable agent skills. A portable
gateway or widget may serve several hosts; keep host-specific manifests,
extensions, and distribution adapters thin and separately identifiable.

### Contract

Create a Contract only for a durable data, API, sync, external-provider,
fixture/artifact, or infrastructure boundary.

Its human part owns the domain meaning, ownership, invariants, lifecycle, and
compatibility expectations. Derived guidance may specify exact wire/schema
representations, serialization, persistence, sync handling, source paths, and
boundary verification. Do not create a Contract merely to complete the graph.

For agent integrations, create Contracts only when the reviewed slice needs a
stable semantic-query language, tool input/output boundary, authorization
scope, result lineage, widget payload, or write-confirmation protocol. Tool
names and schemas belong here when durable; model-facing usage guidance belongs
in derived skills and descriptions.

### Cross-Domain Notes

Use a cross-domain note when knowledge applies across capabilities or when a
domain model, non-functional concern, or technical architecture deserves a
stable shared explanation.

Keep the human part concrete enough for architecture review. Higher-level
PlantUML context, component, data ownership, state, or lifecycle diagrams are
appropriate. Derived guidance must remain traceable to that explanation.
Consumers may link directly to the relevant subsection; the cross-domain note
does not need a manually maintained list of every inbound link.

### Operations And Test Scenarios

- Operations notes own deployment topology, environment facts, procedures,
  release checklists, incident guidance, and operational validation.
- Test scenarios own detailed multi-flow E2E setup, steps, assertions, and
  artifacts. Scenarios link to the relevant Vision capability headings and
  every exercised flow.

## Verification Ownership

- Vision capability subsections contain no test inventory. Their linked flows
  provide behavioral coverage.
- UI Surfaces state visible acceptance intent but link to Flow or Module
  evidence instead of duplicating commands.
- Flows own SIT/integration/E2E decisions and runnable behavioral evidence.
- Agent user Flows own conversation/evaluation cases; Tool Technical Flows own
  host/tool integration and authorization cases.
- Modules own unit/widget/server-unit evidence and commands.
- Contracts own boundary/serialization/sync evidence.
- Operations own runbook and operational evidence.

Classify evidence by the behavior it proves, not by its framework or directory.
Keep each exact command in one owning note and link to it elsewhere.

## Incremental Workflow

### 1. Discover

- Read the request and every referenced file.
- Read `spec/architecture_notes/Cross_Cutting_Concerns.md` and
  `spec/conventions/Documentation_Conventions.md` when present and relevant.
- Use project-configured semantic discovery when available, then direct reads
  and `rg` for exact notes and paths.
- For third-party agent hosts, verify current protocol, authentication, UI, and
  skill support in official provider documentation before asserting it.
- Inspect source only when implementation mapping, drift, or code references
  matter.

### 2. Select The Reviewed Scope

Default to one layer:

1. **Vision:** consolidate concise capability intent and add forward links or
   placeholders; do not author Surface, Flow, or Module detail.
2. **UI Surface:** for visible capabilities, verbalize the interface precisely
   and add links; do not expand cross-screen flows or program design.
3. **Flow:** author user flows after their surfaces, or technical flows directly
   after Vision for capabilities without a UI; include PlantUML.
4. **Cross-domain/Contract:** extract shared meaning or durable boundaries when
   the reviewed upper layers require them.
5. **Module:** connect reviewed behavior to program design and code.

Cross-domain notes can be linked or refined at any layer when they are the true
authority, but do not use that flexibility to bypass review of changed human
intent.

When the user explicitly requests a connected slice such as
`Vision -> Agent UI Surface -> user/tool Flows`, work top-down through exactly
that list. Keep each note within its normal responsibility, use direct links
between the authored layers, mark unrequested lower-layer implementation or
verification as `Backlog`, and stop at the final requested layer. A connected
slice is an explicit exception to the one-layer default, not permission to
cascade into Contracts, Modules, code, or distribution.

### 3. Place And Edit

- Put each statement in the owning note type defined above.
- Keep the requested layer atomic and prefer links over repeated knowledge.
- When moving misplaced knowledge between current notes, establish its new
  authoritative home before removing the duplicate.
- Record unresolved conflicts, drift, and missing traceability in
  `spec/doc_issues.md`.

### 4. Stop For Review

After the requested layer or explicit slice:

- verify every Derived Delivery Guidance item is traceable to human intent;
- add only the forward links needed to make the next layer discoverable;
- report ambiguities or drift instead of resolving product decisions in lower
  layers;
- stop and finish with `Ready for review of <layer or slice>`.

Do not cascade into the next layer merely because its shape appears obvious.

### 5. Validate

After spec edits:

- run the documentation checks declared by the project; report unavailable
  validators or diagram runtimes and any resulting verification gaps;
- check relative links, heading fragments, source paths, and PlantUML blocks;
- check that every changed note has a human part followed by strictly derived
  delivery guidance;
- check that visible capability headings reach a UI Surface and non-UI
  capability headings reach a technical Flow;
- check that Agent UI Surfaces reach their user and Tool Technical Flows, and
  that supported hosts retain useful behavior without a rich widget;
- check Flow/scenario links are bidirectional and verification commands live
  only with their owner.

Finish with the documents changed, validation evidence, material gaps, and the
next review layer. Omit generic process narration.

## Relationship To Other Development Skills

- `fs-dev-ideate`: supplies product ideas; place approved capability intent in
  Vision rather than creating new standalone capability notes.
- `fs-dev-plan`: reads the reviewed documentation graph to create an
  implementation plan.
- `fs-dev-implement` / `fs-dev-iterate`: update code and affected documentation
  without changing human intent implicitly.
- `fs-dev-review`: audits staged implementation against the reviewed human
  intent and its derived guidance.
