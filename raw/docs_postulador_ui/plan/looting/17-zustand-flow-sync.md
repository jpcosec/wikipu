# Piece: Shadow State Mirror (Zustand ↔ ReactFlow Sync)

**Source:** ameliorate — `ameliorate/src/store/useStore.ts` (nodes sync section)

---

## Where it goes

```
apps/review-workbench/src/stores/
  graph-store.ts       ← sync logic lives here (already piece 01, this extends it)
```

---

## What does it solve

ReactFlow maintains its own internal state for node positions, selection, and measured
dimensions. Zustand maintains the source-of-truth for graph data. If the two diverge,
two failure modes appear:

1. **Position loss on save** — the user drags nodes around, ReactFlow updates its
   internal positions, but Zustand never hears about it. On save, the persisted JSON
   has the original positions from `loadGraph()`, not the user's current layout.

2. **Duplicate creation** — if the translator is re-run after a save/load cycle while
   ReactFlow's internal cache still has the old nodes, ReactFlow merges them incorrectly
   and nodes appear duplicated or with stale data.

The fix is a deliberate sync discipline:

- **Position changes** (`onNodesChange` type `'position'`) → write to Zustand via
  `updateNode(..., { isVisualOnly: true })` only when dragging stops (not during drag).
  During drag, ReactFlow's internal state leads; Zustand follows on `dragging: false`.
- **Data changes** (rename, property edit) → always write to Zustand first, let
  `useEffect` propagate to the `nodesState` array fed to ReactFlow.
- **Never** let ReactFlow's `applyNodeChanges` mutate the Zustand store for visual-only
  changes (selection, measurement); those stay in ReactFlow internal state only.

This is already partially implemented in `graph-store.ts` (piece 01) via `isVisualOnly`.
This piece documents the missing detail: the **drag-end** sync trigger.

---

## How we have it implemented

`CvGraphCanvas.tsx` uses `useNodesState` — ReactFlow owns positions completely.
On save, positions are read from `useNodesState` via a callback. This works for
CvGraphCanvas because it never persists to an external store. But when Zustand is
introduced (piece 01), the sync contract must be explicit or positions will be lost.

---

## What will it affect (collateral modifications)

| File | Change needed |
|---|---|
| `stores/graph-store.ts` | `onNodesChange` must write position to store only on `dragging === false` |
| `GraphCanvas.tsx` | Pass `onNodeDragStop` callback that calls `updateNode` with final position |
| `BaseCvEditor.tsx` / `Match.tsx` | `onSave` reads from `graph-store`, not from `useNodesState` |
| `api/client.ts` (save endpoints) | Persist `graph-store` snapshot, not ReactFlow state |

---

## Concrete code pieces + source

### Drag-end sync in `graph-store.onNodesChange`

```ts
onNodesChange: (changes: NodeChange[]) => {
  for (const change of changes) {
    if (change.type === 'position' && change.position) {
      // During drag: visual-only (ReactFlow leads)
      // On drag end (dragging === false): persist to undo-safe store
      const isVisualOnly = change.dragging === true;
      get().updateNode(change.id, { position: change.position }, { isVisualOnly });
    }
    if (change.type === 'select') {
      // Selection is always visual-only — never enters undo stack
      get().updateNode(change.id, { selected: change.selected }, { isVisualOnly: true });
    }
  }
},
```

### ReactFlow → Zustand data effect (prevent stale render)

```ts
// In GraphCanvas.tsx: keep ReactFlow's nodesState in sync with store
const storeNodes = useGraphStore((s) => s.nodes);

useEffect(() => {
  setNodesState(storeNodes.map(asCanvasNode));
}, [storeNodes]);
// Note: position changes from drag go store → effect → ReactFlow,
// creating a loop. This is prevented because drag updates are isVisualOnly
// and don't change storeNodes until drag ends.
```

**Primary source:** `ameliorate/src/store/useStore.ts`
— the `nodes` sync section separates positional updates (ReactFlow owns during drag)
from data updates (Zustand owns always).

**Pattern also in:** node-editor `graph-store.ts` (piece 01), `onNodesChange` handler.
The ameliorate reference adds the `dragging` flag discipline.
