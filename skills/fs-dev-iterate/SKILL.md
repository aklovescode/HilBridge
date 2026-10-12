---
name: fs-dev-iterate
description: >-
  Applies human or independent-agent feedback and test failures to the same
  authorized task. Updates in-scope code, tests, reuse catalogs, and spec notes,
  validates, and stages only the follow-up paths. Use after review or failed checks when
  feedback does not materially change authorized product intent or architecture.
---

# Full-stack Dev — Iterate

## Goal

Resolve review feedback completely while preserving the authorized intent and
keeping the follow-up diff attributable to that feedback.

## Authority And Approval Boundary

- Require the authorized plan and concrete feedback: a human request, independent
  review findings, or test-failure evidence with its candidate identity. Use the
  assigned run reports or project artifact equivalents. If a necessary input
  is missing, report that prerequisite. See [plan authority](../fs-dev-plan/SKILL.md#authority-and-boundary):
  the original implementation request can supply authority; do not invent
  approval or send an unchanged task back through planning.
- Apply in-scope local changes and non-destructive validation without asking
  again. A failing implementation of authorized behavior does not require fresh
  human approval to repair; preserve the accepted behavior and assertions.
- Return to `fs-dev-plan` when feedback changes product behavior, ownership,
  architecture, destructive impact, or material scope outside the authorized plan.
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
existing project documentation conventions, and the authoritative
Vision/UI/Flow/Module/Contract or cross-domain notes.

Preserve the implementation constraints in the authorized plan and project
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

1. Map every feedback item to the authorized plan and current staged/working
   changes; identify any item requiring replanning. Reuse unchanged approvals
   and current source/validation evidence.
2. Implement the smallest in-scope correction and focused regression evidence.
   Preserve assigned file ownership while children are still active. Classify
   failures before editing: product bug, test bug, environment blocker, or known
   gap. Fix a test only when evidence shows its fixture/assertion is wrong;
   do not weaken the authorized expected result to obtain a pass.
3. Update affected reuse catalogs and documentation owners.
4. Run the project-declared documentation checks when specs change and the
   narrowest relevant code/tests from the plan and feedback.
5. Check resolved feedback and original completion criteria against actual
   results. Inspect the diff and index; stage only task-owned follow-up paths or
   hunks. In orchestrated runs, record a new candidate commit under the plan's
   commit authority and return to independent review and affected validation.
   For standalone substantial changes, run `fs-dev-review` again. Iteration's
   write permission does not carry into the review-only step.

Keep each finding linked to its fix and current verification evidence. Escalate
missing access, material scope decisions, or repeated attempts without progress;
do not waive unresolved findings or erase failed runs to declare completion.

## Success Criteria And Output

Lead with feedback resolved, any item returned for replanning, validation
evidence, documentation effects, material caveats, staging status, and
readiness for re-review. Record commands/results and unmet or unverified criteria
with their blockers. Omit generic process narration.
