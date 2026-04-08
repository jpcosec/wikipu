---
identity:
  node_id: "doc:wiki/drafts/minimum_artifact_checks_per_run.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/tool_interaction_and_known_issues.md", relation_type: "documents"}
---

At each pause or completion, verify:

## Details

At each pause or completion, verify:

1. the node just executed wrote its expected state/artifact files,
2. `match` review flow includes `nodes/match/review/decision.md`,
3. `render` wrote `nodes/render/approved/state.json`,
4. `package` wrote `final/*.md` and `final/manifest.json`,
5. `graph/run_summary.json` reflects the latest run status.

Generated from `raw/docs_postulador_langgraph/docs/operations/tool_interaction_and_known_issues.md`.