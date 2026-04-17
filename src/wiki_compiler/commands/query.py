"""
Query command handler.
"""

from __future__ import annotations
import argparse
import json
from pathlib import Path

from ..graph_utils import load_graph
from ..query_executor import execute_query
from ..query_language import StructuredQuery
from ..query_server import query_main


def handle_query(args: argparse.Namespace) -> None:
    """Execute the query command."""
    if getattr(args, "query_file", None):
        graph = load_graph(Path(args.graph))
        query_data = json.loads(Path(args.query_file).read_text(encoding="utf-8"))
        query = StructuredQuery.model_validate(query_data)
        results = execute_query(graph, query)
        print(json.dumps([n.model_dump() for n in results], indent=2))
        return

    if getattr(args, "owl", None):
        _handle_owl_query(args)
        return

    query_main(
        graph_path=Path(args.graph),
        query_type=args.type,
        node_id=args.node_id,
        relation_filter=args.relation_filter,
        medium=args.medium,
        schema_ref=args.schema_ref,
        path_template=args.path_template,
        tasks=args.tasks,
        gaps=args.gaps,
        unimplemented=args.unimplemented,
        search_query=args.search,
    )


def _handle_owl_query(args: argparse.Namespace) -> None:
    """Execute a SPARQL query against the OWL quadstore."""
    try:
        from wiki_compiler.owl_backend.extractor import get_world
    except ImportError:
        print("[ERROR] rdflib not installed. Run: pip install rdflib")
        return

    sparql = getattr(args, "owl", "")
    if not sparql:
        print("[ERROR] --owl requires a SPARQL query string")
        return

    graph = get_world()

    try:
        results = graph.query(sparql)
        serialized_results = []
        for row in results:
            serialized_row = [
                str(item) if hasattr(item, "__str__") else item for item in row
            ]
            serialized_results.append(serialized_row)
        print(
            json.dumps(
                {"results": serialized_results, "count": len(serialized_results)},
                indent=2,
            )
        )
    except Exception as exc:
        print(f"[ERROR] SPARQL query failed: {exc}")
