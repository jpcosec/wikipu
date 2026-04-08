---
identity:
  node_id: "doc:wiki/drafts/3_hidden_fallback_behavior_or_low_quality_generation.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/tool_interaction_and_known_issues.md", relation_type: "documents"}
---

Symptoms:

## Details

Symptoms:

- outputs are repetitive, generic, or still contain placeholders.

Cause:

- prompt/runtime quality issues or insufficient grounding, even when the graph run itself succeeds.

Fix:

1. inspect `nodes/generate_documents/approved/state.json` and generated markdown,
2. verify the approved matches are sensible,
3. tighten prompt or deterministic post-check logic rather than masking the issue.

Generated from `raw/docs_postulador_langgraph/docs/operations/tool_interaction_and_known_issues.md`.