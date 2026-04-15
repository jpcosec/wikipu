# Changelog

## 2026-04-15

- resolved issue 9 `fix test_delta_compile_workflow`: Fixed `_compute_node_id` in ingest.py to properly handle `desk/drafts/` zone, now generates correct `doc:desk/drafts/...` node_id
- resolved issue 10 `fix test_run_skeleton_auto_ingest`: Added fallback in `read_git_status` and `read_git_changes` for non-git repos (test environment), preventing subprocess errors
- resolved issue 14 `zone contracts`: Added `ZoneContract` model and zone-based perception. Now tracks desk/ and drawers/ for modified/untracked files via declarative contracts in `wiki/standards/zones.md`
- resolved issue 11 `reduce file complexity`: Extracted CLI subcommands from main.py into `commands/` module. main.py reduced from 791 to 615 lines, main() from 1489 to 4 statements

## 2026-04-11

- resolved issue 1 `01-zone-reorganization`: Implemented the zone reorganization. Created `desk/` and `future_docs/drawers/` zones. Updated `hausordnung` and `AGENTS.md`. Updated `wiki-compiler guard` (formerly `check-workflow`) to be aware of the new structure and fixed a bug in the `run` command.

- resolved issue 2 `02-improve-query-cli`: Improved `wiki-compiler query` CLI with `--issues`, `--gaps`, and `--unimplemented` flags for more specific searches.

## 2026-04-10


- resolved issue 35 `deepen-socratic-protocol`: expanded the Socratic protocol from a stub to a fully defined operational schema
- resolved issue 36 `commit-after-build-protocol`: established OP-9 rule requiring immediate atomic commits after graph builds and hardened `workflow_guard.py` to track `knowledge_graph.json`
- resolved issue 37 `session-log-management-fix`: consolidated session logs into `desk/autopoiesis/sessions/` via `.gemini/settings.json` and root pollution prevention in `.gitignore` and removed the human placeholder comment

- resolved issue 34 `define-energy-and-calculation`: defined systemic Energy and a deterministic calculation method for orthogonality/cost, resolving human comments in ID-2

- resolved issue 33 `define-topology-and-facet`: defined Topology and Facet concepts in the wiki to clarify structural language and removed human comments from ID-1

- resolved issue 32 `documentation-debt-resolution`: created documentation nodes for coordinator, session_storage, trails, preflight, gates, manifest, drafts, artifact_validation, and fixed scanner_plugins compliance

- resolved issue G1 `perception-gates-phase-mislabel`: moved `perception-gates-and-classification` from Phase 4 to Phase 3 in `plan_docs/issues/Index.md` to reflect correct dependency order
- resolved issue G2 `desk-directory-bootstrap`: created `desk/` directory with `Gates.md` table header, `proposals/` and `autopoiesis/cycles/` stubs, and `autopoiesis/Board.md` to support active operational state tracking
- resolved issue G3 `dangling-issue-references`: replaced 6 dead references to `cross-session-memory.md` and `autopoiesis-loop-coordinator.md` in Phase 3 and Phase 4 issue files with their current atomic replacements
- resolved issue G4 `find-by-io-scanner-coverage`: extended AST scanner to detect `Path.read_text`, `Path.write_text`, `json.load`, and `json.dump` patterns; added `direction` field to `IOFacet`
- resolved issue G5 `find-by-io-cli-documentation`: documented the `find_by_io` scanner-coverage dependency and supported patterns in `wiki/reference/cli/query.md`
- resolved issue G6 `find-by-io-not-found-guard`: added explicit file-existence check to `validate-wiki` to distinguish missing files from malformed frontmatter
- resolved issue G7 `missing-adrs-index-node`: created `wiki/adrs/Index.md` as the navigational entry point for the ADR domain
- resolved issue G8 `cleanser-index-false-positives`: exempted `index` and `reference` node types from the `cleanse --detect` compound-abstract detector
- resolved issue G9 `raw-source-manifest`: added `wiki-compiler manifest` command and CSV-backed raw source tracking for file provenance
- resolved issue G10 `delta-compile-workflow`: implemented stale node detection, draft stub generation, and draft promotion via `wiki-compiler drafts` and `SourceFacet`
- resolved issue G11 `ci-enforcement`: added GitHub Actions workflow to automate wiki build, audit, and workflow discipline checks
- resolved issue G12 `bootstrap-upgrade-lifecycle`: added `wiki-compiler bootstrap` and `wiki-compiler upgrade` commands for lifecycle management
- resolved issue 10 `cleansing-apply-and-advanced-detectors`: implemented `cleanse --apply` for approved structural corrections and added new detector families for misplaced folders, stale configs, and orphaned tests
- resolved issue 12 `operational-artifact-validation`: added structural validators for Issue, Board, Backlog Item, and Gate artifacts to ensure metadata consistency
- resolved issue 13 `artifact-validation-rollup`: implemented repo-wide artifact validation via `validate-wiki --all` and integrated it into the CI hygiene workflow
- resolved issue 14 `scanner-plugin-interface`: refactored the scanner into a language-agnostic plugin system with `ScannerPlugin` protocol and basic TypeScript support
- resolved issue 15 `gate-table-runtime`: implemented read/write helpers and sequential ID generation for the `desk/Gates.md` human-approval table
- resolved issue 21 `perception-gates-and-classification`: implemented perturbation classification and gate-aware reporting in `wiki-compiler status`
- resolved issue 16 `run-skeleton`: added `wiki-compiler run` and the initial autopoietic loop coordinator for safe, non-gated actions
- resolved issue 17 `coordinator-gate-resume-flow`: implemented full gate pause/resume/apply orchestration in the coordinator, including approved proposal execution
- resolved issue 18 `coordinator-identity-preflight`: added identity-rule validation (ID-4, ID-5) and minimal-energy (ID-2) action selection to the coordinator
- resolved issue 19 `cycle-record-persistence`: implemented durable coordinator run history via `CycleRecord` JSON persistence in `desk/autopoiesis/cycles/`
- resolved issue 20 `trail-collect-closeout`: implemented structured session signal extraction and routing via `TrailCollection` in the coordinator closeout step
- resolved issue 22 `context-router-contract`: defined `ContextRequest` and `ContextBundle` contracts and refactored the context router to use them
- resolved issue 23 `context-graph-aware-routing`: upgraded context routing to distinguish between direct matches, ancestors, and descendants with ranking scores and reasons
- resolved issue 24 `context-prose-bundles`: implemented prose snippet hydration and refined markdown/JSON rendering for LLM-ready context bundles
- resolved issue 25 `context-active-work-intersection`: implemented active-issue intersection in context bundles by matching subgraph nodes against `plan_docs/issues/`
- resolved issue 26 `context-checklists-and-rules`: implemented operation-aware checklist selection and parsing from `wiki/standards/checklists.md` for context bundles
- resolved issue 27 `session-log-schema`: defined `SessionLog` and `TrailArtifact` contracts for cross-session memory
- resolved issue 28 `session-log-storage`: implemented session log persistence and discovery helpers with canonical paths in `desk/autopoiesis/sessions/`
- resolved issue 29 `history-command`: added `wiki-compiler history` to summarize development session logs and extracted trail artifacts
- resolved issue 30 `trail-collect-session-log`: integrated `SessionLog` generation into the coordinator's trail collection closeout step
- resolved issue 31 `session-resume-from-log`: implemented session continuity by loading the most recent log at coordinator startup

