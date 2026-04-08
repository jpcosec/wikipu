# Ingest Test Regression

**Explanation:** The Task 5 upgrade to `ingest.py` (atomic decomposition proposer) changed how node IDs are generated. The pre-existing test `test_ingest_scaffolding_creates_draft_nodes` in `tests/test_runtime_features.py` now fails because the upgraded ingest prefixes the temp directory path into node IDs (e.g. `"doc:test_ingest_scaffolding_create0/wiki/raw_notes.md"` instead of `"doc:wiki/raw_notes.md"`).

**Reference:** `tests/test_runtime_features.py::test_ingest_scaffolding_creates_draft_nodes`, `src/wiki_compiler/ingest.py`

**What to fix:** Node IDs produced by `ingest` must be path-relative to the wiki root, not absolute or temp-dir-prefixed. The test assertion `'node_id: "doc:wiki/raw_notes.md"'` should pass.

**How to do it:**
1. Read `src/wiki_compiler/ingest.py` to find where the node_id is constructed.
2. Ensure the path is made relative to the project/wiki root before building the `node_id` string, not relative to any temp or working directory.
3. Re-run the test to confirm it passes without breaking `tests/test_wiki_construction.py`.

**Depends on:** none
