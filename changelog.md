# Changelog

## 2026-04-09

- fixed ingest draft node IDs so generated drafts stay relative to the wiki root and restored planned draft metadata
- restored optional compiled markdown output during `build` and added automatic `documents` edge inference from `wiki/reference/*.md` pages to matching code nodes
- added the canonical `wiki/standards/00_house_rules.md` document for librarian and ecosystem rule references

## 2026-04-07

- added Python source scanning with AST, docstring, decorator, and `.wikiignore` support
- added graph query, context rendering, topology validation, and raw-ingestion scaffolding commands
- added compliance baseline scoring during `build` and regression coverage in `tests/test_runtime_features.py`
