---
identity:
  node_id: "doc:wiki/drafts/github_branch_protection_recommended.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/git_hooks.md", relation_type: "documents"}
---

For complete enforcement, configure in GitHub Settings > Branches:

## Details

For complete enforcement, configure in GitHub Settings > Branches:

### Required Settings

| Setting | Value | Reason |
|---------|-------|--------|
| Require PR before merging | ✓ | Prevents direct pushes |
| Required approvals | 1+ | Human meta-review (Phase 6) |
| Require status checks | ✓ | CI must pass |
| Do not allow bypassers | ✓ | Even admins must follow rules |

### Required Status Checks

- `pytest` — Core tests
- `typecheck` — TypeScript validation
- `lint` — Code quality
- `testsprite-e2e` — E2E tests (if configured in CI)

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/git_hooks.md`.