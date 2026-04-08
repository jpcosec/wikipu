---
identity:
  node_id: "doc:wiki/drafts/5_missing_gemini_credentials.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/tool_interaction_and_known_issues.md", relation_type: "documents"}
---

Symptoms:

## Details

Symptoms:

- LLM nodes fail before or during `extract_understand`, `match`, or `generate_documents`.

Cause:

- missing or invalid `GOOGLE_API_KEY` / Gemini credentials.

Fix:

1. configure the API key in local environment or `.env`,
2. rerun the job,
3. confirm the run advances beyond the previous failure node.

Generated from `raw/docs_postulador_langgraph/docs/operations/tool_interaction_and_known_issues.md`.