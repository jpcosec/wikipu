"""
Ingest command handler.
"""

from __future__ import annotations
import argparse
import json
from pathlib import Path

from ..ingest import ingest_raw_sources


def handle_ingest(args: argparse.Namespace) -> None:
    """Execute the ingest command."""
    written = ingest_raw_sources(
        source_dir=Path(args.source),
        dest_dir=Path(args.dest),
        project_root=Path(args.project_root),
        overwrite=args.overwrite,
        manifest_path=Path(args.manifest) if args.manifest else None,
    )
    print(json.dumps([path.as_posix() for path in written], indent=2))
