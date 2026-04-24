---
pill_type: decision
scope: domain
language: en
nature: context
bound_to: 102-105,107-125,129-131
created: 2026-04-24
lifecycle: current
---

# Shim Lifecycle Decision

## Decision

Use shims as temporary migration scaffolding during the in-repo split, then remove them only after adapter routing and import audits prove the old paths are unused.

## Why

- It keeps the move tasks behavior-preserving.
- It makes each package relocation independently testable.
- It prevents `main.py` and command modules from becoming the place where import breakage is discovered.

## Required order

1. Move module into `kgdb` or `ontology`.
2. Leave a shim at the original `wiki_compiler` path.
3. Build adapters where `wiki_compiler` should depend on the new package surface.
4. Reroute commands and `main.py` through adapters.
5. Run import-law audits.
6. Delete shim families in dedicated cleanup tasks.

## Anti-patterns

- Deleting shims in the same task that introduces them.
- Routing commands directly to `kgdb` or `ontology` internals instead of adapters.
- Keeping shims indefinitely after the adapter layer is green.

## Reference

- `desk/tasks/129-remove-kgdb-shims.md`
- `desk/tasks/130-remove-ontology-contract-and-facet-shims.md`
- `desk/tasks/131-remove-ontology-reasoning-and-energy-shims.md`
