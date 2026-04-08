# Piece: use-graph-layout (Dagre Layout Hook)

**Source:** `node-editor` branch

---

## Where it goes

```
apps/review-workbench/src/features/graph-editor/L2-canvas/hooks/
  use-graph-layout.ts
```

---

## What does it solve

Our current Dagre usage in `CvGraphCanvas.tsx` runs inside a `useMemo` that recomputes
on every render and bakes the positions directly into the node array that feeds
`useNodesState`. This means:

- Layout runs eagerly on load, but never again (no way to trigger a relayout after a
  collapse/expand without remounting the canvas).
- Computed positions are part of `useNodesState`, so a relayout creates a full node
  array replacement — triggering ReactFlow to re-render every node simultaneously.
- Layout never integrates with undo/redo because it bypasses the store entirely.

`use-graph-layout` solves this by:

1. Reading nodes/edges from `graph-store` (not local state).
2. Running Dagre purely on demand via a `layout()` function (not on render).
3. Applying positions via `updateNode(..., { isVisualOnly: true })`, so the undo stack
   is never polluted by a relayout.
4. Returning the computed positions so the caller can chain further work
   (e.g., call `layout()` after a collapse/expand to reflow siblings).

---

## How we have it implemented

`CvGraphCanvas.tsx:~60` — Dagre called in `useMemo` at render time using `@dagrejs/dagre`
directly. Positions are baked into the initial node array. No re-layout capability.

`MatchGraphCanvas.tsx` — no layout; positions come from the fixture JSON (fixed).

`KnowledgeGraph.tsx` — no layout; positions assigned manually in `KnowledgeGraph.tsx`
or via fixture coordinates.

---

## What will it affect (collateral modifications)

| File | Change needed |
|---|---|
| `stores/graph-store.ts` | Must be present — hook reads `nodes`, `edges`, calls `updateNode` |
| `CvGraphCanvas.tsx` | Remove inline Dagre `useMemo`; call `layout()` on mount and after collapse |
| `GroupShell.tsx` | After toggle, call `layout()` so siblings reflow around the collapsed group |
| `GraphEditor.tsx` / `CanvasSidebar.tsx` | Expose a "Re-layout" button wired to `layout()` |

---

## Concrete code pieces + source

### Hook API

```ts
export interface LayoutOptions {
  direction?: 'LR' | 'TB' | 'RL' | 'BT'; // default 'LR'
  nodeSpacing?: number;   // default 50
  rankSpacing?: number;   // default 100
}

export function useGraphLayout(): {
  layout: (options?: LayoutOptions) => Array<{ id: string; position: { x: number; y: number } }>;
}
```

### Core Dagre wiring

```ts
function getLayoutedElements(nodes, edges, options): LayoutResult {
  const dagreGraph = new dagre.graphlib.Graph();
  dagreGraph.setDefaultEdgeLabel(() => ({}));
  dagreGraph.setGraph({ rankdir: options.direction ?? 'LR', nodesep: 50, ranksep: 100 });

  nodes.forEach((n) => dagreGraph.setNode(n.id, { width: 200, height: 80 }));
  edges.forEach((e) => dagreGraph.setEdge(e.source, e.target));

  dagre.layout(dagreGraph);

  return nodes.map((n) => {
    const { x, y, width, height } = dagreGraph.node(n.id);
    return { id: n.id, position: { x: x - width / 2, y: y - height / 2 } };
  }).filter(Boolean);
}

export function useGraphLayout() {
  const nodes = useGraphStore((s) => s.nodes);
  const edges = useGraphStore((s) => s.edges);
  const updateNode = useGraphStore((s) => s.updateNode);

  const layout = useCallback((options = {}) => {
    const result = getLayoutedElements(nodes, edges, options);
    result.forEach(({ id, position }) =>
      updateNode(id, { position }, { isVisualOnly: true })
    );
    return result;
  }, [nodes, edges, updateNode]);

  return { layout };
}
```

**Full source:** `node-editor:apps/review-workbench/src/features/graph-editor/L2-canvas/hooks/use-graph-layout.ts`
