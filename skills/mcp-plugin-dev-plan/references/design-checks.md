# MCP App design checks

Use only the sections relevant to the requested change. These are decision
prompts, not requirements to add every component to every plugin.

## Conversation and guidance

Model the shortest complete journey, including ordinary follow-ups without a new
app mention. Onboarding should ask for missing user choices, not expose resource
URIs, payload construction, or internal identifiers.

If the product is meant to work with the plugin alone, make essential guidance
available through server instructions, discoverable tool descriptions, or a
versioned guide tool/resource supported by the host. Do not hide required behavior
only in an optional uploaded skill. Reuse one guidance source for packaged and
served variants where feasible; retrieve substantial guide topics only as needed.

Keep the primary ordinary workflow, authorization boundary, and completion
contract easy to find. Put conditional procedures in focused references. For a
fragile operation or serialization choice, include one concrete supported request
example instead of more generic runtime teaching. Avoid competing copies of a
normative rule across descriptions, guide topics, and packaged skills; verify
their generated/served versions agree and reach the intended host configuration.

Guidance can explain behavior; it cannot guarantee model execution. For a preview
that must appear before confirmation, prefer attaching the UI resource to the
preview-producing tool. The host fetches the resource; an additional model-called
render tool is unnecessary unless the existing ownership boundary requires it.
Keep a complete text review path for unsupported or failed UI.

Specify when to show a receipt, a focused summary, or a broader review rather than
treating every response as the same dashboard. For a multi-part request, define
the complete result and respect an explicitly narrowed request.

## Tool and resource contracts

For each changed tool, decide its discovery wording, input and output schemas,
actual side effects, auth requirements, and model/app visibility. Define the
structured success result and actionable error behavior. Returning an object does
not prove that the SDK advertises an output schema; inspect serialized discovery.

Keep these channels intentional:

| Channel | Design decision |
|---|---|
| `content` | Human/model-readable result or useful fallback |
| `structuredContent` | Typed facts needed for reasoning and UI; match `outputSchema` |
| Result `_meta` | Component-only details when the host supports them; never secrets |
| Tool `_meta.ui.resourceUri` | Link the producing tool to its registered UI |

For each changed UI resource, check its URI, MIME type, bundled assets, domain,
CSP, and delivery through `resources/read`. In ChatGPT, `_meta.ui.domain` belongs
on resource contents and is a dedicated origin unique per plugin for submission;
multiple templates in that plugin may share it. Local development and submission
have different readiness requirements. Prefer standard fields, keeping aliases
only for supported compatibility needs. [OpenAI reference](https://developers.openai.com/plugins/reference)

Use the standard bridge for supported interactions. Define initial/loading,
success, empty, error, and stale states; determine whether data arrives through
tool input, tool result, or both. Handle host event timing and only combine payloads
belonging to the same operation. A successful acknowledgement is not proof of
rendering. [MCP Apps overview](https://modelcontextprotocol.io/extensions/apps/overview)

Choose accessible controls, responsive sizing, and local interactions for already
loaded data. Distinguish view state from business state. A refresh, older period,
or external action must retain its originating context and use the authorized
tool/connector path; it must not silently operate on a different active object.

## Data, mutations, and recovery

Choose an authoritative owner for identity, arithmetic, dates/timezones, period
boundaries, units/currency, and null-versus-zero semantics. Keep input compact;
avoid making the model construct several redundant fields that can contradict
each other. Normalize only unambiguous equivalents and return field-specific
validation feedback for genuine errors.

When the operation requires a preview/confirmation contract, present the exact
scope, changed/unchanged/excluded items, amounts or impact, and expiry before
confirmation. Bind apply to that preview and enforce auth, stale-state detection,
and retry semantics in the authoritative mutation owner. Tool annotations and widget
buttons do not enforce these rules. A help request or context answer does not
authorize saving newly proposed values; an explicit instruction to save specified
values may already supply the necessary authorization.

Keep an accepted proposal's identity, scope, values, and displayed precision
authoritative through apply and verification. A new or scaled proposal needs
the contract's required acceptance; unchanged accepted values do not need another
confirmation. Do not recompute a different payload from an earlier estimate.
For example, an accepted value of 0.27 must not silently become 0.2725 at save.
Specify duplicate prevention for repeated acceptance and absence of mutations for
declined or superseded proposals. State clearly when a display includes pending
data; neither rendering nor numeric validation proves persistence.

A renderer failure must never repeat a successful write. Repair a malformed
presentation payload from existing verified evidence where possible. Bound
retries; a timeout with uncertain write status requires readback or an idempotency
check before repeating the operation. Do not fabricate success to escape a loop.

## Performance and operations

Measure the journey before changing storage or hosting: model/tool turns,
connector calls, bytes, origin time, and end-to-end latency are separate metrics.
Prefer verified identity reuse, bounded/batched reads, compact projections or
native summaries, and local navigation over speculative infrastructure changes.
Preserve freshness, coverage, write verification, and invalidation after mutations.
Use a native write response as proof only when it contains the contract's required
identity, exact values/types, and source coverage/version. Otherwise plan targeted
readback. Do not require a redundant read or trust a generic acknowledgement.
For formula-backed sources, verify effective values and recalculation in the real
provider; local fixture arithmetic alone cannot prove them.

Public versioned guides and immutable assets may be cacheable. Do not blanket-cache
the MCP endpoint or personalized results; protocol request/session identifiers,
auth, POST/SSE behavior, errors, and user isolation make transport-level caching
a separate design problem. An edge runtime and a CDN cache are different choices.
Smaller payloads prove smaller payloads, not automatically lower latency.

Use programmatic calling only where the actual host supports it and predictable
bounded filtering, aggregation, or validation can return useful compact evidence.
Keep approval boundaries, native artifacts/citations, and write proof intact.
Do not assume it is newly enabled or that code orchestration automatically reduces
calls; measure actual use and outcomes. Count task operations, guide/discovery
calls, orchestration invocations, and resource requests separately.

For diagnosis, trace discovery → invocation → validation → result/resource →
bridge → render. Choose payload-free correlation, error stage, status, and timing
events when observability is needed. Avoid bodies, tokens, private identifiers,
and sensitive query strings in logs. Missing logs cannot prove no request arrived
if that stage is not instrumented.
