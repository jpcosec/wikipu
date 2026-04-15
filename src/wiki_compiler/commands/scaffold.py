"""
Scaffold command handler.
"""

from __future__ import annotations
import argparse
from pathlib import Path

from ..scaffolder import generate_scaffolding


def handle_scaffold(args: argparse.Namespace) -> None:
    """Execute the scaffold command."""
    generate_scaffolding(Path(args.module), args.intent)
    print(f"[OK] Scaffolding successfully created in {args.module}")
