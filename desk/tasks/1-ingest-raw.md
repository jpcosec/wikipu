# Ingest Raw Unimplemented Source

**Explanation:** The file `raw/unimplemented_from_sourcetalk.md` is currently untracked and has not been ingested into the wiki graph.

**Reference:**
- `raw/unimplemented_from_sourcetalk.md`
- `wiki-compiler status`

**What to fix:** Ingest the raw source into `wiki/drafts/` and update the manifest.

**How to do it:**
1. Run `wiki-compiler ingest --source raw --dest wiki/drafts --manifest manifests/raw_sources.csv`
2. Verify nodes appear in knowledge graph
3. Update changelog

**Depends on:** none
