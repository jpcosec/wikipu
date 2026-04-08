---
identity:
  node_id: "doc:wiki/drafts/step_01c_editor_state_history_contract.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md", relation_type: "documents"}
---

### 1. Architecture Logic

## Details

### 1. Architecture Logic

Unified action taxonomy covering all operations including container interactions from CvGraphEditor.

**Semantic action families (undoable):**
- Create / delete node
- Edit node payload (before/after snapshots)
- Create / delete relation
- Edit relation payload
- Attach / detach external reference
- Create / delete annotation anchor
- Reorder within container
- Move node between containers
- Collapse / expand container (borderline — included because it affects proxy edge rendering)

**View-only actions (NOT undoable):**
- Pan / zoom / fit view
- Apply layout preset
- Toggle visibility filters
- Selection changes

**Action metadata:** `actor`, `timestamp`, `affected_ids`, `undo_payload`, `redo_payload`.

**Dirty detection:** Action-count-since-last-save replaces JSON-snapshot comparison.

**Integration:** History stack in zustand store. All mutations through `dispatch(action)`.

### 2. Objectives

1. All graph mutations use the semantic action taxonomy
2. Undo/redo works for all undoable action types including container operations
3. View-only actions never appear in the history stack
4. Dirty detection is action-count-based
5. Action log can be inspected (devtools or sidebar)

### 3. Don'ts

- **Don't log view actions.** Pan/zoom are high-frequency. Bloats stack.
- **Don't implement collaborative conflict resolution.** Single-user only.
- **Don't couple action format to persistence format.** History is in-memory. Persistence saves resulting state.
- **Don't make undo cross-context.** Each graph document gets its own stack.

### 4. Known Gaps & Open Questions

Container operations need to be added to the existing 4-kind HistoryAction. This is new implementation.

### 5. Library Decision Matrix

No new libraries. Zustand middleware for undo/redo stack management. Immer optional for snapshot ergonomics.

### 6. Test Plan

- **Unit**: dispatch create → undo → state matches original. View-only action doesn't change history length. Dirty counter increments on semantic action, resets on save. Container reorder → undo → original order.
- **Component**: Ctrl+Z triggers undo, UI updates.
- **Integration**: create → edit → undo → undo → state is empty.

### 7. Review Checklist

- [ ] Action taxonomy covers all operations including containers
- [ ] Undo/redo works
- [ ] View actions excluded from history
- [ ] Dirty detection is action-based
- [ ] No cross-context undo leaks

---

Generated from `raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md`.