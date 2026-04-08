---
identity:
  node_id: "doc:wiki/drafts/3_graph_state.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_components.md", relation_type: "documents"}
---

`GraphState` (TypedDict) carries only routing signals and artifact refs — not full payloads.

## Details

`GraphState` (TypedDict) carries only routing signals and artifact refs — not full payloads.

```python
class MatchSkillState(TypedDict, total=False):
    source: str
    job_id: str
    status: str
    review_decision: ReviewDecision
    round_number: int
    match_result_hash: str
    artifact_refs: dict[str, str]   # refs, not content
```

Heavy payloads (requirements, evidence, match results) are written to disk by the persistence node and reloaded by nodes that need them. State is the routing bus, not the data bus.

---

Generated from `raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_components.md`.