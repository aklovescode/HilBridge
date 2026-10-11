---
name: fs-test-plan
description: >-
  Plans automated coverage for a testing-only task using specs, source, existing
  harnesses, fixtures, and runners. Produces concrete cases and commands without
  implementation. Its shared test-design reference also supplies the testing
  section of fs-dev-plan; those tests need no separate planning approval.
---

# Full-stack Testing — Plan

Define implementable coverage for approved behavior and actual risk. Use
`fs-dev-plan` when application development and tests need one integrated plan.

## Authority And Context

- Read the project's applicable `AGENTS.md`, specs, source, tests, runners, and
  artifact conventions. Use existing project equivalents; do not invent missing
  spec layers or require a path that the project does not have.
- Treat human spec sections and Contract/cross-domain invariants as expected
  behavior. Code and existing assertions are evidence of current behavior.
- Ask only for missing decisions that materially change expected behavior,
  coverage, testability, destructive setup, or scope. Reuse accepted decisions.
- In actual Plan mode, output only its native planning response/artifact; do not
  write workspace files. Outside Plan mode, use the project's designated plan
  document (default `current_task/plan.md`) without overwriting unrelated work.
  Do not implement application code, tests, fixtures, dependencies, or CI.

## Workflow

1. Establish intended behavior, failure risk, completion criteria, and scope.
2. Read [test design](references/test-design.md), the owning specs, source,
   nearby tests, reusable fixtures, and actual runnable commands.
3. Define the smallest meaningful cases and any justified harness or testability
   work. Stop discovery when expected behavior, owner, fixture, assertions,
   environment, and commands are supported.
4. Assign changes to exact files and documentation owners. Identify prerequisites
   and missing coverage; do not present planned tests as executed evidence.
5. Return the approval-ready test plan and stop before implementation.

## Output

Include scope, relevant authority, existing test surface, planned cases with
setup/action/expected results, file-specific automation changes, documentation
ownership, commands, dependencies, and gaps. Prefer the project's format over
an extra template. End with **Ready for approval**.
