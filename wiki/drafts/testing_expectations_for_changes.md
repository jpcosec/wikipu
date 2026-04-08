---
identity:
  node_id: "doc:wiki/drafts/testing_expectations_for_changes.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/AGENTS.md", relation_type: "documents"}
---

- Add or update focused unit tests near the changed module.

## Details

- Add or update focused unit tests near the changed module.
- Prefer narrow test files under `tests/unit/...`.
- When changing `generate_documents_v2`, run at least the affected test file plus `python -m pytest tests/unit/core/ai/generate_documents_v2 -q` if practical.
- When changing CLI behavior, run `python -m pytest tests/unit/cli/test_main.py -q`.

Generated from `raw/docs_postulador_v2/AGENTS.md`.