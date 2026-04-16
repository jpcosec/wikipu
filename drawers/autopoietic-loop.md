---
identity:
  node_id: "doc:drawers/autopoietic-loop.md"
  node_type: "backlog_item"
edges:
  - {target_id: "doc:wiki/system/pirate.md", relation_type: "implements"}
  - {target_id: "doc:wiki/system/gemma-rag.md", relation_type: "implements"}
---

# Autopoietic Knowledge Loop

**Added:** 2026-04-16

## Why We Loot Pi/Pirate

The autopoietic system needs three layers:

| Layer | Component | Function |
|-------|-----------|----------|
| Knowledge | Wiki | What we know |
| Retrieval | gemma-rag | How we find it |
| Execution | Pirate | How we act on it |

## The Loop

```
Query → Wiki (knowledge) → gemma-rag (retrieve) → Pirate (execute) → Upgrade (loot)
```

Instead of external LLM with giant context window:
1. **Query** structured nodes
2. **RAG** gets relevant context
3. **Pirate** acts as agent (review, edit, run commands)
4. **Loot** external projects to absorb patterns

## Purpose

- **Context Reduction**: Structured knowledge instead of dumping everything into prompts
- **Self-Maintenance**: Pirate can review, edit, upgrade our code using our wiki as context
- **Autopoiesis**: The system maintains and improves itself using its own tools

## Integration

- Pirate uses wiki/selfDocs files as system prompt context
- gemma-rag enables semantic retrieval from our wiki
- Looting external projects absorbs their patterns into topology
- Cross-ruling audit ensures consistency across all layers