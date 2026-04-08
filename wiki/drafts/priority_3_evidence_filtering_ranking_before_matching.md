---
identity:
  node_id: "doc:wiki/drafts/priority_3_evidence_filtering_ranking_before_matching.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/issues/match_skill_hardening_roadmap.md", relation_type: "documents"}
---

### Problem

## Details

### Problem

The current implementation sends all effective evidence into the match prompt.

If the evidence corpus grows, the model call may become:

- too expensive
- too slow
- too large for the context window

### Why It Matters

This is the most important product/runtime scalability gap in the current implementation.

### Recommended Change

Add a deterministic pre-match selection step that reduces evidence to only what is relevant.

Possible strategies:

- keyword overlap scoring
- embeddings-based retrieval
- rule-based requirement-to-evidence ranking
- a separate summarization stage for oversized evidence clusters

### Suggested Graph Extension

Insert a new step before `run_match_llm`, such as:

- `rank_profile_evidence`

Updated flow:

```text
load_match_inputs
  -> rank_profile_evidence
  -> run_match_llm
```

### Suggested Steps

1. define a deterministic evidence ranking contract
2. persist the ranked evidence subset or its ref
3. update prompt inputs to use the selected subset
4. add tests for oversized evidence scenarios

Generated from `raw/docs_postulador_refactor/future_docs/issues/match_skill_hardening_roadmap.md`.