---
identity:
  node_id: "doc:wiki/drafts/storage_roots_and_ownership.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/runtime/data_management.md", relation_type: "documents"}
---

### Job workspace root

## Details

### Job workspace root

- Root: `data/jobs/<source>/<job_id>/`

### Profile base snapshot

- Default profile snapshot used by `generate_documents` fallback:
  - `data/reference_data/profile/base_profile/profile_base_data.json`

### Checkpoints

- Default runtime checkpoint path:
  - `data/jobs/<source>/<job_id>/graph/checkpoint.sqlite`

Generated from `raw/docs_postulador_langgraph/docs/runtime/data_management.md`.