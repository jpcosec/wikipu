---
identity:
  node_id: "doc:wiki/drafts/6_persistence_model.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_components.md", relation_type: "documents"}
---

Artifacts live under `output/<module>/<source>/<job_id>/nodes/<module>/`.

## Details

Artifacts live under `output/<module>/<source>/<job_id>/nodes/<module>/`.

Structure:
```
approved/state.json         ← latest approved proposal
review/current.json         ← current review surface
review/rounds/round_NNN/    ← immutable per-round snapshots
  proposal.json
  decision.json
  feedback.json
```

Rules:
- Round directories are immutable once written
- `approved/state.json` is overwritten only on approval
- All persisted payloads should carry a `schema_version` field (see `future_docs/issues/match_skill_hardening_roadmap.md`)
- Hash the approved artifact and store the hash in state for review validation

---

Generated from `raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_components.md`.