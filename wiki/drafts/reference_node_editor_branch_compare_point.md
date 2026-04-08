---
identity:
  node_id: "doc:wiki/drafts/reference_node_editor_branch_compare_point.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/index_checklist.md", relation_type: "documents"}
---

> Branch `node-editor` contains a parallel implementation of the graph editor with a more

## Details

> Branch `node-editor` contains a parallel implementation of the graph editor with a more
> mature architecture. Items below are available to port — ordered by priority.

### Immediately applicable (graph work, D2+)

- **`stores/graph-store.ts`** — Zustand graph store with semantic undo/redo (`CREATE_ELEMENTS`, `DELETE_ELEMENTS`, `UPDATE_NODE`, `UPDATE_EDGE`). `isVisualOnly` flag keeps drag/selection out of undo history. Replaces `KnowledgeGraphContext`.
- **`stores/ui-store.ts`** — Separate Zustand UI store: editor mode (`browse` / `focus` / `edit_node` / `edit_relation`), filter state, delete-confirm flow, command-dialog toggle.
- **`stores/types.ts`** — `ASTNode`, `ASTEdge`, `SemanticAction` — typed AST layer over ReactFlow primitives.
- **`hooks/use-edge-inheritance.ts`** — `collapseGroupEdges` / `expandGroupEdges`: hides child nodes and re-routes edges to the group parent. The clean version of what D2 collapse/expand needs.
- **`edges/FloatingEdge.tsx` + `edges/edge-helpers.ts`** — Auto-detect source/target attachment geometry (floating handles). Edges with `relationType === 'inherited'` render dashed/dimmed automatically.
- **`edges/ButtonEdge.tsx`** — Extends FloatingEdge with a hover-reveal `×` delete button on the edge path.
- **`hooks/use-keyboard.ts`** — Enter = edit focused node, Escape = browse, Ctrl+Z/Y = undo/redo. Includes `isEditableTarget()` guard so inputs aren't captured.
- **`L2-canvas/GroupShell.tsx`** — Group node with `NodeToolbar` collapse/expand button, `NodeResizer`, handles only when expanded. Pairs with `use-edge-inheritance`.

### For D1 (schema explorer) and beyond

- **`schema/registry.ts`** — `NodeTypeRegistry` class: `register`, `get`, `validatePayload` (Zod), `sanitizePayload`, `canConnect`, `getAll`. Fully tested.
- **`schema/registry.types.ts`** — `NodeTypeDefinition`: `typeId`, `label`, `icon`, `colorToken`, `defaultSize`, `renderers` (detail/label/dot tiers), `payloadSchema`, `sanitizer`, `allowedConnections`.
- **`L2-canvas/NodeShell.tsx`** — Registry-driven node shell with zoom-level rendering tiers (detail ≥0.9×, label ≥0.4×, dot below), context menu (edit / focus neighborhood / copy / delete), category color overrides.
- **`hooks/use-graph-layout.ts`** — Dagre layout hook that reads from graph-store and applies positions with `isVisualOnly: true` (no undo pollution).

### Lower priority (polish)

- **`components/ui/`** — shadcn components not yet in ui-redesign: `command`, `context-menu`, `sheet`, `dropdown-menu`, `popover`, `scroll-area`, `accordion`, `sonner`.
- **`L2-canvas/panels/NodeInspector.tsx`** — Sheet-based node editor form (shadcn `Sheet`), more polished than current inline inspector.

---

Generated from `raw/docs_postulador_ui/plan/index_checklist.md`.