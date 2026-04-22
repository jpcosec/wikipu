"""
Scaffold command handler - creates wiki nodes using SLDB templates.
"""

from __future__ import annotations
import argparse
import json
import subprocess
import sys
from pathlib import Path


NODE_TYPE_MAP = {
    "concept": "wiki_compiler.contracts.wiki_nodes:ConceptDoc",
    "how_to": "wiki_compiler.contracts.wiki_nodes:HowToDoc",
    "doc_standard": "wiki_compiler.contracts.wiki_nodes:DocStandardDoc",
    "reference": "wiki_compiler.contracts.wiki_nodes:ReferenceDoc",
    "index": "wiki_compiler.contracts.wiki_nodes:IndexDoc",
    "adr": "wiki_compiler.contracts.wiki_nodes:ADRDoc",
    "selfDoc": "wiki_compiler.contracts.wiki_nodes:SelfDocDoc",
}

NODE_TYPE_QUESTION = {
    "concept": "What is X?",
    "how_to": "How do I do X?",
    "doc_standard": "What is the rule for X?",
    "reference": "How does X work technically?",
    "index": "What lives in this area?",
    "adr": "What architectural decision?",
    "selfDoc": "What is this system component?",
}


def handle_scaffold(args: argparse.Namespace) -> None:
    """Execute the scaffold command for wiki nodes."""
    if args.type == "module":
        from ..scaffolder import generate_scaffolding

        generate_scaffolding(Path(args.module), args.intent)
        print(f"[OK] Scaffolding successfully created in {args.module}")
    else:
        handle_wiki_scaffold(args)


def handle_wiki_scaffold(args: argparse.Namespace) -> None:
    """Create a new wiki node using SLDB template."""
    node_type = args.type
    title = args.title
    output_path = Path(args.output) if args.output else None

    if node_type not in NODE_TYPE_MAP:
        print(
            f"Error: Unknown node type '{node_type}'. Available: {list(NODE_TYPE_MAP.keys())}"
        )
        sys.exit(1)

    # Determine output path
    if not output_path:
        # Auto-generate path based on node type
        slug = title.lower().replace(" ", "_")
        type_dir = {
            "concept": "wiki/concepts",
            "how_to": "wiki/how_to",
            "doc_standard": "wiki/standards",
            "reference": "wiki/reference",
            "index": "wiki",
            "adr": "wiki/adrs",
            "selfDoc": "wiki/selfDocs",
        }.get(node_type, "wiki")
        output_path = Path(f"{type_dir}/{slug}.md")

    if output_path.exists() and not args.force:
        print(f"Error: {output_path} already exists. Use --force to overwrite.")
        sys.exit(1)

    # Generate node_id
    node_id = f"doc:{output_path}"

    # Build data for the model
    data = _build_scaffold_data(node_type, node_id, title)

    # Render using sldb
    model = NODE_TYPE_MAP[node_type]
    pythonpath = str(Path(__file__).parent.parent.parent / "src")

    try:
        result = subprocess.run(
            ["sldb", "render", model, "-", "-", "--pythonpath", pythonpath],
            input=json.dumps(data),
            capture_output=True,
            text=True,
            timeout=30,
        )

        if result.returncode != 0:
            print(f"Error rendering template: {result.stderr}")
            sys.exit(1)

        # Write the file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(result.stdout)
        print(f"[OK] Created {node_type} at {output_path}")

    except subprocess.TimeoutExpired:
        print("Error: sldb render timed out")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: sldb command not found. Install with: pip install sldb")
        sys.exit(1)


def _build_scaffold_data(node_type: str, node_id: str, title: str) -> dict:
    """Build the data dictionary for a given node type."""

    # Build frontmatter based on node type
    fm = {
        "identity": {"node_id": node_id, "node_type": node_type},
        "edges": [],
        "compliance": {"status": "planned", "failing_standards": []},
    }

    if node_type == "adr":
        # Extract ADR number from title
        parts = title.split(":", 1)
        adr_id = parts[0].strip() if ":" in title else "000"
        adr_title = parts[1].strip() if len(parts) > 1 else title

        fm["adr"] = {"decision_id": adr_id, "status": "proposed", "context_summary": ""}

        return {
            "frontmatter": fm,
            "title": adr_title,
            "abstract": "",
            "context": "",
            "decision": "",
            "consequences": "",
        }

    base = {"frontmatter": fm, "title": title, "abstract": ""}

    if node_type == "concept":
        return {
            **base,
            "definition": "",
            "examples": [],
            "related_concepts": [],
        }

    if node_type == "how_to":
        return {
            **base,
            "prerequisites": [],
            "steps": [],
            "verification": "",
        }

    if node_type in ("doc_standard", "reference"):
        return {
            **base,
            "signature_or_schema": "",
            "rule_schema": "",
            "fields": [],
            "usage_examples": [],
        }

    if node_type == "index":
        return {**base, "content": ""}

    if node_type == "selfDoc":
        return {**base, "content": ""}

    return base
