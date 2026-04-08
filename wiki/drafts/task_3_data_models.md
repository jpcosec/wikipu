---
identity:
  node_id: "doc:wiki/drafts/task_3_data_models.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Create: `src/doc_router/models.py`
- Create: `tests/test_models.py`

- [ ] **Step 1: Write failing tests for models**

```python
# tests/test_models.py
"""Tests for core data models."""

from doc_router.models import RouteNode, RouteEdge, RouteGraph


def test_route_node_creation() -> None:
    node = RouteNode(
        id="pipeline-match-design",
        type="doc",
        path="docs/product/match.md",
        domain="pipeline",
        stage="match",
        nature="philosophy",
        version="2026-03-22",
    )
    assert node.id == "pipeline-match-design"
    assert node.type == "doc"
    assert node.symbol is None


def test_route_node_code_with_symbol() -> None:
    node = RouteNode(
        id="pipeline-match-impl",
        type="code",
        path="src/nodes/match/logic.py",
        domain="pipeline",
        stage="match",
        nature="implementation",
        symbol="MatchLogic",
        tags={"hitl_gate": "review_match", "contract": "src/nodes/match/contract.py::MatchInput"},
    )
    assert node.symbol == "MatchLogic"
    assert node.tags["hitl_gate"] == "review_match"


def test_route_graph_serialization() -> None:
    node = RouteNode(
        id="test-node",
        type="doc",
        path="docs/test.md",
        domain="core",
        nature="philosophy",
    )
    edge = RouteEdge(source="test-node", target="other-node", type="depends_on")
    graph = RouteGraph(nodes=[node], edges=[edge])

    data = graph.to_dict()
    assert len(data["nodes"]) == 1
    assert len(data["edges"]) == 1
    assert data["nodes"][0]["id"] == "test-node"

    restored = RouteGraph.from_dict(data)
    assert restored.nodes[0].id == "test-node"
    assert restored.edges[0].type == "depends_on"


def test_route_graph_filter_by_domain() -> None:
    nodes = [
        RouteNode(id="a", type="doc", path="a.md", domain="ui", nature="impl"),
        RouteNode(id="b", type="doc", path="b.md", domain="pipeline", nature="impl"),
    ]
    graph = RouteGraph(nodes=nodes, edges=[])
    filtered = graph.filter(domain="ui")
    assert len(filtered.nodes) == 1
    assert filtered.nodes[0].id == "a"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_models.py -v`
Expected: FAIL — `ModuleNotFoundError`

- [ ] **Step 3: Implement models**

```python
# src/doc_router/models.py
"""Core data models for the route graph."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RouteNode:
    id: str
    type: str  # "doc" or "code"
    path: str
    domain: str
    nature: str
    stage: str = "global"
    version: str | None = None
    symbol: str | None = None
    tags: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "type": self.type,
            "path": self.path,
            "domain": self.domain,
            "stage": self.stage,
            "nature": self.nature,
            "version": self.version,
            "symbol": self.symbol,
            "tags": self.tags,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> RouteNode:
        return cls(**data)


@dataclass
class RouteEdge:
    source: str
    target: str
    type: str  # "implements", "doc-ref", "depends_on", "contract"

    def to_dict(self) -> dict[str, Any]:
        return {"source": self.source, "target": self.target, "type": self.type}

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> RouteEdge:
        return cls(**data)


@dataclass
class RouteGraph:
    nodes: list[RouteNode]
    edges: list[RouteEdge]

    def to_dict(self) -> dict[str, Any]:
        return {
            "nodes": [n.to_dict() for n in self.nodes],
            "edges": [e.to_dict() for e in self.edges],
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> RouteGraph:
        return cls(
            nodes=[RouteNode.from_dict(n) for n in data["nodes"]],
            edges=[RouteEdge.from_dict(e) for e in data["edges"]],
        )

    def filter(
        self,
        domain: str | None = None,
        stage: str | None = None,
        nature: str | None = None,
    ) -> RouteGraph:
        filtered = self.nodes
        if domain:
            filtered = [n for n in filtered if n.domain == domain]
        if stage:
            filtered = [n for n in filtered if n.stage == stage]
        if nature:
            filtered = [n for n in filtered if n.nature == nature]
        node_ids = {n.id for n in filtered}
        edges = [e for e in self.edges if e.source in node_ids or e.target in node_ids]
        return RouteGraph(nodes=filtered, edges=edges)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_models.py -v`
Expected: 4 passed

- [ ] **Step 5: Commit**

```bash
git add src/doc_router/models.py tests/test_models.py
git commit -m "feat(doc-router): core data models for route graph"
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md`.