## 2026-04-09

- stopped tracking committed Python cache artifacts and the local Obsidian workspace file, while extending `.gitignore` so those local/generated files stay out of future commits
- decomposed the remaining oversized coordinator, context-routing, and cross-session-memory issues into atomic child issues and updated `plan_docs/issues/Index.md` to reflect the new execution order
- resolved the perception foundation: added `GitFacet`, build-time git metadata injection, `wiki-compiler status`, and spun perturbation classification plus gate-aware reporting into a follow-up issue
- resolved the cleansing detection foundation: added `cleanse --detect`, cleansing proposal/report models, first-pass anomaly detectors, and spun the apply/advanced detector work into a follow-up issue
- resolved the artifact validation foundation: added `wiki-compiler validate-wiki`, typed artifact validation reports, wiki/ADR checks, and split the remaining operational and rollup work into follow-up issues
- resolved the self-inclusion issue by adding graph nodes for the remaining CLI surfaces, creating planned protocol placeholders, and linking the house rules to the system surfaces they govern
- resolved the draft curation pipeline: ingest now mirrors source groups with per-source `INDEX.md`, `wiki-compiler curate` can score or promote drafts, and the promotion criteria are encoded in the house rules
- added `wiki-compiler curate` with scoring and promotion support, documented it in `wiki/reference/cli/curate.md`, and encoded draft promotion criteria in the house rules
- removed the resolved `query-server-runtime` issue after confirming the query runtime and topology proposal validation are already implemented and covered by tests
- expanded `wiki/reference/faq.md` to cover the full planned onboarding question set and removed the resolved FAQ issue from `plan_docs/issues/`
- added OP-6 to `wiki/standards/house_rules.md`: never begin editing from a dirty worktree
- added `wiki-compiler check-workflow` plus workflow rules in standards and `AGENTS.md` to enforce issue linkage, changelog updates, and branch naming for non-trivial work
- reorganized wiki information architecture: added `wiki/Index.md`, introduced `wiki/standards/document_topology.md`, moved issue lifecycle rules into `wiki/standards/issues_lifecycle.md`, and updated planning guidance to point to the standards doc
- moved conceptual and reference docs out of the wiki root, relocated FAQ to `wiki/reference/faq.md`, and retired the legacy `wiki/00_INDEX_MOC.md` naming
- added a root `AGENTS.md` with repository-specific commands, workflow guidance, style rules, and current test/lint status for coding agents
- expanded `AGENTS.md` with explicit graph-usage guidance plus issue workflow references to `wiki/how_to/plan.md` and `wiki/issues_guide.md`
- fixed ingest draft node IDs so generated drafts stay relative to the wiki root and restored planned draft metadata
- restored optional compiled markdown output during `build` and added automatic `documents` edge inference from `wiki/reference/*.md` pages to matching code nodes
- added the canonical `wiki/standards/house_rules.md` document for librarian and ecosystem rule references
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
