"""Adapter for ontology energy services."""

from pathlib import Path

import networkx as nx

from ontology.energy import DRIFT_PENALTY_WEIGHT, run_energy_audit as _run_energy_audit


def run_energy_audit(graph: nx.DiGraph, project_root: Path):
    from wiki_compiler.auditor import run_audit
    from wiki_compiler.face import FaceAnalyzer
    from wiki_compiler.perception import build_status_report

    return _run_energy_audit(
        graph,
        project_root,
        audit_runner=run_audit,
        status_builder=build_status_report,
        face_analyzer_cls=FaceAnalyzer,
    )


__all__ = ["DRIFT_PENALTY_WEIGHT", "run_energy_audit"]
