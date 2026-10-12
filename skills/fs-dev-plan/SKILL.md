---
name: fs-dev-plan
description: >-
  Resolves intent and implementation questions before producing a development plan,
  including concrete tests and, for delegated delivery, subplans, ownership,
  dependencies, and execution authority. Uses user intent, specs, and source
  evidence. In Default mode, continues an authorized implementation request
  without a separate plan approval; planning-only requests stop at the plan.
---

# Full-stack Dev — Plan

## Goal

Produce a file-specific plan that can be implemented without reinterpreting
human intent.

## Collaboration Mode And Continuation

Check the runtime's declared collaboration mode. In **Default mode**, use the
read-only planning phases below, then continue an implementation request once
the plan is complete and necessary questions are resolved. Do not ask the user
to enter native Plan mode or approve the completed plan just to continue.

In **actual Plan mode**, honor its runtime restrictions, use its native planning
artifact, and stop before execution or workspace writes. This skill cannot
switch client modes. An implementation request resumes only after the runtime
actually permits execution; a manual mode change is distinct from plan approval.
If the mode cannot be verified, keep the work read-only and report that limitation.

## Clarification Before Implementation

Use three phases; return to an earlier phase when new evidence opens a material
decision. Do not treat Default mode's preference for assumptions as permission
to guess a consequential requirement.

1. **Explore the environment.** Resolve repo facts through targeted reads:
   current behavior, owners, interfaces, constraints, existing tests, and commands.
   Do not ask the user for facts the repository can establish. Ask early about
   an explicit contradiction in the request when exploration cannot resolve it.
2. **Clarify intent.** Establish the goal, success criteria, audience, scope,
   constraints, and meaningful preferences/tradeoffs. Ask before designing past
   an unresolved decision that changes user-visible behavior, compatibility,
   ownership, destructive impact, or material scope. Reuse existing answers.
3. **Clarify implementation.** Resolve interfaces, data flow, failure/edge cases,
   tests, and any applicable migration or rollout choices. Use existing patterns
   for routine engineering decisions; ask about consequential alternatives
   whose choice is not established by the project or accepted intent.

For each unknown, distinguish a discoverable fact, a required user decision,
and a low-risk optional preference. State the consequence of a required question,
offer meaningful options and a recommendation when useful, and wait for an actual
answer before dependent edits or child dispatch. Use an available question tool
within its tool constraints; an optional-only tool cannot carry a required
decision. If no suitable tool is available, ask directly and leave it pending.
Silence, a timeout, and a preselected option are not answers. Continue independent
read-only exploration while waiting.

Record resolved decisions, open questions, and evidence-backed low-risk assumptions
in the plan. No question quota is required: a well-specified task may need none.
Before handoff, check every material decision is resolved and the implementer
has concrete behavior, ownership, interfaces, and verification criteria.
For example, missing intent about searching titles versus note bodies needs a
question; choosing a helper name from existing conventions does not.

## Authority And Boundary

- Read specs, source, tests, task artifacts, and applicable reuse catalogs.
  During planning, change only the task-owned plan artifact in Default mode.
  Use project conventions and preserve unrelated plans; native Plan mode uses
  only its planning response. Do not edit source/specs, stage, or execute the
  proposed change until the planning phases are complete.
- Treat `## Human View` and Vision content above
  `## Derived Delivery Guidance` as product authority. Derived guidance supplies
  constraints and mappings but cannot expand that authority.
- An **authorized plan** is a completed plan within the user's implementation
  request and accepted decisions, or a plan the user explicitly approved.
  Preserve the request/decision reference with the plan; the agent's own plan
  cannot grant execution authority. Downstream skills accept either route and
  must not demand a separate approval milestone for unchanged scope.
- A planning-only request (including "plan only" or "do not implement") ends
  at the plan. Invoking this skill alone does not grant implementation authority.
  Resolve genuinely ambiguous execution intent without a ceremonial approval.
- Record local commit/integration/cleanup authority and external actions from
  the request and applicable project workflow. Do not infer push, deployment,
  destructive operations, or external writes from permission to implement.
  Ask for genuinely new material decisions or missing scoped authorization;
  reuse authorization and answers already given.

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
   and execution authority.
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
10. Check the plan against the clarification phases. For an authorized
    implementation request in Default mode, preserve the plan and continue
    immediately with the appropriate implementation workflow. This is a
    planning-phase handoff, not the end of the overall task.

## Delegated Delivery

Use `fs-dev-orchestrate` for authorized delegated delivery once planning is
complete. Use `fs-dev-implement` for standalone implementation.
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
authorization separately. The recorded task authority carries
through routine child handoffs and in-scope fixes; new material decisions return
to the user. Note resource limits or unavailable capabilities that affect delivery.

Make cleanup an explicit execution step and completion criterion. The parent
records the initial worktree inventory and every task-created path/identity.
After a child stops, verify its output is integrated and its commits, reports,
and needed artifacts are recoverable, then archive/remove its disposable
worktree. Keep checkouts still used for review, tests, or integration until their
work finishes. Verify no disposable task-created worktrees remain at handoff;
preserve unrelated worktrees and report any concrete cleanup blocker. Planning
only describes this cleanup; the execution parent performs it.

## Output

Write the active plan with:

1. **Scope & Intent**
2. **Relevant Specs**
3. **Design Summary**
4. **Proposed Changes** — code/docs and subplans with dependencies/ownership
5. **Test Plan** — cases, expected outcomes, fixtures/seams, paths, and commands
6. **Execution / Handoff** — roles, context, integration, review, authority source,
   and next action
7. **Risks / Gaps**

State dependencies, completion criteria, affected paths, and any external action
requiring separate authorization. Include only sections needed by the task;
do not force decomposition or new infrastructure for a small change.
For an authorized implementation request in Default mode, share a concise plan
update and continue; do not end with **Ready for approval** or ask "Shall I
implement?". For planning-only work, deliver the plan and stop. If a required
question remains, present that question instead of a supposedly complete plan.
In native Plan mode, output the native plan without claiming to exit that mode.
