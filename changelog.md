# Changelog

## 2026-04-09

- fixed ingest draft node IDs so generated drafts stay relative to the wiki root and restored planned draft metadata
- restored optional compiled markdown output during `build` and added automatic `documents` edge inference from `wiki/reference/*.md` pages to matching code nodes
- added the canonical `wiki/standards/00_house_rules.md` document for librarian and ecosystem rule references
- added OP-5 (Atomization) to hausordnung: every work unit must be independently completable and verifiable; split when more than 3-4 steps can fail independently
- added System Core table to hausordnung defining the five load-bearing elements (autopoiesis/wiki/knowledge-graph/git/cli) and their roles
- revised ID-5 (Human Gate): scope narrowed to topology-boundary-crossing operations only; in-topology reversible actions no longer require human approval
- revised NAV-4: renamed MOC concept to Index.md (wiki) / Board.md (desk) with clear distinction between navigational and operational entry points
- added OP-5 (Git Commit Cadence): commit = coherent state transition, never cross session boundary without committing
- revised Layer 5 (Code Style): made language-agnostic, added Python and TypeScript/JavaScript specific sub-rules
- added issues: how-to-wiki-section [5], verification-checklists [6], faq [7], language-style-guides [8], context-routing [16]
- revised Layer 5 header: code style rules now apply to all source regardless of location or language
- revised OP-5 (Git Commit Cadence): one commit per atomic issue resolved; introduced branching model — issue/phase branches for in-progress work, main = stable milestone
- created wiki/standards/artifacts/ with schema definitions for all artifact types: wiki_node, adr, proposal, board, issue, gate, backlog_item
- updated WK-4 in hausordnung to reference artifacts/ instead of inline list
- added issues: artifact-schema-validation [12], scanner-plugin-interface [13]
- clarified validation architecture: artifact validation (markdown/YAML) is always wiki-compiler/Python; code node extraction uses per-language scanner plugins outputting KnowledgeNode
- closed issue `gaps/duplicate-docs-cleanup`: hausordnung now exists and is `status: implemented`; removed the issue file and updated `plan_docs/issues/Index.md` (renumbered items, collapsed Phase 3, cleared resolved dependencies)

## 2026-04-07

- added Python source scanning with AST, docstring, decorator, and `.wikiignore` support
- added graph query, context rendering, topology validation, and raw-ingestion scaffolding commands
- added compliance baseline scoring during `build` and regression coverage in `tests/test_runtime_features.py`
