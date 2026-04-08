---
identity:
  node_id: "doc:wiki/drafts/3_environment_propagation.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/04_best_practices.md", relation_type: "documents"}
---

"Environment" refers to global contextual values that affect pricing and rule evaluation across the entire component tree: the event date, the hour block, the total guest count, venue capacity, or any other session-level parameters.

## Details

"Environment" refers to global contextual values that affect pricing and rule evaluation across the entire component tree: the event date, the hour block, the total guest count, venue capacity, or any other session-level parameters.

### Where Environment Lives

**Environment must not live inside any component.** A component that owned the event date would need to propagate it to all siblings — breaking the tree's parent-to-child flow. Instead, environment is owned by the application layer (an XState context field at the session/quotation machine level, or a plain object managed by the mounting code).

```js
// Application layer — not inside any component
const sessionEnvironment = {
  dia:       '2026-06-15',
  hora:      'noche',
  paxGlobal: 120,
};
```

### Entering the Tree

The root container is the environment's entry point. When the session environment changes, the root container's actor receives an `UPDATE_ENVIRONMENT` event:

```js
// Root container machine action:
function applyEnvironment(ctx, event) {
  const ruleOutputs = {};  // container evaluates its own rules here
  ctx.domainContainer.receiveContext(event.env);
  ctx.domainContainer.evaluateRules(ctx.evaluator);
  ctx.domainContainer.propagateContext(ruleOutputs); // pushes to all children
}
```

### Merge Semantics: Patch, Not Replace

`receiveContext(patch)` merges the patch into `_inheritedContext`. Existing keys survive unless the patch explicitly overwrites them:

```js
// Time 1: environment sets the date
container.receiveContext({ dia: '2026-06-15', paxGlobal: 120 });
// _inheritedContext = { dia: '2026-06-15', paxGlobal: 120 }

// Time 2: user changes pax — only paxGlobal changes, dia survives
container.receiveContext({ paxGlobal: 150 });
// _inheritedContext = { dia: '2026-06-15', paxGlobal: 150 }  ← correct
```

If `receiveContext` replaced instead of merged, the second call would lose `dia`.

### Mid-Session Environment Changes

When the user changes a session-level value, the flow is:

1. Application layer updates its environment object
2. Sends `UPDATE_ENVIRONMENT` event to root container actor
3. Root container: `receiveContext(patch)` → `evaluateRules()` → `propagateContext(ruleOutputs)`
4. Each child receives `receiveContext(merged)` via propagation
5. Each child re-evaluates its own rules, resolves quantities, recalculates price
6. Each child actor emits a snapshot change → parent re-aggregates

This is a full-tree recalculation triggered by a single event. The propagation model is designed for it.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/04_best_practices.md`.