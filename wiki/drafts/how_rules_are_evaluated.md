---
identity:
  node_id: "doc:wiki/drafts/how_rules_are_evaluated.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/rules-engine-integration.md", relation_type: "documents"}
---

### 1. **Filter by Scope**

## Details

### 1. **Filter by Scope**

Only rules matching the component type are considered:

```javascript
const ruleCoordinator = new RulesCoordinator('ITEM', allRules);
// Keeps only rules where scope === 'ITEM'
// Ignores CATEGORY, KIT, CONTAINER, BASKET rules
```

### 2. **Evaluate Condition**

For each active rule, evaluate the **JsonLogic condition** against the component snapshot:

```javascript
const snapshot = {
  itemId: 'SALON_01',
  kind: 'MENU',
  category: 'salón',
  pax: 175,           // User set
  cantidad: 1,
  duracionMin: 120,
  neto: 5000,
};

// Does this condition pass?
const conditionPasses = jsonLogic.apply(rule.condition, snapshot);
// → true if pax > 150
```

**Supported JsonLogic operators:**
- Comparison: `===`, `!==`, `>`, `>=`, `<`, `<=`
- Logical: `and`, `or`, `!`
- Helpers: `in`, `var`

### 3. **Apply Action**

If condition passes, execute the action:

```javascript
switch (rule.actionType) {
  case 'MULTIPLY':      // Percentage increase/decrease
    return { delta: neto * (factor - 1), description: `×${factor} (${(factor-1)*100}%)` };
  
  case 'ADD_FIXED':     // Fixed amount
    return { delta: amount, description: `$${amount} flat` };
  
  case 'WARNING':       // Informational
    return { delta: 0, description: message };
  
  case 'ERROR':         // Blocking
    return { delta: 0, isBlocking: true, description: message };
  
  case 'SET_DEFAULT':   // Set a quantity field
    return { delta: 0, field: fieldName, value: defaultValue };
}
```

### 4. **Combine Results**

All matched rules contribute to final state:

```javascript
const result = coordinator.evaluate(snapshot);

// result = {
//   appliedRules: [ruleA, ruleB, ruleC],
//   isAvailable: true,              // No blocking errors?
//   errors: [ruleB],                // ERROR-type rules
//   warnings: [ruleC],              // WARNING-type rules
//   priceAdjustment: 750,           // Sum of all deltas
// }
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/rules-engine-integration.md`.