---
identity:
  node_id: "doc:wiki/drafts/domain_logic_layer.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/component-architecture.md", relation_type: "documents"}
---

Pure functions isolated from state machine and UI:

## Details

Pure functions isolated from state machine and UI:

```javascript
// domain/calculations.js
export function calculateComponentValues(definition, state, rules) {
  // No side effects, no machine access
  // Returns component-specific calculated values
}

// domain/formatting.js
export function formatDisplayString(component, format) {
  // Convert component state to human-readable string
  // Returns string suitable for UI display
}

// domain/index.js
// Re-export domain functions for clean public API
export { calculateComponentValues, formatDisplayString };
```

**Benefits:**
- ✅ Testable without mocking
- ✅ Reusable in different contexts
- ✅ Easy to understand (no state machine complexity)
- ✅ Fast (no async, no I/O)

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/component-architecture.md`.