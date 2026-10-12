# Clarification-first planning without a separate approval gate

Date: 2026-10-12

## Change

`fs-dev-plan` now supports Default-mode development planning through three
phases: repository exploration, intent clarification, and implementation
clarification. Required material questions wait for actual answers before
dependent source/spec edits or child dispatch. Discoverable facts are resolved
from the repository; low-risk assumptions are recorded rather than converted
into unnecessary questions.

A completed plan within the user's implementation request and accepted decisions
is an authorized plan. That request, not the agent-authored plan, supplies
execution authority. Default-mode implementation requests continue into delegated
or standalone implementation without asking for plan approval. Planning-only
requests stop at the plan. Native Plan mode retains its runtime restrictions;
the skill does not switch modes or claim to define a new client mode.

Implementation, parent-owned testing, orchestration, review, iteration, handoff
state, documentation guidance, and project workflow guidance now accept this
authority consistently. Separate push/deployment/destructive/external-write
authority remains intact. `fs-dev-investigate` remains standalone and stops at
its findings/fix proposal. No application code, product specs, SDK, controller,
test framework, or dependency changed.

## Behavioral evidence

Trials use frozen skill files and independent agents in isolated Python
standard-library fixtures. Evidence and installation backups are preserved at
[/Users/apoorvkul/.codex/artifacts/hilbridge-autonomous-planning-20261012](/Users/apoorvkul/.codex/artifacts/hilbridge-autonomous-planning-20261012).

- **Ambiguous implementation request:** a fresh agent in Default mode read the
  raw project context, then asked about search fields, case behavior, and phrase
  versus word matching. The parent independently verified unchanged production,
  test, and unrelated README hashes, unchanged base HEAD, and no task worktrees
  before supplying answers. Only a planning artifact was written. The requester
  supplied behavior answers without a plan-approval message; delivery continued.
- **Planning-only request:** another fresh Default-mode agent received explicit
  behavior and a plan-only instruction. It completed a concrete plan without
  unnecessary questions or implementation. The parent independently verified
  every initial source/test/product file remained byte-for-byte unchanged and
  Git remained clean. Tests, staging, commits, and delegation did not run.
- **Delegated delivery after answers:** the agent completed the plan, dispatched
  a production-only implementation child, authored seven tests in the parent
  alongside the retained regression, integrated the result, and obtained an
  independent review with no actionable findings. All eight tests passed. The
  fixture's final `main` commit is `2b942a1bd7c76ecafa0cb076a2ea6e594ec760eb`,
  with the same tree as the tested/reviewed candidate:
  `320aa534f32b61ac17deed178e07aa815caf13c5`. Three task worktrees were removed
  after preserving a verified Git bundle. The parent independently checked the
  actual final tree, changed paths, production-only child commit, unchanged
  README, worktree inventory, bundle verification, and raw passing test log.

The evaluating parent acted as the fixture requester. Questions and answers used
agent messages rather than the actual Desktop question UI. These are observed
Default-mode behaviors, not a native Plan-mode comparison or proof of identical
questioning quality across tasks.

## Static validation and installation

At the initial Default-mode handoff, Skill Creator validation passed for all thirteen skill packages; local
Markdown targets and whitespace checks passed. Independent consistency review
found no actionable static issues on that skill/AGENTS diff, identified
by SHA-256 `917f4d4af7a09dd70684fa08fb65d95092e2b6f54011741a6af94626a61c4f0e`.
The eleven development/testing skills were synced to
`/Users/apoorvkul/.agents/skills` after checking for concurrent installed edits
and preserving a backup. All thirteen installed packages validate and match the
repository byte-for-byte. The two MCP companion skills were not changed.

The frozen trial snapshot preceded narrow wording/line-wrap clarifications to recorded
commit authority and handoff text; the core planning/continuation instructions
are unchanged. Final checks bind the resulting repository and installation to
their own manifests rather than treating the trial snapshot as identical.

## MacroSheet feedback cross-check

