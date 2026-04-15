# Zone Alignment Tasks

**Explanation:** Testing checklist for zone renaming (plan_docs→desk/tasks, future_docs→drawers, wiki/drafts→desk/drafts, issues→tasks)

**Reference:** This file tracks remaining test failures and integration checks.

**What to fix:** Fix remaining test failures and verify CLI commands work.

**How to do it:** 

1. Fix test_preflight.py - OP-6 check runs before preflight checks (pre-existing issue)
2. Fix test_run_skeleton.py - git subprocess issue
3. Fix test_runtime_features.py - node_id prefix issue in ingest (writes `doc:drafts/` instead of `doc:desk/drafts/`)
4. Verify `wiki-compiler build` works
5. Verify `wiki-compiler query --tasks` works
6. Verify `wiki-compiler check-workflow` works

**Depends on:** none
