# Piece: FallbackNode (Unknown typeId Debug Card)

**Source:** `node-editor` branch (`NodeShell.tsx`) + agentok pattern

---

## Where it goes

```
apps/review-workbench/src/features/graph-editor/L2-canvas/
  NodeShell.tsx       ← inline unknown-node branch (already in NodeShell, extract if needed)
```

Or as a standalone component if reused outside the shell:

```
apps/review-workbench/src/components/content/
  FallbackNode.tsx    ← optional extraction
```

---

## What does it solve

Currently, if a node's `type` is not in the `nodeTypes` map passed to `<ReactFlow>`,
ReactFlow logs a warning and renders nothing (blank space). If `CvGraphCanvas` receives
a node with an unexpected `category`, it silently shows an empty box.

The FallbackNode rule from the manual de vuelo: **unknown typeId → debug card, never a
crash, never blank**. The debug card:

1. Shows the raw `typeId` string so developers immediately know what's missing.
2. Dumps `data.message` if present (for error nodes produced by the translator's error
   path).
3. Renders with a red border so it's visually unmistakable in development.
4. Still has source/target handles so it doesn't break edge connectivity.

This makes development feedback immediate instead of silent. In production, the same
card can render with a neutral style and a "Unknown node" label.

---

## How we have it implemented

No fallback exists. Unknown node types in `CvGraphCanvas` fall through to a ReactFlow
warning. Unknown types in `MatchGraphCanvas` are simply never rendered — if
`n.kind !== 'requirement'` the node gets `type: 'profile'` regardless.

---

## What will it affect (collateral modifications)

| File | Change needed |
|---|---|
| `NodeShell.tsx` | Replace the current `if (!definition) return null` with the FallbackNode card |
| `schema/registry.ts` | `registry.get()` returning `undefined` is the trigger — no change needed |
| `schema-to-graph.ts` | Error path should produce a node with `typeId: 'error'` and `data.message` |

---

## Concrete code pieces + source

### Inline unknown-node branch from NodeShell (node-editor)

```tsx
if (!definition) {
  const message = getUnknownMessage(data); // reads data.message or data.payload.value.message
  return (
    <ContextMenu>
      <ContextMenuTrigger>
        <div className="min-w-[150px] rounded-lg border-2 border-red-500 bg-red-50 p-2">
          <span className="text-xs text-red-600">Unknown: {typeId ?? 'unknown'}</span>
          {message && <p className="text-[10px] text-red-400">{message}</p>}
          <Handle type="target" position={Position.Top} />
          <Handle type="source" position={Position.Bottom} />
        </div>
      </ContextMenuTrigger>
      <ContextMenuContent>
        <ContextMenuItem onClick={handleEdit}>Edit</ContextMenuItem>
        <ContextMenuItem onClick={handleDelete}>Delete</ContextMenuItem>
      </ContextMenuContent>
    </ContextMenu>
  );
}
```

### Helper

```ts
export function getUnknownMessage(data: ASTNode['data']): string | null {
  const asJson = data as Record<string, unknown>;
  if (typeof asJson.message === 'string' && asJson.message.trim()) return asJson.message;
  const payload = asJson.payload as { value?: Record<string,unknown> } | undefined;
  const msg = payload?.value?.message;
  return typeof msg === 'string' && msg.trim() ? msg : null;
}
```

**Full source:** `node-editor:apps/review-workbench/src/features/graph-editor/L2-canvas/NodeShell.tsx`
(unknown-node branch, lines ~115–140)

**External reference:** agentok `frontend/src/nodes/index.ts` — same principle: any
unregistered typeId gets a visible error placeholder, not a silent blank.
