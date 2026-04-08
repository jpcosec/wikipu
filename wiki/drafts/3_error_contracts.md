---
identity:
  node_id: "doc:wiki/drafts/3_error_contracts.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/basic.md", relation_type: "documents"}
---

Define domain-specific exceptions at the top of the file. Never use bare `Exception` for flow control.

## Details

Define domain-specific exceptions at the top of the file. Never use bare `Exception` for flow control.

```python
class ToolDependencyError(Exception): pass
class ToolFailureError(Exception): pass
```

Never swallow errors silently. If catching a broad exception to trigger a fallback, log with `LogTag.WARN` first, then re-raise with `from e` to preserve the stack trace.

Expose operational limits (chunk sizes, retry budgets, rate limits) as `@property` on ABCs — not buried in loops or config dicts.

---

Generated from `raw/docs_postulador_refactor/docs/standards/code/basic.md`.