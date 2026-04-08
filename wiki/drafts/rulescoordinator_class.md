---
identity:
  node_id: "doc:wiki/drafts/rulescoordinator_class.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/rules-engine-integration.md", relation_type: "documents"}
---

Main entry point for rule evaluation:

## Details

Main entry point for rule evaluation:

```javascript
export class RulesCoordinator {
  // Constructor: filter rules by component type
  constructor(componentType, rules = []) {
    this.componentType = componentType;
    this.rules = rules.filter(r => r.scope === componentType);
  }

  // Main evaluation method
  evaluate(snapshot) {
    // snapshot = { itemId, kind, pax, cantidad, duracionMin, ... }
    // Returns { appliedRules, isAvailable, errors, warnings }
    
    const applied = [];
    
    // Sort by priority
    const sorted = [...this.rules].sort((a, b) => a.priority - b.priority);
    
    for (const rule of sorted) {
      if (!rule.active) continue;
      
      // Evaluate condition
      const condition = rule.condition ?? true;
      const matches = jsonLogic.apply(condition, snapshot);
      
      if (matches) {
        applied.push(rule);
        
        // If not acumulable, stop here
        if (!rule.acumulable) break;
      }
    }
    
    return {
      appliedRules: applied,
      isAvailable: !applied.some(r => r.actionType === 'ERROR'),
      errors: applied.filter(r => r.actionType === 'ERROR'),
      warnings: applied.filter(r => r.actionType === 'WARNING'),
    };
  }

  // Convenience getters
  getAppliedRules() { return this.lastResult?.appliedRules ?? []; }
  isAvailable() { return this.lastResult?.isAvailable ?? true; }
  getErrors() { return this.lastResult?.errors ?? []; }
  getWarnings() { return this.lastResult?.warnings ?? []; }
}
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/rules-engine-integration.md`.