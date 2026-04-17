"""OWL conflict detection check for audit."""

from __future__ import annotations
from typing import Optional

from .contracts import AuditFinding


class OwlConflictCheck:
    """Check for conflicts between Markdown edges and OWL triples."""

    check_name = "owl_conflict"
    question = "Which nodes have conflicts between Markdown and OWL?"
    related_facet = "compliance"

    def __init__(self, world=None):
        self.world = world

    def run(self, graph) -> list[AuditFinding]:
        """Execute the OWL conflict check."""
        findings = []

        if self.world is None:
            try:
                from wiki_compiler.owl_backend import get_world

                self.world = get_world()
            except ImportError:
                return findings

        try:
            from wiki_compiler.sync_gate import SyncGate

            gate = SyncGate(self.world)
            conflicts = gate.sync()

            for node_id, conflict_list in conflicts.items():
                for conflict in conflict_list:
                    findings.append(
                        AuditFinding(
                            check_name=self.check_name,
                            node_id=f"owl:{node_id}",
                            detail=f"OWL sync conflict: {conflict}",
                        )
                    )
        except Exception:
            pass

        return findings
