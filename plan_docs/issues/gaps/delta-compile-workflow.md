# Delta Compile / Draft-Write Workflow

**Explanation:** The external LLM-wiki has `scripts/delta_compile.py --write-drafts` that generates manual draft stubs for stale wiki pages instead of auto-overwriting. This is important — it creates a safety layer where the AI proposes changes but doesn't silently mutate living pages. Our system doesn't have this concept.

**Reference:** LLM-wiki `docs/release-notes-v1.2.2.md` ("Manual delta compile now exists"), `docs/ingest-pipeline.md` ("delta_compile.py --write-drafts")

**What to fix:** Implement a draft-write workflow that:
1. Detects stale wiki pages (where `source_hash` no longer matches current raw)
2. Generates draft stubs in a drafts directory with pre-filled metadata (`source`, `source_hash`, `compiled_at`, `compiled_from`)
3. Does NOT auto-overwrite live wiki pages
4. Provides CLI to review and promote drafts (`wiki-compiler drafts --promote`)

**Depends on:** raw-source-manifest (need raw hash tracking first)

**Priority:** medium — enables safer wiki updates without silent mutation