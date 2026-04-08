"""
Validates topology proposals for new modules against the existing knowledge graph.
Ensures orthogonality by checking for I/O collisions and glossary term compliance.
"""
from __future__ import annotations

import json
from pathlib import Path

import yaml

from .contracts import CollisionReport, IOFacet, KnowledgeNode, TopologyProposal
from .graph_utils import iter_knowledge_nodes, load_graph


DEFAULT_ATTEMPTS = 3


def validate_topology_proposal(
    proposal_data: dict[str, object],
    graph_path: Path,
    glossary_path: Path,
    state_path: Path,
) -> CollisionReport:
    proposal = TopologyProposal.model_validate(proposal_data)
    graph = load_graph(graph_path)
    nodes = iter_knowledge_nodes(graph)
    colliding_nodes = find_io_collisions(
        nodes, proposal.proposed_inputs + proposal.proposed_outputs
    )
    glossary_terms = load_glossary_terms(glossary_path)
    unknown_terms = [
        term
        for term in proposal.glossary_terms_used
        if term.lower() not in glossary_terms
    ]
    raw_write_violation = any(
        port.medium == "disk" and (port.path_template or "").startswith("raw/")
        for port in proposal.proposed_outputs
    )
    is_orthogonal = (
        not colliding_nodes and not unknown_terms and not raw_write_violation
    )
    attempts_remaining = update_attempts(
        state_path, proposal.proposed_module_name, is_orthogonal
    )
    suggestion = build_resolution(colliding_nodes, unknown_terms, raw_write_violation)
    return CollisionReport(
        is_orthogonal=is_orthogonal,
        colliding_node_schemas=colliding_nodes,
        resolution_suggestion=suggestion,
        attempts_remaining=attempts_remaining,
    )


def find_io_collisions(
    nodes: list[KnowledgeNode], proposed_ports: list[IOFacet]
) -> list[KnowledgeNode]:
    matches: list[KnowledgeNode] = []
    for node in nodes:
        if not node.io_ports:
            continue
        for existing_port in node.io_ports:
            if any(
                io_overlaps(existing_port, proposed_port)
                for proposed_port in proposed_ports
            ):
                matches.append(node)
                break
    return matches


def io_overlaps(existing_port: IOFacet, proposed_port: IOFacet) -> bool:
    if existing_port.medium != proposed_port.medium:
        return False
    if (
        existing_port.path_template
        and proposed_port.path_template
        and existing_port.path_template == proposed_port.path_template
    ):
        return True
    if (
        existing_port.schema_ref
        and proposed_port.schema_ref
        and existing_port.schema_ref == proposed_port.schema_ref
    ):
        return True
    return False


def load_glossary_terms(glossary_path: Path) -> set[str]:
    if not glossary_path.exists():
        return set()
    data = yaml.safe_load(glossary_path.read_text(encoding="utf-8")) or {}
    terms: set[str] = set()
    for canonical, entry in data.items():
        terms.add(str(canonical).lower())
        for synonym in (entry or {}).get("synonyms", []):
            terms.add(str(synonym).lower())
    return terms


def update_attempts(state_path: Path, module_name: str, is_orthogonal: bool) -> int:
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state = (
        json.loads(state_path.read_text(encoding="utf-8"))
        if state_path.exists()
        else {}
    )
    if is_orthogonal:
        state[module_name] = DEFAULT_ATTEMPTS
    else:
        state[module_name] = max(0, int(state.get(module_name, DEFAULT_ATTEMPTS)) - 1)
    state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")
    return state[module_name]


def build_resolution(
    colliding_nodes: list[KnowledgeNode],
    unknown_terms: list[str],
    raw_write_violation: bool,
) -> str | None:
    parts: list[str] = []
    if colliding_nodes:
        identifiers = ", ".join(node.identity.node_id for node in colliding_nodes)
        parts.append(f"Reuse or refactor existing nodes: {identifiers}.")
    if unknown_terms:
        parts.append(f"Unknown glossary terms: {', '.join(unknown_terms)}.")
    if raw_write_violation:
        parts.append("Outputs cannot write into `raw/`.")
    return " ".join(parts) or None
