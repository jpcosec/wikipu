"""Wikipu Wiki Compiler - Knowledge Graph-driven development ecosystem."""

from __future__ import annotations

import sys
from pathlib import Path


def _bootstrap_sibling_sources() -> None:
    root = Path(__file__).resolve().parents[2]
    for sibling in ("kgdb", "ontology", "sldb"):
        src_path = root.parent / sibling / "src"
        if src_path.exists():
            sys.path.insert(0, str(src_path))


_bootstrap_sibling_sources()

__version__ = "1.1.0"
