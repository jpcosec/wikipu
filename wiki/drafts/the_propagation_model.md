---
identity:
  node_id: "doc:wiki/drafts/the_propagation_model.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/02_design_strategy.md", relation_type: "documents"}
---

Context flows down the tree. This is the primary data distribution mechanism.

## Details

Context flows down the tree. This is the primary data distribution mechanism.

```
ContainerBase.receiveContext(externalPatch)   ← environment enters here
ContainerBase.evaluateRules(evaluator)        ← container evaluates its own rules
ContainerBase.propagateContext(ruleOutputs)   ← merged context pushed to children
  → child.receiveContext(merged)              ← each child receives the patch
  → child.evaluateRules(evaluator)            ← each child evaluates its own rules
```

Key semantics:
- `receiveContext` is a **patch merge**, not a replacement. Existing keys in `_inheritedContext` survive unless the patch explicitly overwrites them.
- `propagateContext` merges the container's own `_inheritedContext` with the freshly computed `ruleOutputs` before pushing to children. Children therefore receive: base environment + container's rule results.
- Children apply their own rules on top of the received context, adding or overriding further.

This model means environment data (e.g., global pax count, date) set once at the root container automatically reaches all leaf items without any leaf needing to query for it.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/02_design_strategy.md`.