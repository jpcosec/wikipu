---
identity:
  node_id: "doc:wiki/drafts/step_02_structured_documents_subflows.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md", relation_type: "documents"}
---

### 1. Architecture Logic

## Details

### 1. Architecture Logic

Containers compose to represent documents: document → section → block (3-level cap). Uses React Flow's `parentId` + `extent: "parent"` directly for rendering. elkjs compound layout for positioning.

**Nesting model:**
```
Document (container)
  └─ Section (container)
      └─ Block (leaf or container)
          └─ Inline anchor / reference
```

**Each container supports:**
- Collapsed summary (child count, title, status)
- Expanded view (children laid out by elkjs)
- Explicit child ordering (order array, not position-derived)
- Proxy edges when collapsed (dashed, deduplicated)
- Depth limit per view preset

**Structural interactions:**
- Absorption — drag node onto container
- Extraction — drag child out
- Reorder — drag within container (updates order array)
- Cross-container move — drag between containers

All four are semantic actions (01c) — fully undoable.

### 2. Objectives

1. 3-level nesting works (document → section → block)
2. Collapse/expand with correct proxy edges
3. All drag interactions work and are undoable
4. elkjs compound layout produces correct nested positioning
5. Child ordering is explicit (order array)
6. Nesting depth capped per view preset

### 3. Don'ts

- **Don't allow infinite nesting.** Default cap at 3 levels. Configurable per schema via `max_nesting_depth` field (default 3).
- **Don't derive order from Y position.** Order array is truth.
- **Don't render all levels simultaneously.** Progressive expansion.
- **Don't implement content rendering here.** Nesting model only. Content is 03's territory.
- **Don't create a separate "document mode."** Documents are graphs with containers.

### 4. Known Gaps & Open Questions

Proxy edge deduplication logic needs generalization. Performance with many collapsed containers untested.

### 5. Library Decision Matrix

elkjs (already adopted), React Flow parentId/extent (built-in). No new libraries.

### 6. Test Plan

- **Unit**: Order array mutation produces correct sequence. Proxy edge computation on collapse/expand. Cross-container move updates both order arrays.
- **Component**: Drag onto container → absorption feedback → child appears inside.
- **Integration**: Build 3-level doc → collapse all → expand selectively → proxy edges correct.

### 7. Review Checklist

- [ ] 3-level nesting works
- [ ] All drag interactions undoable
- [ ] Proxy edges correct
- [ ] Order array is source of truth
- [ ] elkjs handles compound layout

---

Generated from `raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md`.