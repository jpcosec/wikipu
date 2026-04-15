from __future__ import annotations

import json
from pathlib import Path

import pytest

from wiki_compiler.builder import build_wiki
from wiki_compiler.context import render_context
from wiki_compiler.query_server import query_graph
from wiki_compiler.scanner import scan_python_sources
from wiki_compiler.validator import validate_topology_proposal


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    return path


def test_scan_python_sources_detects_signatures_exemptions_and_ignore(
    tmp_path: Path,
) -> None:
    project_root = tmp_path
    write(
        project_root / ".wikiignore",
        "src/legacy.py # legacy debt",
    )
    write(
        project_root / "src/sample.py",
        '''
        """Sample module.

        Input: disk | data/input.json | InputModel
        Output: disk | data/output.json | OutputModel
        """

        from pathlib import Path
        from wikipu.decorators import wiki_exempt

        @wiki_exempt(reason="third-party boundary")
        def run_job(payload: str) -> str:
            """Run the job."""
            source = Path("data/input.json").read_text()
            Path("data/output.json").write_text(source + payload)
            return payload


        class Worker:
            """Execute work."""

            def execute(self, value: str) -> str:
                return value
        ''',
    )
    write(
        project_root / "src/legacy.py",
        """
        def old_code() -> None:
            return None
        """,
    )

    nodes = scan_python_sources(
        project_root=project_root, source_roots=[project_root / "src"]
    )
    node_map = {node.identity.node_id: node for node in nodes}

    module_node = node_map["file:src/sample.py"]
    function_node = node_map["code:src/sample.py:run_job"]
    class_node = node_map["code:src/sample.py:Worker"]
    ignored_node = node_map["file:src/legacy.py"]

    assert module_node.semantics is not None
    assert module_node.semantics.intent == "Sample module."
    assert module_node.ast is not None
    assert "from pathlib import Path" in module_node.ast.dependencies
    assert {port.path_template for port in module_node.io_ports} >= {
        "data/input.json",
        "data/output.json",
    }

    assert function_node.compliance is not None
    assert function_node.compliance.status == "exempt"
    assert function_node.compliance.exemption_reason == "third-party boundary"
    assert function_node.ast is not None
    assert "run_job(payload: str) -> str" in function_node.ast.signatures

    assert class_node.ast is not None
    assert "class Worker" in class_node.ast.signatures[0]
    assert any("execute" in signature for signature in class_node.ast.signatures)

    assert ignored_node.compliance is not None
    assert ignored_node.compliance.status == "exempt"
    assert ignored_node.compliance.exemption_reason == "legacy debt"


def test_build_wiki_merges_source_nodes_and_tracks_compliance(tmp_path: Path) -> None:
    project_root = tmp_path
    source_dir = project_root / "wiki"
    dest_dir = project_root / "wiki/compiled"
    graph_path = project_root / "knowledge_graph.json"
    baseline_path = dest_dir / "compliance_baseline.json"
    write(
        source_dir / "index.md",
        """
        ---
        identity:
          node_id: "doc:wiki/index.md"
          node_type: "doc_standard"
        edges: []
        compliance:
          status: "tested"
        ---

        # Index

        ![[details]]
        """,
    )
    write(
        source_dir / "details.md",
        """
        ---
        identity:
          node_id: "doc:wiki/details.md"
          node_type: "concept"
        edges: []
        compliance:
          status: "implemented"
        ---

        # Details
        """,
    )
    write(
        project_root / "src/runtime.py",
        '''
        """Runtime module."""

        def execute(task: str) -> str:
            """Execute a task."""
            return task
        ''',
    )

    result = build_wiki(
        source_dir=source_dir,
        dest_dir=dest_dir,
        graph_path=graph_path,
        project_root=project_root,
        code_roots=[project_root / "src"],
        baseline_path=baseline_path,
        update_baseline=True,
    )

    graph_data = json.loads(graph_path.read_text(encoding="utf-8"))
    node_ids = {node["id"] for node in graph_data["nodes"]}
    compiled = (dest_dir / "index.md").read_text(encoding="utf-8")
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))

    assert "doc:wiki/index.md" in node_ids
    assert "file:src/runtime.py" in node_ids
    assert "code:src/runtime.py:execute" in node_ids
    assert "[See details](details.md)" in compiled
    assert result.compliance_score == pytest.approx(100.0)
    assert baseline["score"] == pytest.approx(100.0)


