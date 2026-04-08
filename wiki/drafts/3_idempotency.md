---
identity:
  node_id: "doc:wiki/drafts/3_idempotency.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/ingestion_layer.md", relation_type: "documents"}
---

Ingestion runs must be safe to re-run.

## Details

Ingestion runs must be safe to re-run.

- If the output artifact already exists and is valid, skip and log `LogTag.SKIP`.
- Provide an explicit `--overwrite` / `--force` flag to re-ingest.
- Never silently overwrite existing validated artifacts.

```python
if output_path.exists() and not args.force:
    logger.info(f"{LogTag.SKIP} Already ingested: {output_path}")
    return
```

---

Generated from `raw/docs_postulador_refactor/docs/standards/code/ingestion_layer.md`.