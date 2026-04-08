---
identity:
  node_id: "doc:wiki/drafts/checkpoint_resume_behavior.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/runtime/graph_flow.md", relation_type: "documents"}
---

- `thread_id` is `f"{source}_{job_id}"`.

## Details

- `thread_id` is `f"{source}_{job_id}"`.
- Checkpoint path: `data/jobs/<source>/<job_id>/graph/checkpoint.sqlite`.
- Resume with `--resume` restores checkpointed review context.

Generated from `raw/docs_postulador_langgraph/docs/runtime/graph_flow.md`.