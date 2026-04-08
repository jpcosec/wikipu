---
identity:
  node_id: "doc:wiki/drafts/4_llm_rescue_pattern.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/ingestion_layer.md", relation_type: "documents"}
---

When extraction is primarily deterministic (CSS selectors, regex, structured parsing) but may fail on malformed input, an LLM rescue fallback is acceptable. Rules:

## Details

When extraction is primarily deterministic (CSS selectors, regex, structured parsing) but may fail on malformed input, an LLM rescue fallback is acceptable. Rules:

- The deterministic path is always attempted first.
- LLM rescue is only triggered on explicit failure, never speculatively.
- Log the rescue trigger explicitly with `LogTag.FALLBACK`.
- The rescue output must pass the same validation contract as the deterministic path.
- Cache the LLM-generated extraction schema after the first successful run — do not re-generate on every run.

```python
try:
    result = deterministic_extract(page)
    logger.info(f"{LogTag.FAST} CSS extraction succeeded")
except ExtractionError:
    logger.warning(f"{LogTag.FALLBACK} CSS extraction failed, invoking LLM rescue")
    result = llm_rescue_extract(page)

validated = OutputContract.model_validate(result)
```

---

Generated from `raw/docs_postulador_refactor/docs/standards/code/ingestion_layer.md`.