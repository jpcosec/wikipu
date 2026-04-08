---
identity:
  node_id: "doc:wiki/drafts/control_plane_resume_contract_langgraph.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/tool_interaction_and_known_issues.md", relation_type: "documents"}
---

Execution identity rule:

## Details

Execution identity rule:

- LangGraph `thread_id` is always `f"{source}_{job_id}"`.

### Resume (`run_prep_match --resume`)

`run_prep_match --resume` wakes the graph from checkpoint state.

Flow:

1. compile graph with persistent checkpointer,
2. set runtime config:

```python
config = {"configurable": {"thread_id": f"{source}_{job_id}"}}
```

3. resume from interrupt with empty invocation:

```python
graph.invoke(None, config)
```

When resumed, LangGraph executes the next pending review node (`review_match` in the current prep flow).
That review node reads and parses `nodes/match/review/decision.md`, writes `decision.json` as a runtime artifact, and emits routing such as `{"review_decision": "approve"}`.

Non-negotiable rule:

- CLI never injects human decisions directly into LangGraph state.
- Resume wakes graph execution; `review_match` remains the deterministic parser/validator.

Generated from `raw/docs_postulador_langgraph/docs/operations/tool_interaction_and_known_issues.md`.