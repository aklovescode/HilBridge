---
name: fs-test-plan
description: >-
  Produces an approval-ready automated testing plan in current_task/plan.md
  from the project’s specifications, source, existing tests, fixtures, and
  runners. Chooses the smallest meaningful unit, widget, integration, server,
  or E2E evidence and assigns documentation updates to the owning Flow, Module,
  Contract, Operations, or test-scenario note. Does not implement or edit
  workspace files.
---

# Full-stack Testing — Plan

## Project Context

Read the active project's root and applicable path-local `AGENTS.md` first.
Use that project's stack, test locations, runners, fixtures, discovery tools,
artifact/report paths, and validation commands. The Vision-first paths below
are defaults; honor existing project equivalents and do not create that structure
just to run this workflow. Product and design briefs provide context, while
specifications and explicit user intent define expected behavior.

## Goal

Define deterministic, implementable test coverage for the behavior and risk the
user actually needs protected.

## Authority And Boundary

- Read specs, source, tests, fixtures, runners, logs, and task artifacts. Write
  only `current_task/plan.md`.
- Treat Vision/UI/Flow human sections and relevant Contract/cross-domain
  invariants as expected behavior. Do not infer product behavior from existing
  assertions alone.
- Ask only when a missing product or coverage decision materially changes
  expected behavior, testability, destructive setup, or scope.
- Stop after an approval-ready plan. Do not modify application, tests, specs,
  dependencies, CI, fixtures, or environments.

## Documentation And Evidence Ownership

Read `spec/conventions/Documentation_Conventions.md` and the affected graph:

```text
Vision -> UI Surface -> Flow -> Module -> Code
Vision -> Technical Flow -> Module -> Code
```

- Flow owns the behavioral SIT/integration/E2E decision and exact command.
- Module owns unit/widget/server-unit evidence.
- Contract owns boundary, serialization, and sync evidence.
- Operations owns runbook/operational evidence.
- `spec/test_scenarios/` owns detailed multi-flow E2E setup, steps,
  assertions, and artifacts with bidirectional Flow links.
- Vision contains no test inventory; UI links to evidence rather than
  duplicating commands.

Use the project-configured discovery tools, then direct reads/`rg` for exact notes and paths.

## Existing Test Surface

Discover the project's unit, component/widget, integration, server, and E2E
owners from AGENTS.md, reuse catalogs, source, and existing runners. Reuse its
harnesses, deterministic fixtures, dependency overrides, temporary databases,
client fakes, stable selectors, clocks, and artifact helpers before adding
infrastructure. Do not assume a particular language, database, or test framework.

## Workflow

1. Define the behavior, failure risk, completion criteria, and excluded scope.
2. Read the owning Flow and linked UI/Module/Contract plus nearby tests and
   reusable harnesses.
3. Stop discovery when expected behavior, risk, owner, testability seam,
   fixture, assertions, and commands are supported.
4. Choose the smallest useful layer:
   - unit for pure logic;
   - widget for visible states and isolated interaction;
   - integration/SIT for navigation, providers, and seeded local data;
   - E2E for full-stack or multi-client journeys;
   - server unit/integration according to runtime dependencies.
5. Specify minimal testability changes. Any hook that changes visible behavior,
   schema, API, sync, or ownership is an application change requiring explicit
   plan approval.
6. Define each case with target file, setup, action, assertions, fixtures, and
   dependent implementation.
7. Assign documentation updates to the evidence owner. For a changed E2E
   journey, update the natural owning scenario note or create one only when no
   existing journey owns it; link every exercised Flow both ways.
8. List exact narrow validation commands and wider suites only when their added
   confidence is stated.

## Output

Write:

1. **Scope & Intent**
2. **Relevant Specs**
3. **Existing Test Surface**
4. **Test Strategy**
5. **Automation Implementation Changes**
6. **Planned Test Cases**
7. **Verification Documentation**
8. **Validation Commands**
9. **Risks / Gaps**

State dependencies and completion criteria. Omit speculative alternatives.
End with: **Ready for approval**
