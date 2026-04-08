---
identity:
  node_id: "doc:wiki/drafts/d2_group_node_collapse_expand_implementation_plan.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/plans/2026-03-24-d2-group-node-collapse.md", relation_type: "documents"}
---

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

## Details

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add collapse/expand to `GroupNode` using ReactFlow-native primitives (`NodeToolbar`, `node.hidden`, `useNodeId`, `useReactFlow`, `NodeResizer`) with proxy edges, and remove the prop-threading anti-pattern from `SimpleNodeCard`.

**Architecture:** All changes are in one file (`KnowledgeGraph.tsx`). First, a `KnowledgeGraphContext` replaces the `onEditNode`/`nodeId` fields threaded through `node.data`. Then `GroupNode` is made fully self-contained: it uses `useNodeId()` to know its own ID and `useReactFlow()` to manipulate nodes/edges directly — no callbacks from the parent needed. Child visibility is managed via `node.hidden` / `edge.hidden`. Proxy edges (dashed) are injected on collapse and removed on expand.

**Tech Stack:** `@xyflow/react` (NodeToolbar, NodeResizer, useNodeId, useReactFlow, useStore), React 18, TypeScript, Vitest

---

Generated from `raw/docs_postulador_ui/plan/01_ui/plans/2026-03-24-d2-group-node-collapse.md`.