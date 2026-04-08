---
identity:
  node_id: "doc:wiki/drafts/1_the_ingestion_contract.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/ingestion_layer.md", relation_type: "documents"}
---

Every ingestion component has exactly one job: receive external input, validate it, and produce a typed internal representation. It never does anything else.

## Details

Every ingestion component has exactly one job: receive external input, validate it, and produce a typed internal representation. It never does anything else.

```
External input (uncontrolled)
        ↓
  [Ingestion component]
        ↓
  Validated Pydantic model (internal contract)
```

The output model is the boundary. Downstream modules depend on the model, never on the raw external format.

---

Generated from `raw/docs_postulador_refactor/docs/standards/code/ingestion_layer.md`.