---
identity:
  node_id: "doc:wiki/how_to_use.md"
  node_type: "doc_standard"
edges: []
---

# 🚀 How to Use `wikipu`

The `llm-wiki-compiler` provides a Command Line Interface (CLI) to manage your knowledge graph ecosystem. It's designed for both human developers and integrated AI agents to interact with the project's architecture.

## 📦 Installation

To make the `wiki-compiler` available globally in your terminal, navigate to the root of the `llm-wiki-compiler` repository and install it in editable mode:

```bash
pip install -e .
```

This will link the `wiki-compiler` command to the `main.py` script, allowing you to use it from any directory.

## 🛠️ CLI Commands

Here are the primary commands available through the `wiki-compiler` CLI:

### `wiki-compiler init`

Initializes the base directory structure required by the `[[00_house_rules]]`. This command sets up essential folders for raw data, documentation, wiki nodes, and concepts, ensuring your repository adheres to the foundational structure.

```bash
wiki-compiler init
```

**Purpose:** To set up a new or existing repository to be compliant with `wikipu`'s directory structure.
**Output:** Creates directories like `raw/`, `wiki/adrs/`, `wiki/`, `wiki/concepts/`.

### `wiki-compiler scaffold --module <PATH> --intent "<INTENT>"`

Generates the boilerplate (skeleton) for a new module within your `src/` directory. This ensures that every new component starts with the mandatory files (`contracts.py`, `__init__.py`, `README.md`) and basic YAML frontmatter, adhering to the `[[00_house_rules#Law of Structural Integrity (Scaffolding CLI)]]`.

```bash
wiki-compiler scaffold --module src/my_new_module --intent "Handles user authentication"
```

*   `<PATH>`: The relative path to the new module (e.g., `src/data_processor`).
*   `<INTENT>`: A brief, high-level description of the module's purpose.

**Purpose:** To quickly and compliantly create the initial structure for any new component, saving time and enforcing standards.
**Output:** Creates the specified module directory with `contracts.py`, `__init__.py`, and a `README.md` (which serves as its `KnowledgeNode`).

### `wiki-compiler build --source <SOURCE_DIR> --graph <GRAPH_PATH>`

Parses the Wiki source files (Markdown with YAML frontmatter) and generates the project's machine-readable Knowledge Graph (NetworkX JSON) and compliance baseline.

```bash
wiki-compiler build --source wiki --graph knowledge_graph.json
```

*   `<SOURCE_DIR>`: The directory containing your Wiki's source Markdown files (e.g., `wiki`).
*   `<GRAPH_PATH>`: The path where the NetworkX JSON representation of the Knowledge Graph will be saved (e.g., `knowledge_graph.json`).

**Purpose:** To keep the AI agents provided with a comprehensive, machine-readable graph of the repository's architecture and knowledge. This command is typically run in CI/CD pipelines.
**Output:** A `knowledge_graph.json` file and a `.compliance_baseline.json` file.
