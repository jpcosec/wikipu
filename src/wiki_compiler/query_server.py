from __future__ import annotations

import json
from pathlib import Path

import networkx as nx

from .graph_utils import load_graph, load_knowledge_node


def query_graph(
    graph_path: Path,
    query_type: str,
    node_id: str | None = None,
    relation_filter: str | None = None,
    medium: str | None = None,
    schema_ref: str | None = None,
    path_template: str | None = None,
) -> dict[str, object]:
    graph = load_graph(graph_path)
    if query_type == "get_node":
        ensure_node(node_id)
        return {
            "query_type": query_type,
            "node": load_knowledge_node(graph, node_id).model_dump(),
        }
    if query_type == "get_ancestors":
        ensure_node(node_id)
        filtered = filter_graph_by_relation(graph, relation_filter)
        nodes = sorted(nx.ancestors(filtered, node_id))
        return {
            "query_type": query_type,
            "nodes": [
                load_knowledge_node(graph, value).model_dump() for value in nodes
            ],
        }
    if query_type == "get_descendants":
        ensure_node(node_id)
        filtered = filter_graph_by_relation(graph, relation_filter)
        nodes = sorted(nx.descendants(filtered, node_id))
        return {
            "query_type": query_type,
            "nodes": [
                load_knowledge_node(graph, value).model_dump() for value in nodes
            ],
        }
    if query_type == "find_by_io":
        matches = []
        for candidate in graph.nodes:
            node = load_knowledge_node(graph, candidate)
            if any(
                matches_io(port, medium, schema_ref, path_template)
                for port in node.io_ports
            ):
                matches.append(node.model_dump())
        return {"query_type": query_type, "nodes": matches}
    raise ValueError(f"Unsupported query type: {query_type}")


def filter_graph_by_relation(
    graph: nx.DiGraph, relation_filter: str | None
) -> nx.DiGraph:
    if not relation_filter:
        return graph
    filtered = nx.DiGraph()
    filtered.add_nodes_from(graph.nodes(data=True))
    for source, target, data in graph.edges(data=True):
        if data.get("relation") == relation_filter:
            filtered.add_edge(source, target, **data)
    return filtered


def matches_io(
    port: object, medium: str | None, schema_ref: str | None, path_template: str | None
) -> bool:
    values = port.model_dump() if hasattr(port, "model_dump") else dict(port)
    return (
        (medium is None or values.get("medium") == medium)
        and (schema_ref is None or values.get("schema_ref") == schema_ref)
        and (path_template is None or values.get("path_template") == path_template)
    )


def ensure_node(node_id: str | None) -> str:
    if not node_id:
        raise ValueError("node_id is required for this query type")
    return node_id


def query_main(
    graph_path: Path,
    query_type: str,
    node_id: str | None = None,
    relation_filter: str | None = None,
    medium: str | None = None,
    schema_ref: str | None = None,
    path_template: str | None = None,
) -> None:
    result = query_graph(
        graph_path=graph_path,
        query_type=query_type,
        node_id=node_id,
        relation_filter=relation_filter,
        medium=medium,
        schema_ref=schema_ref,
        path_template=path_template,
    )
    payload = json.loads(json.dumps(result, default=serialize_model))
    print(json.dumps(payload, indent=2))


def serialize_model(value: object) -> object:
    if hasattr(value, "model_dump"):
        return value.model_dump()
    raise TypeError(f"Object of type {type(value)!r} is not JSON serializable")
