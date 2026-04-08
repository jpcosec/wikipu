---
identity:
  node_id: "doc:wiki/drafts/d2_group_node_collapse_expand_2026_03_24.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/plans/2026-03-24-d2-group-node-collapse.md", relation_type: "documents"}
---

- `GroupNode` now has a `NodeToolbar` (▼/▶) at top-left with child count badge

## Details

- `GroupNode` now has a `NodeToolbar` (▼/▶) at top-left with child count badge
- Collapsing hides children via `node.hidden` and injects dashed proxy edges
- Expanding restores children and removes proxy edges
- `NodeResizer` inside `GroupNode` — auto-resizes when selected, collapses to 48px height
- `GroupNode` is now self-contained: uses `useNodeId()` + `useReactFlow()`, no parent callbacks
- `SimpleNodeCard` Edit button now uses `KnowledgeGraphContext` + `useNodeId()` — no prop threading
- Removed `nodeId`/`onEditNode` from `SimpleNodeData` interface
- Exported `deduplicateByEndpoints` helper with 4 unit tests
```

- [ ] **Step 3: Commit**

```bash
git add plan/index_checklist.md changelog.md
git commit -m "docs: D2 group node collapse — changelog and checklist"
```

Generated from `raw/docs_postulador_ui/plan/01_ui/plans/2026-03-24-d2-group-node-collapse.md`.