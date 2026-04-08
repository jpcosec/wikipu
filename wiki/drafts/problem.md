---
identity:
  node_id: "doc:wiki/drafts/problem.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/issues/api_only_execution.md", relation_type: "documents"}
---

Both `pipeline` and `review` CLI commands implement a two-path execution model: try the LangGraph API first, fall back to local SQLite if unreachable. This fallback is broken and causes state divergence.

## Details

Both `pipeline` and `review` CLI commands implement a two-path execution model: try the LangGraph API first, fall back to local SQLite if unreachable. This fallback is broken and causes state divergence.

### Broken local fallback in `_run_review` (`src/cli/main.py`)

```python
app = build_match_skill_graph(checkpointer=None)  # compiled without checkpointer
app.checkpointer = checkpointer                    # silently ignored — too late
```

LangGraph bakes the checkpointer in at `compile()` time. Setting it afterward has no effect. The fallback runs without persistence — threads are lost on exit.

### Split state problem

The LangGraph API server manages its own thread database. The local fallback uses a separate `data/jobs/checkpoints.db`. These two stores never sync. A thread started via the API cannot be resumed by the local fallback and vice versa. This is what produced the stale `tuberlin_201665` checkpoint: a partial `review_payload` update was written to the local DB, but the full thread state only ever lived in the API.

### Explorer mode bug

`_run_review` always computes `thread_id = f"{args.source}_{args.job_id}"` even in explorer mode where both are `None`, producing `thread_id = "None_None"`.

Generated from `raw/docs_postulador_refactor/future_docs/issues/api_only_execution.md`.