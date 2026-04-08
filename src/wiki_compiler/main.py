"""
Entry point for the Wiki Compiler CLI, coordinating build, audit, and query operations.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .auditor import run_audit
from .builder import build_wiki
from .context import render_context
from .facet_validator import validate_facet_proposal
from .graph_utils import load_graph
from .ingest import ingest_raw_sources
from .query_executor import execute_query
from .query_language import StructuredQuery
from .query_server import query_main
from .registry import build_default_registry
from .scaffolder import generate_scaffolding, init_repository
from .validator import validate_topology_proposal


def main() -> None:
    """
    Parses command-line arguments and dispatches to the appropriate sub-command handler.
    """
    parser = build_parser()
    args = parser.parse_args()
    try:
        if args.command == "scaffold":
            generate_scaffolding(Path(args.module), args.intent)
            print(f"[OK] Scaffolding successfully created in {args.module}")
            return
        if args.command == "build":
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
            return
        if args.command == "query":
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
            )
            return
        if args.command == "audit":
            graph = load_graph(Path(args.graph))
            report = run_audit(graph)
            if args.format == "json":
                print(json.dumps({
                    "summary": report.summary,
                    "findings": [
                        {"check": f.check_name, "node_id": f.node_id, "detail": f.detail}
                        for f in report.findings
                    ],
                }, indent=2))
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
            return
        if args.command == "propose-facet":
            from .contracts import FacetProposal
            proposal_data = json.loads(Path(args.proposal).read_text(encoding="utf-8"))
            proposal = FacetProposal.model_validate(proposal_data)
            registry = build_default_registry()
            import networkx as nx
            graph = load_graph(Path(args.graph)) if Path(args.graph).exists() else nx.DiGraph()
            report = validate_facet_proposal(
                proposal=proposal,
                registry=registry,
                graph=graph,
                state_path=Path(args.state_file),
            )
            print(json.dumps(report.model_dump(), indent=2))
            if not report.is_orthogonal:
                sys.exit(1)
            return
        if args.command == "validate":
            proposal_data = json.loads(Path(args.proposal).read_text(encoding="utf-8"))
            report = validate_topology_proposal(
                proposal_data=proposal_data,
                graph_path=Path(args.graph),
                glossary_path=Path(args.glossary),
                state_path=Path(args.state_file),
            )
            print(json.dumps(report.model_dump(), indent=2))
            if not report.is_orthogonal:
                sys.exit(1)
            return
        if args.command == "context":
            print(
                render_context(
                    graph_path=Path(args.graph),
                    node_ids=args.nodes,
                    task_hint=args.task,
                    depth=args.depth,
                    output_format=args.format,
                    include_planned=args.include_planned,
                )
            )
            return
        if args.command == "ingest":
            written = ingest_raw_sources(
                source_dir=Path(args.source),
                dest_dir=Path(args.dest),
                project_root=Path(args.project_root),
                overwrite=args.overwrite,
            )
            print(json.dumps([path.as_posix() for path in written], indent=2))
            return
        if args.command == "compose":
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
            lines.extend([
                "---",
                "",
                f"# {args.title}",
                "",
                args.abstract,
                "",
            ])
            for nid in node_ids:
                # Extract slug from node_id (e.g., 'doc:wiki/foo.md' -> 'foo')
                slug = Path(nid.split(":")[-1]).stem
                lines.append(f"![[{slug}]]")
            
            output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            print(f"[OK] Composite node created at {args.output}")
            return
        if args.command == "init":
            init_repository()
            print("[OK] Wikipu ecosystem initialized. Base folders created.")
            return
    except Exception as exc:
        print(f"[ERROR] {exc}")
        sys.exit(1)


def build_parser() -> argparse.ArgumentParser:
    """
    Constructs the argument parser with all supported sub-commands and options.
    """
    parser = argparse.ArgumentParser(description="LLM Wiki Compiler")
    subparsers = parser.add_subparsers(dest="command", required=True)

    scaffold_parser = subparsers.add_parser(
        "scaffold", help="Generate boilerplate for a new module"
    )
    scaffold_parser.add_argument("--module", required=True, help="Path to the module")
    scaffold_parser.add_argument(
        "--intent", required=True, help="Purpose of the module"
    )

    build_parser = subparsers.add_parser(
        "build", help="Compile the wiki and generate the graph"
    )
    build_parser.add_argument(
        "--source", default="wiki", help="Source wiki directory"
    )
    build_parser.add_argument(
        "--graph", default="knowledge_graph.json", help="NetworkX JSON output path"
    )
    build_parser.add_argument(
        "--project-root", default=".", help="Project root used for source scanning"
    )
    build_parser.add_argument(
        "--code-root",
        action="append",
        default=["src"],
        help="Python source root to scan",
    )
    build_parser.add_argument(
        "--baseline",
        default=".compliance_baseline.json",
        help="Compliance baseline path",
    )
    build_parser.add_argument(
        "--update-baseline",
        action="store_true",
        help="Overwrite the compliance baseline",
    )

    query_parser = subparsers.add_parser("query", help="Query a knowledge graph export")
    query_parser.add_argument(
        "--graph", default="knowledge_graph.json", help="Graph JSON path"
    )
    query_parser.add_argument(
        "--type",
        choices=["get_node", "get_ancestors", "get_descendants", "find_by_io"],
    )
    query_parser.add_argument("--node-id", help="Node identifier")
    query_parser.add_argument(
        "--relation-filter", help="Restrict traversal to a relation type"
    )
    query_parser.add_argument("--medium", help="Filter I/O medium")
    query_parser.add_argument("--schema-ref", help="Filter I/O schema")
    query_parser.add_argument("--path-template", help="Filter I/O path template")
    query_parser.add_argument("--query-file", help="Path to a StructuredQuery JSON file")

    audit_parser = subparsers.add_parser("audit", help="Run documentation quality checks")
    audit_parser.add_argument("--graph", default="knowledge_graph.json")
    audit_parser.add_argument("--format", default="markdown", choices=["markdown", "json"])

    propose_facet_parser = subparsers.add_parser(
        "propose-facet", help="Validate a new facet proposal for orthogonality"
    )
    propose_facet_parser.add_argument(
        "--proposal", required=True, help="FacetProposal JSON file"
    )
    propose_facet_parser.add_argument(
        "--graph", default="knowledge_graph.json", help="Graph JSON path"
    )
    propose_facet_parser.add_argument(
        "--state-file", default=".facet_proposal_state.json", help="Attempt state file"
    )

    validate_parser = subparsers.add_parser(
        "validate", help="Validate a topology proposal"
    )
    validate_parser.add_argument(
        "--proposal", required=True, help="TopologyProposal JSON file"
    )
    validate_parser.add_argument(
        "--graph", default="knowledge_graph.json", help="Graph JSON path"
    )
    validate_parser.add_argument(
        "--glossary", default="wiki/domain_glossary.yaml", help="Glossary YAML path"
    )
    validate_parser.add_argument(
        "--state-file",
        default=".validation_session.json",
        help="Validation attempt state file",
    )

    context_parser = subparsers.add_parser(
        "context", help="Render focused graph context"
    )
    context_parser.add_argument(
        "--graph", default="knowledge_graph.json", help="Graph JSON path"
    )
    context_parser.add_argument("--nodes", nargs="*", help="Entry-point node ids")
    context_parser.add_argument(
        "--task", help="Task hint used to select relevant nodes"
    )
    context_parser.add_argument(
        "--depth", type=int, default=1, help="Neighborhood depth"
    )
    context_parser.add_argument(
        "--format",
        default="markdown",
        choices=["markdown", "json"],
        help="Output format",
    )
    context_parser.add_argument(
        "--include-planned",
        action="store_true",
        help="Include planned nodes in the output",
    )

    ingest_parser = subparsers.add_parser(
        "ingest", help="Create draft wiki nodes from raw sources"
    )
    ingest_parser.add_argument("--source", default="raw", help="Raw source directory")
    ingest_parser.add_argument(
        "--dest", default="wiki/drafts", help="Draft node destination"
    )
    ingest_parser.add_argument(
        "--project-root", default=".", help="Project root used for .wikiignore lookup"
    )
    ingest_parser.add_argument(
        "--overwrite", action="store_true", help="Overwrite existing draft files"
    )
    ingest_parser.add_argument(
        "--model", help="Reserved for future LLM-backed extraction"
    )

    compose_parser = subparsers.add_parser(
        "compose", help="Create a composite node from atomic ones"
    )
    compose_parser.add_argument("--nodes", required=True, help="Space-separated list of node IDs")
    compose_parser.add_argument("--title", required=True, help="Title of the composite node")
    compose_parser.add_argument("--abstract", required=True, help="Abstract of the composite node")
    compose_parser.add_argument("--output", required=True, help="Output markdown path")

    subparsers.add_parser("init", help="Initialize the base wikipu structure")
    return parser


if __name__ == "__main__":
    main()
