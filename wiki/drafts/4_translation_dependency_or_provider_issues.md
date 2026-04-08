---
identity:
  node_id: "doc:wiki/drafts/4_translation_dependency_or_provider_issues.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/tool_interaction_and_known_issues.md", relation_type: "documents"}
---

Symptoms:

## Details

Symptoms:

- translation node fails or long input translation breaks.

Cause:

- missing dependency, provider failure, or long input edge cases.

Fix:

1. verify environment dependencies,
2. rerun the deterministic translation tests,
3. inspect `raw/language_check.json` and `nodes/translate_if_needed/approved/state.json` when present.

Generated from `raw/docs_postulador_langgraph/docs/operations/tool_interaction_and_known_issues.md`.