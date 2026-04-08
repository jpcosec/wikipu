---
identity:
  node_id: "doc:wiki/drafts/installation.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/git_hooks.md", relation_type: "documents"}
---

```bash

## Details

```bash
bash docs/seed/practices/scripts/setup_hooks.sh
```

Or manually:
```bash
cp docs/seed/practices/scripts/hooks/* .git/hooks/
chmod +x .git/hooks/commit-msg .git/hooks/pre-push
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/git_hooks.md`.