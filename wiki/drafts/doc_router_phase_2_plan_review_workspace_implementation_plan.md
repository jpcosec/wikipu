---
identity:
  node_id: "doc:wiki/drafts/doc_router_phase_2_plan_review_workspace_implementation_plan.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/superpowers/plans/2026-03-23-doc-router-phase2.md", relation_type: "documents"}
---

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

## Details

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extend Doc-Router with plan visualization, file tree browsing, and an interactive review editor with span tagging and graph editing.

**Architecture:** Backend gains two modules (`plans.py`, `filetree.py`) + new API routes in `server.py`. Config extended with `plan_paths`. Frontend adds TabNav, Plans tab (list + timeline + editor), and Files tab (tree + preview). Components copied from review-workbench where available.

**Tech Stack:** Python (FastAPI, PyYAML, AST), React 18 (@xyflow/react, @codemirror/*, @tanstack/react-query, Tailwind v4)

**Spec:** `docs/superpowers/specs/2026-03-23-doc-router-phase2-design.md`

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/superpowers/plans/2026-03-23-doc-router-phase2.md`.