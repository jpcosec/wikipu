# Add Descriptive Abstraction Penalties

**Explanation:** Enforce the usage of small, highly descriptive functions and classes. Long files must be heavily penalized to force division into smaller, structurally ordered files.

**Reference:**
- `src/wiki_compiler/energy.py`
- `wiki/standards/house_rules.md` (CS-9)

**What to fix:**
1. Add penalty for files exceeding N lines (configurable threshold)
2. Add penalty for functions/methods exceeding N statements
3. Add test-level linting penalties (test files must match clarity standards)

**How to do it:**
1. Add line count penalty per file in energy.py
2. Add cyclomatic complexity-style penalty for long functions
3. Add test file quality heuristics

**Depends on:** 7 (replace node count heuristic)
