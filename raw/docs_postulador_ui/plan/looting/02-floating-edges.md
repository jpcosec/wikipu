# Piece: Floating Edges (FloatingEdge + ButtonEdge + edge-helpers)

**Source:** `node-editor` branch

---

## Where it goes

```
apps/review-workbench/src/features/graph-editor/L2-canvas/edges/
  edge-helpers.ts     ← geometry utilities
  FloatingEdge.tsx    ← base floating edge
  ButtonEdge.tsx      ← floating edge + hover delete button
  index.ts
```

---

## What does it solve

Our current edges use fixed `Handle` positions (`Position.Top` / `Position.Bottom`).
When nodes are arranged horizontally, the edges still exit from the top/bottom, creating
diagonal crossing lines that are hard to read.

`FloatingEdge` computes the attachment point geometrically: it finds where the bezier
from center-to-center intersects the node boundary, giving the shortest clean path
regardless of layout direction.

Bonus: edges with `relationType === 'inherited'` (produced by group collapse) render
dashed and semi-transparent automatically — no extra code needed at the collapse site.

`ButtonEdge` extends FloatingEdge with a `×` button that appears on hover/selection,
wired to `graph-store.removeElements`. Transparent wide hit-target (`strokeWidth={24}`)
makes the edge easy to click.

---

## How we have it implemented

- `ProxyEdge.tsx` (CvGraphCanvas) — custom bezier that manually offsets for proxy nodes.
  Does not adapt to layout direction.
- `EdgeScoreBadge.tsx` (MatchGraphCanvas) — label-only edge, fixed `Position.Top` handles.
- `GraphCanvas.tsx` (organism) — passes `edgeTypes` prop but uses ReactFlow default edges.

None have floating geometry or a delete affordance.

---

## What will it affect (collateral modifications)

| File | Change needed |
|---|---|
| `CvGraphCanvas.tsx` | Replace `ProxyEdge` with `FloatingEdge`; proxy routing logic no longer needed |
| `MatchGraphCanvas.tsx` / `GraphCanvas.tsx` | Register `FloatingEdge` / `ButtonEdge` as edge types |
| `features/base-cv/lib/cvToGraph.ts` | Edges no longer need `type: 'proxy'`; use `type: 'floating'` |
| `features/job-pipeline/lib/matchToGraph.ts` | Same |
| `styles.css` | Remove any `.react-flow__edge` overrides that assume fixed handle positions |

---

## Concrete code pieces + source

### `edge-helpers.ts` — intersection geometry

```ts
// Finds where the line from source center to target center exits the source boundary.
// Returns { sx, sy, tx, ty, sourcePosition, targetPosition } for getBezierPath().
export function getEdgeParams(source: NodeBounds, target: NodeBounds): EdgeParams { ... }
```

### `FloatingEdge.tsx` — auto-attach + inherited styling

```tsx
export const FloatingEdge = memo(function FloatingEdge({ id, source, target, style, markerEnd, data }) {
  const sourceNode = useStore((s) => s.nodeLookup.get(source));
  const targetNode = useStore((s) => s.nodeLookup.get(target));

  const relationType = data?.relationType;
  const params = getEdgeParams(sourceNode, targetNode);
  const [path, labelX, labelY] = getBezierPath({ ...params });

  const isInherited = relationType === 'inherited';
  const edgeStyle = isInherited
    ? { ...style, strokeDasharray: '3 4', opacity: 0.5 }
    : style;

  return (
    <>
      <BaseEdge id={id} path={path} style={edgeStyle} markerEnd={isInherited ? undefined : markerEnd} />
      <EdgeLabelRenderer>
        {/* relation type label — visible on hover */}
        <div style={{ transform: `translate(-50%,-50%) translate(${labelX}px,${labelY}px)` }}
             className="opacity-0 hover:opacity-100 text-[10px] ...">
          {relationType || 'linked'}
        </div>
      </EdgeLabelRenderer>
    </>
  );
});
```

### `ButtonEdge.tsx` — delete affordance

```tsx
export const ButtonEdge = memo(function ButtonEdge({ id, source, target, selected, data, ...rest }) {
  const removeElements = useGraphStore((s) => s.removeElements);
  // wide transparent hit zone
  return (
    <>
      <FloatingEdge id={id} source={source} target={target} data={data} {...rest} />
      <path d={edgePath} fill="none" stroke="transparent" strokeWidth={24} pointerEvents="stroke"
            onMouseEnter={() => setIsEdgeHovered(true)} onMouseLeave={() => setIsEdgeHovered(false)} />
      <EdgeLabelRenderer>
        <button onClick={() => removeElements([], [id])}
                className={showButton ? 'h-5 w-5 rounded border ...' : 'hidden'}>
          x
        </button>
      </EdgeLabelRenderer>
    </>
  );
});
```

**Full source:** `node-editor:apps/review-workbench/src/features/graph-editor/L2-canvas/edges/`
