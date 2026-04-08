---
identity:
  node_id: "doc:wiki/drafts/external_dependencies.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md", relation_type: "documents"}
---

**Production:**

## Details

**Production:**
- `xstate@5.28.0` — State management (14-15 KB gzipped)
- `json-logic-js@2.0.5` — Rule conditions (lightweight)

**Development:**
- `vitest` — Test runner (all packages)
- `rollup` — Bundler (top-level)

**Total bundle size:** ~354 KB (10,989 lines, includes all logic)

**Why minimal dependencies?**
- Easier to understand code
- Smaller bundle
- No supply chain risk
- No runtime version conflicts
- Works in Google Apps Script environment

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md`.