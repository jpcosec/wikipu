# Changelog

## 2026-04-09

- decomposed the remaining oversized coordinator, context-routing, and cross-session-memory issues into atomic child issues and updated `plan_docs/issues/Index.md` to reflect the new execution order
- resolved the perception foundation: added `GitFacet`, build-time git metadata injection, `wiki-compiler status`, and spun perturbation classification plus gate-aware reporting into a follow-up issue
- resolved the cleansing detection foundation: added `cleanse --detect`, cleansing proposal/report models, first-pass anomaly detectors, and spun the apply/advanced detector work into a follow-up issue
- resolved the artifact validation foundation: added `wiki-compiler validate-wiki`, typed artifact validation reports, wiki/ADR checks, and split the remaining operational and rollup work into follow-up issues
- resolved the self-inclusion issue by adding graph nodes for the remaining CLI surfaces, creating planned protocol placeholders, and linking the house rules to the system surfaces they govern
- resolved the draft curation pipeline: ingest now mirrors source groups with per-source `INDEX.md`, `wiki-compiler curate` can score or promote drafts, and the promotion criteria are encoded in the house rules
- added `wiki-compiler curate` with scoring and promotion support, documented it in `wiki/reference/cli/curate.md`, and encoded draft promotion criteria in the house rules
- removed the resolved `query-server-runtime` issue after confirming the query runtime and topology proposal validation are already implemented and covered by tests
- expanded `wiki/reference/faq.md` to cover the full planned onboarding question set and removed the resolved FAQ issue from `plan_docs/issues/`
- added OP-6 to `wiki/standards/00_house_rules.md`: never begin editing from a dirty worktree
- added `wiki-compiler check-workflow` plus workflow rules in standards and `AGENTS.md` to enforce issue linkage, changelog updates, and branch naming for non-trivial work
- reorganized wiki information architecture: added `wiki/Index.md`, introduced `wiki/standards/document_topology.md`, moved issue lifecycle rules into `wiki/standards/issues_lifecycle.md`, and updated planning guidance to point to the standards doc
- moved conceptual and reference docs out of the wiki root, relocated FAQ to `wiki/reference/faq.md`, and retired the legacy `wiki/00_INDEX_MOC.md` naming
- added a root `AGENTS.md` with repository-specific commands, workflow guidance, style rules, and current test/lint status for coding agents
- expanded `AGENTS.md` with explicit graph-usage guidance plus issue workflow references to `wiki/how_to/plan.md` and `wiki/issues_guide.md`
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
- created wiki/standards/checklists.md with binary pass/fail verification checklists for core operations (issue-resolution, new-wiki-node, new-module, structural-change, session-close)
- expanded KnowledgeNode schema in contracts.py to include 'index' as a valid node_type and 'extends' and 'implements' as valid relation_types
- updated node_templates.py registry to use 'doc_standard' instead of 'standard' and aligned required sections with current wiki nodes
- updated issues index: marked verification-checklists [6] as resolved
- added issues: artifact-schema-validation [12], scanner-plugin-interface [13]
- clarified validation architecture: artifact validation (markdown/YAML) is always wiki-compiler/Python; code node extraction uses per-language scanner plugins outputting KnowledgeNode
- closed issue [4] wiki-template-compliance: all wiki nodes now have mandatory abstracts and correct section structure; fixed `## Rule/Schema` → `## Rule Schema` heading normalization; extended contracts.py node_type Literal with how_to/adr/reference/faq; fixed how_to template section name (outcome → verification)
- closed issue [5] how-to-wiki-section: created wiki/how_to/ with Index.md and 8 nodes (plan, design, document, research, use_the_graph, use_the_cli, use_socratic_methodology, use_autopoiesis); migrated and deleted wiki/how_to_use.md and wiki/how_to_add_component.md
- closed issue [8] language-style-guides: created wiki/standards/languages/ with Index.md, python.md, typescript.md; Zod vs. interface split clarified; CS-4 TypeScript enforcement marked partial
- closed issue `gaps/duplicate-docs-cleanup`: hausordnung now exists and is `status: implemented`; removed the issue file and updated `plan_docs/issues/Index.md` (renumbered items, collapsed Phase 3, cleared resolved dependencies)

## 2026-04-07

- added Python source scanning with AST, docstring, decorator, and `.wikiignore` support
- added graph query, context rendering, topology validation, and raw-ingestion scaffolding commands
- added compliance baseline scoring during `build` and regression coverage in `tests/test_runtime_features.py`
