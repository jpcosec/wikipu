"""
Status command handler.
"""

from __future__ import annotations
import argparse
import json
from pathlib import Path

from ..perception import build_status_report


def handle_status(args: argparse.Namespace) -> None:
    """Execute the status command."""
    report = build_status_report(
        graph_path=Path(args.graph),
        project_root=Path(args.project_root),
    )
    print(json.dumps(report, indent=2))
