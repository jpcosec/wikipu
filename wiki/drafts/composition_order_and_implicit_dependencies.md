---
identity:
  node_id: "doc:wiki/drafts/composition_order_and_implicit_dependencies.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/01_system_overview.md", relation_type: "documents"}
---

The order in which mixins appear matters — innermost is applied first, outermost is applied last and sits highest in the prototype chain.

## Details

The order in which mixins appear matters — innermost is applied first, outermost is applied last and sits highest in the prototype chain.

```
Alpineable              ← outermost (highest in prototype chain)
  Storable
    Rulable             ← provides _inheritedContext read by Prizable
      Prizable          ← reads _inheritedContext (initialized by Rulable)
        Actorlike       ← innermost
          class {}      ← empty root
```

Two implicit dependencies exist between domain mixins:

1. **Prizable → Rulable**: `resolveQuantities()` reads `this._inheritedContext`. This field is initialized to `{}` by `Rulable`. Without `Rulable` in the chain, `_inheritedContext` is `undefined` and falls back via `?? {}` — correct behavior, but only by accident.

2. **Rulable → Aggregable** (containers only): `propagateContext()` iterates `this._children?.values?.()`. `_children` is a `Map` initialized by `Aggregable`. On an item (no `Aggregable`), `this._children` is `undefined`, the optional chain returns `undefined`, and the loop is skipped — again, correct by accident, not by design.

These dependencies are **not enforced** at composition time. The base classes pair the right mixins by convention.

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/01_system_overview.md`.