---
identity:
  node_id: "doc:wiki/drafts/reference_external_projects_compare_point.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/index_checklist.md", relation_type: "documents"}
---

> These are open-source projects analyzed during design of the node-editor branch.

## Details

> These are open-source projects analyzed during design of the node-editor branch.
> Listed here because they solved problems our current implementation still has open.

### Problems our implementation has — and where they were solved

**Hardcoded node types leaking into L2**
Our `CvGraphCanvas` and `MatchGraphCanvas` check `node.category` / `node.type` directly.
- Fix pattern: `agentok` → `frontend/src/nodes/index.ts` — a plain `{ [typeId]: Component }` map, no conditionals in the canvas layer.
- Rule: L2 must never branch on a type string. Unknown `typeId` → `FallbackNode` (renders raw JSON), not a red error box.

**No formal data contract at the graph entry point**
`cvToGraph` and `matchToGraph` accept loosely-typed objects; schema changes break silently.
- Fix pattern: `prismaliser` → `src/lib/layout.ts` + schema transform. Formalise with a typed `DomainGraph` interface at the boundary:
  ```ts
  interface DomainGraph {
    entities: Array<{ id: string; typeId: string; properties: Record<string, unknown> }>;
    relations: Array<{ sourceId: string; targetId: string; label?: string }>;
    schema: Record<string, { label: string; icon?: string; l3ComponentId: string }>;
  }
  ```
  The translator (`schema-to-graph.ts`) must be a **pure function** — testable in isolation, no side effects, fails at TypeScript level if `DomainGraph` contract is violated.

**Collapse/expand re-layout not triggering**
When a group collapses in D2, sibling nodes don't reflow to fill the space.
- Fix pattern: L3 emits a size-change signal → L2 re-runs Dagre. `use-edge-inheritance` + `use-graph-layout` in node-editor branch already wire this up; our D2 implementation skips the re-layout step.

**Focus mode is declared but not implemented**
`ui-store` has `'focus'` as an editor state but nothing moves when it activates.
- Fix pattern: d3-force repulsion around the focused node. On `setEditorState('focus')`, compute neighbor distances and apply position offsets so related nodes orbit the hero. Reference: [react-flow force layout examples](https://reactflow.dev/examples/layout/force-layout) + d3-force.
- Layer attribution: L1 owns which node is hero → L2 applies force layout → L3 receives `isFocused` prop and can expand detail tier.

### Layer ownership reference (anti-confusion map)

| Behavior | L1 (App) | L2 (Canvas/Shell) | L3 (Node Content) |
|---|---|---|---|
| Collapse/expand attributes | — | re-layout after | owns toggle state |
| Toolbar (edit, delete, copy) | — | `NodeToolbar` wrapper | — |
| Hover highlight | — | detects `onMouseEnter`, applies CSS | receives `hovered` prop |
| Focus + neighborhood radial | sets hero node id | applies d3-force, dims non-neighbors | receives `isFocused` |
| Undo/redo | — | `graph-store` semantic actions | `isVisualOnly` for visual-only changes |

### Manual de vuelo (anti-hardcoding rules)

1. **L2 is type-blind.** No `if (typeId === 'person')` anywhere in canvas or shell code. All branching goes through the registry.
2. **Translator is a pure function.** `DomainGraph → { nodes, edges }`. No imports from UI layers. Must have unit tests before connecting to any real data source.
3. **Unknown types get a FallbackNode.** Never a crash, never a silent blank. Raw JSON dump styled as a debug card.
4. **Visual actions don't pollute undo history.** Drag position, zoom, hover, selection → `isVisualOnly: true`. Only semantic edits (rename, delete, add edge) go into the undo stack.

---

Generated from `raw/docs_postulador_ui/plan/index_checklist.md`.