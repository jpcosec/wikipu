# Piece: GraphEditor Shell (L2 Aesthetic Container)

**Source:** `node-editor` branch (`GraphEditor.tsx` + `CanvasSidebar`)

---

## Where it goes

```
apps/review-workbench/src/features/graph-editor/L2-canvas/
  GraphEditor.tsx         ← canvas + sidebar + panels + toasts
  sidebar/
    CanvasSidebar.tsx
    ActionsSection.tsx
    CreationSection.tsx
    FiltersSection.tsx
    ViewSection.tsx
```

---

## What does it solve

Our canvases (`CvGraphCanvas`, `MatchGraphCanvas`) are raw ReactFlow wrappers with no
chrome around them. Controls, sidebars, and panels are ad-hoc arrangements per page.
The `GraphEditor` shell provides a polished, reusable L2 frame that:

1. **Aesthetic wrapper** — rounded canvas with a glass-panel header overlay, radial
   gradient background, and a consistent dark theme that matches the Terran Command
   design system. Not just functional — it looks like a professional tool.

2. **Sidebar** (`CanvasSidebar`) — collapsible right rail with four accordion sections:
   - `ActionsSection` — Save, Undo, Redo buttons wired to the store.
   - `CreationSection` — Add node by typeId (uses the registry to populate options).
   - `FiltersSection` — Hide relation types, filter by text or attribute value.
   - `ViewSection` — Toggle MiniMap, re-layout button, direction selector.

3. **Panels** — `NodeInspector` + `EdgeInspector` mounted at the L2 level; they
   self-open via store subscription, no prop wiring from the page.

4. **`DeleteConfirm` dialog** — wired to `ui-store.deleteConfirmOpen`; fires
   `executePendingDelete` on confirm.

5. **`CommandMenu`** — Ctrl+K palette for quick actions (add node, save, layout).
   Driven by `ui-store.commandDialogOpen`.

6. **`Toaster`** (sonner) — toast notifications for save, delete, etc.

7. **`useKeyboard()`** mounted here — single location for all canvas shortcuts.

---

## How we have it implemented

No equivalent shell exists. Each page (`BaseCvEditor`, `Match`) composes its own layout
with `SplitPane` or flex divs. Controls are scattered across `ControlPanel` molecules,
page-level state, and feature-specific toolbars.

The closest thing is `GraphCanvas.tsx` (organism), which wraps ReactFlow with
`Background`, `Controls`, `MiniMap` — but no sidebar, no panels, no command menu.

---

## What will it affect (collateral modifications)

| File | Change needed |
|---|---|
| All pieces 01–09 | Must be present — this shell wires them together |
| `pages/global/BaseCvEditor.tsx` | Render `<GraphEditor>` instead of manual canvas + panel layout |
| `pages/job/Match.tsx` | Same |
| `pages/global/KnowledgeGraph.tsx` | Can be replaced entirely by `GraphEditor` |
| `components/ui/` (sonner, command, dialog, tabs, accordion, scroll-area) | Must be installed — see piece 10 |

---

## Concrete code pieces + source

### GraphEditor composition

```tsx
export function GraphEditor({ initialNodes, initialEdges, onSave }: GraphEditorProps) {
  useKeyboard();  // shortcut handler

  return (
    <div className="flex h-screen w-full overflow-hidden px-4 pb-4 pt-4">
      {/* Canvas area */}
      <div className="relative flex-1 overflow-hidden rounded-[2rem] border border-white/8
                      shadow-[0_30px_90px_rgba(0,0,0,0.28)]">

        {/* Glass header overlay — purely aesthetic */}
        <div className="pointer-events-none absolute inset-x-0 top-0 z-10 flex justify-between px-6 py-5">
          <div className="glass-panel max-w-md rounded-2xl px-4 py-3">
            <p className="font-mono text-[11px] uppercase tracking-[0.32em] text-primary">Graph Studio</p>
            <h1 className="mt-2 font-headline text-2xl font-bold text-on-surface">...</h1>
          </div>
        </div>

        {/* Radial glow background */}
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_top,rgba(0,242,255,0.08),
                        transparent_26%),radial-gradient(circle_at_bottom_left,
                        rgba(255,170,0,0.08),transparent_24%)]" />

        <div className="relative h-full">
          <GraphCanvas />   {/* pure ReactFlow layer */}
        </div>
      </div>

      {/* Right sidebar */}
      <CanvasSidebar onSave={onSave} />

      {/* Self-subscribing panels */}
      <NodeInspector />
      <EdgeInspector />

      {/* Dialogs */}
      <DeleteConfirm ... />
      <CommandMenu ... />
      <Toaster />
    </div>
  );
}
```

### CanvasSidebar sections

```tsx
// Four accordion items, each section is a separate file
<Accordion type="multiple" defaultValue={['actions', 'view']}>
  <ActionsSection onSave={onSave} />     {/* save / undo / redo */}
  <CreationSection />                     {/* add node by typeId */}
  <FiltersSection />                      {/* hide types, text filter */}
  <ViewSection />                         {/* minimap, re-layout, direction */}
</Accordion>
```

**Full source:** `node-editor:apps/review-workbench/src/features/graph-editor/L2-canvas/GraphEditor.tsx`
`node-editor:apps/review-workbench/src/features/graph-editor/L2-canvas/sidebar/`
