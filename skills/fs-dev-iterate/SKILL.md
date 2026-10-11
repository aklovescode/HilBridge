---
name: fs-dev-iterate
description: >-
  Applies human review feedback to the same approved task, updates
  in-scope code, tests, reuse catalogs, and affected Vision-first spec notes,
  validates, and stages only the follow-up paths. Use after fs-dev-review when
  feedback does not materially change approved product intent or architecture.
---

# Full-stack Dev — Iterate

## Goal

Resolve review feedback completely while preserving the approved intent and
keeping the follow-up diff attributable to that feedback.

## Authority And Approval Boundary

- Require the approved plan, `current_task/changes_summary.md`, and human
  feedback from chat or `current_task/review_feedback.md`, using project artifact
  equivalents. If an input is missing, report that prerequisite; do not invent
  approval or send an unchanged task back through planning.
- Apply in-scope local changes and non-destructive validation without asking
  again.
- Return to `fs-dev-plan` when feedback changes product behavior, ownership,
  architecture, destructive impact, or material scope outside the approved plan.
- Commit, push, deploy, destructive operations, and external writes require
  separate authorization for that action. Honor authorization already given;
  never stage unrelated dirty work.

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

Read the plan, review artifacts, relevant code, affected `reuse.md` catalogs,
`spec/conventions/Documentation_Conventions.md`, and the authoritative
Vision/UI/Flow/Module/Contract or cross-domain notes.

Preserve the implementation constraints in the approved plan and project
`AGENTS.md`, including state ownership, persistence, interface compatibility,
and applicable UI conventions. Keep testability hooks minimal.

## Documentation Rules

- Update only documentation affected by the feedback.
- Put changed intent in Vision, visible-in-place behavior in UI, temporal
  behavior and behavioral evidence in Flow, program responsibility/code/unit
  evidence in Module, and durable boundaries in Contracts.
- Use cross-domain, Operations, or test-scenario notes only for their owned
  knowledge.
- Preserve `## Human View` as authority. Every delivery instruction must derive
  from a named human statement or linked authority; never introduce behavior in
  Derived Delivery Guidance.
- Keep verification commands with their owning Flow, Module, Contract, or
  Operations note and keep Flow/scenario links bidirectional.

## Workflow

1. Map every feedback item to the approved plan and current staged/working
   changes; identify any item requiring replanning. Reuse unchanged approvals
   and current source/validation evidence.
2. Implement the smallest in-scope correction and focused regression evidence.
3. Update affected reuse catalogs and documentation owners.
4. Run the project-declared documentation checks when specs change and the
   narrowest relevant code/tests from the plan and feedback.
5. Check resolved feedback and original completion criteria against actual
   results. Inspect the diff and index; stage only task-owned follow-up paths or
   hunks. For a substantial batch, run `fs-dev-review` again without letting
   iteration's write permission carry into the review-only step.

## Success Criteria And Output

Lead with feedback resolved, any item returned for replanning, validation
evidence, documentation effects, material caveats, staging status, and
readiness for re-review. Record commands/results and unmet or unverified criteria
with their blockers. Omit generic process narration.
