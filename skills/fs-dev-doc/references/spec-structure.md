# Specification structure and responsibility

Read the graph when choosing links, then the responsibility section for the
requested note type. Read verification ownership when adding or moving evidence.
These are defaults for Vision-first projects; follow project-declared equivalents.
The graph describes ownership and navigation, not permission to author every layer.

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
