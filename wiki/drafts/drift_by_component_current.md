---
identity:
  node_id: "doc:wiki/drafts/drift_by_component_current.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixins-style-drift-assessment.md", relation_type: "documents"}
---

| Component | Mixin Deficit | Actor Deficit | Runtime Deficit | API Deficit | Drift Total |

## Details

| Component | Mixin Deficit | Actor Deficit | Runtime Deficit | API Deficit | Drift Total |
|---|---:|---:|---:|---:|---:|
| `item` | 25 | 20 | 0 | 10 | **55** |
| `category` | 25 | 25 | 0 | 20 | **70** |
| `catalog` | 25 | 25 | 0 | 20 | **70** |
| `basket-day` | 25 | 25 | 0 | 20 | **70** |
| `basket` | 25 | 25 | 0 | 20 | **70** |
| `quotation` (package overall) | 5 | 15 | 25 | 15 | **60** |

Interpretation:

- `0-20`: aligned
- `21-40`: minor drift
- `41-60`: moderate drift
- `61-80`: high drift
- `81-100`: severe drift

Current system has moderate-to-high drift in all core runtime components.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixins-style-drift-assessment.md`.