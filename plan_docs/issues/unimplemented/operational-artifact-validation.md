# Operational Artifact Validation

**Explanation:** The new artifact validation foundation only validates authored wiki markdown with frontmatter-bearing rules and ADR-local checks. Operational artifacts such as issue files, board files, backlog items, and gate rows still rely on prose conventions with no executable validator.

**Reference:** `wiki/standards/artifacts/issue.md`, `wiki/standards/artifacts/board.md`, `wiki/standards/artifacts/backlog_item.md`, `wiki/standards/artifacts/gate.md`

**What to fix:** Add structural validators for body-only operational artifacts and expose them through the artifact validation runtime.

**How to do it:**
1. Add validators for issue, board, backlog item, and gate row structures.
2. Reuse the artifact reporting shape from the wiki validation foundation.
3. Add focused tests for each artifact category.

**Depends on:** `none`
