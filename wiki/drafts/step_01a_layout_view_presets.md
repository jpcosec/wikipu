---
identity:
  node_id: "doc:wiki/drafts/step_01a_layout_view_presets.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md", relation_type: "documents"}
---

### 1. Architecture Logic

## Details

### 1. Architecture Logic

elkjs from the start. No dagre. Compound/nested layout natively supports containers (02) and document subflows without migration.

**Six preset types:**
- `dag_default` — elkjs layered algorithm, left-to-right
- `focus_centered` — concentric rings around a focal node
- `timeline_horizontal(property)` — sort by date/sequence on X axis
- `compare_lanes(left_prop, right_prop)` — two-column comparison
- `tree_top_down(root_rule)` — elkjs tree algorithm
- `manual_saved(name)` — user-positioned snapshot

**Saved view = preset + viewport + collapsed_state + filter_state + panel_layout (FlexLayout serialized state).** Persisted only when explicitly named.

**Each schema view can declare its default layout** — views that are subgraph queries get their own preset.

elkjs feeds React Flow directly. No abstraction layer.

### 2. Objectives

1. User can select a preset type and graph re-layouts via elkjs
2. User can name and save the current view (preset + viewport + filters + collapsed state + panel layout)
3. Reloading a saved view restores the full visual state
4. elkjs compound layout works with container/child relationships
5. Property-driven presets (timeline, compare) work with any attribute key
6. Schema views declare default layouts

### 3. Don'ts

- **Don't store node positions in graph_content.** Positions are view state.
- **Don't auto-save presets.** Explicit user action only.
- **Don't tune elkjs parameters per-graph.** Sensible defaults per preset type.
- **Don't keep dagre as fallback.** Full migration to elkjs.

### 4. Known Gaps & Open Questions

- **GAP-IMPL-03** (resolved here): Layout presets are local state only.
- Property-driven presets need attribute type awareness (which properties are dates? numbers?) — resolved by schema's attribute declarations.

### 5. Library Decision Matrix

**LIB-LAYOUT-01**: elkjs (committed). WASM worker for non-blocking layout. Handles compound, layered, tree, force algorithms in one library.

### 6. Test Plan

- **Unit**: Each preset type produces deterministic positions for a fixture graph. Compound layout respects parent-child containment. Save/restore round-trip preserves all view state fields. Property-driven preset: fixture graph with date attributes → `timeline_horizontal("created_at")` → nodes ordered by date on X axis.
- **Integration**: Apply preset → save → reload → viewport matches. Schema view declares layout → view loads with correct preset.

### 7. Review Checklist

- [ ] elkjs integrated, dagre removed
- [ ] All 6 preset types work
- [ ] Save/restore view works
- [ ] Compound layout handles containers
- [ ] Schema views declare default layouts
- [ ] No positions in graph_content

---

Generated from `raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md`.