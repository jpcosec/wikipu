# Perception Layer: Drift Detection and Perturbation Classification

**Explanation:** Every process in the system requires manual invocation. The system cannot detect its own perturbations — a file appearing in `raw/`, source code changing since last build, a node's content drifting from the graph's cached state, a gate sitting open past a threshold. Without perception, there is no autonomous response cycle and no autopoietic closure. The system is a set of tools, not a self-maintaining network.

**Reference:** `raw/autopoiesis_system.md`, `raw/git_tracked_nodes.md`, `src/wiki_compiler/auditor.py`

**What to fix:**
1. Implement `GitFacet` in `contracts.py` with fields: `blob_sha`, `created_at_commit`, `last_modified_commit`, `last_modified_author`, `status` (`tracked` | `untracked` | `modified_since_build`). Populate during `build_wiki()` by calling `git hash-object` and `git log` per file.
2. Add a `wiki-compiler status` command that compares current `blob_sha` of each tracked file against the stored `GitFacet.blob_sha` in the graph. Output: list of nodes with `modified_since_build`, new files in `raw/` not yet ingested, open gates in `desk/Gates.md` older than a configurable threshold.
3. Add a perturbation classifier that maps detected changes to response types:
   - New file in `raw/` → trigger `ingest`
   - Source file changed → flag node as `modified_since_build`, suggest `build`
   - Open gate older than N days → surface in `status` output as stale
   - Node's `blob_sha` drifted → add to cleansing candidates
4. The `status` command output is machine-readable (JSON) so the autopoiesis loop coordinator can consume it.

**How to do it:**
- `git hash-object <file>` gives the blob SHA for any file without a commit.
- `git log --follow -1 --format="%H %ae" -- <file>` gives last commit and author.
- `status` command reads `knowledge_graph.json`, iterates nodes with `GitFacet`, runs hash comparison, outputs structured diff.
- Perturbation classification is a simple lookup table: file path pattern + change type → response category.

**Depends on:** `gaps/ingest-test-regression.md` (path handling must be correct before git paths can be tracked reliably)
