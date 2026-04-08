---
identity:
  node_id: "doc:wiki/drafts/step_03a_text_annotation_links.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md", relation_type: "documents"}
---

### 1. Architecture Logic

## Details

### 1. Architecture Logic

Reusable anchor model for text spans across any text-bearing content type. RichTextPane's patterns inform the design; built fresh for the graph context.

**Anchor model:**
- `document_ref` — which node's payload contains the text
- `anchor_id` — unique identifier
- `selector_type` — offset_range | line_range | quote | block_id
- `selector_payload` — type-specific data
- `linked_node_ids[]` — graph nodes this anchor connects to
- `confidence` — validity likelihood after text edits (1.0 = exact, degrades)

**Lifecycle:** Select text → create anchor → link to nodes → on text edit: recompute offsets, degrade confidence if content changed → below threshold: mark stale.

### 2. Objectives

1. Nodes can attach to text anchors in any text-bearing content
2. Content-type-appropriate selectors (offset for text, line for code)
3. Anchors survive normal edits with confidence tracking
4. Stale anchors visually flagged, not silently dropped
5. Creating an anchor is undoable

### 3. Don'ts

- **Don't silently delete stale anchors.** Flag them.
- **Don't store anchor content as a copy.** Anchor is a pointer.
- **Don't build CRDT-style tracking.** Simple offset shift + quote matching.
- **Don't couple to RichTextPane's category system.** Anchor model is generic.

### 4–7: Gaps, Libraries, Tests, Review

See consolidated matrices in 00_gap_matrix.md and 00_library_decisions.md. Tests: anchor offset shift on insertion, confidence degradation on deletion, quote selector after surrounding edits, create/undo cycle.

---

Generated from `raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md`.