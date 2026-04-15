"""
Context command handler.
"""

from __future__ import annotations
import argparse
from pathlib import Path

from ..context import render_context


def handle_context(args: argparse.Namespace) -> None:
    """Execute the context command."""
    print(
        render_context(
            graph_path=Path(args.graph),
            node_ids=args.nodes,
            task_hint=args.task,
            depth=args.depth,
            output_format=args.format,
            include_planned=args.include_planned,
        )
    )
