---
identity:
  node_id: "doc:wiki/drafts/file_i_o_and_persistence.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/AGENTS.md", relation_type: "documents"}
---

- Prefer centralized file I/O patterns through `DataManager` and related storage helpers.

## Details

- Prefer centralized file I/O patterns through `DataManager` and related storage helpers.
- There is a legacy guardrail test that bans direct `.read_text()`, `.write_text()`, `.read_bytes()`, `.write_bytes()`, and `.mkdir()` calls in much of runtime code under `src/core/ai`, `src/core/tools`, and `src/graph`.
- Some current files already exceed that older rule, so use judgment and follow the local module pattern when editing existing code.
- Do not scatter new ad hoc persistence logic across node implementations.

Generated from `raw/docs_postulador_v2/AGENTS.md`.