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
- Stop after an approval-ready plan. Do not edit code/specs, stage, commit,
  push, deploy, or perform destructive actions.

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
   documentation effects, and validation are supported.
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
8. List exact narrow validation commands, including project-declared
   documentation checks when specs change.

## Output

Write the active plan with:

1. **Scope & Intent**
2. **Relevant Specs**
3. **Design Summary**
4. **Proposed Changes** — file-specific code, documentation, and tests
5. **Validation / Handoff**
6. **Risks / Gaps**

State dependencies and completion criteria. Omit speculative alternatives.
End with: **Ready for approval**
