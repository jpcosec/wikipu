---
identity:
  node_id: "doc:wiki/drafts/pipeline_graph_unification_implementation_plan.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/superpowers/plans/2026-03-29-pipeline-graph-unification.md", relation_type: "documents"}
---

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

## Details

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Unify the pipeline into a single LangGraph graph where `match_skill` is a native compiled subgraph with fully visible topology in Studio — no opaque wrapper nodes, no `Command`-based orphan edges.

**Architecture:** Fix `apply_review_decision` to use `add_conditional_edges` instead of `Command(goto=...)` so Studio can statically render all routing paths. Extend `GraphState` with `requirements` and `profile_evidence` fields so the match_skill subgraph receives inputs through normal state passing. Replace the opaque `make_match_skill_node` wrapper with a directly embedded compiled subgraph.

**Tech Stack:** LangGraph `StateGraph`, LangGraph subgraph embedding, Pydantic `TypedDict`, pytest-asyncio.

---

Generated from `raw/docs_postulador_refactor/docs/superpowers/plans/2026-03-29-pipeline-graph-unification.md`.