---
identity:
  node_id: "doc:wiki/drafts/the_injected_function_design.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/02_design_strategy.md", relation_type: "documents"}
---

Domain mixins define *slots* for behavior, not the behavior itself:

## Details

Domain mixins define *slots* for behavior, not the behavior itself:

| Mixin | Slot | Type |
|-------|------|------|
| `Prizable` | `_pricingFn` | `(profile, pax, cantidad, duracion) => number` |
| `Rulable` | `_evaluator` | `(rule, context) => object | null` |
| `Actorlike` | `_actorRef` | XState actor reference |

This has three consequences:

1. **Testability** — Mixin tests use mock functions. The mixin's logic is tested in isolation without a domain setup, a running actor, or real rules.

2. **Substitutability** — The pricing algorithm can change without touching the `Item` class. The rule evaluator can be swapped for a different implementation per environment.

3. **Explicit wiring** — Nothing happens automatically. A component that has not received its pricing function calculates `null`. This is intentional: a component that fails silently is harder to debug than one that produces null and makes the missing dependency visible.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/02_design_strategy.md`.