---
identity:
  node_id: "doc:wiki/how_it_works.md"
  node_type: "concept"
edges: []
---

# 📖 How `wikipu` Works

The `llm-wiki-compiler` is a powerful tool designed to maintain architectural integrity and provide a structured knowledge base for both human and AI developers. It operates on a few core principles:

## 🧠 The Meta-Graph

At its heart, `wikipu` builds and maintains a **Meta-Graph** (or Knowledge Graph) of your repository. This graph is a machine-readable representation of your codebase's structure, dependencies, and semantics. It's composed of:

*   **Knowledge Nodes**: Every significant element in your repository (directories, files, code constructs, documentation standards, concepts) is a `KnowledgeNode`. Each node has a `SystemIdentity` (a unique ID and type) and can have various `Facets` attached to it.
*   **Edges**: Nodes are connected by `Edges` that define their relationships (e.g., `contains`, `depends_on`, `reads_from`, `writes_to`, `documents`, `transcludes`).

This graph is powered by `networkx` and can be queried by AI agents to understand the system's topology.

## 🌟 Facets: Dimensions of Knowledge

`KnowledgeNode`s are enriched with `Facets`, which represent different dimensions of knowledge about that element:

*   **`IOFacet`**: Describes input/output operations (medium, schema references, path templates).
*   **`ASTFacet`**: Captures information from the Abstract Syntax Tree (code construct type, signatures, dependencies).
*   **`SemanticFacet`**: Stores the high-level intent and raw docstrings.
*   **`ADRFacet`**: Records Architectural Decision Records related to the node.
*   **`ComplianceFacet`**: Tracks the node's adherence to the `00_house_rules` and its implementation status. The full lifecycle is:
    1. `planned` — mentioned in `future_docs/` or `plan_docs/`, no code yet
    2. `scaffolding` — directory and required files created (`contracts.py`, `__init__.py`, `README.md`)
    3. `mocked` — logic exists but runs against fakes/stubs, no real dependencies
    4. `implemented` — connected to real dependencies and production-ready
    5. `tested` — automated tests cover the node's behaviour
    6. `exempt` — excluded from compliance tracking via `.wikiignore` or `@wiki_exempt`
*   **`TestMapFacet`**: Records the testing strategy for a node (test type and coverage).

## 📜 The House Rules (`00_house_rules.md`)

The `00_house_rules.md` document (`[[00_house_rules]]`) is the foundational standard that governs the entire ecosystem. It defines strict laws regarding:

*   **Separation of Concerns**: Preventing mixing transient data with semantic knowledge.
*   **Single Source of Truth**: Code as truth, documentation as why, the wiki as index.
*   **Visibility**: Requiring Pydantic models for I/O contracts and comprehensive docstrings.
*   **Life Cycle**: Defining the lifespan and purpose of different document types.
*   **Orthogonality**: Ensuring new components don't clash with existing ones.
*   **Immutability**: Protecting the `raw/` directory as a seed.
*   **Atomic Transclusion**: Enforcing DRY principles in documentation.

## 🔄 Closed-Loop Development & Orthogonality

`wikipu` enforces a **Closed-Loop Development** process, especially for AI agents. Before any new code is written, a `TopologyProposal` must be submitted to the compiler. The compiler checks for **Orthogonality** using a "collision matrix," ensuring the proposed module's I/O and semantics do not clash with existing components. This prevents redundant or conflicting designs.

## 🍪 Single Source of Truth & Transclusion

The `wiki_compiler` processes source Markdown files (located in `wiki/`) that can contain `![[transclusion]]` syntax or standard Markdown links. The `wiki/` directory acts as the single source of truth for both humans and machines. YAML frontmatter is used to declare node characteristics cleanly, maintaining the DRY principle for documentation.

By combining these elements, `wikipu` provides a dynamic, auditable, and intelligent framework for managing complex software projects.
