---
identity:
  node_id: "doc:wiki/drafts/5_how_to_mark_future_work.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/docs/documentation_and_planning_guide.md", relation_type: "documents"}
---

See [`future_docs_guide.md`](future_docs_guide.md) for the full convention.

## Details

See [`future_docs_guide.md`](future_docs_guide.md) for the full convention.

**Short version:**

1. Create `future_docs/<topic>.md` describing the problem, why it's deferred, and a proposed direction.
2. Leave an inline marker at the relevant code location:

```python
# TODO(future): <short description> — see future_docs/<topic>.md
```

3. When the item is prioritized, promote to `plan_docs/`, delete the `future_docs/` entry, and remove the inline marker when done.

---

Generated from `raw/docs_postulador_refactor/docs/standards/docs/documentation_and_planning_guide.md`.