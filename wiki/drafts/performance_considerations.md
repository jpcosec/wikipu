---
identity:
  node_id: "doc:wiki/drafts/performance_considerations.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/rules-engine-integration.md", relation_type: "documents"}
---

- **No I/O:** Rules use JSON-Logic only, no database access

## Details

- **No I/O:** Rules use JSON-Logic only, no database access
- **Fast condition evaluation:** JsonLogic is O(n) where n = operators in condition
- **Caching:** Results cached per snapshot; invalidated on rule changes
- **Early termination:** `acumulable: false` stops loop after first match

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/rules-engine-integration.md`.