---
identity:
  node_id: "doc:wiki/drafts/task_9_cli_commands_scan_lint_graph.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Modify: `src/doc_router/cli.py`
- Create: `tests/test_cli.py`

- [ ] **Step 1: Write failing tests**

```python
# tests/test_cli.py
"""Tests for CLI commands."""

import json
from pathlib import Path

from click.testing import CliRunner

from doc_router.cli import cli


def test_cli_scan(sample_project_dir: Path) -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["scan", "--project", str(sample_project_dir)])
    assert result.exit_code == 0
    assert "3 nodes" in result.output


def test_cli_scan_json(sample_project_dir: Path) -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["scan", "--project", str(sample_project_dir), "--json"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert "nodes" in data
    assert len(data["nodes"]) == 3


def test_cli_lint(sample_project_dir: Path) -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["lint", "--project", str(sample_project_dir)])
    assert result.exit_code == 0


def test_cli_graph_text(sample_project_dir: Path) -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["graph", "--project", str(sample_project_dir)])
    assert result.exit_code == 0
    assert "pipeline-match-design" in result.output


def test_cli_graph_filter(sample_project_dir: Path) -> None:
    runner = CliRunner()
    result = runner.invoke(cli, [
        "graph", "--project", str(sample_project_dir),
        "--domain", "core",
    ])
    assert result.exit_code == 0
    assert "core-architecture" in result.output
    assert "pipeline-match-design" not in result.output
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_cli.py -v`
Expected: FAIL

- [ ] **Step 3: Implement CLI commands**

```python
# src/doc_router/cli.py
"""CLI entrypoint for doc-router."""

from __future__ import annotations

import json
from pathlib import Path

import click

from doc_router import __version__
from doc_router.config import load_config
from doc_router.graph import build_graph
from doc_router.linter import lint_nodes
from doc_router.scanner.registry import scan_project


def _find_config(project: str | None) -> Path:
    root = Path(project) if project else Path.cwd()
    config_path = root / "doc-router.yml"
    if not config_path.exists():
        raise click.ClickException(f"No doc-router.yml found in {root}")
    return config_path


def _scan_and_build(project: str | None):
    config_path = _find_config(project)
    project_root = config_path.parent
    config = load_config(config_path)
    nodes, edges = scan_project(project_root, config)
    graph, build_issues = build_graph(nodes, edges)
    return project_root, config, graph, build_issues


@click.group()
@click.version_option(version=__version__)
def cli() -> None:
    """Documentation-driven development framework."""


@cli.command()
@click.option("--project", default=None, help="Project root (default: cwd)")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def scan(project: str | None, as_json: bool) -> None:
    """Scan project and build route graph."""
    _, _, graph, issues = _scan_and_build(project)
    if as_json:
        click.echo(json.dumps(graph.to_dict(), indent=2))
    else:
        doc_count = sum(1 for n in graph.nodes if n.type == "doc")
        code_count = sum(1 for n in graph.nodes if n.type == "code")
        click.echo(f"Scanned: {len(graph.nodes)} nodes ({doc_count} docs, {code_count} code), {len(graph.edges)} edges")
        if issues:
            click.echo(f"Issues: {len(issues)}")
            for issue in issues:
                click.echo(f"  [{issue['type']}] {issue}")


@cli.command()
@click.option("--project", default=None, help="Project root (default: cwd)")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def lint(project: str | None, as_json: bool) -> None:
    """Validate tags against project vocabulary."""
    config_path = _find_config(project)
    config = load_config(config_path)
    nodes, _ = scan_project(config_path.parent, config)
    issues = lint_nodes(nodes, config)
    if as_json:
        click.echo(json.dumps(issues, indent=2))
    elif issues:
        click.echo(f"Lint issues: {len(issues)}")
        for issue in issues:
            click.echo(f"  [{issue['type']}] {issue['node_id']} in {issue['path']}: "
                       f"'{issue['value']}' not in [{issue['valid']}]")
        raise SystemExit(1)
    else:
        click.echo("Lint: all tags valid")


@cli.command()
@click.option("--project", default=None, help="Project root (default: cwd)")
@click.option("--domain", default=None, help="Filter by domain")
@click.option("--stage", default=None, help="Filter by stage")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def graph(project: str | None, domain: str | None, stage: str | None, as_json: bool) -> None:
    """Print or export the route graph."""
    _, _, full_graph, _ = _scan_and_build(project)
    filtered = full_graph.filter(domain=domain, stage=stage)

    if as_json:
        click.echo(json.dumps(filtered.to_dict(), indent=2))
    else:
        click.echo(f"Nodes ({len(filtered.nodes)}):")
        for node in filtered.nodes:
            symbol = f"::{node.symbol}" if node.symbol else ""
            click.echo(f"  [{node.domain}/{node.stage}] {node.id} ({node.type}: {node.path}{symbol})")
        click.echo(f"\nEdges ({len(filtered.edges)}):")
        for edge in filtered.edges:
            click.echo(f"  {edge.source} --[{edge.type}]--> {edge.target}")


@cli.command()
def init() -> None:
    """Create doc-router.yml and templates directory."""
    click.echo("doc-router init — not yet implemented")
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_cli.py -v`
Expected: 5 passed

- [ ] **Step 5: Run all tests**

Run: `python -m pytest tests/ -v`
Expected: All passed (17 tests)

- [ ] **Step 6: Commit**

```bash
git add src/doc_router/cli.py tests/test_cli.py
git commit -m "feat(doc-router): CLI commands scan, lint, graph with JSON output"
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md`.