"""
Cleanse command handler.
"""

from __future__ import annotations
import argparse
import json
from pathlib import Path

from ..cleanser import detect_cleansing_candidates, apply_cleansing_proposal
from ..contracts import CleansingReport


def handle_cleanse(args: argparse.Namespace) -> None:
    """Execute the cleanse command."""
    if args.detect:
        report = detect_cleansing_candidates(Path(args.graph))
        print(json.dumps(report.model_dump(), indent=2))
        return
    if args.apply:
        report_data = json.loads(Path(args.apply).read_text(encoding="utf-8"))
        report = CleansingReport.model_validate(report_data)
        for proposal in report.proposals:
            apply_cleansing_proposal(proposal, project_root=Path("."))
        return
    raise ValueError("cleanse requires --detect or --apply <report.json>")
