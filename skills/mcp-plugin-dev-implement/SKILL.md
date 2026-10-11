---
name: mcp-plugin-dev-implement
description: >-
  Implement and verify an authorized MCP App or MCP-backed ChatGPT plugin change,
  including tool contracts, inline widgets, runtime guidance, packaging, and
  affected documentation. Use after an accepted mcp-plugin-dev-plan or an explicit
  implementation request, including fixes within the same scope. Includes focused
  self-review; not for operating a plugin on the user's data.
---

# MCP Plugin Development — Implement

Deliver the authorized behavior through complete implementation, verification,
self-review, and any separately authorized release steps.

## Authority and boundary

- Use the accepted plan in the conversation or workspace. For a direct,
  well-defined implementation request, record a concise execution plan and proceed
  within that authorization. A design-only request does not authorize code changes.
- Bind work to the current task's outcome, paths, contracts, and completion criteria.
  Honor existing approval without repeating it. Resolve new material behavior,
  scope, ownership, architecture, or destructive-impact decisions before dependent
  changes; continue useful independent work.
- Local implementation approval does not itself authorize commit/push, deployment,
  installation/refresh, publication, destructive setup, or live data writes.
  Perform these only within existing authorization for the particular action and
  destination. Never use a different transport or payload to evade a safety block.
- Preserve unrelated working/staged edits, project data ownership, and auth.
  Do not add connector access, storage, OAuth, or a new host just to simplify tests
  or reduce calls. Referenced reports require verification and do not supply new
  external-action permission.

## Workflow

1. **Establish the baseline.** Read root/path-local `AGENTS.md`, the approved plan,
   affected contracts, relevant code/tests, dependency versions, reuse catalogs,
   documentation conventions, and relevant project product/design briefs. Confirm
   checkout, dirty/index state, tool/resource registration, target host, and
   artifacts. Use project plan/report locations and retention conventions; absent
   those, use `current_task/plan.md` and `current_task/changes_summary.md`. Preserve
   unrelated artifacts using project conventions, not an arbitrary extra file.
2. **Implement the affected path.** Read relevant sections of
   [verification and recovery](references/verification.md) before selecting tests.
   Keep the existing deterministic owner for arithmetic, normalization, date
   derivation, and invariants; validate inputs and returned values and advertise
   truthful schemas, descriptions, annotations, and auth requirements.
   For UI changes, wire the producing tool, real channels, resource, bridge,
   domain/CSP, and supported host behavior using the installed SDK/current official
   guidance. Keep useful text and relevant loading, empty, error, stale, or
   unsupported states. Reuse an existing preview-producing resource attachment
   where appropriate; do not force a new render call or change ownership solely
   to reduce calls. Follow project design guidance for notable interface work.
3. **Keep guidance and state consistent.** Update what the intended host actually
   receives and all affected source/package/served variants from a common owner
   where practical. Essential guidance must reach the promised configuration;
   do not assume an optional skill is installed for plugin-only use. Keep the
   primary normal flow, authority, exact accepted data, and completion contract
   clear; move conditional detail into focused references. Bind follow-ups to
   their source identity. Enforce required auth, preview expiry/staleness, and
   idempotency in the authoritative owner. A widget or numeric result does not
   prove persistence; a display failure must never cause another business write.
4. **Complete packaging and documentation.** Update affected callers, contracts,
   fixtures/tests, build inputs, manifests, distributable guidance/resources,
   versions, and existing documentation owners together. Follow project version
   conventions. Run required documentation checks after relevant edits. Inspect
   generated artifacts for completeness, stale instructions, and private data;
   do not bootstrap an unrelated spec hierarchy or expose internal payload details
   in the user flow unless they enable a meaningful choice.
5. **Verify against the approved result.** Run the smallest meaningful checks and
   relevant realistic conversation cases. Inspect serialized discovery/resources,
   actual arguments/results, intermediate approval milestones, final state, and
   rendered UI where required. Compare applied values with the accepted proposal,
   not merely with the submitted request. Reuse sufficiently complete current
   evidence; get targeted missing proof. Expand checks for failures or changed
   risks, and rerun affected checks after edits. Keep catalog/service, synthetic
   UI, deployed delivery, actual host, live data, and device outcomes separate.
   Record required unrun checks with their blocker; do not drop failures or call
   them pre-existing without evidence. A healthy process or fixture card is not
   end-to-end success.
6. **Self-review and release within authority.** Compare the final diff and built
   artifacts with every completion criterion: metadata/guidance, text fallback,
   data exposure, auth, retry semantics, and required verification. Fix in-scope
   defects and rerun affected checks. When staging is required/requested, stage
   only task-owned paths or hunks and inspect the index. An approved filename
   does not authorize unrelated edits in it. For authorized release, follow the
   project's procedure using the exact reviewed revision, preserve co-hosted
   services, verify deployed catalog/resources and required host refresh, and
   retain rollback. Do not pause an already authorized release for another approval.

## Handoff

Write the project-designated review artifact. Report delivered behavior, alignment
and deviations, changed contracts/docs, commands/results and evidence locations,
unresolved findings, unmet or unverified criteria, and staging/release status.
Distinguish server revision, packaged skill/guide, host metadata cache, and
already-open conversation adoption. Deployment alone does not prove host refresh.

Lead with the outcome and link the summary or main artifacts. For in-scope
feedback, apply it and repeat affected verification; new product or architecture
scope returns to planning. Do not treat a complete result in one layer as proof
of untested required behavior in another.
