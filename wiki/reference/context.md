---
identity:
  node_id: "doc:wiki/reference/context.md"
  node_type: "doc_standard"
edges:
  - target_id: "file:src/wiki_compiler/context.py"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/context.py:render_context"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/context.py:match_nodes_from_task"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/context.py:collect_neighborhood"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/context.py:render_markdown"
    relation_type: documents
---

Context rendering for the Knowledge Graph. Extracts and formats neighborhoods around specific nodes for LLM context generation.

## Rule Schema

```python
def render_context(
    graph_path: Path,
    node_ids: list[str] | None = None,
    task_hint: str | None = None,
    depth: int = 1,
    output_format: str = "markdown",
    include_planned: bool = False,
) -> str
```

## Fields

- `graph_path`: Path to the `knowledge_graph.json` file.
- `node_ids`: Explicit list of node IDs to include in the context.
- `task_hint`: Natural language string used to heuristically find relevant nodes.
- `depth`: How many hops to traverse from the starting nodes.

## Usage Examples

```python
from pathlib import Path
from wiki_compiler.context import render_context

context = render_context(
    graph_path=Path("knowledge_graph.json"),
    task_hint="Explain the build process",
    depth=2
)
print(context)
```
