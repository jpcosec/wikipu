---
identity:
  node_id: "doc:wiki/drafts/source_garage_map.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/looting/README.md", relation_type: "documents"}
---

| Layer | Piece | Garage | Exact location |

## Details

| Layer | Piece | Garage | Exact location |
|---|---|---|---|
| L1 (App) | Zustand store + undo/redo | node-editor branch | `src/stores/graph-store.ts` |
| L1 (App) | Zustand-ReactFlow sync discipline | ameliorate | `src/store/useStore.ts` |
| L1 (App) | DomainGraph contract + translator | prismaliser | `src/lib/layout.ts` + schema transform |
| L2 (Canvas) | Dagre layout engine | prismaliser | `src/lib/layout.ts` |
| L2 (Canvas) | NodeShell + toolbar + zoom tiers | node-editor branch | `src/features/graph-editor/L2-canvas/NodeShell.tsx` |
| L2 (Canvas) | NodeShell toolbar aesthetics | ui.reactflow.dev | NodeToolbar component docs |
| L2 (Canvas) | Selection/hover aesthetics | Dify | `web/app/components/workflow/nodes/` |
| L2 (Canvas) | GroupShell + NodeResizer | node-editor branch | `src/features/graph-editor/L2-canvas/GroupShell.tsx` |
| L2 (Canvas) | Floating edges | node-editor branch | `src/features/graph-editor/L2-canvas/edges/` |
| L2 (Canvas) | Edge inheritance (collapse) | node-editor branch | `src/features/graph-editor/L2-canvas/hooks/use-edge-inheritance.ts` |
| L2 (Canvas) | Parent-child hierarchy | chaiNNer | `src/util/graph-util.ts` |
| L2 (Canvas) | Ghost drag + selection box | chaiNNer | SelectionBox implementation |
| L2 (Canvas) | Smart / dynamic handles | Dify | `web/app/components/workflow/nodes/` |
| L3 (Content) | Node type registry | node-editor branch | `src/schema/registry.ts` |
| L3 (Content) | InternalNodeRouter | agentok | `frontend/src/nodes/index.ts` |
| L3 (Content) | FallbackNode | node-editor + agentok | `NodeShell.tsx` unknown branch |
| UX | Keyboard shortcuts | node-editor branch | `L2-canvas/hooks/use-keyboard.ts` |
| UX | Inspector Sheet panel | node-editor branch | `L2-canvas/panels/NodeInspector.tsx` |
| UX | GraphEditor shell + sidebar | node-editor branch | `L2-canvas/GraphEditor.tsx` + `sidebar/` |
| UX | Focus + neighborhood radial | ReactFlow examples | [reactflow.dev/examples](https://reactflow.dev/examples/layout/force-layout) |
| UI | Missing shadcn components | node-editor branch | `src/components/ui/` |

Generated from `raw/docs_postulador_ui/plan/looting/README.md`.