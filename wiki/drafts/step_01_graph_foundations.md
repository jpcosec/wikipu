---
identity:
  node_id: "doc:wiki/drafts/step_01_graph_foundations.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md", relation_type: "documents"}
---

### 1. Architecture Logic

## Details

### 1. Architecture Logic

The NodeEditor is the single graph editing surface. It must support everything CvGraphEditor does today while remaining domain-agnostic via the representation schema.

**Four state layers (zustand store):**

- **graph_content** — nodes (with typed payloads), edges (with typed payloads), container relationships (parent_id, child ordering). Domain truth.
- **graph_view** — viewport, selected/focused IDs, collapsed containers, visible relation types, active layout preset, active view, active EditorState (5-state machine: browse/focus/focus_relation/edit_node/edit_relation). Per-session, not persisted by default. `active_view` references a view from the loaded schema (00c). Switching schemas resets `active_view` to the new schema's default view. Switching views within a schema triggers the view's declared query (if subgraph type) or filter application.
- **graph_history** — semantic action log. Only domain mutations, not view changes.
- **external_refs** — pointers to documents, datasources, schemas, annotation anchors. References, not copies. Shape: `{ ref_id, ref_type: "document" | "datasource" | "schema" | "anchor", target_uri: string, node_id?: string, metadata?: Record<string, unknown> }`. Resolution happens lazily at render time (e.g., document ref resolved when inspector section mounts). This is a forward declaration — 03 (anchor_refs) and 04 (datasource refs) populate specific ref_types. Initial implementation only needs the shape; resolution logic comes with each consuming step.

**What this absorbs from CvGraphEditor:**
- Container/group model → first-class graph_content concept
- Proxy edges → view-layer behavior driven by container state
- Typed payloads (entries, skills) → handled by schema + registry (01b)
- API persistence → generalized into pluggable persistence boundary
- Drag reorder → semantic action in graph_history

**Persistence boundary:** graph_content and external_refs are persistable. graph_view is session-local with optional named snapshots (→ 01a presets). graph_history is append-only, optionally persistable for audit. Persistence API is pluggable — localStorage for sandbox, REST API for production, neo4j adapter for graph database.

### 2. Objectives

1. Written state contract covers all four layers and accommodates container nesting
2. NodeEditor can represent everything CvGraphEditor currently does through the contract
3. Adding a new layout preset (01a) or node type (01b) does not require changing the state contract shape
4. Persistence boundary is explicit: what's saved, what's session-only, what's optional
5. zustand store replaces the current useState sprawl
6. Persistence API is pluggable (localStorage, REST, neo4j)

### 3. Don'ts

- **Don't persist graph_view by default.** View state is ephemeral. Named presets (01a) are the deliberate persistence mechanism.
- **Don't put annotation content in graph_content.** Annotations are references (external_refs), not graph nodes.
- **Don't implement container rendering here.** This step defines that containers exist in the data model. Rendering comes in 02.
- **Don't add undo/redo implementation here.** This step defines what actions are loggable. 01c defines undo/redo.
- **Don't design around CvGraphEditor's API shape.** Persistence API should be generic.

### 4. Known Gaps & Open Questions

- **GAP-ARCH-01** (Blocker → resolved here): No shared persistence boundary — this step defines it.
- **GAP-ARCH-02** (High → resolved here): No unified state contract — this step creates it.
- **GAP-IMPL-01** (High): NodeEditor has no save/load — persistence API addresses this.

### 5. Library Decision Matrix

**LIB-STATE-01**: zustand (committed). Smallest API surface, works outside React, devtools support, no provider boilerplate. Middleware for persistence (zustand/middleware persist) and undo (temporal or custom).

### 6. Test Plan

- **Unit**: State layer separation — graph_content mutation doesn't affect graph_view. Container nesting model (parent_id, child ordering). Pluggable persistence serialization/deserialization.
- **Component**: NodeEditor hydrates from a shared fixture including containers.
- **Integration**: Save graph → reload → state matches. Switch persistence adapter → same behavior.

### 7. Review Checklist

- [ ] State contract file exists with all four layers
- [ ] Container model in graph_content (parent_id, child ordering)
- [ ] Persistence boundary documented
- [ ] No graph_view in persistence
- [ ] zustand store replaces useState
- [ ] Pluggable persistence API defined

---

Generated from `raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md`.