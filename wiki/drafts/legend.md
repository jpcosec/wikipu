---
identity:
  node_id: "doc:wiki/drafts/legend.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/runtime/node_io_matrix.md", relation_type: "documents"}
---

- Execution class:

## Details

- Execution class:
  - `LLM` = step uses an LLM.
  - `NLLM-D` = non-LLM deterministic step.
  - `NLLM-ND` = non-LLM bounded-nondeterministic step.
- Review gate: whether the node requires explicit HITL review before flow continues.
- Paths are relative to `data/jobs/<source>/<job_id>/`.

Generated from `raw/docs_postulador_langgraph/docs/runtime/node_io_matrix.md`.