---
identity:
  node_id: "doc:wiki/drafts/pieces.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/looting/README.md", relation_type: "documents"}
---

| # | File | Piece | Source | Priority |

## Details

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

Generated from `raw/docs_postulador_ui/plan/looting/README.md`.