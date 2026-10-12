---
name: fs-dev-review
description: >-
  Independently reviews a staged implementation or explicit base/head commit
  range against the authorized plan, specs, and validation evidence. Use after
  implementation or iteration, including as an orchestration review child.
  Reports findings and closure evidence; does not fix implementation or tests.
---

# Full-stack Dev — Review

## Goal

Give the requesting human or parent a concise, evidence-backed account of plan
alignment, material defects, documentation drift, and validation risk.

## Authority And Boundary

- Require the authorized master plan/context and an explicit review target:
  either the staged batch or base/head commits. Read all relevant subplans.
  See [plan authority](../fs-dev-plan/SKILL.md#authority-and-boundary); the user's
  implementation request/accepted decisions can supply authority without a
  separate plan approval. If the target or authority is missing, report the blocker.
- For staged work, inspect `git diff --cached` and its base/index identity.
  For committed work, verify the supplied SHAs, inspect `git diff BASE HEAD`,
  and read connected source at HEAD. An empty index after integration does not
  mean there is nothing to review. Use an immutable candidate checkout for
  parallel review so parent fixes cannot change the source beneath the review.
- Read existing project documentation conventions and affected authoritative specs.
- Write only the project-designated review report (default:
  `current_task/changes_summary.md`), plus project-required archival of an unrelated
  prior report. Follow its retention/handoff rules; do not overwrite another task's
  evidence. In delegated runs, use the separate candidate-specific report path
  supplied by the parent, not its test report or another task's summary.
  Do not fix code, change specs, restage files, or expand inferred scope.

## Project Context

Read the target project's root and applicable path-local `AGENTS.md` first.
Use its stack, domain invariants, state ownership, paths, reuse catalogs,
discovery tools, checks, task-artifact conventions, and applicable migration
rules. Read project-local `PRODUCT.md` and `DESIGN.md` when relevant.

Vision-first paths below are defaults; honor project equivalents. Do not import
another project's assumptions or bootstrap missing layers, tools, or validators
unless requested. Use available request/source evidence when guidance is absent;
report missing required context or validation instead of claiming completeness.

## Review

### Plan And Product Intent

- Confirm every change in the review target is required by the plan and every
  completion criterion is addressed.
- Compare the actual result with the authorized requirement, independently
  of the implementer's completion claim. Inspect working-tree differences where
  tests may have exercised content that is not staged.
  For example, passing tests after an unstaged fix do not validate the earlier
  staged code. Record that mismatch; keep staged validation unverified until
  evidence covers the actual review target.
- Review the combined implementation, parent-authored tests, integration edits,
  and cross-subplan effects. Compare test expectations with authorized behavior;
  passing assertions cannot validate an incorrectly weakened expectation.
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
- Confirm non-Vision product notes put `## Human View` before strictly derived
  guidance; Vision's upper content is its human authority. Human reviewability
  does not require a new human approval for every in-scope documentation edit.
- Confirm UI/Flow/Module links, Flow/scenario backlinks, and Module/Contract
  `## Code` paths remain current.
- Confirm behavioral commands live in Flows, unit commands in Modules, boundary
  commands in Contracts, and operational commands in Operations.
- Check the project-declared documentation validation when specs changed and
  record any validation that was skipped, unavailable, or weakened.
- Check commands, results, tested revision, and relevant failure/recovery
  coverage. Reuse current evidence; run safe focused checks when it is missing
  or stale. In delegated delivery, the parent executes tests; request missing
  evidence through the parent instead of launching a duplicate suite. A passing
  unit check does not prove an untested integration or UI.
- Confirm `spec/doc_issues.md` records unresolved intent/code drift.

## Output

Write:

1. **Review Target** — plan version, base/head or staged identity, source tree
2. **Findings** — stable IDs, severity, violated criterion, files/evidence, remedy
3. **Plan Alignment**
4. **Validation Evidence** — checked source/environment and missing evidence
5. **Finding Dispositions** — open, fixed-and-verified, or rejected with evidence

If there are no findings, say so explicitly. Lead the user handoff with
findings, then plan alignment, caveats, and the next review action. Separate
passed criteria, failed criteria, and unverified criteria; do not turn missing
evidence into a pass or infer authorization to fix a finding.

On another round, inspect the fixes and their effects on the authorized whole.
Close a finding only with evidence on the current candidate. Explain rejected
findings; do not silently drop them or demand a human rubber stamp for routine
in-scope fixes. A required verification gap keeps the completion gate open.
