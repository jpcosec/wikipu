---
identity:
  node_id: "doc:wiki/drafts/1_what_this_codebase_is_for.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/agent_entrypoint.md", relation_type: "documents"}
---

This repo implements a human-in-the-loop pipeline for PhD/job application support.

## Details

This repo implements a human-in-the-loop pipeline for PhD/job application support.

Current implemented runtime scope:

1. Scrape one job posting.
2. Translate if needed.
3. Extract structured job requirements.
4. Match requirements against profile evidence.
5. Stop at review gate and require a human decision.
6. Resume with deterministic routing (`approve`, `request_regeneration`, `reject`).

The current executable subgraph is the prep+match flow, not the full end-to-end architecture target.

Generated from `raw/docs_postulador_langgraph/docs/operations/agent_entrypoint.md`.