---
identity:
  node_id: "doc:wiki/drafts/verification_pattern.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/agent_planning_and_verification_pattern.md", relation_type: "documents"}
---

Each significant task should include:

## Details

Each significant task should include:

- the scenario being verified
- the tool/command used
- exact steps
- expected result
- durable evidence location when the evidence belongs in the repo

Preferred verification order:

1. targeted unit or slice tests
2. build/type-check
3. browser or operator flow validation for UI/runtime behavior
4. final end-to-end sanity check

Generated from `raw/docs_postulador_langgraph/docs/operations/agent_planning_and_verification_pattern.md`.