---
identity:
  node_id: "doc:wiki/drafts/task_7_graph_builder.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Create: `src/doc_router/graph.py`
- Create: `tests/test_graph.py`

- [ ] **Step 1: Write failing tests**

```python
# tests/test_graph.py
"""Tests for graph builder."""

from pathlib import Path

from doc_router.config import load_config
from doc_router.graph import build_graph
from doc_router.scanner.registry import scan_project


def test_build_graph_resolves_edges(sample_project_dir: Path) -> None:
    config = load_config(sample_project_dir / "doc-router.yml")
    nodes, edges = scan_project(sample_project_dir, config)
    graph, issues = build_graph(nodes, edges)
    assert len(graph.nodes) == 3
    # depends_on edge from design → architecture (both exist)
    dep_edges = [e for e in graph.edges if e.type == "depends_on"]
    assert len(dep_edges) == 1


def test_build_graph_detects_broken_implements(sample_project_dir: Path) -> None:
    config = load_config(sample_project_dir / "doc-router.yml")
    nodes, edges = scan_project(sample_project_dir, config)
    # design.md implements src/module.py — but the edge target is a path, not a node id
    # The builder should resolve path-based targets or flag them
    graph, issues = build_graph(nodes, edges)
    broken = [i for i in issues if i["type"] == "broken_link"]
    # src/module.py exists as a file but "src/module.py" is not a node id
    # The implements edge target "src/module.py::MatchLogic" should resolve to pipeline-match-impl
    # The bare "src/module.py" cannot resolve to a single node → broken
    assert any("src/module.py" in str(i.get("target", "")) for i in broken)


def test_build_graph_detects_duplicate_ids() -> None:
    from doc_router.models import RouteNode, RouteEdge

    nodes = [
        RouteNode(id="dup", type="doc", path="a.md", domain="ui", nature="impl"),
        RouteNode(id="dup", type="doc", path="b.md", domain="ui", nature="impl"),
    ]
    graph, issues = build_graph(nodes, [])
    dups = [i for i in issues if i["type"] == "duplicate_id"]
    assert len(dups) == 1


def test_build_graph_stats() -> None:
    from doc_router.models import RouteNode

    nodes = [
        RouteNode(id="a", type="doc", path="a.md", domain="ui", nature="impl"),
        RouteNode(id="b", type="code", path="b.py", domain="pipeline", nature="impl"),
    ]
    graph, issues = build_graph(nodes, [])
    assert len(graph.nodes) == 2
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_graph.py -v`
Expected: FAIL

- [ ] **Step 3: Implement graph builder**

```python
# src/doc_router/graph.py
"""Build and validate the route graph from scanned entities."""

from __future__ import annotations

from doc_router.models import RouteEdge, RouteGraph, RouteNode

Issue = dict[str, str]


def build_graph(
    nodes: list[RouteNode],
    edges: list[RouteEdge],
) -> tuple[RouteGraph, list[Issue]]:
    issues: list[Issue] = []

    # Check duplicate IDs
    seen_ids: dict[str, str] = {}
    unique_nodes: list[RouteNode] = []
    for node in nodes:
        if node.id in seen_ids:
            issues.append({
                "type": "duplicate_id",
                "id": node.id,
                "paths": f"{seen_ids[node.id]}, {node.path}",
            })
        else:
            seen_ids[node.id] = node.path
            unique_nodes.append(node)

    # Build path-to-id index for resolving implements targets
    path_to_ids: dict[str, list[str]] = {}
    for node in unique_nodes:
        key = node.path
        path_to_ids.setdefault(key, []).append(node.id)
        if node.symbol:
            symbol_key = f"{node.path}::{node.symbol}"
            path_to_ids.setdefault(symbol_key, []).append(node.id)

    # Resolve and validate edges
    resolved_edges: list[RouteEdge] = []
    node_ids = {n.id for n in unique_nodes}

    for edge in edges:
        target = edge.target
        if target in node_ids:
            resolved_edges.append(edge)
        elif target in path_to_ids:
            # Resolve path to node id(s)
            for resolved_id in path_to_ids[target]:
                resolved_edges.append(
                    RouteEdge(source=edge.source, target=resolved_id, type=edge.type)
                )
        else:
            issues.append({
                "type": "broken_link",
                "source": edge.source,
                "target": target,
                "edge_type": edge.type,
            })

    return RouteGraph(nodes=unique_nodes, edges=resolved_edges), issues
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_graph.py -v`
Expected: 4 passed

- [ ] **Step 5: Commit**

```bash
git add src/doc_router/graph.py tests/test_graph.py
git commit -m "feat(doc-router): graph builder with edge resolution and validation"
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md`.