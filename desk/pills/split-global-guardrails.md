---
pill_type: guardrail
scope: global
language: en
nature: implementation
bound_to: 101-135
created: "2026-04-24"
lifecycle: current
---

# kgdb + ontology Split Guardrails

## Non-negotiable boundaries

- `kgdb` is graph storage, traversal, and generic query only.
- `ontology` is domain semantics: OWL reasoning, facets, and cleansing detection; energy stays in `wikipu` until task `136` redesigns that boundary.
- `wiki_compiler` remains the workspace application and orchestration layer.

## Move rules

- No task may change runtime behavior intentionally unless that task explicitly says so.
- Package-move tasks prefer shims first, then adapter routing, then shim deletion.
- Do not mix package relocation with physical extraction to sibling repos in the same task.

## Dependency rules

- `src/kgdb/` must not import `ontology` or `wiki_compiler`.
- `src/ontology/` must not import `wiki_compiler`.
- `src/wiki_compiler/commands/` and `src/wiki_compiler/main.py` must not import `kgdb` or `ontology` internals directly once adapter tasks start landing.

## Verification posture

- Every task keeps the existing test baseline stable.
- Import-law greps are part of the acceptance criteria, not optional cleanup.
- If a task reveals a hidden mixed concern, split the task before implementing more code.

## Reference

- `desk/tasks/Board.md`
- `desk/tasks/136-keep-energy-in-wikipu.md`
- `drawers/kgdb-storage-boundary.md`
