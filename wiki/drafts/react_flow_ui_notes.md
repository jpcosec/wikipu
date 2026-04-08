---
identity:
  node_id: "doc:wiki/drafts/react_flow_ui_notes.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/future/README.md", relation_type: "documents"}
---

Reference checked: `https://reactflow.dev/ui`

## Details

Reference checked: `https://reactflow.dev/ui`

- React Flow UI provides copyable components, not a black-box package.
- It is designed around `shadcn/ui` + Tailwind.
- Good candidates for reuse here:
  - base node patterns
  - labeled group node patterns
  - database schema node patterns
  - button/data edges
  - node search / zoom controls
- Recommendation: borrow patterns selectively, do not adopt wholesale before defining our node-type registry.

Generated from `raw/docs_postulador_ui/plan/future/README.md`.