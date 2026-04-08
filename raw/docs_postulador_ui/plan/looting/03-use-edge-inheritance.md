# Piece: use-edge-inheritance (Group Collapse/Expand)

**Source:** `node-editor` branch

---

## Where it goes

```
apps/review-workbench/src/features/graph-editor/L2-canvas/hooks/
  use-edge-inheritance.ts
```

---

## What does it solve

Our D2 collapse/expand hides child nodes using `node.hidden` but leaves edges dangling —
they still reference hidden nodes as source/target, so ReactFlow either renders broken
arrows or simply drops them. The group appears collapsed visually but the graph is
structurally broken.

`use-edge-inheritance` solves this by re-routing edges when a group collapses:

- Child nodes → `hidden: true` (visual only, no undo entry).
- Any edge whose source or target is a child gets its endpoint moved to the group node,
  its `relationType` set to `'inherited'`, and the original endpoints stored in
  `_originalSource` / `_originalTarget` so expand can restore them exactly.
- Self-edges (both endpoints map to the same group) are silently dropped.

On expand: all child nodes become visible again, edges restore their original
source/target and `relationType`. The group node's `data.properties.__collapsed`
flag is toggled to drive the toolbar button state.

All mutations go through `updateNode` / `updateEdge` with `isVisualOnly: true`,
so the entire collapse/expand cycle leaves the undo stack clean.

---

## How we have it implemented

`KnowledgeGraph.tsx` tracks `expandedGroups: Set<string>` in local state and
recomputes the full node/edge array on every toggle via `useMemo`. Edges are
not re-routed — they simply disappear when child nodes are hidden because ReactFlow
cannot resolve their endpoints.

`GroupNode.tsx` (D2) calls `onToggle` which flips the Set; the parent re-renders
the entire canvas. No edge re-routing, no inherited styling, undo stack not involved.

---

## What will it affect (collateral modifications)

| File | Change needed |
|---|---|
| `L2-canvas/GroupShell.tsx` | Call `collapseGroup` / `expandGroup` from this hook instead of local toggle |
| `stores/graph-store.ts` | Must be present — hook reads `nodes`, `edges`, `updateNode`, `updateEdge` from it |
| `edges/FloatingEdge.tsx` | Must be present — `inherited` relationType triggers dashed style |
| `KnowledgeGraph.tsx` | Remove `expandedGroups` Set + collapse useMemo; delete manual hide logic |
| `features/base-cv/components/GroupNode.tsx` | Remove local toggle state; delegate to hook via GroupShell |

---

## Concrete code pieces + source

### Core API

```ts
export function useEdgeInheritance(): {
  collapseGroup: (groupId: string) => void;
  expandGroup:   (groupId: string) => void;
}
```

### Collapse logic (simplified)

```ts
export function collapseGroupEdges(groupId: string, state: EdgeInheritanceState): void {
  const childIds = new Set(
    state.nodes.filter((n) => n.parentId === groupId).map((n) => n.id)
  );

  // 1. hide children
  childIds.forEach((id) => state.updateNode(id, { hidden: true }, { isVisualOnly: true }));

  // 2. re-route edges
  state.edges
    .filter((e) => childIds.has(e.source) || childIds.has(e.target))
    .forEach((e) => {
      const nextSource = childIds.has(e.source) ? groupId : e.source;
      const nextTarget = childIds.has(e.target) ? groupId : e.target;
      if (nextSource === nextTarget) return; // drop self-edges

      state.updateEdge(e.id, {
        source: nextSource,
        target: nextTarget,
        data: {
          relationType: 'inherited',
          properties: e.data?.properties ?? {},
          _originalSource: e.source,
          _originalTarget: e.target,
          _originalRelationType: e.data?.relationType ?? 'linked',
        },
      }, { isVisualOnly: true });
    });

  // 3. mark group as collapsed
  state.updateNode(groupId, {
    data: { ...groupNode.data, properties: { ...groupNode.data.properties, __collapsed: 'true' } }
  }, { isVisualOnly: true });
}
```

**Full source:** `node-editor:apps/review-workbench/src/features/graph-editor/L2-canvas/hooks/use-edge-inheritance.ts`
