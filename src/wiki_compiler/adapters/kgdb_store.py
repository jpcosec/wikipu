"""Adapter for kgdb graph storage operations."""

from kgdb.graph import (
    add_knowledge_node,
    iter_knowledge_nodes,
    load_graph,
    load_knowledge_node,
    save_graph,
)

__all__ = [
    "add_knowledge_node",
    "iter_knowledge_nodes",
    "load_graph",
    "load_knowledge_node",
    "save_graph",
]
