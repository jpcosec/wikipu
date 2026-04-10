# Session Log Schema

**Explanation:** Cross-session memory needs a typed contract before any runtime starts writing logs. Right now the standards and the issue describe overlapping but not identical ideas, so the schema must reconcile them first.

**Reference:** `src/wiki_compiler/contracts.py`, `wiki/standards/00_house_rules.md`, `raw/trail_collect.md`

**What to fix:** Define `SessionLog` and `TrailArtifact` models and reconcile the standards language around session history.

**How to do it:**
1. Add typed models for session logs and trail artifacts.
2. Decide whether commit SHA and active branch are required fields.
3. Update docs/tests so the schema and rules agree.

**Depends on:** `none`
