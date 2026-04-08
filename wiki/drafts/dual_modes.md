---
identity:
  node_id: "doc:wiki/drafts/dual_modes.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/item-component.md", relation_type: "documents"}
---

### CATALOG Mode

## Details

### CATALOG Mode

**Purpose:** Browse available items, see pricing formula

**Visual:**
```
┌─────────────────────────────────────┐
│ ☕ Coffee Service          [extras]  │
├─────────────────────────────────────┤
│ Formula: $2 per pax                 │
│ Policy: Minimum 10 pax, max 200     │
│                                     │
│ [Add to Order] [View Details]       │
└─────────────────────────────────────┘
```

**User actions:**
- View pricing formula
- See restrictions/policies
- Add to basket → switches to BASKET mode

### BASKET Mode

**Purpose:** Adjust quantities, review pricing, see applied rules

**Visual:**
```
┌─────────────────────────────────────┐
│ ☕ Coffee Service         [BASKET]   │
├─────────────────────────────────────┤
│ Guests (pax):     [50    ] override  │
│ Units (cantidad): [50    ] manual   │
│ Duration (min):   [45    ] auto     │
│                                     │
│ Subtotal:         $250.00           │
│ Rules applied:    [2]               │
│ Total:            $275.00           │
│                                     │
│ [Save] [Remove]                     │
└─────────────────────────────────────┘
```

**User actions:**
- Adjust pax, cantidad, duration
- See recalculated prices in real-time
- View applied rules and blockers
- Save or remove item

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/item-component.md`.