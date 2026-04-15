# Tasks Board

> **Single entry point for all active work.** Read this before starting any task.

## Active (status=open|in_progress)

| ID | Domain | Task | Priority | Depends On |
|----|--------|------|----------|------------|
| 9 | test | Fix test_delta_compile_workflow | p0 | none |
| 10 | test | Fix test_run_skeleton_auto_ingest | p0 | none |
| 11 | energy | Reduce file complexity (main.py 791 lines) | p1 | none |
| 12 | energy | Reduce file complexity (contracts.py 628 lines) | p1 | none |
| 13 | refactor | Refactor main.py:main (1489 statements) | p2 | 11 |
| 14 | perception | Add zone contracts for automatic tracking | p1 | none |

## Blocked (status=blocked)

No blocked items.

## Ready to Promote (from drawers/)

| ID | Domain | Item |
|----|--------|------|
| 1 | ingest | Ingest raw unimplemented source |
| 8 | audit | Multidimensional styling audit |

---

**Working rules for every task:**

1. Check whether any existing test is no longer valid and delete it if needed.
2. Add new tests where necessary.
3. Run the relevant tests.
4. Update `changelog.md`.
5. Delete the solved task file from `desk/tasks/`.
6. Update this Board.
7. Make a commit that clearly states what was fixed, making sure all required files are staged.
