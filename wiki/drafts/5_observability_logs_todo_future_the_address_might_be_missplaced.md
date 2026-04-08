---
identity:
  node_id: "doc:wiki/drafts/5_observability_logs_todo_future_the_address_might_be_missplaced.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/docs/documentation_quality_checklist.md", relation_type: "documents"}
---

- [ ] All log messages use `LogTag` from `src/shared/log_tags.py` — no hand-written emoji strings.

## Details

- [ ] All log messages use `LogTag` from `src/shared/log_tags.py` — no hand-written emoji strings.
- [ ] `LogTag.LLM` is used only on paths that invoke an LLM — not on deterministic logic.
- [ ] `LogTag.FAST` is used on deterministic paths to make the distinction explicit.
- [ ] No log messages use plain text where a `LogTag` applies.

---

Generated from `raw/docs_postulador_refactor/docs/standards/docs/documentation_quality_checklist.md`.