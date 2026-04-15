"""Git-backed perception helpers for build and status reporting."""

from __future__ import annotations

import subprocess
from pathlib import Path

from .contracts import GitFacet, ZoneContract
from .graph_utils import iter_knowledge_nodes
from .graph_utils import load_graph

DEFAULT_ZONE_CONTRACTS = [
    ZoneContract(
        zone="raw",
        path="raw/",
        track_modified=False,
        track_untracked=True,
        energy_weight=1.0,
        response_action="ingest",
    ),
    ZoneContract(
        zone="exclusion",
        path="exclusion/",
        track_modified=False,
        track_untracked=False,
        energy_weight=0.0,
        response_action="ignore",
    ),
    ZoneContract(
        zone="wiki",
        path="wiki/",
        track_modified=True,
        track_untracked=False,
        energy_weight=1.0,
        response_action="rebuild",
    ),
    ZoneContract(
        zone="desk",
        path="desk/",
        track_modified=True,
        track_untracked=True,
        energy_weight=2.0,
        response_action="scan",
    ),
    ZoneContract(
        zone="drawers",
        path="drawers/",
        track_modified=True,
        track_untracked=True,
        energy_weight=0.5,
        response_action="review",
    ),
    ZoneContract(
        zone="src",
        path="src/",
        track_modified=True,
        track_untracked=False,
        energy_weight=1.5,
        response_action="audit",
    ),
]


def load_zone_contracts(project_root: Path | None = None) -> list[ZoneContract]:
    """Load zone contracts from wiki topology or return defaults."""
    if project_root is None:
        return DEFAULT_ZONE_CONTRACTS

    zones_md = project_root / "wiki/standards/zones.md"
    if not zones_md.exists():
        return DEFAULT_ZONE_CONTRACTS

    try:
        import yaml

        content = zones_md.read_text(encoding="utf-8")
        yaml_match = (
            __import__("re")
            .compile(r"\A---\s*\n(.*?)\n---(\s*\n|$)", __import__("re").DOTALL)
            .search(content)
        )
        if yaml_match:
            data = yaml.safe_load(yaml_match.group(1))
            if data and "zones" in data:
                return [ZoneContract(**zone) for zone in data["zones"]]
    except Exception:
        pass

    return DEFAULT_ZONE_CONTRACTS


def attach_git_facets(graph: object, project_root: Path) -> None:
    """Attach GitFacet metadata to doc/file nodes backed by real files."""
    for node in iter_knowledge_nodes(graph):
        file_path = node_id_to_path(project_root, node.identity.node_id)
        if file_path is None or not file_path.exists():
            continue
        node.git = build_git_facet(project_root, file_path)
        graph.nodes[node.identity.node_id]["schema"] = node.model_dump()


def build_status_report(
    graph_path: Path | None,
    project_root: Path,
    graph: object | None = None,
    zone_contracts: list[ZoneContract] | None = None,
) -> dict[str, object]:
    """Compare stored GitFacet data against the current worktree and report perturbations."""
    if graph is None:
        if graph_path is None:
            raise ValueError("Either graph or graph_path must be provided.")
        graph = load_graph(graph_path)

    if zone_contracts is None:
        zone_contracts = load_zone_contracts(project_root)

    contracts_by_path = {c.path: c for c in zone_contracts}

    modified_nodes: list[dict[str, str]] = []
    for node in iter_knowledge_nodes(graph):
        if node.git is None:
            continue
        file_path = node_id_to_path(project_root, node.identity.node_id)
        if file_path is None or not file_path.exists():
            continue
        current_sha = git_hash_object(project_root, file_path)
        if current_sha != node.git.blob_sha:
            modified_nodes.append(
                {
                    "node_id": node.identity.node_id,
                    "path": file_path.relative_to(project_root).as_posix(),
                    "stored_blob_sha": node.git.blob_sha,
                    "current_blob_sha": current_sha,
                    "status": "modified_since_build",
                }
            )

    untracked_by_zone: dict[str, list[str]] = {}
    for contract in zone_contracts:
        if contract.track_untracked:
            zone_path = Path(contract.path)
            if zone_path.exists() or not is_git_tracked(
                project_root, project_root / zone_path
            ):
                untracked = git_untracked_files(project_root, zone_path)
                if untracked:
                    untracked_by_zone[contract.zone] = untracked

    raw_files = untracked_by_zone.get("raw", [])

    # Gate perception
    from .gates import load_gates

    gates_table = load_gates(project_root / "desk/Gates.md")
    open_gates = [g.model_dump() for g in gates_table.gates if g.status == "open"]

    # Classification using zone contracts
    perturbations: list[dict[str, str]] = []
    for node in modified_nodes:
        action = classify_perturbation_by_zones(node["node_id"], zone_contracts)
        perturbations.append(
            {
                "type": "modified_node",
                "id": node["node_id"],
                "action": action,
                "zone": get_zone_for_path(node["path"], zone_contracts),
            }
        )
    for zone_name, files in untracked_by_zone.items():
        for file_path in files:
            contract = contracts_by_path.get(f"{zone_name}/")
            action = contract.response_action if contract else "ignore"
            perturbations.append(
                {
                    "type": "untracked_file",
                    "id": file_path,
                    "action": action,
                    "zone": zone_name,
                }
            )
    for gate in open_gates:
        perturbations.append(
            {
                "type": "open_gate",
                "id": gate["gate_id"],
                "action": "await_human_approval",
                "zone": "desk",
            }
        )

    return {
        "modified_nodes": modified_nodes,
        "untracked_by_zone": untracked_by_zone,
        "open_gates": open_gates,
        "perturbations": perturbations,
    }


