"""
Energy and Zone models for the Knowledge Graph.
"""

from pydantic import BaseModel, Field
from typing import Literal


class SystemicEnergy(BaseModel):
    """
    ID-2: Minimal Energy.
    The conceptual and structural cost of the current system state.
    """

    energy_score: float = Field(description="The total calculated energy score.")
    node_count: int = Field(description="Total number of nodes in the graph.")
    edge_count: int = Field(description="Total number of edges in the graph.")
    compliance_violations: int = Field(
        description="Total number of failing standards across all nodes."
    )
    perturbations: int = Field(
        description="Number of detected git-backed drifts or untracked files."
    )
    open_gates: int = Field(description="Number of active human-in-the-loop gates.")
    agent_violations: int = Field(
        default=0, description="Number of agent rule violations."
    )

    redundant_nodes: int = Field(
        default=0,
        description="Number of semantically redundant nodes.",
    )
    boilerplate_ratio: float = Field(
        default=0.0, description="Ratio of boilerplate to unique content."
    )

    long_files: int = Field(
        default=0, description="Number of files exceeding line threshold."
    )
    complex_functions: int = Field(
        default=0, description="Number of functions exceeding statement threshold."
    )

    drift_flags: int = Field(
        default=0, description="Number of code-doc drift violations detected."
    )

    structural_energy: float = Field(
        description="Energy from redundancy and boilerplate."
    )
    abstraction_energy: float = Field(
        default=0.0, description="Energy from descriptive abstraction penalties."
    )
    violation_energy: float = Field(
        description="Energy contributed by compliance debt."
    )
    perturbation_energy: float = Field(
        description="Energy contributed by systemic uncertainty/drift."
    )
    agent_violation_energy: float = Field(
        default=0.0, description="Energy contributed by agent rule violations."
    )

    fft_code_wiki_so: float = Field(
        default=0.0,
        description="Spectral overlap between code and wiki (lower = more distinct).",
    )
    fft_code_wiki_corr: float = Field(
        default=0.0,
        description="Correlation between code and wiki spectra (lower = more distinct).",
    )
    fft_code_within_so: float = Field(
        default=0.0,
        description="Average spectral overlap within code files (coherence).",
    )
    fft_code_within_corr: float = Field(
        default=0.0,
        description="Average correlation within code files (consistency).",
    )
    fft_complexity_score: float = Field(
        default=0.0,
        description="Complexity score from FFT variance (higher = more chaotic).",
    )
    fft_energy: float = Field(
        default=0.0,
        description="Energy contribution from FFT-based metrics.",
    )


class EnergyReport(BaseModel):
    """The result of an energy audit."""

    timestamp: str = Field(description="ISO-8601 timestamp of the measurement.")
    current_energy: SystemicEnergy = Field(
        description="The energy state at the time of measurement."
    )
    baseline_energy: SystemicEnergy | None = Field(
        default=None, description="The energy state at the last stable baseline."
    )
    delta: float = Field(
        default=0.0, description="The change in total energy since the baseline."
    )
    consistency_status: str | None = Field(
        default=None,
        description="OWL consistency check result (CONSISTENT/INCONSISTENT).",
    )
    reasoning_output: dict | None = Field(
        default=None, description="OWL reasoner output with inferred relationships."
    )
    inferred_relationships: list[dict] = Field(
        default_factory=list, description="Inferred class memberships from reasoner."
    )


class ZoneContract(BaseModel):
    """Declarative contract for zone-based sensing in perception and energy."""

    zone: str = Field(description="Zone name (e.g., 'raw', 'desk', 'drawers').")
    path: str = Field(description="Relative path to the zone directory.")
    track_modified: bool = Field(
        default=True, description="Whether to track modified files in this zone."
    )
    track_untracked: bool = Field(
        default=True, description="Whether to track untracked files in this zone."
    )
    energy_weight: float = Field(
        default=1.0, description="Weight multiplier for energy calculations."
    )
    response_action: str = Field(
        default="scan",
        description="Response action when perturbations detected.",
    )
