---
identity:
  node_id: "doc:wiki/drafts/what_to_port_from_dev_jobnodeeditorpage.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/01_ui/match_node_editor_merge.md", relation_type: "documents"}
---

### 1. Undo / Redo for Manual Edges

## Details

### 1. Undo / Redo for Manual Edges

**Source:** `apps/review-workbench/src/pages/JobNodeEditorPage.tsx`
- `history: Record<string, unknown>[]` state (max 50 items)
- `historyIndex` pointer
- `pushToHistory()` helper called on every mutation
- Ctrl+Z → undo, Ctrl+Y / Ctrl+Shift+Z → redo

**Target:** `pages/job/Match.tsx` — replace `manualEdges` useState with a history-aware version

**What to adapt:** history only needs to track `manualEdges[]` (not the full JSON payload), so the stack is simpler — just `Array<{ source: string; target: string }[]>` with an index pointer.

---

### 2. Search / Filter Nodes

**Source:** `JobNodeEditorPage.tsx`
- `searchQuery: string` state
- `"/"` key shortcut focuses the search input (`searchRef.current?.focus()`)
- Arrow Up/Down navigates through filtered results
- Nodes matching query get highlighted; non-matching are dimmed

**Target:** Add a search bar above the `MatchGraphCanvas`

**Adaptation:** In the bipartite layout, search should filter/highlight both `ProfileNode` and `RequirementNode` by label text. Non-matching nodes get `opacity-30` style; matching nodes get a highlight ring.

---

### 3. Keyboard Navigation Between Nodes

**Source:** `JobNodeEditorPage.tsx` — `focusedNode` state + `ArrowUp`/`ArrowDown` handler

**Target:** `Match.tsx` — add `focusedNodeId` state; ArrowUp/Down cycles through visible nodes in the canvas (profile nodes first, then requirement nodes)

---

### 4. Focus Mode (Single Node Expanded)

**Source:** `JobNodeEditorPage.tsx` — `focusedNode` state + click to set

**Target:** When a node is clicked → `selectedNode` already tracks this. Extend `MatchControlPanel` to show a richer detail view (not just raw JSON) when a node is selected. The raw JSON readout in `MatchControlPanel` already does this partially — just improve the display (structured fields instead of raw JSON).

---

### 5. Keyboard Shortcuts Reference

**Source:** `JobNodeEditorPage.tsx` — `SHORTCUTS` array + `showShortcuts` modal

**Target:** New atom `ShortcutsModal.tsx` in `components/atoms/` or inline in `Match.tsx`

**Shortcuts for Match:**
| Key | Action |
|---|---|
| Ctrl+S | Save state |
| Ctrl+Enter | Open commit modal |
| Ctrl+Z | Undo last manual edge |
| Ctrl+Y / Ctrl+Shift+Z | Redo |
| / | Focus search bar |
| Arrow Up/Down | Navigate nodes |
| ? | Show this shortcuts reference |
| Escape | Deselect / close modal |

---

### 6. Inline Field Editor for Selected Node

**Source:** `JobNodeEditorPage.tsx` — `editorValue` + `selectedPath` + JSON inline textarea

**Target:** Extend `MatchControlPanel` right panel

**What to add:** When a `RequirementNode` is selected, show editable fields:
- `priority` (select: must / should / nice_to_have)
- `text` (textarea — the requirement text)
- Score display (read-only, computed by backend)

When a `ProfileNode` is selected, show read-only fields from the evidence item.

This replaces the raw `JSON.stringify` dump currently in `MatchControlPanel`.

---

Generated from `raw/docs_postulador_langgraph/plan/01_ui/match_node_editor_merge.md`.