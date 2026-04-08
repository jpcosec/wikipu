# Piece: Parent-Child Hierarchy (parentNode + extent: 'parent')

**Source:** chaiNNer — `chaiNNer/src/util/graph-util.ts`
**Secondary:** ReactFlow Expand/Collapse official example

---

## Where it goes

Logic is split across two files:

```
apps/review-workbench/src/features/graph-editor/lib/
  domain-graph.types.ts    ← DomainEntity.parentId field (already in piece 11)
  schema-to-graph.ts       ← sets parentNode + extent + relative coordinates

apps/review-workbench/src/features/graph-editor/L2-canvas/hooks/
  use-expand-collapse.ts   ← hide/show descendant nodes + edges recursively
```

---

## What does it solve

We currently compute group membership manually in `CvGraphCanvas` via a `byCategory`
map and position child nodes with absolute coordinates relative to an assumed group
origin. When groups move, children don't follow. When groups collapse, children stay
in the DOM.

ReactFlow's native parent-child system solves this cleanly:
- Set `parentNode: groupId` on a child → it moves with the parent automatically.
- Set `extent: 'parent'` → the child cannot be dragged outside its parent boundary.
- Positions become **relative** to the parent's top-left corner, not the canvas origin.

The chaiNNer pattern adds the piece ReactFlow doesn't give you: recursive
collapse/expand that hides all **descendants** (not just direct children) and all
edges that touch any of them. This is different from `use-edge-inheritance` (piece 03),
which re-routes edges to the group boundary. These two can coexist:
- `use-edge-inheritance` → for single-level group collapse (re-routes edges to parent).
- `use-expand-collapse` → for document hierarchies with multiple nesting levels (hides
  entire subtrees).

---

## How we have it implemented

`CvGraphCanvas.tsx` — group nodes use `extent: 'parent'` and `parentId` in the node
data, but only at the top level (section → entries). There is no recursive collapse.
Child positions are baked as absolute coordinates in `cvToGraph.ts` with manual offsets
(`SECTION_PADDING`, `ITEM_HEIGHT`, etc.). If the section moves, children do not follow
because positions are absolute.

`KnowledgeGraph.tsx` — no parent-child at all; groups are styled divs inside a
`subflows`-style arrangement, not native ReactFlow parent nodes.

---

## What will it affect (collateral modifications)

| File | Change needed |
|---|---|
| `schema-to-graph.ts` / `cvToGraph.ts` | When entity has `parentId`: set `parentNode`, convert absolute → relative position |
| `use-graph-layout.ts` (piece 08) | Dagre must be configured for compound graphs (`dagreGraph.setGraph({ compound: true })`) when parent-child nodes are present |
| `GroupShell.tsx` (piece 05) | Call `expandDescendants` / `collapseDescendants` instead of single-level collapse |
| `stores/graph-store.ts` | `updateNode` with `isVisualOnly: true` is sufficient — no store changes needed |

---

## Concrete code pieces + source

### Translator: set parentNode + relative coordinates

```ts
// In schema-to-graph.ts, when building ASTNode from DomainEntity:
if (entity.parentId) {
  const parent = entityMap.get(entity.parentId);
  const parentOrigin = parent?.position ?? { x: 0, y: 0 };

  node.parentNode = entity.parentId;   // ReactFlow native parent-child
  node.extent = 'parent';             // child cannot leave parent bounds
  node.position = {                   // relative to parent origin
    x: entity.position.x - parentOrigin.x,
    y: entity.position.y - parentOrigin.y,
  };
}
```

### Recursive expand/collapse hook (chaiNNer pattern)

```ts
// use-expand-collapse.ts
export function useExpandCollapse() {
  const nodes = useGraphStore((s) => s.nodes);
  const edges = useGraphStore((s) => s.edges);
  const updateNode = useGraphStore((s) => s.updateNode);
  const updateEdge = useGraphStore((s) => s.updateEdge);

  function getDescendantIds(groupId: string): string[] {
    const direct = nodes.filter((n) => n.parentNode === groupId).map((n) => n.id);
    return [...direct, ...direct.flatMap((id) => getDescendantIds(id))];
  }

  const collapse = useCallback((groupId: string) => {
    const descendantIds = new Set(getDescendantIds(groupId));
    descendantIds.forEach((id) =>
      updateNode(id, { hidden: true }, { isVisualOnly: true })
    );
    edges
      .filter((e) => descendantIds.has(e.source) || descendantIds.has(e.target))
      .forEach((e) => updateEdge(e.id, { hidden: true }, { isVisualOnly: true }));
  }, [nodes, edges, updateNode, updateEdge]);

  const expand = useCallback((groupId: string) => {
    // Only reveal direct children — their own collapsed state governs deeper levels
    nodes
      .filter((n) => n.parentNode === groupId)
      .forEach((n) => updateNode(n.id, { hidden: false }, { isVisualOnly: true }));
  }, [nodes, updateNode]);

  return { collapse, expand };
}
```

### Compound graph layout (Dagre config)

```ts
// In use-graph-layout.ts, when parent-child nodes are present:
dagreGraph.setGraph({
  rankdir: direction,
  compound: true,          // ← enables compound graph mode in Dagre
  nodesep: 50,
  ranksep: 100,
});

// Register parent-child relationships
nodes.forEach((n) => {
  if (n.parentNode) dagreGraph.setParent(n.id, n.parentNode);
});
```

**Primary source:** `chaiNNer/src/util/graph-util.ts`
— relative coordinate calculation and recursive subtree hiding.

**Secondary source:** [ReactFlow Expand/Collapse example](https://reactflow.dev/examples/layout/expand-collapse)
— official pattern for hiding descendant nodes and their connecting edges.
