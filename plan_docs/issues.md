# Design Commentary

Three perspectives on the current state of `wikipu`.

---

## 🧑 Human Developer Perspective

The architecture is well-thought-out and the contracts are clean. But right now, if I clone this repo and run `wiki-compiler build`, I get a graph with six nodes — all of them are the documentation files about the compiler itself. The system is documenting itself, but it's not documenting anything I'm actually building. That's backwards.

The duplicate files (two house rule docs, two agent intros) are the kind of thing that starts as "I'll clean it up later" and becomes the thing that bites you six months in. One of them will be outdated and someone — human or LLM — will follow the wrong one.

The `raw/old_standards/` content is a decision that was never made. Either those ideas survived into the new architecture or they didn't. Leaving them in `raw/` makes them neither reference material nor deleted history. They need a verdict.

The thing I'm most concerned about: the orthogonality validator is the centerpiece of the whole design — the "closed loop" that prevents duplication — and it doesn't exist. The house rules say agents have 3 attempts to submit a valid topology proposal, but there's nothing to submit to. The system enforces a process that has no runtime.

---

## 🤖 LLM (Librarian Agent) Perspective

My operational protocol tells me to call `query_knowledge_graph` to navigate the codebase before doing anything. When I try to call that tool, there is no server. There is no SQLite database. There is a JSON file that gets generated when someone runs `build`, but I have no way to query it with the interface I was given.

If I proceed without the tool and read the wiki directly, I find six nodes. None of them describe the actual Python modules I would need to understand to answer a real question about this codebase. `src/wiki_compiler/builder.py` is not a node. `src/wiki_compiler/contracts.py` is not a node. The graph I'm supposed to trust doesn't know these files exist.

When I try to propose a new module, I'm supposed to submit a `TopologyProposal` to the `submit_topology_proposal` tool. That tool also has no server. I would be blocked at step 1 of the only allowed workflow for creating new code.

The system is architecturally coherent but operationally inert. I can read the house rules and understand the design. I cannot act on any of it.

---

## 📌 Karpathy Compliance Check

Karpathy's description (see `raw/karpathy_tweet.md`) has five concrete components. Here's where `wikipu` stands:

**1. raw/ as the immutable data dump** ✅
Law 10 covers this. `raw/` is read-only for agents. The design is compliant.

**2. LLM compiles raw/ into an organized wiki** ❌
This is the core gap. `wiki-compiler build` compiles `wiki/` — a directory of manually-written nodes — into compiled output. It does not read `raw/` and produce wiki nodes. The compile step is real, but it's not triggered by `raw/`. The ingestion pipeline from raw sources to wiki nodes doesn't exist. See `issues/unimplemented/raw_ingestion_pipeline.md`.

**3. Wiki as navigable index (with backlinks and concept articles)** ⚠️
The `00_INDEX_MOC.md` and transclusion syntax exist, which is the right structure. But the index is hand-maintained, there are no concept articles generated from `raw/`, and the graph has no backlink traversal exposed to the agent. Partially there.

**4. Q&A against the wiki** ❌
Karpathy describes querying an LLM agent against the wiki with it autonomously reading relevant files. The librarian agent protocol is designed for this but the tool runtime doesn't exist. The agent has no backed interface to query the graph.

**5. "Extra tools" and outputs filed back into the wiki** ⚠️
The closed-loop design (TopologyProposal → validation → scaffolding) is a strong version of "filing outputs back into the wiki." But it requires the orthogonality validator to function. Currently the loop is open.

**Summary:** `wikipu` has built the enforcement layer (contracts, house rules, scaffolder) but not the generation layer (raw ingestion, LLM compilation, agent tool runtime). Karpathy's workflow is `raw → compile → query`. The current system is `(manually write) wiki_source → compile → (no query interface)`. The vision is there; the data pipeline isn't.
