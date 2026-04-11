---
identity:
  node_id: "doc:wiki/concepts/core_philosophy.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/sourcetalk.txt", relation_type: "documents"}
  - {target_id: "doc:wiki/concepts/how_wikipu_works.md", relation_type: "extends"}
compliance:
  status: "implemented"
  failing_standards: []
---

The Core Philosophy of Wikipu is the transformation of passive documentation into an active, compiled Knowledge Graph—shifting the paradigm from stateless RAG to a stateful "LLM Wiki."

## The "Compile" vs. "Search" Paradigm
Traditional Retrieval-Augmented Generation (RAG) is "stateless": it searches for disconnected fragments of text at query time. Wikipu, following the April 2026 vision of Andrej Karpathy, treats knowledge as **Source Code** that must be **Compiled**.

- **Raw Ore (`raw/`):** Dirty, unorganized source material (PDFs, transcripts, tweets).
- **Compilation:** The `wiki-compiler` acts as a deterministic librarian, atomizing raw ore into structured Markdown nodes with typed metadata.
- **Knowledge Graph:** The result is a unified, traversable graph (`knowledge_graph.json`) that provides the LLM with a coherent "world map" of the system.

## The LLM as "Bibliotecario" (Librarian)
In this ecosystem, the LLM is not just a text generator; it is a **Librarian**.
- It does not "guess" how the system works; it queries the graph.
- It is responsible for synthesis: when new information enters `raw/`, the Librarian "compiles" it into the existing structure, resolving contradictions and identifying gaps.
- It maintains the **Hausordnung** (House Rules) as the Law of the repository.

## The Desk Metaphor
The repository structure mirrors a physical working desk:
- **The Drawer:** Future designs and deferred concepts are stored in "Drawers" until they are ready to be consumed.
- **The Desk (`desk/tasks/`):** The active operational surface where implementation happens.
- **The Ledger (`changelog.md`):** Every change is recorded, ensuring traceable causality from raw perturbation to implemented code.

## Why it Matters
This architecture ensures that "learning" is cumulative. Design decisions made during a refactor are not lost; they are "compiled" back into the Wiki, becoming part of the permanent intelligence of the system. This eliminates the "amnesia" of standard AI interactions.

Generated from the `sourcetalk.txt` genesis transcript.
