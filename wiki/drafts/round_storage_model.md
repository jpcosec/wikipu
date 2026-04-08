---
identity:
  node_id: "doc:wiki/drafts/round_storage_model.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/runtime/match_review_cycle.md", relation_type: "documents"}
---

`RoundManager` stores immutable review artifacts under:

## Details

`RoundManager` stores immutable review artifacts under:

- `nodes/match/review/rounds/round_<NNN>/`

Active review surface is mirrored at:

- `nodes/match/review/decision.md`

So each generation creates a new immutable round file and updates the active review file.

Generated from `raw/docs_postulador_langgraph/docs/runtime/match_review_cycle.md`.