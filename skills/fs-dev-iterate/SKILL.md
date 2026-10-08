---
name: fs-dev-iterate
description: >-
  Applies human review feedback to the same approved task, updates
  in-scope code, tests, reuse catalogs, and affected Vision-first spec notes,
  validates, and stages only the follow-up paths. Use after fs-dev-review when
  feedback does not materially change approved product intent or architecture.
---

# Full-stack Dev — Iterate

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

Resolve review feedback completely while preserving the approved intent and
keeping the follow-up diff attributable to that feedback.

## Authority And Approval Boundary

- Require the approved plan, `current_task/changes_summary.md`, and human
  feedback from chat or `current_task/review_feedback.md`.
- Apply in-scope local changes and non-destructive validation without asking
  again.
- Return to `fs-dev-plan` when feedback changes product behavior, ownership,
  architecture, destructive impact, or material scope, or when a required input
  is missing.
- Do not commit, push, deploy, perform destructive actions, or stage unrelated
  dirty work.

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
   changes; identify any item requiring replanning.
2. Implement the smallest in-scope correction and focused regression evidence.
3. Update affected reuse catalogs and documentation owners.
4. Run the project-declared documentation checks when specs change and the
   narrowest relevant code/tests from the plan and feedback.
5. Inspect the diff, stage only follow-up paths, and run `fs-dev-review` again
   for a substantial batch.

## Success Criteria And Output

Lead with feedback resolved, any item returned for replanning, validation
evidence, documentation effects, material caveats, staging status, and
readiness for re-review. Omit generic process narration.
