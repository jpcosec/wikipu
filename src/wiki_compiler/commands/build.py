"""
Build command handler.
"""

from __future__ import annotations
import argparse
import sys
from pathlib import Path

from ..builder import build_wiki


def handle_build(args: argparse.Namespace) -> None:
    """Execute the build command."""
    result = build_wiki(
        source_dir=Path(args.source),
        graph_path=Path(args.graph),
        project_root=Path(args.project_root),
        code_roots=[Path(path) for path in args.code_root],
        baseline_path=Path(args.baseline),
        update_baseline=args.update_baseline,
    )
    print(f"[OK] Graph saved to {args.graph}")
    print(f"[INFO] Compliance score: {result.compliance_score:.2f}")
    if result.baseline_regressed:
        print("[ERROR] Compliance score regressed against the baseline")
        sys.exit(1)

    if getattr(args, "owl", False):
        try:
            from wiki_compiler.owl_backend.export import export_wikipu_ontology

            output = export_wikipu_ontology(Path(args.project_root) / args.source)
            print(f"[OK] OWL ontology saved to {output}")
        except ImportError:
            print("[WARNING] owlready2 not installed, skipping OWL export")
