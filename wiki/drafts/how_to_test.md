---
identity:
  node_id: "doc:wiki/drafts/how_to_test.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-3-category/phases/01_category_loader.md", relation_type: "documents"}
---

### Automated

## Details

### Automated

```bash
npm test
```

Expected:

- New Category runtime tests pass.
- Existing item/database tests remain green.

### Manual

```bash
npm run serve:sandbox
```

Open new category route and verify:

1. Category selector loads data correctly.
2. Changing `paxGlobal` changes affected child totals.
3. Aggregates reflect current child state.
4. Switching categories does not duplicate stale entries.

Generated from `raw/docs_cotizador/plan/legacy/I-3-category/phases/01_category_loader.md`.