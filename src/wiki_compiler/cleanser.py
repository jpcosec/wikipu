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
    proposals.extend(_misplaced_folder_proposals(graph))
    proposals.extend(_stale_config_proposals(graph))
    proposals.extend(_orphaned_test_proposals(graph))
    return CleansingReport(proposals=_dedupe(proposals))


def _stale_edge_proposals(graph: object) -> list[CleansingProposal]:
    """Find edges that point to missing target nodes."""
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


def _stale_config_proposals(graph: object) -> list[CleansingProposal]:
    """Detects config/data nodes that are not read by any code node."""
    proposals: list[CleansingProposal] = []

    # Common config/data suffixes
    config_suffixes = {".json", ".yaml", ".yml", ".toml", ".csv"}

    for node_id in graph.nodes:
        data = graph.nodes[node_id]
        if data.get("type") != "file":
            continue

        path = Path(node_id.removeprefix("file:"))
        if path.suffix not in config_suffixes:
            continue

        # Check for incoming 'reads_from', 'configures', or 'documents' edges
        has_usage = False
        for _, _, edge_data in graph.in_edges(node_id, data=True):
            if edge_data.get("relation_type") in {
                "reads_from",
                "configures",
                "documents",
            }:
                has_usage = True
                break

        if not has_usage:
            proposals.append(
                CleansingProposal(
                    node_id=node_id,
                    operation="destroy",
                    rationale="Configuration/data file has no graph connections indicating usage.",
                    affected_nodes=[node_id],
                )
            )
    return proposals


def _orphaned_test_proposals(graph: object) -> list[CleansingProposal]:
    """Detects test files that do not cover any existing code node."""
    proposals: list[CleansingProposal] = []
    for node_id in graph.nodes:
        data = graph.nodes[node_id]
        if data.get("type") != "file" or not node_id.startswith("file:tests/"):
            continue

        # Check for 'covers' edges to existing code/file nodes
        has_coverage = False
        for _, target, edge_data in graph.out_edges(node_id, data=True):
            if edge_data.get("relation_type") == "covers":
                if target in graph.nodes:
                    has_coverage = True
                    break

        if not has_coverage:
            proposals.append(
                CleansingProposal(
                    node_id=node_id,
                    operation="destroy",
                    rationale="Test file does not cover any identified code or wiki node.",
                    affected_nodes=[node_id],
                )
            )
    return proposals


def _orphaned_plan_proposals(graph: object) -> list[CleansingProposal]:
    """Find planned nodes with no graph connections."""
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
    """Find nodes with abstracts containing multiple sentences."""
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
    """Find nodes with duplicate abstract content."""
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


def _misplaced_folder_proposals(graph: object) -> list[CleansingProposal]:
    """Detects nodes whose folder path does not match their declared node_type."""
    proposals: list[CleansingProposal] = []

    # Mapping of node_type to expected directory prefixes (repo-relative)
    type_to_prefix = {
        "concept": "wiki/concepts/",
        "reference": "wiki/reference/",
        "doc_standard": "wiki/standards/",
        "adr": "wiki/adrs/",
        "how_to": "wiki/how_to/",
    }

    for node in iter_knowledge_nodes(graph):
        node_id = node.identity.node_id
        if not node_id.startswith("doc:wiki/"):
            continue

        path_str = node_id.removeprefix("doc:")
        expected_prefix = type_to_prefix.get(node.identity.node_type)
        if not expected_prefix:
            continue

        if not path_str.startswith(expected_prefix):
            # Propose relocation
            correct_path = expected_prefix + Path(path_str).name
            proposals.append(
                CleansingProposal(
                    node_id=node_id,
                    operation="relocate",
                    rationale=f"Node type `{node.identity.node_type}` should be in `{expected_prefix}`.",
                    affected_nodes=[node_id, f"doc:{correct_path}"],
                )
            )
    return proposals


def apply_cleansing_proposal(proposal: CleansingProposal, project_root: Path) -> None:
    """Executes one approved cleansing proposal on the filesystem."""
    # Note: node_id 'doc:wiki/foo.md' maps to 'wiki/foo.md' relative to project_root.
    # file: and code: nodes are derived from code, we don't 'cleanse' them by
    # editing code yet, usually we cleanse the doc nodes that point to them.
    # But some file: nodes might be config/data that we can destroy.

    if proposal.operation == "destroy":
        _execute_destroy(proposal, project_root)
    elif proposal.operation == "relocate":
        _execute_relocate(proposal, project_root)
    elif proposal.operation == "split":
        _execute_split(proposal, project_root)
    elif proposal.operation == "merge":
        _execute_merge(proposal, project_root)
    else:
        raise ValueError(f"Unknown cleansing operation: {proposal.operation}")


def _execute_destroy(proposal: CleansingProposal, project_root: Path) -> None:
    path = _node_id_to_path(proposal.node_id, project_root)
    if path and path.exists():
        path.unlink()
        print(f"[OK] Destroyed: {proposal.node_id} ({path.relative_to(project_root)})")
    else:
        print(f"[WARN] Could not destroy {proposal.node_id}: path not found.")


def _execute_relocate(proposal: CleansingProposal, project_root: Path) -> None:
    # Relocate needs a destination in the proposal.
    # Current CleansingProposal doesn't have a 'destination' field.
    # We should probably add it or derive it from the rationale if it's there.
    # For now, let's assume it might be in affected_nodes[1] if operation is relocate.
    if len(proposal.affected_nodes) < 2:
        print(f"[ERROR] Relocate proposal for {proposal.node_id} missing destination.")
        return

    old_path = _node_id_to_path(proposal.node_id, project_root)
    new_node_id = proposal.affected_nodes[1]
    new_path = _node_id_to_path(new_node_id, project_root)

    if old_path and old_path.exists() and new_path:
        new_path.parent.mkdir(parents=True, exist_ok=True)
        old_path.rename(new_path)
        # We also need to update the node_id inside the frontmatter
        content = new_path.read_text(encoding="utf-8")
        updated = content.replace(
            f'node_id: "{proposal.node_id}"', f'node_id: "{new_node_id}"'
        )
        new_path.write_text(updated, encoding="utf-8")
        print(f"[OK] Relocated {proposal.node_id} to {new_node_id}")
    else:
        print(f"[ERROR] Could not relocate {proposal.node_id}.")


def _execute_split(proposal: CleansingProposal, project_root: Path) -> None:
    # Split is complex: requires creating new nodes.
    # The proposal should ideally contain the new content or paths.
    # For now, we'll mark it as manual or needing more metadata.
    print(
        f"[INFO] Split operation for {proposal.node_id} requires manual intervention or more metadata."
    )


def _execute_merge(proposal: CleansingProposal, project_root: Path) -> None:
    if len(proposal.affected_nodes) < 2:
        return
    canonical = proposal.affected_nodes[0]
    to_dissolve = proposal.affected_nodes[1]

    dissolve_path = _node_id_to_path(to_dissolve, project_root)
    if dissolve_path and dissolve_path.exists():
        dissolve_path.unlink()
        print(f"[OK] Merged {to_dissolve} into {canonical} (dissolved {to_dissolve})")


def _node_id_to_path(node_id: str, project_root: Path) -> Path | None:
    if node_id.startswith("doc:"):
        return project_root / node_id.removeprefix("doc:")
    if node_id.startswith("file:"):
        return project_root / node_id.removeprefix("file:")
    return None


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
