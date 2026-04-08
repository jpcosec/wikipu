---
identity:
  node_id: "doc:wiki/drafts/naming_conventions.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/AGENTS.md", relation_type: "documents"}
---

- Modules and functions: `snake_case`

## Details

- Modules and functions: `snake_case`
- Classes and Pydantic models: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Internal helpers: prefix with `_`
- Parser builders should use `_build_parser()` in CLI modules.
- LangGraph node names should reflect role clearly, such as `load_*`, `build_*`, `persist_*`, `apply_*`, `prepare_*`.

Generated from `raw/docs_postulador_v2/AGENTS.md`.