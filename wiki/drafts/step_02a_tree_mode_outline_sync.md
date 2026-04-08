---
identity:
  node_id: "doc:wiki/drafts/step_02a_tree_mode_outline_sync.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md", relation_type: "documents"}
---

### 1. Architecture Logic

## Details

### 1. Architecture Logic

Sidebar tree panel derived from graph_content's container relationships. No separate data model. Bidirectional sync with canvas.

**Sync contract:**
- Selection: tree click → canvas focus. Canvas click → tree highlight.
- Expand/collapse: syncs both directions.
- Drag reorder in tree → dispatches same semantic action as canvas.
- Cross-container drag in tree → same as canvas.

**Placement:** Sidebar panel extension via FlexLayout. Dockable left/right/float.

**Per item:** Node icon (from registry), label, child count badge, type indicator. No payload preview.

### 2. Objectives

1. Tree reflects container hierarchy from graph_content
2. Bidirectional selection sync
3. Bidirectional expand/collapse sync
4. Drag reorder in tree is undoable
5. Tree updates reactively on graph_content changes
6. Tree is a dockable sidebar panel (FlexLayout)

### 3. Don'ts

- **Don't create a separate tree data model.** graph_content IS the tree.
- **Don't show non-hierarchical edges in tree.** Containment only.
- **Don't add content preview.** Tree is for navigation.
- **Don't make tree required.** Optional panel.
- **Don't implement tree-only mutations.** Same semantic actions as canvas.

### 4. Known Gaps & Open Questions

Performance at 200+ nodes — react-arborist handles virtualization but needs testing.

### 5. Library Decision Matrix

**LIB-TREE-01**: react-arborist (committed). Built-in virtualization, drag-drop, keyboard nav, controlled mode.

### 6. Test Plan

- **Unit**: Tree derivation from graph_content produces correct hierarchy.
- **Component**: Click tree item → onFocus fires. Drag reorder → dispatches action.
- **Integration**: Create nested structure → open tree → select → canvas focuses → collapse in tree → canvas collapses.

### 7. Review Checklist

- [ ] Tree derives from graph_content
- [ ] Selection sync both directions
- [ ] Expand/collapse sync both directions
- [ ] Drag dispatches semantic actions
- [ ] Tree is optional FlexLayout panel

---

Generated from `raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md`.