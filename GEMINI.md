# GEMINI Context for Wikipu

This document provides a comprehensive overview of the Wikipu repository, designed to be used as instructional context for Gemini.

## Project Overview

**Wikipu** is a self-contained **Seed Repository** and **Development Operating System** designed for human-AI collaboration. Its primary purpose is to "compile" knowledge from various project sources (source code, documentation, raw notes) into a unified, machine-readable **Knowledge Graph** (`knowledge_graph.json`).

This graph serves as a single source of truth that can be queried by both humans and AI agents to understand the codebase, enforce architectural principles, and guide development with full context.

### Core Concepts

*   **Knowledge Graph (Meta-Graph):** A `networkx` graph representing the entire repository. It's composed of **Knowledge Nodes** and **Edges**.
*   **Knowledge Nodes:** Represent every significant element (files, functions, concepts, standards). Each node has a unique ID and can be enriched with **Facets**.
*   **Facets:** Optional Pydantic models that add "dimensions" of information to a node, such as `ASTFacet` (code structure), `IOFacet` (data flows), `SemanticFacet` (intent), and `ComplianceFacet` (status).
*   **The 4-Place Design:** The repository is organized into four distinct zones to manage the flow of information over time:
    *   **`raw/` (Source/Origin):** Immutable "seed" content like brainstorming notes and external documents.
    *   **`wiki/` (Past/Truth):** The curated, living documentation and standards. The single source of truth.
    *   **`plan_docs/` (Present/Doing):** Ephemeral plans for active work. Deleted upon completion.
    *   **`future_docs/` (Future/Waiting):** A backlog for ideas not yet in progress.

## Building and Running

This is a Python project managed with `setuptools`. The core functionality is exposed through the `wiki-compiler` command-line tool.

### Installation

To make the `wiki-compiler` command available in your environment, install the project in editable mode from the root directory:

```bash
pip install -e .
```

### Key Commands

The main entry point is `src/wiki_compiler/main.py`, which provides the following commands:

*   **`wiki-compiler init`**: Initializes the repository with the required directory structure (`raw/`, `wiki/`, etc.).
*   **`wiki-compiler build`**: The primary command. It scans the `wiki/` and `src/` directories, builds the knowledge graph, saves it to `knowledge_graph.json`, and checks for compliance with house rules.
*   **`wiki-compiler ingest`**: Processes files from the `raw/` directory to create draft documentation nodes in `wiki/drafts/`.
*   **`wiki-compiler audit`**: Runs quality and compliance checks against the existing knowledge graph and reports findings.
*   **`wiki-compiler scaffold`**: Generates boilerplate for a new Python module, including the necessary file structure and contracts.
*   **`wiki-compiler query`**: Allows for querying the knowledge graph to find nodes, traverse relationships, and get information about the codebase.
*   **`wiki-compiler validate`**: Validates a `TopologyProposal` to ensure a proposed new module is "orthogonal" and doesn't conflict with existing components.

## Development Conventions

The project's development process is governed by a strict set of rules defined in `wiki/standards/00_house_rules.md`. These rules are enforced by the `wiki-compiler` and are critical for maintaining the integrity of the knowledge graph.

### Core Principles

*   **Orthogonality (ID-1):** No two elements should do the same thing. New modules must be validated for non-overlap before creation using `wiki-compiler validate`.
*   **Typed Contracts at Every Boundary (ID-3):** All data crossing a process boundary (e.g., between modules) **must** be a typed Pydantic model. `Field(description=...)` is mandatory, as LLMs read these descriptions.
*   **Zone Separation (ID-4):** The four information zones (`raw`, `wiki`, `plan_docs`, `future_docs`) are inviolable and have strict rules about how they can interact.
*   **Code Style (CS-1 to CS-10):**
    *   All modules must have `from __future__ import annotations`.
    *   Modules and public functions/classes require structured docstrings.
    *   Pydantic models are the only way to pass data between modules.
    *   No silent error swallowing; log and re-raise.
    *   Update `changelog.md` on every significant change.
*   **Closed-Loop Development:** AI-driven or major structural changes require submitting a `TopologyProposal`. The system validates this proposal for orthogonality before any code is written, preventing redundant or conflicting designs.
