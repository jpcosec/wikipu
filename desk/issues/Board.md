# Issues Board

> **Single entry point for all active work.** Read this before starting any issue.

## Active (status=open|in_progress)

| ID | Domain | Issue | Priority | Depends On |
|----|--------|-------|----------|------------|
| 1 | ingest | Ingest raw unimplemented source | p0 | none | {closed with commit id f7b42e9} |
| 2 | cleanse | Resolve Cleansing Gate | p0 | none | {closed with commit id pending} |
| 3 | compliance | Fix Compliance Regressions | p1 | 2 |
| 4 | compliance | Reduce Compliance Debt | p0 | none |

## Blocked (status=blocked)

No blocked items.

## Ready to Promote (from drawers/)

No items pending promotion.

---

**Working rules for every issue:**

1. Check whether any existing test is no longer valid and delete it if needed.
2. Add new tests where necessary.
3. Run the relevant tests.
4. Update `changelog.md`.
5. Delete the solved issue file from `desk/issues/`.
6. Update this Board.
7. Make a commit that clearly states what was fixed, making sure all required files are staged.
