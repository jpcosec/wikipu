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
from .contracts import (
    ContextRequest,
    ContextBundle,
    Edge,
    KnowledgeNode,
    Checklist,
    ChecklistItem,
)


def get_context_bundle(graph_path: Path, request: ContextRequest) -> ContextBundle:
    """
    Graph-aware context routing with active issue intersection, checklists, and prose hydration.
    """
    graph = load_graph(graph_path)
    project_root = graph_path.parent

    # 1. Identify seeds (direct matches)
    seeds = set(request.node_ids)
    if request.task_hint:
        seeds.update(match_nodes_from_task(graph_path, request.task_hint))

    # 2. Score and categorize
    scores: dict[str, float] = {}
    rationale: dict[str, str] = {}
    subgraph_node_ids: set[str] = set()

    # Direct matches
    for node_id in seeds:
        if node_id in graph:
            scores[node_id] = 1.0
            rationale[node_id] = "direct_match"
            subgraph_node_ids.add(node_id)

    # Ancestors (dependencies)
    for node_id in list(subgraph_node_ids):
        for ancestor in collect_neighborhood_by_direction(
            graph, {node_id}, request.depth, direction="incoming"
        ):
            if ancestor not in subgraph_node_ids:
                subgraph_node_ids.add(ancestor)
                scores[ancestor] = 0.8
                rationale[ancestor] = f"ancestor_of_{node_id}"

    # Descendants (dependents)
    for node_id in list(seeds):
        for descendant in collect_neighborhood_by_direction(
            graph, {node_id}, request.depth, direction="outgoing"
        ):
            if descendant not in subgraph_node_ids:
                subgraph_node_ids.add(descendant)
                scores[descendant] = 0.6
                rationale[descendant] = f"descendant_of_{node_id}"

    # 3. Intersection (Tasks & Checklists)
    active_tasks = match_active_tasks(
        project_root, subgraph_node_ids, request.task_hint
    )
    checklists = load_relevant_checklists(project_root, request.task_hint)

    # 4. Filter and Build Bundle
    nodes: list[KnowledgeNode] = []
    edges: list[Edge] = []
    prose: dict[str, str] = {}

    for node_id in sorted(subgraph_node_ids):
        node = load_knowledge_node(graph, node_id)
        if (
            node.compliance
            and node.compliance.status == "planned"
            and not request.include_planned
        ):
            continue

        nodes.append(node)

        # Hydrate prose for wiki nodes
        if node_id.startswith("doc:"):
            rel_path = node_id.removeprefix("doc:")
            abs_path = project_root / rel_path
            if abs_path.exists():
                prose[node_id] = abs_path.read_text(encoding="utf-8")

        for _, target, data in graph.out_edges(node_id, data=True):
            if target in subgraph_node_ids:
                edges.append(
                    Edge(
                        target_id=target,
                        relation_type=data.get("relation_type", "contains"),
                    )
                )

    return ContextBundle(
        nodes=nodes,
        edges=edges,
        rationale=rationale,
        scores=scores,
        active_issues=active_issues,
        checklists=checklists,
        prose=prose,
    )


def load_relevant_checklists(
    project_root: Path, task_hint: str | None
) -> list[Checklist]:
    """Parses checklists.md and selects those relevant to the task."""
    checklist_path = project_root / "wiki/standards/checklists.md"
    if not checklist_path.exists():
        return []

    content = checklist_path.read_text(encoding="utf-8")
    checklists: list[Checklist] = []

    kw_to_checklist = {
        "issue": "issue-resolution",
        "resolve": "issue-resolution",
        "wiki": "new-wiki-node",
        "node": "new-wiki-node",
        "module": "new-module",
        "topology": "new-module",
        "structure": "structural-change",
        "refactor": "structural-change",
        "session": "session-close",
        "finish": "session-close",
    }

    selected_names = set()
    if task_hint:
        for kw, name in kw_to_checklist.items():
            if kw in task_hint.lower():
                selected_names.add(name)

    if not selected_names:
        return []

    sections = re.split(r"### \d+\. ", content)
    for section in sections:
        match = re.match(r"(.*?) \(`(.*?)`\)", section)
        if match:
            title, name = match.groups()
            if name in selected_names:
                items = []
                item_matches = re.findall(
                    r"\d+\. \*\*(.*?)\*\* \((.*?)\) — .*?`Verification:` `(.*?)`",
                    section,
                    re.DOTALL,
                )
                for desc, rule, verify in item_matches:
                    items.append(
                        ChecklistItem(
                            description=desc, rule_id=rule, verification=verify
                        )
                    )

                checklists.append(Checklist(name=name, items=items))

    return checklists


