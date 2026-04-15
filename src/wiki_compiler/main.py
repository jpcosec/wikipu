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
from .energy import run_energy_audit, DRIFT_PENALTY_WEIGHT
from .facet_validator import validate_facet_proposal
from .graph_utils import load_graph
from .contracts import CleansingReport
from .perception import build_status_report
from .query_server import query_main
from .registry import build_default_registry
from .scaffolder import generate_scaffolding, init_repository
from .validator import validate_topology_proposal
from .workflow_guard import guard_workflow
from .workflow_guard import read_current_branch
from .workflow_guard import read_git_changes
from .commands import (
    build,
    query,
    audit,
    context,
    cleanse,
    ingest,
    curate,
    compose,
    scaffold,
    status,
    energy,
)


def main() -> None:
    """
    Parses command-line arguments and dispatches to the appropriate sub-command handler.
    """
    parser = build_parser()
    args = parser.parse_args()
    try:
        if args.command == "scaffold":
            scaffold.handle_scaffold(args)
            return
        if args.command == "build":
            build.handle_build(args)
            return
        if args.command == "query":
            query.handle_query(args)
            return
        if args.command == "audit":
            audit.handle_audit(args)
            return
        if args.command == "propose-facet":
            from .contracts import FacetProposal

            proposal_data = json.loads(Path(args.proposal).read_text(encoding="utf-8"))
            proposal = FacetProposal.model_validate(proposal_data)
            registry = build_default_registry()
            import networkx as nx

            graph = (
                load_graph(Path(args.graph))
                if Path(args.graph).exists()
                else nx.DiGraph()
            )
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
        if args.command == "validate-wiki":
            from .artifact_validation import (
                validate_wiki_artifact,
                validate_all_artifacts,
            )

            if args.all:
                reports = validate_all_artifacts(project_root=Path("."))
                all_valid = True
                for report in reports:
                    if not report.is_valid:
                        all_valid = False
                        print(json.dumps(report.model_dump(), indent=2))
                if not all_valid:
                    sys.exit(1)
                print(f"[OK] Validated {len(reports)} artifacts.")
                return

            if args.path:
                report = validate_wiki_artifact(Path(args.path))
                print(json.dumps(report.model_dump(), indent=2))
                if not report.is_valid:
                    sys.exit(1)
                return
            raise ValueError("validate-wiki requires --path <path> or --all")
        if args.command == "context":
            context.handle_context(args)
            return
        if args.command == "cleanse":
            cleanse.handle_cleanse(args)
            return
        if args.command == "ingest":
            ingest.handle_ingest(args)
            return
        if args.command == "curate":
            curate.handle_curate(args)
            return
        if args.command == "compose":
            compose.handle_compose(args)
            return
        if args.command == "init":
            init_repository()
            return
        if args.command == "bootstrap":
            from .scaffolder import bootstrap_repository

            bootstrap_repository(
                project_root=Path(args.project),
                project_name=args.name,
            )
            return
        if args.command == "upgrade":
            from .scaffolder import upgrade_repository

            upgrade_repository(project_root=Path("."))
            return
        if args.command == "history":
            from .session_storage import list_sessions

            sessions = list_sessions(Path(args.project_root))
            recent = sessions[-args.limit :]
            if not recent:
                print("No session history found.")
                return

            print(f"## Session History (showing last {len(recent)})\n")
            for s in reversed(recent):
                print(f"### Session: {s.session_id}")
                print(f"- Time: {s.start_time}")
                if s.branch:
                    print(f"- Branch: {s.branch}")
                if s.resolved_issues:
                    print(f"- Resolved: {', '.join(s.resolved_issues)}")
                if s.pending_issues:
                    print(f"- Pending: {', '.join(s.pending_issues)}")
                if s.trails and s.trails.artifacts:
                    print("- Trails:")
                    for a in s.trails.artifacts:
                        print(f"  - [{a.kind}] {a.content} -> {a.destination}")
                print("")
            return
        if args.command == "run":
            # First, guard the workflow
            report = guard_workflow(
                read_git_changes(Path(args.project_root)),
                branch_name=read_current_branch(Path(args.project_root)),
                allow_structural=False,  # run should not be structural
            )
            if report.checked_files:
                print("[INFO] Checked files:")
                for path in report.checked_files:
                    print(f"- {path}")
            if report.errors:
                for error in report.errors:
                    print(f"[ERROR] {error}")
                sys.exit(1)
            print("[OK] Workflow discipline checks passed.")

            # Then, run the coordinator cycle
            from .coordinator import run_coordinator_cycle

            result = run_coordinator_cycle(
                project_root=Path(args.project_root),
                graph_path=Path(args.graph),
                wiki_dir=Path(args.source),
                manifest_path=Path(args.manifest),
            )
            print(json.dumps(result, indent=2))
            return
        if args.command == "guard":
            report = guard_workflow(
                read_git_changes(Path(args.project_root)),
                branch_name=read_current_branch(Path(args.project_root)),
                allow_structural=args.allow_structural,
            )
            if report.checked_files:
                print("[INFO] Checked files:")
                for path in report.checked_files:
                    print(f"- {path}")
            if report.errors:
                for error in report.errors:
                    print(f"[ERROR] {error}")
                sys.exit(1)
            print("[OK] Workflow discipline checks passed.")
            return
        if args.command == "drafts":
            from .drafts import (
                detect_stale_nodes,
                write_stale_drafts,
                promote_draft_node,
            )

            if args.detect_stale:
                stale_ids = detect_stale_nodes(
                    graph_path=Path(args.graph),
                    manifest_path=Path(args.manifest),
                )
                print(json.dumps(stale_ids, indent=2))
                return
            if args.write_drafts:
                written = write_stale_drafts(
                    graph_path=Path(args.graph),
                    manifest_path=Path(args.manifest),
                    drafts_dir=Path(args.drafts_dir),
                )
                print(json.dumps([path.as_posix() for path in written], indent=2))
                return
            if args.promote:
                dest = promote_draft_node(
                    node_id=args.promote,
                    drafts_dir=Path(args.drafts_dir),
                )
                print(f"[OK] Promoted {args.promote} to {dest}")
                return
            raise ValueError(
                "drafts requires --detect-stale, --write-drafts, or --promote <id>"
            )
        if args.command == "status":
            status.handle_status(args)
            return
        if args.command == "energy":
            energy.handle_energy(args)
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
    build_parser.add_argument("--source", default="wiki", help="Source wiki directory")
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
    query_parser.add_argument(
        "--query-file", help="Path to a StructuredQuery JSON file"
    )
    query_parser.add_argument(
        "--tasks", action="store_true", help="Find all task nodes"
    )
    query_parser.add_argument(
        "--search", help="Free text search across markdown files in the wiki"
    )
    query_parser.add_argument(
        "--gaps", action="store_true", help="Find all gap task nodes"
    )
    query_parser.add_argument(
        "--unimplemented", action="store_true", help="Find all unimplemented task nodes"
    )

    audit_parser = subparsers.add_parser(
        "audit", help="Run documentation quality checks"
    )
    audit_parser.add_argument("--graph", default="knowledge_graph.json")
    audit_parser.add_argument(
        "--format", default="markdown", choices=["markdown", "json"]
    )

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

    validate_wiki_parser = subparsers.add_parser(
        "validate-wiki", help="Validate authored wiki artifacts"
    )
    validate_wiki_parser.add_argument(
        "--path", help="Path to a single wiki artifact markdown file"
    )
    validate_wiki_parser.add_argument(
        "--all", action="store_true", help="Validate all wiki and operational artifacts"
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

    cleanse_parser = subparsers.add_parser(
        "cleanse", help="Detect or apply structural cleansing proposals"
    )
    cleanse_mode = cleanse_parser.add_mutually_exclusive_group(required=True)
    cleanse_mode.add_argument(
        "--detect", action="store_true", help="Detect cleansing candidates"
    )
    cleanse_mode.add_argument(
        "--apply", help="Apply one approved cleansing proposal report"
    )
    cleanse_parser.add_argument(
        "--graph", default="knowledge_graph.json", help="Graph JSON path"
    )

    ingest_parser = subparsers.add_parser(
        "ingest", help="Create draft wiki nodes from raw sources"
    )
    ingest_parser.add_argument("--source", default="raw", help="Raw source directory")
    ingest_parser.add_argument(
        "--dest", default="desk/drafts", help="Draft node destination"
    )
    ingest_parser.add_argument(
        "--project-root", default=".", help="Project root used for .wikiignore lookup"
    )
    ingest_parser.add_argument(
        "--overwrite", action="store_true", help="Overwrite existing draft files"
    )
    ingest_parser.add_argument(
        "--manifest",
        help="Optional path to the CSV manifest file to update during ingestion.",
    )
    ingest_parser.add_argument(
        "--model", help="Reserved for future LLM-backed extraction"
    )

    curate_parser = subparsers.add_parser(
        "curate", help="Score or promote draft wiki nodes"
    )
    curate_mode = curate_parser.add_mutually_exclusive_group(required=True)
    curate_mode.add_argument(
        "--score", action="store_true", help="Score all draft wiki nodes"
    )
    curate_mode.add_argument(
        "--promote",
        nargs=2,
        metavar=("NODE_ID", "DEST"),
        help="Promote one draft node into wiki/<DEST>",
    )
    curate_parser.add_argument(
        "--graph", default="knowledge_graph.json", help="Graph JSON path"
    )
    curate_parser.add_argument(
        "--drafts-dir", default="desk/drafts", help="Draft wiki directory"
    )
    curate_parser.add_argument(
        "--wiki-dir", default="wiki", help="Canonical wiki directory"
    )

    compose_parser = subparsers.add_parser(
        "compose", help="Create a composite node from atomic ones"
    )
    compose_parser.add_argument(
        "--nodes", required=True, help="Space-separated list of node IDs"
    )
    compose_parser.add_argument(
        "--title", required=True, help="Title of the composite node"
    )
    compose_parser.add_argument(
        "--abstract", required=True, help="Abstract of the composite node"
    )
    compose_parser.add_argument("--output", required=True, help="Output markdown path")

    workflow_parser = subparsers.add_parser(
        "guard", help="Validate issue and changelog discipline"
    )
    workflow_parser.add_argument(
        "--project-root", default=".", help="Git repository root to inspect"
    )
    workflow_parser.add_argument(
        "--allow-structural",
        action="store_true",
        help="Allow docs-only structural work without an issue link",
    )

    status_parser = subparsers.add_parser(
        "status", help="Report git-backed drift and untracked raw files"
    )
    status_parser.add_argument(
        "--graph", default="knowledge_graph.json", help="Graph JSON path"
    )
    status_parser.add_argument(
        "--project-root", default=".", help="Project root directory"
    )

    energy_parser = subparsers.add_parser(
        "energy",
        help="Calculate the systemic energy score (structural and operational cost)",
    )
    energy_parser.add_argument(
        "--graph", default="knowledge_graph.json", help="Graph JSON path"
    )
    energy_parser.add_argument(
        "--project-root", default=".", help="Project root directory"
    )
    energy_parser.add_argument(
        "--format", default="markdown", choices=["markdown", "json"]
    )

    subparsers.add_parser("init", help="Initialize the base wikipu structure")

    # --- manifest ---
    manifest_parser = subparsers.add_parser(
        "manifest",
        help="Manage the raw source manifest for file provenance.",
    )
    manifest_parser.add_argument(
        "--add", help="Relative path to a raw source file to register."
    )
    manifest_parser.add_argument(
        "--manifest",
        default="manifests/raw_sources.csv",
        help="Path to the CSV manifest file.",
    )
    manifest_parser.add_argument(
        "--notes", default="", help="Optional notes for the manifest entry."
    )

    # --- drafts ---
    drafts_parser = subparsers.add_parser(
        "drafts",
        help="Manage wiki draft stubs and stale node detection.",
    )
    drafts_parser.add_argument(
        "--detect-stale", action="store_true", help="Detect stale wiki nodes"
    )
    drafts_parser.add_argument(
        "--write-drafts", action="store_true", help="Write draft stubs for stale nodes"
    )
    drafts_parser.add_argument(
        "--promote", help="Promote a draft node ID to the live wiki"
    )
    drafts_parser.add_argument(
        "--graph", default="knowledge_graph.json", help="Graph JSON path"
    )
    drafts_parser.add_argument(
        "--manifest",
        default="manifests/raw_sources.csv",
        help="Path to the CSV manifest file.",
    )
    drafts_parser.add_argument(
        "--drafts-dir", default="desk/drafts", help="Drafts destination directory"
    )

    # --- bootstrap ---
    bootstrap_parser = subparsers.add_parser(
        "bootstrap",
        help="Scaffold a new Wikipu project from scratch.",
    )
    bootstrap_parser.add_argument(
        "--project", required=True, help="Path to the project root directory."
    )
    bootstrap_parser.add_argument(
        "--name", default="New Project", help="Name of the project."
    )

    # --- upgrade ---
    subparsers.add_parser(
        "upgrade",
        help="Upgrade an existing project to the latest structure.",
    )

    # --- history ---
    history_parser = subparsers.add_parser(
        "history",
        help="Summarize session log history.",
    )
    history_parser.add_argument(
        "--limit", type=int, default=10, help="Max number of sessions to show."
    )
    history_parser.add_argument(
        "--project-root", default=".", help="Project root directory"
    )

    # --- run ---
    run_parser = subparsers.add_parser(
        "run",
        help="Run the autopoietic loop coordinator cycle.",
    )
    run_parser.add_argument(
        "--graph", default="knowledge_graph.json", help="Graph JSON path"
    )
    run_parser.add_argument(
        "--project-root", default=".", help="Project root directory"
    )
    run_parser.add_argument("--source", default="wiki", help="Source wiki directory")
    run_parser.add_argument(
        "--manifest",
        default="manifests/raw_sources.csv",
        help="Path to the CSV manifest file.",
    )

    return parser


if __name__ == "__main__":
    main()
