---
identity:
  node_id: "doc:wiki/drafts/what_we_are_not_building_future_scope.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/D2_group_node_collapse.md", relation_type: "documents"}
---

| Feature | Why deferred |

## Details

| Feature | Why deferred |
|---|---|
| `collapse_behavior: summary \| hide` from schema | Hardcode `summary` for now |
| elkjs compound layout | Dagre + `NodeResizer` is sufficient |
| Zustand store / unified state contract | `useReactFlow` + local state is sufficient |
| Collapse as undoable action | Borderline per future doc; deferred |
| 3-level nesting depth cap | Not needed yet |
| Absorption via drag (parent-child reparenting) | Coordinate transform complexity — separate iteration |
| "Group selected nodes" action | Enabled by `useOnSelectionChange` — separate task |
| `useInternalNode` for proxy edge routing from group boundary | Only needed if floating edges need to originate at group perimeter |

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/D2_group_node_collapse.md`.