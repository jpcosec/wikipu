---
identity:
  node_id: "doc:wiki/drafts/key_constraints.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/component-architecture.md", relation_type: "documents"}
---

### ✅ DO

## Details

### ✅ DO

- Keep domain functions pure (no side effects, no I/O)
- Use XState for state transitions and lifecycle
- Define all component-scoped rules in the definition
- Test pure functions independently
- Use Alpine.js for reactive UI binding only
- Cache rule evaluation results

### ❌ DON'T

- Access database from domain functions
- Modify component definition after initialization
- Call machine methods directly (use public API)
- Store derived state (recalculate on access)
- Mix async operations into domain logic
- Hardcode business rules (use JSON-Logic)

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/component-architecture.md`.