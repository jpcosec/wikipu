---
identity:
  node_id: "doc:wiki/drafts/what_will_it_affect_collateral_modifications.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/looting/01-zustand-stores.md", relation_type: "documents"}
---

| File | Change needed |

## Details

| File | Change needed |
|---|---|
| `CvGraphCanvas.tsx` | Replace `useNodesState`/`useEdgesState` with `useGraphStore` selectors |
| `pages/global/KnowledgeGraph.tsx` | Remove node/edge state; read from `graph-store` |
| `MatchGraphCanvas.tsx` | Remove `useMemo` node/edge derivation; use store |
| `BaseCvEditor.tsx` | Call `loadGraph()` on mount instead of passing raw arrays |
| `pages/job/Match.tsx` | Same as BaseCvEditor |
| `features/base-cv/lib/cvToGraph.ts` | Output must match `ASTNode[]` / `ASTEdge[]` |
| `features/job-pipeline/lib/matchToGraph.ts` | Same |

---

Generated from `raw/docs_postulador_ui/plan/looting/01-zustand-stores.md`.