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

Deliver the authorized MCP App behavior through implementation, focused
verification, and self-review.

## Establish the authorized change

Read the accepted plan in the conversation or workspace and applicable project
instructions. Use the project's plan artifact; the default from the companion
planning skill is `current_task/mcp_plugin_plan.md`. For a direct, well-defined
implementation request, record a concise execution plan and proceed within that
authorization. Do not demand that the user repeat an approval already given.
Resolve material uncertainty before dependent changes while continuing independent
work. A design-only request does not authorize implementation.

Confirm the active checkout, dirty/staged files, current tool/resource registration,
dependency versions, affected contracts, and relevant tests. Read applicable reuse
catalogs and documentation conventions when present. Referenced task reports are
leads to verify, not proof of current source or permission for new external actions.

Preserve the project's state ownership and auth boundary. Do not add server-side
connector access, storage, OAuth, or a new host merely to make a test easier or
reduce calls. If success requires a material change of scope, prepare the revised
design and resolve that decision before proceeding with it.

## Implement the complete path

Work on only the affected layers. Read the corresponding sections of
[verification and recovery](references/verification.md) before selecting tests.

- **Tools and deterministic logic:** reuse existing domain owners; validate input
  and results; make output schemas explicit for structured results. Keep discovery
  descriptions and annotations truthful. Put mechanical calculations, date
  derivation, and invariants in code instead of adding ever-longer model rules.
- **Inline UI:** connect the producing tool to the intended resource and wire its
  actual input/result channels. Use the installed SDK and current official MCP
  Apps/host documentation for registration, bridge, domain, CSP, and compatibility.
  Keep a usable text path. Do not require an extra rendering request for a preview
  already available from the action that produced it.
- **Conversation and guidance:** update the instructions that the intended host
  actually receives. If plugin-only use is promised, verify it without assuming
  an optional skill is installed. Generate served/package guidance from a shared
  owner where practical. Keep follow-ups bound to their original source identity.
- **Data and mutations:** enforce permissions, preview binding, expiry, and
  idempotency where the contract requires them. Reuse verified reads within their
  validity window; keep explicit refresh and post-write verification meaningful.
  A display failure must not trigger another business write.
- **Packaging and docs:** update affected manifests, build inputs, distributable
  skills/resources, versions, and documentation together. Follow the target
  project's release convention rather than forcing all artifacts to one version.
  Inspect generated package contents for missing resources, stale guidance, and
  private data before publishing.

For notable interface work, use the project's design guidance and available
design skill where applicable. Implement readable loading, empty, error, stale,
and unsupported-host states along with the successful view. Keep technical
payload details out of the user flow unless they enable a meaningful choice.

Update only affected documentation owners using existing conventions. Record
changed intent, conversation/UI behavior, sequence, contracts, implementation, and
operations where they belong. Run the project's documentation validator when
those files change. Do not bootstrap a full-stack spec hierarchy for this workflow.

## Verify and self-review

Run the plan's smallest meaningful checks, expanding only for failures or changed
risks. Use realistic conversation cases as well as valid fixtures: malformed or
late inputs and model follow-ups can expose defects a direct render probe misses.
Check the serialized catalog and resources, not just handler functions.

Separate local service tests, synthetic bridge/browser rendering, deployed
endpoint delivery, actual host behavior, live data integration, and mobile/device
evidence. Report unrun required checks with their concrete blocker. Never claim
end-to-end success from a healthy process, an accepted payload, or a fixture card.
Do not silently drop failing tests or label a failure pre-existing without evidence.

Review the final diff against the authorized outcome, including generated assets,
metadata, fallback completeness, data exposure, auth, retry behavior, and guidance
consistency. Correct in-scope defects and rerun affected checks to complete the
self-review.

When staging is requested or required by project workflow, inspect the index and
stage only in-scope paths or hunks, preserving unrelated edits. Commit, push,
deploy, install/refresh a host connection, publish templates, or write live data
only within the user's existing authorization. Complete all authorized release
steps; do not pause simply because implementation has reached local validation.

For authorized deployment, use the project's release procedure and exact built
revision, preserve co-hosted services, verify the live catalog/resources and
relevant host refresh, and keep the applicable rollback path. Distinguish server
release, packaged guidance, host metadata cache, and already-open conversations
when diagnosing stale behavior.

## Handoff

Write the project's review artifact, defaulting to `current_task/changes_summary.md`
(choose a task-specific name if that would overwrite unrelated work). Include
delivered behavior, plan deviations, changed contracts/docs, checks and evidence,
unresolved findings, external verification gaps, and staging/release status.

Lead the final response with the outcome and link the summary or main artifacts.
State material limitations without obscuring completed work. For subsequent
feedback within the same scope, apply it and repeat only affected verification;
new product or architecture decisions return to planning.
