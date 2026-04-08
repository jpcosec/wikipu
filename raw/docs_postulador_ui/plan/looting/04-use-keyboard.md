# Piece: use-keyboard (Keyboard Shortcut Handler)

**Source:** `node-editor` branch

---

## Where it goes

```
apps/review-workbench/src/features/graph-editor/L2-canvas/hooks/
  use-keyboard.ts
```

Mounted once inside `GraphEditor` (L2 root), no props needed.

---

## What does it solve

None of our current graph canvases have keyboard shortcuts. Users cannot undo, redo,
enter edit mode, or exit it without clicking UI controls. The hook centralises all
canvas-level keyboard behaviour with two important guards:

1. **Editable target guard** — `isEditableTarget()` checks if the event target is an
   `input`, `textarea`, `select`, or `contenteditable`. If so, the hook does nothing,
   so users can type inside node forms without triggering shortcuts.

2. **Editor state awareness** — shortcuts only fire when the current `editorState`
   makes them meaningful (e.g. Enter only opens edit mode when a node is focused in
   `'browse'` state; Escape only exits when in `'edit_node'` or `'edit_relation'`).

The command resolution is a pure function (`resolveKeyboardCommand`) that is independently
testable without mounting a component.

---

## How we have it implemented

No keyboard shortcuts exist in any canvas component. `KnowledgeGraph.tsx` has no
`keydown` listener. The only keyboard interaction is native browser behaviour on
`<input>` elements inside node editors.

---

## What will it affect (collateral modifications)

| File | Change needed |
|---|---|
| `stores/ui-store.ts` | Must be present — hook reads `editorState`, `focusedNodeId`, calls `setEditorState`, `setFocusedNode` |
| `stores/graph-store.ts` | Must be present — hook calls `undo()`, `redo()` |
| `L2-canvas/GraphEditor.tsx` | Add `useKeyboard()` call at the top of the component |

---

## Concrete code pieces + source

### Command resolution (pure, testable)

```ts
export type KeyboardCommand =
  | 'edit-node'
  | 'exit-edit-mode'
  | 'undo'
  | 'redo'
  | null;

export function resolveKeyboardCommand(
  event: Pick<KeyboardEvent, 'key' | 'ctrlKey' | 'metaKey' | 'shiftKey'>,
  context: { editorState: EditorState; focusedNodeId: string | null },
): KeyboardCommand {
  const isMod = event.ctrlKey || event.metaKey;
  const key = event.key.toLowerCase();

  if (key === 'enter' && context.editorState === 'browse' && context.focusedNodeId)
    return 'edit-node';
  if (key === 'escape' && (context.editorState === 'edit_node' || context.editorState === 'edit_relation'))
    return 'exit-edit-mode';
  if (context.editorState !== 'browse' || !isMod) return null;
  if (key === 'z' && !event.shiftKey) return 'undo';
  if (key === 'y' || (key === 'z' && event.shiftKey)) return 'redo';
  return null;
}
```

### Editable target guard

```ts
export function isEditableTarget(target: EventTarget | null): boolean {
  if (!target || typeof target !== 'object') return false;
  const el = target as { isContentEditable?: unknown; tagName?: unknown };
  if (el.isContentEditable === true) return true;
  const tag = typeof el.tagName === 'string' ? el.tagName.toLowerCase() : '';
  return tag === 'input' || tag === 'textarea' || tag === 'select';
}
```

### Hook wiring

```ts
export function useKeyboard() {
  // reads from ui-store and graph-store via selectors
  useEffect(() => {
    const onKeyDown = (event: KeyboardEvent) => {
      if (isEditableTarget(event.target)) return;
      const command = resolveKeyboardCommand(event, { editorState, focusedNodeId });
      if (!command) return;
      event.preventDefault();
      // dispatch to store actions...
    };
    window.addEventListener('keydown', onKeyDown);
    return () => window.removeEventListener('keydown', onKeyDown);
  }, [editorState, focusedNodeId, ...]);
}
```

**Full source:** `node-editor:apps/review-workbench/src/features/graph-editor/L2-canvas/hooks/use-keyboard.ts`