def test_query_and_context_runtime_cover_graph_navigation(tmp_path: Path) -> None:
    graph_path = tmp_path / "knowledge_graph.json"
    graph_data = {
        "directed": True,
        "multigraph": False,
        "graph": {},
        "nodes": [
            {
                "id": "file:src/service.py",
                "type": "file",
                "status": "implemented",
                "schema": {
                    "identity": {"node_id": "file:src/service.py", "node_type": "file"},
                    "edges": [],
                    "semantics": {
                        "intent": "Service entrypoint.",
                        "raw_docstring": "Service entrypoint.",
                    },
                    "ast": {
                        "construct_type": "script",
                        "signatures": ["module src/service.py"],
                        "dependencies": [],
                    },
                    "io_ports": [
                        {
                            "medium": "disk",
                            "path_template": "data/output.json",
                            "schema_ref": "OutputModel",
                        }
                    ],
                    "compliance": {
                        "status": "implemented",
                        "failing_standards": [],
                        "exemption_reason": None,
                    },
                    "adr": None,
                },
            },
            {
                "id": "code:src/service.py:run",
                "type": "code_construct",
                "status": "implemented",
                "schema": {
                    "identity": {
                        "node_id": "code:src/service.py:run",
                        "node_type": "code_construct",
                    },
                    "edges": [],
                    "semantics": {
                        "intent": "Run the service.",
                        "raw_docstring": "Run the service.",
                    },
                    "ast": {
                        "construct_type": "function",
                        "signatures": ["run() -> None"],
                        "dependencies": [],
                    },
                    "io_ports": [],
                    "compliance": {
                        "status": "implemented",
                        "failing_standards": [],
                        "exemption_reason": None,
                    },
                    "adr": None,
                },
            },
        ],
        "links": [
            {
                "source": "file:src/service.py",
                "target": "code:src/service.py:run",
                "relation": "contains",
                "metadata": {},
            },
        ],
    }
    graph_path.write_text(json.dumps(graph_data, indent=2), encoding="utf-8")

    node_result = query_graph(
        graph_path, query_type="get_node", node_id="file:src/service.py"
    )
    descendants = query_graph(
        graph_path, query_type="get_descendants", node_id="file:src/service.py"
    )
    by_io = query_graph(
        graph_path, query_type="find_by_io", path_template="data/output.json"
    )
    context = render_context(
        graph_path=graph_path,
        node_ids=["file:src/service.py"],
        depth=1,
        output_format="markdown",
    )

    assert node_result["node"]["identity"]["node_id"] == "file:src/service.py"
    assert descendants["nodes"][0]["identity"]["node_id"] == "code:src/service.py:run"
    assert by_io["nodes"][0]["identity"]["node_id"] == "file:src/service.py"
    assert "## `file:src/service.py`" in context
    assert "Service entrypoint." in context
    assert "routing: descendant_of_file:src/service.py" in context


