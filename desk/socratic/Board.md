# Socratic Interrogation: First-Class Concept of "Contradiction"

**Input Artifact:** Proposal to define "Contradiction" as a first-class concept within the Wikipu topology, beyond its current use in Socratic methodology, to enable its direct measurement and resolution.

## Open Questions

### 1. Missing Constraint
**Claim:** "Contradiction" can be a first-class concept to be solved by a mechanism not yet mapped.
**Question:** If contradiction is a fundamental issue, how do we prevent its proliferation? What is the *cost* of a contradiction in terms of energy? Does it have a compliance status, similar to how `failing_standards` are tracked? What mechanisms automatically detect and flag contradictions (e.g., semantic vs. structural)?
**Resolution:** Define the types of contradictions (semantic, structural, temporal, behavioral) and their respective energy penalties. Establish a `ContradictionFacet` to track them.

### 2. Unstated Assumption
**Claim:** There might be an issue that can only be solved via a concept we have not yet mapped into the system: contradiction.
**Question:** Is "Contradiction" always a negative state to be resolved? Can a temporary, acknowledged contradiction exist (e.g., during refactoring, or a deliberate divergence for experimentation)? If so, how do we track its lifecycle, similar to how we track `compliance.status`?
**Resolution:** Introduce `Contradiction.status` (e.g., `active`, `acknowledged`, `resolved`) and define its lifecycle rules, possibly linking to a new type of `issue` node.

### 3. Contradiction (Self-Referential)
**Claim:** Define "Contradiction" as a concept.
**Question:** Does defining "Contradiction" as a concept inherently create a meta-contradiction? Is it possible to define a concept that, by its very nature, challenges the logical consistency of the system? How do we ensure the definition of "Contradiction" itself is non-contradictory?
**Resolution:** The definition of "Contradiction" must focus on its *detection and resolution mechanisms* rather than attempting to define its philosophical essence in a way that could lead to paradox. It is a signal for action, not an abstract truth.

### 4. Undefined Edge Case
**Claim:** Contradictions can only be solved by a concept not yet mapped into the system.
**Question:** What if the contradiction itself *is* a mapped concept (e.g., two rules that clash)? How do we prioritize or resolve contradictions between core house rules or architectural principles (Layer 1 rules like Orthogonality vs. a new rule)?
**Resolution:** Define a hierarchy or precedence for contradiction resolution, possibly linking to ADRs for decisions on clashing principles.

### 5. Ownership Gap
**Claim:** We need a way to track contradiction in our system.
**Question:** Who is responsible for detecting semantic contradictions between `SemanticFacet.intent` fields if there is no explicit `contradiction_detector` in the `auditor.py`? Who manually or automatically creates the `Contradiction.status` and manages its lifecycle?
**Resolution:** The "Auditor" (specifically `auditor.py`) must be upgraded to include specific contradiction checks, and the autopoietic loop (`coordinator.py`) must integrate contradiction resolution into its motor stage.
