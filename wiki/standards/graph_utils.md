---
identity:
  node_id: "doc:wiki/standards/graph_utils.md"
  node_type: "doc_standard"
edges:
  - target_id: "file:src/wiki_compiler/graph_utils.py"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/graph_utils.py:add_knowledge_node"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/graph_utils.py:load_graph"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/graph_utils.py:save_graph"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/graph_utils.py:load_knowledge_node"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/graph_utils.py:iter_knowledge_nodes"
    relation_type: documents
---

Provides utility functions for manipulating and persisting the Knowledge Graph. This module handles the integration of KnowledgeNodes into NetworkX graphs and their serialization to/from JSON.

## Rule Schema

```python
def add_knowledge_node(graph: nx.DiGraph, node: KnowledgeNode) -> None: ...
def load_graph(graph_path: Path) -> nx.DiGraph: ...
def save_graph(graph: nx.DiGraph, graph_path: Path) -> None: ...
def load_knowledge_node(graph: nx.DiGraph, node_id: str) -> KnowledgeNode: ...
def iter_knowledge_nodes(graph: nx.DiGraph) -> list[KnowledgeNode]: ...
```

## Fields

This module provides functions and does not define public classes or fields.

## Usage Examples

```python
from pathlib import Path
import networkx as nx
from wiki_compiler.graph_utils import load_graph, save_graph, add_knowledge_node

# Load a graph
graph = load_graph(Path("knowledge_graph.json"))

# Add a new node
# add_knowledge_node(graph, my_node)

# Save the graph
save_graph(graph, Path("knowledge_graph.json"))
```
