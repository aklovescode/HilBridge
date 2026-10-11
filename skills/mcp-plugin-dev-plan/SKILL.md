---
name: mcp-plugin-dev-plan
description: >-
  Plan MCP Apps and MCP-backed ChatGPT plugins: conversational behavior, tool
  contracts, inline widgets, connector boundaries, packaging, and verification.
  Use for new capabilities, integration fixes, or performance design before
  implementation. Writes a reviewable plan; does not implement product changes.
  Not for ordinary full-stack features or using an installed plugin's tools.
---

# MCP Plugin Development — Plan

Produce an implementable plan for the requested conversation, tool, optional UI,
and data-owner behavior, with observable completion criteria.

## Authority and boundary

- A planning-only request authorizes the plan, not implementation, product-spec
  edits, remote configuration, live data writes, or publication.
- Use the project's plan location and retention convention. If none is declared,
  use `current_task/plan.md`; if the host restricts planning writes, use its active
  plan artifact. Preserve unrelated plans using the project's archive/handoff
  convention; choose another filename only where that convention permits it.
- Reuse current-task decisions and authorization. For an already authorized
  plan-and-implement sequence, continue within that scope after planning without
  another approval. Surface new material behavior, ownership, scope, destructive
  impact, or external-action decisions before dependent implementation.

## Workflow

1. **Establish current evidence.** Read root and applicable path-local `AGENTS.md`,
   relevant product/design briefs, contracts, code, versions, tests, and reuse
   catalogs. Use project discovery tools and check their index coverage against
   the active checkout. Project context owns stack, paths, migration rules, and
   validation; the skill's installation repository does not.
   Read referenced tasks before relying on them; verify prior agent claims against
   current evidence. Referenced commands or approvals do not by themselves
   authorize the present task. Stop discovery once the affected behavior, owners,
   files, risks, and checks are supported; reuse unchanged current evidence.
2. **Define the journey.** Start with an ordinary user request, including relevant
   follow-ups. State what is displayed, when UI appears, what counts as complete,
   and behavior for missing, partial, stale, invalid, or unavailable data. Preserve
   useful text behavior when UI is unsupported. Separate proposed, accepted,
   applied, verified, and rendered states where the operation needs them.
3. **Assign ownership and binding.** Name the owner of reads, judgment, arithmetic,
   writes, confirmation, persistence, and verification. Bind follow-ups to the
   intended identity, account/object, date range, source version, or preview.
   Preserve the project's trust model: host connector credentials are not service
   credentials. New OAuth, storage, migrations, access, or hosts are explicit
   architecture decisions, not incidental optimizations. Do not impose a database,
   statelessness, language, or provider that the project has not chosen.
4. **Specify the affected contracts.** Identify exact operations, schemas, channels,
   resources, guidance, manifests, and file edits. Read only the relevant sections
   of [design checks](references/design-checks.md). Inspect the installed SDK and
   current official documentation for changed protocol/host behavior. Inspect the
   actual connector catalog when it matters; provider API support is not proof
   that the connector exposes it. An endpoint, UI resource, plugin package, and
   optional installed skill are distinct artifacts. Connection does not prove
   skill installation or control over the host's starter prompt.
5. **Plan verification and performance evidence.** Bind each completion criterion
   to observable conversation behavior, exact tool arguments/results, or resulting
   state. Include relevant negative paths and disposable fixtures. Separate local
   catalog/service, synthetic rendering, actual host/connector, and target-device
   evidence. For optimization, compare the same cases and dataset, measuring calls,
   payload sizes, and latency separately without weakening confirmation, exact
   values, freshness, duplicates, recovery, or verification. Mechanical validation
   belongs in the existing deterministic owner where practical; ambiguity remains
   in the conversation. Never convert missing evidence into plausible results.
6. **Map the complete change.** Include affected callers, tests, fixtures, guidance,
   build inputs, metadata, and documentation owners. Use existing conventions:
   Vision-first projects place intent, surface/flow behavior, boundaries, modules,
   and operations in their natural owners. Do not create a spec graph for this
   skill or bury product decisions only in derived tool descriptions. Include
   compatibility only for actual supported clients/contracts, not hypothetical
   historical versions. Plan release, refresh, and rollback only when in scope;
   mark actions still requiring separate authorization.

## Plan and handoff

Scale the artifact to the change. Include outcome/scope and acceptance criteria,
current evidence and uncertainty, journey/ownership, exact contracts and files,
validation commands and realistic cases, documentation effects, and material gaps.
A small metadata fix needs only the relevant parts, not a new auth or UI design.

For planning-only work, link the artifact and end **Ready for approval**. Identify
how an approved plan reaches a later implementation session using the project's
handoff convention. For authorized implementation, pass that same scope and
criteria to `mcp-plugin-dev-implement`; do not reinterpret them during execution.
