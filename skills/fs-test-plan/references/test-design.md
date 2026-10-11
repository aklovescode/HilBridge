# Test Design For An Approved Development Outcome

Use from `fs-dev-plan` for its integrated testing section, or from `fs-test-plan`
for a testing-only task. The plan is the approval unit; this reference does not
require a second approval for tests already covered by that plan.

## Choose Evidence

Read applicable project instructions, relevant specs/source, nearby tests,
fixtures, and runners. Use human intent and durable Contract/cross-domain
invariants as expected behavior. Existing code/assertions show current behavior,
not permission to change the expected result.

Reuse the project's harnesses, deterministic fixtures, dependency overrides,
temporary databases, client fakes, stable selectors, clocks, and artifact helpers.
If no runner exists, name the smallest justified setup in the plan or explain
why existing runtime checks suffice. Do not introduce a framework by default.

Choose the smallest useful layer: unit for pure logic, component/widget for
isolated UI states, integration for cooperating components and seeded data,
E2E for full journeys, and boundary checks for contracts. Include relevant
failure, recovery, and regression cases. Trivial reversible edits need no
artificial test. State wider checks only when they add identifiable confidence.

## Each Planned Case

Specify the authoritative criterion, target file, setup/fixture, action,
expected observable result, and exact runnable command. Include implementation
dependencies, environment prerequisites, and documentation owner where needed.
Assertions should protect approved behavior rather than repeat implementation.

For example, an approved rule that invalid input leaves stored data unchanged
needs a case that supplies invalid input, checks the defined failure result,
and independently inspects unchanged stored state. Checking only the handler's
success/failure message cannot establish persistence behavior.

For delegated delivery, assign tests/fixtures/harness configuration to the
parent and production testability hooks to the appropriate implementation child.
Specify the seam/interface before dispatch. A hook that changes behavior,
schema, API, or ownership needs to be included in the approved application plan.
Allow final test wiring after integration without revising accepted expectations.

## Documentation And Completion

Follow project equivalents for these owners:

- Flow: behavioral integration/SIT/E2E decisions and commands.
- Module: unit/widget/server-unit evidence.
- Contract: boundary/serialization/sync evidence.
- Operations: operational validation.
- Test scenario: detailed multi-flow journeys with bidirectional Flow links.

Vision holds no test inventory; UI links to evidence rather than duplicating
commands. Keep exact commands in their natural owner.

Distinguish planned, authored, executed, and passed coverage. Bind final evidence
to the actual candidate tree and environment. Reuse current evidence unless
relevant source, fixtures, requirements, or environment changed. Missing devices,
credentials, or services are explicit gaps, not passing checks.
