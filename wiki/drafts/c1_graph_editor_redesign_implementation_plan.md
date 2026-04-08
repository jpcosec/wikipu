---
identity:
  node_id: "doc:wiki/drafts/c1_graph_editor_redesign_implementation_plan.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/plans/2026-03-23-c1-graph-editor-redesign.md", relation_type: "documents"}
---

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

## Details

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix KnowledgeGraph Terran dark theme, add sub-flow GroupNode, wire CV and Match pages to use KnowledgeGraph as their base editor.

**Architecture:** Three independent tasks sharing KnowledgeGraph.tsx as foundation. C1-A fixes visuals and adds GroupNode/sub-flow support. C1-B creates a CV→graph adapter and replaces BaseCvEditor with a thin KnowledgeGraph wrapper. C1-C creates a match→graph adapter and replaces Match with KnowledgeGraph + UnmappedSkillsPanel.

**Tech Stack:** React 18, TypeScript, @xyflow/react, Terran CSS tokens (`--panel`, `--accent`, `--line`, `--text-main`)

**Spec:** `plan/01_ui/specs/C1_graph_editor_redesign.md`

---

Generated from `raw/docs_postulador_ui/plan/01_ui/plans/2026-03-23-c1-graph-editor-redesign.md`.