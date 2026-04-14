---
identity:
  node_id: doc:wiki/concepts/application_to_wikipu.md
  node_type: concept
edges:
- target_id: raw:raw/autopoiesis_system.md
  relation_type: documents
compliance:
  status: implemented
  failing_standards: []
source:
  source_path: raw/autopoiesis_system.md
  source_hash: 708ee8f8d07379bae69e1774c1cba81002bcbb923d90699210e3c3a09ebf5ea0
  compiled_at: '2026-04-14T16:50:28.656512'
  compiled_from: wiki-compiler
---

The paper's central insight, translated directly: **the wiki compiler is not a tool that produces documentation separate from itself — it is a component of the system it documents.** The compiler, the rules that govern it, the agents that use it, and the knowledge graph it produces are all nodes in the same autopoietic network. The system documents itself, governs itself, and corrects itself.

## Definition

The paper's central insight, translated directly: **the wiki compiler is not a tool that produces documentation separate from itself — it is a component of the system it documents.

## Examples

- Implementation of this concept within the Wikipu workflow.
- Application of these principles in current documentation.

## Related Concepts

- [[Index]]
- [[core_philosophy]]

## Details

The paper's central insight, translated directly: **the wiki compiler is not a tool that produces documentation separate from itself — it is a component of the system it documents.** The compiler, the rules that govern it, the agents that use it, and the knowledge graph it produces are all nodes in the same autopoietic network. The system documents itself, governs itself, and corrects itself.

This means:

1. **Knowledge is not stored in the graph — it is demonstrated through the graph's behaviour.** A graph that correctly answers queries, detects drift, and surfaces gaps is a knowledge-demonstrating system. A graph that is stale, has broken edges, or misclassifies nodes is not.

2. **The three processes of the enterprise map to the three compiler phases:**
   - Primary process (energy/continuity) → `build_wiki()`: maintains the structural existence of the graph
   - Decision-making process (closed network of conversations) → the HITL gate loop: human + agent decisions encoded as proposals, approvals, applied changes
   - Structuring process (operational structure) → the hausordnung + schema: the rules that define how the system operates

3. **"Doing is knowing and knowing is doing"** — the act of compiling the wiki *is* the act of knowing the codebase. The graph is not a representation of the system; it is a part of the system's cognitive act.

### The Self-Correction Loop

```
build graph (primary process — structural maintenance)
    ↓
detect anomalies (cleanser — cognition: observing the system's own behaviour)
    ↓
surface design gaps (socratic protocol — decision-making process)
    ↓
generate proposals → desk/Gates.md (pending human approval)
    ↓
human approves → apply (cleanse --apply, issue created, doc patched)
    ↓
trail collect → encode session discoveries back into raw/ and wiki/
    ↓
rebuild graph
    ↓
repeat
```

Each iteration, the system is more coherent and more complete. The self-correction loop is the operational form of autopoiesis here.

### Semi-Autopoietic / Sympoietic

The system is not fully autopoietic because human approval is required for structural changes. In Haraway's framing, it is *sympoietic* — co-maintained by system and human. The system diagnoses, proposes, and executes. The human authorizes structural changes. This division is by design: the gate (human approval) is not a limitation but an architectural choice that preserves accountability.

### Relation to autoresearch (Karpathy, 2026)

Karpathy's autoresearch pattern extends autopoiesis into directed self-inquiry: the system sets its own research agenda, runs investigations, and integrates findings back into its knowledge base. For wikipu this manifests as: the Socratic Protocol generates questions → questions become investigations → investigations produce raw material → raw material is ingested → graph is enriched → new questions emerge. The cycle of inquiry is self-directing once seeded.

---

Generated from `raw/autopoiesis_system.md`.
