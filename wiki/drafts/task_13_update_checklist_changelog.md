---
identity:
  node_id: "doc:wiki/drafts/task_13_update_checklist_changelog.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md", relation_type: "documents"}
---

- [ ] **Step 1: Update index_checklist.md**

## Details

- [ ] **Step 1: Update index_checklist.md**

Add new section for component_map compliance phase:

```markdown
### Fase 11 — Component Map Compliance ✅
- [x] `IntelligentEditor` — fixed decorations, added `onSpanSelect`
- [x] `SourceTextPane` → uses IntelligentEditor (tag-hover)
- [x] `DocumentEditor` → uses IntelligentEditor (fold)
- [x] `ScrapeControlPanel` → uses ControlPanel molecule
- [x] `ExtractControlPanel` → uses ControlPanel molecule
- [x] `MatchControlPanel` → uses ControlPanel molecule
- [x] `GraphCanvas` → added onConnect support
- [x] `MatchGraphCanvas` → uses GraphCanvas organism
- [x] `ExplorerTree` → delegates to FileTree organism
- [x] `JsonPreview` → uses IntelligentEditor (fold/json)
- [x] `MarkdownPreview` → uses IntelligentEditor (fold/markdown)
- [x] `CvGraphCanvas` → uses GraphCanvas organism (manual layout)
- [x] E2E tests — TestSprite suite passing
```

- [ ] **Step 2: Add changelog entry**

In `changelog.md`:
```markdown

Generated from `raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md`.