# Tasks Board

> **Single entry point for all active work.** Read this before starting any task.

## Active (status=open|in_progress)

| ID | Domain | Task | Priority | Depends On |
|----|--------|------|----------|------------|
| 6a | energy | Add descriptive abstraction penalties | p2 | none | (7 done)
| 6c | audit | Add code-documentation drift detection | ✓ DONE | 7 |
| 7 | energy | Replace node count with redundancy heuristic | ✓ DONE | none |
| 12 | energy | Reduce file complexity (contracts.py 649 lines) | p1 | none |
| 15 | audit | Auto-generate tasks from audit findings | p2 | none |
| pirate | system | Loot and reconstruct pi-coding-agent as "pirate" | ✓ DONE | none |
| 16 | system | Teach Pirate to use wiki-compiler for context efficiency | p1 | none |

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
