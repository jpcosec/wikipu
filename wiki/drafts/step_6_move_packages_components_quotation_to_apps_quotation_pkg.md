---
identity:
  node_id: "doc:wiki/drafts/step_6_move_packages_components_quotation_to_apps_quotation_pkg.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/0-cleanup/agent_guideline.md", relation_type: "documents"}
---

```bash

## Details

```bash
mkdir -p apps/quotation/pkg
cp -r packages/components/quotation/. apps/quotation/pkg/
rm -rf packages/components/quotation
```

Now find and fix all broken imports. Search for any file that still imports from the old path:
```bash
grep -r "packages/components/quotation" . --include="*.js" --include="*.html" | grep -v node_modules
```

For each result, update the import path to point to `apps/quotation/pkg/` (adjust `../` depth based on where the importing file lives).

Run tests. All tests must pass.

---

Generated from `raw/docs_cotizador/plan/legacy/0-cleanup/agent_guideline.md`.