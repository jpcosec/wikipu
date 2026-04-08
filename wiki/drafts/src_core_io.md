---
identity:
  node_id: "doc:wiki/drafts/src_core_io.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/docs/repo_maps/tests_to_src_map.md", relation_type: "documents"}
---

### `tests/unit/core/io/test_workspace_manager.py`

## Details

### `tests/unit/core/io/test_workspace_manager.py`

- status: `current`
- maps to:
  - `src/core/io/workspace_manager.py`

### `tests/legacy/guardrails/test_file_management_guardrails.py`

- status: `outdated`
- maps to:
  - `src/core/data_manager.py`
  - `src/core/io/`
  - `src/core/ai/generate_documents_v2/`
- reason:
  - encodes an older “DataManager-only filesystem access” rule and still assumes legacy graph boundaries

Generated from `raw/docs_postulador_v2/docs/repo_maps/tests_to_src_map.md`.