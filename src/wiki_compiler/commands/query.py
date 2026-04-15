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
