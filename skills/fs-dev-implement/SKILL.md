---
name: fs-dev-implement
description: >-
  Implements an explicitly approved implementation plan, including in-scope code,
  tests, reuse catalogs, and affected Vision-first spec notes; runs relevant
  non-destructive validation and stages only the planned paths. Use after
  fs-dev-plan or fs-dev-investigate approval, then hand off to fs-dev-review.
---

# Full-stack Dev — Implement

## Goal

Deliver the approved outcome completely without changing its product intent or
expanding its scope.

## Authority And Approval Boundary

- Require the approved plan from the current session or a saved workspace copy.
  If it is missing, report that prerequisite before dependent edits. Bind work
  to its approved outcome, paths, constraints, and completion criteria.
- Once approved, make all in-scope local changes and run non-destructive
  validation without asking again.
- Stop and return to planning when source evidence exposes a material
  contradiction or when success requires new behavior, ownership,
  architecture, destructive impact, or scope outside the approved plan.
- Implementation approval covers in-scope local work and non-destructive checks.
  Commit, push, deploy, destructive operations, and external writes require
  separate authorization for that action. Honor authorization already given;
  finish authorized steps without asking again. Never stage unrelated edits.

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
4. Add or update focused tests when needed to prove changed behavior. Compare
   results with approved expectations, not just with newly written assertions.
5. Update affected reuse catalogs and documentation owners.
6. Run the project-declared documentation checks when specs change and report
   any unavailable validation.
7. Run the plan’s narrow checks first, then justified broader checks.
8. Check every completion criterion against the actual diff and validation
   evidence. Stage only planned paths or task-owned hunks, then inspect the
   index. An allowed filename does not authorize its unrelated edits.
9. Stop implementation edits and hand off to `fs-dev-review`. Any separately
   authorized release follows the project's review/release procedure; keep the
   review step read-only.

## Success Criteria And Output

Lead with the delivered outcome, plan alignment, changed product/code surfaces,
validation evidence, documentation changes, material caveats, and staging/release
status. Record commands, results, and evidence locations. Mark unmet criteria or
unrun checks and their concrete blockers; do not describe partial verification
as a complete pass. Rerun affected checks after a relevant edit or environment
change; otherwise reuse current evidence. Omit generic process narration.
