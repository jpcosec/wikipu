# Socratic Interrogation: Energy-Based Model (EBM) Analogy

**Input Artifact:** Proposal to formally adopt Energy-Based Model (EBM) terminology and theory into `wiki/concepts/energy.md` to mathematically frame Wikipu's autopoietic cycle.

## Open Questions

### 1. Missing Constraint
**Claim:** Wikipu's energy calculation is a macro-scale EBM objective function.
**Question:** If we formally state Wikipu is an Energy-Based Model, does this impose any new constraints on how `wiki-compiler energy` operates? 
**Resolution:** Explicitly define in `energy.md` that our heuristic is a deterministic, macro-scale proxy for an EBM energy function. The state space $x$ is the repository's graph state, and the optimization step is the autopoietic loop.

### 2. Unstated Assumption
**Claim:** We perform "inference time optimization" via the autopoietic cycle, similar to gradient descent.
**Question:** EBMs use continuous gradient descent to find the optimal $x$. We use discrete operations (create, delete, edit). Do we assume our discrete operations are mathematically guaranteed to lower energy monotonically?
**Resolution:** We must acknowledge that our "gradient descent" is actually a discrete structural optimizer. The autopoietic motor (cleansing, merging, committing) takes discrete steps that must evaluate to a strictly lower systemic energy score to be accepted as a valid transition.

### 3. Contradiction
**Claim:** Incorporating EBM theory changes how we view energy.
**Question:** Does this contradict ID-2 (Minimal Energy) which defines energy purely as "conceptual and structural cost"?
**Resolution:** It does not contradict; it expands it. Energy represents both the structural cost AND the mathematical incompatibility of the graph state. High debt/drift = high energy = incompatible state.

### 4. Undefined Edge Case
**Claim:** We map EBM generation to Wikipu generation.
**Question:** EBMs have a concept of "temperature" controlling exploration vs exploitation (the Boltzmann distribution). Does Wikipu have a temperature equivalent?
**Resolution:** We operate at effectively $T=0$ (greedy deterministic optimization towards minimum energy) when enforcing topological invariants. Exploratory drafting happens in `drawers/` or `desk/` before optimization locks it into the invariant `wiki/`.