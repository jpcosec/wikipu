---
identity:
  node_id: "doc:wiki/drafts/how_we_have_it_implemented.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/looting/01-zustand-stores.md", relation_type: "documents"}
---

- `CvGraphCanvas.tsx:15` — `useNodesState` / `useEdgesState` from ReactFlow (ephemeral).

## Details

- `CvGraphCanvas.tsx:15` — `useNodesState` / `useEdgesState` from ReactFlow (ephemeral).
- `pages/global/KnowledgeGraph.tsx` — `SimpleNode[]` / `SimpleEdge[]` state owned by the
  page, passed as props into ReactFlow. No undo. Collapse state is a local `Set<string>`.
- `MatchGraphCanvas.tsx` — nodes/edges derived via `useMemo` on every render from parent
  props; no store at all.

---

Generated from `raw/docs_postulador_ui/plan/looting/01-zustand-stores.md`.