---
identity:
  node_id: "doc:wiki/drafts/required_environment_variables.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/runtime/langsmith_verification.md", relation_type: "documents"}
---

- `LANGSMITH_API_KEY` (required in verifiable mode)

## Details

- `LANGSMITH_API_KEY` (required in verifiable mode)
- `LANGSMITH_PROJECT` (optional, default: `phd-20`)
- `LANGSMITH_ENDPOINT` (optional; only needed for custom LangSmith endpoints)

You can also enforce verification globally by setting:

- `PHD2_LANGSMITH_REQUIRE_VERIFICATION=1`

Generated from `raw/docs_postulador_langgraph/docs/runtime/langsmith_verification.md`.