┄ Wikipu Issues Index

This file is the entrypoint for subagents deployed to solve issues in this repository.

All issue-fixing work must stay aligned with the rest of `plan_docs/` and `wiki/`, with special care for `wiki/standards/` so implementation, tests, and documentation remain consistent with the project's rules.

┄┄ Working rule for every issue

Once an issue is solved, the next step is always:

 1. Check whether any existing test is no longer valid and delete it if needed.
 2. Add new tests where necessary.
 3. Run the relevant tests.
 4. Update `changelog.md`.
 5. Delete the solved issue from both this index and the corresponding file in `plan_docs/issues/`.
 6. Make a commit that clearly states what was fixed, making sure all required files are staged.

┄┄ Priority roadmap

┄┄┄ Phase 1 — Restoration and Ingestion

 1. plan_docs/issues/gaps/1-ingest-raw-unimplemented.md
 2. plan_docs/issues/gaps/2-resolve-cleansing-gate.md
 3. plan_docs/issues/gaps/3-fix-compliance-regressions.md

┄┄ Dependency summary

• plan_docs/issues/gaps/3-fix-compliance-regressions.md  ->  plan_docs/issues/gaps/2-resolve-cleansing-gate.md

┄┄ Parallelization map

Phase 1  [1][2]
Phase 2     [3]
