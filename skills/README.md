# Shared Development Skills

Maintain these project-neutral workflows here and commit changes to HilBridge:

- `fs-dev-*`: product documentation, investigation, planning, implementation,
  review, and iteration.
- `fs-test-*`: test planning, implementation, and execution.
- `mcp-plugin-*`: MCP/plugin planning and implementation.

They replace the older `fullstack-*` skills previously under `.agents/skills`.
Project requirements belong in each target repository's `AGENTS.md`, relevant
`PRODUCT.md` and `DESIGN.md`, specifications, and source.

## Delegated Development In Codex

Start in Default mode with [fs-dev-plan](fs-dev-plan/SKILL.md). It explores the
repository, resolves intent and implementation questions, and includes test cases
and useful subplans with dependencies and file ownership. Necessary unanswered
questions stop dependent work. Once the plan is complete, an implementation
request continues directly through
[fs-dev-orchestrate](fs-dev-orchestrate/SKILL.md): implementation children work
in separate worktrees while the parent writes tests, integrates, runs validation,
and resolves independent review findings. Final integration and cleanup follow
the authorized execution scope. Push/deployment are included only when authorized.
The plan includes parent-owned worktree cleanup: finished children leave no
disposable worktrees after their outputs are integrated and preserved. Final
handoff verifies the remaining task worktrees are cleaned up too.

For example, "Use fs-dev-plan to implement title search with delegated delivery"
authorizes planning and implementation within that request; it does not require
"Approve this plan?". "Plan title search; do not implement" ends at the plan.
The initial request and accepted answers supply authority, not the agent's plan.

Native Codex Plan mode remains available for planning-only work, but its runtime
restrictions still apply. A skill cannot automatically exit it. Default mode's
clarification workflow is an instruction-based process, not a new client mode;
questioning equivalence with native Plan mode is not guaranteed.

Human View remains the authoritative, human-reviewable product/design meaning.
Routine execution and fixes within an authorized plan do not require repeated
human review. A new material decision returns to the user.

The family is installed together: development planning uses
[shared test design](fs-test-plan/references/test-design.md), and orchestration
uses the implementation, testing, review, and iteration skills. Standalone
implementation and testing remain available. Saved run state supports resuming
an interrupted chat; it does not create an unattended scheduler or guarantee
execution after the app stops. No SDK is required for this app-based workflow.

## Sync To The User-Level Installation

From the HilBridge checkout, preview changes before copying:

```bash
mkdir -p "$HOME/.agents/skills"
rsync -avnc skills/fs-dev-* skills/fs-test-* skills/mcp-plugin-* "$HOME/.agents/skills/"
```

After reviewing the preview, sync the tracked workflows:

```bash
rsync -avc skills/fs-dev-* skills/fs-test-* skills/mcp-plugin-* "$HOME/.agents/skills/"
```

The user-level directories remain installed copies. Edit and commit in this
checkout, then sync when ready. Before syncing, preserve any user-level edits
that should be brought back into Git; matching files will be overwritten.
These commands do not delete files or touch unrelated skills. When intentionally
removing or renaming a skill or supporting file, also remove its obsolete
installed copy after verifying the migration.

Codex discovers `$HOME/.agents/skills` across projects. Existing Claude links
to these installed directories continue to work. Restart a client if it does
not refresh its skill list. Committing to HilBridge does not itself update the
installed copies or another machine.
