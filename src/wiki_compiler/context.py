"""
Context rendering for the Knowledge Graph.
Extracts and formats neighborhoods around specific nodes for LLM context generation.
"""
from __future__ import annotations

import json
import re
from collections import deque
from pathlib import Path

from .graph_utils import load_graph, load_knowledge_node


def render_context(
    graph_path: Path,
    node_ids: list[str] | None = None,
    task_hint: str | None = None,
    depth: int = 1,
    output_format: str = "markdown",
    include_planned: bool = False,
) -> str:
    """
    Renders a subset of the Knowledge Graph into a human-readable or machine-parsable context.
    """
    graph = load_graph(graph_path)
    selected = node_ids or match_nodes_from_task(graph_path, task_hint)
    subgraph_nodes = collect_neighborhood(graph, selected, depth)
    payload = []
    for node_id in sorted(subgraph_nodes):
        node = load_knowledge_node(graph, node_id)
        status = node.compliance.status if node.compliance else None
        if status == "planned" and not include_planned:
            continue
        payload.append(
            {
                "node": node.model_dump(),
                "edges": [
                    {
                        "target": target,
                        "relation": data.get("relation"),
                    }
                    for _, target, data in graph.out_edges(node_id, data=True)
                    if target in subgraph_nodes
                ],
            }
        )
    if output_format == "json":
        return json.dumps(payload, indent=2)
    return render_markdown(payload)


def match_nodes_from_task(graph_path: Path, task_hint: str | None) -> list[str]:
    """
    Identifies relevant Knowledge Graph nodes based on a natural language task description.
    """
    if not task_hint:
        raise ValueError("Provide node_ids or a task_hint")
    graph = load_graph(graph_path)
    terms = {
        token
        for token in re.findall(r"[a-z0-9_]+", task_hint.lower())
        if len(token) > 2
    }
    scored: list[tuple[int, str]] = []
    for node_id in graph.nodes:
        node = load_knowledge_node(graph, node_id)
        haystack = " ".join(
            [
                node.identity.node_id,
                node.semantics.intent if node.semantics else "",
                " ".join(node.ast.signatures if node.ast else []),
            ]
        ).lower()
        score = sum(1 for term in terms if term in haystack)
        if score:
            scored.append((score, node_id))
    return [node_id for _, node_id in sorted(scored, reverse=True)[:3]]


def collect_neighborhood(graph, starting_nodes: list[str], depth: int) -> set[str]:
    """
    Expands a set of starting nodes by traversing the graph up to a specified depth.
    """
    visited = set(starting_nodes)
    queue = deque((node_id, 0) for node_id in starting_nodes)
    while queue:
        node_id, level = queue.popleft()
        if level >= depth:
            continue
        neighbors = set(graph.predecessors(node_id)) | set(graph.successors(node_id))
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            queue.append((neighbor, level + 1))
    return visited


def render_markdown(payload: list[dict[str, object]]) -> str:
    """
    Formats a list of node payloads into a structured Markdown representation.
    """
    blocks: list[str] = []
    for item in payload:
        node = item["node"]
        identity = node["identity"]
        semantics = node.get("semantics") or {}
        ast = node.get("ast") or {}
        compliance = node.get("compliance") or {}
        lines = [f"## `{identity['node_id']}`"]
        lines.append(f"- type: `{identity['node_type']}`")
        if compliance.get("status"):
            lines.append(f"- status: `{compliance['status']}`")
        if semantics.get("intent"):
            lines.append(f"- intent: {semantics['intent']}")
        signatures = ast.get("signatures") or []
        if signatures:
            lines.append(
                f"- signatures: {', '.join(f'`{value}`' for value in signatures)}"
            )
        edges = item["edges"]
        if edges:
            edge_lines = ", ".join(
                f"{edge['relation']} -> `{edge['target']}`" for edge in edges
            )
            lines.append(f"- edges: {edge_lines}")
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)
