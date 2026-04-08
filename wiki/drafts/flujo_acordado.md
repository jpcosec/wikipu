---
identity:
  node_id: "doc:wiki/drafts/flujo_acordado.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/app-flow-state-screen-foundation.md", relation_type: "documents"}
---

```text

## Details

```text
Entry page -> database_browser / New_quotation / load_previous_quotation
database_browser -> table_selector
New_quotation -> select_client / new_client -> quotation
quotation -> save / validate
validate -> print -> save
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/app-flow-state-screen-foundation.md`.