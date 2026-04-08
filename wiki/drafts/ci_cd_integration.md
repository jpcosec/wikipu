---
identity:
  node_id: "doc:wiki/drafts/ci_cd_integration.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/git_hooks.md", relation_type: "documents"}
---

Add to your CI pipeline (GitHub Actions example):

## Details

Add to your CI pipeline (GitHub Actions example):

```yaml
# .github/workflows/validate.yml
name: PhD 2.0 Validation
on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install deps
        run: pip install pytest pytest-cov
      
      - name: Run Core tests
        run: pytest src/core/tests/
      
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'
      
      - name: Install deps
        run: cd apps/review-workbench && npm ci
      
      - name: Type check
        run: cd apps/review-workbench && npm run typecheck
      
      - name: Lint
        run: cd apps/review-workbench && npm run lint
```

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/git_hooks.md`.