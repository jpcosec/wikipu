---
identity:
  node_id: "doc:wiki/drafts/rule_examples.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/rules-engine-integration.md", relation_type: "documents"}
---

### Example 1: Overflow Surcharge (Percentage Multiplier)

## Details

### Example 1: Overflow Surcharge (Percentage Multiplier)

**Scenario:** Salons with >150 pax incur 15% surcharge

```javascript
{
  ruleId: 'R001_SALON_OVERFLOW',
  name: 'Salon overflow surcharge',
  scope: 'ITEM',
  
  condition: {
    "and": [
      { "===": [{ "var": "kind" }, "MENU"] },
      { ">": [{ "var": "pax" }, 150] }
    ]
  },
  
  actionType: 'MULTIPLY',
  payload: { factor: 1.15 },
  
  priority: 10,
  acumulable: false,  // Stop after this rule
  active: true,
}
```

**Trigger:** When `kind === 'MENU'` AND `pax > 150`
**Effect:** Price multiplied by 1.15 (+15%)

### Example 2: Minimum Pax Validation (Blocking)

**Scenario:** Coffee service requires minimum 10 pax

```javascript
{
  ruleId: 'R002_COFFEE_MIN_PAX',
  name: 'Coffee minimum pax',
  scope: 'ITEM',
  
  condition: {
    "and": [
      { "===": [{ "var": "kind" }, "EXTRA"] },
      { "<": [{ "var": "pax" }, 10] }
    ]
  },
  
  actionType: 'ERROR',
  payload: { message: 'Coffee requires minimum 10 pax' },
  
  priority: 5,
  acumulable: true,   // Continue checking other rules
  active: true,
}
```

**Trigger:** When `kind === 'EXTRA'` AND `pax < 10`
**Effect:** Item becomes unavailable (`.available = false`)

### Example 3: Warning (Non-Blocking)

**Scenario:** Alert if pax exceeds typical capacity

```javascript
{
  ruleId: 'R003_HIGH_PAX_WARNING',
  name: 'High pax warning',
  scope: 'ITEM',
  
  condition: {
    ">": [{ "var": "pax" }, 500]
  },
  
  actionType: 'WARNING',
  payload: { message: 'Pax count exceeds typical venue capacity. Contact manager.' },
  
  priority: 100,
  acumulable: true,
  active: true,
}
```

**Trigger:** When `pax > 500`
**Effect:** Added to `.warnings` array, but item remains available

### Example 4: Fixed Discount

**Scenario:** Military discount: flat $500 off

```javascript
{
  ruleId: 'R004_MILITARY_DISCOUNT',
  name: 'Military discount',
  scope: 'ITEM',
  
  condition: {
    "===": [{ "var": "discountCode" }, "MILITARY"]
  },
  
  actionType: 'ADD_FIXED',
  payload: { amount: -500 },
  
  priority: 50,
  acumulable: true,
  active: true,
}
```

**Trigger:** When `discountCode === 'MILITARY'`
**Effect:** Price reduced by $500 (negative amount = discount)

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/rules-engine-integration.md`.