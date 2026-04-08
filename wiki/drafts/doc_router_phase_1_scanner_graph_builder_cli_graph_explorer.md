---
identity:
  node_id: "doc:wiki/drafts/doc_router_phase_1_scanner_graph_builder_cli_graph_explorer.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md", relation_type: "documents"}
---

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

## Details

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the foundation — a CLI that scans tagged docs and code, builds a navigable graph, validates tags, and serves an interactive graph explorer UI.

**Architecture:** Python CLI (`click`) scans project files for tag annotations (YAML frontmatter in docs, structured docstrings in code). Parsed tags become a `RouteGraph` (nodes + edges) stored as JSON. FastAPI serves the graph to a React Flow UI. The UI reuses the Terran Command design system and graph components from PhD review-workbench.

**Tech Stack:**
- Backend: Python 3.11+, click (CLI), FastAPI (serve), PyYAML, hashlib
- Frontend: React 18, @xyflow/react 12, @dagrejs/dagre, Tailwind v4, CodeMirror (preview only)
- Testing: pytest, vitest
- Source reference: `apps/review-workbench/` in `ui-redesign` worktree

**Spec:** `docs/doc-router-design.md` (Sections 1, 2.1, 3, 4.1)

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md`.