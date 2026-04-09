# find_by_io Scanner Coverage — Pathlib and JSON Patterns

**Explanation:** `wiki-compiler query --type find_by_io` always returns zero nodes because `infer_io_from_ast` only detects `open()` built-in calls. The dominant I/O pattern in this codebase is `Path.read_text()`, `Path.write_text()`, `json.load()`, and `json.dump()` — none of which are detected. As a result, `io_ports` is empty on every module node and `find_by_io` is silently useless against the real graph.

**Reference:** `src/wiki_compiler/scanner.py` (`infer_io_from_ast`, `infer_open_call`, `infer_pathlib_call`), `src/wiki_compiler/contracts.py` (`IOFacet`)

**What to fix:** Extend `infer_io_from_ast` to detect `Path.read_text` / `Path.write_text` (disk read/write) and `json.load` / `json.dump` (disk read/write via file handle) call patterns, emitting appropriate `IOFacet` entries.

**How to do it:**
1. In `infer_pathlib_call`, add detection for `.read_text()` → `IOFacet(medium="disk", direction="input")` and `.write_text()` → `IOFacet(medium="disk", direction="output")`.
2. In `infer_io_from_ast`, add detection for `json.load` / `json.dump` call nodes.
3. Add a scanner unit test with a source snippet containing these patterns and assert the resulting node has non-empty `io_ports`.
4. Run `wiki-compiler build` and confirm at least several module nodes now have populated `io_ports`.

**Depends on:** `none`
