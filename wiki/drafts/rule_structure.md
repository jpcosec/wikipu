---
identity:
  node_id: "doc:wiki/drafts/rule_structure.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/rules-engine-integration.md", relation_type: "documents"}
---

Each rule is a JavaScript object with:

## Details

Each rule is a JavaScript object with:

```javascript
{
  // Identification
  ruleId: 'R001_OVERFLOW',
  name: 'Salon overflow surcharge',

  // Scope: which component type(s) this rule applies to
  scope: 'ITEM',  // ITEM, CATEGORY, KIT, CONTAINER, BASKET

  // Condition: when does this rule fire?
  condition: { 
    "and": [
      { "===": [{ "var": "kind" }, "MENU"] },
      { ">": [{ "var": "pax" }, 150] }
    ]
  },

  // Action: what does the rule do?
  actionType: 'MULTIPLY',           // or ADD_FIXED, WARNING, ERROR, etc.
  payload: { factor: 1.15 },        // Action-specific parameters

  // Flags
  active: true,                     // Logical enable/disable
  priority: 10,                     // Execution order (lower = first)
  acumulable: false,                // Stop processing after this rule?

  // Metadata
  description: 'When pax exceeds 150, apply 15% surcharge',
}
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/rules-engine-integration.md`.