"""
Audit command handler.
"""

from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

from ..adapters import OwlConflictCheck, get_world, load_graph
from ..auditor import run_audit


def handle_audit(args: argparse.Namespace) -> None:
    """Execute the audit command."""
    graph = load_graph(Path(args.graph))
    report = run_audit(graph)

    if getattr(args, "sync_check", False):
        try:
            world = get_world()
            owl_check = OwlConflictCheck(world)
            owl_findings = owl_check.run(graph)
            report.findings.extend(owl_findings)
        except ImportError:
            pass

    if args.format == "json":
        print(
            json.dumps(
                {
                    "summary": report.summary,
                    "findings": [
                        {
                            "check": f.check_name,
                            "node_id": f.node_id,
                            "detail": f.detail,
                        }
                        for f in report.findings
                    ],
                },
                indent=2,
            )
        )
    else:
        print("## Audit Report\n")
        for check_name, count in report.summary.items():
            print(f"- **{check_name}**: {count} finding(s)")
        if report.findings:
            print()
            for f in report.findings:
                print(f"[{f.check_name}] {f.node_id}\n  {f.detail}")
    if report.findings:
        sys.exit(1)
