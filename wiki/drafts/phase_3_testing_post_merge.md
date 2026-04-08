---
identity:
  node_id: "doc:wiki/drafts/phase_3_testing_post_merge.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/plan/UI_REDESIGN_MERGE_PLAN.md", relation_type: "documents"}
---

### Local Verification

## Details

### Local Verification

```bash
# 1. TypeScript compilation
cd apps/review-workbench
npm run typecheck

# 2. Lint
npm run lint

# 3. Build
npm run build

# 4. Start dev server
npm run dev
```

### E2E Tests (TestSprite)

```bash
# Run full TestSprite suite
npx testsprite run --suite=ui-redesign-merge

# Expected: 49 tests passing
```

### Compatibility Verification

| Test | Expected Result |
|------|-----------------|
| Portfolio loads | ✅ Shows mock jobs |
| Job workspace opens | ✅ Shell renders with pipeline tabs |
| Scrape diagnostics | ✅ Shows source text and error screenshot |
| Extract view | ✅ Requirements list with spans |
| Match graph | ✅ Nodes with score badges |
| Documents view | ✅ Tabbed editor with save |
| Package view | ✅ Checklist and file list |

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/plan/UI_REDESIGN_MERGE_PLAN.md`.