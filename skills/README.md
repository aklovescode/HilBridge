# Shared Development Skills

Maintain these project-neutral workflows here and commit changes to HilBridge:

- `fs-dev-*`: product documentation, investigation, planning, implementation,
  review, and iteration.
- `fs-test-*`: test planning, implementation, and execution.
- `mcp-plugin-*`: MCP/plugin planning and implementation.

They replace the older `fullstack-*` skills previously under `.agents/skills`.
Project requirements belong in each target repository's `AGENTS.md`, relevant
`PRODUCT.md` and `DESIGN.md`, specifications, and source.

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
