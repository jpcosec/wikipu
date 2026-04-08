# Piece: Ghost Drag & Selection Box (Mass Selection Performance)

**Source:** chaiNNer — custom `SelectionBox` implementation

---

## Where it goes

```
apps/review-workbench/src/features/graph-editor/L2-canvas/
  styles/selection.css        ← selection box and ghost drag CSS
  hooks/use-ghost-drag.ts     ← ghost position tracking during multi-node drag
```

---

## What does it solve

When the user selects and drags 30+ nodes simultaneously, ReactFlow re-renders every
selected node on every mouse move event — each with its own layout recalculation.
On graphs with complex node content (markdown editors, attribute lists), this creates
visible lag.

The ghost drag pattern decouples visual feedback from actual node position updates:

1. **During drag:** render a single lightweight ghost rectangle showing where the
   selection will land. The actual nodes stay frozen at their original positions.
2. **On drag end (`onNodeDragStop`):** apply the delta offset to all selected nodes via
   `graph-store.updateNode`. One batch update instead of N continuous updates.

Similarly, ReactFlow's default selection box (drag on empty canvas) can be replaced with
a custom styled version that matches the Terran Command dark theme — the default is a
bright blue rectangle that clashes.

**Scope note:** Lower priority. Implement when graph views routinely have 20+ nodes
visible simultaneously (Knowledge Graph, schema explorer). Not needed for CV or Match
graphs which are smaller.

---

## How we have it implemented

Not implemented. Multi-node drag uses ReactFlow's default behaviour — every node
re-renders on every `mousemove`. There is no ghost and no custom selection box.

The Terran Command theme has partial ReactFlow style overrides in `styles.css` but does
not address selection box colour or drag performance.

---

## What will it affect (collateral modifications)

| File | Change needed |
|---|---|
| `GraphCanvas.tsx` | Add `onNodeDragStop` handler; pass `selectionOnDrag={true}` and custom `selectionStyle` |
| `stores/graph-store.ts` | `updateNode` batch variant: `updateNodes(patches[])` to avoid multiple renders |
| `styles.css` / `selection.css` | Override `.react-flow__selection` with Terran Command colours |
| `use-graph-layout.ts` (piece 08) | Layout should not run during active drag — add drag guard |

---

## Concrete code pieces + source

### Custom selection box styles (`selection.css`)

```css
/* Override ReactFlow's default bright-blue selection */
.react-flow__selection {
  background: rgba(0, 242, 255, 0.04);
  border: 1.5px solid rgba(0, 242, 255, 0.4);
  border-radius: 4px;
}

/* Ghost placeholder during multi-drag */
.node-ghost {
  position: absolute;
  border: 1.5px dashed rgba(0, 242, 255, 0.5);
  border-radius: 8px;
  background: rgba(0, 242, 255, 0.04);
  pointer-events: none;
  transition: none; /* no animation during drag */
}
```

### `use-ghost-drag.ts`

```ts
export function useGhostDrag() {
  const [ghost, setGhost] = useState<{ x: number; y: number; w: number; h: number } | null>(null);

  const onNodeDragStart = useCallback((_event: MouseEvent, _node: Node, selectedNodes: Node[]) => {
    if (selectedNodes.length < 2) return; // only for multi-select
    const xs = selectedNodes.map((n) => n.position.x);
    const ys = selectedNodes.map((n) => n.position.y);
    setGhost({
      x: Math.min(...xs),
      y: Math.min(...ys),
      w: Math.max(...xs) - Math.min(...xs) + 200,
      h: Math.max(...ys) - Math.min(...ys) + 80,
    });
  }, []);

  const onNodeDrag = useCallback((_event: MouseEvent, node: Node, selectedNodes: Node[]) => {
    if (!ghost || selectedNodes.length < 2) return;
    // Update ghost position but DO NOT update actual nodes (stays frozen)
    const first = selectedNodes[0];
    if (first) setGhost((g) => g && { ...g, x: first.position.x, y: first.position.y });
  }, [ghost]);

  const onNodeDragStop = useCallback(
    (_event: MouseEvent, _node: Node, selectedNodes: Node[]) => {
      // Now apply the final positions to all selected nodes in one batch
      selectedNodes.forEach((n) =>
        useGraphStore.getState().updateNode(n.id, { position: n.position }, { isVisualOnly: false })
      );
      setGhost(null);
    },
    [],
  );

  return { ghost, onNodeDragStart, onNodeDrag, onNodeDragStop };
}
```

### GraphCanvas integration

```tsx
const { ghost, onNodeDragStart, onNodeDrag, onNodeDragStop } = useGhostDrag();

<ReactFlow
  ...
  onNodeDragStart={onNodeDragStart}
  onNodeDrag={onNodeDrag}
  onNodeDragStop={onNodeDragStop}
  selectionOnDrag
  selectionMode={SelectionMode.Partial}
>
  {ghost && (
    <div className="node-ghost" style={{ left: ghost.x, top: ghost.y, width: ghost.w, height: ghost.h }} />
  )}
</ReactFlow>
```

**Primary source:** [chaiNNer](https://github.com/chaiNNer/chaiNNer) — custom `SelectionBox`
component and the `onNodeDragStop` batch-update pattern for multi-node moves.
