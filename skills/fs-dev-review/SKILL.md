---
name: fs-dev-review
description: >-
  Reviews a staged implementation against its approved plan and the
  Vision-first documentation graph, then writes
  current_task/changes_summary.md for human review. Use after fs-dev-implement
  or fs-dev-iterate. This skill reports findings and does not fix code or alter
  the staged batch.
---

# Full-stack Dev — Review

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

Give the human reviewer a concise, evidence-backed account of plan alignment,
material defects, documentation drift, and validation risk.

## Authority And Boundary

- Require a staged implementation batch and its approved plan. If either is
  missing, report the exact blocker.
- Read the plan, `spec/conventions/Documentation_Conventions.md`, affected
  authoritative specs, and `git diff --cached`.
- Write only `current_task/changes_summary.md`. Do not fix code, change specs,
  restage files, or expand the inferred scope.

## Review

### Plan And Product Intent

- Confirm every staged change is required by the plan and every completion
  criterion is addressed.
- Compare visible behavior with Vision and UI human sections, temporal behavior
  with Flows, and durable meaning with Contracts/cross-domain notes.
- Flag behavior that exists only in Derived Delivery Guidance or code.

### Architecture And Correctness

- Check architecture, state ownership, persistence, and interface compatibility
  against the target project's `AGENTS.md` and linked specs.
- Check ownership, authorization, temporal, deletion, idempotency, migration,
  localization, and failure behavior where applicable.
- Distinguish generated consequences from hand-authored design; inspect both
  when generated output exposes schema or provider drift.

### Documentation And Verification

- Confirm changed documentation uses the correct owner:
  `Vision -> UI Surface -> Flow -> Module -> Code` or
  `Vision -> Technical Flow -> Module -> Code`, with Contracts and cross-domain
  notes only where useful.
- Confirm `## Human View` precedes strictly derived delivery guidance.
- Confirm UI/Flow/Module links, Flow/scenario backlinks, and Module/Contract
  `## Code` paths remain current.
- Confirm behavioral commands live in Flows, unit commands in Modules, boundary
  commands in Contracts, and operational commands in Operations.
- Check the project-declared documentation validation when specs changed and
  record any validation that was skipped, unavailable, or weakened.
- Confirm `spec/doc_issues.md` records unresolved intent/code drift.

## Output

Write:

1. **Findings** — severity ordered, with files/evidence
2. **Plan Alignment**
3. **Files Changed** — grouped by product UI, backend, docs, and tests
4. **Validation Evidence**
5. **Reviewer Focus**

If there are no findings, say so explicitly. Lead the user handoff with
findings, then plan alignment, caveats, and the next review action.
