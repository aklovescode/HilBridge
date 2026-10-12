---
name: fs-test-implement
description: >-
  Implements an authorized automated-testing plan with minimal
  behavior-preserving testability hooks, existing harnesses, deterministic
  fixtures, and concrete tests in the project’s stack. Updates the owning
  Vision-first verification and E2E scenario notes, validates, and stages only
  planned paths. Accepts an authorized fs-test-plan or the testing section of an
  authorized fs-dev-plan, including parent-owned tests during delegated delivery.
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

Deliver the authorized automated evidence without weakening expectations or
changing production behavior to make a test pass.

## Authority And Approval Boundary

- Require the completed test plan or integrated development plan's testing
  section, from the session or saved project/run artifact, within the user's
  implementation request/accepted decisions or explicit plan approval. See
  [plan authority](../fs-dev-plan/SKILL.md#authority-and-boundary). Do not demand
  a second approval or a particular filename; a planning-only request remains
  planning-only.
- Make its in-scope local changes and run non-destructive validation without
  further confirmation.
- Return to the owning planning workflow when source/spec facts materially
  conflict with the plan or success requires changed behavior, ownership, architecture,
  destructive setup, or expanded scope.
- Local checkpoint commits follow recorded task authority in the orchestration
  plan. Honor that authority without asking again; do not infer push/deployment
  or destructive reset authority. Preserve unrelated dirty work.

## Required Context

Read the plan, existing project documentation conventions, owning
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

## Parent Role In Delegated Delivery

The parent writes tests, fixtures, and harness/configuration changes in its
integration worktree while implementation children work elsewhere. Production
testability hooks belong to their assigned child; communicate the authorized seam
instead of editing that child's paths. The parent owns assigned shared specs and
verification notes to avoid competing documentation edits.

Build tests from authorized behavior, not the child's completion claims. Author
against agreed interfaces and finish wiring after integration. Capture useful
baseline failures when runnable, but do not describe missing implementation as
a final test result. Defer implementation-dependent tests until the candidate is
integrated; the orchestration parent runs final tests alongside independent review.

## Workflow

1. Confirm plan scope, existing dirty state, target environments, and
   completion criteria.
2. Implement planned harness/fixture support and concrete tests. In standalone
   work also implement authorized minimal production hooks; in delegated work
   coordinate those hooks with their assigned owner.
3. Update the owning documentation notes. Keep `## Human View` authoritative;
   verification instructions in Derived Delivery Guidance must trace to the
   human behavior and must not add product outcomes.
4. Keep exact commands in one evidence owner and keep scenario/Flow links
   bidirectional.
5. Run the project-required documentation validation when specs change.
6. Run narrow runnable tests first, followed by justified broader suites. During
   parallel development, record deferred checks and their prerequisites; after
   integration run them against the recorded candidate without concurrent edits.
7. Inspect the final diff and stage only planned paths.

If an environment is unavailable, preserve the implemented work and report the
exact blocked command and prerequisite; do not guess at a passing result.
Record command, result, source tree, and environment with the evidence. Test
authoring complete is distinct from validation complete.

## Output

Lead with evidence delivered, plan alignment, testability/product files
changed, documentation ownership updates, commands and results, blockers or
caveats, and staging status. Omit generic process narration.
