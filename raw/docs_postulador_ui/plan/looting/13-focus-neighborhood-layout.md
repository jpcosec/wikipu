# Piece: Focus Mode — Neighborhood Radial Layout

**Source:** ReactFlow d3-force examples + ui-store `'focus'` editor state (node-editor)

---

## Where it goes

```
apps/review-workbench/src/features/graph-editor/L2-canvas/hooks/
  use-focus-layout.ts     ← new hook

apps/review-workbench/src/features/graph-editor/L2-canvas/
  GraphCanvas.tsx         ← apply dim effect on non-neighbors
```

---

## What does it solve

`ui-store` declares `editorState: 'focus'` and `focusedNodeId: string | null`, but
nothing happens when `setEditorState('focus')` is called. Clicking "Focus Neighborhood"
in the `NodeShell` context menu sets the state but the canvas doesn't react.

The intended behaviour (from the Chewbacca conversation and the ui-store design):
- The focused node moves to a central position.
- Its direct neighbors orbit around it using a force-directed repulsion.
- Non-neighbor nodes are dimmed (CSS opacity) and pushed to the canvas periphery.
- Exiting to `'browse'` state restores the full layout.

This is the most complex piece in the looting list. It is lower priority than the
others — implement after stores, edge inheritance, and the registry are stable.

---

## How we have it implemented

Not implemented at all. `focusedNodeId` is set in the store but nothing reads it in
the canvas layer. `MatchGraphCanvas` has a `focusedNodeId` prop that dims non-matching
nodes via a `highlighted` flag on node data, but it is driven by search, not by the
store, and does not reposition nodes.

---

## What will it affect (collateral modifications)

| File | Change needed |
|---|---|
| `stores/ui-store.ts` | `focusedNodeId` and `setEditorState('focus')` must be present |
| `stores/graph-store.ts` | `updateNode(..., { isVisualOnly: true })` used for position + opacity patches |
| `GraphCanvas.tsx` | Subscribe to `editorState`; apply `opacity` style to non-neighbor nodes |
| `NodeShell.tsx` | "Focus Neighborhood" context menu item already wires to `setEditorState('focus')` |
| `use-graph-layout.ts` | Layout must be callable after focus exits to restore positions |
| `package.json` | Add `d3-force` (or `@d3/force-simulation` types) |

---

## Concrete code pieces + source

### Layer attribution (from manual de vuelo)

| Responsibility | Owner |
|---|---|
| Which node is the hero | L1 / `ui-store.focusedNodeId` |
| Force simulation & position updates | L2 `use-focus-layout` hook |
| Dim non-neighbors | L2 `GraphCanvas` reads `editorState` + neighbor set |
| Expand detail tier | L3 — node receives `isFocused` prop and can show more |

### Hook skeleton

```ts
import { forceSimulation, forceLink, forceManyBody, forceCenter } from 'd3-force';

export function useFocusLayout() {
  const editorState = useUIStore((s) => s.editorState);
  const focusedNodeId = useUIStore((s) => s.focusedNodeId);
  const nodes = useGraphStore((s) => s.nodes);
  const edges = useGraphStore((s) => s.edges);
  const updateNode = useGraphStore((s) => s.updateNode);

  useEffect(() => {
    if (editorState !== 'focus' || !focusedNodeId) return;

    // 1. Find neighbors
    const neighborIds = new Set(
      edges
        .filter((e) => e.source === focusedNodeId || e.target === focusedNodeId)
        .flatMap((e) => [e.source, e.target])
    );

    // 2. Run d3-force simulation for hero + neighbors only
    const simNodes = nodes
      .filter((n) => n.id === focusedNodeId || neighborIds.has(n.id))
      .map((n) => ({ id: n.id, x: n.position.x, y: n.position.y }));

    const simulation = forceSimulation(simNodes)
      .force('charge', forceManyBody().strength(-300))
      .force('center', forceCenter(0, 0))
      .stop();

    // Run synchronously (tick N times)
    for (let i = 0; i < 100; i++) simulation.tick();

    // 3. Apply positions via visual-only updates
    simNodes.forEach(({ id, x, y }) => {
      updateNode(id, { position: { x, y } }, { isVisualOnly: true });
    });

    // 4. Push non-neighbors far away
    nodes
      .filter((n) => n.id !== focusedNodeId && !neighborIds.has(n.id))
      .forEach((n) => {
        updateNode(n.id, { style: { opacity: 0.15 } }, { isVisualOnly: true });
      });

    return () => {
      // Restore on exit — trigger relayout
    };
  }, [editorState, focusedNodeId]);
}
```

### ReactFlow reference

[ReactFlow Force Layout example](https://reactflow.dev/examples/layout/force-layout) —
shows the d3-force integration pattern with `useEffect` + `simulation.tick()`.

**External reference (Chewbacca conversation):**
> "On `setEditorState('focus')`, compute neighbor distances and apply position offsets
> so related nodes orbit the hero. L1 owns which node is hero → L2 applies force
> layout → L3 receives `isFocused` prop and can expand detail tier."
