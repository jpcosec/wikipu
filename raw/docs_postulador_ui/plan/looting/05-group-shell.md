# Piece: GroupShell (Group Node Component)

**Source:** `node-editor` branch

---

## Where it goes

```
apps/review-workbench/src/features/graph-editor/L2-canvas/
  GroupShell.tsx
```

Registered as `nodeTypes.group` in `GraphCanvas.tsx`.

---

## What does it solve

Our current `GroupNode.tsx` (in `features/base-cv/components/`) is tightly coupled to
`CvGraphCanvas`: it receives CV-specific props, uses `onToggleGroup` callbacks, and has
no resize support. It cannot be reused for Match or the Knowledge Graph.

`GroupShell` solves this with three improvements:

1. **`NodeToolbar`** — the collapse/expand button floats above the node boundary using
   ReactFlow's native `NodeToolbar`, so it never clips inside the group rectangle and
   works at any zoom level.

2. **`NodeResizer`** — lets the user drag-resize the group. Resizer only appears when
   the node is selected *and* not collapsed, preventing accidental resizes.

3. **Handles conditional on collapse state** — when collapsed, source/target handles
   are hidden entirely; the edge re-routing hook (`use-edge-inheritance`) takes over
   and attaches edges directly to the group boundary via the floating edge geometry.

The group reads its title from `data.label` (direct JSON format) or
`data.payload.value.name` (AST format), making it format-agnostic.

---

## How we have it implemented

`features/base-cv/components/GroupNode.tsx` — hardcoded to CV domain:
- Receives `onToggle`, `onSelectGroup`, `onAddEntry` as callbacks from `CvGraphCanvas`.
- No `NodeResizer`, no `NodeToolbar`.
- Collapse state is a `Set<string>` in the parent canvas.
- Handles are always visible regardless of collapse state.

`KnowledgeGraph.tsx` uses `GroupNode` from `pages/global/KnowledgeGraph.tsx` which is
a different component — inline, also not resizable and not using NodeToolbar.

---

## What will it affect (collateral modifications)

| File | Change needed |
|---|---|
| `features/graph-editor/L2-canvas/GraphCanvas.tsx` | Register `GroupShell` as `nodeTypes.group` |
| `hooks/use-edge-inheritance.ts` | Must be present — `GroupShell` calls `collapseGroup` / `expandGroup` from this hook |
| `stores/graph-store.ts` | Must be present — hook needs `updateNode` / `updateEdge` |
| `CvGraphCanvas.tsx` | Stop passing `onToggleGroup`; collapse state moves to the store |
| `features/base-cv/components/GroupNode.tsx` | Can be retired once `GroupShell` covers the CV use case |

---

## Concrete code pieces + source

```tsx
export const GroupShell = memo(function GroupShell({ id, data, selected }) {
  const { collapseGroup, expandGroup } = useEdgeInheritance();
  const collapsed = isCollapsed(data); // reads data.properties.__collapsed

  const toggleCollapse = () => collapsed ? expandGroup(id) : collapseGroup(id);

  return (
    <>
      {/* Toolbar floats above the node — always visible */}
      <NodeToolbar position={Position.Top} align="start" isVisible>
        <div className="flex items-center gap-2 rounded border bg-background px-2 py-1 text-xs">
          <button onClick={toggleCollapse} className="hover:text-primary">
            {collapsed ? 'Expand' : 'Collapse'}
          </button>
          <span className="font-semibold">{getGroupTitle(data)}</span>
        </div>
      </NodeToolbar>

      <div className="h-full w-full rounded-lg border-2 border-dashed bg-transparent"
           style={{ borderColor }}>
        {/* Resizer only when selected and expanded */}
        <NodeResizer isVisible={selected && !collapsed} minWidth={160} minHeight={60} />

        {/* Handles only when not collapsed */}
        {!collapsed && (
          <>
            <Handle type="target" position={Position.Top} />
            <Handle type="source" position={Position.Bottom} />
          </>
        )}
      </div>
    </>
  );
});
```

### Helper: reading collapse state (format-agnostic)

```ts
export function isCollapsed(data: ASTNode['data']): boolean {
  // AST format: data.properties.__collapsed === 'true'
  const props = (data as Record<string, unknown>).properties as Record<string, string> | undefined;
  if (props && '__collapsed' in props) return props['__collapsed'] === 'true';
  // Direct JSON format: data.collapsed === true
  if ('collapsed' in (data as object)) return Boolean((data as Record<string,unknown>).collapsed);
  return false;
}
```

**Full source:** `node-editor:apps/review-workbench/src/features/graph-editor/L2-canvas/GroupShell.tsx`
