# Duplicate Documentation Cleanup

**Explanation:** There are duplicated house rule and agent intro documents across `wiki/`, `agents/`, and `raw/`. This leads to context drift where an agent or human might follow an outdated version of a rule. `raw/` should contain "seed" artifacts, but they should not be the primary reference for active development if they are already "refined" in `wiki/`.

**Reference:** 
- `wiki/standards/00_house_rules.md` vs `raw/sourcetalk_artifacts/00_hausordnung_draft.md`
- `agents/librarian/intro.md` vs `raw/sourcetalk_artifacts/librarian_agent_draft.md`

**What to fix:** Consolidate to a single source of truth for each. Ensure the versions in `wiki/` and `agents/` are the canonical ones and the versions in `raw/` are clearly marked as immutable source ore or historical drafts.

**How to do it:** 
1. Compare `wiki/standards/00_house_rules.md` and `raw/sourcetalk_artifacts/00_hausordnung_draft.md`. If the wiki version is a complete refinement, keep it as truth.
2. Compare `agents/librarian/intro.md` and `raw/sourcetalk_artifacts/librarian_agent_draft.md`.
3. If they are identical, we can leave the `raw/` version (as it is immutable) but the documentation should point to the `wiki/` or `agents/` version.
4. If there are contradictions, the `wiki/` version must win.
5. Consider adding a note to `raw/sourcetalk_artifacts/` indicating they are superseded by the `wiki/` versions (though `raw/` is supposedly immutable, so we might just need to adjust our reading priority).

**Depends on:** none
