---
name: fs-dev-investigate
description: >-
  Investigates a bug or regression against the Vision-first spec graph,
  source, logs, tests, and runtime evidence, then writes a minimal approval-ready
  fix plan in the active planning artifact. Use for root-cause analysis before
  corrective implementation. This skill does not edit workspace code or docs.
---

# Full-stack Dev — Investigate

## Goal

Explain the causal break from intended human behavior to implementation and
propose the smallest fix that restores it.

In an approved orchestration loop, use this skill when a failure needs root-cause
investigation; send findings to the parent. Routine repairs already covered by
the approved plan use `fs-dev-iterate` without another human approval. A proposal
that changes accepted behavior still returns to planning.

## Authority And Boundary

- Read specs, code, logs, databases, tests, and runtime state. Use the project's
  discovery tools, language tooling, and debugger evidence when useful. Keep
  inspections read-only and use non-destructive reproductions; live writes or
  destructive setup need separate authorization.
- Write only the active planning artifact. Do not modify workspace files,
  suppress failures, add features, or redesign behavior.
- Treat the relevant human spec sections as intended behavior and code/runtime
  as evidence. Record a docs/code conflict in the plan rather than choosing
  silently.
- Ask only when missing access or a product decision prevents a supported root
  cause. Stop after the fix plan.

## Project Context

Read the target project's root and applicable path-local `AGENTS.md` first.
Use its stack, domain invariants, state ownership, paths, reuse catalogs,
discovery tools, checks, task-artifact conventions, and applicable migration
rules. Read project-local `PRODUCT.md` and `DESIGN.md` when relevant.

Vision-first paths below are defaults; honor project equivalents. Do not import
another project's assumptions or bootstrap missing layers, tools, or validators
unless requested. Use available request/source evidence when guidance is absent;
report missing required context or validation instead of claiming completeness.

## Documentation And Architecture Context

Read existing project documentation conventions and follow the affected
path:

```text
Vision -> UI Surface -> Flow -> Module -> Code
Vision -> Technical Flow -> Module -> Code
```

Use Contracts for durable invariants and cross-domain notes for shared
architecture, domain, security, or sync meaning. Behavioral evidence belongs to
Flows; unit evidence to Modules; boundary evidence to Contracts.

Preserve the architecture, state ownership, persistence, and interface
constraints declared in the target project's `AGENTS.md` and linked specs.

## Workflow

1. **Observed problem:** record the visible/system symptom, impact, exact
   reproduction, and current evidence without hypothesizing.
2. **Intended behavior:** cite the Vision/UI/Flow human statements and any
   Contract invariant that define what should happen.
3. **Runtime path:** trace the narrow path through the relevant interface,
   application logic, integrations, and persistence. Correlate tool output with
   source and logs.
4. **Root cause:** identify the first supported causal break, why it violates
   intent, and which owner must change. Distinguish observations, hypotheses,
   and confirmed causes; an opaque provider rejection is not proof of a bug
   in the submitted data or application.
5. **Minimal fix:** name exact files, behavior-preserving correction, required
   regression evidence, and affected documentation notes.
6. Stop tracing when the symptom, violated intent, cause, fix surface, and
   verification are supported. If reproduction is unavailable, record the
   evidence gap instead of widening the search or inventing certainty. Reuse
   current evidence until the relevant source, environment, or symptoms change.
7. If the fix would introduce behavior absent from the human authority, return
   to product planning rather than hiding it in Derived Delivery Guidance.

## Output

Write:

1. **Bug Summary**
2. **Relevant Specs**
3. **Intended Behavior**
4. **Root Cause Analysis**
5. **Proposed Fix**
6. **Validation**
7. **Risk Assessment**

Include the project-declared documentation checks when the fix changes specs.
For a new fix plan, end with **Ready for approval**. For investigation inside an
approved run, identify the violated criterion, supported cause, and in-scope next
action; distinguish any new decision that actually needs approval.
