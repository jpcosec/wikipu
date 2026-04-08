---
identity:
  node_id: "doc:wiki/drafts/2_validation_at_the_boundary.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/ingestion_layer.md", relation_type: "documents"}
---

All validation happens at ingestion time, not downstream.

## Details

All validation happens at ingestion time, not downstream.

- MANDATORY fields: missing or invalid → raise a domain-specific exception. Never allow a partial record to propagate.
- OPTIONAL fields: absent is valid. Document which fields are optional and what downstream behavior to expect when they're absent.
- Schema evolution: when the external format changes (new portal layout, new review payload shape), update the ingestion adapter — not the downstream contract.

```python
class IngestionValidationError(Exception): pass
class PartialExtractionError(Exception): pass  # LLM rescue produced incomplete output
```

---

Generated from `raw/docs_postulador_refactor/docs/standards/code/ingestion_layer.md`.