---
identity:
  node_id: "doc:wiki/drafts/internal_architecture.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/item-component.md", relation_type: "documents"}
---

### Class Hierarchy

## Details

### Class Hierarchy

```
Item
├── Properties
│   ├── definition (ItemDefinition)
│   ├── mode (CATALOG | BASKET)
│   ├── context (ItemContext)
│   └── state (ItemState)
├── Lifecycle
│   ├── initialize()
│   ├── setMode(newMode)
│   └── resetToDefaults()
├── Calculations
│   ├── calculate() ← main entry point
│   ├── #computeQuantity()
│   ├── #computePricing()
│   └── #evaluateRules()
└── Overrides
    ├── setOverride(field, value)
    ├── clearOverride(field)
    ├── clearAllOverrides()
    └── isUserSet(field)
```

### Context Flow

```
ItemDefinition (static)
├── name, kind, category
├── pricingProfile { basePax, baseNeto, durMin, durMax }
├── categoryDefaults { pax, cantidad, durMin }
└── rules []
     │
     ▼
ItemContext (mutable)
├── userOverrides { pax, cantidad, duracionMin }
├── userSetFields Set(['pax'])
├── appliedRules [ { ruleId, action, payload } ]
├── errors [ { message, ruleId } ]
└── warnings [ { message, ruleId } ]
     │
     ▼
ItemState (calculated)
├── quantities { pax, cantidad, duracionMin }
├── pricing { neto, subtotal, total }
├── available (true if no errors)
└── displayString (formatted for UI)
```

### Calculation Pipeline

```
┌─────────────────────────────────────────┐
│ 1. RESOLVE QUANTITIES                   │
│    Use: definition.categoryDefaults     │
│         context.userOverrides           │
│    Result: { pax, cantidad, duracionMin} │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ 2. COMPUTE PRICING                      │
│    Use: pricingProfile, quantities      │
│    Result: { neto, subtotal }           │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ 3. EVALUATE RULES                       │
│    Use: definition.rules, snapshot      │
│    Result: {appliedRules, errors,       │
│             warnings, available}        │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ 4. FINAL STATE                          │
│    Combine all above                    │
│    Generate displayString               │
│    Return toDisplayObject()             │
└─────────────────────────────────────────┘
```

### Domain Modules

**`domain/pricing.js`**
```javascript
export function detectKind(name, kind)                    // POS → MENU, SERVICE, EXTRA, SETUP
export function convertCantidad(pax, factor)             // Pax → units
export function calculateNeto(profile, quantities)       // Base → adjusted by duration/qty
export function applyMultiplier(neto, factor)            // Apply rule factor
export function calculateSubtotal(neto, adjustments)     // With rule adjustments
```

**`domain/quantity.js`**
```javascript
export function resolveQuantity(definition, overrides)   // Override precedence
export function getPaxDefault(definition)                // Category → default pax
export function getDurationDefault(definition)           // Category → default duration
export function isQuantityValid(qty, min, max)          // Bounds checking
```

**`domain/formatting.js`**
```javascript
export function formatItem(item, kind, mode)            // Full display string
export function formatPrice(neto, subtotal, total)      // Price formatting
export function formatQuantity(pax, cantidad, dur)      // Qty formatting
export function formatRuleDescription(rule)             // Human-readable rule
```

**`domain/rulesEngine/coordinator.js`**
```javascript
export class RulesCoordinator {
  constructor(componentType, rules)     // Filter rules by type
  evaluate(snapshot)                    // Evaluate all conditions
  isAvailable()                         // No blocking errors?
  getAppliedRules()                     // Which rules fired
  getErrors()                           // Blocking errors
  getWarnings()                         // Non-blocking warnings
}
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/item-component.md`.