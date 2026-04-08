---
identity:
  node_id: "doc:wiki/drafts/integration_with_item_component.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/rules-engine-integration.md", relation_type: "documents"}
---

### Initialization

## Details

### Initialization

```javascript
// Item.js constructor
export class Item {
  #rulesCoordinator;

  constructor(definition, context = {}) {
    this.#definition = definition;
    
    // Create coordinator for ITEM scope rules
    this.#rulesCoordinator = new RulesCoordinator(
      'ITEM',
      definition.rules || []
    );
  }
}
```

### Evaluation (in calculate())

```javascript
// Item.js calculate() method
calculate() {
  // ... compute quantities and pricing ...
  
  // Create snapshot for rule evaluation
  const snapshot = {
    itemId: this.#definition.itemId,
    kind: this.#definition.kind,
    category: this.#definition.category,
    pax: this.state.quantities.pax,
    cantidad: this.state.quantities.cantidad,
    duracionMin: this.state.quantities.duracionMin,
    neto: this.state.pricing.neto,
  };
  
  // Evaluate rules
  const ruleResult = this.#rulesCoordinator.evaluate(snapshot);
  
  // Store results in state
  this.state.appliedRules = ruleResult.appliedRules;
  this.state.available = ruleResult.isAvailable;
  this.state.errors = ruleResult.errors;
  this.state.warnings = ruleResult.warnings;
}
```

### Exposure in API

```javascript
// Item.js toDisplayObject()
toDisplayObject() {
  return {
    // ... other state ...
    appliedRules: this.state.appliedRules.map(r => ({
      ruleId: r.ruleId,
      name: r.name,
      description: r.description,
    })),
    available: this.state.available,
    errors: this.state.errors.map(r => ({ message: r.description })),
    warnings: this.state.warnings.map(r => ({ message: r.description })),
  };
}
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/rules-engine-integration.md`.