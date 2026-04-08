---
identity:
  node_id: "doc:wiki/drafts/what_does_it_solve.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/looting/01-zustand-stores.md", relation_type: "documents"}
---

Our current graph state lives in component-local `useNodesState` / `useEdgesState` hooks

## Details

Our current graph state lives in component-local `useNodesState` / `useEdgesState` hooks
(`CvGraphCanvas`, `MatchGraphCanvas`) and a `KnowledgeGraphContext` that couples data with
ReactFlow internals. Problems:

- No undo/redo — position drags and semantic edits are equally untrackable.
- Collapse/expand state lives inside the canvas component, making it impossible to drive
  from outside (e.g., a sidebar button).
- Multiple components re-read the same state via prop drilling or context re-renders.
- No separation between "visual-only" changes (drag, selection) and "semantic" changes
  (rename, delete, add edge), so a re-layout wipes the undo stack.

The Zustand stores solve all of this by owning graph truth globally with a semantic action
history. `isVisualOnly: true` keeps drag positions and selection out of the undo stack.

---

Generated from `raw/docs_postulador_ui/plan/looting/01-zustand-stores.md`.