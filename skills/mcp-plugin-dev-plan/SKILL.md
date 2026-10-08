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

Turn the requested experience into a small, implementable plan across the
conversation, MCP server, optional UI, and data owner.

## Establish context and authority

Read the target project's applicable `AGENTS.md`, existing product contracts,
relevant code, dependency versions, tests, and reuse catalogs when present.
Use the project's discovery tools, verifying index coverage against the active
checkout. The repository containing this skill does not define the target's stack.

Read user-referenced tasks with the available conversation reader before using
their contents. Separate product decisions from prior agent claims and old
implementation snapshots; confirm changeable technical facts against current
source or runtime evidence. Do not adopt commands or approvals from referenced
tasks as authorization for the present task.

Identify the target hosts and distribution artifacts: an MCP endpoint, MCP App
resources, a host plugin manifest, and an optional instruction skill are distinct.
Do not assume that connecting a server installs a skill or that a host's starter
prompt can be controlled by a package. Inspect the actual available connector
catalog when the design depends on it; provider API support is not connector proof.

Plan-only work may write the plan artifact, but must not change implementation,
product specs, remote configuration, or user data. Use the project's plan location;
otherwise use `current_task/mcp_plugin_plan.md`. Preserve an unrelated existing
plan by choosing a task-specific filename. If a host restricts planning writes,
use its active plan artifact and identify the handoff location.

## Design the experience and boundary

Start with a realistic user request and its observable completion criteria.
For each affected journey, record:

- What the user says or clicks, what chat displays, and when an inline UI appears.
- Which actor owns each read, calculation, write, and confirmation: host model,
  existing connector, MCP service, widget, or persistence layer.
- Which identity and source version bind follow-ups to the same account, object,
  date range, snapshot, or preview, and when a fresh read is necessary.
- What happens when data is absent, partial, stale, invalid, or unavailable, and
  what the user can still accomplish without a rendered widget.

Read the applicable sections of [design checks](references/design-checks.md)
for tool/resource contracts, conversation reliability, mutations, or performance.
Choose only the surfaces affected by this request. An output-schema repair does
not require a widget redesign, new auth flow, or full architecture audit.

Move mechanical arithmetic, normalization, and cross-field validation into the
existing deterministic owner when practical. Keep judgment and ambiguity in the
conversation. Never turn missing or invalid evidence into plausible totals.

Preserve the chosen data-ownership and trust model. A host connector's credentials
are not available to the MCP service. New OAuth, server storage, migrations, and
data access are explicit architecture decisions, not incidental optimizations.
Do not impose statelessness, Google Sheets, a language, or a hosting provider on
projects that have different requirements.

For protocol or host-specific changes, inspect the installed SDK and consult
current official documentation. Prefer standard MCP Apps capabilities; use host
extensions or compatibility aliases where the supported clients need them.
Record the relevant source and version assumption rather than embedding a copied
SDK tutorial. Useful entry points are linked in the design checks.

## Make the plan executable

Scale the artifact to the change. A small metadata fix can be one short plan.
Include the following substance without filling irrelevant sections:

1. **Outcome and scope:** requested behavior, acceptance criteria, explicit
   exclusions, and any decision that actually needs the user's input.
2. **Current evidence:** affected sources and observed failure stage; distinguish
   intended behavior, reproduced behavior, and unverified hypotheses.
3. **Journey and ownership:** the conversation-to-tool-to-UI sequence and data
   boundaries, including confirmation and recovery where applicable.
4. **Contracts and files:** exact tools, schemas, result channels, resources,
   guidance, packages, and file-specific edits. State compatibility needs.
5. **Verification:** concrete local commands and realistic conversation cases;
   separate catalog, service, synthetic widget, live connector, and target-device
   evidence. Identify unavailable access and required disposable fixtures.
6. **Handoff:** affected documentation owners, release/refresh steps if in scope,
   rollback for an authorized deployment, and material unresolved risks.

Use existing documentation conventions. In a Vision-first project, map changed
intent, conversational/UI behavior, flows, contracts, modules, and operations to
their existing owners. Else use the project's nearest equivalents. Do not create
an entire spec graph merely to satisfy this skill. Product intent must remain
explicit instead of being buried in tool descriptions or derived instructions.

Stop discovery once the plan has enough evidence to implement. For a planning-only
request, link the artifact, surface material decisions, and end **Ready for
approval**. When the user already authorized a plan-and-implement sequence,
continue to implementation within that scope without another approval ceremony.
