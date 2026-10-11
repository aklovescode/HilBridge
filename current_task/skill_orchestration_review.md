# Delegated development skills — implementation and validation

Date: 2026-10-11

## Delivered

Added `fs-dev-orchestrate` and updated the ten existing `fs-dev-*` and
`fs-test-*` skills, their shared test-design guidance, the maintenance README,
and HilBridge's `AGENTS.md`. Installed the eleven development/testing skills
under `/Users/apoorvkul/.agents/skills`; installed files match the repository
byte-for-byte. No SDK, service, scheduler, application source change, or new
dependency was introduced.

The workflow requires actual Plan mode for development planning, includes test
cases and useful subplans, and reuses approval for execution within that scope.
Production children work in separate worktrees without writing or running
tests. The parent owns tests, integration, independent review coordination,
validation, and iteration. Final destination integration follows successful
review and validation; cleanup follows verified integration. Human View remains
authoritative. New material decisions return to the user.

Approval, context packets, ownership, commit/tree identities, evidence, findings,
and cleanup state are saved so an interrupted run can be resumed by inspecting
its actual state. Skills cannot switch the client's mode or guarantee execution
after the app stops.

## MacroSheet feedback applied

Read the referenced [Review MacroSheet skill feedback](thread://01a124e9-b08c-7672-9334-1372c713b852?hostId=local)
chat and its local skill-consistency report. Applied these lessons:

- Put purpose, authority, the normal workflow, and completion conditions early;
  move detailed handoff/recovery and test-design instructions into references.
- Carry accepted intent forward without reconfirming unchanged scope. Preserve
  project-specific requirements in the target project's instructions.
- Verify actual diffs, trees, tests, and final state independently of agent
  claims. Keep authored, committed, integrated, tested, and reviewed distinct.
- Test connected workflows and negative cases using frozen instructions and
  preserved evidence. A successful pilot does not establish general reliability.

## Validation

All thirteen repository skill packages passed Skill Creator validation. Local
Markdown link targets and `git diff --check` passed. All eleven installed
development/testing packages also passed validation and checksum comparison.
An independent static review found no actionable inconsistencies.

Three behavioral trials were performed in isolated temporary fixtures:

1. **Plan-mode gate:** a fresh agent in Default mode was asked to use
   `fs-dev-plan`. It requested the actual client mode change and made no plan or
   source edits. This checks the refusal path, not native Plan-mode execution.
2. **Delegated delivery:** two native implementation children changed separate
   production modules while the parent authored tests. A separate reviewer
   reviewed the integrated candidate while the parent validated it. All sixteen
   tests passed. The fixture's final squash commit was
   `107cb8567ba5eddca08e6fea77a1b1757b287fd7`; its tree
   `7097aca0757ef2308dc333ef687823010d1913a8` exactly matched the reviewed/tested
   candidate. Four task worktrees were removed after preserving evidence and a
   Git bundle. An unrelated dirty README edit remained unchanged and unstaged.
3. **In-scope iteration:** a fresh agent reproduced two approved test failures,
   repaired the production guard through `fs-dev-iterate`, and passed all four
   tests without asking for approval again. The test file stayed unchanged;
   only the production fix was staged. No commit authority was given or used.

The parent independently checked the final delivery tree, preserved README,
worktree cleanup, unchanged iteration test, and staged repair scope. The
delivery pilot used a frozen skill snapshot; subsequent small clarifications
about mutable report placement and iteration triggers received structural and
independent static review, not a second full delivery run.

Evidence, frozen pilot skills, final manifests, installation backup, reports,
logs, repair patch, and Git bundle are preserved at
[/Users/apoorvkul/.codex/artifacts/hilbridge-skill-orchestration-20261011](/Users/apoorvkul/.codex/artifacts/hilbridge-skill-orchestration-20261011).

## Limits and repository state

Native Plan-mode planning/approval transition, a full same-run fix/re-review
cycle, interruption recovery, moving destination branches, merge conflicts,
managed Codex worktree lifecycle, shared runtime resources, and publication were
not exercised. The fixtures used ordinary Git worktrees. These cases remain
instructional support, not demonstrated runtime guarantees.

Application typecheck/build and specification validation were skipped because
application source and `spec/` did not change. Existing unrelated task plan and
review artifacts were preserved. At the validation handoff, changes were
uncommitted and unpushed;
`Stable-HIL` still points to `9c86863d1824346b44a4b751b2d5af5622e7b57d`.
The updated installed copies may require a client refresh to appear in a
previously loaded skill catalog.
