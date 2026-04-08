---
identity:
  node_id: "doc:wiki/drafts/step_03_rich_content_nodes_shared_contract.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md", relation_type: "documents"}
---

### 1. Architecture Logic

## Details

### 1. Architecture Logic

Bridge between node type registry (01b) and specific content renderers (03a–03f). Defines the shared payload and rendering contract.

**Rich node payload contract:**
- `content_type` — discriminant matching registry type_id
- `payload` — actual content (markdown string, JSON object, image ref, etc.)
- `anchor_refs[]` — annotation anchors attached to ranges within content
- `external_asset_refs[]` — pointers to external files, URLs, schema entries
- `edit_capabilities` — what this content type supports: inline edit, full editor, read-only, format-on-save

**Renderer contract:** Each content type provides a React component per mode (as a node_renderer extension). Commits changes through `dispatch(edit_node_payload)`.

**Anchor attachment model:** Rich content can have internal anchors (text range, line range, image region, key path). Content-type-specific selectors stored in `anchor_refs`.

### 2. Objectives

1. Shared payload contract exists as TypeScript interface
2. All 03a–03f types implement it without editor special-casing
3. Anchor model supports content-type-specific selectors
4. Edits flow through dispatch(edit_node_payload)
5. Persistence handles all payload types through one path

### 3. Don'ts

- **Don't let content renderers manage own persistence.** Commit through dispatch.
- **Don't define anchor selectors for unimplemented types.** Each 03x step defines its own.
- **Don't embed display_mode in persisted payload.** display_mode is view state.
- **Don't create abstract base classes.** Interface + discriminated union.

### 4. Known Gaps & Open Questions

- **GAP-ARCH-03** (resolved here): Anchor identity model defined.

### 5. Library Decision Matrix

None. Contract definition step.

### 6. Test Plan

- **Unit**: Each content type payload serializes/deserializes correctly. Anchor_refs survive payload edits. TypeScript exhaustiveness check.

### 7. Review Checklist

- [ ] Contract interface exists
- [ ] All 03x types can implement it
- [ ] Anchor model supports multiple selectors
- [ ] display_mode not in persisted payload
- [ ] Single dispatch path

---

Generated from `raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md`.