"""
Compose command handler.
"""

from __future__ import annotations
import argparse
from pathlib import Path


def handle_compose(args: argparse.Namespace) -> None:
    """Execute the compose command."""
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    node_ids = args.nodes.split()
    lines = [
        "---",
        "identity:",
        f'  node_id: "doc:{output_path.as_posix()}"',
        '  node_type: "index"',
        "edges:",
    ]
    for nid in node_ids:
        lines.append(f'  - {{target_id: "{nid}", relation_type: "transcludes"}}')
    lines.extend(
        [
            "---",
            "",
            f"# {args.title}",
            "",
            args.abstract,
            "",
        ]
    )
    for nid in node_ids:
        slug = Path(nid.split(":")[-1]).stem
        lines.append(f"![[{slug}]]")

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[OK] Composite node created at {args.output}")
