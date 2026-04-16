---
identity:
  node_id: "doc:drawers/cross-ruling-audit.md"
  node_type: "backlog_item"
edges:
  - {target_id: "doc:wiki/concepts/facet.md", relation_type: "implements"}
  - {target_id: "doc:wiki/system/gemma-rag.md", relation_type: "uses"}
---

# Multidimensional Styling (Cross-Ruling) Audit

**Added:** 2026-04-15
**Updated:** 2026-04-16

## Purpose

The autopoietic knowledge system is our **entire topology** (wiki + code). It's queriable via CLI, reviewable via looting, and upgradable via pattern absorption.

### What This Enables

1. **Exact + Semantic Retrieval**: Query returns exact data you put in, plus cross-linked knowledge via facets
2. **Context Reduction**: Structured nodes instead of giant context windows
3. **Self-Upgrade**: Loot external projects, absorb patterns, audit compliance

### How It Works

```
User Query → Facet Match → Nodes → Extract → Compose → Relevant Context
```

Example: "flowers bloom" → facet:season=spring → returns "bees appear" (linked via facet:nectar_source)

### Comparison

| Aspect | gemma-rag | Our Topology |
|--------|-----------|-------------|
| Storage | SQLite + FAISS | Wiki + knowledge graph |
| Query | Vector similarity | CLI + facets |
| LLM Context | Giant window | Structured nodes |
| Upgrade | Manual | Loot + absorb |

### Integration

- gemma-rag capabilities (ingestion, chunking, embedding) can be absorbed to query our own wiki
- Facets provide semantic cross-links between distributed nodes
- Cross-ruling audit ensures facet consistency across all topology

## Why Deferred
Lower priority than core energy heuristics. Can be revisited after core energy system is stable.

## Trigger
When we need composite rule checking across multiple dimensions (e.g., uses Library X AND performs Disk I/O).
