---
identity:
  node_id: "doc:wiki/drafts/patch_evidence_injection_format.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/runtime/match_review_cycle.md", relation_type: "documents"}
---

Reviewer can attach extra evidence in comments using:

## Details

Reviewer can attach extra evidence in comments using:

`PATCH_EVIDENCE: {"id":"<PATCH_ID>","description":"<TEXT>"}`

Valid patch evidence is extracted into `feedback.json` and later merged by `match` into effective profile evidence for next rounds.

Generated from `raw/docs_postulador_langgraph/docs/runtime/match_review_cycle.md`.