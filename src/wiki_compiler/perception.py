"""Git-backed perception helpers for build and status reporting."""

from __future__ import annotations

import subprocess
from pathlib import Path

from .contracts import GitFacet
from .graph_utils import iter_knowledge_nodes
from .graph_utils import load_graph


def attach_git_facets(graph: object, project_root: Path) -> None:
    """Attach GitFacet metadata to doc/file nodes backed by real files."""
    for node in iter_knowledge_nodes(graph):
        file_path = node_id_to_path(project_root, node.identity.node_id)
        if file_path is None or not file_path.exists():
            continue
        node.git = build_git_facet(project_root, file_path)
        graph.nodes[node.identity.node_id]["schema"] = node.model_dump()


def build_status_report(graph_path: Path, project_root: Path) -> dict[str, object]:
    """Compare stored GitFacet data against the current worktree and report perturbations."""
    graph = load_graph(graph_path)
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
    
    untracked_raw = git_untracked_files(project_root, Path("raw"))
    
    # Gate perception
    from .gates import load_gates
    gates_table = load_gates(project_root / "desk/Gates.md")
    open_gates = [g.model_dump() for g in gates_table.gates if g.status == "open"]
    
    # Classification
    perturbations: list[dict[str, str]] = []
    for node in modified_nodes:
        perturbations.append({
            "type": "modified_node",
            "id": node["node_id"],
            "action": classify_perturbation("modified_node", node["node_id"])
        })
    for raw in untracked_raw:
        perturbations.append({
            "type": "untracked_raw",
            "id": raw,
            "action": classify_perturbation("untracked_raw", raw)
        })
    for gate in open_gates:
        perturbations.append({
            "type": "open_gate",
            "id": gate["gate_id"],
            "action": "await_human_approval"
        })

    return {
        "modified_nodes": modified_nodes,
        "untracked_raw_files": untracked_raw,
        "open_gates": open_gates,
        "perturbations": perturbations
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
