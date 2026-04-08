---
identity:
  node_id: "doc:wiki/drafts/legacy_e2e_bucket.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/docs/repo_maps/tests_to_src_map.md", relation_type: "documents"}
---

### `tests/legacy/e2e/test_pipeline.py`

## Details

### `tests/legacy/e2e/test_pipeline.py`

- status: `outdated`
- maps to:
  - legacy pipeline / removed `match_skill` flow
- reason:
  - imports removed modules and expects old artifacts like `pipeline_inputs/` and legacy final package manifests

### `tests/legacy/e2e/fixtures/stub_profile.json`

- status: `review`
- maps to:
  - legacy e2e support data
- reason:
  - fixture may still be useful, but its owning test is currently outdated

Generated from `raw/docs_postulador_v2/docs/repo_maps/tests_to_src_map.md`.