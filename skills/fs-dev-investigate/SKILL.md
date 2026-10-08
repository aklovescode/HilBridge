---
name: fs-dev-investigate
description: >-
  Investigates a bug or regression against the Vision-first spec graph,
  source, logs, tests, and runtime evidence, then writes a minimal approval-ready
  fix plan in the active planning artifact. Use for root-cause analysis before
  corrective implementation. This skill does not edit workspace code or docs.
---

# Full-stack Dev — Investigate

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

Explain the causal break from intended human behavior to implementation and
propose the smallest fix that restores it.

## Authority And Boundary

- Read specs, code, logs, databases, tests, and runtime state. Use the project's
  discovery tools, language tooling, and debugger evidence when useful.
- Write only the active planning artifact. Do not modify workspace files,
  suppress failures, add features, or redesign behavior.
- Treat the relevant human spec sections as intended behavior and code/runtime
  as evidence. Record a docs/code conflict in the plan rather than choosing
  silently.
- Ask only when missing access or a product decision prevents a supported root
  cause. Stop after the fix plan.

## Documentation And Architecture Context

Read `spec/conventions/Documentation_Conventions.md` and follow the affected
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
4. **Root cause:** identify the first causal break, why it violates intent, and
   which owner must change.
5. **Minimal fix:** name exact files, behavior-preserving correction, required
   regression evidence, and affected documentation notes.
6. Stop tracing when the symptom, violated intent, cause, fix surface, and
   verification are supported. If reproduction is unavailable, record the
   evidence gap instead of widening the search.
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
End with: **Ready for approval**
