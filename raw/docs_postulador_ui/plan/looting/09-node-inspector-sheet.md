# Piece: NodeInspector Sheet (Side Panel Node Editor)

**Source:** `node-editor` branch

---

## Where it goes

```
apps/review-workbench/src/features/graph-editor/L2-canvas/panels/
  NodeInspector.tsx
  EdgeInspector.tsx     ← companion for edge editing
```

---

## What does it solve

Our current `NodeInspector.tsx` (in `features/base-cv/components/`) is a plain div that
renders inline beside the canvas. It is tightly coupled to CV domain types: it receives
`entries`, `skills`, and typed callbacks (`onEntryChange`, `onSkillChange`, etc.).

Problems:
- Cannot be reused for Match or Knowledge Graph nodes.
- Has no animation or accessible close behaviour.
- The inspector re-renders with the whole canvas when any node changes.

The node-editor `NodeInspector` uses a **shadcn `Sheet`** (slide-over panel) that:

1. Opens/closes driven by `ui-store.focusedNodeId` — no prop threading needed.
2. Reads the focused node from `graph-store` by ID.
3. Uses a local `draft` state for the edit form, only writing back to the store on Save.
4. Is format-agnostic: reads `data.label` / `data.name` / `data.properties` regardless
   of whether the node came from a CV, match graph, or schema explorer.
5. Supports a key-value `PropertyEditor` for arbitrary `properties` entries.

---

## How we have it implemented

`features/base-cv/components/NodeInspector.tsx:1` — inline div, CV-specific props,
no Sheet, no `draft` pattern.

No inspector exists for MatchGraphCanvas or KnowledgeGraph — clicking a node shows
inline highlighted state only.

---

## What will it affect (collateral modifications)

| File | Change needed |
|---|---|
| `components/ui/sheet.tsx` | Must be installed (shadcn) — see piece 10 |
| `stores/ui-store.ts` | Must be present — inspector reads `focusedNodeId`, calls `setFocusedNode` |
| `stores/graph-store.ts` | Must be present — inspector reads `nodes`, calls `updateNode` |
| `BaseCvEditor.tsx` | Remove inspector props; inspector self-subscribes via store |
| `features/base-cv/components/NodeInspector.tsx` | Retire or repurpose as a CV-specific L3 renderer |
| `Match.tsx` | Remove manual selected-node state; inspector handles it via store |

---

## Concrete code pieces + source

### Panel structure

```tsx
export function NodeInspector() {
  const focusedNodeId = useUIStore((s) => s.focusedNodeId);
  const setFocusedNode = useUIStore((s) => s.setFocusedNode);
  const setEditorState = useUIStore((s) => s.setEditorState);
  const nodes = useGraphStore((s) => s.nodes);
  const updateNode = useGraphStore((s) => s.updateNode);

  const node = nodes.find((n) => n.id === focusedNodeId) ?? null;
  const [draft, setDraft] = useState<{ title: string; properties: Record<string,string> } | null>(null);

  useEffect(() => {
    if (!node) { setDraft(null); return; }
    setDraft({ title: getNodeTitle(node.data), properties: node.data.properties ?? {} });
  }, [node]);

  const handleClose = () => { setFocusedNode(null); setEditorState('browse'); };
  const handleSave = () => {
    if (!node || !draft) return;
    updateNode(node.id, { data: { ...node.data, label: draft.title, properties: draft.properties } });
    handleClose();
  };

  return (
    <Sheet open={Boolean(focusedNodeId)} onOpenChange={(open) => !open && handleClose()}>
      <SheetContent side="right" className="w-[400px]">
        <SheetHeader>
          <SheetTitle>Edit Node</SheetTitle>
        </SheetHeader>
        {draft && (
          <>
            <Input value={draft.title} onChange={(e) => setDraft({ ...draft, title: e.target.value })} />
            <PropertyEditor
              pairs={pairsFromRecord(draft.properties)}
              onChange={(pairs) => setDraft({ ...draft, properties: recordFromPairs(pairs) })}
            />
            <Button onClick={handleSave}>Save</Button>
          </>
        )}
      </SheetContent>
    </Sheet>
  );
}
```

**Full source:** `node-editor:apps/review-workbench/src/features/graph-editor/L2-canvas/panels/NodeInspector.tsx`
