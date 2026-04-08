---
identity:
  node_id: "doc:wiki/drafts/commit_msg_hook.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/git_hooks.md", relation_type: "documents"}
---

**Validates:**

## Details

**Validates:**
1. Message follows format: `<type>(<domain>): <description> (<spec-id>)`
2. Contains TestSprite evidence: `TestSprite: Passed` or `TestSprite: ID-123`

**Valid examples:**
```bash
feat(ui): implement strategy form (spec-123)
fix(pipeline): correct span offset calculation (hotfix-456)
docs(core): update contract schema documentation
```

**Invalid — blocks commit:**
```bash
fix: corrected bug                 # Missing (spec-id)
feat(ui): new feature              # Missing (spec-id)
feat(ui): implement form (spec)    # spec-id format wrong
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/git_hooks.md`.