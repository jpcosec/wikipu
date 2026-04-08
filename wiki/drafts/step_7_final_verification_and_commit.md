---
identity:
  node_id: "doc:wiki/drafts/step_7_final_verification_and_commit.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/0-cleanup/agent_guideline.md", relation_type: "documents"}
---

```bash

## Details

```bash
# Confirm no references to old path remain
grep -r "packages/components/quotation" . --include="*.js" --include="*.html" | grep -v node_modules
# Expected: no output

npm test
# Expected: all tests pass
```

Commit:
```bash
git add -A
git commit -m "refactor: cleanup — remove wrappers, relocate quotation flow to apps/quotation/pkg"
```

Generated from `raw/docs_cotizador/plan/legacy/0-cleanup/agent_guideline.md`.