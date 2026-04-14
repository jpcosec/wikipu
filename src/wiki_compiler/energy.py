"""
Minimal Energy (ID-2) calculation and reporting.
"""

from __future__ import annotations

import datetime
from pathlib import Path

from .contracts import SystemicEnergy, EnergyReport
from .perception import build_status_report
from .auditor import run_audit
import networkx as nx


def calculate_systemic_energy(graph: nx.DiGraph, project_root: Path) -> SystemicEnergy:
    """
    Calculates the systemic energy score based on the heuristic in wiki/concepts/energy.md.

    Heuristic:
    Energy = (Nodes * 1) + (Edges * 0.2) + (Violations * 10) + (Perturbations * 5) + (Gates * 20)
    """
    node_count = graph.number_of_nodes()
    edge_count = graph.number_of_edges()

    # Get audit findings for violation count
    audit_report = run_audit(graph)
    violations = len(audit_report.findings)

    # Get status report for perturbations and gates
    status = build_status_report(
        graph_path=None, project_root=project_root, graph=graph
    )
    perturbations = status.get("perturbations", [])
    open_gates = len(status.get("open_gates", []))

    # Check for uncommitted changes (highest energy state)
    uncommitted = 0
    for p in perturbations:
        if p.get("type") in ("modified_node", "untracked_raw", "staged"):
            uncommitted += 1

    # Weighted energy components
    node_energy = node_count * 1.0
    edge_energy = edge_count * 0.2
    violation_energy = violations * 10.0
    perturbation_energy = len(perturbations) * 5.0
    gate_energy = open_gates * 20.0
    uncommitted_energy = uncommitted * 50.0  # Maximum entropy - uncommitted changes

    total_score = (
        node_energy
        + edge_energy
        + violation_energy
        + perturbation_energy
        + gate_energy
        + uncommitted_energy
    )

    return SystemicEnergy(
        energy_score=total_score,
        node_count=node_count,
        edge_count=edge_count,
        compliance_violations=violations,
        perturbations=len(perturbations),
        open_gates=open_gates,
        node_energy=node_energy + edge_energy,
        violation_energy=violation_energy,
        perturbation_energy=perturbation_energy + gate_energy,
    )


def run_energy_audit(graph: nx.DiGraph, project_root: Path) -> EnergyReport:
    """Produces a full energy report."""
    current = calculate_systemic_energy(graph, project_root)

    return EnergyReport(
        timestamp=datetime.datetime.now().isoformat(),
        current_energy=current,
        delta=0.0,  # Baseline comparison TODO
    )
