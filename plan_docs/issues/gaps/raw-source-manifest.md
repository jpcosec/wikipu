# Raw Source Manifest

**Explanation:** The external LLM-wiki repo has `manifests/raw_sources.csv` that tracks raw source files (PDFs, Excel, etc.) with content hash, file kind, and status. This provides provenance at the raw level. Our system doesn't have this — we track wiki page provenance but not raw file inventory.

**Reference:** LLM-wiki `examples/demo-project/manifests/raw_sources.csv`, `docs/ingest-pipeline.md`

**What to fix:** Create a raw source manifest system that:
1. Defines the CSV schema (filename, path, file_kind, content_hash, status, created, notes)
2. Provides a CLI command to register new raw files (`wiki-compiler manifest --add <path>`)
3. Integrates with the scanner to link raw sources to wiki pages

**Depends on:** none

**Priority:** medium — enables provenance tracking at the raw level