def match_active_tasks(
    project_root: Path, subgraph_node_ids: set[str], task_hint: str | None
) -> list[str]:
    """Finds active tasks in desk/tasks/ relevant to the current context."""
    tasks_dir = project_root / "desk/tasks"
    if not tasks_dir.exists():
        return []

    relevant_issues: list[str] = []
    node_names = set()
    for node_id in subgraph_node_ids:
        node_names.add(node_id)
        if ":" in node_id:
            val = node_id.split(":", 1)[1]
            node_names.add(val)
            stem = Path(val).stem
            if len(stem) > 3:
                node_names.add(stem)

    for issue_file in issues_dir.rglob("*.md"):
        content = issue_file.read_text(encoding="utf-8").lower()
        rel_issue = issue_file.relative_to(project_root).as_posix()

        matched = False
        for name in node_names:
            if name.lower() in content:
                relevant_issues.append(rel_issue)
                matched = True
                break
        if matched:
            continue

        if task_hint:
            terms = [
                t.lower() for t in re.findall(r"[a-z0-9_]+", task_hint) if len(t) > 3
            ]
            if any(term in content for term in terms):
                relevant_issues.append(rel_issue)

    return sorted(list(set(relevant_issues)))


def collect_neighborhood_by_direction(
    graph, starting_nodes: set[str], depth: int, direction: str
) -> set[str]:
    """Collect nodes within a given depth and direction (in/out) from starting nodes."""
    visited = set()
    queue = deque((node_id, 0) for node_id in starting_nodes)
    while queue:
        node_id, level = queue.popleft()
        if level >= depth:
            continue

        neighbors = set()
        if direction == "incoming":
            neighbors = set(graph.predecessors(node_id))
        elif direction == "outgoing":
            neighbors = set(graph.successors(node_id))
        else:
            neighbors = set(graph.predecessors(node_id)) | set(
                graph.successors(node_id)
            )

        for neighbor in neighbors:
            if neighbor not in visited and neighbor not in starting_nodes:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))
    return visited


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
    request = ContextRequest(
        node_ids=node_ids or [],
        task_hint=task_hint,
        depth=depth,
        include_planned=include_planned,
    )
    bundle = get_context_bundle(graph_path, request)

    if output_format == "json":
        return bundle.model_dump_json(indent=2)
    return render_markdown_bundle(bundle)


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
    Legacy helper for backward compatibility.
    """
    return collect_neighborhood_by_direction(
        graph, set(starting_nodes), depth, direction="both"
    ) | set(starting_nodes)


def render_markdown_bundle(bundle: ContextBundle) -> str:
    """
    Formats a ContextBundle into a structured Markdown representation.
    """
    blocks: list[str] = []

    if bundle.active_issues:
        blocks.append(
            "## Relevant Active Issues\n"
            + "\n".join(f"- `{i}`" for i in bundle.active_issues)
        )

    if bundle.checklists:
        cl_blocks = ["## Verification Checklists"]
        for cl in bundle.checklists:
            cl_blocks.append(f"### {cl.name}")
            for item in cl.items:
                rule_info = f" ({item.rule_id})" if item.rule_id else ""
                cl_blocks.append(f"- [ ] **{item.description}**{rule_info}")
                if item.verification:
                    cl_blocks.append(f"  - `Verification:` `{item.verification}`")
        blocks.append("\n".join(cl_blocks))

    for node in bundle.nodes:
        node_id = node.identity.node_id
        lines = [f"## `{node_id}`"]
        lines.append(f"- type: `{node.identity.node_type}`")
        if node.compliance and node.compliance.status:
            lines.append(f"- status: `{node.compliance.status}`")

        reason = bundle.rationale.get(node_id, "unknown")
        score = bundle.scores.get(node_id, 0.0)
        lines.append(f"- routing: {reason} (score: {score:.2f})")

        if node_id in bundle.prose:
            # Extract content between frontmatter separators
            full_prose = bundle.prose[node_id]
            body = re.sub(
                r"\A---\s*\n.*?\n---(\s*\n|$)", "", full_prose, flags=re.DOTALL
            ).strip()
            lines.append("\n" + body)
        elif node.semantics and node.semantics.intent:
            lines.append(f"- intent: {node.semantics.intent}")

        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)
