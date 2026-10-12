---
name: fs-dev-implement
description: >-
  Implements an authorized development plan or assigned subplan. In delegated
  delivery, children own production code and assigned docs while the parent
  owns tests; standalone implementation includes planned tests. Validates the
  assigned scope and hands off evidence without expanding authority.
---

# Full-stack Dev — Implement

## Goal

Deliver the authorized outcome completely without changing its product intent or
expanding its scope.

## Assigned Role

For an implementation child under `fs-dev-orchestrate`, use the assigned
worktree, base commit, paths, and context packet. Verify the directory and base
before edits; spawning a child does not itself change the working directory.
Own production changes, authorized production testability hooks, and assigned
docs only. Do not create/update test cases, fixtures, or test harnesses and do
not run tests. Run assigned typecheck/build/documentation checks; inspect scripts
so an apparently non-test command does not run a test suite indirectly. Report
any project check that must wait for integration. The parent owns test execution
and final completion; do not claim this subplan is tested.

Without that delegated assignment, implement the authorized code, docs, and tests
and run the planned validation as usual. Do not silently offload a standalone task.

## Authority And Approval Boundary

- Require a completed plan from the current session or a saved workspace copy,
  with implementation authority from the user's request/accepted decisions or
  explicit plan approval. See [plan authority](../fs-dev-plan/SKILL.md#authority-and-boundary).
  If a prerequisite is missing, report it before dependent edits. Bind work
  to its authorized outcome, paths, constraints, and completion criteria.
- Once planning and required questions are complete, make in-scope changes and
  run non-destructive validation without asking again.
- Stop and return to planning when source evidence exposes a material
  contradiction or when success requires new behavior, ownership,
  architecture, destructive impact, or scope outside the authorized plan.
- Implementation authority covers in-scope local work and non-destructive checks.
  Honor local commit authority recorded in the handoff; children commit only
  assigned work in their worktree and return its SHA. Push, deploy,
  destructive operations, and external writes require scoped authorization
  for that action. Honor authorization already given;
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

Read the plan, existing project documentation conventions, affected
Vision/UI/Flow/Module/Contract or cross-domain notes, and the source paths they
own. Read relevant `spec/doc_issues.md` entries.

For UI or server work, read relevant existing `reuse.md` catalogs. Reuse
or enhance the narrowest existing owner before adding a new abstraction.

## Implementation Constraints

- Follow the target project's stack, state ownership, persistence, interface,
  localization, and UI constraints in `AGENTS.md` and linked specs.
- Update all affected sides of shared contracts as required by the project.
- Keep production testability hooks minimal and behavior-preserving.
- Preserve unrelated dirty work.

## Documentation Rules

Update only notes affected by the authorized change:

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

1. Confirm the authorized files, completion criteria, risks, validation, and
   existing dirty state.
2. Implement the smallest coherent code and schema change, including symmetric
   models and migrations where required.
3. Run code generation only when required by changed sources.
4. In standalone work, add/update planned tests and compare results with authorized
   expectations. In a delegated role, preserve test ownership with the parent
   and communicate interface/testability changes without writing or running tests.
5. Update affected reuse catalogs and documentation owners.
6. Run the project-declared documentation checks when specs change and report
   any unavailable validation.
7. Run the checks assigned to this role, narrow checks first. Defer checks that
   require another subplan to the parent with the exact dependency recorded.
8. Check every completion criterion against the actual diff and validation
   evidence. Stage only planned paths or task-owned hunks, then inspect the
   index. An allowed filename does not authorize its unrelated edits.
   Preserve unrelated edits and their existing staging state.
   For example, when a file contains an initially unstaged user-edited setting
   and your handler fix,
   stage only the handler hunk (such as with `git add -p <path>`) and inspect
   `git diff --cached -- <path>`. Leave the user's setting unchanged and unstaged.
9. Delegated children return their actual commit, changed paths, fulfilled
   criteria, checks run, unrun tests, and blockers to the parent. Standalone
   work hands off to `fs-dev-review`. Any separately
   authorized release follows the project's review/release procedure; keep the
   review step read-only.

## Success Criteria And Output

Lead with the delivered outcome, plan alignment, changed product/code surfaces,
validation evidence, documentation changes, material caveats, and staging/release
status. Record commands, results, and evidence locations. Mark unmet criteria or
unrun checks and their concrete blockers; do not describe partial verification
as a complete pass. Rerun affected checks after a relevant edit or environment
change; otherwise reuse current evidence. Omit generic process narration.
