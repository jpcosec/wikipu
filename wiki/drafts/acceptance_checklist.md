---
identity:
  node_id: "doc:wiki/drafts/acceptance_checklist.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/ui/node_editor_behavior_spec.md", relation_type: "documents"}
---

Each assertion must be independently verifiable in the sandbox using mock graph data (not real CV data).

## Details

Each assertion must be independently verifiable in the sandbox using mock graph data (not real CV data).

### Visibility

- [ ] AC-01: Every node shows `name` at all times, regardless of zoom or state.
- [ ] AC-02: Hovering a node reveals hover-tier properties; leaving hides them.
- [ ] AC-02b: Node edit affordance appears contextually on hover/selection.
- [ ] AC-03: A container node starts collapsed showing name + child count only.
- [ ] AC-04: Expanding a container reveals its child nodes linked to the parent.

### Browse mode

- [ ] AC-05: Free nodes are draggable; contained nodes are not.
- [ ] AC-06: Clicking canvas background clears selection and returns to browse state.

### Focus mode

- [ ] AC-07: Focusing a node centers + zooms to it, fades non-focused nodes, and makes them non-interactive.
- [ ] AC-08: Sidebar unfocus/reset returns to browse with all nodes restored.
- [ ] AC-09: Only relations attached to the focused node are visible; others are hidden or faded.
- [ ] AC-09b: 1-hop neighbors stay fully visible and interactive in default focus policy.
- [ ] AC-09c: Non-neighbors stay visible (dimmed) by default, with optional `Hide non-neighbors` toggle.

### Edit mode

- [ ] AC-10: Selecting a focused node opens an overlay modal form for property editing.
- [ ] AC-11: Editing any field marks the workspace as dirty; Save button activates.
- [ ] AC-12: Discard reverts unsaved changes; dirty indicator clears if no other pending edits.
- [ ] AC-13: Leaving edit mode is blocked while unsaved changes exist (guard rule).

### Relations

- [ ] AC-14: Clicking a relation line opens relation inspection (and editing if attributes exist).
- [ ] AC-15: Sidebar relation-type toggle hides/shows edges by type.
- [ ] AC-16: Dragging a handle from one node to another creates a new relation.

### Visual mapping

- [ ] AC-17: Changing a mapping rule (for example node category to fill color) updates the canvas immediately.
- [ ] AC-17b: Handle visibility/mode and edge style options are configurable in `View Options`.

### Layout and handles

- [ ] AC-19: `Layout All` deterministically arranges the entire visible graph.
- [ ] AC-20: `Layout Focus Neighborhood` deterministically arranges centered node + direct neighbors.
- [ ] AC-21: Handle zones support top/right/bottom/left anchors.
- [ ] AC-22: Floating-edge style anchoring picks shortest-angle attachment path.

### Mode visibility

- [ ] AC-23: A visible mode badge indicates current editor mode and allows returning to browse.

### Conflict resolution

- [ ] AC-18: An actively edited node stays visible and interactive even when filters would normally hide it.

Generated from `raw/docs_postulador_langgraph/docs/ui/node_editor_behavior_spec.md`.