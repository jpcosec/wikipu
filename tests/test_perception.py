from __future__ import annotations

import json
from pathlib import Path

from wiki_compiler.builder import build_wiki
from wiki_compiler.perception import build_status_report


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    return path


def test_build_wiki_attaches_git_facet_to_file_backed_nodes(tmp_path: Path) -> None:
    project_root = tmp_path
    write(
        project_root / "wiki" / "concept.md",
        """
        ---
        identity:
          node_id: "doc:wiki/concept.md"
          node_type: "concept"
        edges: []
        compliance:
          status: "implemented"
          failing_standards: []
        ---

        A concept node.

        ## Definition

        Definition.

        ## Examples

        Example.

        ## Related Concepts

        Related.
        """,
    )
    write(project_root / "src" / "module.py", '"""Runtime module."""')

    result = build_wiki(
        source_dir=project_root / "wiki",
        graph_path=project_root / "knowledge_graph.json",
        project_root=project_root,
        code_roots=[project_root / "src"],
        baseline_path=project_root / ".compliance_baseline.json",
        update_baseline=True,
    )
    graph_data = json.loads(result.graph_path.read_text(encoding="utf-8"))
    concept_node = next(
        node for node in graph_data["nodes"] if node["id"] == "doc:wiki/concept.md"
    )

    assert concept_node["schema"]["git"]["blob_sha"]
    assert concept_node["schema"]["git"]["status"] in {"tracked", "untracked"}


def test_status_report_flags_modified_file_and_untracked_raw(tmp_path: Path) -> None:
    project_root = tmp_path
    concept_path = write(
        project_root / "wiki" / "concept.md",
        """
        ---
        identity:
          node_id: "doc:wiki/concept.md"
          node_type: "concept"
        edges: []
        compliance:
          status: "implemented"
          failing_standards: []
        ---

        A concept node.

        ## Definition

        Definition.

        ## Examples

        Example.

        ## Related Concepts

        Related.
        """,
    )

    build_wiki(
        source_dir=project_root / "wiki",
        graph_path=project_root / "knowledge_graph.json",
        project_root=project_root,
        code_roots=[project_root / "src"],
        baseline_path=project_root / ".compliance_baseline.json",
        update_baseline=True,
    )
    concept_path.write_text(
        concept_path.read_text(encoding="utf-8") + "\nExtra line.\n",
        encoding="utf-8",
    )
    write(project_root / "raw" / "new_note.md", "# New raw note")

    report = build_status_report(
        graph_path=project_root / "knowledge_graph.json",
        project_root=project_root,
    )

    assert any(
        item["node_id"] == "doc:wiki/concept.md" for item in report["modified_nodes"]
    )
    assert "raw/new_note.md" in report["untracked_by_zone"].get("raw", [])
