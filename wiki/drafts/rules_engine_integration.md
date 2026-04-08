---
identity:
  node_id: "doc:wiki/drafts/rules_engine_integration.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/component-architecture.md", relation_type: "documents"}
---

Rules are evaluated **per component instance** in the domain layer:

## Details

Rules are evaluated **per component instance** in the domain layer:

```javascript
// packages/components/<component>/domain/rulesEngine/coordinator.js

export class RulesCoordinator {
  constructor(componentType, rules) {
    this.componentType = componentType;  // ITEM, CATEGORY, KIT, CONTAINER, etc.
    this.rules = rules.filter(r => r.scope === componentType);
  }

  evaluate(snapshot) {
    // snapshot = { componentId, state fields, ... }
    // Returns { appliedRules, isAvailable, errors, warnings }
    
    const applied = [];
    for (const rule of this.rules) {
      if (this.#conditionMatches(rule, snapshot)) {
        applied.push(rule);
      }
    }
    return {
      appliedRules: applied,
      isAvailable: !applied.some(r => r.actionType === 'ERROR'),
      errors: applied.filter(r => r.actionType === 'ERROR'),
      warnings: applied.filter(r => r.actionType === 'WARNING'),
    };
  }
}
```

**Key properties:**
- Rules are **component-scoped** (filtered by component type)
- Conditions evaluated with **JSON-Logic** (`jsonLogic.apply()`)
- Results cached and **invalidated** when rules/definition change
- Errors **block** availability, warnings are **informational**

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/component-architecture.md`.