---
identity:
  node_id: "doc:wiki/drafts/complete_matrix.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/11_routing_matrix.md", relation_type: "documents"}
---

| Domain | Stage | Nature | Doc Path | Target Code | Keywords | Description | What It Does NOT Contain |

## Details

| Domain | Stage | Nature | Doc Path | Target Code | Keywords | Description | What It Does NOT Contain |
|--------|-------|--------|----------|-------------|----------|-------------|-------------------------|
| **pipeline** | all | philosophy | `docs/seed/product/04_pipeline_stages_phd2.md` | - | scrape, extract, match, generate, render, package, langgraph, stages, flow | 8-stage pipeline definition with HITL gates | Specific node contracts (→ `pipeline`) |
| **pipeline** | all | implementation | `docs/runtime/pipeline/README.md` | `src/graph.py` | langgraph, graph assembly, create_prep_match_app, node registry, edges | LangGraph orchestration and flow assembly | Node implementation (→ `pipeline:scrape`) |
| **pipeline** | all | implementation | `docs/runtime/pipeline/node_matrix.md` | `src/nodes/*/logic.py` | node, input, output, execution class, review gate, artifacts | Node I/O matrix with execution classes | Graph assembly (→ `pipeline`) |
| **pipeline** | scrape | implementation | `docs/runtime/pipeline/node_matrix.md` | `src/nodes/scrape/logic.py` | scrape, source, capture, html, url, nllm-nd | Scrape stage: NLLM-ND fetch | Translation (→ `pipeline:translate`) |
| **pipeline** | translate | implementation | `docs/runtime/pipeline/node_matrix.md` | `src/nodes/translate_if_needed/logic.py` | translate, language, normalize, nllm-nd | Translate if needed: conditional normalization | Extract (→ `pipeline:extract`) |
| **pipeline** | extract | implementation | `docs/runtime/pipeline/node_matrix.md` | `src/nodes/extract_understand/logic.py` | extract, llm, requirements, spans, tagging | Extract stage: LLM structured extraction | Match (→ `pipeline:match`) |
| **pipeline** | match | implementation | `docs/runtime/pipeline/node_matrix.md` | `src/nodes/match/logic.py` | match, llm, evidence, alignment, links, graph | Match stage: LLM evidence linking | Review Match (→ `pipeline:review_match`) |
| **pipeline** | review_match | implementation | `docs/runtime/pipeline/node_matrix.md` | `src/nodes/review_match/logic.py` | review_match, nllm-d, decision, approve, reject, route | Review Match: deterministic decision parser | Generate (→ `pipeline:drafting`) or Match (loop) |
| **pipeline** | drafting | implementation | `docs/runtime/pipeline/node_matrix.md` | `src/nodes/generate_documents/logic.py` | drafting, llm, documents, markdown, templates | Generate Documents: LLM + deterministic | Render (→ `pipeline:render`) |
| **pipeline** | render | implementation | `docs/runtime/pipeline/node_matrix.md` | `src/nodes/render/logic.py` | render, nllm-d, markdown, copy | Render stage: markdown copy + hash recording | Package (→ `pipeline:package`) |
| **pipeline** | package | implementation | `docs/runtime/pipeline/node_matrix.md` | `src/nodes/package/logic.py` | package, nllm-d, zip, email, manifest | Package stage: final deliverables | - |
| **ui** | all | philosophy | `docs/seed/product/02_system_architecture.md` | - | ui, frontend, workbench, react, architecture | UI architecture overview (Local-First, CLI > API > UI) | Backend logic (→ `pipeline`) |
| **ui** | all | philosophy | `docs/seed/product/10_ui_dev_integration_map.md` | - | ui vs backend gaps, integration map, workarounds | UI/Dev state mapping (current gaps) | Target architecture (→ `docs/runtime/ui/architecture.md`) |
| **ui** | scrape | implementation | `docs/runtime/ui/architecture.md` | `apps/review-workbench/src/features/job-pipeline/` | react, components, features, atoms, molecules, terran command | Terran Command design system + Feature-Sliced architecture | Legacy sandbox code (→ DELETE) |
| **ui** | scrape | implementation | `docs/runtime/ui/views.md` | `apps/review-workbench/src/features/job-pipeline/` | scrape, diagnostics, source text, error screenshot | Scrape Diagnostics view (B1) | Other pipeline views (→ respective stage) |
| **ui** | extract | implementation | `docs/runtime/ui/views.md` | `apps/review-workbench/src/features/job-pipeline/` | extract, understand, text tagger, requirements, spans | Extract & Understand view (B2) | Match logic (→ `ui:match`) |
| **ui** | match | implementation | `docs/runtime/ui/views.md` | `apps/review-workbench/src/features/job-pipeline/` | match, evidence, graph, reactflow, hitl | Match view (B3) with Evidence Bank + Decision Modal | Drafting logic (→ `ui:drafting`) |
| **ui** | drafting | implementation | `docs/runtime/ui/views.md` | `apps/review-workbench/src/features/job-pipeline/` | drafting, documents, editor, diff, sculpt | Generate Documents view (B4) | Package logic (→ `ui:package`) |
| **ui** | package | implementation | `docs/runtime/ui/views.md` | `apps/review-workbench/src/features/job-pipeline/` | package, deployment, zip, checklist, deploy | Package & Deployment view (B5) | - |
| **ui** | all | implementation | `docs/runtime/ui/components.md` | `apps/review-workbench/src/components/` | atoms, molecules, organisms, button, badge, tag, icon | Component library (Atomic Design atoms/molecules) | Feature-specific logic (→ `features/`) |
| **ui** | all | implementation | `docs/runtime/ui/design_system.md` | `apps/review-workbench/src/styles.css` | terran command, theme, colors, typography, glow effects | Terran Command design tokens and effects | Implementation details (→ `docs/runtime/ui/components.md`) |
| **ui** | all | implementation | `docs/runtime/ui/api_contract.md` | `apps/review-workbench/src/api/`, `apps/review-workbench/src/mock/` | api client, mock, fixtures, v2 contract, cqrs | API v2 contract and mock layer | Backend contracts (→ `api/spec.md`) |
| **api** | all | implementation | `docs/runtime/api/README.md` | `src/interfaces/api/` | fastapi, endpoints, http, get, post, put, patch, bridge, routers | FastAPI endpoints and filesystem-backed data access | Pipeline logic (→ `pipeline`) |
| **api** | all | implementation | `docs/runtime/ui/api_contract.md` | `apps/review-workbench/src/api/` | api client, mock, fixtures, v2 contract, cqrs | UI API v2 contract and mock layer | Backend API (→ `api`) |
| **cli** | all | implementation | `docs/runtime/cli/README.md` | `src/cli/` | cli, command, operator, entrypoint, run_prep_match, run_review_api | CLI operator entrypoints | Pipeline logic (→ `pipeline`) |
| **cli** | all | implementation | `docs/runtime/cli/README.md` | `src/cli/` | scripts, dev.sh, dev-all.sh, environment | Development scripts and environment variables | CLI commands (→ `cli`) |
| **core** | all | implementation | `docs/runtime/core/README.md` | `src/core/` | scraping, pdf, render, io, deterministic, functions, state, round_manager | Core deterministic functions (scraping, text, review) | LLM prompts (→ `pipeline`) |
| **core** | scrape | implementation | `docs/runtime/core/README.md` | `src/core/scraping/` | scrape_detail, crawl_listing, adapter, facade | Scraping facade and adapter registry | Node logic (→ `pipeline:scrape`) |
| **core** | all | implementation | `docs/runtime/core/README.md` | `src/core/text/` | span_resolver, resolve_span, offsets, line numbers | Deterministic span resolution for text matching | UI highlighting (→ `ui:extract`) |
| **data** | all | implementation | `docs/seed/product/canonical_path_registry.md` | - | data/jobs, local-first, files, folders, persistence | **Canonical path registry** | HTTP endpoints (→ `api`) |
| **data** | all | implementation | `docs/seed/product/05_data_architecture.md` | - | data structure, json schemas, folders | Data folder structure and conventions | API endpoints (→ `api`) |
| **data** | all | philosophy | `docs/seed/product/07_evidence_tree_feedback_loop.md` | - | evidence_bank, profile.json, cv profile, skills, augment | Evidence tree philosophy | Stage-specific review (→ `pipeline`) |
| **data** | all | implementation | `docs/seed/product/06_review_node_schema.md` | - | review_node, correction, augmentation, style, rejection | Generic ReviewNode schema | Specific gate (→ `pipeline`) |
| **policy** | all | philosophy | `docs/seed/product/03_methodology.md` | - | determinism, decoupling, cli > api > ui, progressive | PhD 2.0 philosophy | Implementation details (→ `core`) |
| **policy** | all | philosophy | `docs/seed/product/implementation_status.md` | - | implemented, partial, planned, blocked, gaps | **Implementation status tracker** | - |
| **practices** | all | development | `docs/seed/practices/planning_template_ui.md` | - | planning, template, spec, feature, ui | **UI planning template** | - |
| **practices** | all | development | `docs/seed/practices/12_context_router_protocol.md` | `src/tools/context_router.py` | router, context, fetch, orthogonal, mcp | **Context router protocol** | - |
| **practices** | all | development | `docs/seed/practices/13_agent_intervention_templates.md` | - | agent, workflow, sync, implement, design, hotfix | **Agent intervention templates** | - |
| **practices** | all | design | `docs/doc-router-design.md` | - | doc-router, tags, routing, drift, scanner, graph, packet, mcp, templates, task generation | **Doc-Router framework design** — reusable CLI for documentation-driven development | Implementation (→ future `doc-router/` repo) |
| **practices** | all | migration | `docs/seed/plan/UI_REDESIGN_MERGE_PLAN.md` | - | merge, worktree, ui-redesign, integrate, terran command | **UI-Redesign merge plan** (dev ← ui-redesign) | Runtime docs (→ `docs/runtime/ui/`) |
| **practices** | all | migration | `plan/01_ui/specs/00_architecture.md` | `apps/review-workbench/src/` | atomic design, feature-sliced, src structure | Atomic + Feature-Sliced architecture spec | Implementation (→ `docs/runtime/ui/architecture.md`) |
| **practices** | all | migration | `plan/01_ui/specs/00_design_system.md` | `apps/review-workbench/src/styles.css` | terran command, colors, typography, glow, scanline | Terran Command design system spec | Runtime design tokens (→ `docs/runtime/ui/design_system.md`) |
| **practices** | all | migration | `plan/01_ui/specs/00_component_map.md` | `apps/review-workbench/src/components/` | atoms, molecules, organisms, view composition | Component map spec (views → molecules → atoms) | Runtime component library (→ `docs/runtime/ui/components.md`) |
| **practices** | all | migration | `plan/01_ui/specs/A1_portfolio_dashboard.md` | `apps/review-workbench/src/features/portfolio/` | portfolio, dashboard, jobs table, status badge | A1 Portfolio Dashboard spec | Runtime view (→ `docs/runtime/ui/views.md`) |
| **practices** | all | migration | `plan/01_ui/specs/A2_data_explorer.md` | `apps/review-workbench/src/features/explorer/` | explorer, file tree, preview, split pane | A2 Data Explorer spec | Runtime view (→ `docs/runtime/ui/views.md`) |
| **practices** | all | migration | `plan/01_ui/specs/A3_base_cv_editor.md` | `apps/review-workbench/src/features/base-cv/` | cv, editor, graph, nodes, skills | A3 Base CV Editor spec | Runtime view (→ `docs/runtime/ui/views.md`) |
| **practices** | all | migration | `plan/01_ui/specs/B0_job_flow_inspector.md` | `apps/review-workbench/src/features/job-pipeline/` | job, flow, inspector, timeline, pipeline | B0 Job Flow Inspector spec | Runtime view (→ `docs/runtime/ui/views.md`) |
| **practices** | all | migration | `plan/01_ui/specs/B1_scrape.md` | `apps/review-workbench/src/features/job-pipeline/` | scrape, diagnostics, source text, screenshot | B1 Scrape Diagnostics spec | Runtime view (→ `docs/runtime/ui/views.md`) |
| **practices** | all | migration | `plan/01_ui/specs/B2_extract_understand.md` | `apps/review-workbench/src/features/job-pipeline/` | extract, understand, tagger, requirements, spans | B2 Extract & Understand spec | Runtime view (→ `docs/runtime/ui/views.md`) |
| **practices** | all | migration | `plan/01_ui/specs/B3_match.md` | `apps/review-workbench/src/features/job-pipeline/` | match, graph, evidence, reactflow, hitl | B3 Match spec | Runtime view (→ `docs/runtime/ui/views.md`) |
| **practices** | all | migration | `plan/01_ui/specs/B4_generate_documents.md` | `apps/review-workbench/src/features/job-pipeline/` | drafting, documents, editor, diff | B4 Generate Documents spec | Runtime view (→ `docs/runtime/ui/views.md`) |
| **practices** | all | migration | `plan/01_ui/specs/B5_package_deployment.md` | `apps/review-workbench/src/features/job-pipeline/` | package, deployment, zip, checklist | B5 Package & Deployment spec | Runtime view (→ `docs/runtime/ui/views.md`) |

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/11_routing_matrix.md`.