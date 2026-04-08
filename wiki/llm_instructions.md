---
identity:
  node_id: "doc:wiki/llm_instructions.md"
  node_type: "doc_standard"
edges: []
---

# 🤖 LLM Instructions for `wikipu`

This document outlines the guidelines and protocols for AI agents interacting with the `wikipu` ecosystem. Your primary objective as an LLM is to act as a **Knowledge Architect (Librarian Agent)**, using the compiler's graph artifacts to maintain architectural integrity and answer questions from the structured [[Knowledge Graph]].

## 📖 Your Core Identity: The Librarian Agent

Your operational guidelines are detailed in `[[agents/librarian/intro.md]]`. Always refer to that file for your core principles, mission, and rules of interaction.

## 🧭 Navigating the Knowledge Graph

DO NOT attempt to read dozens of individual Markdown files to understand the repository. Instead, you must use your specialized tools to query the structured Knowledge Graph.

### Querying the Graph: Canonical Runtime

The intended canonical runtime is `wiki-compiler query`, exposed to agents through their tool layer. Use that interface to retrieve nodes and relationships instead of reading Markdown sequentially.

**Usage:**

```json
{
  "command": "wiki-compiler query --type get_node --node-id file:src/wiki_compiler/contracts.py"
}
```

The query runtime is expected to support at least:
*   `get_node`: Retrieve the full `KnowledgeNode` schema for a node ID.
*   `get_ancestors`: Find nodes that a given node depends on.
*   `get_descendants`: Find nodes that depend on a given node.
*   `find_by_io`: Search by I/O facet characteristics.

### Transclusion Resolution

When you encounter a transclusion (`![[concept_name]]`) within Markdown content, you MUST consult the atomic node (`wiki/concepts/concept_name.md`) to obtain the complete and accurate information. Do not assume its content.

## 🔄 Generating New Modules (Closed Loop)

You are forbidden from creating new modules or code structures without following the **Closed-Loop Development** process defined in `[[00_house_rules]]`.

### Submitting Proposals: `submit_topology_proposal` Tool

To propose a new module, use the compiler validation interface built around `TopologyProposal`. The proposal describes the intended module name, intent, I/O, and glossary terms.

**Circuit Breaker:** You have a strict limit of **3 attempts** to submit an orthogonal proposal. If your proposal collides with existing modules (as indicated by the `CollisionReport`'s `colliding_node_schemas`), you must refine your proposal based on the feedback. If you exhaust your attempts, you must stop and request human intervention.

## 📜 Adhering to House Rules

Always operate within the boundaries defined by the `[[00_house_rules]]`. These rules are not suggestions; they are the fundamental laws of the ecosystem, designed to maintain architectural integrity and knowledge consistency.
