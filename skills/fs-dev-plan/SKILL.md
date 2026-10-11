---
name: fs-dev-plan
description: >-
  Produces an approval-ready development plan in actual Codex Plan mode,
  including concrete tests and, for delegated delivery, subplans, ownership,
  dependencies, and execution authority. Uses user intent, specs, and source
  evidence. Planning is read-only and does not edit workspace files.
---

# Full-stack Dev — Plan

## Goal

Produce a file-specific plan that can be implemented without reinterpreting
human intent.

## Plan Mode First

Check the runtime's declared collaboration mode before planning. Require actual
Plan mode; a prose plan, task checklist, or instruction saying "plan mode" does
not establish it. If the mode is Default or cannot be verified, explain this
requirement and ask the user to select Plan mode in the client. Do not pretend
to switch it or invoke implementation. Use a supported mode-control tool only
if one is actually exposed, then verify the resulting mode.

In Plan mode, use the native planning response/artifact and available question
tool. Do not save a workspace plan file during this read-only phase. After
approval and the switch to execution mode, the executor preserves that exact
approved plan using the project's handoff convention.

## Authority And Boundary

- Read specs, source, tests, task artifacts, and applicable reuse catalogs.
  Write only the tool’s active planning artifact.
- Treat `## Human View` and Vision content above
  `## Derived Delivery Guidance` as product authority. Derived guidance supplies
  constraints and mappings but cannot expand that authority.
- Ask only when a missing decision materially changes behavior, ownership,
  architecture, destructive impact, or scope. Otherwise make an evidence-backed
  assumption and record it.
- Reuse explicit decisions and approvals from the current task; do not ask for
  them again. A planning-only request still ends before implementation.
- Stop after an approval-ready plan. Do not edit code/specs, stage, commit,
  push, deploy, or perform destructive actions.

## Project Context

Read the target project's root and applicable path-local `AGENTS.md` first.
Use its stack, domain invariants, state ownership, paths, reuse catalogs,
discovery tools, checks, task-artifact conventions, and applicable migration
rules. Read project-local `PRODUCT.md` and `DESIGN.md` when relevant.

Vision-first paths below are defaults; honor project equivalents. Do not import
another project's assumptions or bootstrap missing layers, tools, or validators
unless requested. Use available request/source evidence when guidance is absent;
report missing required context or validation instead of claiming completeness.

## Required Context

Read the project's documentation conventions when present and the affected path:

```text
Visible capability:
Vision heading -> UI Surface -> Flow -> Module -> Code

Capability without UI:
Vision heading -> Technical Flow -> Module -> Code
```

Read relevant Contracts for durable data/API/sync/provider/fixture boundaries,
cross-domain notes for shared architecture/domain/security concerns, Operations
for runtime changes, and `spec/doc_issues.md` for known drift. Use the project's
discovery tools and direct reads/`rg` for exact evidence.

Read the reuse catalogs declared by the project, including applicable
path-local catalogs. Prefer an existing reusable owner.

## Architecture Constraints

- Apply the target project's architecture and domain constraints from
  `AGENTS.md` and the linked authoritative notes.
- Preserve declared state ownership and interface compatibility.
- Include only components and deployment surfaces that the project actually uses.

## Workflow

1. Establish the requested outcome, completion criteria, explicit exclusions,
   and approval boundary.
2. Read staged spec changes with `git diff --name-only --cached -- spec/` and
   every user-referenced note. If neither exists, use the request and current
   graph without inventing scope.
3. Follow Module/Contract `## Code` paths and inspect the current
   implementation, tests, dependencies, and reuse options.
4. Stop discovery when behavior, ownership, files, dependencies, risks,
   documentation effects, and validation are supported. Reuse inspected context
   while its checkout, source, requirements, and environment remain current.
5. Design the smallest coherent change. State interface, application logic,
   integration, persistence, migration, test, and operational work only when
   applicable.
6. Assign documentation changes by responsibility:
   - Vision for changed product intent.
   - UI Surface for changed visible behavior in place.
   - Flow for changed behavior through time and behavioral verification.
   - Module for changed program responsibility, code paths, and unit evidence.
   - Contract for a changed durable boundary.
   - Cross-domain, Operations, or test scenario for their owned knowledge.
7. If requested behavior is absent from the authoritative human sections,
   include the supplied intent and its owning spec update in the plan. Ask only
   for a still-missing material decision; do not introduce behavior solely in
   Derived Delivery Guidance or ask again for a decision already supplied.
8. Read [test design](../fs-test-plan/references/test-design.md) and include
   concrete test additions/updates, fixtures, testability seams, expected
   results, and exact commands. Include project-required checks. Do not hand
   off testing as "add tests later" or require a separate fs-test-plan approval.
9. For delegated delivery, use the decomposition and authority rules below.

## Delegated Delivery

Use `fs-dev-orchestrate` after approval when the user requests delegated delivery.
Split a large plan only along useful responsibility boundaries. Each subplan
needs acceptance criteria, owned paths, dependencies, agreed interfaces, and
relevant context beyond the plan. Keep tightly coupled edits with one child;
use dependency waves rather than parallel writers to the same file.

Assign production code, production testability hooks, and specific Module notes
to implementation children. Assign tests, fixtures, harness configuration,
shared documentation, and verification evidence to the parent. Children do not
author or run tests; list their allowed typecheck/build/documentation checks.
List deferred full-project checks for the parent if a subplan cannot run them
before its dependencies are integrated.

The execution section names the base/destination branch, local checkpoint
commits, integration branch, final commit strategy, independent review, test/fix
loop, and worktree cleanup. State any push/deployment or external action and its
authorization separately. Approval of this explicit execution scope carries
through routine child handoffs and in-scope fixes; new material decisions return
to the user. Note resource limits or unavailable capabilities that affect delivery.

## Output

Write the active plan with:

1. **Scope & Intent**
2. **Relevant Specs**
3. **Design Summary**
4. **Proposed Changes** — code/docs and subplans with dependencies/ownership
5. **Test Plan** — cases, expected outcomes, fixtures/seams, paths, and commands
6. **Execution / Handoff** — roles, context, integration, review, and authority
7. **Risks / Gaps**

State dependencies, completion criteria, affected paths, and any external action
requiring separate authorization. Include only sections needed by the task;
do not force decomposition or new infrastructure for a small change.
End with: **Ready for approval**
