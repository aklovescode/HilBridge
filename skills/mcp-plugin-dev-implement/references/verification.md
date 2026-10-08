# Verification and recovery for MCP Apps

Choose checks that prove the changed contract. This is not a requirement to run
every layer for a metadata-only or guidance-only change. Record each relevant
layer as passed, failed, or unrun with its evidence and limitation.

## Catalog and service boundary

Use the actual supported transport to exercise initialization, `tools/list`,
resource discovery/read, and representative calls. Assert the emitted contract:

- Input/output schemas describe the actual accepted and returned values, including
  nested results and meaningful optional/null semantics. Validate outputs too.
- Tool names, descriptions, side-effect annotations, security schemes, and
  model/app visibility agree with behavior. Auth is enforced by the service;
  annotations and client metadata are not an authorization boundary.
- The producing tool points to an existing resource, and `resources/read` returns
  the intended HTML/MIME type plus appropriate resource metadata. For changed
  shared metadata, check every affected template, not just the first one.
- Validation and operational failures have useful, distinguishable results;
  callers can identify a correctable field without receiving private payloads.

For ChatGPT's current field placement and compatibility rules, consult the
[official reference](https://developers.openai.com/plugins/reference). Validate
what the installed SDK actually serializes; typed handlers and successful calls
alone can miss absent advertised schemas or metadata.

When auth or writes change, test the relevant unauthorized identity, cross-account
access, stale preview, duplicate retry, and concurrency cases with synthetic or
disposable data. A presentation-only change does not require a production write.

## Widget and bridge

Exercise the built bundle through a bridge harness or real supported host, not
only by opening standalone HTML. Cover the changed event path, including missing
initial input, delayed result, mismatched operation identity, or repeated events
where they can occur. Approval-gated hosts may intentionally withhold arguments
until approval; do not bypass this or treat it as corruption.

Check the states affected by the feature: loading, populated, partial, empty,
error, stale, unsupported, and expired preview. Verify responsive layout and
keyboard-accessible controls for notable UI work. Keep already-loaded navigation
local and confirm refresh/follow-up actions preserve source identity.

A host-independent harness establishes renderer behavior only. It does not prove
that a particular host discovers tools, delivers bridge events, renders the card,
or supports the same behavior on mobile.

## Conversation and live integration

Start a fresh conversation in the requested host/account when authorized and
available. Verify the intended plugin/skill configuration; do not silently enable
an optional skill to make a plugin-only test pass. Try an ordinary user request
without handing the model a fully formed tool payload.

Pick realistic cases from the affected journey:

| Change | Useful behavior to observe |
|---|---|
| Onboarding/guidance | Natural starter, only missing context requested, complete proposal, intended connector path |
| Preview/mutation | Full review appears before confirmation; exact accepted scope is applied and verified |
| Dashboard | Correct identity and dates, unlogged versus zero, partial settings, post-write view |
| Follow-up | No repeated app mention needed; retained identity; explicit refresh gets fresh source data |
| Date handling | Backdated entries, midnight/timezone rollover, period boundaries relevant to the contract |
| Recovery | Actionable invalid-input response; bounded correction; text fallback without a duplicate write |

Inspect visible behavior and raw calls/results where available. A transcript that
says “tool unavailable” does not establish an outage; a message-only reader cannot
prove which tool was called. If actual host or device access is unavailable, retain
the acceptance case and label it unverified rather than simulating a pass.

For live connector tests, verify available operations and the intended account,
use an authorized disposable destination, and perform source readback. Do not
reseed personal data or publish/share a fixture merely to complete testing. Native
formula correctness, recalculation timing, and copy permissions need provider-side
evidence when those behaviors are in scope.

## Diagnosis and retries

Locate the first failing boundary before choosing a fix:

| Evidence | Next check |
|---|---|
| Tool absent or host warning | Discovery metadata, package/connection version, auth, host refresh |
| Call rejected | Capture the minimal failing input; inspect schema, coverage, date and unit constraints |
| Result accepted but blank UI | Resource link/fetch, asset/CSP errors, bridge event delivery and identity |
| Write succeeded but display failed | Preserve receipt and write result; repair presentation or give text |
| Timeout during a write | Read back or check the idempotency record before any repeat |
| Missing service logs | Confirm instrumentation coverage; absence alone proves nothing |

For a field-correctable presentation error, normally make one correction from the
same verified evidence. For repeated or opaque failures, stop automatic retries
and surface the useful fallback plus the actual blocker. Retries must have a
reason to succeed and must preserve source freshness and mutation semantics.

When instrumentation is necessary, use payload-free method/stage/status/duration
and safe correlation tokens. Do not log user datasets, auth material, or private
source identifiers. Compare known-good and failing cases before blaming a device,
host, proxy, or deployment platform.

## Package, release, and performance evidence

Run applicable build/package validators and inspect the generated archive or
manifest. Check that referenced guides, UI assets, and resources exist and agree
with source. Do not assume a host honors a packaged “Try in chat” prompt; verify
the observed host behavior if it is part of the outcome.

After authorized release, compare the exact deployed revision or asset hashes,
tool catalog, resource metadata, and representative endpoint behavior. Confirm
host metadata refresh when required; do not equate deployment with adoption by
an already-open conversation. Record rollback and co-hosted service checks where
the deployment topology makes them relevant.

For optimization, compare the same journey and dataset before/after. Report call
counts, bytes, service time, and end-to-end latency separately, including cache
state and sample limitations. Keep correctness and freshness checks intact.
