"""
Implements the trail-collect closeout step for distilling durable facts from sessions.
"""

from __future__ import annotations

import json
from pathlib import Path
from .contracts import TrailArtifact, TrailCollection


def collect_cycle_trails(
    session_id: str, 
    actions_taken: list[str], 
    perturbations: int
) -> TrailCollection:
    """
    Classifies cycle outcomes into trail artifacts.
    In a full implementation, this might use LLM extraction from conversation.
    In this skeleton, we derive it from coordinator actions.
    """
    artifacts: list[TrailArtifact] = []
    
    for action in actions_taken:
        if action.startswith("applied_cleansing"):
            artifacts.append(TrailArtifact(
                kind="correction",
                content=f"Applied structural correction: {action}",
                destination="knowledge_graph.json"
            ))
        elif action.startswith("ingested"):
            artifacts.append(TrailArtifact(
                kind="new_concept",
                content=f"Extracted new concepts from raw source.",
                destination="wiki/drafts/"
            ))
            
    return TrailCollection(session_id=session_id, artifacts=artifacts)


def persist_trail(project_root: Path, collection: TrailCollection) -> Path:
    """Saves a trail collection to the durable operational surface."""
    trail_dir = project_root / "desk/autopoiesis/trails"
    trail_dir.mkdir(parents=True, exist_ok=True)
    
    path = trail_dir / f"{collection.session_id}.json"
    path.write_text(collection.model_dump_json(indent=2), encoding="utf-8")
    return path
