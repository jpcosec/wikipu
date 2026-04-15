# Tasks Board

> **Single entry point for all active work.** Read this before starting any task.

## Active (status=open|in_progress)

| ID | Domain | Task | Priority | Depends On |
|----|--------|------|----------|------------|
| 1 | ingest | Ingest raw unimplemented source | p0 | none |
| 7 | energy | Replace node count with redundancy heuristic | p0 | none |
| 6a | energy | Add descriptive abstraction penalties | p1 | 7 |
| 6c | energy | Add code-doc drift detection | p1 | 7 |
| 8 | audit | Multidimensional styling audit | p1 | 7 |

## Blocked (status=blocked)

No blocked items.

## Ready to Promote (from drawers/)

No items pending promotion.

---

**Working rules for every task:**

1. Check whether any existing test is no longer valid and delete it if needed.
2. Add new tests where necessary.
3. Run the relevant tests.
4. Update `changelog.md`.
5. Delete the solved task file from `desk/tasks/`.
6. Update this Board.
7. Make a commit that clearly states what was fixed, making sure all required files are staged.
