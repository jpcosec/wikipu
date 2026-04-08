---
identity:
  node_id: "doc:wiki/drafts/schema_explorer_implementation_plan.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/docs/superpowers/plans/2026-03-24-schema-explorer.md", relation_type: "documents"}
---

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

## Details

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make KnowledgeGraph accept a `readOnly` prop and add new color tokens, then build a SchemaExplorer page that feeds `cv.schema.json` through a `schemaToGraph` adapter and renders it read-only.

**Architecture:** Schema JSONs (one per domain) define node types, render hints, edge types, and visual encoding. A pure `schemaToGraph` function converts them to `SimpleNode[]` + `SimpleEdge[]`. `SchemaExplorer` selects a domain, converts, and passes to `KnowledgeGraph readOnly`. No new component primitives — KnowledgeGraph is the runtime.

**Tech Stack:** React 18 · TypeScript · @xyflow/react · Vitest (added) · Tailwind Terran tokens

---

Generated from `raw/docs_postulador_ui/docs/superpowers/plans/2026-03-24-schema-explorer.md`.