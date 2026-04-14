# 📜 Desk Standards — Unified Execution Framework

> **These standards are executable.** Agents MUST read this file before performing any work. The rituals described here are enforced by the autopoiesis coordinator.

---

## 1. The Multi-Surface Model

```
wikipu/
├── desk/          # Active work surface. Ephemeral — items deleted when resolved.
│   ├── issues/   # Issue tracking + execution queue (The Board)
│   ├── tasks/    # In-flight task artifacts
│   ├── proposals/ # Pending human approval
│   └── Gates.md   # Cross-domain blocking decisions
├── drawers/      # Future work surface. Deferred — ideas waiting for prioritization.
│   └── <topic>   # Organized by domain/theme
└── plan_docs/    # Durable rationale and context pills.
```

| Surface | State | Lifecycle | Entry Gate |
|---------|-------|-----------|------------|
| `desk/` | Active work | Resolve → Delete → Changelog | Any actionable item |
| `drawers/` | Deferred ideas | Stale at 6 months, promote or delete | Design review |
| `plan_docs/` | Durable context | Research → Context Pills | Domain analysis |

**Rule:** No directory may reference a surface below it. `desk/` may reference `drawers/` (to see what's deferred), but never the reverse.

---

## 2. Issue Format (Executable)

Every issue in `desk/issues/` MUST follow this structure:

```markdown
---
id: <uuid-short>
domain: <module/domain>
status: open | blocked | in_progress | done
priority: p0 | p1 | p2 | p3
depends_on: []
created: <ISO date>
---

## Explanation
What is wrong or missing.

## Reference
Files/locations where the issue manifests.

## What to Fix
End state after resolution.

## How to Do It
Implementation path.

## Validation
How to verify the fix works.
```

**Field semantics:**
- `status: open` → Ready to work
- `status: blocked` → Waiting on external dependency (e.g., human decision in Gates.md)
- `status: in_progress` → Currently being worked
- `status: done` → Resolved, awaiting verify → delete

---

## 3. The Initialization Ritual

Before executing ANY issue, the executor MUST perform:

```
1. ATOMIZE     → Break into smallest possible child issues
2. DEDUPE      → Merge overlapping items, verify unambiguous ownership
3. CLEAN      → Delete legacy content, convert to ADR if significant
4. RESOLVE     → Resolve contradictory end states
5. INDEX       → Regenerate desk/issues/Board.md
6. EXECUTE     → Begin work with explicit boundaries
```

**Why:** Prevents parallelization errors where multiple issues touch the same code with inconsistent end states.

---

## 4. The Execution Ritual

Once an issue is resolved, the executor MUST:

```
1. INVALIIDATE → Check if existing tests are broken, update/delete
2. VERIFY     → Run new tests, ensure coverage
3. COMPLY     → Check against all standards in this document
4. CHANGELOG  → Update ../changelog.md with what changed
5. DELETE    → Remove issue file from desk/issues/
6. INDEX     → Update desk/issues/Board.md
7. COMMIT    → Make atomic commit stating exactly what was fixed
```

**Validation rules:**
- No DIP violations (domain may not import infrastructure)
- All Pydantic models have `Field(description=...)`
- Log tags follow the standard set
- Test structure mirrors src/ structure

---

## 5. Issues Board (Single Entry Point)

`desk/issues/Board.md` is the single entry point for all active work.

```markdown
# Issues Board

## Active (status=open|in_progress)
| ID | Domain | Issue | Priority | Depends On |
|----|--------|-------|----------|------------|

## Blocked (status=blocked)
| ID | Domain | Blocker | Gate |
|----|--------|--------|------|

## Ready to Promote (from drawers/)
| ID | Domain | Item |
|----|--------|------|
```



---

## 6. Gate Protocol (Human-in-the-Loop)

When an issue requires human approval:

```
1. PROPOSE    → Add entry to desk/Gates.md with: issue_id, proposal_summary, decision_needed
2. WAIT      → status = blocked until resolution
3. RESOLVE   → Human approves/rejects
4. APPLY     → Apply resolution, update changelog
5. CLEAN    → Remove gate entry
```

**Validity:** A gate entry is valid only if:
- Has explicit issue_id reference
- Has clear decision statement
- Has been updated within the last cycle

**Stale rule:** Gate entries older than 1 cycle with no activity → escalate to review.

---

## 7. Drawer Organization (Future Work)

`drawers/` holds deferred work with this structure:

```markdown
---
id: <uuid>
topic: <broad theme>
status: deferred
stale_after: <ISO date + 6 months>
last_reviewed: <ISO date>
---

## Problem
Description.

## Proposed Direction
High-level approach.

## Linked TODO
Code location: `# TODO(future): <description> — see drawers/<file>.md`
```

**Stale rule:** If not reviewed in 6 months → promote, delete, or re-date. No graveyard.

---

## 8. Phase Completion Ritual

When all parallelizable issues in a Phase/Level are complete:

```
1. COMPILE   → Run wiki-compiler build
2. AUDIT    → Run wiki-compiler audit, fix any new gaps
3. TEST     → Run full pytest suite
4. REGRESS  → Fix any test failures or audit violations
5. ADVANCE  → Move to next phase
```

---

## 9. Code Architecture Contracts

**Layer Separation (enforced):**
- `contracts.py` or `models.py` — All Pydantic schemas. No business logic.
- `storage.py` or `repository.py` — All I/O. No business logic.
- `main.py` — CLI entry. Accepts `argv: list[str] | None` for testing. Returns exit code.
- `__init__.py` — Public surface only.

**Dependency Inversion:** Domain layers NEVER import infrastructure. Infrastructure injected via registry.

**Docstrings:**
- Module-level required
- ABCs list all abstract methods in class docstring
- Public functions include intent + params

**Error Contracts:**
- Domain-specific exceptions defined at top of file
- Never use bare `Exception` for flow control
- Catch → log with `[⚠️]` → re-raise with `from e`

---

## 10. Observability (Log Tags)

Use ONLY these log tags. Do not invent:

| Tag | Meaning | When |
|-----|---------|------|
| `[🧠]` | LLM reasoning | Non-deterministic paths |
| `[⚡]` | Fast/deterministic | Simple paths |
| `[🤖]` | Fallback active | Retry/heuristic kicks in |
| `[✅]` | Success | Validation passed |
| `[⚠️]` | Handled error | Expected failure, logged |
| `[❌]` | Hard failure | Pipeline breaks |
| `[⏭️]` | Skipped | Idempotency check |
| `[📦]` | Cache hit | Loaded existing artifact |

---

## 11. Git Hygiene Rules

- **NEVER edit with dirty tree.** Commit clean state first, then edit.
- Commit message format: `[<domain>] <action>: <what>`

  Examples:
  - `[scanner] fix: missing docstring extraction in nested functions`
  - `[contracts] add: TestMapFacet for coverage tracking`
  - `[docs] update: knowledge_node_facets.md with ADR example`

- Deletable rule: A plan that survives its own completion is drift.

---

## 12. Enforcement

**Automated checks (via autopoiesis coordinator):**
1. `cleanse --apply` — checks topology boundaries before structural changes
2. `wiki-compiler audit` — runs all quality gap checks
3. `github hook` — blocks merge if audit score decreases (TODO: not implemented)

**Manual enforcement:**
- Review Board.md before starting work
- Run Initialization Ritual before any issue
- Run Execution Ritual after any resolution

---

## 13. Quick Reference

| Command | What |
|---------|------|
| `ls desk/issues/` | See active issues |
| `cat desk/issues/Board.md` | Full board view |
| `ls drawers/` | See deferred items |
| `cat desk/Gates.md` | See blocking decisions |
| `wiki-compiler build` | Recompile graph |
| `wiki-compiler audit` | Run quality checks |

---

## 14. Anti-Patterns (Do Not Do)

- [ ] Creating new issue without checking Board.md first
- [ ] Working on issue without running Initialization Ritual
- [ ] Closing issue without Execution Ritual steps (especially delete + changelog)
- [ ] Importing infrastructure into domain layer
- [ ] Using `dict` instead of Pydantic for inter-process data
- [ ] Using bare `Exception` for flow control
- [ ] Leaving stale gate entries (>1 cycle)
- [ ] Keeping items in drawers >6 months without review
- [ ] Writing to `drawers/` from `desk/` surface
- [ ] Creating archive folders (history lives in git + changelog)