---
identity:
  node_id: "doc:wiki/drafts/phase_5_git_workflow.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/plan/UI_REDESIGN_MERGE_PLAN.md", relation_type: "documents"}
---

### Commit Message Format

## Details

### Commit Message Format

```bash
# After merge resolution
git commit -m "merge(ui): integrate Terran Command design system

- Feature-Sliced organization (features/portfolio, features/job-pipeline, features/base-cv)
- Terran Command atoms (Button, Badge, Tag, Icon, Kbd, Spinner, ShortcutsModal)
- Layout components (AppShell, JobWorkspaceShell)
- Mock API layer with full fixture data
- Removed legacy sandbox, views, and pages directories
- 49 TestSprite E2E tests passing
- Documentation promoted to docs/runtime/
TestSprite: Passed
"
```

### Branch Cleanup

```bash
# After successful merge
git branch -d ui-redesign
git worktree remove /home/jp/phd-workspaces/dev/.worktrees/ui-redesign
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/plan/UI_REDESIGN_MERGE_PLAN.md`.