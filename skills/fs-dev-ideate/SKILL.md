---
name: fs-dev-ideate
description: >-
  Captures a feature idea as concise human product intent in
  spec/Vision.md and, when needed, shared domain or non-functional meaning in
  cross-domain notes. Use before fs-dev-plan when a user wants product behavior,
  guarantees, business rules, or open decisions documented without designing
  flows, modules, contracts, or code.
---

# Full-stack Dev — Ideate

## Goal

Turn the user’s idea into human-reviewable product intent without hiding design
or implementation decisions in lower-level guidance.

## Authority And Boundary

- Treat the user’s idea and existing human sections in `spec/` as product
  authority. Treat code as evidence of current behavior only.
- Edit only `spec/Vision.md`, directly affected cross-domain notes under
  `spec/architecture_notes/`, and `spec/doc_issues.md`.
- Do not create standalone capability notes. Capabilities are concise headings
  in Vision.
- Do not author UI, Flow, Module, Contract, test-scenario, or implementation
  detail unless the user explicitly expands the task.
- Read and search freely. Ask only when a missing product choice would
  materially change human intent. Stop after the ideation documents and
  non-destructive validation; do not implement, commit, push, or deploy.

## Project Context

Read the target project's root and applicable path-local `AGENTS.md` first.
Use its stack, domain invariants, state ownership, paths, reuse catalogs,
discovery tools, checks, task-artifact conventions, and applicable migration
rules. Read project-local `PRODUCT.md` and `DESIGN.md` when relevant.

Vision-first paths below are defaults; honor project equivalents. Do not import
another project's assumptions or bootstrap missing layers, tools, or validators
unless requested. Use available request/source evidence when guidance is absent;
report missing required context or validation instead of claiming completeness.

## Documentation Context

Read existing project documentation conventions, the relevant Vision
headings, and linked cross-domain notes. Use project-configured discovery tools
when available, then direct reads and `rg` for exact text.

The downstream graph is:

```text
Visible capability:
Vision -> UI Surface -> Flow -> Module -> Code

Capability without UI:
Vision -> Technical Flow -> Module -> Code
```

Contracts hold durable boundaries when useful. Ideation changes only the
upper human authority; later skills author the appropriate lower-layer human
meaning and its derived guidance. Human View means reviewable authority, not a
requirement to interrupt an approved execution for every documentation change.

## Workflow

1. Extract the human outcome, durable business meaning, guarantees, material
   non-goals, and unresolved decisions.
2. Find the existing Vision capability heading and shared domain authority.
   Add a new Vision heading only when no existing heading owns the outcome.
3. Write the minimum product language needed to preserve intent. Keep screen
   structure, sequence, ownership design, code, and test inventories out.
4. Link to existing UI or technical Flows when they already apply. Use
   `spec/doc_issues.md` for a missing lower layer; do not invent a placeholder
   file.
5. If a shared domain or non-functional meaning changes, update the human part
   of its cross-domain note. Update `## Derived Delivery Guidance` only with
   instructions traceable to a named human statement.
6. Run the project-declared documentation checks and report any unavailable
   validation.
7. Check the final diff against the user's idea and the authorized note scope.
   When the next step consumes staged intent, stage only task-owned paths or
   hunks and inspect the index; preserve unrelated existing edits.

## Success Criteria

- A human can identify the intended outcome and material constraint from Vision
  without reading agent guidance.
- No visible behavior or business rule exists only in Derived Delivery
  Guidance.
- The graph remains valid and unresolved choices are explicit.

## Output

Lead with the intent captured, changed notes, validation result, unresolved
decisions, and readiness for `fs-dev-plan`. Cite the actual checks and mark
unavailable evidence; capturing an idea is not implementation approval.
Omit generic process narration.
