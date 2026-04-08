---
identity:
  node_id: "doc:wiki/drafts/2_layer_separation.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/basic.md", relation_type: "documents"}
---

Regardless of module type, separate these concerns into distinct files:

## Details

Regardless of module type, separate these concerns into distinct files:

| File | Owns |
|---|---|
| `contracts.py` | All Pydantic input/output models. The schema boundary. |
| `storage.py` | All file I/O, artifact paths, persistence logic. No business logic. |
| `main.py` | CLI entry point only. No business logic. Delegates to graph/coordinator. |

Additional layers (prompt, graph, coordinator) depend on module type — see the specialized guides.

The rule: **no file does two things.** If a function in `graph.py` is also writing to disk, that write belongs in `storage.py`.

---

Generated from `raw/docs_postulador_refactor/docs/standards/code/basic.md`.