---
pill_type: warning
scope: component
language: en
nature: implementation
bound_to: 120-131
created: 2026-04-24
lifecycle: current
---

# Adapter Import Law

## What counts as success

- `wiki_compiler` command modules call adapters, not package internals.
- `wiki_compiler.main` calls adapters, not package internals.
- The adapter layer is thin: translation, delegation, small compatibility helpers only.

## What not to do

- Do not move business logic into adapters.
- Do not let adapters become a second implementation layer.
- Do not import `kgdb` or `ontology` directly from arbitrary `wiki_compiler` modules once routing tasks begin.

## Audit rules

- `src/wiki_compiler/commands/` should be boundary-clean after command-routing tasks.
- `src/wiki_compiler/main.py` should be boundary-clean after the main-routing task.
- Any remaining direct imports from `kgdb` or `ontology` inside `src/wiki_compiler/` must be limited to `src/wiki_compiler/adapters/`.

## Preferred adapter split

- store
- query
- energy
- cleanse
- reasoning
- facets

If a new adapter need appears that does not fit these six, stop and check whether the task graph needs another atomization pass.

## Reference

- `drawers/executable-extraction-plan.md`
