---
identity:
  node_id: "doc:wiki/drafts/priority_2_add_artifact_schema_versioning.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/issues/match_skill_hardening_roadmap.md", relation_type: "documents"}
---

### Problem

## Details

### Problem

Persisted JSON artifacts currently have no explicit schema version field.

### Why It Matters

- future schema evolution becomes ambiguous
- backward compatibility is harder to reason about
- migrations become brittle

### Recommended Change

Add a version marker to all persisted top-level payloads, for example:

- `schema_version: 1`

Suggested files:

- `approved/state.json`
- `review/current.json`
- `review/decision.json`
- `review/rounds/round_<NNN>/proposal.json`
- `review/rounds/round_<NNN>/decision.json`
- `review/rounds/round_<NNN>/feedback.json`

### Suggested Steps

1. introduce constants for schema versions in `src/core/ai/match_skill/storage.py`
2. write schema version into all persisted payloads
3. update loaders to validate or at least tolerate the version field
4. document version semantics in the product guide

Generated from `raw/docs_postulador_refactor/future_docs/issues/match_skill_hardening_roadmap.md`.