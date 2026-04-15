from __future__ import annotations

import json
from pathlib import Path

import networkx as nx

from wiki_compiler.cleanser import detect_cleansing_candidates
from wiki_compiler.contracts import ComplianceFacet
from wiki_compiler.contracts import Edge
from wiki_compiler.contracts import KnowledgeNode
from wiki_compiler.contracts import SemanticFacet
from wiki_compiler.contracts import SystemIdentity
from wiki_compiler.graph_utils import add_knowledge_node
from wiki_compiler.graph_utils import save_graph


def make_node(node_id: str, node_type: str = "file", **kwargs) -> KnowledgeNode:
    return KnowledgeNode(
        identity=SystemIdentity(node_id=node_id, node_type=node_type),
        **kwargs,
    )


def write_graph(path: Path, *nodes: KnowledgeNode) -> Path:
    graph = nx.DiGraph()
    for node in nodes:
        add_knowledge_node(graph, node)
    save_graph(graph, path)
    return path


def test_cleanse_detect_flags_stale_edge(tmp_path: Path) -> None:
    graph_path = write_graph(
        tmp_path / "graph.json",
        make_node(
            "doc:wiki/reference/foo.md",
            node_type="reference",
            edges=[Edge(target_id="file:src/missing.py", relation_type="documents")],
        ),
    )

    report = detect_cleansing_candidates(graph_path)

    assert any(proposal.operation == "relocate" for proposal in report.proposals)


def test_cleanse_detect_flags_orphaned_plan(tmp_path: Path) -> None:
    graph_path = write_graph(
        tmp_path / "graph.json",
        make_node(
            "doc:desk/tasks/lonely.md",
            node_type="doc_standard",
            compliance=ComplianceFacet(status="planned", failing_standards=[]),
        ),
    )

    report = detect_cleansing_candidates(graph_path)

    assert any(proposal.operation == "destroy" for proposal in report.proposals)


def test_cleanse_detect_flags_compound_abstract(tmp_path: Path) -> None:
    graph_path = write_graph(
        tmp_path / "graph.json",
        make_node(
            "doc:wiki/concepts/compound.md",
            node_type="concept",
            semantics=SemanticFacet(
                intent="This node explains the graph. It also explains the CLI.",
                raw_docstring=None,
            ),
        ),
    )

    report = detect_cleansing_candidates(graph_path)

    assert any(proposal.operation == "split" for proposal in report.proposals)


def test_cleanse_detect_flags_duplicate_abstracts(tmp_path: Path) -> None:
    graph_path = write_graph(
        tmp_path / "graph.json",
        make_node(
            "doc:wiki/reference/a.md",
            node_type="reference",
            semantics=SemanticFacet(intent="Same abstract.", raw_docstring=None),
        ),
        make_node(
            "doc:wiki/reference/b.md",
            node_type="reference",
            semantics=SemanticFacet(intent="Same abstract.", raw_docstring=None),
        ),
    )

    report = detect_cleansing_candidates(graph_path)

    assert any(proposal.operation == "merge" for proposal in report.proposals)


def test_cleanse_detect_exempts_index_and_reference(tmp_path: Path) -> None:
    graph_path = write_graph(
        tmp_path / "graph.json",
        make_node(
            "doc:wiki/adrs/Index.md",
            node_type="index",
            semantics=SemanticFacet(
                intent="This index lists all ADRs and explains their relationships.",
                raw_docstring=None,
            ),
        ),
        make_node(
            "doc:wiki/reference/cli/query.md",
            node_type="reference",
            semantics=SemanticFacet(
                intent="This command queries the graph and also supports structured queries.",
                raw_docstring=None,
            ),
        ),
        make_node(
            "doc:wiki/concepts/real_compound.md",
            node_type="concept",
            semantics=SemanticFacet(
                intent="This node does A. It also does B and C.",
                raw_docstring=None,
            ),
        ),
    )

    report = detect_cleansing_candidates(graph_path)

    # Should only flag 'real_compound.md'
    split_nodes = [p.node_id for p in report.proposals if p.operation == "split"]
    assert len(split_nodes) == 1
    assert split_nodes[0] == "doc:wiki/concepts/real_compound.md"
