---
name: fs-test-run
description: >-
  Runs the smallest relevant project unit, integration, server, or E2E tests;
  analyzes logs and artifacts against the Vision-first specification graph;
  classifies product bugs, test defects, environment blockers, and known gaps;
  and writes current_task/changes_summary.md. Use for validation and test triage. Does not
  fix code, tests, or documentation.
---

# Full-stack Testing — Run And Triage

## Project Context

Read the active project's root and applicable path-local `AGENTS.md` first.
Use that project's stack, test locations, runners, fixtures, discovery tools,
artifact/report paths, and validation commands. The Vision-first paths below
are defaults; honor existing project equivalents and do not create that structure
just to run this workflow. Product and design briefs provide context, while
specifications and explicit user intent define expected behavior.

## Goal

Report whether the intended behavior passed and localize failures with enough
evidence for the smallest correct next action.

## Authority And Boundary

- Read specs, source, tests, plans, logs, reports, and artifacts; run safe,
  non-destructive tests and inspections.
- Write the project-designated test report (default: `current_task/changes_summary.md`);
  capture generated reports/artifacts only in the project-designated location.
- Do not change application, tests, fixtures, specs, plans, assertions, or
  environments. Do not suppress or fix failures.
- Stop after the report. Record an evidence-backed blocker when prerequisites
  are unavailable.

## Choose Evidence

Read `spec/conventions/Documentation_Conventions.md` and the owning notes:

- Flow Derived Delivery Guidance for behavioral SIT/integration/E2E commands.
- Module for unit/widget/server-unit commands.
- Contract for boundary/serialization/sync commands.
- Operations for operational checks.
- `spec/test_scenarios/` plus every linked Flow for named multi-flow journeys.

Use Vision/UI human sections and Contract/cross-domain invariants to judge
expected behavior. Use the current plan first when it names exact commands.
Use project-configured discovery tools and direct reads for exact authority.

Run the smallest relevant suite first and widen only when the result needs
additional localization or confidence. Do not use retired feature-file runners.

## Workflow

1. Establish target behavior, environment, owning evidence note, and exact
   command. Confirm destructive setup targets before allowing a runner to reset
   state.
2. Run and capture command, pass/fail result, assertion, stack trace, logs,
   screenshots, scenario artifacts, and environment facts.
3. Rerun a focused failing case when ordering, fixture state, or flakiness is
   plausible. Preserve both results.
4. Classify each failure:
   - **Product bug:** implementation violates authoritative behavior.
   - **Test bug:** assertion, fixture, harness, or expected state is wrong.
   - **Environment blocker:** required database, device, credential, service,
     network, or setup is unavailable.
   - **Known gap:** the owning documentation already records missing coverage
     or implementation.
5. For a product bug, identify the violated human statement/invariant, first
   causal layer, likely files, minimal reproduction, severity, and rerun
   command. Do not claim root cause beyond the collected evidence.
6. Stop when each failure is classified and the next action is clear.

## Output

Write:

1. **Execution Summary**
2. **Relevant Specs**
3. **Environment Notes**
4. **Bugs** — one evidence-backed subsection per product bug
5. **Non-bug Failures**
6. **Recommended Next Step**

If no product bug is found, state that explicitly. Lead the user handoff with
pass/fail status, material evidence, caveats, and the smallest next action.
