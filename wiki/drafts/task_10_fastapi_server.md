---
identity:
  node_id: "doc:wiki/drafts/task_10_fastapi_server.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Create: `src/doc_router/server.py`
- Create: `tests/test_server.py`

- [ ] **Step 1: Write failing tests**

```python
# tests/test_server.py
"""Tests for FastAPI server."""

from pathlib import Path

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from doc_router.server import create_app


@pytest.fixture
def app(sample_project_dir: Path):
    return create_app(project_root=sample_project_dir)


@pytest_asyncio.fixture
async def client(app):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest.mark.asyncio
async def test_get_graph(client) -> None:
    resp = await client.get("/api/graph")
    assert resp.status_code == 200
    data = resp.json()
    assert "nodes" in data
    assert "edges" in data
    assert len(data["nodes"]) == 3


@pytest.mark.asyncio
async def test_get_graph_filtered(client) -> None:
    resp = await client.get("/api/graph", params={"domain": "core"})
    assert resp.status_code == 200
    data = resp.json()
    assert len(data["nodes"]) == 1
    assert data["nodes"][0]["domain"] == "core"


@pytest.mark.asyncio
async def test_get_stats(client) -> None:
    resp = await client.get("/api/stats")
    assert resp.status_code == 200
    data = resp.json()
    assert "total_nodes" in data
    assert data["total_nodes"] == 3


@pytest.mark.asyncio
async def test_get_node_detail(client) -> None:
    resp = await client.get("/api/nodes/pipeline-match-design")
    assert resp.status_code == 200
    data = resp.json()
    assert data["node"]["id"] == "pipeline-match-design"
    assert "connected_edges" in data


@pytest.mark.asyncio
async def test_get_node_not_found(client) -> None:
    resp = await client.get("/api/nodes/nonexistent")
    assert resp.status_code == 404
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_server.py -v`
Expected: FAIL

- [ ] **Step 3: Implement server**

```python
# src/doc_router/server.py
"""FastAPI server for doc-router graph API and static UI."""

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from doc_router.config import load_config
from doc_router.graph import build_graph
from doc_router.models import RouteGraph
from doc_router.scanner.registry import scan_project


def create_app(project_root: Path | None = None) -> FastAPI:
    app = FastAPI(title="Doc-Router", version="0.1.0")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Build graph on startup
    root = project_root or Path.cwd()
    config = load_config(root / "doc-router.yml")
    nodes, edges = scan_project(root, config)
    graph, issues = build_graph(nodes, edges)

    # Store in app state
    app.state.graph = graph
    app.state.issues = issues
    app.state.config = config

    @app.get("/api/graph")
    def get_graph(
        domain: str | None = None,
        stage: str | None = None,
        nature: str | None = None,
    ):
        filtered = app.state.graph.filter(domain=domain, stage=stage, nature=nature)
        return filtered.to_dict()

    @app.get("/api/stats")
    def get_stats():
        g: RouteGraph = app.state.graph
        return {
            "total_nodes": len(g.nodes),
            "doc_nodes": sum(1 for n in g.nodes if n.type == "doc"),
            "code_nodes": sum(1 for n in g.nodes if n.type == "code"),
            "total_edges": len(g.edges),
            "issues": len(app.state.issues),
            "domains": sorted({n.domain for n in g.nodes}),
            "stages": sorted({n.stage for n in g.nodes}),
        }

    @app.get("/api/nodes/{node_id}")
    def get_node(node_id: str):
        g: RouteGraph = app.state.graph
        node = next((n for n in g.nodes if n.id == node_id), None)
        if not node:
            raise HTTPException(404, f"Node not found: {node_id}")
        connected = [e for e in g.edges if e.source == node_id or e.target == node_id]
        return {
            "node": node.to_dict(),
            "connected_edges": [e.to_dict() for e in connected],
        }

    @app.post("/api/rescan")
    def rescan():
        nodes, edges = scan_project(root, config)
        new_graph, new_issues = build_graph(nodes, edges)
        app.state.graph = new_graph
        app.state.issues = new_issues
        return {"status": "ok", "nodes": len(new_graph.nodes)}

    # Mount static UI if built
    ui_dist = Path(__file__).parent.parent.parent / "ui" / "dist"
    if ui_dist.is_dir():
        app.mount("/", StaticFiles(directory=str(ui_dist), html=True), name="ui")

    return app
```

- [ ] **Step 4: Add serve command to CLI**

Add to `src/doc_router/cli.py`:

```python
@cli.command()
@click.option("--project", default=None, help="Project root (default: cwd)")
@click.option("--port", default=8030, help="Server port")
def serve(project: str | None, port: int) -> None:
    """Start UI and API server."""
    import uvicorn
    from doc_router.server import create_app

    root = Path(project) if project else Path.cwd()
    app = create_app(project_root=root)
    click.echo(f"Serving doc-router on http://127.0.0.1:{port}")
    uvicorn.run(app, host="127.0.0.1", port=port)
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python -m pytest tests/test_server.py -v`
Expected: 5 passed

- [ ] **Step 6: Commit**

```bash
git add src/doc_router/server.py src/doc_router/cli.py tests/test_server.py pyproject.toml
git commit -m "feat(doc-router): FastAPI server with graph API and serve CLI command"
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md`.