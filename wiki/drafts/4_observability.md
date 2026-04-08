---
identity:
  node_id: "doc:wiki/drafts/4_observability.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/basic.md", relation_type: "documents"}
---

Import `LogTag` from `src/shared/log_tags.py`. Never write emoji tag strings by hand.

## Details

Import `LogTag` from `src/shared/log_tags.py`. Never write emoji tag strings by hand.

```python
from src.shared.log_tags import LogTag

logger.info(f"{LogTag.LLM} Generating match proposal for {job_id}")
logger.warning(f"{LogTag.WARN} Rate limit hit, retrying in {delay}s")
logger.error(f"{LogTag.FAIL} Validation failed: {err}")
```

`LogTag.LLM` is only used on paths that invoke an LLM. `LogTag.FAST` on deterministic paths. Misusing the tags degrades the execution trace.

---

Generated from `raw/docs_postulador_refactor/docs/standards/code/basic.md`.