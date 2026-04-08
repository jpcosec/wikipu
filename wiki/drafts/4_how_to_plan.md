---
identity:
  node_id: "doc:wiki/drafts/4_how_to_plan.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/docs/documentation_and_planning_guide.md", relation_type: "documents"}
---

Active execution plans live in `plan_docs/`. They are **ephemeral** — deleted when the work is done.

## Details

Active execution plans live in `plan_docs/`. They are **ephemeral** — deleted when the work is done.

```
plan_docs/
  match_skill_tui_refactor.md
  render_docx_engine.md
```

A plan file contains: goal, constraints, ordered steps, and open questions. It is a working document — edit it freely as understanding improves. It is not documentation; do not write it as if future readers will study it.

**Lifecycle:**

```
spec / requirement
      ↓
  plan_docs/<plan>.md   ←  written before touching code
      ↓  (execution complete, all tests pass)
  deleted               ←  changelog.md updated with what changed and why
```

If an execution plan reveals a deferred item (something real but out of scope), move it to `future_docs/` before closing the plan.

---

Generated from `raw/docs_postulador_refactor/docs/standards/docs/documentation_and_planning_guide.md`.