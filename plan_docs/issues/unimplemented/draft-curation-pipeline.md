# Draft Curation Pipeline

**Explanation:** `wiki-compiler ingest` generates draft nodes into `wiki/drafts/` but there is no defined step between ingestion and promotion into the canonical wiki. The result is a flat, unordered pile of machine-generated stubs with no way to distinguish relevant nodes from noise, no grouping by source, and no tooling to surface candidates for promotion. The review process is the missing middle step in the pipeline: `raw/ → [ingest] → wiki/drafts/ → [curation] → wiki/`.

**What to fix:**

1. **Mirror source structure in `wiki/drafts/`.**
   Change `ingest.py` so that draft nodes land in subdirectories that mirror their source path under `raw/`. Example: `raw/docs_cotizador/docs/ARCHITECTURE/design-principles.md` → `wiki/drafts/docs_cotizador/design_principles.md`. This makes it possible to browse drafts by source without reading every file.

2. **Add a draft index per source group.**
   After ingestion, generate a `wiki/drafts/<source>/INDEX.md` per source subdirectory listing all draft node IDs, titles, and their first-line abstracts. This gives a scannable map without opening individual files.

3. **Add a `wiki-compiler curate` command.**
   Two modes:
   - `curate --score`: runs quality checks on all drafts and emits a report. Quality signals: non-empty abstract, abstract length > 1 sentence, node_type is not the default fallback, source file still exists. Outputs a ranked list — highest quality first.
   - `curate --promote <node_id> <dest>`: moves a draft node from `wiki/drafts/` to the specified destination in `wiki/`, updating its `node_id` to match the new path.

4. **Define promotion criteria in the hausordnung.**
   A draft node is ready to promote when: (a) its abstract states a single clear concept, (b) its node_type is not a fallback default, (c) it is relevant to this repository (not external project content), (d) it has no duplicate in the existing wiki graph.

**How to do it:**
- The source subdirectory is already available inside `ingest.py` — `source_path.relative_to(source_dir)` gives the full relative path. Use the first path component as the subdirectory name in `wiki/drafts/`.
- The index generator can reuse `summarize_source()` from `ingest.py` — title and summary are already extracted per node.
- `curate --score` can reuse the graph: load `knowledge_graph.json`, filter nodes whose `node_id` starts with `doc:wiki/drafts/`, and run quality checks against their `semantics.intent` and `identity.node_type`.
- `curate --promote` is a file move + `node_id` rewrite in frontmatter + graph rebuild trigger.

**Depends on:** `gaps/ingest-test-regression.md` (fix path relativization in ingest first, or the subdirectory logic will inherit the same bug)
