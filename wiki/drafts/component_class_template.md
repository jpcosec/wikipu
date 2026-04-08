---
identity:
  node_id: "doc:wiki/drafts/component_class_template.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/component-architecture.md", relation_type: "documents"}
---

Every component follows this structure:

## Details

Every component follows this structure:

```javascript
// packages/components/<component>/MyComponent.js

export class MyComponent {
  #definition       // Private: component definition + rules
  #machine          // Private: XState actor
  #uiState          // Private: Alpine.js reactive state
  #userSetFields    // Private: track manual overrides

  constructor(definition, context = {}) {
    this.#definition = definition;
    // Initialize private fields
  }

  // Lifecycle methods
  async initialize() {
    // Setup machine, context, initial state
  }

  // State getters
  toDisplayObject() {
    // Return UI-friendly state snapshot
  }

  toSeed() {
    // Return serializable state for storage
  }

  static fromSeed(seed, definition) {
    // Load component from persisted state
  }

  // User-facing methods
  setMode(mode) {
    // Transition between display modes
  }

  setOverride(field, value) {
    // Mark field as user-set, update context
  }

  clearOverride(field) {
    // Clear user-set marker
  }

  // Internal: sync methods
  #syncCalculations() {
    // Recalculate domain values (pricing, quantity, rules, etc.)
  }

  #syncUI() {
    // Push changes to Alpine.js
  }
}
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/component-architecture.md`.