---
identity:
  node_id: "doc:wiki/drafts/3_what_each_implemented_step_does.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/agent_entrypoint.md", relation_type: "documents"}
---

1. `scrape`

## Details

1. `scrape`
   - Reads `source_url`, fetches posting content, and builds ingestion payload for downstream steps.
2. `translate_if_needed`
   - Detects/normalizes language and translates only when required.
3. `extract_understand` (LLM)
   - Produces structured job understanding (requirements and related metadata).
4. `match` (LLM)
   - Maps job requirements to profile evidence.
   - Writes `nodes/match/approved/state.json`.
   - Generates review markdown for human evaluation.
5. `review_match` (deterministic gate)
   - Reads and parses `nodes/match/review/decision.md`.
   - Enforces source hash checks to prevent stale decisions.
   - Emits routing decision:
     - `approve` -> `package` (prep terminal)
     - `request_regeneration` -> back to `match`
     - `reject` -> end
6. `package` (prep terminal in current graph)
   - Marks run as completed for this subgraph.

Generated from `raw/docs_postulador_langgraph/docs/operations/agent_entrypoint.md`.