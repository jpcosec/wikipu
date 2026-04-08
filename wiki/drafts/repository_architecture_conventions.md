---
identity:
  node_id: "doc:wiki/drafts/repository_architecture_conventions.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/AGENTS.md", relation_type: "documents"}
---

- Each module should have one clear responsibility.

## Details

- Each module should have one clear responsibility.
- Public surface goes through `__init__.py`; avoid deep imports from implementation internals when a public import exists.
- `main.py` is for CLI entrypoints only.
- `storage.py` owns persistence and artifact paths.
- `contracts/` or `contracts.py` owns typed schemas.
- `graph.py` owns orchestration, nodes, edges, and Studio graph exposure.
- Prompt construction belongs in dedicated prompt modules, not in graph wiring.

Generated from `raw/docs_postulador_v2/AGENTS.md`.