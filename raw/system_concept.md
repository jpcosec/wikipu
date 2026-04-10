# Wikipu — Conceptual Foundation

## The System is a Living Knowledge Ecosystem with Two Layers

---

### Layer 1 — The Information Zones

Where things live. Each zone has a distinct role and mutability contract.

| Zone | Role | Mutability |
|---|---|---|
| `raw/` | Seminal source material. The origin. | Immutable (read-only) |
| `wiki/` | Documentation + routing index. The map. | Curated, human+AI editable |
| `src/` (code) | Implementation. The truth. Must have module READMEs + docstrings + clean code. | Editable, tightly governed |
| `data/`, `config/`, `.env` | Runtime I/O. What the system consumes and produces. | Operational |
| `logs/` | Execution trace. What actually happened. | Append-only |
| `plan_docs/` | Active feature work. Ephemeral — deleted when done. | Temporary |
| `future_docs/` | Backlog. Ideas not yet in motion. | Deferred |
| `git` | The system's memory. The immutable audit trail. | Append-only |

---

### Layer 2 — The Five Capabilities

What the system does.

**1. Dynamic Documentation**
The system knows where knowledge belongs and keeps it there. When a conversation happens or code changes, documentation flows to the right zone automatically — not manually. Nothing gets orphaned.

**2. Structured Data Creation & Modification**
There are clear, enforced pathways for creating and modifying data. Not ad hoc writes — intentional, traceable operations with known inputs and outputs.

**3. Association via the Graph**
Everything is connected. Files, code, docs, concepts — all nodes. The graph makes relationships explicit: what contains what, what depends on what, what documents what, what produces what.

**4. Orthogonalization (the Circuit Breaker)**
Before anything new is added to the graph, it must prove it doesn't duplicate or collide with what already exists. This is the TopologyProposal mechanism — a structured gate that keeps the graph clean, non-redundant, and semantically coherent over time.

**5. Context Retrieval**
The graph is queryable. Given a task or a node, the system can surface the minimal relevant subgraph — the right slice of documentation, code, and relationships — to give an LLM (or a human) precisely the context they need.

---

### The North Star: Radical Transparency

Every dynamic in the system must be:
- **Auditable** — you can see what happened and why
- **Replicable** — the same inputs always produce the same outputs
- **Testable** — no hidden side effects, no magic

`git` is the backbone of this — not just version control, but the ground truth of the system's evolution. The whole design resists obscure, uncheckable behavior at every level.
