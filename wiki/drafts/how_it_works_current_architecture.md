---
identity:
  node_id: "doc:wiki/drafts/how_it_works_current_architecture.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/ui/node_editor_customization_and_architecture.md", relation_type: "documents"}
---

### 1) Frontend runtime (sandbox)

## Details

### 1) Frontend runtime (sandbox)

- The editor is a single React Flow page (`NodeEditorInner`) with local state for nodes, edges, filters, focus, edit drafts, and save/discard snapshots.
- Core state machine is `EditorState = "browse" | "focus" | "edit_node" | "edit_relation"`.
- React Flow state is managed with `useNodesState` and `useEdgesState`.
- Render output is derived through two pipelines:
  - `displayNodes`: applies filter/focus/edit visibility and interactivity.
  - `displayEdges`: applies relation-type filtering + focus dim/hide behavior.
- Save/discard in the sandbox is workspace-local (snapshot compare via `serializeGraph`) and does not call backend APIs.

### 2) Focus and connect behavior

- Focus neighbor graph is computed by `neighborsForNode`.
- Default focus UX now starts with `hideNonNeighbors = true`.
- The `Vacant nodes` drawer computes candidates from non-connected nodes under active constraints (`vacantCandidateNodes`) and creates links with `onConnectFromVacantDrawer`.
- This means you can still connect to currently hidden non-neighbors from the drawer while focused.

### 3) Layout behavior

- `Layout all` uses deterministic Dagre (`layoutAllDeterministic`).
- `Layout focus` uses deterministic radial arrangement around focused node (`layoutFocusNeighborhood`).
- `Layout custom` restores saved manual ordering from a pre-layout position snapshot (`snapshotNodePositions` + `applySavedNodePositions`).

### 4) Backend (where graph data comes from)

- API endpoints:
  - `GET /api/v1/portfolio/base-cv-graph`
  - `GET /api/v1/portfolio/cv-profile-graph`
  - `PUT /api/v1/portfolio/cv-profile-graph`
- Backend payload assembly and persistence are implemented in `read_models.py`:
  - baseline source profile: `data/reference_data/profile/base_profile/profile_base_data.json`
  - saved override file name: `cv_profile_graph_saved.json` (`SAVED_GRAPH_FILENAME`)

Generated from `raw/docs_postulador_langgraph/docs/ui/node_editor_customization_and_architecture.md`.