Re-read the live [Review MacroSheet skill feedback](thread://01a124e9-b08c-7672-9334-1372c713b852?hostId=local)
chat and its local skill/top-level guide consistency reports. The transferable
learnings map to this workflow as follows:

| Learning | Application and evidence |
| --- | --- |
| Make the common path easy to find; disclose detail progressively | Planning starts with mode/continuation and clarification rules. Handoff/recovery and shared test design remain focused references. Project-specific stack, ownership, licensing, and release rules remain project-owned. |
| Use concrete examples at consequential choices | Title/body search illustrates required intent clarification. The dispatch packet names ownership and checks. Added a mixed-file staging example and a staged-versus-working-test evidence example. |
| Preserve accepted decisions without repeat confirmation | The implementation request and accepted answers supply authority. The delivery trial implemented title-only search despite the agent recommending title-and-body search, with no separate plan approval. |
| Check the whole workflow after refinements | The frozen multi-turn trial covered unanswered questions, planning, parent tests, production delegation, independent review, final tree identity, integration, and cleanup; the planning-only negative case stopped. |
| Reuse trustworthy current evidence; do not optimize to a fixed call count | Review/test instructions bind evidence to the candidate and environment, reuse current results, and keep missing proof unverified. The final fixture commit reused validation only after its tree was proven unchanged. |
| Use programmatic calling only for a concrete benefit | No mandatory programmatic interface or controller was introduced. Existing MCP guidance keeps it conditional on host support and useful bounded work. |
| Evaluate behavior and resulting state independently | Frozen skills, raw fixture requests, hashes, candidate identities, isolated data, raw logs, parent audits, and a recovery bundle support the observations. These trials do not establish general performance superiority or native Plan-mode equivalence. |

The source chat's historical separate plan-approval policy is superseded by
the user's explicit current decision to remove that extra gate. Accepted intent,
necessary clarification, and scoped external-action authority remain intact.

The additional isolated trials preserved an unrelated initially unstaged setting
while staging only the implementation fix; all three existing regression tests
passed. A reviewer also caught a staged Unicode regression despite supplied
passing tests on an unstaged correction, leaving staged validation unverified
and making no source/index changes. Parent audits checked the actual files,
index, unchanged tests, and unchanged HEADs independently of those reports.

Independent static review found one wording conflict: the example needed to
preserve an already staged user edit as well as an unstaged one. The example now
specifies its initial state and explicitly preserves unrelated edits' existing
staging state. The separate pre-staged fixture passed: the user setting remained
staged, the task fix was added, all three tests passed, and HEAD/tests stayed
unchanged. Parent readbacks confirmed the actual index and working file. CC-1
is closed with static and behavioral evidence; no actionable static findings
remain. The reviewed skill/AGENTS diff is
`0de0d3bb2d5ffb0ae662a1f96337fd6079d2c92d8b1a35cff412fbcac0319029`.
No approval
gate, product behavior, invocation setting, dependency, or project-specific
MacroSheet constraint was added.

Additional frozen skills, reports, fixture/index evidence, installed backups,
and parent audits are at
[/Users/apoorvkul/.codex/artifacts/hilbridge-macro-learning-crosscheck-20261012](/Users/apoorvkul/.codex/artifacts/hilbridge-macro-learning-crosscheck-20261012).
The final refinements were synced after checking installed copies against their
backups. All thirteen installed packages validate and match the repository
byte-for-byte. Existing PyYAML was reused; no dependency was installed.

## Required worktree cleanup

`fs-dev-plan` now includes parent-owned cleanup as an execution step and
completion criterion. The plan records the initial inventory and task-created
identities. Finished child worktrees are archived/removed after their output is
verified integrated and their commits, reports, and needed artifacts are
recoverable. Review/test/integration checkouts stay while still in use; final
handoff verifies no disposable task-created worktrees remain. Unrelated,
original, active, shared, or protected checkouts are preserved. Unexpected dirty
work and unsupported stale registrations are reported as concrete blockers.

The parent executor performs cleanup; planning remains read-only. Managed
worktrees use Codex's lifecycle tool, and ordinary worktrees use scoped Git
removal. The guide does not authorize blanket pruning or directory deletion.
Review/test readiness permits finalization to start; verified integration and
cleanup are final completion conditions after that work, avoiding the circular
gate identified and closed as WT-1 in independent static review.

An isolated resumed-run trial removed three recorded task worktrees and retained
both pre-existing checkouts. The original dirty README and an unrelated dirty
worktree were unchanged. Main stayed at the same commit/tree, and all outputs
remained reachable or available in a verified bundle. Parent readbacks checked
actual paths, Git inventory, hashes, refs, and bundle verification independently
of the completion report. The trial also reconciled stale saved completion
labels against actual pending worktree registrations.

The final reviewed source diff is
`3811563010dc3eb8429ccd582410f13dede69235e525ea388468079f995b5246`.
All thirteen installed packages validate and match the repository after syncing
the planning/orchestration updates. Backups, frozen skills, raw fixture state,
cleanup reports, and parent audits are at
[/Users/apoorvkul/.codex/artifacts/hilbridge-worktree-cleanup-20261012](/Users/apoorvkul/.codex/artifacts/hilbridge-worktree-cleanup-20261012).
Managed archival, removal of a missing task checkout's stale registration, and
cleanup during a still-running development cycle were not runtime-tested. The
trial used ordinary Git with already completed and integrated child output.

## Limits

No true native Plan-mode comparison, native mode transition, actual Desktop
question-form interaction, fresh-context code-review configuration, fix/re-review
loop, interruption recovery, moving destination branch, merge conflict, managed
worktree lifecycle, or publication was exercised. The
fixture uses ordinary Git worktrees. Application typecheck/build and spec
validation are not applicable because their owning source/spec files did not
change. Existing task artifacts are preserved. At the validation handoff, this
batch was uncommitted and unpushed; the `Stable-HIL` tag was not moved.
