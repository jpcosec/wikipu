---
identity:
  node_id: "doc:wiki/drafts/match_regeneration_memory_flow_implemented.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/runtime/data_management.md", relation_type: "documents"}
---

1. Reviewer marks `Regen` in `nodes/match/review/decision.md`.

## Details

1. Reviewer marks `Regen` in `nodes/match/review/decision.md`.
2. `review_match` parses and writes `decision.json` + `feedback.json` in the round folder.
3. `match` on `request_regeneration` loads latest feedback via `RoundManager`.
4. Optional `patch_evidence` items are appended into the effective evidence set.
5. New round artifacts are created under `round_<NNN>/`.

Generated from `raw/docs_postulador_langgraph/docs/runtime/data_management.md`.