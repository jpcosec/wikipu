---
identity:
  node_id: "doc:wiki/drafts/7_ingestion_component_structure.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/ingestion_layer.md", relation_type: "documents"}
---

```

## Details

```
src/<module>/
  models.py       ← output Pydantic model (the internal contract)
  adapter.py      ← base adapter (abstract, defines the extraction contract)
  providers/      ← source-specific adapters
  main.py         ← CLI: discovery, dispatch, idempotency check
  storage.py      ← artifact paths, meta.json, idempotency state
```

For LLM-assisted ingestion, also:
```
  schema_cache/   ← cached LLM-generated extraction schemas (not committed)
```

Generated from `raw/docs_postulador_refactor/docs/standards/code/ingestion_layer.md`.