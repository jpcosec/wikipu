---
identity:
  node_id: "doc:wiki/drafts/what_to_port_from_dev_richtextpane.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/01_ui/extract_text_tagger_merge.md", relation_type: "documents"}
---

### 1. Character-Level Inline Span Highlighting

## Details

### 1. Character-Level Inline Span Highlighting

**Source:** `RichTextPane` — `buildSegments()` + `<mark>` rendering (lines 134–171, 828–846)

**Target:** `SourceTextPane.tsx` — replace line-range highlight with character-offset highlight

**What changes:**
- `RequirementItem` data gains character offsets (`start_char`, `end_char`) in addition to the existing `text_span: { start_line, end_line }`
- `SourceTextPane` receives all requirement spans (not just the hovered/selected one) and renders each as a colored `<mark>` inline
- Each requirement gets a distinct color (by priority: primary for must, secondary for nice)
- Clicking a highlighted span in the source selects that requirement in the list

**Why it matters:** Currently hovering a card only highlights an entire line range. Character offsets let the operator see exactly which text fragment produced each requirement.

---

### 2. Select Text → Create Requirement

**Source:** `RichTextPane` — `captureSelection()` + `addNote()` (lines 522–596)

**Target:** `SourceTextPane.tsx` + `ExtractUnderstand.tsx`

**What to add:**
- `onMouseUp` / `onKeyUp` handler on the source text pane captures `window.getSelection()`
- Converts DOM range to character offsets (same `toOffset()` helper as `RichTextPane`)
- Shows a floating "Tag as requirement" chip above the selection (replaces `SelectionChip`)
- Pressing `1` (must) or `2` (nice) while text is selected immediately creates a new `RequirementItem` with the selected text pre-filled and the `text_span` / character offsets recorded

**Why it matters:** The operator can read the source and create requirements in-place — much faster than clicking "+ ADD" and typing.

**Note:** Only carry over the selection → requirement creation. Drop the "Info" category and all its subcategories — the pipeline only needs `must` / `nice` / `nice_to_have` priority.

---

### 3. Keyboard-First Priority Assignment

**Source:** `RichTextPane` — `useEffect` keydown handler (lines 690–736)

**Target:** `ExtractUnderstand.tsx` — extend existing `handleKeyDown`

**Shortcuts to add:**
| Key | Action |
|---|---|
| `1` | Tag selection as `must` (when text selected in source) |
| `2` | Tag selection as `nice` / `nice_to_have` |
| `Escape` | Clear selection |

Simple two-step: select text in source → press `1` or `2` → requirement card created.

---

### 4. Details / Annotation Field per Requirement

**Source:** `RichTextPane` — `EditableField` + `NoteCard` details field (lines 192–253, 461–473)

**Target:** `RequirementItem.tsx` — add collapsible "Notes" textarea

**What to add:**
- Each `RequirementItem` gets an optional `notes?: string` field
- When expanded (selected), shows a textarea for operator annotations
- Notes are saved with the editor state via `useEditorState`
- Displayed as a dimmed italic preview in the collapsed card

**Why it matters:** Operator may want to record *why* a requirement was adjusted, or flag it for later.

---

### 5. Collapse / Expand Cards

**Source:** `RichTextPane` — `collapsedNoteIds: Set<string>` + `toggleCollapse()` (lines 496, 772–782)

**Target:** `RequirementItem.tsx` — add collapsed state

**What to add:**
- Collapsed (default): shows only ID badge + priority chip + first ~60 chars of text
- Expanded (on click): shows full text editor + notes field + delete button
- Selected card auto-expands

**Why it matters:** With 10–20 requirements the list gets long. Collapsed cards give an overview; expanded shows editing controls.

---

### 6. Search / Filter in Requirement List

**Source:** `RichTextPane` — `searchQuery` state + filter logic (lines 497, 785–804)

**Target:** `RequirementList.tsx` — add search input in header

**What to add:**
- Search input in the "Extracted Reqs (N)" header bar
- Filters cards by requirement text, notes, or ID
- Clears on `Escape`

---

### 7. Drag-and-Drop Priority Reclassification

**Source:** `RichTextPane` — `@dnd-kit/core`, `MainCategoryBox` as drop target, `NoteCard` as draggable (lines 1–13, 276–349, 363–481)

**Target:** `RequirementList.tsx` — optional, lowest priority

**What to add:**
- Drag a requirement card from the list onto a "MUST" or "NICE" zone at the top of the list
- Reclassifies the requirement priority on drop

**Note:** This is the most complex feature to port. Implement only after 1–6 are done.

---

Generated from `raw/docs_postulador_langgraph/plan/01_ui/extract_text_tagger_merge.md`.