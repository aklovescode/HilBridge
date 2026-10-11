---
name: fs-dev-doc
description: >-
  Create or update Vision-first specifications, documentation links, and
  verification mapping. Use for documentation-first work, graph maintenance,
  implementation traceability, or an explicitly requested connected review slice,
  including conversational-agent surfaces and tool flows. Does not implement code.
---

# Vision-first Spec Documentation

Deliver the requested documentation layer or explicit connected slice, with
human intent authoritative and derived guidance traceable to it.

## Authority and boundary

- Default to one requested layer. An explicit slice such as
  `Vision -> Agent UI Surface -> user/tool Flows` authorizes those layers in that
  order; stop at its final layer. Do not infer lower-layer work to complete the graph.
- Edit documentation only. Application code, documentation tooling, or skill
  maintenance requires an explicit request for that work. Do not commit, push,
  deploy, or perform external writes without separate authorization.
- Source code shows current behavior; it does not authorize product meaning.
  Ask when a missing decision materially changes human intent, ownership, or
  the graph. Reuse decisions already supplied for the current scope.
- Keep capability intent as headings in `spec/Vision.md`; create a standalone
  capability note only when explicitly requested.

## Project context

Read the target project's root and applicable path-local `AGENTS.md` first.
Use its documentation conventions, paths, discovery tools, validators, task
artifacts, and applicable migration rules. Read project-local product/design
briefs when relevant; do not import the skill installation repository's assumptions.

Read the request, every referenced note, and relevant existing authority. Read
`spec/conventions/Documentation_Conventions.md` and
`spec/architecture_notes/Cross_Cutting_Concerns.md` when present and relevant.
Follow project equivalents; do not bootstrap absent layers or tooling merely
for this workflow. Use project discovery tools, then direct reads and `rg`.
Inspect source for implementation mapping or drift. Verify changeable third-party
host/protocol facts against current official documentation before asserting them.

Read the applicable sections of [specification structure](references/spec-structure.md)
before choosing an owner, authoring that note type, or moving verification evidence.
It contains graph/link rules, note responsibilities, conversational-agent guidance,
and verification ownership; do not load unrelated note-type detail.

## Human authority and derived guidance

**Human View** is the complete human-reviewable statement of intended behavior,
meaning, guarantees, or design at that note's layer. It may be technical: Module
responsibility and Contract invariants belong here. **Derived Delivery Guidance**
turns that authority into implementation and verification instructions, mappings,
and constraints. For example, "Cancel leaves the saved record unchanged" is
human authority; "persist only on Save and verify Cancel preserves stored state"
is guidance derived from that statement.

Human reviewability does not require a separate approval for every in-scope edit.
An approved development plan authorizes its specified updates; ask again only
when the proposed meaning exceeds accepted intent. A documentation-only request
still stops at its requested review boundary.

Vision's content above `## Derived Delivery Guidance` is human authority. Other
product/spec notes put `## Human View` above the complete human part and
`## Derived Delivery Guidance` below it.

- Derive every delivery instruction from a named human statement or exact heading.
  A human section may adopt a directly linked Vision, Contract, or cross-domain
  requirement; say which applies before deriving it. Use short stable IDs only
  when headings are insufficient.
- Guidance may specify boundaries, ownership, code mapping, verification, and
  stopping points. It cannot introduce visible behavior, business rules, outcomes,
  or exceptions. If the request supplies missing intent, record it in the human
  part before deriving it. Otherwise surface the proposed decision for human
  review before proceeding with dependent guidance.
- Preserve human intent when code differs; record unresolved drift in
  `spec/doc_issues.md`. Prefer links over duplicated requirements.
- Skills, manifests, tool descriptions, and widgets are derived delivery artifacts;
  they must not become the sole authority for product meaning or guarantees.

## Workflow

1. Establish the requested layer/slice, human outcome, affected notes, and explicit
   exclusions. Apply any project-specific migration gate only to migration work.
2. Inspect existing authority and select the natural owner: Vision for intent,
   UI Surface for behavior in place, Flow for behavior through time, Module for
   program design, Contract for a durable boundary, and cross-domain/Operations/
   scenario notes for their shared meaning, procedures, or detailed journeys.
3. Edit in authority order within the approved scope. Keep each statement in its
   owner and use direct relative links with heading fragments. Establish a moved
   statement's new authoritative home before removing its duplicate.
4. Record unresolved decisions, missing traceability, and unrequested lower-layer
   work in `spec/doc_issues.md` or the owning note's `Backlog`. Link real existing
   destinations; do not invent placeholder files or cascade to another layer.
5. Validate before handoff: run project-declared documentation checks; check
   changed links/fragments, source paths, PlantUML, human/derived ordering, and
   derivation against the request. Check applicable capability-to-surface/technical
   Flow links, Agent Surface-to-user/tool Flow links, Flow/scenario backlinks,
   fallback behavior, and single-owner verification commands. Report missing
   coverage or unavailable validators/runtime rather than calling it a pass.
6. Inspect the final diff against the requested layer/slice. Stage only task-owned
   paths or hunks when requested or required by the project workflow; preserve
   unrelated edits. Stop at the authorized documentation boundary.

For example, a request for an Agent Surface and its user/tool Flows does not
permit a new Module, Contract, server handler, or package just because a link is
missing. Record that gap and retain the requested review boundary.

## Handoff

Report changed notes, validation commands/results, material gaps, unresolved
product decisions, and the next review layer. End `Ready for review of <layer or
slice>` only after validation; distinguish readiness for review from complete
verification. Omit generic process narration.

`fs-dev-ideate` captures upper product intent; `fs-dev-plan` plans development and
tests in actual Plan mode; `fs-dev-orchestrate` coordinates approved delegated
delivery. Implementation/iteration update authorized code and affected notes;
`fs-dev-review` checks a staged or committed result without fixing it.
