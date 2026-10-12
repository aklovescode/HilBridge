---
name: fs-dev-orchestrate
description: >-
  Coordinates an authorized development plan in Codex: delegates implementation
  to child agents in separate worktrees, owns tests in the parent, integrates
  changes, runs independent review and validation, and iterates to completion.
  Use for delegated delivery after fs-dev-plan completion, including resuming an
  interrupted run. Does not replace planning or authorize publication.
---

# Full-stack Dev — Orchestrate

Deliver the authorized outcome with human involvement at scope decisions and final
handoff. The parent owns tests, integration, and the evidence for completion.

## Entry And Authority

- Require the completed plan and its testing section, with the user's
  implementation request/accepted decisions or explicit plan approval. Use
  [plan authority](../fs-dev-plan/SKILL.md#authority-and-boundary); no separate
  approval milestone is required. If a material decision remains, use
  `fs-dev-plan` to ask and resolve it before dependent implementation.
- Execute only outside Plan mode. Check the runtime's declared mode; a prompt
  saying "implement" does not itself switch modes. If needed, explain the mode
  requirement and ask the user to switch through the client.
- Read the target project's applicable `AGENTS.md`, relevant specs, and setup
  and artifact conventions. Project rules own required validation and release
  procedures. This workflow uses native Codex subagents and Git worktrees;
  verify those capabilities before dispatch. Report a missing capability instead
  of silently substituting a different delivery workflow.
- The authorized execution section must name local commit/integration/cleanup
  authority and the destination branch. Push, deployment, destructive data work,
  and external writes require their own scoped authorization, which may already
  be included in the authorized plan. Skills cannot override host permissions.

## Normal Workflow

1. **Save the execution context.** Once planning is complete, preserve the plan,
   subplans, decisions, relevant source/spec evidence, and base commit. Read
   [handoffs and recovery](references/handoffs.md) to record the small amount of
   state needed to resume. Honor project retention rules and leave unrelated
   task artifacts intact. Do not rewrite accepted requirements during delivery.
2. **Prepare isolation.** Inspect dirty state and existing attached worktrees.
   Record the initial inventory and each new worktree's path/managed identity
   and owner so cleanup can distinguish task-created checkouts from existing ones.
   Use a task-owned integration branch/worktree for the parent. Establish an
   explicit base commit containing the authorized prerequisites; new worktrees
   do not automatically receive dirty files or the chat's plan. Preserve user
   edits, and carry only authorized prerequisite changes into the task base.
3. **Delegate production work.** Spawn native child agents with `fs-dev-implement`,
   the delegated role, a dedicated worktree at the assigned base, and the
   context packet from the reference. Give each file/shared interface one
   writer. Dispatch independent subplans together within available concurrency;
   dependent subplans start from an integrated prerequisite commit. Use one
   implementation child when further splitting would create overlapping work.
4. **Write tests in the parent.** While children work, use `fs-test-implement`
   with the authorized testing section. Own tests, fixtures, harness/configuration
   changes, shared documentation, and verification notes assigned to the parent.
   Production testability hooks remain with their assigned child. Author
   expectations from authorized behavior; wire implementation-dependent details
   after integration. Preserve useful pre-change failures without claiming a
   final pass. Check child messages between useful work; prefer bounded waits
   or completion notifications to repeated full chat reads.
5. **Integrate completed work.** Inspect each child's actual commit/diff, path
   ownership, and handoff. A completion message is not integration evidence.
   Commit the parent's task-owned work before merging child commits into the
   integration branch in dependency order. Resolve mechanical conflicts;
   escalate conflicting product decisions. After a child stops and its output
   is verified integrated, preserve recoverable commits, reports, and needed
   artifacts, then clean up its disposable worktree using the reference.
6. **Review and test one candidate.** Commit all task source/test/spec changes
   and record the candidate commit and tree. Keep mutable run reports outside
   that candidate; distinguish their paths from unexpected dirty source files.
   Delegate `fs-dev-review` to an independent child with the full authorized plan,
   all subplans, context, and explicit base/head commits. Give it an immutable
   checkout and a separate report destination. While it reviews, the parent
   uses `fs-test-run` and project-required checks on that same candidate. Poll
   for review feedback between test commands or while a nonblocking command
   runs; do not launch duplicate suites just to keep busy. Preserve raw logs
   outside the candidate source and send the reviewer compact evidence.
7. **Close findings.** Collect review findings and test failures in one ledger,
   then use `fs-dev-iterate` for in-scope fixes. A test failure is not permission
   to change its expected behavior. Disputed findings need a reasoned reviewer
   disposition; missing required evidence remains open. After an edit, create
   a new candidate, rerun affected checks, and have the reviewer examine fixes,
   remaining findings, and their impact on the whole authorized change. Keep
   source stable during each review/test round; newly arriving feedback is
   queued for the next round.
8. **Finalize and clean up.** Once acceptance criteria, required validation,
   documentation, and independent review pass, finalize the task's commit
   message with resulting behavior, significant design
   choices, validation, and limitations. Use an unpublished task commit or a
   final squash/merge commit; do not rewrite published history. Advance the
   authorized destination branch only after verifying its current base and the
   validated tree. If it moved, incorporate the new base and repeat affected
   review/validation. Verify the destination contains the result, preserve
   reports and needed ignored artifacts, then archive task-created managed
   worktrees through Codex's lifecycle tool (or remove task-created ordinary
   worktrees with Git). Finish any remaining task worktree cleanup and verify
   the final inventory against the run ledger. Never prune unrelated worktrees
   or discard unmerged work.

## Completion And Escalation

Finish when all authorized acceptance criteria are evidenced, required checks pass
on the final source tree/environment, the reviewer has no unresolved actionable
findings, documentation matches the result, and authorized integration/cleanup
is verified, with no disposable task-created worktrees left behind. Distinguish
authored, committed, integrated, tested, reviewed, and published states. A failure
in a later step does not erase an earlier success.

Continue routine fixes without asking the human again. Escalate a new product or
architecture decision, missing access/environment, exceeded agreed budget, or
repeated attempts with no new evidence or progress. Do not weaken tests, silently
waive findings, or claim completion to escape a loop. Respect provider/host
rejections; do not evade them by changing tools or rephrasing the same operation.

Report delivered behavior, final revision/branch, review and test evidence,
unresolved limitations, and cleanup/publication status. Save detailed logs and
handoffs in the run artifacts rather than flooding the main conversation.
