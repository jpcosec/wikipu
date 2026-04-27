"""Adapter for the current wikipu-owned energy service."""

from pathlib import Path

import networkx as nx

from wiki_compiler.energy import (
    DRIFT_PENALTY_WEIGHT,
    run_energy_audit as _run_energy_audit,
)


def run_energy_audit(graph: nx.DiGraph, project_root: Path):
    from wiki_compiler.auditor import run_audit
    from wiki_compiler.perception import build_status_report

    face_analyzer_cls = None
    try:
        from wiki_compiler.face import FaceAnalyzer
    except ImportError:
        FaceAnalyzer = None

    if FaceAnalyzer is not None:
        face_analyzer_cls = FaceAnalyzer

    return _run_energy_audit(
        graph,
        project_root,
        audit_runner=run_audit,
        status_builder=build_status_report,
        face_analyzer_cls=face_analyzer_cls,
    )


__all__ = ["DRIFT_PENALTY_WEIGHT", "run_energy_audit"]
