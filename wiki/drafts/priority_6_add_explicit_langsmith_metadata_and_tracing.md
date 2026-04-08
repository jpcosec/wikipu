---
identity:
  node_id: "doc:wiki/drafts/priority_6_add_explicit_langsmith_metadata_and_tracing.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/issues/match_skill_hardening_roadmap.md", relation_type: "documents"}
---

### Problem

## Details

### Problem

Studio is connected, but observability is still fairly local and operationally thin.

### Why It Matters

We want to know:

- cost per run
- round count per job
- frequency of regeneration
- whether patch evidence improves outcomes

### Recommended Change

Add explicit tags/metadata to the model runnable and graph invocations.

Useful metadata:

- `source`
- `job_id`
- `round_number`
- `review_decision`
- `regeneration_scope_size`
- `used_demo_chain`

### Suggested Steps

1. tag the LangChain runnable
2. add per-run metadata on invoke/resume
3. document recommended LangSmith dashboards/queries

Generated from `raw/docs_postulador_refactor/future_docs/issues/match_skill_hardening_roadmap.md`.