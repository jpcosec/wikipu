---
identity:
  node_id: "doc:drawers/graph-edges-not-populated.md"
  node_type: "backlog_item"
---

# Graph Has Zero Edges

**Added:** 2026-04-16

## Description

The knowledge graph (`knowledge_graph.json`) contains 540 nodes but 0 edges. This means:
- Nodes don't have their `edges` field populated
- Graph traversal queries (ancestors/descendants) don't work
- Only property-based filtering and full-text search work

## Root Cause

Investigation shows:
- `graph_utils.add_knowledge_node()` correctly adds edges to NetworkX graph (lines 26-32)
- But nodes in the JSON don't seem to have edges defined

Need to trace where edges should be populated - likely in scanner.py when processing files.

## Why Deferred

Lower priority - full-text search works, property filtering works.

## Trigger

When graph traversal (ancestors/descendants) is needed for context routing.