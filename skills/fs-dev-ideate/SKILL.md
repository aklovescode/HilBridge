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

## Documentation Context

Read `spec/conventions/Documentation_Conventions.md`, the relevant Vision
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
upper human authority; later skills derive the lower layers.

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
7. Stage only the documentation paths changed by this skill when the next step
   will consume staged intent.

## Success Criteria

- A human can identify the intended outcome and material constraint from Vision
  without reading agent guidance.
- No visible behavior or business rule exists only in Derived Delivery
  Guidance.
- The graph remains valid and unresolved choices are explicit.

## Output

Lead with the intent captured, changed notes, validation result, unresolved
decisions, and readiness for `fs-dev-plan`. Omit generic process narration.
