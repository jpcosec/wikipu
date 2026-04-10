---
identity:
  node_id: "doc:wiki/how_to/use_the_cli.md"
  node_type: "how_to"
compliance:
  status: "implemented"
  failing_standards: []
---

The `wiki-compiler` CLI is the deterministic entry point for all Wikipu operations — for both human developers and integrated AI agents. It exposes commands for initializing repository structure, scaffolding new modules, compiling the knowledge graph, and querying the graph at runtime.

# How to Use the CLI

The `wiki-compiler` CLI is the deterministic entry point for all Wikipu operations — for both human developers and integrated AI agents. It exposes commands for initializing repository structure, scaffolding new modules, compiling the knowledge graph, and querying the graph at runtime. Every structural operation in the ecosystem is invoked through this interface rather than performed by hand, ensuring that all changes are traceable, compliant, and reproducible.

## Prerequisites

- Python environment with `wiki-compiler` installed. From the repository root: `pip install -e .`
- This links the `wiki-compiler` command to `main.py` and makes it available from any directory.

## Steps

### Initialize a repository

1. Navigate to the root of the target repository.
2. Run `wiki-compiler init` to create the base directory structure required by `house_rules`: `raw/`, `wiki/`, `wiki/adrs/`, `wiki/concepts/`.

```bash
wiki-compiler init
```

### Scaffold a new module

3. Once a `TopologyProposal` for a new module is approved, run `wiki-compiler scaffold` to generate the required boilerplate:

```bash
wiki-compiler scaffold --module src/my_new_module --intent "Handles user authentication"
```

- `--module`: Relative path to the new module (e.g., `src/data_processor`).
- `--intent`: One-sentence description of the module's purpose.

This creates: `contracts.py` (Pydantic input/output models), `__init__.py` (public interface), and `README.md` (the module's `KnowledgeNode` with YAML frontmatter).

### Build the knowledge graph

4. After adding or modifying wiki nodes or source code, compile the knowledge graph:

```bash
wiki-compiler build --source wiki --graph knowledge_graph.json
```

- `--source`: Directory containing wiki Markdown files (default: `wiki`).
- `--graph`: Output path for the NetworkX JSON knowledge graph (default: `knowledge_graph.json`).

This also produces `.compliance_baseline.json`. Run this command in CI/CD pipelines to keep the graph current and compliance checks enforced.

### Query the knowledge graph

5. Retrieve or traverse graph nodes at runtime:

```bash
wiki-compiler query --type get_node --node-id doc:wiki/how_to/use_the_cli.md
wiki-compiler query --type get_ancestors --node-id file:src/wiki_compiler/contracts.py
wiki-compiler query --type get_descendants --node-id dir:src/wiki_compiler
```

Supported query types: `get_node`, `get_ancestors`, `get_descendants`, `find_by_io`.

## Verification

- [ ] `wiki-compiler --help` prints the command list without errors after installation.
- [ ] `wiki-compiler init` creates `raw/`, `wiki/`, `wiki/adrs/`, and `wiki/concepts/` directories.
- [ ] `wiki-compiler scaffold` creates `contracts.py`, `__init__.py`, and `README.md` under the specified module path.
- [ ] `wiki-compiler build` produces `knowledge_graph.json` and `.compliance_baseline.json` without parse errors.
- [ ] `wiki-compiler query --type get_node --node-id <id>` returns the node schema for a known node ID.
