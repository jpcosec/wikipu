"""
Curate command handler.
"""

from __future__ import annotations
import argparse
import json
from pathlib import Path

from ..curate import promote_draft, score_drafts


def handle_curate(args: argparse.Namespace) -> None:
    """Execute the curate command."""
    if args.score:
        results = score_drafts(
            graph_path=Path(args.graph),
            drafts_dir=Path(args.drafts_dir),
        )
        print(json.dumps(results, indent=2))
        return
    if args.promote:
        node_id, dest = args.promote
        promote_draft(
            node_id=node_id,
            dest=dest,
            drafts_dir=Path(args.drafts_dir),
            wiki_dir=Path(args.wiki_dir),
        )
        print(f"[OK] Promoted {node_id} to wiki/{dest}")
        return
    raise ValueError("curate requires --score or --promote <node_id> <dest>")
