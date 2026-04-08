---
identity:
  node_id: "doc:wiki/drafts/workspace_layout.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/ui/node_editor_behavior_spec.md", relation_type: "documents"}
---

- Fullscreen canvas workspace (neutral background; exact color is not constrained).

## Details

- Fullscreen canvas workspace (neutral background; exact color is not constrained).
- Collapsible sidebar controls:
  - add node
  - show/hide relation types
  - save
  - unfocus/reset focus
  - auto-layout controls (`Layout All`, `Layout Focus Neighborhood`)
  - filter nodes by selected fields
  - expose candidate nodes for new connections

Layout policy:

- Auto-layout must be deterministic (same graph state => same arrangement)
- Prefer stable, non-jittery transitions over continuous physics simulation

`candidate nodes` means nodes currently eligible to receive a new relation from the selected node under active type/filter constraints.

Generated from `raw/docs_postulador_langgraph/docs/ui/node_editor_behavior_spec.md`.