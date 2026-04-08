---
identity:
  node_id: "doc:wiki/drafts/extraction_lifecycle_for_a_new_source.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/crawl4ai_usage.md", relation_type: "documents"}
---

Every new source follows this progression:

## Details

Every new source follows this progression:

1. start with Crawl4AI-assisted extraction to get the source working quickly
2. learn the DOM and stabilize selectors across multiple real pages
3. persist a deterministic schema in `scrapping_schemas/<source>_schema.json`
4. switch the source to prefer the saved schema for steady-state extraction
5. keep LLM extraction only as a fallback or temporary bootstrap tool

The steady-state goal is always: saved schema first, LLM second.

Generated from `raw/docs_postulador_refactor/docs/standards/code/crawl4ai_usage.md`.