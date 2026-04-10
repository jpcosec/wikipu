# CI Enforcement for Knowledge Hygiene

**Explanation:** The external LLM-wiki has `.github/workflows/wiki-lint.yml` that runs validation scripts on every push (`wiki_check.py`, `raw_manifest_check.py`, `untracked_raw_check.py`, `provenance_check.py`). Our system has `wiki-compiler audit` but it's not automated on every push. We also have `wiki-compiler check-workflow` for issue/changelog discipline but it's not in CI.

**Reference:** LLM-wiki `.github/workflows/wiki-lint.yml`, `docs/release-notes-v1.2.2.md`

**What to fix:** Add CI workflow that runs on push/PR:
1. `wiki-compiler build` — verify graph builds cleanly
2. `wiki-compiler audit` — run all audit checks
3. `wiki-compiler check-workflow` — verify issue linkage and changelog
4. Exit non-zero on failure

**Depends on:** none (can be done independently)

**Priority:** low — nice to have for automated hygiene enforcement