---
identity:
  node_id: "doc:wiki/drafts/1_module_structure.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/basic.md", relation_type: "documents"}
---

Every module is a self-contained package under `src/<module>/` with a single clear responsibility. Cross-module dependencies go through public contracts (`contracts.py`), never by importing internal implementation files.

## Details

Every module is a self-contained package under `src/<module>/` with a single clear responsibility. Cross-module dependencies go through public contracts (`contracts.py`), never by importing internal implementation files.

Each module exposes its public surface through `__init__.py`. Consumers should not need to import from deep internal paths.

---

Generated from `raw/docs_postulador_refactor/docs/standards/code/basic.md`.