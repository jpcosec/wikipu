---
identity:
  node_id: "doc:wiki/drafts/data_dependency_flow.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md", relation_type: "documents"}
---

### User Input → State Update → Calculation → Output

## Details

### User Input → State Update → Calculation → Output

```
USER INPUT (via AlpineXStateBridge)
    │
    ▼
XState Machine
    │
    ├─→ actions/ ──→ Load/Update data from Store
    │   ├── services.js (async DB calls)
    │   ├── guards.js (validation)
    │   └── actions.js (state mutations)
    │
    ├─→ context.store ──→ Database Package
    │   │   ├── InMemoryStore (testing)
    │   │   ├── FileStore (local dev)
    │   │   └── GasSheetStore (production)
    │   │
    │   └── 11 Auto-Generated Models
    │       (from Config_Schema.js)
    │
    └─→ Pricing/Domain Calculations
        │   Pass context data as parameters
        │   Returns computed values
        │
        ├── Pricing.pipeline() [Legacy]
        ├── Domain.Item/Basket/Category [Phase B]
        └── RulesCoordinator.evaluate()
            (JSON-Logic expressions)

RESULT SYNCED BACK
    │
    ▼
Frontend Package (AlpineXStateBridge)
    │
    └─→ Alpine.js reactive UI
        Display totals, lineas, errors
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md`.