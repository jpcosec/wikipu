---
identity:
  node_id: "doc:wiki/drafts/key_properties.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/rules-engine-integration.md", relation_type: "documents"}
---

### Scope Filtering

## Details

### Scope Filtering

Rules are scoped to component types. A rule only fires if scope matches:

```javascript
const itemRules = [
  { ruleId: 'R1', scope: 'ITEM', ... },      // ✅ Included
  { ruleId: 'R2', scope: 'CATEGORY', ... },  // ❌ Filtered out
  { ruleId: 'R3', scope: 'BASKET', ... },    // ❌ Filtered out
];

const coordinator = new RulesCoordinator('ITEM', itemRules);
// Only R1 will be evaluated
```

### Priority & Acumulable

Control execution order and early termination:

```javascript
// Sorted by priority (lower = earlier)
[
  { priority: 5, acumulable: true },   // Runs first, continues
  { priority: 10, acumulable: false }, // Runs if P5 matched, stops here
  { priority: 20, acumulable: true },  // Skipped if P10 matched
]
```

### Active Flag

Disable rules without deletion:

```javascript
const inactiveRule = {
  ruleId: 'R001',
  active: false,  // ← Skipped during evaluation
  // ... rest of rule ...
};
```

### Caching

Results are cached after first evaluation:

```javascript
coordinator.evaluate(snapshot1);  // Computes all rules
coordinator.evaluate(snapshot2);  // Recomputes (new snapshot)

// Cache invalidated when:
coordinator.defineRules(newRules);  // Update rule set
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/rules-engine-integration.md`.