---
name: fs-dev-implement
description: >-
  Implements an explicitly approved implementation plan, including in-scope code,
  tests, reuse catalogs, and affected Vision-first spec notes; runs relevant
  non-destructive validation and stages only the planned paths. Use after
  fs-dev-plan or fs-dev-investigate approval, then hand off to fs-dev-review.
---

# Full-stack Dev — Implement

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

Deliver the approved outcome completely without changing its product intent or
expanding its scope.

## Authority And Approval Boundary

- Require the approved plan from the current session or a saved workspace copy.
  If it is missing, stop.
- Once approved, make all in-scope local changes and run non-destructive
  validation without asking again.
- Stop and return to planning when source evidence exposes a material
  contradiction or when success requires new behavior, ownership,
  architecture, destructive action, external write, or scope.
- Do not commit, push, deploy, or stage unrelated changes unless separately
  requested.

## Required Context

Read the plan, `spec/conventions/Documentation_Conventions.md`, affected
Vision/UI/Flow/Module/Contract or cross-domain notes, and the source paths they
own. Read relevant `spec/doc_issues.md` entries.

For UI or server work, read the root and path-local `reuse.md` catalogs. Reuse
or enhance the narrowest existing owner before adding a new abstraction.

## Implementation Constraints

- Follow the target project's stack, state ownership, persistence, interface,
  localization, and UI constraints in `AGENTS.md` and linked specs.
- Update all affected sides of shared contracts as required by the project.
- Keep production testability hooks minimal and behavior-preserving.
- Preserve unrelated dirty work.

## Documentation Rules

Update only notes affected by the approved change:

- Vision for changed human capability intent.
- `spec/UI/` for changed visible behavior in place.
- Flow for changed behavior through time and behavioral SIT/E2E evidence.
- Module for changed responsibility, collaborators, code paths, and
  unit/widget/server-unit evidence.
- Contract for a changed durable data/API/sync/provider/fixture boundary.
- Cross-domain notes for shared domain, architecture, security, or
  non-functional meaning.
- Operations for topology, facts, procedures, release, or recovery.
- Test scenarios for detailed multi-flow E2E journeys.

In every non-Vision product note, keep `## Human View` above
`## Derived Delivery Guidance`. Add or revise human authority before deriving
agent constraints. Every derived instruction must cite a human statement or
linked authority and must not introduce visible behavior, business rules,
outcomes, or exceptions.

Keep exact verification commands with their owner: Flow for behavioral
integration/E2E, Module for unit/widget/server-unit, Contract for boundary
evidence, and Operations for operational evidence. UI and Vision link to that
evidence rather than duplicating it. Keep scenario/Flow links bidirectional.

## Workflow

1. Confirm the approved files, completion criteria, risks, validation, and
   existing dirty state.
2. Implement the smallest coherent code and schema change, including symmetric
   models and migrations where required.
3. Run code generation only when required by changed sources.
4. Add or update focused tests.
5. Update affected reuse catalogs and documentation owners.
6. Run the project-declared documentation checks when specs change and report
   any unavailable validation.
7. Run the plan’s narrow checks first, then justified broader checks.
8. Inspect the final diff against the plan and stage only planned paths.
9. Stop and hand off to `fs-dev-review`.

## Success Criteria And Output

Lead with the delivered outcome, plan alignment, changed product/code surfaces,
validation evidence, documentation changes, material caveats, and staging
status. State any unrun check and why. Omit generic process narration.
