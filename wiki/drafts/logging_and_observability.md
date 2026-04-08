---
identity:
  node_id: "doc:wiki/drafts/logging_and_observability.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/AGENTS.md", relation_type: "documents"}
---

- Use `logging.getLogger(__name__)`.

## Details

- Use `logging.getLogger(__name__)`.
- Use shared logging bootstrap from `src/shared/logging_config.py` at entrypoints.
- Import `LogTag` from `src/shared/log_tags.py`.
- Never hardcode emoji tags by hand.
- Use `LogTag.LLM` only for LLM-invoking paths.
- Use `LogTag.FAST` for deterministic paths and `LogTag.WARN` / `LogTag.FAIL` for warnings and failures.

Generated from `raw/docs_postulador_v2/AGENTS.md`.