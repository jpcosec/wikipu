from __future__ import annotations
from pathlib import Path
import pytest
from wiki_compiler.preflight import evaluate_action_safety, select_minimal_energy_action

def test_preflight_zone_separation():
    # ID-4: writing to raw/ should be blocked
    finding = evaluate_action_safety("write", "raw/illegal.md", Path("."))
    assert finding is not None
    assert finding.rule_id == "ID-4"
    assert finding.severity == "error"
    assert finding.action_override == "abort"

def test_preflight_topology_boundary():
    # ID-5: writing outside safe zones should be gated
    finding = evaluate_action_safety("write", "external_config.json", Path("."))
    assert finding is not None
    assert finding.rule_id == "ID-5"
    assert finding.severity == "warning"
    assert finding.action_override == "gate"

def test_preflight_safe_action():
    finding = evaluate_action_safety("write", "wiki/concept.md", Path("."))
    assert finding is None

def test_minimal_energy_selection():
    # ID-2: Prefer update over rebuild
    candidates = ["rebuild", "update", "create"]
    selection = select_minimal_energy_action("perturbation", "id", candidates)
    assert selection == "update"
    
    # Prefer rebuild if update not present
    candidates = ["rebuild", "create"]
    selection = select_minimal_energy_action("perturbation", "id", candidates)
    assert selection == "rebuild"
