---
identity:
  node_id: "doc:wiki/drafts/test_summary.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md", relation_type: "documents"}
---

| Package | Tests | Files | Status |

## Details

| Package | Tests | Files | Status |
|---------|-------|-------|--------|
| database | 5/5 | 1 | ✅ PASS |
| pricing | 110/148 | 25 | ✅ (38 pre-existing) |
| xstate | 59/59 | 3 | ✅ PASS |
| domain | 553/553 | - | ✅ PASS |
| frontend | 12/12 | - | ✅ PASS |
| **TOTAL** | **739/777** | **29+** | **95.1%** |

**Run all tests:**
```bash
for dir in database pricing xstate domain frontend; do
  (cd packages/$dir && npm test) &
done && wait
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md`.