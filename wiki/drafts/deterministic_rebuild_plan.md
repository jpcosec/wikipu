---
identity:
  node_id: "doc:wiki/drafts/deterministic_rebuild_plan.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/refactor_deterministic/README.md", relation_type: "documents"}
---

This folder contains the step-by-step refactor plan approved for the deterministic rebuild.

## Details

This folder contains the step-by-step refactor plan approved for the deterministic rebuild.

Execution rule:
- Implement one step at a time.
- Run deterministic tests after each step.
- Do not preserve legacy runtime behavior except contracts, graph reference, and deterministic tools.

Plan index:
- `00_scope_and_survivors.md`
- `01_documentation_and_contract_preservation.md`
- `02_hard_deletion.md`
- `03_new_langgraph_skeleton.md`
- `04_incremental_reimplementation.md`
- `05_testing_policy.md`
- `06_tracking_and_governance.md`

Generated from `raw/docs_postulador_langgraph/plan/refactor_deterministic/README.md`.