def classify_perturbation(p_type: str, p_id: str) -> str:
    """Classifies a perturbation into a recommended system response."""
    if p_type == "modified_node":
        if p_id.startswith("doc:wiki/"):
            return "rebuild_graph"
        if p_id.startswith("file:src/"):
            return "rebuild_graph_and_audit"
    if p_type == "untracked_raw":
        return "ingest_raw_source"
    return "ignore"


def classify_perturbation_by_zones(
    node_id: str, zone_contracts: list[ZoneContract]
) -> str:
    """Classify perturbation based on zone contracts."""
    for contract in zone_contracts:
        if node_id.startswith(f"doc:{contract.path}") or node_id.startswith(
            f"file:{contract.path}"
        ):
            return contract.response_action
    return "ignore"


def get_zone_for_path(file_path: str, zone_contracts: list[ZoneContract]) -> str | None:
    """Get the zone for a given file path."""
    for contract in zone_contracts:
        if file_path.startswith(contract.path):
            return contract.zone
    return None


def build_git_facet(project_root: Path, file_path: Path) -> GitFacet:
    """Build GitFacet metadata for one file path."""
    status = "tracked" if is_git_tracked(project_root, file_path) else "untracked"
    last_commit, last_author = git_last_commit(project_root, file_path)
    return GitFacet(
        blob_sha=git_hash_object(project_root, file_path),
        created_at_commit=git_first_commit(project_root, file_path),
        last_modified_commit=last_commit,
        last_modified_author=last_author,
        status=status,
    )


def node_id_to_path(project_root: Path, node_id: str) -> Path | None:
    """Map a graph node id to a filesystem path when it represents a file."""
    for prefix in ("doc:", "file:"):
        if node_id.startswith(prefix):
            return project_root / node_id[len(prefix) :]
    return None


def git_hash_object(project_root: Path, file_path: Path) -> str:
    """Return the git blob hash for a file."""
    result = subprocess.run(
        ["git", "hash-object", file_path.relative_to(project_root).as_posix()],
        cwd=project_root,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def git_last_commit(
    project_root: Path, file_path: Path
) -> tuple[str | None, str | None]:
    """Return the last commit SHA and author email for a file."""
    result = subprocess.run(
        [
            "git",
            "log",
            "--follow",
            "-1",
            "--format=%H|%ae",
            "--",
            file_path.relative_to(project_root).as_posix(),
        ],
        cwd=project_root,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None, None
    if not result.stdout.strip():
        return None, None
    commit, author = result.stdout.strip().split("|", maxsplit=1)
    return commit, author


def git_first_commit(project_root: Path, file_path: Path) -> str | None:
    """Return the first commit SHA that introduced a file, if available."""
    result = subprocess.run(
        [
            "git",
            "log",
            "--follow",
            "--format=%H",
            "--",
            file_path.relative_to(project_root).as_posix(),
        ],
        cwd=project_root,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None
    lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return lines[-1] if lines else None


def is_git_tracked(project_root: Path, file_path: Path) -> bool:
    """Return True when a file is tracked by git."""
    result = subprocess.run(
        [
            "git",
            "ls-files",
            "--error-unmatch",
            file_path.relative_to(project_root).as_posix(),
        ],
        cwd=project_root,
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def git_untracked_files(project_root: Path, relative_root: Path) -> list[str]:
    """Return untracked files under a relative subtree."""
    result = subprocess.run(
        ["git", "ls-files", "--others", "--exclude-standard", relative_root.as_posix()],
        cwd=project_root,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        search_root = project_root / relative_root
        if not search_root.exists():
            return []
        return sorted(
            path.relative_to(project_root).as_posix()
            for path in search_root.rglob("*")
            if path.is_file()
        )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]
