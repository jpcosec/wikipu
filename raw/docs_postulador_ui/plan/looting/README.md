# Looting Plan

Each file describes one adaptation: what it solves, what we currently have, what it
will break/require, and the concrete code to port or use as reference.

## Pieces

| # | File | Piece | Source | Priority |
|---|---|---|---|---|
| 01 | `01-zustand-stores.md` | Zustand graph-store + ui-store + types | node-editor branch | P0 — everything depends on this |
| 02 | `02-floating-edges.md` | FloatingEdge + ButtonEdge + edge-helpers | node-editor branch | P0 — fixes broken edge routing |
| 03 | `03-use-edge-inheritance.md` | Group collapse/expand with edge re-routing | node-editor branch | P0 — fixes D2 collapse |
| 04 | `04-use-keyboard.md` | Keyboard shortcut handler | node-editor branch | P1 |
| 05 | `05-group-shell.md` | GroupShell with NodeToolbar + NodeResizer | node-editor branch | P1 — depends on 01, 03 |
| 06 | `06-node-shell-zoom-tiers.md` | Universal NodeShell with zoom tiers + context menu | node-editor branch | P1 — depends on 01, 07, 10 |
| 07 | `07-node-type-registry.md` | NodeTypeRegistry + register-defaults | node-editor branch | P1 — needed for 06 |
| 08 | `08-use-graph-layout.md` | Dagre layout hook (on-demand, undo-safe) | node-editor / prismaliser | P1 — depends on 01 |
| 09 | `09-node-inspector-sheet.md` | NodeInspector Sheet panel | node-editor branch | P2 — depends on 01, 10 |
| 10 | `10-shadcn-components.md` | Missing shadcn/ui components | node-editor branch | P1 — install before 06, 09, 14 |
| 11 | `11-domain-graph-contract.md` | DomainGraph typed entry contract | prismaliser pattern | P1 — clean translator boundary |
| 12 | `12-fallback-node.md` | FallbackNode for unknown typeId | node-editor + agentok | P1 — no crashes on bad data |
| 13 | `13-focus-neighborhood-layout.md` | Focus mode with d3-force radial layout | ReactFlow examples | P3 — nice-to-have |
| 14 | `14-graph-editor-shell.md` | GraphEditor L2 shell + CanvasSidebar | node-editor branch | P2 — depends on 01–12 |
| 15 | `15-internal-node-router.md` | InternalNodeRouter + L3 COMPONENT_REGISTRY | agentok | P1 — L2 agnosticism |
| 16 | `16-parent-child-hierarchy.md` | parentNode + extent:'parent' + recursive collapse | chaiNNer + ReactFlow | P2 — document hierarchies |
| 17 | `17-zustand-flow-sync.md` | Shadow state mirror: drag-end sync discipline | ameliorate | P1 — prevents position loss on save |
| 18 | `18-smart-edges-dynamic-handles.md` | Dynamic handles pointing to L3 sub-components | Dify Workflow Editor | P3 — field-level connections |
| 19 | `19-ghost-drag-selection.md` | Ghost drag + custom selection box (perf) | chaiNNer | P3 — large graph performance |

## Dependency order (suggested porting sequence)

```
10 (shadcn install)  ← do this first, no deps

01 (stores + sync discipline from 17)
  ├─ 02 (floating edges)
  ├─ 03 (edge inheritance)  →  05 (GroupShell)  →  16 (recursive collapse)
  ├─ 08 (layout hook)
  └─ 11 (DomainGraph contract)  →  15 (InternalNodeRouter + L3 registry)

07 (type registry)  →  06 (NodeShell + zoom tiers + 12 FallbackNode inline)
                    └─  09 (Inspector Sheet)
                    └─  14 (GraphEditor shell)

04 (keyboard)       →  mounts inside 14
13 (focus layout)   →  after stores + layout stable
18 (smart handles)  →  after L3 registry + NodeShell stable
19 (ghost drag)     →  last, only if performance is an actual problem
```

## Source garage map

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
