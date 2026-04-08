---
identity:
  node_id: "doc:wiki/how_to_add_component.md"
  node_type: "doc_standard"
edges: []
---

# ➕ How to Add a Component in `wikipu`

Adding new modules or components to a `wikipu`-managed repository is a structured process designed to ensure architectural integrity, prevent conflicts, and facilitate both human and AI understanding. This guide outlines the steps, emphasizing compliance with the `[[00_house_rules]]`.

## 1. Design with `TopologyProposal` (For Agents)

For AI agents, the first step is to design the new component's "topology" by creating a `TopologyProposal`. This Pydantic model (`![[TopologyProposal]]`) defines the module's name, intent, I/O ports, and any glossary terms used.

This proposal acts as a blueprint that `wiki-compiler` evaluates for orthogonality against the existing [[Knowledge Graph]].

## 2. Scaffold the Module

Once the `TopologyProposal` is approved (for agents) or the design is finalized (for humans), use the `wiki-compiler scaffold` command. This ensures the component starts with the correct directory structure and essential files, adhering to the `[[00_house_rules#Law of Structural Integrity (Scaffolding CLI)]]`.

```bash
wiki-compiler scaffold --module src/my_new_feature --intent "Processes incoming data from API"
```

This command will create:
*   `src/my_new_feature/contracts.py`: For defining `Pydantic` models for inputs and outputs.
*   `src/my_new_feature/__init__.py`: The module's public interface.
*   `src/my_new_feature/README.md`: The `KnowledgeNode` for your module, with YAML frontmatter.

## 3. Define Contracts in `contracts.py`

Inside `src/my_new_feature/contracts.py`, define your `Pydantic` models for the component's inputs and outputs. This is crucial for adhering to the `[[00_house_rules#Law of Code Visibility]]`.

```python
# src/my_new_feature/contracts.py
from pydantic import BaseModel

class MyNewFeatureInput(BaseModel):
    data: str
    # ... other input fields

class MyNewFeatureOutput(BaseModel):
    processed_data: str
    # ... other output fields
```

## 4. Implement Logic

Write the core business logic of your component. Remember to:

*   **Follow `[[00_house_rules]]`**: Especially regarding the separation of state and semantics.
*   **Use Type Hints**: Ensure clarity and allow `wiki-compiler` to extract AST-based `Facets`.
*   **Write Docstrings**: Every public class and function should have a comprehensive docstring, which feeds into the `SemanticFacet` of your `KnowledgeNode`.

## 5. Update Your Module's `README.md` (Knowledge Node)

The `README.md` in your module's root directory is its `KnowledgeNode`. Update its YAML frontmatter and Markdown body:

*   **YAML Frontmatter**:
    *   `identity`: Update `node_id` and `node_type` if necessary.
    *   `edges`: Add `depends_on`, `reads_from`, `writes_to`, `documents` edges to other nodes (e.g., other modules, ADRs, glossary terms).
    *   `io_ports`: Detail the `IOFacet` for your module, specifying `medium`, `schema_ref`, and `path_template`.
    *   `compliance`: Update the `status` as you progress (`scaffolding`, `implemented`, `tested`). If an exemption is needed, use `exemption_reason` and the `@wiki_exempt` decorator (`![[wiki_exempt]]`).
*   **Markdown Body**:
    *   Clearly describe the component's intent.
    *   Use `![[transclusions]]` for shared concepts to maintain DRY documentation.
    *   Reference relevant `[[ADRs]]` and `[[00_house_rules]]` sections.

## 6. Build and Verify

After implementing and documenting, run `wiki-compiler build` to:

*   Rebuild the `knowledge_graph.json` for AI agents.
*   Update the `.compliance_baseline.json` to ensure rules are met.

This step is typically integrated into your CI/CD pipeline (`[[00_house_rules#The CI/CD Guardian]]`) to ensure the graph is always up-to-date and compliant.
