# find_by_io CLI Documentation Gap

**Explanation:** The `wiki-compiler query --type find_by_io` command silently returns empty results when no nodes have populated `io_ports`, with no indication to the user of why. The CLI reference (`wiki/reference/cli/query.md`) does not document which code patterns the scanner detects, leaving users unable to predict when the query will return results.

**Reference:** `wiki/reference/cli/query.md`, `src/wiki_compiler/scanner.py` (`infer_io_from_ast`)

**What to fix:** Update `wiki/reference/cli/query.md` to document that `find_by_io` only matches nodes where the scanner detected disk I/O calls (currently `open()` built-ins), list the currently supported patterns, and note that modules using `pathlib` or `json` without detected calls will not appear in results.

**How to do it:**
1. Read the current `wiki/reference/cli/query.md`.
2. Add a `find_by_io` subsection explaining scanner-coverage dependency, currently detected patterns, and what an empty result means.
3. Run `wiki-compiler build` and `wiki-compiler validate-wiki --path wiki/reference/cli/query.md` to confirm the node is still valid.
4. No code changes, no new tests — docs-only.

**Depends on:** `none`
