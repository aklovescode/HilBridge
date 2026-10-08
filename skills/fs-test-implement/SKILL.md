---
name: fs-test-implement
description: >-
  Implements an approved automated-testing plan with minimal
  behavior-preserving testability hooks, existing harnesses, deterministic
  fixtures, and concrete tests in the project’s stack. Updates the owning
  Vision-first verification and E2E scenario notes, validates, and stages only
  planned paths. Use after fs-test-plan approval.
---

# Full-stack Testing — Implement

## Project Context

Read the active project's root and applicable path-local `AGENTS.md` first.
Use that project's stack, test locations, runners, fixtures, discovery tools,
artifact/report paths, and validation commands. The Vision-first paths below
are defaults; honor existing project equivalents and do not create that structure
just to run this workflow. Product and design briefs provide context, while
specifications and explicit user intent define expected behavior.

## Goal

Deliver the approved automated evidence without weakening expectations or
changing production behavior to make a test pass.

## Authority And Approval Boundary

- Require the approved `current_task/plan.md`.
- Make its in-scope local changes and run non-destructive validation without
  further confirmation.
- Return to `fs-test-plan` when source/spec facts materially conflict with the
  plan or success requires changed behavior, ownership, architecture,
  destructive setup, or expanded scope.
- Do not commit, push, deploy, reset an ambiguous database, or stage unrelated
  dirty work.

## Required Context

Read the plan, `spec/conventions/Documentation_Conventions.md`, owning
Flow/Module/Contract and scenario notes, source, nearby tests, fixtures, and
runners. Use project-configured discovery tools when the plan lacks an exact spec path.

Verification ownership:

- Flow: behavioral SIT/integration/E2E decision and exact command.
- Module: unit/widget/server-unit evidence.
- Contract: boundary/serialization/sync evidence.
- Operations: operational evidence.
- Test scenario: detailed multi-flow journey and artifacts, linked
  bidirectionally with every exercised Flow.

## Implementation Rules

- Extend the project's existing test harnesses before creating new ones.
- Prefer stable selectors, dependency injection/overrides, isolated temporary
  databases, deterministic clocks, sanitized fixtures, existing client fakes,
  and the project's artifact helpers.
- Keep production hooks minimal, planned, and behavior-preserving.
- Keep tests deterministic, isolated, readable, and behavior-focused.
- Do not add feature files, framework churn, unrelated refactors, or
  opportunistic cleanup.
- Preserve unrelated dirty work and exact reset targets.

## Workflow

1. Confirm plan scope, existing dirty state, target environments, and
   completion criteria.
2. Implement planned testability hooks, then harness/fixture support, then
   concrete tests.
3. Update the owning documentation notes. Keep `## Human View` authoritative;
   verification instructions in Derived Delivery Guidance must trace to the
   human behavior and must not add product outcomes.
4. Keep exact commands in one evidence owner and keep scenario/Flow links
   bidirectional.
5. Run the project-required documentation validation when specs change.
6. Run narrow planned tests first, followed by justified broader suites.
7. Inspect the final diff and stage only planned paths.

If an environment is unavailable, preserve the implemented work and report the
exact blocked command and prerequisite; do not guess at a passing result.

## Output

Lead with evidence delivered, plan alignment, testability/product files
changed, documentation ownership updates, commands and results, blockers or
caveats, and staging status. Omit generic process narration.
