# Piece: NodeShell (Registry-driven Node with Zoom Tiers)

**Source:** `node-editor` branch

---

## Where it goes

```
apps/review-workbench/src/features/graph-editor/L2-canvas/
  NodeShell.tsx
```

Registered as `nodeTypes.default` in `GraphCanvas.tsx`.

---

## What does it solve

Our current nodes (`EntryNode`, `SkillBallNode`, `RequirementNode`, `ProfileNode`) each
hardcode their own layout and are registered by name in domain-specific canvases. They
cannot be shared across CV, Match, or Knowledge Graph views.

`NodeShell` is a universal container that:

1. **Reads `typeId` from `data`** and asks the registry for the matching `NodeTypeDefinition`.
   The shell itself has zero knowledge of CV entries, skills, or requirements.

2. **Three zoom-level rendering tiers:**
   - `detail` (zoom ≥ 0.9×) — full `EntityCard` or custom `DetailRenderer` with all fields.
   - `label` (zoom ≥ 0.4×) — icon + title only, compact.
   - `dot` (zoom < 0.4×) — single colored circle. Very large graphs stay readable.
   The tier is recomputed from the live zoom via `useStore(zoomSelector)`.

3. **Context menu** (right-click) with Edit, Focus Neighborhood, Copy, Delete — wired
   to `ui-store` and `graph-store`. No domain-specific logic inside the menu.

4. **Category color override** — `data.category` maps to a color token for the border.
   If a `visualToken` is present it takes precedence. Falls back to the registry's
   `colorToken`.

5. **FallbackNode behaviour** — if `typeId` is not in the registry, the node renders a
   red debug card showing the unknown type and any `data.message` payload. Never crashes.

---

## How we have it implemented

Each canvas registers its own hardcoded node types:
- `CvGraphCanvas`: `{ entry: EntryNode, skill: SkillBallNode, group: GroupNode }`
- `MatchGraphCanvas` → `GraphCanvas`: `{ requirement: RequirementNode, profile: ProfileNode }`
- `KnowledgeGraph`: `{ default: ..., group: ... }` (inline anonymous components)

No zoom-level tiers exist. No context menu. No shared registry lookup. Unknown types
crash with a React error or silently show nothing.

---

## What will it affect (collateral modifications)

| File | Change needed |
|---|---|
| `schema/registry.ts` + `schema/register-defaults.ts` | Must be present — shell calls `registry.get(typeId)` |
| `GraphCanvas.tsx` (organism) | Replace hardcoded `nodeTypes` map with `{ default: NodeShell, group: GroupShell }` |
| `CvGraphCanvas.tsx` | Retire `EntryNode`, `SkillBallNode`; they become L3 renderers registered in the registry |
| `MatchGraphCanvas.tsx` | Retire `RequirementNode`, `ProfileNode`; same migration |
| `components/ui/context-menu.tsx` | Must be installed (shadcn) — see piece 10 |
| `stores/ui-store.ts` | Must be present — context menu calls `setFocusedNode`, `openDeleteConfirm`, etc. |

---

## Concrete code pieces + source

### Zoom tier resolver

```ts
const ZOOM_DETAIL = 0.9;
const ZOOM_LABEL  = 0.4;

export function getRenderTier(zoom: number): 'detail' | 'label' | 'dot' {
  if (zoom >= ZOOM_DETAIL) return 'detail';
  if (zoom >= ZOOM_LABEL)  return 'label';
  return 'dot';
}
```

### Shell skeleton

```tsx
export const NodeShell = memo(function NodeShell({ id, data, selected }: NodeProps<CanvasNode>) {
  const zoom = useStore((s) => s.transform[2]); // live zoom from ReactFlow internal store

  const typeId = (data as Record<string,unknown>).typeId as string | undefined;
  const definition = registry.get(typeId ?? '') ?? registry.get('entity');

  // unknown type → debug card
  if (!definition) return <UnknownNodeCard typeId={typeId} data={data} />;

  const tier = getRenderTier(zoom);
  const Renderer = definition.renderers[tier];

  return (
    <ContextMenu>
      <ContextMenuTrigger>
        <div className={`rounded-lg border-2 bg-card ${selected ? 'ring-2 ring-primary/40' : ''}`}
             style={{ borderColor: definition.colorToken, minWidth: definition.defaultSize.width }}>
          <Handle type="target" position={Position.Top} />
          <Renderer {...payloadProps} />
          <Handle type="source" position={Position.Bottom} />
        </div>
      </ContextMenuTrigger>
      <ContextMenuContent>
        <ContextMenuItem onClick={handleEdit}>Edit <ContextMenuShortcut>Enter</ContextMenuShortcut></ContextMenuItem>
        <ContextMenuItem onClick={handleFocusNeighborhood}>Focus Neighborhood</ContextMenuItem>
        <ContextMenuSeparator />
        <ContextMenuItem onClick={handleDelete}>Delete <ContextMenuShortcut>Del</ContextMenuShortcut></ContextMenuItem>
      </ContextMenuContent>
    </ContextMenu>
  );
});
```

**Full source:** `node-editor:apps/review-workbench/src/features/graph-editor/L2-canvas/NodeShell.tsx`
