---
identity:
  node_id: "doc:wiki/drafts/component_map_compliance_implementation_plan.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md", relation_type: "documents"}
---

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

## Details

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refactor all remaining pages to use the organisms/molecules from `component_map.md`, then validate with TestSprite E2E.

**Architecture:** Feature components become thin wrappers over generic organisms (IntelligentEditor, GraphCanvas, FileTree, ControlPanel). Pages stay dumb — no logic changes, only swap internal rendering to organisms.

**Tech Stack:** React 18, TypeScript, @uiw/react-codemirror, @xyflow/react, dagre, Tailwind CSS, TestSprite

---

Generated from `raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md`.