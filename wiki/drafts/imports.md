---
identity:
  node_id: "doc:wiki/drafts/imports.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/AGENTS.md", relation_type: "documents"}
---

- Use `from __future__ import annotations` at the top of Python modules; this is common across the repo.

## Details

- Use `from __future__ import annotations` at the top of Python modules; this is common across the repo.
- Group imports in this order:
  1. standard library
  2. third-party packages
  3. local `src.*` imports
- Prefer absolute imports from `src...` over fragile relative imports.
- Keep imports explicit; avoid wildcard imports.

Generated from `raw/docs_postulador_v2/AGENTS.md`.