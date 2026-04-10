"""Detect structural cleansing candidates in the knowledge graph."""

from __future__ import annotations

import re
from pathlib import Path

from .contracts import CleansingProposal
from .contracts import CleansingReport
from .graph_utils import iter_knowledge_nodes
from .graph_utils import load_graph


def detect_cleansing_candidates(graph_path: Path) -> CleansingReport:
    """Load a graph and return the current cleansing candidate proposals."""
    graph = load_graph(graph_path)
    proposals: list[CleansingProposal] = []
    proposals.extend(_stale_edge_proposals(graph))
    proposals.extend(_orphaned_plan_proposals(graph))
    proposals.extend(_compound_abstract_proposals(graph))
    proposals.extend(_duplicate_abstract_proposals(graph))
    return CleansingReport(proposals=_dedupe(proposals))


def _stale_edge_proposals(graph: object) -> list[CleansingProposal]:
    proposals: list[CleansingProposal] = []
    for source, target, data in graph.edges(data=True):
        if "type" in graph.nodes[target]:
            continue
        proposals.append(
            CleansingProposal(
                node_id=source,
                operation="relocate",
                rationale=f"Edge relation={data.get('relation')!r} points to missing node `{target}`.",
                affected_nodes=[source, target],
            )
        )
    return proposals


def _orphaned_plan_proposals(graph: object) -> list[CleansingProposal]:
    proposals: list[CleansingProposal] = []
    for node in iter_knowledge_nodes(graph):
        compliance = node.compliance
        if not node.identity.node_id.startswith("doc:plan_docs/"):
            continue
        if not compliance or compliance.status != "planned":
            continue
        if graph.in_degree(node.identity.node_id) or graph.out_degree(
            node.identity.node_id
        ):
            continue
        proposals.append(
            CleansingProposal(
                node_id=node.identity.node_id,
                operation="destroy",
                rationale="Planned node has no graph connections and is a candidate for removal.",
                affected_nodes=[node.identity.node_id],
            )
        )
    return proposals


def _compound_abstract_proposals(graph: object) -> list[CleansingProposal]:
    proposals: list[CleansingProposal] = []
    for node in iter_knowledge_nodes(graph):
        if not node.identity.node_id.startswith("doc:") or not node.semantics:
            continue
        if node.identity.node_type in {"index", "reference"}:
            continue
        abstract = node.semantics.intent.strip()
        if not abstract:
            continue
        sentence_count = _sentence_count(abstract)
        if sentence_count > 3 or (
            sentence_count > 1 and _has_dual_purpose_language(abstract)
        ):
            proposals.append(
                CleansingProposal(
                    node_id=node.identity.node_id,
                    operation="split",
                    rationale="Abstract appears compound and may cover multiple responsibilities.",
                    affected_nodes=[node.identity.node_id],
                )
            )
    return proposals


def _duplicate_abstract_proposals(graph: object) -> list[CleansingProposal]:
    proposals: list[CleansingProposal] = []
    seen: dict[str, str] = {}
    for node in iter_knowledge_nodes(graph):
        if not node.identity.node_id.startswith("doc:") or not node.semantics:
            continue
        normalized = _normalize_text(node.semantics.intent)
        if not normalized:
            continue
        other = seen.get(normalized)
        if other is None:
            seen[normalized] = node.identity.node_id
            continue
        proposals.append(
            CleansingProposal(
                node_id=node.identity.node_id,
                operation="merge",
                rationale=f"Abstract duplicates existing node `{other}`.",
                affected_nodes=[other, node.identity.node_id],
            )
        )
    return proposals


def _sentence_count(text: str) -> int:
    return len(re.findall(r"[.!?]+", text))


def _has_dual_purpose_language(text: str) -> bool:
    lowered = text.lower()
    return " and " in lowered or " also " in lowered


def _normalize_text(text: str) -> str:
    return re.sub(r"\W+", " ", text).strip().lower()


def _dedupe(proposals: list[CleansingProposal]) -> list[CleansingProposal]:
    unique: list[CleansingProposal] = []
    seen: set[tuple[str, str, str]] = set()
    for proposal in proposals:
        key = (proposal.node_id, proposal.operation, proposal.rationale)
        if key in seen:
            continue
        seen.add(key)
        unique.append(proposal)
    return unique
