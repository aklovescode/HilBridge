---
name: fs-dev-plan
description: >-
  Produces an approval-ready implementation plan from user intent,
  staged or referenced spec/ notes, project context, and source evidence. Maps
  visible behavior through Vision, UI Surfaces, Flows, Modules, and Code;
  includes Contracts or cross-domain notes only when their durable boundary
  changes. Planning is read-only and does not edit workspace files.
---

# Full-stack Dev — Plan

## Goal

Produce a file-specific plan that can be implemented without reinterpreting
human intent.

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

Read `spec/conventions/Documentation_Conventions.md` and the affected path:

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
7. If the requested implementation needs human behavior absent from the
   authoritative human sections, surface the decision for approval; do not plan
   it only as Derived Delivery Guidance.
8. Tie each completion criterion to an observable result and exact narrow
   validation command, including project-declared documentation checks when
   specs change. Include failure/recovery cases relevant to the change.

## Output

Write the active plan with:

1. **Scope & Intent**
2. **Relevant Specs**
3. **Design Summary**
4. **Proposed Changes** — file-specific code, documentation, and tests
5. **Validation / Handoff**
6. **Risks / Gaps**

State dependencies, completion criteria, affected paths, and any external action
requiring separate authorization. Preserve the approved plan for a later session
using the project's handoff convention when requested; do not assume this permits
an otherwise prohibited workspace write. Omit speculative alternatives.
End with: **Ready for approval**
