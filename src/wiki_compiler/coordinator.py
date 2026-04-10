"""
The central orchestrator for the autopoietic loop.
"""

from __future__ import annotations

import json
from pathlib import Path
from .perception import build_status_report
from .builder import build_wiki
from .ingest import ingest_raw_sources


def run_coordinator_cycle(
    project_root: Path,
    graph_path: Path,
    wiki_dir: Path,
    manifest_path: Path | None = None,
) -> dict[str, object]:
    """
    Executes one cycle of the autopoietic loop.
    1. Perception: detect perturbations.
    2. Classification: decide response actions.
    3. Execution: run safe, non-gated actions.
    4. Rebuild: update the knowledge graph.
    """
    report = build_status_report(graph_path, project_root)
    perturbations = report.get("perturbations", [])
    
    executed_actions: list[str] = []
    
    # 1. Handle untracked raw files (safe auto-ingest)
    untracked_raw = [p for p in perturbations if p["type"] == "untracked_raw"]
    if untracked_raw:
        # In this first skeleton, we'll auto-ingest untracked raw files into drafts
        # if they match the classification action 'ingest_raw_source'
        raw_to_ingest = [p["id"] for p in untracked_raw if p["action"] == "ingest_raw_source"]
        if raw_to_ingest:
            # We currently ingest the whole directory in ingest_raw_sources, 
            # but we can filter or just call it since it skips existing.
            ingest_raw_sources(
                source_dir=project_root / "raw",
                dest_dir=wiki_dir / "drafts",
                project_root=project_root,
                manifest_path=manifest_path
            )
            executed_actions.append(f"ingested_{len(raw_to_ingest)}_raw_files")

    # 2. Rebuild graph if needed
    needs_rebuild = any(p["action"] in {"rebuild_graph", "rebuild_graph_and_audit"} for p in perturbations)
    if needs_rebuild or executed_actions:
        build_wiki(
            source_dir=wiki_dir,
            graph_path=graph_path,
            project_root=project_root
        )
        executed_actions.append("rebuilt_graph")

    return {
        "status": "success",
        "perturbations_detected": len(perturbations),
        "actions_taken": executed_actions
    }
