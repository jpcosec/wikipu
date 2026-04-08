---
identity:
  node_id: "doc:wiki/drafts/ui_improvements_data_explorer_implementation_plan.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/superpowers/plans/2026-03-21-ui-improvements-and-data-explorer.md", relation_type: "documents"}
---

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

## Details

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix broken icon rendering, add a JSON/MD data explorer at `/explorer`, fix console errors, and clean up the portfolio page.

**Architecture:** Four independent tasks that can be parallelized. The data explorer requires a new backend endpoint (`GET /api/v1/explorer/browse`) that returns directory listings and file contents from `data/jobs/`, plus a new React page. Icons are a one-line HTML fix. Console errors need deduplication in the view payloads.

**Tech Stack:** React 18 + TypeScript, FastAPI, React Router, existing Terran Command CSS theme

---

Generated from `raw/docs_postulador_langgraph/docs/superpowers/plans/2026-03-21-ui-improvements-and-data-explorer.md`.