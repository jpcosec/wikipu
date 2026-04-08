---
identity:
  node_id: "doc:wiki/drafts/doc_router_phase_2_plan_review_workspace.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/superpowers/specs/2026-03-23-doc-router-phase2-design.md", relation_type: "documents"}
---

> **For agentic workers:** This is a design spec. Use superpowers:writing-plans to create the implementation plan.

## Details

> **For agentic workers:** This is a design spec. Use superpowers:writing-plans to create the implementation plan.

**Goal:** Extend Doc-Router with plan visualization, file tree browsing, and an interactive review editor that supports inline editing, span tagging on code files, and graph editing with comment prompts.

**Architecture:** Plan-centric backend (Approach A). Backend owns plan indexing, iteration tracking, and file tree serving. Frontend adds two tabbed views (Plans, Files) alongside the existing Graph tab. Shared components imported from review-workbench.

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/superpowers/specs/2026-03-23-doc-router-phase2-design.md`.