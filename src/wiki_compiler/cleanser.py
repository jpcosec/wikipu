"""Apply approved cleansing proposals on the filesystem."""

from __future__ import annotations

from pathlib import Path

from ontology.cleansing import detect_cleansing_candidates
from .contracts import CleansingProposal


def apply_cleansing_proposal(proposal: CleansingProposal, project_root: Path) -> None:
    """Executes one approved cleansing proposal on the filesystem."""
    # Note: node_id 'doc:wiki/foo.md' maps to 'wiki/foo.md' relative to project_root.
    # file: and code: nodes are derived from code, we don't 'cleanse' them by
    # editing code yet, usually we cleanse the doc nodes that point to them.
    # But some file: nodes might be config/data that we can destroy.

    if proposal.operation == "destroy":
        _execute_destroy(proposal, project_root)
    elif proposal.operation == "relocate":
        _execute_relocate(proposal, project_root)
    elif proposal.operation == "split":
        _execute_split(proposal, project_root)
    elif proposal.operation == "merge":
        _execute_merge(proposal, project_root)
    else:
        raise ValueError(f"Unknown cleansing operation: {proposal.operation}")


def _execute_destroy(proposal: CleansingProposal, project_root: Path) -> None:
    """Delete the file referenced by the proposal."""
    path = _node_id_to_path(proposal.node_id, project_root)
    if path and path.exists():
        path.unlink()
        print(f"[OK] Destroyed: {proposal.node_id} ({path.relative_to(project_root)})")
    else:
        print(f"[WARN] Could not destroy {proposal.node_id}: path not found.")


def _execute_relocate(proposal: CleansingProposal, project_root: Path) -> None:
    """Move the file to a new location based on affected_nodes."""
    # Relocate needs a destination in the proposal.
    # Current CleansingProposal doesn't have a 'destination' field.
    # We should probably add it or derive it from the rationale if it's there.
    # For now, let's assume it might be in affected_nodes[1] if operation is relocate.
    if len(proposal.affected_nodes) < 2:
        print(f"[ERROR] Relocate proposal for {proposal.node_id} missing destination.")
        return

    old_path = _node_id_to_path(proposal.node_id, project_root)
    new_node_id = proposal.affected_nodes[1]
    new_path = _node_id_to_path(new_node_id, project_root)

    if old_path and old_path.exists() and new_path:
        new_path.parent.mkdir(parents=True, exist_ok=True)
        old_path.rename(new_path)
        # We also need to update the node_id inside the frontmatter
        content = new_path.read_text(encoding="utf-8")
        updated = content.replace(
            f'node_id: "{proposal.node_id}"', f'node_id: "{new_node_id}"'
        )
        new_path.write_text(updated, encoding="utf-8")
        print(f"[OK] Relocated {proposal.node_id} to {new_node_id}")
    else:
        print(f"[ERROR] Could not relocate {proposal.node_id}.")


def _execute_split(proposal: CleansingProposal, project_root: Path) -> None:
    """Split a node into multiple nodes (requires manual intervention)."""
    # Split is complex: requires creating new nodes.
    # The proposal should ideally contain the new content or paths.
    # For now, we'll mark it as manual or needing more metadata.
    print(
        f"[INFO] Split operation for {proposal.node_id} requires manual intervention or more metadata."
    )


def _execute_merge(proposal: CleansingProposal, project_root: Path) -> None:
    """Merge multiple affected nodes into one."""
    if len(proposal.affected_nodes) < 2:
        return
    canonical = proposal.affected_nodes[0]
    to_dissolve = proposal.affected_nodes[1]

    dissolve_path = _node_id_to_path(to_dissolve, project_root)
    if dissolve_path and dissolve_path.exists():
        dissolve_path.unlink()
        print(f"[OK] Merged {to_dissolve} into {canonical} (dissolved {to_dissolve})")


def _node_id_to_path(node_id: str, project_root: Path) -> Path | None:
    """Convert a node_id to a file path."""
    if node_id.startswith("doc:"):
        return project_root / node_id.removeprefix("doc:")
    if node_id.startswith("file:"):
        return project_root / node_id.removeprefix("file:")
    return None
