# Tasks Board

> **Single entry point for all active work.** Read this before starting any task.

## Active (status=open|in_progress)

| ID | Domain | Task | Priority | Depends On |
|----|--------|------|----------|------------|
| owl-p1 | owl | Phase 1: Owlready2 Parallel Run | ✅ | none |
| owl-p2 | owl | Phase 2: Quadstore as Primary Backend | ✅ | owl-p1 |
| owl-p3 | owl | Phase 3: Reasoning Integration | ✅ | owl-p2 |
| owl-p4 | owl | Phase 4: Full OWL Migration | ✅ | owl-p3 |

## Blocked (status=blocked)

No blocked items.

## Ready to Promote (from drawers/)

- 1 (ingest raw) → drawers/ingest-raw.md
- 8 (cross-ruling) → drawers/cross-ruling-audit.md

---

**Working rules for every task:**

1. Check whether any existing test is no longer valid and delete it if needed.
2. Add new tests where necessary.
3. Run the relevant tests.
4. Update `changelog.md`.
5. Delete the solved task file from `desk/tasks/`.
6. Update this Board.
7. Make a commit that clearly states what was fixed, making sure all required files are staged.
