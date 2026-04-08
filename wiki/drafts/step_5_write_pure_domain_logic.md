---
identity:
  node_id: "doc:wiki/drafts/step_5_write_pure_domain_logic.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/GUIDES/creating-a-component.md", relation_type: "documents"}
---

**File:** `domain/index.js`

## Details

**File:** `domain/index.js`

```javascript
/**
 * Pure functions for MyComponent calculations
 * No side effects, no I/O, no machine access
 */

export function clampValue(value, min, max) {
  return Math.max(min, Math.min(max, value));
}

export function validateValue(value, definition) {
  const { min = -Infinity, max = Infinity } = definition;
  
  if (value < min) {
    return {
      valid: false,
      error: `Value must be at least ${min}`,
    };
  }
  
  if (value > max) {
    return {
      valid: false,
      error: `Value must be at most ${max}`,
    };
  }
  
  return { valid: true, error: null };
}

export function formatValue(value, definition) {
  const { prefix = '', suffix = '' } = definition;
  return `${prefix}${value}${suffix}`;
}
```

---

Generated from `raw/docs_cotizador/docs/GUIDES/creating-a-component.md`.