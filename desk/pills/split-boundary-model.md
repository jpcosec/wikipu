---
pill_type: model
scope: domain
language: en
nature: context
bound_to: 101-131
created: "2026-04-24"
lifecycle: current
---

# Split Boundary Model

## Package ownership map

| Layer | Owns | Must not own |
|---|---|---|
| `kgdb` | graph contracts, graph persistence, graph traversal, generic structured query, graph CLI | OWL, facets, energy, cleansing rules, workspace policy |
| `ontology` | domain contracts, OWL backend, reasoner, OWL audit, energy audit, facet registry/injectors/validator, cleansing detection | filesystem mutation, repo policy, graph storage implementation |
| `wiki_compiler` | CLI orchestration, workspace scanning policy, markdown build flow, cleansing apply side, adapter layer | direct ownership of moved package logic |

## Mixed-module split targets

| Module | Goes to `kgdb` | Goes to `ontology` | Stays in `wiki_compiler` |
|---|---|---|---|
| `context.py` | neighborhood traversal | - | task hydration, checklist loading, rendering |
| `scanner.py` | - | entity extraction | project discovery, exclusions, scan policy |
| `builder.py` | - | edge inference, compliance scoring | wiki compilation, orchestration |
| `cleanser.py` | - | detection/proposal rules | apply/execution side |

## Public surfaces to preserve during migration

- Existing `wiki_compiler.*` imports stay valid through temporary shims.
- New package APIs must be importable directly before any shim is deleted.
- Adapter modules are the only long-term bridge from `wiki_compiler` into split-package internals.

## Reference

- `drawers/diagrams/target_architecture.md`
- `drawers/kgdb-module-ownership-audit.md`
