---
identity:
  node_id: "doc:wiki/drafts/1_review_artifact_contract_mismatch_primary.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/reviewed_jobs_pipeline_diagnosis.md", relation_type: "documents"}
---

Current review gate logic in `src/nodes/review_match/logic.py` requires `source_state_hash` locking for edited decisions.

## Details

Current review gate logic in `src/nodes/review_match/logic.py` requires `source_state_hash` locking for edited decisions.

Existing reviewed files were generated in an earlier format (no front matter hash), then manually edited. This triggers intentional fail-closed behavior:

- missing hash + checked decisions => hard error

This prevents applying human decisions to potentially stale match payloads.

Generated from `raw/docs_postulador_langgraph/docs/operations/reviewed_jobs_pipeline_diagnosis.md`.