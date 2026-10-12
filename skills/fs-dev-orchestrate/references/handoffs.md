# Handoffs And Recovery

Use this when preparing a delegated run or resuming one. Choose the project's
artifact location first. If none is declared, use a task-specific directory
under `current_task/runs/`; projects that restrict that directory may use an
external run directory instead. Record its absolute path. Do not make application
builds depend on these artifacts or copy private context into a public repository.

## Durable Context

The parent maintains one small state note and separate plan, review, and test
artifacts. A simple Markdown table is enough; no database or SDK is required.
Keep mutable run evidence out of source commits unless the project explicitly
versions it. Record its paths so untracked reports cannot hide uncommitted code
or be accidentally included by broad staging. Version any required final summary
deliberately and verify the resulting candidate before integration.

Record:

- completed plan version/digest and the user's implementation request/decision
  reference or explicit plan approval, accepted decisions, scope, and authorized
  local/external actions;
- repository, explicit base SHA, integration branch/worktree, and destination;
- subplan dependencies, file ownership, agent identifiers, worktree paths,
  assigned base SHAs, produced commits, and actual integration status;
- current candidate commit/tree, reviewer target, and report/log locations;
- each finding's ID, source revision, violated criterion, disposition, fix,
  and verification; record reviewer agreement for rejected findings;
- commands, environment/fixture identity, results, tested tree, and outstanding
  blockers; preserve earlier failures as well as later passes;
- current phase, next action, and cleanup status.

Use separate report files per role/candidate so a test run cannot overwrite the
review. For example, `review-<candidate>.md` and `tests-<candidate>.md` in the
external run directory. Update state after dispatch, child completion,
integration, each validation round, and finalization. In Default mode, capture
the completed plan before implementation. In native Plan mode, wait until the
runtime permits workspace writes; do not claim an automatic mode transition.
An agent-written plan is not evidence of the user's execution authority.

## Implementation Packet

Give each child enough context to make its assigned decisions:

- authorized master plan and assigned subplan, with acceptance criteria;
- relevant user decisions and constraints that the plan abbreviates;
- exact spec headings, source findings, contract shapes, and unresolved issues;
- dependency status, expected interfaces/test seams, assigned worktree and base;
- owned paths and the parent/other children's overlapping responsibilities;
- allowed checks, commit authority, and handoff destination.

Full-history inheritance may help, but does not replace explicit ownership or
verified files at the assigned revision. References must be accessible from the
child's environment. Supply excerpts when a referenced conversation or artifact
is unavailable there. Never rely on an uncommitted plan appearing in a worktree.

Example dispatch (replace example values with the actual authorized assignment):

```text
Use fs-dev-implement in its delegated role for subplan API-1.
Approved context: <absolute plan path>, section API-1 and linked contracts.
Worktree: <absolute worktree path>; expected base: <full SHA>.
Own backend/src/handler.ts and its assigned Module note.
The parent owns tests, fixtures, package configuration, and shared Flow notes.
Implement the authorized error contract and test seam. Do not author or run tests.
Run the assigned typecheck/build checks. Local task commits are authorized.
Return commit SHA, changed paths, fulfilled criteria, checks actually run,
unrun tests, and blockers. Ask the parent about an ownership conflict.
```

## Isolation And Integration

Subagents may initially share the parent's directory. Create a worktree through
the supported Codex tool and use its returned path; pass an explicit ref because
the default may be the remote default branch. If managed worktrees are not
available for this repository, use ordinary Git worktrees within the authorized
scope. Do not assume the spawn operation changes directories. Verify each
child's repository/path and starting commit before it edits.

Use unique `codex/` task branch names unless the user/project specifies otherwise.
Detached worktree commits are also usable when their SHAs are recorded and kept
reachable before cleanup. Worktrees isolate files, not ports, databases, external
services, shared Git refs, or host permissions. Assign separate runtime resources
where needed; children must not mutate the integration/destination branch.

Inspect project setup scripts before running them: dependency setup may invoke
tests or write to shared services. Keep test execution with the parent. Do not
auto-initialize all submodules or copy secrets; follow the target project's
actual submodule, private/public, environment, and publication requirements.

The parent checks both `git status --short` and actual child changes against the
base, including changed/deleted/untracked paths. Only committed task-owned work
is integrated; preserve and report unexpected dirty files. A file allowlist does
not authorize unrelated edits inside that file.

The reviewer receives the authorized master plan, relevant subplans/decisions,
base SHA, candidate SHA, known findings, and validation evidence. Prefer a fresh
reviewer context, without implementer conclusions presented as facts. Review
the complete combined change, including the parent's tests, integration edits,
and cross-subplan effects. The reviewer returns findings and evidence, not fixes.

Finalize history only within authority. A message-only amend changes a commit
SHA but not its tree: record both identities. A squash/merge result must have
the validated tree; source changes or target-base changes require new evidence.
Never reset a destination checkout to force a merge through dirty user work.

## Worktree Cleanup

The parent owns cleanup. Use the initial inventory and run ledger, not a broad
name pattern or a child's completion message, to identify task-created worktrees.
Once a child has stopped, verify its commits are integrated and remain reachable,
preserve its handoff/report and needed ignored artifacts, and inspect its dirty
state before cleanup. Keep a checkout while any review, test, integration, or
background command still uses it. Unexpected uncommitted work remains a blocker;
do not force-remove it to make the inventory look clean.

Archive managed worktrees through Codex's lifecycle tool using their recorded
identity. Remove ordinary worktrees with `git worktree remove <recorded-path>`;
this also removes their Git registration. Avoid blanket `git worktree prune` or
directory deletion: a missing path or an old branch name does not establish task
ownership. Reconcile any remaining stale task registration through the supported
lifecycle mechanism or report the exact blocker. Preserve unrelated, original,
shared, pinned, or still-active checkouts and reachable task history.

After cleanup, compare the actual worktree inventory with the ledger and record
removed/archived identities, retained checkouts, and blockers. A run is not fully
cleaned up merely because its children finished. Final handoff requires every
disposable task-created worktree to be gone and the result/artifacts recoverable.

## Resume

Read saved state and inspect live agent status, worktrees, Git refs/diffs, and
report artifacts before deciding what remains. Do not trust stale phase labels
or redispatch a still-running child. Reuse verified completed work and approvals.
Check whether a commit is already integrated before applying it again. If an
action's outcome is uncertain, inspect resulting state before retrying.

Resume the first unfinished supported step. Mark missing evidence as unverified;
do not turn it into a pass. The saved note supports resumption when Codex runs
again; it is not an automatic scheduler or a guarantee of crash recovery.
