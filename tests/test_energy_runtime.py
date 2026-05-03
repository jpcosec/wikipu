from __future__ import annotations

import networkx as nx

from wiki_compiler.contracts import EnergyReport, ZoneContract
from wiki_compiler.energy import run_energy_audit


class _AuditReport:
    def __init__(self, findings: list[str]):
        self.findings = findings


def test_run_energy_audit_uses_wikipu_signals(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "wiki").mkdir()
    (tmp_path / "desk").mkdir()
    (tmp_path / "desk/agent_violations.log").write_text("one\ntwo\n", encoding="utf-8")

    graph = nx.DiGraph()
    graph.add_edge("a", "b")

    def audit_runner(_: nx.DiGraph) -> _AuditReport:
        return _AuditReport(["f1", "f2", "f3"])

    def status_builder(**_: object) -> dict[str, object]:
        return {
            "perturbations": [{"type": "modified_node"}, {"type": "other"}],
            "open_gates": [{"gate_id": "gate-001"}],
        }

    report = run_energy_audit(
        graph,
        tmp_path,
        audit_runner=audit_runner,
        status_builder=status_builder,
    )

    current = report.current_energy
    assert isinstance(report, EnergyReport)
    assert current.compliance_violations == 3
    assert current.perturbations == 2
    assert current.open_gates == 1
    assert current.agent_violations == 2
    assert current.violation_energy == 30.0
    assert current.perturbation_energy == 30.0
    assert current.agent_violation_energy == 50.0
    assert current.energy_score > 100.0