def test_validator_rejects_collisions_and_tracks_attempts(tmp_path: Path) -> None:
    graph_path = tmp_path / "knowledge_graph.json"
    glossary_path = tmp_path / "wiki/domain_glossary.yaml"
    state_path = tmp_path / "wiki/compiled/validation_session.json"
    write(
        glossary_path,
        """
        Service:
          description: "Service component"
          synonyms: ["Worker"]
        """,
    )
    graph_path.parent.mkdir(parents=True, exist_ok=True)
    graph_path.write_text(
        json.dumps(
            {
                "directed": True,
                "multigraph": False,
                "graph": {},
                "nodes": [
                    {
                        "id": "file:src/service.py",
                        "type": "file",
                        "status": "implemented",
                        "schema": {
                            "identity": {
                                "node_id": "file:src/service.py",
                                "node_type": "file",
                            },
                            "edges": [],
                            "semantics": {
                                "intent": "Service entrypoint.",
                                "raw_docstring": "Service entrypoint.",
                            },
                            "ast": {
                                "construct_type": "script",
                                "signatures": ["module"],
                                "dependencies": [],
                            },
                            "io_ports": [
                                {
                                    "medium": "disk",
                                    "path_template": "data/output.json",
                                    "schema_ref": "OutputModel",
                                }
                            ],
                            "compliance": {
                                "status": "implemented",
                                "failing_standards": [],
                                "exemption_reason": None,
                            },
                            "adr": None,
                        },
                    }
                ],
                "links": [],
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    proposal = {
        "proposed_module_name": "new_service",
        "intent": "Write service output.",
        "glossary_terms_used": ["UnknownTerm"],
        "proposed_inputs": [],
        "proposed_outputs": [
            {
                "medium": "disk",
                "path_template": "data/output.json",
                "schema_ref": "OutputModel",
            }
        ],
    }

    report = validate_topology_proposal(
        proposal_data=proposal,
        graph_path=graph_path,
        glossary_path=glossary_path,
        state_path=state_path,
    )

    assert report.is_orthogonal is False
    assert report.attempts_remaining == 2
    assert report.colliding_node_schemas[0].identity.node_id == "file:src/service.py"
    assert "Unknown glossary terms" in (report.resolution_suggestion or "")


def test_build_wiki_infers_documents_edges_from_reference_pages(tmp_path: Path) -> None:
    project_root = tmp_path
    source_dir = project_root / "wiki"
    graph_path = project_root / "knowledge_graph.json"
    write(
        source_dir / "reference/scanner.md",
        """
        ---
        identity:
          node_id: "doc:wiki/reference/scanner.md"
          node_type: "doc_standard"
        edges: []
        compliance:
          status: "implemented"
          failing_standards: []
        ---

        Scanner reference.
        """,
    )
    write(
        project_root / "src/wiki_compiler/scanner.py",
        '''
        """Scanner module."""

        def scan() -> None:
            """Scan the source tree."""
            return None
        ''',
    )

    build_wiki(
        source_dir=source_dir,
        graph_path=graph_path,
        project_root=project_root,
        code_roots=[project_root / "src"],
        baseline_path=project_root / "baseline.json",
        update_baseline=True,
    )

    graph = json.loads(graph_path.read_text(encoding="utf-8"))
    scanner_doc = next(
        node for node in graph["nodes"] if node["id"] == "doc:wiki/reference/scanner.md"
    )
    edges = {
        (link["source"], link["target"], link["relation"]) for link in graph["links"]
    }

    assert (
        "doc:wiki/reference/scanner.md",
        "file:src/wiki_compiler/scanner.py",
        "documents",
    ) in edges
    assert (
        "doc:wiki/reference/scanner.md",
        "code:src/wiki_compiler/scanner.py:scan",
        "documents",
    ) in edges
    assert any(
        edge["relation_type"] == "documents"
        and edge["target_id"] == "file:src/wiki_compiler/scanner.py"
        for edge in scanner_doc["schema"]["edges"]
    )


def test_ingest_scaffolding_creates_draft_nodes(tmp_path: Path) -> None:
    from wiki_compiler.ingest import ingest_raw_sources

    source_dir = tmp_path / "raw"
    dest_dir = tmp_path / "wiki"
    write(
        source_dir / "notes.md",
        """
        # Raw Notes

        This raw document explains the ingestion pipeline.
        """,
    )

    written_files = ingest_raw_sources(source_dir=source_dir, dest_dir=dest_dir)
    draft_text = written_files[0].read_text(encoding="utf-8")

    assert written_files
    assert 'node_id: "doc:wiki/raw_notes.md"' in draft_text
    assert 'status: "planned"' in draft_text
    assert "Generated from `raw/notes.md`" in draft_text


def test_ingest_mirrors_source_subdirs_and_writes_index(tmp_path: Path) -> None:
    from wiki_compiler.ingest import ingest_raw_sources

    source_dir = tmp_path / "raw"
    dest_dir = tmp_path / "desk/drafts"
    write(
        source_dir / "source_a" / "notes.md",
        """
        # Source A Notes

        This source explains one concept.
        """,
    )

    written_files = ingest_raw_sources(source_dir=source_dir, dest_dir=dest_dir)
    draft_path = dest_dir / "source_a" / "source_a_notes.md"
    index_path = dest_dir / "source_a" / "INDEX.md"

    assert draft_path in written_files
    assert (
        'node_id: "doc:desk/drafts/source_a/source_a_notes.md"'
        in draft_path.read_text(encoding="utf-8")
    )
    assert "doc:desk/drafts/source_a/source_a_notes.md" in index_path.read_text(
        encoding="utf-8"
    )


def test_curate_score_reports_ranked_draft_quality(tmp_path: Path) -> None:
    from networkx.readwrite import json_graph
    from wiki_compiler.curate import score_drafts

    graph_path = tmp_path / "knowledge_graph.json"
    drafts_dir = tmp_path / "desk/drafts"
    good_draft = drafts_dir / "group" / "good.md"
    good_draft.parent.mkdir(parents=True, exist_ok=True)
    good_draft.write_text("draft", encoding="utf-8")

    graph_data = {
        "directed": True,
        "multigraph": False,
        "graph": {},
        "nodes": [
            {
                "id": "doc:desk/drafts/group/good.md",
                "schema": {
                    "identity": {
                        "node_id": "doc:desk/drafts/group/good.md",
                        "node_type": "concept",
                    },
                    "semantics": {"intent": "A clear abstract. Another sentence."},
                },
            },
            {
                "id": "doc:desk/drafts/group/bad.md",
                "schema": {
                    "identity": {
                        "node_id": "doc:desk/drafts/group/bad.md",
                        "node_type": "file",
                    },
                    "semantics": {"intent": ""},
                },
            },
        ],
        "links": [],
    }
    graph_path.write_text(json.dumps(graph_data), encoding="utf-8")

    results = score_drafts(graph_path=graph_path, drafts_dir=drafts_dir)

    assert results[0]["node_id"] == "doc:desk/drafts/group/good.md"
    assert results[0]["score"] > results[1]["score"]


def test_curate_promote_moves_draft_and_rewrites_node_id(tmp_path: Path) -> None:
    from wiki_compiler.curate import promote_draft

    drafts_dir = tmp_path / "desk/drafts"
    wiki_dir = tmp_path / "wiki"
    draft_path = drafts_dir / "group" / "draft.md"
    draft_path.parent.mkdir(parents=True, exist_ok=True)
    draft_path.write_text(
        """---
identity:
  node_id: "doc:desk/drafts/group/draft.md"
  node_type: "concept"
---

Draft abstract.
""",
        encoding="utf-8",
    )

    promote_draft(
        node_id="doc:desk/drafts/group/draft.md",
        dest="concepts/promoted.md",
        drafts_dir=drafts_dir,
        wiki_dir=wiki_dir,
    )

    promoted_path = wiki_dir / "concepts" / "promoted.md"
    assert promoted_path.exists()
    assert not draft_path.exists()
    assert 'node_id: "doc:wiki/concepts/promoted.md"' in promoted_path.read_text(
        encoding="utf-8"
    )
