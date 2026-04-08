---
identity:
  node_id: "doc:wiki/drafts/chainable_api_contract.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/02_design_strategy.md", relation_type: "documents"}
---

All mutation methods return `this`. This is a load-bearing convention, not a style preference. It enables fluent construction and update sequences:

## Details

All mutation methods return `this`. This is a load-bearing convention, not a style preference. It enables fluent construction and update sequences:

```js
item
  .setRules(rules)
  .receiveContext(globalContext)
  .evaluateRules(evaluator)
  .resolveQuantities(containerContext)
  .calculatePrice();
```

Without chaining, each of these would require a separate statement with no structural benefit. The pattern also makes the mutation order explicit and readable.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/02_design_strategy.md`.