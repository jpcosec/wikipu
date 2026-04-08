---
identity:
  node_id: "doc:wiki/drafts/5_notes.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/02_migration/api_migration_and_gap_analysis.md", relation_type: "documents"}
---

- The `doc-methodology-2.0` worktree (`runtime/ui/api_contract.md`) is the **canonical spec** for the v2 API. All new backend endpoints should match it exactly.

## Details

- The `doc-methodology-2.0` worktree (`runtime/ui/api_contract.md`) is the **canonical spec** for the v2 API. All new backend endpoints should match it exactly.
- The mock client in `ui-redesign` is the source of truth for fixture data shapes. When wiring real endpoints, validate against mock response shape first.
- `GraphNode.category` is already populated in the dev branch fixtures and the `build_view_one_payload()` builder — no shape change needed there.
- The `view_extract` response from dev does **not** include `char_start`/`char_end`. The real backend will need to compute and return these (or the UI can compute them client-side from the source markdown — simpler for now).

Generated from `raw/docs_postulador_ui/plan/02_migration/api_migration_and_gap_analysis.md`.