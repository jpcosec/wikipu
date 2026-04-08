---
identity:
  node_id: "doc:wiki/drafts/recommended_convergence_plan_option_b.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/actor-ownership-drift-diagnostics.md", relation_type: "documents"}
---

### Stage 1 - Freeze the target contract

## Details

### Stage 1 - Freeze the target contract

Define one canonical component contract:

- `new Component(...)`
- internal actor creation/start
- event-driven public methods
- `getSnapshot()` / `toDisplayObject()`
- `stop()` and deterministic cleanup

### Stage 2 - Item migration with compatibility

1. Introduce actor ownership inside `Item` while preserving current public methods.
2. Re-implement `createItemActor()` as a compatibility wrapper over the actor-owned class.
3. Keep `toDisplayObject()` shape unchanged to avoid breaking category/basket bindings.

### Stage 3 - Container migration (Category -> Catalog -> BasketDay -> Basket)

1. Add actor-owned classes for each container component.
2. Keep existing `createXActor()` factories as thin adapters calling the class API.
3. Move teardown responsibilities into class-owned `stop()` methods.

### Stage 4 - Documentation and tests alignment

1. Update architecture/guides to one canonical pattern.
2. Add contract tests asserting actor ownership and lifecycle cleanup for every component.
3. Remove transitional wrappers only after all integration routes pass.

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/actor-ownership-drift-diagnostics.md`.