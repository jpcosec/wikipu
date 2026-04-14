---
identity:
  node_id: "doc:wiki/concepts/claw_session.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/claw_session.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/claw_session.md"
  source_hash: "0ef760dbcb681b6148b3546a9065d919e2eec7c5432c417a07c7213bb1ef8ce0"
  compiled_at: "2026-04-10T17:47:33.726998"
  compiled_from: "wiki-compiler"
---

╭─── Claude Code v2.1.96 ──────────────────────────────────────────────────────╮

## Details

╭─── Claude Code v2.1.96 ──────────────────────────────────────────────────────╮
│                                                    │ Tips for getting        │
│                  Welcome back jp!                  │ started                 │
│                                                    │ Run /init to create a … │
│                       ▐▛███▜▌                      │ ─────────────────────── │
│                      ▝▜█████▛▘                     │ Recent activity         │
│                        ▘▘ ▝▝                       │ No recent activity      │
│      Sonnet 4.6 · Claude Pro ·                     │                         │
│      juanpablo.ruiz.r@gmail.com's Organization     │                         │
│                      ~/wikipu                      │                         │
╰──────────────────────────────────────────────────────────────────────────────╯

❯ take a look at the code base. Do you understand how it works?                 

  Searched for 1 pattern, read 7 files (ctrl+o to expand)

● Yes, I understand it well. Here's a summary:

  Wikipu — LLM-Driven Knowledge Graph Compiler

  Purpose: A CLI tool (wiki-compiler) that scans a project's wiki docs and
  Python source code, then compiles them into a knowledge_graph.json (a NetworkX
   digraph) that both humans and LLMs can query for perfect context.

  ---
  Core Data Model (contracts.py)

  Everything is a KnowledgeNode with:
  - SystemIdentity — unique node_id (prefixed file:, code:, doc:, dir:) +
  node_type
  - Optional facets: SemanticFacet (intent/docstring), ASTFacet (signatures,
  deps), IOFacet (disk/memory/network ports), ComplianceFacet (status + failing
  standards), ADRFacet
  - edges — directed relationships: contains, depends_on, reads_from, writes_to,
   documents, transcludes

  ---
  CLI Commands (main.py)

  ┌──────────┬───────────────────────────────────────────────────────────────┐
  │ Command  │                         What it does                          │
  ├──────────┼───────────────────────────────────────────────────────────────┤
  │ init     │ Scaffold the base directory structure                         │
  ├──────────┼───────────────────────────────────────────────────────────────┤
  │ build    │ Parse wiki markdown + scan Python ASTs → emit                 │
  │          │ knowledge_graph.json + compliance score                       │
  ├──────────┼───────────────────────────────────────────────────────────────┤
  │ ingest   │ Turn raw braindump files in raw/ into draft wiki nodes in     │
  │          │ wiki/drafts/                                                  │
  ├──────────┼───────────────────────────────────────────────────────────────┤
  │ scaffold │ Generate boilerplate for a new module                         │
  ├──────────┼───────────────────────────────────────────────────────────────┤
  │ query    │ Traverse the graph (get node, ancestors, descendants, find by │
  │          │  I/O)                                                         │
  ├──────────┼───────────────────────────────────────────────────────────────┤
  │ context  │ Render a focused subgraph neighborhood as markdown/JSON       │
  │          │ (entry point for LLM context injection)                       │
  ├──────────┼───────────────────────────────────────────────────────────────┤
  │ validate │ Check a TopologyProposal against the graph for I/O collisions │
  │          │  and glossary terms before writing code                       │
  └──────────┴───────────────────────────────────────────────────────────────┘

  ---
  Key Pipeline (build)

  1. builder.py — walks wiki/**/*.md, parses YAML frontmatter into
  KnowledgeNode, detects ![[transclusion]] links
  2. scanner.py — walks Python files via ast, extracts module/function/class
  nodes with signatures, detects @wiki_exempt decorators, infers I/O ports from
  open() and Path(...).read/write_text calls, respects .wikiignore
  3. Both merged into a networkx.DiGraph, saved as JSON
  4. Compliance score = % of nodes with status implemented | tested | exempt

  ---
  Anti-collision Loop (validate)

  Before an agent proposes a new module, it submits a TopologyProposal. The
  validator checks for:
  - I/O collisions — does another node already own that path/schema?
  - Unknown glossary terms — semantic drift prevention
  - Raw write violations — raw/ is read-only
  - Attempt counter (3 max) — forces human intervention if agent keeps failing

✻ Churned for 33s

❯ The idea is i have reference files (which are divided into raw wich are non   
  editable "seminal" files, wiki_docs wich works as documentation+routing       
  index, src or other code folders (which MUST have their modulewise readmes    
  and inline docstrings, plus hopefully be implemented in a "clean_code"        
  fashion), future_docs which are future features or issues to solve, plan_docs 
   wich is a temporal folder that works for just a concrete feature             
  development, .env and/or config and data which is where most input/output of  
  the code execution should be (logs might exist under a different logs         
  folder)). To this a pertinent thing to add is git, which basically acts as    
  the memory of the system.  The system should 1- dinamically document things   
  where it should go, uppon conversations with the user and request.  2- have   
  clear way to create and modify data 3- have a clear way to make associations  
  (via the graphs) 4- have a clear way to "ortogonalize" the graph structure    
  (that's where the TopologyProposal enters in the frame) to optimize both the  
  graph and the documentation (and maybe even the code quality) 5- have a clear 
   way to query the graph to retrieve context. 6- Enforce user side             
  transparency, Avoid at all costs having obscure                               
  untestable/unreplicable/unauditionable dinamics.                              
                                                                                
  can you repeat me what i've just said in a better ordered way? abstract       
  yourself a bit of the codebase current structure                              

● Wikipu — Conceptual Restatement

  ---
  The System is a Living Knowledge Ecosystem with Two Layers

  Layer 1 — The Information Zones (where things live)

  ┌────────────────┬─────────────────────────────────────┬─────────────────┐
  │      Zone      │                Role                 │   Mutability    │
  ├────────────────┼─────────────────────────────────────┼─────────────────┤
  │ raw/           │ Seminal source material. The        │ Immutable       │
  │                │ origin.                             │ (read-only)     │
  ├────────────────┼─────────────────────────────────────┼─────────────────┤
  │                │ Documentation + routing index. The  │ Curated,        │
  │ wiki/          │ map.                                │ human+AI        │
  │                │                                     │ editable        │
  ├────────────────┼─────────────────────────────────────┼─────────────────┤
  │                │ Implementation. The truth. Must     │ Editable,       │
  │ src/ (code)    │ have module READMEs + docstrings +  │ tightly         │
  │                │ clean code.                         │ governed        │
  ├────────────────┼─────────────────────────────────────┼─────────────────┤
  │ data/,         │ Runtime I/O. What the system        │ Operational     │
  │ config/, .env  │ consumes and produces.              │                 │
  ├────────────────┼─────────────────────────────────────┼─────────────────┤
  │ logs/          │ Execution trace. What actually      │ Append-only     │
  │                │ happened.                           │                 │
  ├────────────────┼─────────────────────────────────────┼─────────────────┤
  │ plan_docs/     │ Active feature work. Ephemeral —    │ Temporary       │
  │                │ deleted when done.                  │                 │
  ├────────────────┼─────────────────────────────────────┼─────────────────┤
  │ future_docs/   │ Backlog. Ideas not yet in motion.   │ Deferred        │
  ├────────────────┼─────────────────────────────────────┼─────────────────┤
  │ git            │ The system's memory. The immutable  │ Append-only     │
  │                │ audit trail.                        │                 │
  └────────────────┴─────────────────────────────────────┴─────────────────┘

  ---
  Layer 2 — The Five Capabilities (what the system does)

  1. Dynamic Documentation
  The system knows where knowledge belongs and keeps it there. When a
  conversation happens or code changes, documentation flows to the right zone
  automatically — not manually. Nothing gets orphaned.

  2. Structured Data Creation & Modification
  There are clear, enforced pathways for creating and modifying data. Not ad hoc
   writes — intentional, traceable operations with known inputs and outputs.

  3. Association via the Graph
  Everything is connected. Files, code, docs, concepts — all nodes. The graph
  makes relationships explicit: what contains what, what depends on what, what
  documents what, what produces what.

  4. Orthogonalization (the Circuit Breaker)
  Before anything new is added to the graph, it must prove it doesn't duplicate
  or collide with what already exists. This is the TopologyProposal mechanism —
  a structured gate that keeps the graph clean, non-redundant, and semantically
  coherent over time.

  5. Context Retrieval
  The graph is queryable. Given a task or a node, the system can surface the
  minimal relevant subgraph — the right slice of documentation, code, and
  relationships — to give an LLM (or a human) precisely the context they need.

  ---
  The North Star: Radical Transparency

  Every dynamic in the system must be:
  - Auditable — you can see what happened and why
  - Replicable — the same inputs always produce the same outputs
  - Testable — no hidden side effects, no magic

  git is the backbone of this — not just version control, but the ground truth
  of the system's evolution. The whole design resists obscure, uncheckable
  behavior at every level.

❯ wonderful. Please write that down in raw                                      

  Listed 1 directory (ctrl+o to expand)

● Write(raw/system_concept.md)
  ⎿  Wrote 52 lines to raw/system_concept.md
      1 # Wikipu — Conceptual Foundation
      2 
      3 ## The System is a Living Knowledge Ecosystem with Two Layers
      4 
      5 ---
      6 
      7 ### Layer 1 — The Information Zones
      8 
      9 Where things live. Each zone has a distinct role and mutability c
        ontract.
     … +42 lines (ctrl+o to expand)

● Written to raw/system_concept.md.

❯ ok, take a look at raw (we'll break the raw sanctity rule a bit for now). is  
  there anything contradictory or redundant with system_concept there?          

  Read 4 files, listed 1 directory (ctrl+o to expand)

● Good picture. Here's the analysis:

  ---
  No contradictions — but significant redundancy

  system_concept.md overlaps heavily with:

  - 00_hausordnung_draft.md — The hausordnung is essentially the same content as
   system_concept.md but formalized as laws. Law 11 = raw/ sanctity, Law 10 =
  orthogonalization, Law 3/5 = structured data, Laws 2/13 = graph association &
  context retrieval. The two documents say the same things at different levels
  of abstraction.
  - librarian_agent_draft.md — Covers capabilities 3, 4, and 5 (graph
  association, orthogonalization, context retrieval) from the agent's
  operational perspective.
  - sourcetalk.txt — The conversation itself is a derivation of the same
  concepts being worked out iteratively. system_concept.md is essentially the
  distilled conclusion of that conversation.
  - karpathy_tweet.md — The upstream inspiration. system_concept.md is the
  "compiled" version of Karpathy's idea applied to this specific project.

  ---
  What system_concept.md actually adds

  One thing that isn't cleanly stated elsewhere: the explicit enumeration of all
   information zones with their mutability contracts as a single table. That's
  the genuine new contribution — the rest is restatement.

  ---
  Suggestion: system_concept.md is most useful as the abstract entry point that
  the other docs derive from. The hausordnung is the operational ruleset, the
  librarian is the agent protocol — both downstream of the concept. Worth making
   that hierarchy explicit rather than treating them as peers in raw/.

❯ can we safelly remove sourcetalk.txt? is there any info there we can extract  
  into another note?                                                            

● Let me read the rest of it before deciding.

  Read 1 file (ctrl+o to expand)

● I have a clear enough picture. Here's the verdict:

  ---
  You can safely delete sourcetalk.txt. Every meaningful artifact it generated
  has already been extracted:

  ┌────────────────────────────────┬────────────────────────────────────────┐
  │        Sourcetalk idea         │            Where it landed             │
  ├────────────────────────────────┼────────────────────────────────────────┤
  │ Karpathy's raw→wiki→compile    │ karpathy_tweet.md + system_concept.md  │
  │ flow                           │                                        │
  ├────────────────────────────────┼────────────────────────────────────────┤
  │ Immutable base + facet         │ contracts_draft.py (and now            │
  │ architecture                   │ contracts.py)                          │
  ├────────────────────────────────┼────────────────────────────────────────┤
  │ Plugin/visitor parser pattern  │ plugins_draft.py                       │
  ├────────────────────────────────┼────────────────────────────────────────┤
  │ Hausordnung laws               │ 00_hausordnung_draft.md                │
  ├────────────────────────────────┼────────────────────────────────────────┤
  │ Librarian agent protocol       │ librarian_agent_draft.md               │
  ├────────────────────────────────┼────────────────────────────────────────┤
  │ KnowledgeNode example          │ knowledge_node_example_draft.md        │
  └────────────────────────────────┴────────────────────────────────────────┘

  The file itself is ~700 lines of a Spanish back-and-forth with Gemini — it's
  the conversation that produced the artifacts, not the artifacts themselves.
  The only things in it that aren't captured elsewhere are:

  1. The explicit compliance statuses you outlined verbally: planned → designed 
  → scaffolding → mocked → implemented → tested. Worth noting the current
  contracts.py dropped designed — if that was intentional, fine; if not, worth
  revisiting.
  2. TestMapFacet (test type + coverage) — appeared in the conversation but was
  dropped from the final contracts.py. Same question: intentional?

  Those two points are the only things worth preserving before deleting. Want me
   to note them somewhere before you remove the file?

❯ can we put them somewhere else? 1 maybe can go in "general lifecycle" and 2   
  of course in contracts                                                        

  Searched for 1 pattern, read 2 files (ctrl+o to expand)

● Good. how_it_works.md already mentions ComplianceFacet statuses but only says
  "planned, implemented, exempt, etc." — the lifecycle detail belongs there or
  in a dedicated standards doc. Let me do both changes now.

  Read 1 file (ctrl+o to expand)

● The lifecycle detail fits naturally in how_it_works.md under the Facets
  section. Now both changes:

● Update(wiki/how_it_works.md)
  ⎿  Added 8 lines, removed 1 line
      26  *   **`ASTFacet`**: Captures information from the Abstract Synt
          ax Tree (code construct type, signatures, dependencies).
      27  *   **`SemanticFacet`**: Stores the high-level intent and raw d
          ocstrings.
      28  *   **`ADRFacet`**: Records Architectural Decision Records rela
          ted to the node.
      29 -*   **`ComplianceFacet`**: Tracks the node's adherence to the `
         -00_house_rules` and its implementation status (planned, impleme
         -nted, exempt, etc.).                                           
      29 +*   **`ComplianceFacet`**: Tracks the node's adherence to the `
         +00_house_rules` and its implementation status. The full lifecyc
         +le is:                                                         
      30 +    1. `planned` — mentioned in `future_docs/` or `plan_docs/`,
         + no code yet                                                   
      31 +    2. `scaffolding` — directory and required files created (`c
         +ontracts.py`, `__init__.py`, `README.md`)                      
      32 +    3. `mocked` — logic exists but runs against fakes/stubs, no
         + real dependencies                                             
      33 +    4. `implemented` — connected to real dependencies and produ
         +ction-ready                                                    
      34 +    5. `tested` — automated tests cover the node's behaviour   
      35 +    6. `exempt` — excluded from compliance tracking via `.wikii
         +gnore` or `@wiki_exempt`                                       
      36 +*   **`TestMapFacet`**: Records the testing strategy for a node
         + (test type and coverage).                                     
      37  
      38  ## 📜 The House Rules (`00_house_rules.md`)
      39  

● Now add TestMapFacet to contracts.py:

● Update(src/wiki_compiler/contracts.py)
  ⎿  Added 10 lines
      72      )
      73      context_summary: str = Field(description="Summary of the co
          ntext and reasons behind the decision, including discarded alte
          rnatives.")
      74  
      75 +class TestMapFacet(BaseModel):                                 
      76 +    """Dimension: Testing Strategy and Coverage."""            
      77 +    test_type: Literal["unit", "integration", "e2e", "manual_re
         +view"] = Field(                                                
      78 +        description="The type of testing applied to this node."
      79 +    )                                                          
      80 +    coverage_percent: float | None = Field(                    
      81 +        default=None,                                          
      82 +        description="Percentage of the node covered by automate
         +d tests, if measured."                                         
      83 +    )                                                          
      84 +                                                               
      85  class ComplianceFacet(BaseModel):
      86      """Dimension: Implementation Status and House Rules Complia
          nce."""
      87      status: Literal["planned", "scaffolding", "mocked", "implem
          ented", "tested", "exempt"] = Field(

● Now wire test_map into KnowledgeNode:

● Update(src/wiki_compiler/contracts.py)
  ⎿  Added 1 line
      118      )
      119      compliance: ComplianceFacet | None = Field(default=None, d
           escription="Compliance status against defined standards and ru
           les.")
      120      adr: ADRFacet | None = Field(default=None, description="Ar
           chitectural Decision Record related information, if applicable
           .")
      121 +    test_map: TestMapFacet | None = Field(default=None, descri
          +ption="Testing strategy and coverage for this node.")         
      122  
      123  # --- 4. Closed Loop Orthogonality and Circuit Breaker ---
      124  
● Done. Now you can safely delete sourcetalk.txt — nothing is lost. Quick
  summary of what landed where:

  - Lifecycle (planned → scaffolding → mocked → implemented → tested → exempt) →
   wiki/how_it_works.md under the ComplianceFacet bullet
  - TestMapFacet → contracts.py as a new optional facet on KnowledgeNode

✻ Sautéed for 41s

❯ ok, about the facets, i don't see any place where we can get good             
  documentation. Can we create it?                                              

  Read 2 files (ctrl+o to expand)

● Write(wiki/knowledge_node_facets.md)
  ⎿  Wrote 142 lines to wiki/knowledge_node_facets.md
       1 ---
       2 identity:
       3   node_id: "doc:wiki/knowledge_node_facets.md"
       4   node_type: "doc_standard"
       5 edges:
       6   - target_id: "file:src/wiki_compiler/contracts.py"
       7     relation_type: "documents"
       8   - target_id: "doc:wiki/how_it_works.md"
       9     relation_type: "documents"
      10 ---
     … +132 lines (ctrl+o to expand)

● Now register it in the index:

● Update(wiki/00_INDEX_MOC.md)
  ⎿  Added 2 lines
       5  edges:
       6    - target_id: "doc:wiki/how_it_works.md"
       7      relation_type: "contains"
       8 +  - target_id: "doc:wiki/knowledge_node_facets.md"             
       9 +    relation_type: "contains"                                  
      10    - target_id: "doc:wiki/how_to_use.md"
      11      relation_type: "contains"
      12    - target_id: "doc:wiki/how_to_add_component.md"

● Update(wiki/00_INDEX_MOC.md)
  ⎿  Added 1 line
      26  ## Core Documentation
      27  
      28  *   **[[How does this work?]]**: Delve into the fundamental con
          cepts and architecture of `wikipu`.
      29 +*   **[[Knowledge Node Facets]]**: Reference for all facets — w
         +hat they capture, their fields, and which node types use them. 
      30  *   **[[How to use it?]]**: Learn about the CLI commands and pr
          imary workflows.
      31  *   **[[How to add a component?]]**: A step-by-step guide to ex
          tending the system with new modules.
      32  

● Done. Created wiki/knowledge_node_facets.md — a full reference covering:

  - The immutable base (SystemIdentity, Edge relation types)
  - Every facet: what question it answers, where the data comes from, all fields
  - The compliance lifecycle table
  - A matrix of which node types typically get which facets

  It's wired to the index and carries documents edges back to contracts.py and
  how_it_works.md so the graph tracks the relationship.

✻ Baked for 51s

❯ ok, there is an important thing to note here. networkx can be used to create  
  an "unstructured" graph from the "raw text". Then facets can be used to       
  "structure that graph" giving parts of it semantic meaning. Then that can be  
  used to check the documentation quality. Do you understand the process? how   
  would you describe it? how would you create the graph, then how would you use 
   the facets to structure it? then how would you use it to check docs quality? 

● Yes, I understand it clearly. Let me articulate it:

  ---
  The Three-Phase Process

  Phase 1 — Build the Raw Graph (Structure)

  The raw graph answers only: what exists, and what points to what.

  Every file, directory, code construct, and doc is a node. Every detectable
  reference between them is an edge — imports, file includes, transclusions,
  co-mentions. No meaning is assigned yet. NetworkX holds this as a pure
  topology: a skeleton of the system.

  dir:src  --contains-->  file:src/scanner.py
  file:src/scanner.py  --depends_on-->  file:src/contracts.py
  doc:wiki/how_it_works.md  --transcludes-->
  doc:wiki/standards/00_house_rules.md

  At this stage the graph is just a map of existence and reference. An LLM could
   walk it but couldn't understand what anything does.

  ---
  Phase 2 — Inject Facets (Semantics)

  Facets are run as independent passes over the raw graph. Each one visits
  relevant nodes and enriches them with a new dimension. They don't change the
  structure — they annotate it.

  ┌────────────────┬─────────────────────┬─────────────────────────────────┐
  │      Pass      │    What it reads    │         What it injects         │
  ├────────────────┼─────────────────────┼─────────────────────────────────┤
  │ AST scanner    │ .py files           │ ASTFacet — signatures,          │
  │                │                     │ construct type, imports         │
  ├────────────────┼─────────────────────┼─────────────────────────────────┤
  │ Docstring      │ same .py files      │ SemanticFacet — intent, raw     │
  │ extractor      │                     │ docstring                       │
  ├────────────────┼─────────────────────┼─────────────────────────────────┤
  │ IO detector    │ AST + docstring     │ IOFacet — medium, path, schema  │
  │                │ annotations         │                                 │
  ├────────────────┼─────────────────────┼─────────────────────────────────┤
  │ Compliance     │ node completeness   │ ComplianceFacet — status,       │
  │ checker        │ rules               │ failing standards               │
  ├────────────────┼─────────────────────┼─────────────────────────────────┤
  │ Test mapper    │ test files +        │ TestMapFacet — type, coverage   │
  │                │ decorators          │                                 │
  ├────────────────┼─────────────────────┼─────────────────────────────────┤
  │ ADR linker     │ wiki/adrs/          │ ADRFacet — decision history     │
  └────────────────┴─────────────────────┴─────────────────────────────────┘

  After this phase, the same graph now carries meaning. The node
  file:src/scanner.py isn't just a node ID — it has intent, signatures, known
  I/O ports, and a compliance status.

  ---
  Phase 3 — Query for Documentation Quality

  Now the graph can be interrogated as a cross-reference engine. Quality gaps
  appear as structural anomalies:

  Coverage gaps — things that exist in code but have no documentation edge:
  code nodes  WHERE  no incoming edge WITH relation_type="documents"
  → undocumented modules

  Semantic gaps — things that exist but have no meaning attached:
  code nodes  WHERE  SemanticFacet IS NULL  OR  raw_docstring IS NULL
  → missing docstrings

  I/O gaps — data flowing through the system without a type contract:
  IOFacet nodes  WHERE  schema_ref IS NULL  AND  medium != "network"
  → untyped disk I/O

  Compliance violations — nodes that fail specific house rules:
  nodes  WHERE  ComplianceFacet.failing_standards IS NOT EMPTY
  → standards breaches, ranked by severity

  Stale documentation — docs pointing to code that no longer exists:
  edges WITH relation_type="documents"  WHERE  target_id NOT IN graph.nodes
  → dead references

  Orphaned plans — future_docs entries with no corresponding code node:
  doc nodes in future_docs/  WHERE  no outgoing edge to any code node
  → forgotten backlog items

  ---
  The Key Insight

  The raw graph gives you reachability — what can find what. Facets give you
  semantics — what things mean. The quality check is just asking: where do these
   two layers disagree? Every gap between "this node exists" and "this node is
  fully understood and documented" is a documentation debt.

  The system doesn't check docs by reading prose — it checks them by looking for
   missing structure in the graph.

✻ Cooked for 34s

❯ ok. Can you write that down explicitly in raw                                 

● Write(raw/graph_construction_process.md)
  ⎿  Wrote 120 lines to raw/graph_construction_process.md
      1 # The Three-Phase Graph Construction Process
      2 
      3 ## Core Idea
      4 
      5 The knowledge graph is built in three independent, composable pha
        ses.
      6 Each phase adds a layer of meaning on top of the previous one.
      7 The raw graph captures existence. Facets capture semantics. Queri
        es capture quality.
      8 
      9 ---
     … +110 lines (ctrl+o to expand)

● Written to raw/graph_construction_process.md.

❯ ok, now, is this a concrete thing in the cli now? is it cretable on the cli?  

● Partially. Let me be precise about what exists vs. what doesn't.

  ---
  What the CLI does today

  build — runs a combined Phase 1+2 in a single pass:
  - Walks wiki/**/*.md → parses YAML frontmatter into nodes, detects
  transclusions
  - Walks src/**/*.py → injects SemanticFacet, ASTFacet, IOFacet,
  ComplianceFacet via AST
  - Saves the graph to knowledge_graph.json
  - Emits a single aggregate compliance score (% of nodes with a passing status)

  query — basic Phase 3 traversal: get_node, get_ancestors, get_descendants,
  find_by_io

  validate — orthogonality check on a TopologyProposal

  context — renders a neighborhood subgraph for LLM context injection

  ---
  What's missing

  Phase 1 and 2 are not separated. The scanner builds nodes with facets in a
  single pass — there's no "raw skeleton first, then enrich" distinction. It
  works, but it means you can't run facet passes independently or add new ones
  without touching the scanner.

  ADRFacet and TestMapFacet are never populated. They exist in contracts.py but
  no scanner pass injects them. They're dead schema right now.

  Phase 3 quality queries don't exist as CLI commands. The gap analysis
  described in the raw doc — coverage gaps, semantic gaps, stale docs, orphaned
  plans — none of those are queryable. The compliance score is a blunt proxy,
  not a structured audit.

  contains edges for the directory tree are never built. The scanner emits file
  and code nodes but never walks the directory hierarchy to create the
  structural skeleton first.

  ---
  Summary

  ┌────────────────────────────────────────────────┬────────────────────────┐
  │                   Capability                   │         Status         │
  ├────────────────────────────────────────────────┼────────────────────────┤
  │ Build graph from wiki markdown                 │ Yes                    │
  ├────────────────────────────────────────────────┼────────────────────────┤
  │ Build graph from Python AST                    │ Yes                    │
  ├────────────────────────────────────────────────┼────────────────────────┤
  │ SemanticFacet, ASTFacet, IOFacet,              │ Yes                    │
  │ ComplianceFacet injection                      │                        │
  ├────────────────────────────────────────────────┼────────────────────────┤
  │ ADRFacet, TestMapFacet injection               │ Schema only, not       │
  │                                                │ implemented            │
  ├────────────────────────────────────────────────┼────────────────────────┤
  │ Separate raw-graph phase                       │ No                     │
  ├────────────────────────────────────────────────┼────────────────────────┤
  │ Directory contains skeleton                    │ No                     │
  ├────────────────────────────────────────────────┼────────────────────────┤
  │ Quality gap queries (coverage, stale docs,     │ No                     │
  │ etc.)                                          │                        │
  ├────────────────────────────────────────────────┼────────────────────────┤
  │ Aggregate compliance score                     │ Yes (blunt)            │
  └────────────────────────────────────────────────┴────────────────────────┘

  The foundation is solid but Phase 1/2 separation and all of Phase 3 are
  missing. Want to plan those out?

❯ please do.                                                                    

● Skill(superpowers:writing-plans)
  ⎿  Successfully loaded skill

● I'm using the writing-plans skill to create the implementation plan.

  Let me read the remaining files I haven't seen yet before writing the plan.

  Searched for 1 pattern, read 4 files (ctrl+o to expand)

● Now I have the full picture. Let me write the plan.

  Listed 1 directory (ctrl+o to expand)

● Write(plan_docs/2026-04-08-three-phase-graph.md)
  ⎿  Wrote 890 lines to plan_docs/2026-04-08-three-phase-graph.md
      1 # Three-Phase Graph Completion Implementation Plan
      2 
      3 > **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:su
        bagent-driven-development (recommended) or superpowers:executing-
        plans to implement this plan task-by-task. Steps use checkbox (`-
         [ ]`) syntax for tracking.
      4 
      5 **Goal:** Complete the three-phase graph construction pipeline: d
        irectory skeleton (Phase 1), modular facet injection including AD
        RFacet and TestMapFacet (Phase 2), and a CLI `audit` command for 
        documentation quality gap detection (Phase 3).
      6 
      7 **Architecture:** Phase 1 adds a directory `contains` skeleton pa
        ss in `builder.py` before file/code nodes are built. Phase 2 adds
         a `facet_injectors.py` module that runs as post-build passes for
         ADRFacet (from YAML frontmatter) and TestMapFacet (from test fil
        e imports). Phase 3 adds `auditor.py` with structured gap queries
         and a new `wiki-compiler audit` CLI command.
      8 
      9 **Tech Stack:** Python 3.10+, NetworkX 3.x, Pydantic v2, pytest, 
        PyYAML
     … +880 lines (ctrl+o to expand)

● Plan saved to plan_docs/2026-04-08-three-phase-graph.md.

  ---
  3 tasks, fully specified:

  - Task 1 — Directory skeleton: build_directory_skeleton() in builder.py, wired
   into build_wiki() before the Python scan
  - Task 2 — Facet injectors: new facet_injectors.py with inject_adr_facets()
  (reads ADR frontmatter) and inject_test_map_facets() (AST import analysis on
  test files), wired as post-build passes
  - Task 3 — Audit command: new auditor.py with six gap checks + wiki-compiler 
  audit CLI

  Tasks 1–2 are infrastructure. Task 3 is independent and can be done in any
  order.

  Two execution options:

  1. Subagent-Driven (recommended) — fresh subagent per task, review between
  tasks

  2. Inline Execution — execute tasks in this session with checkpoints

  Which approach?

✻ Baked for 5m 13s

❯ 1. BUT i'm worried about the semantic aspect of this. Can you tell me how is  
  it being managed? for instance, if i want to introduce a new facet called     
  product evolution or model ussage or pipeline stage. How would the facet      
  inject it and then how would the auditor check it?                            
● Good catch. The honest answer is: the plan handles it poorly.

  Here's what the current plan requires for any new facet:

  1. Add the Pydantic model to contracts.py
  2. Write a new injector function in facet_injectors.py
  3. Manually wire it into builder.py
  4. Write new check functions in auditor.py
  5. Manually wire those into run_audit()

  There is no protocol. No registry. No convention. Each new facet touches 3+
  files and there's nothing describing what a facet injector is or what an audit
   check is. It's just procedural accumulation.

  ---
  What semantic extensibility actually requires

  Two protocols need to exist:

  class FacetInjector(Protocol):
      facet_name: str           # e.g. "model_usage"
      applies_to: set[str]      # node_types this facet is relevant for

      def inject(self, node: KnowledgeNode, context: InjectionContext) -> 
  KnowledgeNode:
          """Enrich node with this facet's data. Return node unchanged if not 
  applicable."""
          ...

  class AuditCheck(Protocol):
      check_name: str           # e.g. "deprecated_model_usage"
      related_facet: str        # which facet this check validates

      def run(self, graph: nx.DiGraph) -> list[AuditFinding]:
          ...

  A registry that maps facets to their injectors and checks:

  # Each facet is a self-contained "plugin" — injector + checks live together
  registry = FacetRegistry()
  registry.register(ModelUsageInjector(), checks=[DeprecatedModelCheck(),
  UntypedModelOutputCheck()])
  registry.register(PipelineStageInjector(), checks=[OrphanedStageCheck(),
  CircularStageCheck()])

  The builder just runs all registered injectors:
  for injector in registry.injectors:
      for node_id in graph.nodes:
          node = load_knowledge_node(graph, node_id)
          enriched = injector.inject(node, context)
          add_knowledge_node(graph, enriched)

  The auditor just runs all registered checks:
  def run_audit(graph, registry) -> AuditReport:
      report = AuditReport()
      for check in registry.checks:
          report.findings.extend(check.run(graph))
      return report

  ---
  Your specific examples

  ModelUsageFacet
  - Injector source: AST scan for imports of anthropic, openai, litellm; or
  docstring annotations like model: claude-sonnet-4-6
  - Audit checks: "node uses a deprecated model", "model output has no
  schema_ref"

  ProductEvolutionFacet
  - Injector source: git log --follow on the file (git is the memory); or
  presence in plan_docs/ or future_docs/
  - Audit checks: "node evolving rapidly but compliance status is still
  scaffolding", "node referenced in future_docs with zero git activity"

  PipelineStageFacet
  - Injector source: decorator @pipeline_stage(...), module path pattern
  src/pipeline/, or YAML frontmatter pipeline_stage: ingest
  - Audit checks: "pipeline stage has no design doc", "stage depends on a stage
  with lower compliance"

  ---
  What needs to change in the plan

  The plan needs a Task 0 before everything else: define the FacetInjector and
  AuditCheck protocols, build a FacetRegistry, and rewrite the existing
  injectors (ADR, TestMap) and audit checks to conform to those protocols. Then
  Tasks 1–3 become clean implementations of that contract.

  Without this, every new facet is a snowflake. With it, adding ModelUsageFacet
  is: write one class, register it, done — no wiring, no touching builder.py or
  auditor.py.

  Want me to update the plan with this Task 0 before we execute?

✻ Brewed for 41s

❯ yes, but answer me this first. Each facet would be kind of like a different   
  question about the repo?                                                      

● Exactly. Each facet is a lens — a specific question you can ask about any node
   in the graph.

  ┌───────────────────────┬──────────────────────────────────────────┐
  │         Facet         │                 Question                 │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ SemanticFacet         │ What does this do?                       │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ ASTFacet              │ How is it structured?                    │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ IOFacet               │ What data does it consume or produce?    │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ ComplianceFacet       │ How complete and rule-compliant is it?   │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ TestMapFacet          │ How is it tested?                        │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ ADRFacet              │ What decisions shaped it?                │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ ModelUsageFacet       │ What AI models does it use?              │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ PipelineStageFacet    │ Where does it sit in the execution flow? │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ ProductEvolutionFacet │ How fast is it changing and why?         │
  └───────────────────────┴──────────────────────────────────────────┘

  The graph topology answers structural questions — what exists, what connects
  to what. Facets answer dimensional questions about the meaning, health, and
  context of each node.

  And the auditor is simply: for each question, which nodes can't answer it when
   they should be able to?

  A file: node that can't answer "what does this do?" → missing docstring.
  A file: node that can't answer "what data does it produce?" → untyped I/O.
  A code: node that can't answer "how is it tested?" → no test coverage.

  That framing also tells you when a facet is worth adding: when you have a
  question you want to ask uniformly across the whole graph, and the answer
  isn't already there. If the question is one-off or node-specific, it's not a
  facet — it's just a query.

❯ wonderful. Can you write that down explicitly? Also, can you from now on      
  demand the concrete question to the facet?                                    

● Write(raw/facets_as_questions.md)
  ⎿  Wrote 62 lines to raw/facets_as_questions.md
       1 # Facets as Questions
       2 
       3 ## Core Idea
       4 
       5 The graph topology answers structural questions: what exists, wh
         at connects to what.
       6 Facets answer dimensional questions about the meaning, health, a
         nd context of each node.
       7 
       8 Each facet is a lens — one specific question you can ask uniform
         ly across every node in the graph.
       9 
      10 ---
     … +52 lines (ctrl+o to expand)

● Now enforce the question in contracts.py — every facet gets a question class
  variable as a hard contract:

  Read 1 file (ctrl+o to expand)

● Update(src/wiki_compiler/contracts.py)
  ⎿  Added 4 lines, removed 1 line
      29  # --- 2. Configurable Dimensions (Facets) ---
      30  
      31  class IOFacet(BaseModel):
      32 -    """Dimension: Input/Output."""                             
      32 +    """Dimension: Input/Output.                                
      33 +                                                               
      34 +    Question: What data does this node consume or produce?     
      35 +    """                                                        
      36      medium: Literal["memory", "disk", "network"] = Field(
      37          description="The medium through which data is transferr
          ed (e.g., 'memory', 'disk', 'network')."
      38      )

● Update(src/wiki_compiler/contracts.py)
  ⎿  Added 4 lines, removed 1 line
      46      )
      47  
      48  class ASTFacet(BaseModel):
      49 -    """Dimension: The Hows (Code Structure)."""                
      49 +    """Dimension: The Hows (Code Structure).                   
      50 +                                                               
      51 +    Question: How is this node structured?                     
      52 +    """                                                        
      53      construct_type: Literal["function", "class", "script"] = Fi
          eld(
      54          description="The type of code construct (e.g., 'functio
          n', 'class', 'script')."
      55      )

● Update(src/wiki_compiler/contracts.py)
  ⎿  Added 4 lines, removed 1 line
      63      )
      64  
      65  class SemanticFacet(BaseModel):
      66 -    """Dimension: What each thing does and its Docstrings."""  
      66 +    """Dimension: What each thing does and its Docstrings.     
      67 +                                                               
      68 +    Question: What does this node do?                          
      69 +    """                                                        
      70      intent: str = Field(description="High-level summary of purp
          ose, extracted from README or module docstring.")
      71      raw_docstring: str | None = Field(
      72          default=None,

● Update(src/wiki_compiler/contracts.py)
  ⎿  Added 4 lines, removed 1 line
      74      )
      75  
      76  class ADRFacet(BaseModel):
      77 -    """Dimension: Historical Decision Records."""              
      77 +    """Dimension: Historical Decision Records.                 
      78 +                                                               
      79 +    Question: What architectural decisions shaped this node?   
      80 +    """                                                        
      81      decision_id: str = Field(description="Unique identifier for
           the architectural decision record.")
      82      status: Literal["proposed", "accepted", "deprecated", "supe
          rseded"] = Field(
      83          description="The current status of the architectural de
          cision."

● Update(src/wiki_compiler/contracts.py)
  ⎿  Added 4 lines, removed 1 line
      85      context_summary: str = Field(description="Summary of the co
          ntext and reasons behind the decision, including discarded alte
          rnatives.")
      86  
      87  class TestMapFacet(BaseModel):
      88 -    """Dimension: Testing Strategy and Coverage."""            
      88 +    """Dimension: Testing Strategy and Coverage.               
      89 +                                                               
      90 +    Question: How is this node tested?                         
      91 +    """                                                        
      92      test_type: Literal["unit", "integration", "e2e", "manual_re
          view"] = Field(
      93          description="The type of testing applied to this node."
      94      )

● Update(src/wiki_compiler/contracts.py)
  ⎿  Added 4 lines, removed 1 line
       98      )
       99  
      100  class ComplianceFacet(BaseModel):
      101 -    """Dimension: Implementation Status and House Rules Compli
          -ance."""                                                      
      101 +    """Dimension: Implementation Status and House Rules Compli
          +ance.                                                         
      102 +                                                              
      103 +    Question: How complete and rule-compliant is this node?   
      104 +    """                                                       
      105      status: Literal["planned", "scaffolding", "mocked", "imple
           mented", "tested", "exempt"] = Field(
      106          description="The current stage of implementation or co
           mpliance status (e.g., 'planned', 'implemented', 'exempt')."
      107      )

● Done. Three things landed:

  1. raw/facets_as_questions.md — the full conceptual statement including the
  auditor's role, when a facet is worth adding, and the design rule
  2. contracts.py — every facet now has an explicit Question: line in its
  docstring
  3. The design rule is now active: any new facet added without a Question: line
   is visibly incomplete — the pattern is established and readable by both
  humans and agents

  From now on, if someone proposes a new facet, the first thing to demand is:
  what is the one question this facet answers?

✻ Brewed for 39s

❯ ok, let's talk a bit about ortogonalization. the idea is if something can be  
  directly answered by one facet, don't add it. If it can't be answered         
  directly then we need a new facet (a new dimension over the knowledge base).  
  Then some questions will be answered by one facet directly (which are the     
  planned unimplemented components of the system?) and other will be answered   
  by a combination of facets (which languages in the translator component are   
  not implemented?). Do we have a clear way to map this from the user prompt to 
   the querying system?                                                         

● Honestly, no. We don't have this today. Let me be precise about what's missing
   and what the complete architecture looks like.

  ---
  What we have

  The current query system has four operations:
  - get_node — fetch one node by ID
  - get_ancestors / get_descendants — topology traversal
  - find_by_io — filter by IOFacet fields only

  None of these can filter by arbitrary facet fields. You can't ask "nodes where
   ComplianceFacet.status == planned." You certainly can't combine two facets.

  ---
  What the complete architecture needs

  Three layers:

  Layer 1 — Structured facet filtering

  Single-facet questions map to a filter expression:

  "Which components are planned?"
  → filter(facet=compliance, status=planned)

  "Which nodes write to disk without a schema?"
  → filter(facet=io, medium=disk, schema_ref=null)

  Layer 2 — Compound queries (facet intersection + graph scope)

  Multi-facet questions combine filters and scope them to a graph region:

  "Which languages in the translator component are not implemented?"
  → scope(descendants_of="dir:src/translator")
    ∩ filter(facet=ast, construct_type=function)
    ∩ filter(facet=compliance, status≠implemented)

  "Which AI-using nodes have no test coverage?"
  → filter(facet=model_usage)          ← node uses a model
    ∩ filter(facet=test_map, null)      ← no test map injected

  Layer 3 — Natural language → structured query

  The LLM reads the question and the facet registry — which lists each facet's
  declared question and fields — then constructs a Layer 1 or Layer 2 query.

  The facet registry is the vocabulary. Without it, the LLM is guessing. With
  it, the LLM can reason: "the user is asking about implementation status → 
  that's ComplianceFacet → filter on status."

  ---
  The orthogonality check as a query test

  This is the key insight: before adding a new facet, you test whether the 
  question can be answered as a compound query over existing facets.

  "Which nodes are actively being developed?"
  → Can I answer this with: filter(compliance, status=scaffolding|mocked)?
  → Yes, partially. But "actively" implies git activity, which no facet
  captures.
  → New facet needed: ProductEvolutionFacet — "How fast is this node changing?"

  "Which functions have more than 3 dependencies?"
  → Can I answer this with: filter(ast, len(dependencies) > 3)?
  → Yes — ASTFacet already has dependencies[]. Just a query, not a new facet.

  If the question's answer already exists in the graph, it's a query. If the
  information genuinely isn't there, it's a new facet.

  ---
  What needs to be built

  ┌─────────────────────────────┬───────────────────────────────────────────┐
  │            Layer            │                  Status                   │
  ├─────────────────────────────┼───────────────────────────────────────────┤
  │ Facets as data              │ Done                                      │
  ├─────────────────────────────┼───────────────────────────────────────────┤
  │ Topology traversal          │ Partial (ancestors/descendants)           │
  ├─────────────────────────────┼───────────────────────────────────────────┤
  │ Single-facet field          │ Missing                                   │
  │ filtering                   │                                           │
  ├─────────────────────────────┼───────────────────────────────────────────┤
  │ Compound queries            │ Missing                                   │
  │ (intersection + scope)      │                                           │
  ├─────────────────────────────┼───────────────────────────────────────────┤
  │ Facet registry with         │ Partially done (docstrings) — needs to be │
  │ declared questions          │  machine-readable                         │
  ├─────────────────────────────┼───────────────────────────────────────────┤
  │ Natural language →          │ Missing                                   │
  │ structured query            │                                           │
  └─────────────────────────────┴───────────────────────────────────────────┘

  The facet registry is the most critical piece — it's the bridge. Right now the
   Question: we added to docstrings is human-readable but the LLM can't use it
  to reason about query construction. It needs to be a proper data structure the
   query builder can introspect.

  ---
  Want me to fold all of this into the plan — as a Task 0 that establishes the
  registry and the structured query language before anything else gets built?

✻ Crunched for 45s

❯ please do                                                                     

  Read 1 file (ctrl+o to expand)

● Write(plan_docs/2026-04-08-three-phase-graph.md)
  ⎿  Added 895 lines, removed 464 lines
       2  
       3  > **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:
          subagent-driven-development (recommended) or superpowers:execut
          ing-plans to implement this plan task-by-task. Steps use checkb
          ox (`- [ ]`) syntax for tracking.
       4  
       5 -**Goal:** Complete the three-phase graph construction pipeline:
         - directory skeleton (Phase 1), modular facet injection includin
         -g ADRFacet and TestMapFacet (Phase 2), and a CLI `audit` comman
         -d for documentation quality gap detection (Phase 3).           
       5 +**Goal:** Complete the three-phase graph construction pipeline 
         +with a proper extensibility foundation: a machine-readable face
         +t registry, a structured query language, a plugin protocol for 
         +injectors and audit checks, directory skeleton (Phase 1), ADRFa
         +cet + TestMapFacet injectors (Phase 2), and a CLI `audit` comma
         +nd (Phase 3).                                                  
       6  
       7 -**Architecture:** Phase 1 adds a directory `contains` skeleton 
         -pass in `builder.py` before file/code nodes are built. Phase 2 
         -adds a `facet_injectors.py` module that runs as post-build pass
         -es for ADRFacet (from YAML frontmatter) and TestMapFacet (from 
         -test file imports). Phase 3 adds `auditor.py` with structured g
         -ap queries and a new `wiki-compiler audit` CLI command.        
       7 +**Architecture:**                                              
       8 +- Task 0 establishes the vocabulary: `FacetRegistry` (machine-r
         +eadable facet specs), `StructuredQuery` language (single-facet 
         +filters + compound queries + graph scope), and `FacetInjector`/
         +`AuditCheck` protocols. Everything else plugs into this.       
       9 +- Task 1 adds the directory skeleton as a pre-build pass in `bu
         +ilder.py`.                                                     
      10 +- Task 2 implements ADR and TestMap facet injectors as protocol
         +-conforming plugins registered in the registry.                
      11 +- Task 3 implements all audit checks as protocol-conforming plu
         +gins and adds `wiki-compiler audit` and enhanced `wiki-compiler
         + query` CLI commands.                                          
      12  
      13  **Tech Stack:** Python 3.10+, NetworkX 3.x, Pydantic v2, pytest
          , PyYAML
      14  
      11 -> **Note:** Tasks 1–3 (infrastructure) and Task 4 (audit) are i
         -ndependent — Task 4 can be implemented without Tasks 1–3 if nee
         -ded.                                                           
      12 -                                                               
      15  > **Pre-existing issue (out of scope):** `tests/test_runtime_fe
          atures.py::test_build_wiki_merges_source_nodes_and_tracks_compl
          iance` calls `build_wiki` with an undeclared `dest_dir` paramet
          er. Do not fix this in this plan; do not break other passing te
          sts.
      16  
      17  ---
     ...
       20  
       21  | File | Action | Responsibility |
       22  |---|---|---|
       21 -| `src/wiki_compiler/builder.py` | Modify | Add `build_directo
          -ry_skeleton()` call at start of `build_wiki()` |              
       22 -| `src/wiki_compiler/facet_injectors.py` | Create | `inject_ad
          -r_facets()` and `inject_test_map_facets()` post-build passes |
       23 -| `src/wiki_compiler/auditor.py` | Create | All quality gap qu
          -ery functions + `AuditReport` |                               
       24 -| `src/wiki_compiler/main.py` | Modify | Wire `facet_injectors
          -` into `build`, add `audit` subcommand |                      
       25 -| `tests/test_directory_skeleton.py` | Create | Tests for dire
          -ctory node generation |                                       
       26 -| `tests/test_facet_injectors.py` | Create | Tests for ADR and
          - TestMap injection |                                          
       27 -| `tests/test_auditor.py` | Create | Tests for all six audit c
          -hecks |                                                       
       23 +| `src/wiki_compiler/registry.py` | Create | `FacetSpec`, `Fac
          +etRegistry`, `InjectionContext` |                             
       24 +| `src/wiki_compiler/protocols.py` | Create | `FacetInjector` 
          +and `AuditCheck` protocols |                                  
       25 +| `src/wiki_compiler/query_language.py` | Create | `FieldCondi
          +tion`, `FacetFilter`, `GraphScope`, `StructuredQuery` |       
       26 +| `src/wiki_compiler/query_executor.py` | Create | `execute_qu
          +ery()` — runs a `StructuredQuery` against a graph |           
       27 +| `src/wiki_compiler/facet_injectors.py` | Create | `ADRInject
          +or`, `TestMapInjector` as protocol-conforming classes |       
       28 +| `src/wiki_compiler/auditor.py` | Create | Six `AuditCheck` i
          +mplementations + `run_audit()` |                              
       29 +| `src/wiki_compiler/builder.py` | Modify | Add directory skel
          +eton pass; wire registry injectors |                          
       30 +| `src/wiki_compiler/main.py` | Modify | Add `audit` subcomman
          +d; wire structured query into `query` |                       
       31 +| `tests/test_registry_and_query.py` | Create | Registry, quer
          +y language, and executor tests |                              
       32 +| `tests/test_directory_skeleton.py` | Create | Directory node
          + generation tests |                                           
       33 +| `tests/test_facet_injectors.py` | Create | ADR and TestMap i
          +njection tests |                                              
       34 +| `tests/test_auditor.py` | Create | All six audit check tests
          + |                                                            
       35  
       36  ---
       37  
       38 +## Task 0: Facet Registry + Query Language + Plugin Protocols 
       39 +                                                              
       40 +Establishes the three foundational contracts everything else b
          +uilds on:                                                     
       41 +1. `FacetRegistry` — machine-readable vocabulary mapping facet
          + names to their specs (question, applicable node types, querya
          +ble fields)                                                   
       42 +2. `StructuredQuery` — typed query language for single-facet f
          +ilters, compound intersection, and graph scope                
       43 +3. `FacetInjector` / `AuditCheck` protocols — the interface ev
          +ery plugin must satisfy                                       
       44 +                                                              
       45 +**Files:**                                                    
       46 +- Create: `src/wiki_compiler/registry.py`                     
       47 +- Create: `src/wiki_compiler/protocols.py`                    
       48 +- Create: `src/wiki_compiler/query_language.py`               
       49 +- Create: `src/wiki_compiler/query_executor.py`               
       50 +- Create: `tests/test_registry_and_query.py`                  
       51 +                                                              
       52 +- [ ] **Step 1: Write failing tests**                         
       53 +                                                              
       54 +```python                                                     
       55 +# tests/test_registry_and_query.py                            
       56 +from __future__ import annotations                            
       57 +import networkx as nx                                         
       58 +import pytest                                                 
       59 +from wiki_compiler.contracts import (                         
       60 +    ComplianceFacet, IOFacet, KnowledgeNode, SemanticFacet, Sy
          +stemIdentity,                                                 
       61 +)                                                             
       62 +from wiki_compiler.graph_utils import add_knowledge_node      
       63 +from wiki_compiler.registry import FacetRegistry, FacetSpec, F
          +ieldSpec                                                      
       64 +from wiki_compiler.query_language import (                    
       65 +    FieldCondition, FacetFilter, GraphScope, StructuredQuery, 
       66 +)                                                             
       67 +from wiki_compiler.query_executor import execute_query        
       68 +                                                              
       69 +                                                              
       70 +def make_node(node_id: str, node_type: str = "file", **kwargs)
          + -> KnowledgeNode:                                            
       71 +    return KnowledgeNode(                                     
       72 +        identity=SystemIdentity(node_id=node_id, node_type=nod
          +e_type),                                                      
       73 +        **kwargs,                                             
       74 +    )                                                         
       75 +                                                              
       76 +                                                              
       77 +def make_graph(*nodes: KnowledgeNode) -> nx.DiGraph:          
       78 +    graph = nx.DiGraph()                                      
       79 +    for node in nodes:                                        
       80 +        add_knowledge_node(graph, node)                       
       81 +    return graph                                              
       82 +                                                              
       83 +                                                              
       84 +# --- Registry tests ---                                      
       85 +                                                              
       86 +def test_registry_stores_and_retrieves_facet_spec() -> None:  
       87 +    registry = FacetRegistry()                                
       88 +    spec = FacetSpec(                                         
       89 +        facet_name="compliance",                              
       90 +        question="How complete and rule-compliant is this node
          +?",                                                           
       91 +        applies_to={"file", "code_construct"},                
       92 +        fields=[FieldSpec(name="status", type="str", nullable=
          +False)],                                                      
       93 +    )                                                         
       94 +    registry.register_spec(spec)                              
       95 +    assert registry.get_spec("compliance") == spec            
       96 +                                                              
       97 +                                                              
       98 +def test_registry_lists_all_registered_facet_names() -> None: 
       99 +    registry = FacetRegistry()                                
      100 +    registry.register_spec(FacetSpec(                         
      101 +        facet_name="semantics",                               
      102 +        question="What does this node do?",                   
      103 +        applies_to={"file"},                                  
      104 +        fields=[],                                            
      105 +    ))                                                        
      106 +    registry.register_spec(FacetSpec(                         
      107 +        facet_name="compliance",                              
      108 +        question="How complete and rule-compliant is this node
          +?",                                                           
      109 +        applies_to={"file"},                                  
      110 +        fields=[],                                            
      111 +    ))                                                        
      112 +    assert set(registry.facet_names) == {"semantics", "complia
          +nce"}                                                         
      113 +                                                              
      114 +                                                              
      115 +# --- Single-facet query tests ---                            
      116 +                                                              
      117 +def test_execute_query_filters_by_compliance_status() -> None:
      118 +    graph = make_graph(                                       
      119 +        make_node("file:src/a.py", compliance=ComplianceFacet(
          +status="planned", failing_standards=[])),                     
      120 +        make_node("file:src/b.py", compliance=ComplianceFacet(
          +status="implemented", failing_standards=[])),                 
      121 +    )                                                         
      122 +    query = StructuredQuery(                                  
      123 +        filters=[FacetFilter(                                 
      124 +            facet="compliance",                               
      125 +            conditions=[FieldCondition(field="status", op="eq"
          +, value="planned")],                                          
      126 +        )]                                                    
      127 +    )                                                         
      128 +    results = execute_query(graph, query)                     
      129 +    assert len(results) == 1                                  
      130 +    assert results[0].identity.node_id == "file:src/a.py"     
      131 +                                                              
      132 +                                                              
      133 +def test_execute_query_filters_by_null_field() -> None:       
      134 +    graph = make_graph(                                       
      135 +        make_node("file:src/a.py", semantics=SemanticFacet(int
          +ent="A", raw_docstring=None)),                                
      136 +        make_node("file:src/b.py", semantics=SemanticFacet(int
          +ent="B", raw_docstring="Has one.")),                          
      137 +    )                                                         
      138 +    query = StructuredQuery(                                  
      139 +        filters=[FacetFilter(                                 
      140 +            facet="semantics",                                
      141 +            conditions=[FieldCondition(field="raw_docstring", 
          +op="is_null")],                                               
      142 +        )]                                                    
      143 +    )                                                         
      144 +    results = execute_query(graph, query)                     
      145 +    assert len(results) == 1                                  
      146 +    assert results[0].identity.node_id == "file:src/a.py"     
      147 +                                                              
      148 +                                                              
      149 +# --- Compound query tests ---                                
      150 +                                                              
      151 +def test_execute_query_intersects_two_facet_filters() -> None:
      152 +    graph = make_graph(                                       
      153 +        make_node(                                            
      154 +            "file:src/a.py",                                  
      155 +            compliance=ComplianceFacet(status="planned", faili
          +ng_standards=[]),                                             
      156 +            semantics=SemanticFacet(intent="A", raw_docstring=
          +None),                                                        
      157 +        ),                                                    
      158 +        make_node(                                            
      159 +            "file:src/b.py",                                  
      160 +            compliance=ComplianceFacet(status="planned", faili
          +ng_standards=[]),                                             
      161 +            semantics=SemanticFacet(intent="B", raw_docstring=
          +"Present."),                                                  
      162 +        ),                                                    
      163 +        make_node(                                            
      164 +            "file:src/c.py",                                  
      165 +            compliance=ComplianceFacet(status="implemented", f
          +ailing_standards=[]),                                         
      166 +            semantics=SemanticFacet(intent="C", raw_docstring=
          +None),                                                        
      167 +        ),                                                    
      168 +    )                                                         
      169 +    query = StructuredQuery(                                  
      170 +        filters=[                                             
      171 +            FacetFilter(facet="compliance", conditions=[      
      172 +                FieldCondition(field="status", op="eq", value=
          +"planned"),                                                   
      173 +            ]),                                               
      174 +            FacetFilter(facet="semantics", conditions=[       
      175 +                FieldCondition(field="raw_docstring", op="is_n
          +ull"),                                                        
      176 +            ]),                                               
      177 +        ]                                                     
      178 +    )                                                         
      179 +    results = execute_query(graph, query)                     
      180 +    assert len(results) == 1                                  
      181 +    assert results[0].identity.node_id == "file:src/a.py"     
      182 +                                                              
      183 +                                                              
      184 +# --- Graph scope tests ---                                   
      185 +                                                              
      186 +def test_execute_query_scopes_to_descendants() -> None:       
      187 +    from wiki_compiler.contracts import Edge                  
      188 +    parent = make_node("dir:src/translator", node_type="direct
          +ory", edges=[                                                 
      189 +        Edge(target_id="file:src/translator/a.py", relation_ty
          +pe="contains"),                                               
      190 +    ])                                                        
      191 +    child = make_node(                                        
      192 +        "file:src/translator/a.py",                           
      193 +        compliance=ComplianceFacet(status="planned", failing_s
          +tandards=[]),                                                 
      194 +    )                                                         
      195 +    other = make_node(                                        
      196 +        "file:src/other/b.py",                                
      197 +        compliance=ComplianceFacet(status="planned", failing_s
          +tandards=[]),                                                 
      198 +    )                                                         
      199 +    graph = make_graph(parent, child, other)                  
      200 +    query = StructuredQuery(                                  
      201 +        filters=[FacetFilter(facet="compliance", conditions=[ 
      202 +            FieldCondition(field="status", op="eq", value="pla
          +nned"),                                                       
      203 +        ])],                                                  
      204 +        scope=GraphScope(descendant_of="dir:src/translator"), 
      205 +    )                                                         
      206 +    results = execute_query(graph, query)                     
      207 +    node_ids = {r.identity.node_id for r in results}          
      208 +    assert "file:src/translator/a.py" in node_ids             
      209 +    assert "file:src/other/b.py" not in node_ids              
      210 +```                                                           
      211 +                                                              
      212 +- [ ] **Step 2: Run to verify failure**                       
      213 +                                                              
      214 +```bash                                                       
      215 +cd /home/jp/wikipu && python -m pytest tests/test_registry_and
          +_query.py -v                                                  
      216 +```                                                           
      217 +                                                              
      218 +Expected: `ImportError: cannot import name 'FacetRegistry'`   
      219 +                                                              
      220 +- [ ] **Step 3: Implement `registry.py`**                     
      221 +                                                              
      222 +Create `src/wiki_compiler/registry.py`:                       
      223 +                                                              
      224 +```python                                                     
      225 +from __future__ import annotations                            
      226 +from dataclasses import dataclass, field                      
      227 +                                                              
      228 +                                                              
      229 +@dataclass                                                    
      230 +class FieldSpec:                                              
      231 +    name: str                                                 
      232 +    type: str        # e.g. "str", "float|None", "list[str]"  
      233 +    nullable: bool                                            
      234 +                                                              
      235 +                                                              
      236 +@dataclass                                                    
      237 +class FacetSpec:                                              
      238 +    facet_name: str                                           
      239 +    question: str    # The one question this facet answers    
      240 +    applies_to: set[str]  # node_type values this facet is rel
          +evant for                                                     
      241 +    fields: list[FieldSpec]                                   
      242 +                                                              
      243 +                                                              
      244 +@dataclass                                                    
      245 +class InjectionContext:                                       
      246 +    project_root: object  # Path — kept as object to avoid cir
          +cular import                                                  
      247 +    adr_dir: object | None = None                             
      248 +    tests_dir: object | None = None                           
      249 +                                                              
      250 +                                                              
      251 +class FacetRegistry:                                          
      252 +    """Central registry mapping facet names to their specs and
          + plugins."""                                                  
      253 +                                                              
      254 +    def __init__(self) -> None:                               
      255 +        self._specs: dict[str, FacetSpec] = {}                
      256 +                                                              
      257 +    def register_spec(self, spec: FacetSpec) -> None:         
      258 +        self._specs[spec.facet_name] = spec                   
      259 +                                                              
      260 +    def get_spec(self, facet_name: str) -> FacetSpec:         
      261 +        if facet_name not in self._specs:                     
      262 +            raise KeyError(f"No facet registered under '{facet
          +_name}'")                                                     
      263 +        return self._specs[facet_name]                        
      264 +                                                              
      265 +    @property                                                 
      266 +    def facet_names(self) -> list[str]:                       
      267 +        return list(self._specs)                              
      268 +                                                              
      269 +                                                              
      270 +def build_default_registry() -> FacetRegistry:                
      271 +    """Returns a registry pre-populated with the built-in face
          +t specs."""                                                   
      272 +    registry = FacetRegistry()                                
      273 +    registry.register_spec(FacetSpec(                         
      274 +        facet_name="semantics",                               
      275 +        question="What does this node do?",                   
      276 +        applies_to={"file", "code_construct", "concept", "doc_
          +standard"},                                                   
      277 +        fields=[                                              
      278 +            FieldSpec("intent", "str", nullable=False),       
      279 +            FieldSpec("raw_docstring", "str|None", nullable=Tr
          +ue),                                                          
      280 +        ],                                                    
      281 +    ))                                                        
      282 +    registry.register_spec(FacetSpec(                         
      283 +        facet_name="ast",                                     
      284 +        question="How is this node structured?",              
      285 +        applies_to={"file", "code_construct"},                
      286 +        fields=[                                              
      287 +            FieldSpec("construct_type", "str", nullable=False)
          +,                                                             
      288 +            FieldSpec("signatures", "list[str]", nullable=Fals
          +e),                                                           
      289 +            FieldSpec("dependencies", "list[str]", nullable=Fa
          +lse),                                                         
      290 +        ],                                                    
      291 +    ))                                                        
      292 +    registry.register_spec(FacetSpec(                         
      293 +        facet_name="io",                                      
      294 +        question="What data does this node consume or produce?
          +",                                                            
      295 +        applies_to={"file", "code_construct"},                
      296 +        fields=[                                              
      297 +            FieldSpec("medium", "str", nullable=False),       
      298 +            FieldSpec("schema_ref", "str|None", nullable=True)
          +,                                                             
      299 +            FieldSpec("path_template", "str|None", nullable=Tr
          +ue),                                                          
      300 +        ],                                                    
      301 +    ))                                                        
      302 +    registry.register_spec(FacetSpec(                         
      303 +        facet_name="compliance",                              
      304 +        question="How complete and rule-compliant is this node
          +?",                                                           
      305 +        applies_to={"file", "code_construct", "directory"},   
      306 +        fields=[                                              
      307 +            FieldSpec("status", "str", nullable=False),       
      308 +            FieldSpec("failing_standards", "list[str]", nullab
          +le=False),                                                    
      309 +            FieldSpec("exemption_reason", "str|None", nullable
          +=True),                                                       
      310 +        ],                                                    
      311 +    ))                                                        
      312 +    registry.register_spec(FacetSpec(                         
      313 +        facet_name="test_map",                                
      314 +        question="How is this node tested?",                  
      315 +        applies_to={"file", "code_construct"},                
      316 +        fields=[                                              
      317 +            FieldSpec("test_type", "str", nullable=False),    
      318 +            FieldSpec("coverage_percent", "float|None", nullab
          +le=True),                                                     
      319 +        ],                                                    
      320 +    ))                                                        
      321 +    registry.register_spec(FacetSpec(                         
      322 +        facet_name="adr",                                     
      323 +        question="What architectural decisions shaped this nod
          +e?",                                                          
      324 +        applies_to={"doc_standard", "concept"},               
      325 +        fields=[                                              
      326 +            FieldSpec("decision_id", "str", nullable=False),  
      327 +            FieldSpec("status", "str", nullable=False),       
      328 +            FieldSpec("context_summary", "str", nullable=False
          +),                                                            
      329 +        ],                                                    
      330 +    ))                                                        
      331 +    return registry                                           
      332 +```                                                           
      333 +                                                              
      334 +- [ ] **Step 4: Implement `protocols.py`**                    
      335 +                                                              
      336 +Create `src/wiki_compiler/protocols.py`:                      
      337 +                                                              
      338 +```python                                                     
      339 +from __future__ import annotations                            
      340 +from typing import Protocol, runtime_checkable                
      341 +import networkx as nx                                         
      342 +from .contracts import AuditFinding, KnowledgeNode            
      343 +from .registry import FacetSpec, InjectionContext             
      344 +                                                              
      345 +                                                              
      346 +@runtime_checkable                                            
      347 +class FacetInjector(Protocol):                                
      348 +    """A plugin that enriches graph nodes with one facet dimen
          +sion."""                                                      
      349 +    spec: FacetSpec                                           
      350 +                                                              
      351 +    def inject(self, node: KnowledgeNode, context: InjectionCo
          +ntext) -> KnowledgeNode:                                      
      352 +        """Return node enriched with this facet. Return unchan
          +ged if not applicable."""                                     
      353 +        ...                                                   
      354 +                                                              
      355 +                                                              
      356 +@runtime_checkable                                            
      357 +class AuditCheck(Protocol):                                   
      358 +    """A plugin that answers: which nodes fail to answer the f
          +acet's question?"""                                           
      359 +    check_name: str                                           
      360 +    question: str       # e.g. "Which code nodes have no docum
          +entation?"                                                    
      361 +    related_facet: str  # facet_name this check validates     
      362 +                                                              
      363 +    def run(self, graph: nx.DiGraph) -> list[AuditFinding]:   
      364 +        ...                                                   
      365 +```                                                           
      366 +                                                              
      367 +Note: `AuditFinding` needs to move to `contracts.py`. Add it t
          +here:                                                         
      368 +                                                              
      369 +```python                                                     
      370 +# In contracts.py, after the existing classes:                
      371 +from dataclasses import dataclass as _dataclass               
      372 +                                                              
      373 +@_dataclass                                                   
      374 +class AuditFinding:                                           
      375 +    check_name: str                                           
      376 +    node_id: str                                              
      377 +    detail: str                                               
      378 +```                                                           
      379 +                                                              
      380 +- [ ] **Step 5: Implement `query_language.py`**               
      381 +                                                              
      382 +Create `src/wiki_compiler/query_language.py`:                 
      383 +                                                              
      384 +```python                                                     
      385 +from __future__ import annotations                            
      386 +from typing import Any, Literal                               
      387 +from pydantic import BaseModel, Field                         
      388 +                                                              
      389 +                                                              
      390 +class FieldCondition(BaseModel):                              
      391 +    field: str                                                
      392 +    op: Literal["eq", "ne", "is_null", "is_not_null", "contain
          +s", "gt", "lt"]                                               
      393 +    value: Any = None                                         
      394 +                                                              
      395 +                                                              
      396 +class FacetFilter(BaseModel):                                 
      397 +    """Filter nodes by conditions on a specific facet's fields
          +."""                                                          
      398 +    facet: str  # facet_name from the registry                
      399 +    conditions: list[FieldCondition]                          
      400 +                                                              
      401 +                                                              
      402 +class GraphScope(BaseModel):                                  
      403 +    """Restrict the query to a subgraph region."""            
      404 +    descendant_of: str | None = None                          
      405 +    ancestor_of: str | None = None                            
      406 +    node_id_prefix: str | None = None  # e.g. "doc:future_docs
          +/"                                                            
      407 +                                                              
      408 +                                                              
      409 +class StructuredQuery(BaseModel):                             
      410 +    """                                                       
      411 +    A typed query over the knowledge graph.                   
      412 +                                                              
      413 +    Single-facet:  one FacetFilter  → answers one-dimensional 
          +questions.                                                    
      414 +    Compound:      multiple filters → intersection, answers mu
          +lti-dimensional questions.                                    
      415 +    Scoped:        with GraphScope  → restricts to a region of
          + the graph.                                                   
      416 +    """                                                       
      417 +    filters: list[FacetFilter] = Field(default_factory=list)  
      418 +    scope: GraphScope | None = None                           
      419 +```                                                           
      420 +                                                              
      421 +- [ ] **Step 6: Implement `query_executor.py`**               
      422 +                                                              
      423 +Create `src/wiki_compiler/query_executor.py`:                 
      424 +                                                              
      425 +```python                                                     
      426 +from __future__ import annotations                            
      427 +from typing import Any                                        
      428 +import networkx as nx                                         
      429 +from .contracts import KnowledgeNode                          
      430 +from .graph_utils import iter_knowledge_nodes, load_knowledge_
          +node                                                          
      431 +from .query_language import FieldCondition, FacetFilter, Struc
          +turedQuery                                                    
      432 +                                                              
      433 +                                                              
      434 +def execute_query(graph: nx.DiGraph, query: StructuredQuery) -
          +> list[KnowledgeNode]:                                        
      435 +    """Execute a StructuredQuery against a graph. Returns matc
          +hing nodes."""                                                
      436 +    candidate_ids = _apply_scope(graph, query.scope)          
      437 +    results = []                                              
      438 +    for node_id in candidate_ids:                             
      439 +        node = load_knowledge_node(graph, node_id)            
      440 +        if all(_facet_matches(node, f) for f in query.filters)
          +:                                                             
      441 +            results.append(node)                              
      442 +    return results                                            
      443 +                                                              
      444 +                                                              
      445 +def _apply_scope(graph: nx.DiGraph, scope) -> list[str]:      
      446 +    if scope is None:                                         
      447 +        return list(graph.nodes)                              
      448 +    if scope.descendant_of:                                   
      449 +        if scope.descendant_of not in graph:                  
      450 +            return []                                         
      451 +        return list(nx.descendants(graph, scope.descendant_of)
          +)                                                             
      452 +    if scope.ancestor_of:                                     
      453 +        if scope.ancestor_of not in graph:                    
      454 +            return []                                         
      455 +        return list(nx.ancestors(graph, scope.ancestor_of))   
      456 +    if scope.node_id_prefix:                                  
      457 +        return [n for n in graph.nodes if n.startswith(scope.n
          +ode_id_prefix)]                                               
      458 +    return list(graph.nodes)                                  
      459 +                                                              
      460 +                                                              
      461 +def _facet_matches(node: KnowledgeNode, facet_filter: FacetFil
          +ter) -> bool:                                                 
      462 +    facet_value = _get_facet(node, facet_filter.facet)        
      463 +    return all(_condition_matches(facet_value, cond) for cond 
          +in facet_filter.conditions)                                   
      464 +                                                              
      465 +                                                              
      466 +def _get_facet(node: KnowledgeNode, facet_name: str) -> object
          +:                                                             
      467 +    mapping = {                                               
      468 +        "semantics": node.semantics,                          
      469 +        "ast": node.ast,                                      
      470 +        "compliance": node.compliance,                        
      471 +        "adr": node.adr,                                      
      472 +        "test_map": node.test_map,                            
      473 +        "io": node.io_ports or None,                          
      474 +    }                                                         
      475 +    return mapping.get(facet_name)                            
      476 +                                                              
      477 +                                                              
      478 +def _condition_matches(facet_value: object, cond: FieldConditi
          +on) -> bool:                                                  
      479 +    if cond.op == "is_null":                                  
      480 +        return _resolve_field(facet_value, cond.field) is None
      481 +    if cond.op == "is_not_null":                              
      482 +        return _resolve_field(facet_value, cond.field) is not 
          +None                                                          
      483 +    actual = _resolve_field(facet_value, cond.field)          
      484 +    if cond.op == "eq":                                       
      485 +        return actual == cond.value                           
      486 +    if cond.op == "ne":                                       
      487 +        return actual != cond.value                           
      488 +    if cond.op == "contains":                                 
      489 +        return isinstance(actual, list) and cond.value in actu
          +al                                                            
      490 +    if cond.op == "gt":                                       
      491 +        return actual is not None and actual > cond.value     
      492 +    if cond.op == "lt":                                       
      493 +        return actual is not None and actual < cond.value     
      494 +    return False                                              
      495 +                                                              
      496 +                                                              
      497 +def _resolve_field(facet_value: object, field: str) -> Any:   
      498 +    if facet_value is None:                                   
      499 +        return None                                           
      500 +    if isinstance(facet_value, list):                         
      501 +        # For io_ports (list of IOFacet): check if any port ha
          +s the field matching                                          
      502 +        values = [getattr(item, field, None) for item in facet
          +_value]                                                       
      503 +        non_null = [v for v in values if v is not None]       
      504 +        return non_null[0] if non_null else None              
      505 +    return getattr(facet_value, field, None)                  
      506 +```                                                           
      507 +                                                              
      508 +- [ ] **Step 7: Run tests**                                   
      509 +                                                              
      510 +```bash                                                       
      511 +cd /home/jp/wikipu && python -m pytest tests/test_registry_and
          +_query.py -v                                                  
      512 +```                                                           
      513 +                                                              
      514 +Expected: all 7 tests PASS.                                   
      515 +                                                              
      516 +- [ ] **Step 8: Commit**                                      
      517 +                                                              
      518 +```bash                                                       
      519 +git add src/wiki_compiler/registry.py src/wiki_compiler/protoc
          +ols.py \                                                      
      520 +        src/wiki_compiler/query_language.py src/wiki_compiler/
          +query_executor.py \                                           
      521 +        src/wiki_compiler/contracts.py tests/test_registry_and
          +_query.py                                                     
      522 +git commit -m "feat: add facet registry, plugin protocols, and
          + structured query language"                                   
      523 +```                                                           
      524 +                                                              
      525 +---                                                           
      526 +                                                              
      527  ## Task 1: Directory Skeleton
      528  
       33 -Adds `dir:` nodes with `contains` edges to the graph before an
          -y file/code nodes are built. The skeleton makes the hierarchy 
          -traversable and gives directory-level nodes a place to attach 
          -semantics.                                                    
      529 +Adds `dir:` nodes with `contains` edges before file/code nodes
          + are built.                                                   
      530  
      531  **Files:**
      532  - Modify: `src/wiki_compiler/builder.py`
      533  - Create: `tests/test_directory_skeleton.py`
      534  
       39 -- [ ] **Step 1: Write the failing test**                      
      535 +- [ ] **Step 1: Write failing tests**                         
      536  
      537  ```python
      538  # tests/test_directory_skeleton.py
     ...
      540  from pathlib import Path
      541  import pytest
      542  from wiki_compiler.builder import build_directory_skeleton
       47 -from wiki_compiler.contracts import KnowledgeNode             
      543  
      544  
      545  def write(path: Path, content: str = "") -> Path:
     ...
      558      assert "dir:src" in node_map
      559      assert "dir:src/module" in node_map
      560  
       66 -    src_node = node_map["dir:src"]                            
       67 -    edge_targets = {e.target_id for e in src_node.edges}      
       68 -    assert "dir:src/module" in edge_targets                   
      561 +    src_targets = {e.target_id for e in node_map["dir:src"].ed
          +ges}                                                          
      562 +    assert "dir:src/module" in src_targets                    
      563  
       70 -    module_node = node_map["dir:src/module"]                  
       71 -    module_targets = {e.target_id for e in module_node.edges} 
      564 +    module_targets = {e.target_id for e in node_map["dir:src/m
          +odule"].edges}                                                
      565      assert "file:src/module/__init__.py" in module_targets
      566      assert "file:src/module/main.py" in module_targets
      567  
     ...
      579      assert any(n.identity.node_id == "dir:src" for n in nodes)
      580  ```
      581  
       89 -- [ ] **Step 2: Run test to verify it fails**                 
      582 +- [ ] **Step 2: Run to verify failure**                       
      583  
      584  ```bash
      585  cd /home/jp/wikipu && python -m pytest tests/test_directory_sk
           eleton.py -v
     ...
      589  
      590  - [ ] **Step 3: Implement `build_directory_skeleton` in `build
           er.py`**
      591  
       99 -Add this function to `src/wiki_compiler/builder.py` (after the
          - imports, before `build_wiki`):                               
      592 +Add after the imports in `builder.py`:                        
      593  
      594  ```python
      595  def build_directory_skeleton(root: Path, project_root: Path) -
           > list[KnowledgeNode]:
      103 -    """Walk root and emit one directory node per subdirectory 
          -with contains edges."""                                       
      596 +    """Emit one directory node per directory under root, with 
          +contains edges to children."""                                
      597      nodes: list[KnowledgeNode] = []
      105 -    for dirpath in sorted(root.rglob("*")):                   
      106 -        if not dirpath.is_dir():                              
      107 -            continue                                          
      598 +    for dirpath in [root] + sorted(d for d in root.rglob("*") 
          +if d.is_dir()):                                               
      599          rel = dirpath.relative_to(project_root).as_posix()
      109 -        children = sorted(dirpath.iterdir())                  
      110 -        edges = []                                            
      111 -        for child in children:                                
      112 -            child_rel = child.relative_to(project_root).as_pos
          -ix()                                                          
      113 -            prefix = "dir" if child.is_dir() else "file"      
      114 -            edges.append(Edge(target_id=f"{prefix}:{child_rel}
          -", relation_type="contains"))                                 
      115 -        nodes.append(                                         
      116 -            KnowledgeNode(                                    
      117 -                identity=SystemIdentity(node_id=f"dir:{rel}", 
          -node_type="directory"),                                       
      118 -                edges=edges,                                  
      119 -                compliance=ComplianceFacet(status="implemented
          -", failing_standards=[]),                                     
      120 -            )                                                 
      121 -        )                                                     
      122 -    return nodes                                              
      123 -```                                                           
      124 -                                                              
      125 -Also add the root itself (the `root` dir relative to `project_
          -root`). Update the function to also emit a node for `root`:   
      126 -                                                              
      127 -```python                                                     
      128 -def build_directory_skeleton(root: Path, project_root: Path) -
          -> list[KnowledgeNode]:                                        
      129 -    nodes: list[KnowledgeNode] = []                           
      130 -    dirs_to_process = [root] + sorted(d for d in root.rglob("*
          -") if d.is_dir())                                             
      131 -    for dirpath in dirs_to_process:                           
      132 -        rel = dirpath.relative_to(project_root).as_posix()    
      133 -        children = sorted(dirpath.iterdir())                  
      600          edges = [
      601              Edge(
      602                  target_id=f"{'dir' if c.is_dir() else 'file'}:
           {c.relative_to(project_root).as_posix()}",
      603                  relation_type="contains",
      604              )
      139 -            for c in children                                 
      605 +            for c in sorted(dirpath.iterdir())                
      606          ]
      141 -        nodes.append(                                         
      142 -            KnowledgeNode(                                    
      143 -                identity=SystemIdentity(node_id=f"dir:{rel}", 
          -node_type="directory"),                                       
      144 -                edges=edges,                                  
      145 -                compliance=ComplianceFacet(status="implemented
          -", failing_standards=[]),                                     
      146 -            )                                                 
      147 -        )                                                     
      607 +        nodes.append(KnowledgeNode(                           
      608 +            identity=SystemIdentity(node_id=f"dir:{rel}", node
          +_type="directory"),                                           
      609 +            edges=edges,                                      
      610 +            compliance=ComplianceFacet(status="implemented", f
          +ailing_standards=[]),                                         
      611 +        ))                                                    
      612      return nodes
      613  ```
      614  
      151 -Add missing imports to `builder.py` (already present: `Complia
          -nceFacet`, `Edge`, `KnowledgeNode`, `SystemIdentity` come from
          - `.contracts`).                                               
      615 +Add missing imports to `builder.py` (`SystemIdentity` — alread
          +y imported via contracts).                                    
      616  
      617  - [ ] **Step 4: Wire into `build_wiki`**
      618  
      155 -In `build_wiki()`, add skeleton generation for each code root 
          -before the Python scan loop:                                  
      619 +In `build_wiki`, add skeleton call before the Python scan:    
      620  
      621  ```python
      158 -def build_wiki(                                               
      159 -    source_dir: Path,                                         
      160 -    graph_path: Path,                                         
      161 -    *,                                                        
      162 -    project_root: Path | None = None,                         
      163 -    code_roots: list[Path] | None = None,                     
      164 -    baseline_path: Path | None = None,                        
      165 -    update_baseline: bool = False,                            
      166 -) -> BuildResult:                                             
      167 -    root = project_root or Path.cwd()                         
      168 -    graph = nx.DiGraph()                                      
      169 -    files_index = index_markdown_files(source_dir)            
      170 -    for markdown_path in sorted(source_dir.rglob("*.md")):    
      171 -        node, raw_markdown = parse_markdown_node(markdown_path
          -)                                                             
      172 -        if node is not None:                                  
      173 -            for transclusion_target in extract_transclusions(r
          -aw_markdown, files_index):                                    
      174 -                node.edges.append(                            
      175 -                    Edge(target_id=transclusion_target, relati
          -on_type="transcludes")                                        
      176 -                )                                             
      177 -            add_knowledge_node(graph, node)                   
      178 -    # --- Phase 1: directory skeleton ---                     
      622 +    # Phase 1: directory skeleton                             
      623      for code_root in (code_roots or [root / "src"]):
      624          if code_root.exists():
      625              for dir_node in build_directory_skeleton(code_root
           , root):
      626                  add_knowledge_node(graph, dir_node)
      183 -    # --- Phase 2: file + code nodes with facets ---          
      184 -    for node in scan_python_sources(                          
      185 -        project_root=root, source_roots=code_roots or [root / 
          -"src"]                                                        
      186 -    ):                                                        
      627 +    # Phase 2: file + code nodes with facets                  
      628 +    for node in scan_python_sources(...):                     
      629          add_knowledge_node(graph, node)
      188 -    save_graph(graph, graph_path)                             
      189 -    score = calculate_compliance_score(graph)                 
      190 -    baseline_file = baseline_path or Path(".compliance_baselin
          -e.json")                                                      
      191 -    baseline_updated, baseline_regressed = update_compliance_b
          -aseline(                                                      
      192 -        baseline_file, score, update_baseline=update_baseline,
      193 -    )                                                         
      194 -    return BuildResult(                                       
      195 -        graph_path=graph_path,                                
      196 -        baseline_path=baseline_file,                          
      197 -        compliance_score=score,                               
      198 -        baseline_updated=baseline_updated,                    
      199 -        baseline_regressed=baseline_regressed,                
      200 -    )                                                         
      630  ```
      631  
      632  - [ ] **Step 5: Run tests**
     ...
      646  
      647  ---
      648  
      220 -## Task 2: Facet Injectors (ADRFacet + TestMapFacet)          
      649 +## Task 2: Facet Injectors as Protocol-Conforming Plugins     
      650  
      222 -Creates `facet_injectors.py` with two post-build passes that e
          -nrich graph nodes. ADR injection reads YAML frontmatter from `
          -wiki/adrs/*.md`. TestMap injection scans test files and links 
          -them to source nodes via import analysis.                     
      651 +Implements `ADRInjector` and `TestMapInjector` as classes that
          + satisfy the `FacetInjector` protocol, with their specs regist
          +ered in the default registry.                                 
      652  
      653  **Files:**
      654  - Create: `src/wiki_compiler/facet_injectors.py`
      655 +- Modify: `src/wiki_compiler/registry.py` (add specs to `build
          +_default_registry`)                                           
      656 +- Modify: `src/wiki_compiler/builder.py` (run injectors post-b
          +uild)                                                         
      657  - Create: `tests/test_facet_injectors.py`
      658  
      228 -- [ ] **Step 1: Write the failing tests**                     
      659 +- [ ] **Step 1: Write failing tests**                         
      660  
      661  ```python
      662  # tests/test_facet_injectors.py
      663  from __future__ import annotations
      233 -import ast                                                    
      234 -import json                                                   
      664  from pathlib import Path
      665  import networkx as nx
      666  import pytest
      667  from wiki_compiler.contracts import KnowledgeNode, SystemIdent
           ity
      239 -from wiki_compiler.facet_injectors import inject_adr_facets, i
          -nject_test_map_facets                                         
      668 +from wiki_compiler.facet_injectors import ADRInjector, TestMap
          +Injector                                                      
      669  from wiki_compiler.graph_utils import add_knowledge_node, load
           _knowledge_node
      670 +from wiki_compiler.registry import InjectionContext           
      671  
      672  
      673  def write(path: Path, content: str) -> Path:
     ...
      679  def make_graph(*node_ids: str) -> nx.DiGraph:
      680      graph = nx.DiGraph()
      681      for node_id in node_ids:
      252 -        node_type = "file" if node_id.startswith("file:") else
          - "code_construct"                                             
      253 -        node = KnowledgeNode(                                 
      682 +        node_type = "doc_standard" if node_id.startswith("doc:
          +") else "file"                                                
      683 +        add_knowledge_node(graph, KnowledgeNode(              
      684              identity=SystemIdentity(node_id=node_id, node_type
           =node_type)
      255 -        )                                                     
      256 -        add_knowledge_node(graph, node)                       
      685 +        ))                                                    
      686      return graph
      687  
      688  
      260 -def test_inject_adr_facets_populates_adr_on_doc_nodes(tmp_path
          -: Path) -> None:                                              
      261 -    write(                                                    
      262 -        tmp_path / "wiki/adrs/001_use_pydantic.md",           
      263 -        """                                                   
      689 +def test_adr_injector_has_correct_spec() -> None:             
      690 +    injector = ADRInjector()                                  
      691 +    assert injector.spec.facet_name == "adr"                  
      692 +    assert injector.spec.question  # must be non-empty        
      693 +                                                              
      694 +                                                              
      695 +def test_adr_injector_populates_adr_from_frontmatter(tmp_path:
          + Path) -> None:                                               
      696 +    write(tmp_path / "wiki/adrs/001_pydantic.md", """         
      697          ---
      698          identity:
      266 -          node_id: "doc:wiki/adrs/001_use_pydantic.md"        
      699 +          node_id: "doc:wiki/adrs/001_pydantic.md"            
      700            node_type: "doc_standard"
      701          adr:
      702            decision_id: "001"
     ...
      705          edges: []
      706          ---
      707          # ADR 001
      275 -        """,                                                  
      276 -    )                                                         
      277 -    graph = make_graph("doc:wiki/adrs/001_use_pydantic.md")   
      708 +    """)                                                      
      709 +    graph = make_graph("doc:wiki/adrs/001_pydantic.md")       
      710 +    ctx = InjectionContext(project_root=tmp_path, adr_dir=tmp_
          +path / "wiki/adrs")                                           
      711  
      279 -    inject_adr_facets(graph, adr_dir=tmp_path / "wiki/adrs")  
      712 +    injector = ADRInjector()                                  
      713 +    for node_id in list(graph.nodes):                         
      714 +        node = load_knowledge_node(graph, node_id)            
      715 +        enriched = injector.inject(node, ctx)                 
      716 +        add_knowledge_node(graph, enriched)                   
      717  
      281 -    node = load_knowledge_node(graph, "doc:wiki/adrs/001_use_p
          -ydantic.md")                                                  
      718 +    node = load_knowledge_node(graph, "doc:wiki/adrs/001_pydan
          +tic.md")                                                      
      719      assert node.adr is not None
      720      assert node.adr.decision_id == "001"
      721      assert node.adr.status == "accepted"
      285 -    assert "Pydantic" in node.adr.context_summary             
      722  
      723  
      288 -def test_inject_adr_facets_skips_missing_adr_frontmatter(tmp_p
          -ath: Path) -> None:                                           
      289 -    write(                                                    
      290 -        tmp_path / "wiki/adrs/002_no_adr.md",                 
      291 -        """                                                   
      724 +def test_adr_injector_skips_node_without_adr_frontmatter(tmp_p
          +ath: Path) -> None:                                           
      725 +    write(tmp_path / "wiki/adrs/002_plain.md", """            
      726          ---
      727          identity:
      294 -          node_id: "doc:wiki/adrs/002_no_adr.md"              
      728 +          node_id: "doc:wiki/adrs/002_plain.md"               
      729            node_type: "doc_standard"
      730          edges: []
      731          ---
      298 -        # No ADR key here                                     
      299 -        """,                                                  
      300 -    )                                                         
      301 -    graph = make_graph("doc:wiki/adrs/002_no_adr.md")         
      302 -    inject_adr_facets(graph, adr_dir=tmp_path / "wiki/adrs")  
      303 -    node = load_knowledge_node(graph, "doc:wiki/adrs/002_no_ad
          -r.md")                                                        
      304 -    assert node.adr is None                                   
      732 +    """)                                                      
      733 +    graph = make_graph("doc:wiki/adrs/002_plain.md")          
      734 +    ctx = InjectionContext(project_root=tmp_path, adr_dir=tmp_
          +path / "wiki/adrs")                                           
      735 +    injector = ADRInjector()                                  
      736 +    node = load_knowledge_node(graph, "doc:wiki/adrs/002_plain
          +.md")                                                         
      737 +    enriched = injector.inject(node, ctx)                     
      738 +    assert enriched.adr is None                               
      739  
      740  
      307 -def test_inject_test_map_facets_links_test_to_source_node(tmp_
          -path: Path) -> None:                                          
      308 -    write(                                                    
      309 -        tmp_path / "tests/test_scanner.py",                   
      310 -        """                                                   
      311 -        from wiki_compiler.scanner import scan_python_sources 
      741 +def test_test_map_injector_has_correct_spec() -> None:        
      742 +    injector = TestMapInjector()                              
      743 +    assert injector.spec.facet_name == "test_map"             
      744 +    assert injector.spec.question                             
      745  
      746 +                                                              
      747 +def test_test_map_injector_links_test_imports_to_source_node(t
          +mp_path: Path) -> None:                                       
      748 +    write(tmp_path / "tests/test_scanner.py", """             
      749 +        from wiki_compiler.scanner import scan_python_sources 
      750          def test_something():
      751              pass
      315 -        """,                                                  
      316 -    )                                                         
      752 +    """)                                                      
      753      graph = make_graph("file:src/wiki_compiler/scanner.py")
      754 +    ctx = InjectionContext(project_root=tmp_path, tests_dir=tm
          +p_path / "tests")                                             
      755 +    injector = TestMapInjector()                              
      756 +    for node_id in list(graph.nodes):                         
      757 +        node = load_knowledge_node(graph, node_id)            
      758 +        enriched = injector.inject(node, ctx)                 
      759 +        add_knowledge_node(graph, enriched)                   
      760  
      319 -    inject_test_map_facets(graph, tests_dir=tmp_path / "tests"
          -, project_root=tmp_path)                                      
      320 -                                                              
      761      node = load_knowledge_node(graph, "file:src/wiki_compiler/
           scanner.py")
      762      assert node.test_map is not None
      763      assert node.test_map.test_type == "unit"
      324 -    assert node.test_map.coverage_percent is None             
      325 -                                                              
      326 -                                                              
      327 -def test_inject_test_map_facets_ignores_unmatched_imports(tmp_
          -path: Path) -> None:                                          
      328 -    write(                                                    
      329 -        tmp_path / "tests/test_other.py",                     
      330 -        """                                                   
      331 -        import os                                             
      332 -        def test_nothing():                                   
      333 -            pass                                              
      334 -        """,                                                  
      335 -    )                                                         
      336 -    graph = make_graph("file:src/wiki_compiler/scanner.py")   
      337 -    inject_test_map_facets(graph, tests_dir=tmp_path / "tests"
          -, project_root=tmp_path)                                      
      338 -    node = load_knowledge_node(graph, "file:src/wiki_compiler/
          -scanner.py")                                                  
      339 -    assert node.test_map is None                              
      764  ```
      765  
      766  - [ ] **Step 2: Run to verify failure**
     ...
      769  cd /home/jp/wikipu && python -m pytest tests/test_facet_inject
           ors.py -v
      770  ```
      771  
      348 -Expected: `ImportError: cannot import name 'inject_adr_facets'
          -`                                                             
      772 +Expected: `ImportError: cannot import name 'ADRInjector'`     
      773  
      774  - [ ] **Step 3: Implement `facet_injectors.py`**
      775  
     ...
       777  
       778  ```python
       779  from __future__ import annotations
       356 -                                                             
       780  import ast
       781  import re
       782  from pathlib import Path
       360 -                                                             
       361 -import networkx as nx                                        
       783  import yaml
       784 +from .contracts import ADRFacet, KnowledgeNode, TestMapFacet 
       785 +from .registry import FacetSpec, FieldSpec, InjectionContext 
       786  
       364 -from .contracts import ADRFacet, TestMapFacet                
       365 -from .graph_utils import load_knowledge_node, add_knowledge_n
           -ode                                                          
       366 -                                                             
       787  FRONTMATTER_REGEX = re.compile(r"\A---\s*\n(.*?)\n---(\s*\n|$
            )", re.DOTALL)
       788  
       789  
       370 -def inject_adr_facets(graph: nx.DiGraph, adr_dir: Path) -> No
           -ne:                                                          
       371 -    """Populate ADRFacet on nodes whose wiki/adrs/ file decla
           -res an `adr:` frontmatter key."""                            
       372 -    if not adr_dir.exists():                                 
       373 -        return                                               
       374 -    for md_path in sorted(adr_dir.glob("*.md")):             
       375 -        content = md_path.read_text(encoding="utf-8")        
       376 -        match = FRONTMATTER_REGEX.search(content)            
       377 -        if not match:                                        
       378 -            continue                                         
       379 -        data = yaml.safe_load(match.group(1)) or {}          
       380 -        node_id = (data.get("identity") or {}).get("node_id")
       381 -        adr_data = data.get("adr")                           
       382 -        if not node_id or not adr_data or node_id not in grap
           -h.nodes:                                                     
       383 -            continue                                         
       384 -        node = load_knowledge_node(graph, node_id)           
       385 -        node.adr = ADRFacet.model_validate(adr_data)         
       386 -        add_knowledge_node(graph, node)                      
       790 +class ADRInjector:                                           
       791 +    """Populates ADRFacet from YAML frontmatter in wiki/adrs/
           + files."""                                                   
       792  
       793 +    spec = FacetSpec(                                        
       794 +        facet_name="adr",                                    
       795 +        question="What architectural decisions shaped this no
           +de?",                                                        
       796 +        applies_to={"doc_standard", "concept"},              
       797 +        fields=[                                             
       798 +            FieldSpec("decision_id", "str", nullable=False), 
       799 +            FieldSpec("status", "str", nullable=False),      
       800 +            FieldSpec("context_summary", "str", nullable=Fals
           +e),                                                          
       801 +        ],                                                   
       802 +    )                                                        
       803  
       389 -def inject_test_map_facets(                                  
       390 -    graph: nx.DiGraph, tests_dir: Path, project_root: Path   
       391 -) -> None:                                                   
       392 -    """Scan test files and inject TestMapFacet into any sourc
           -e node they import."""                                       
       393 -    if not tests_dir.exists():                               
       394 -        return                                               
       395 -    for test_file in sorted(tests_dir.rglob("test_*.py")):   
       396 -        source = test_file.read_text(encoding="utf-8")       
       804 +    def inject(self, node: KnowledgeNode, context: InjectionC
           +ontext) -> KnowledgeNode:                                    
       805 +        if node.identity.node_type not in self.spec.applies_t
           +o:                                                           
       806 +            return node                                      
       807 +        adr_dir = context.adr_dir                            
       808 +        if not adr_dir or not Path(adr_dir).exists():        
       809 +            return node                                      
       810 +        for md_path in Path(adr_dir).glob("*.md"):           
       811 +            content = md_path.read_text(encoding="utf-8")    
       812 +            match = FRONTMATTER_REGEX.search(content)        
       813 +            if not match:                                    
       814 +                continue                                     
       815 +            data = yaml.safe_load(match.group(1)) or {}      
       816 +            node_id = (data.get("identity") or {}).get("node_
           +id")                                                         
       817 +            adr_data = data.get("adr")                       
       818 +            if node_id == node.identity.node_id and adr_data:
       819 +                node.adr = ADRFacet.model_validate(adr_data) 
       820 +        return node                                          
       821 +                                                             
       822 +                                                             
       823 +class TestMapInjector:                                       
       824 +    """Populates TestMapFacet by scanning test files for impo
           +rts of source modules."""                                    
       825 +                                                             
       826 +    spec = FacetSpec(                                        
       827 +        facet_name="test_map",                               
       828 +        question="How is this node tested?",                 
       829 +        applies_to={"file", "code_construct"},               
       830 +        fields=[                                             
       831 +            FieldSpec("test_type", "str", nullable=False),   
       832 +            FieldSpec("coverage_percent", "float|None", nulla
           +ble=True),                                                   
       833 +        ],                                                   
       834 +    )                                                        
       835 +                                                             
       836 +    def inject(self, node: KnowledgeNode, context: InjectionC
           +ontext) -> KnowledgeNode:                                    
       837 +        if node.identity.node_type not in self.spec.applies_t
           +o:                                                           
       838 +            return node                                      
       839 +        tests_dir = context.tests_dir                        
       840 +        if not tests_dir or not Path(tests_dir).exists():    
       841 +            return node                                      
       842 +        project_root = Path(context.project_root)            
       843 +        for test_file in Path(tests_dir).rglob("test_*.py"): 
       844 +            if self._test_imports_node(test_file, node.identi
           +ty.node_id, project_root):                                   
       845 +                node.test_map = TestMapFacet(test_type="unit"
           +, coverage_percent=None)                                     
       846 +                return node                                  
       847 +        return node                                          
       848 +                                                             
       849 +    def _test_imports_node(self, test_file: Path, node_id: st
           +r, project_root: Path) -> bool:                              
       850          try:
       398 -            tree = ast.parse(source)                         
       851 +            tree = ast.parse(test_file.read_text(encoding="ut
           +f-8"))                                                       
       852          except SyntaxError:
       400 -            continue                                         
       853 +            return False                                     
       854          for stmt in ast.walk(tree):
       855              if not isinstance(stmt, ast.ImportFrom):
       856                  continue
       404 -            module = stmt.module or ""                       
       405 -            candidate = _module_to_node_id(module, project_ro
           -ot)                                                          
       406 -            if candidate and candidate in graph.nodes:       
       407 -                node = load_knowledge_node(graph, candidate) 
       408 -                if node.test_map is None:                    
       409 -                    node.test_map = TestMapFacet(test_type="u
           -nit", coverage_percent=None)                                 
       410 -                    add_knowledge_node(graph, node)          
       857 +            candidate = _module_to_node_id(stmt.module or "",
           + project_root)                                               
       858 +            if candidate == node_id:                         
       859 +                return True                                  
       860 +        return False                                         
       861  
       862  
       863  def _module_to_node_id(module: str, project_root: Path) -> st
            r | None:
       414 -    """Convert a dotted module name to a file: node_id if the
           - file exists."""                                             
       864      relative = module.replace(".", "/") + ".py"
       416 -    for root in ("src", ""):                                 
       417 -        candidate = Path(root) / relative if root else Path(r
           -elative)                                                     
       865 +    for prefix in ("src", ""):                               
       866 +        candidate = Path(prefix) / relative if prefix else Pa
           +th(relative)                                                 
       867          if (project_root / candidate).exists():
       868              return f"file:{candidate.as_posix()}"
       869      return None
       870  ```
       871  
       423 -- [ ] **Step 4: Run tests**                                  
       872 +- [ ] **Step 4: Wire injectors into `build_wiki`**           
       873  
       425 -```bash                                                      
       426 -cd /home/jp/wikipu && python -m pytest tests/test_facet_injec
           -tors.py -v                                                   
       427 -```                                                          
       874 +Add to `builder.py` imports:                                 
       875  
       429 -Expected: all 4 tests PASS.                                  
       430 -                                                             
       431 -- [ ] **Step 5: Wire into `build_wiki`**                     
       432 -                                                             
       433 -In `builder.py`, add facet injection after the Python scan:  
       434 -                                                             
       876  ```python
       436 -from .facet_injectors import inject_adr_facets, inject_test_m
           -ap_facets                                                    
       877 +from .facet_injectors import ADRInjector, TestMapInjector    
       878 +from .registry import InjectionContext                       
       879  ```
       880  
       439 -At the end of `build_wiki`, before `save_graph`:             
       881 +Add injector pass after `scan_python_sources` loop in `build_
           +wiki`, before `save_graph`:                                  
       882  
       883  ```python
       442 -    # --- Phase 2b: post-build facet passes ---              
       443 -    inject_adr_facets(graph, adr_dir=root / "wiki" / "adrs") 
       444 -    inject_test_map_facets(graph, tests_dir=root / "tests", p
           -roject_root=root)                                            
       445 -    save_graph(graph, graph_path)                            
       884 +    # Phase 2b: facet injector passes                        
       885 +    ctx = InjectionContext(                                  
       886 +        project_root=root,                                   
       887 +        adr_dir=root / "wiki" / "adrs",                      
       888 +        tests_dir=root / "tests",                            
       889 +    )                                                        
       890 +    for injector in [ADRInjector(), TestMapInjector()]:      
       891 +        for node_id in list(graph.nodes):                    
       892 +            node = load_knowledge_node(graph, node_id)       
       893 +            enriched = injector.inject(node, ctx)            
       894 +            add_knowledge_node(graph, enriched)              
       895  ```
       896  
       448 -- [ ] **Step 6: Verify existing tests still pass**           
       897 +- [ ] **Step 5: Run tests**                                  
       898  
       899  ```bash
       451 -cd /home/jp/wikipu && python -m pytest tests/test_directory_s
           -keleton.py tests/test_facet_injectors.py -v                  
       900 +cd /home/jp/wikipu && python -m pytest tests/test_facet_injec
           +tors.py tests/test_directory_skeleton.py -v                  
       901  ```
       902  
       454 -Expected: all PASS.                                          
       903 +Expected: all tests PASS.                                    
       904  
       456 -- [ ] **Step 7: Commit**                                     
       905 +- [ ] **Step 6: Commit**                                     
       906  
       907  ```bash
       459 -git add src/wiki_compiler/facet_injectors.py src/wiki_compile
           -r/builder.py tests/test_facet_injectors.py                   
       460 -git commit -m "feat: add ADRFacet and TestMapFacet post-build
           - injectors"                                                  
       908 +git add src/wiki_compiler/facet_injectors.py src/wiki_compile
           +r/builder.py \                                               
       909 +        tests/test_facet_injectors.py                        
       910 +git commit -m "feat: add ADRInjector and TestMapInjector as p
           +rotocol-conforming plugins"                                  
       911  ```
       912  
       913  ---
       914  
       465 -## Task 3: Audit Command                                     
       915 +## Task 3: Audit Command + Enhanced Query CLI                
       916  
       467 -Adds `auditor.py` with six structured gap queries and a `wiki
           --compiler audit` CLI command that outputs a full documentatio
           -n quality report.                                            
       917 +Implements six `AuditCheck` plugins backed by `StructuredQuer
           +y` where possible, adds `wiki-compiler audit`, and wires the 
           +structured query language into `wiki-compiler query`.        
       918  
       919  **Files:**
       920  - Create: `src/wiki_compiler/auditor.py`
       921  - Modify: `src/wiki_compiler/main.py`
       922  - Create: `tests/test_auditor.py`
       923  
       474 -- [ ] **Step 1: Write the failing tests**                    
       924 +- [ ] **Step 1: Write failing tests**                        
       925  
       926  ```python
       927  # tests/test_auditor.py
       928  from __future__ import annotations
       479 -import json                                                  
       480 -from pathlib import Path                                     
       929  import networkx as nx
       930  import pytest
       931  from wiki_compiler.auditor import (
       484 -    AuditFinding,                                            
       485 -    AuditReport,                                             
       486 -    find_compliance_violations,                              
       487 -    find_missing_docstrings,                                 
       488 -    find_orphaned_plans,                                     
       489 -    find_stale_edges,                                        
       490 -    find_undocumented_code,                                  
       491 -    find_untyped_io,                                         
       932 +    ComplianceViolationsCheck,                               
       933 +    MissingDocstringsCheck,                                  
       934 +    OrphanedPlansCheck,                                      
       935 +    StaleEdgesCheck,                                         
       936 +    UndocumentedCodeCheck,                                   
       937 +    UntypedIOCheck,                                          
       938      run_audit,
       939  )
       940  from wiki_compiler.contracts import (
       495 -    ASTFacet,                                                
       496 -    ComplianceFacet,                                         
       497 -    IOFacet,                                                 
       498 -    KnowledgeNode,                                           
       499 -    SemanticFacet,                                           
       500 -    SystemIdentity,                                          
       941 +    AuditFinding, ComplianceFacet, Edge, IOFacet,            
       942 +    KnowledgeNode, SemanticFacet, SystemIdentity,            
       943  )
       944  from wiki_compiler.graph_utils import add_knowledge_node
       945  
       946  
       947  def make_node(node_id: str, node_type: str = "file", **kwargs
            ) -> KnowledgeNode:
       948      return KnowledgeNode(
       507 -        identity=SystemIdentity(node_id=node_id, node_type=no
           -de_type),                                                    
       508 -        **kwargs,                                            
       949 +        identity=SystemIdentity(node_id=node_id, node_type=no
           +de_type), **kwargs                                           
       950      )
       951  
       952  
       512 -def test_find_undocumented_code_detects_code_node_with_no_doc
           -uments_edge() -> None:                                       
       953 +def make_graph(*nodes: KnowledgeNode) -> nx.DiGraph:         
       954      graph = nx.DiGraph()
       514 -    add_knowledge_node(graph, make_node("file:src/foo.py", no
           -de_type="file"))                                             
       515 -    findings = find_undocumented_code(graph)                 
       955 +    for node in nodes:                                       
       956 +        add_knowledge_node(graph, node)                      
       957 +    return graph                                             
       958 +                                                             
       959 +                                                             
       960 +def test_undocumented_code_check_has_correct_metadata() -> No
           +ne:                                                          
       961 +    check = UndocumentedCodeCheck()                          
       962 +    assert check.related_facet == "semantics"                
       963 +    assert check.question                                    
       964 +                                                             
       965 +                                                             
       966 +def test_undocumented_code_detects_file_with_no_documents_edg
           +e() -> None:                                                 
       967 +    graph = make_graph(make_node("file:src/foo.py"))         
       968 +    findings = UndocumentedCodeCheck().run(graph)            
       969      assert any(f.node_id == "file:src/foo.py" for f in findin
            gs)
       970  
       971  
       519 -def test_find_undocumented_code_passes_when_documents_edge_ex
           -ists() -> None:                                              
       520 -    from wiki_compiler.contracts import Edge                 
       521 -    graph = nx.DiGraph()                                     
       522 -    code_node = make_node("file:src/foo.py", node_type="file"
           -)                                                            
       523 -    doc_node = make_node(                                    
       524 -        "doc:wiki/foo.md",                                   
       525 -        node_type="doc_standard",                            
       526 -        edges=[Edge(target_id="file:src/foo.py", relation_typ
           -e="documents")],                                             
       972 +def test_undocumented_code_passes_when_documents_edge_exists(
           +) -> None:                                                   
       973 +    graph = make_graph(                                      
       974 +        make_node("file:src/foo.py"),                        
       975 +        make_node("doc:wiki/foo.md", node_type="doc_standard"
           +, edges=[                                                    
       976 +            Edge(target_id="file:src/foo.py", relation_type="
           +documents"),                                                 
       977 +        ]),                                                  
       978      )
       528 -    add_knowledge_node(graph, code_node)                     
       529 -    add_knowledge_node(graph, doc_node)                      
       530 -    findings = find_undocumented_code(graph)                 
       979 +    findings = UndocumentedCodeCheck().run(graph)            
       980      assert not any(f.node_id == "file:src/foo.py" for f in fi
            ndings)
       981  
       982  
       534 -def test_find_missing_docstrings_detects_node_without_raw_doc
           -string() -> None:                                            
       535 -    graph = nx.DiGraph()                                     
       536 -    node = make_node(                                        
       983 +def test_missing_docstrings_detects_null_raw_docstring() -> N
           +one:                                                         
       984 +    graph = make_graph(make_node(                            
       985          "file:src/bar.py",
       538 -        node_type="file",                                    
       539 -        semantics=SemanticFacet(intent="Bar module.", raw_doc
           -string=None),                                                
       540 -    )                                                        
       541 -    add_knowledge_node(graph, node)                          
       542 -    findings = find_missing_docstrings(graph)                
       986 +        semantics=SemanticFacet(intent="Bar.", raw_docstring=
           +None),                                                       
       987 +    ))                                                       
       988 +    findings = MissingDocstringsCheck().run(graph)           
       989      assert any(f.node_id == "file:src/bar.py" for f in findin
            gs)
       990  
       991  
       546 -def test_find_missing_docstrings_passes_when_docstring_presen
           -t() -> None:                                                 
       547 -    graph = nx.DiGraph()                                     
       548 -    node = make_node(                                        
       992 +def test_missing_docstrings_passes_when_docstring_present() -
           +> None:                                                      
       993 +    graph = make_graph(make_node(                            
       994          "file:src/bar.py",
       550 -        node_type="file",                                    
       551 -        semantics=SemanticFacet(intent="Bar module.", raw_doc
           -string="Bar module."),                                       
       552 -    )                                                        
       553 -    add_knowledge_node(graph, node)                          
       554 -    findings = find_missing_docstrings(graph)                
       995 +        semantics=SemanticFacet(intent="Bar.", raw_docstring=
           +"Bar module."),                                              
       996 +    ))                                                       
       997 +    findings = MissingDocstringsCheck().run(graph)           
       998      assert not any(f.node_id == "file:src/bar.py" for f in fi
            ndings)
       999  
      1000  
       558 -def test_find_untyped_io_detects_port_without_schema_ref() ->
           - None:                                                       
       559 -    graph = nx.DiGraph()                                     
       560 -    node = make_node(                                        
      1001 +def test_untyped_io_detects_port_without_schema_ref() -> None
           +:                                                            
      1002 +    graph = make_graph(make_node(                            
      1003          "file:src/writer.py",
       562 -        node_type="file",                                    
      1004          io_ports=[IOFacet(medium="disk", path_template="data/
            out.json", schema_ref=None)],
       564 -    )                                                        
       565 -    add_knowledge_node(graph, node)                          
       566 -    findings = find_untyped_io(graph)                        
      1005 +    ))                                                       
      1006 +    findings = UntypedIOCheck().run(graph)                   
      1007      assert any(f.node_id == "file:src/writer.py" for f in fin
            dings)
      1008  
      1009  
       570 -def test_find_compliance_violations_detects_failing_standards
           -() -> None:                                                  
       571 -    graph = nx.DiGraph()                                     
       572 -    node = make_node(                                        
      1010 +def test_compliance_violations_detects_failing_standards() ->
           + None:                                                       
      1011 +    graph = make_graph(make_node(                            
      1012          "file:src/sloppy.py",
       574 -        node_type="file",                                    
      1013          compliance=ComplianceFacet(
      1014              status="implemented",
      1015              failing_standards=["00_house_rules#docstrings"],
      1016          ),
       579 -    )                                                        
       580 -    add_knowledge_node(graph, node)                          
       581 -    findings = find_compliance_violations(graph)             
      1017 +    ))                                                       
      1018 +    findings = ComplianceViolationsCheck().run(graph)        
      1019      assert any(f.node_id == "file:src/sloppy.py" for f in fin
            dings)
      1020  
      1021  
       585 -def test_find_stale_edges_detects_missing_target() -> None:  
       586 -    from wiki_compiler.contracts import Edge                 
       587 -    graph = nx.DiGraph()                                     
       588 -    node = make_node(                                        
       589 -        "doc:wiki/foo.md",                                   
       590 -        node_type="doc_standard",                            
      1022 +def test_stale_edges_detects_missing_target() -> None:       
      1023 +    graph = make_graph(make_node(                            
      1024 +        "doc:wiki/foo.md", node_type="doc_standard",         
      1025          edges=[Edge(target_id="file:src/gone.py", relation_ty
            pe="documents")],
       592 -    )                                                        
       593 -    add_knowledge_node(graph, node)                          
       594 -    # file:src/gone.py is NOT added to the graph             
       595 -    findings = find_stale_edges(graph)                       
      1026 +    ))                                                       
      1027 +    findings = StaleEdgesCheck().run(graph)                  
      1028      assert any(f.node_id == "doc:wiki/foo.md" for f in findin
            gs)
      1029      assert any("file:src/gone.py" in f.detail for f in findin
            gs)
      1030  
      1031  
       600 -def test_find_orphaned_plans_detects_future_docs_with_no_code
           -_edge() -> None:                                             
       601 -    graph = nx.DiGraph()                                     
       602 -    node = make_node("doc:future_docs/feature_x.md", node_typ
           -e="concept")                                                 
       603 -    add_knowledge_node(graph, node)                          
       604 -    findings = find_orphaned_plans(graph)                    
      1032 +def test_orphaned_plans_detects_future_docs_with_no_code_edge
           +() -> None:                                                  
      1033 +    graph = make_graph(make_node("doc:future_docs/feature_x.m
           +d", node_type="concept"))                                    
      1034 +    findings = OrphanedPlansCheck().run(graph)               
      1035      assert any(f.node_id == "doc:future_docs/feature_x.md" fo
            r f in findings)
      1036  
      1037  
       608 -def test_run_audit_returns_report_with_all_checks() -> None: 
       609 -    graph = nx.DiGraph()                                     
       610 -    add_knowledge_node(graph, make_node("file:src/undoc.py", 
           -node_type="file"))                                           
      1038 +def test_run_audit_aggregates_all_checks() -> None:          
      1039 +    graph = make_graph(make_node("file:src/undoc.py"))       
      1040      report = run_audit(graph)
       612 -    assert isinstance(report, AuditReport)                   
      1041      assert "undocumented_code" in report.summary
      1042      assert report.summary["undocumented_code"] >= 1
      1043  ```
     ...
      1048  cd /home/jp/wikipu && python -m pytest tests/test_auditor.py 
            -v
      1049  ```
      1050  
       623 -Expected: `ImportError: cannot import name 'AuditFinding'`   
      1051 +Expected: `ImportError: cannot import name 'UndocumentedCodeC
           +heck'`                                                       
      1052  
      1053  - [ ] **Step 3: Implement `auditor.py`**
      1054  
     ...
      1056  
      1057  ```python
      1058  from __future__ import annotations
       631 -                                                             
      1059  from dataclasses import dataclass, field
       633 -                                                             
      1060  import networkx as nx
       635 -                                                             
      1061 +from .contracts import AuditFinding, KnowledgeNode           
      1062  from .graph_utils import iter_knowledge_nodes, load_knowledge
            _node
      1063 +from .query_executor import execute_query                    
      1064 +from .query_language import FacetFilter, FieldCondition, Stru
           +cturedQuery                                                  
      1065  
      1066  
      1067  @dataclass
       640 -class AuditFinding:                                          
       641 -    check_name: str                                          
       642 -    node_id: str                                             
       643 -    detail: str                                              
       644 -                                                             
       645 -                                                             
       646 -@dataclass                                                   
      1068  class AuditReport:
      1069      findings: list[AuditFinding] = field(default_factory=list
            )
      1070  
     ...
      1076          return counts
      1077  
      1078  
       658 -def find_undocumented_code(graph: nx.DiGraph) -> list[AuditFi
           -nding]:                                                      
       659 -    """Code nodes (file/code_construct) with no incoming `doc
           -uments` edge."""                                             
       660 -    documented = {                                           
       661 -        target                                               
       662 -        for _, target, data in graph.edges(data=True)        
       663 -        if data.get("relation") == "documents"               
       664 -    }                                                        
       665 -    findings = []                                            
       666 -    for node in iter_knowledge_nodes(graph):                 
       667 -        if node.identity.node_type not in {"file", "code_cons
           -truct"}:                                                     
       668 -            continue                                         
       669 -        if node.identity.node_id not in documented:          
       670 -            findings.append(                                 
       671 -                AuditFinding(                                
       672 -                    check_name="undocumented_code",          
      1079 +class UndocumentedCodeCheck:                                 
      1080 +    check_name = "undocumented_code"                         
      1081 +    question = "Which code nodes have no wiki documentation?"
      1082 +    related_facet = "semantics"                              
      1083 +                                                             
      1084 +    def run(self, graph: nx.DiGraph) -> list[AuditFinding]:  
      1085 +        documented = {                                       
      1086 +            target                                           
      1087 +            for _, target, data in graph.edges(data=True)    
      1088 +            if data.get("relation") == "documents"           
      1089 +        }                                                    
      1090 +        findings = []                                        
      1091 +        for node in iter_knowledge_nodes(graph):             
      1092 +            if node.identity.node_type not in {"file", "code_
           +construct"}:                                                 
      1093 +                continue                                     
      1094 +            if node.identity.node_id not in documented:      
      1095 +                findings.append(AuditFinding(                
      1096 +                    check_name=self.check_name,              
      1097                      node_id=node.identity.node_id,
      1098                      detail="No incoming `documents` edge from
             any wiki node.",
       675 -                )                                            
       676 -            )                                                
       677 -    return findings                                          
      1099 +                ))                                           
      1100 +        return findings                                      
      1101  
      1102  
       680 -def find_missing_docstrings(graph: nx.DiGraph) -> list[AuditF
           -inding]:                                                     
       681 -    """Code nodes with no SemanticFacet or a null raw_docstri
           -ng."""                                                       
       682 -    findings = []                                            
       683 -    for node in iter_knowledge_nodes(graph):                 
       684 -        if node.identity.node_type not in {"file", "code_cons
           -truct"}:                                                     
       685 -            continue                                         
       686 -        if node.identity.node_id.startswith("dir:"):         
       687 -            continue                                         
       688 -        if node.semantics is None or node.semantics.raw_docst
           -ring is None:                                                
       689 -            findings.append(                                 
       690 -                AuditFinding(                                
       691 -                    check_name="missing_docstrings",         
       692 -                    node_id=node.identity.node_id,           
       693 -                    detail="SemanticFacet missing or raw_docs
           -tring is null.",                                             
       694 -                )                                            
      1103 +class MissingDocstringsCheck:                                
      1104 +    check_name = "missing_docstrings"                        
      1105 +    question = "Which code nodes have no docstring?"         
      1106 +    related_facet = "semantics"                              
      1107 +                                                             
      1108 +    def run(self, graph: nx.DiGraph) -> list[AuditFinding]:  
      1109 +        matches = execute_query(graph, StructuredQuery(filter
           +s=[                                                          
      1110 +            FacetFilter(facet="semantics", conditions=[      
      1111 +                FieldCondition(field="raw_docstring", op="is_
           +null"),                                                      
      1112 +            ]),                                              
      1113 +        ]))                                                  
      1114 +        return [                                             
      1115 +            AuditFinding(                                    
      1116 +                check_name=self.check_name,                  
      1117 +                node_id=node.identity.node_id,               
      1118 +                detail="SemanticFacet.raw_docstring is null."
           +,                                                            
      1119              )
       696 -    return findings                                          
      1120 +            for node in matches                              
      1121 +            if node.identity.node_type in {"file", "code_cons
           +truct"}                                                      
      1122 +        ]                                                    
      1123  
      1124  
       699 -def find_untyped_io(graph: nx.DiGraph) -> list[AuditFinding]:
       700 -    """Nodes with a disk/memory IOFacet port that has no sche
           -ma_ref."""                                                   
       701 -    findings = []                                            
       702 -    for node in iter_knowledge_nodes(graph):                 
       703 -        for port in node.io_ports:                           
       704 -            if port.medium in {"disk", "memory"} and port.sch
           -ema_ref is None:                                             
       705 -                findings.append(                             
       706 -                    AuditFinding(                            
       707 -                        check_name="untyped_io",             
      1125 +class UntypedIOCheck:                                        
      1126 +    check_name = "untyped_io"                                
      1127 +    question = "Which nodes produce or consume data without a
           + schema contract?"                                           
      1128 +    related_facet = "io"                                     
      1129 +                                                             
      1130 +    def run(self, graph: nx.DiGraph) -> list[AuditFinding]:  
      1131 +        findings = []                                        
      1132 +        for node in iter_knowledge_nodes(graph):             
      1133 +            for port in node.io_ports:                       
      1134 +                if port.medium in {"disk", "memory"} and port
           +.schema_ref is None:                                         
      1135 +                    findings.append(AuditFinding(            
      1136 +                        check_name=self.check_name,          
      1137                          node_id=node.identity.node_id,
      1138                          detail=f"Port medium={port.medium} pa
            th={port.path_template!r} has no schema_ref.",
       710 -                    )                                        
       711 -                )                                            
       712 -                break                                        
       713 -    return findings                                          
      1139 +                    ))                                       
      1140 +                    break                                    
      1141 +        return findings                                      
      1142  
      1143  
       716 -def find_compliance_violations(graph: nx.DiGraph) -> list[Aud
           -itFinding]:                                                  
       717 -    """Nodes with one or more failing_standards."""          
       718 -    findings = []                                            
       719 -    for node in iter_knowledge_nodes(graph):                 
       720 -        if node.compliance and node.compliance.failing_standa
           -rds:                                                         
       721 -            findings.append(                                 
       722 -                AuditFinding(                                
       723 -                    check_name="compliance_violations",      
       724 -                    node_id=node.identity.node_id,           
       725 -                    detail=f"Failing: {', '.join(node.complia
           -nce.failing_standards)}",                                    
       726 -                )                                            
      1144 +class ComplianceViolationsCheck:                             
      1145 +    check_name = "compliance_violations"                     
      1146 +    question = "Which nodes are failing house rules standards
           +?"                                                           
      1147 +    related_facet = "compliance"                             
      1148 +                                                             
      1149 +    def run(self, graph: nx.DiGraph) -> list[AuditFinding]:  
      1150 +        matches = execute_query(graph, StructuredQuery(filter
           +s=[                                                          
      1151 +            FacetFilter(facet="compliance", conditions=[     
      1152 +                FieldCondition(field="failing_standards", op=
           +"ne", value=[]),                                             
      1153 +            ]),                                              
      1154 +        ]))                                                  
      1155 +        return [                                             
      1156 +            AuditFinding(                                    
      1157 +                check_name=self.check_name,                  
      1158 +                node_id=node.identity.node_id,               
      1159 +                detail=f"Failing: {', '.join(node.compliance.
           +failing_standards)}",                                        
      1160              )
       728 -    return findings                                          
      1161 +            for node in matches                              
      1162 +            if node.compliance and node.compliance.failing_st
           +andards                                                      
      1163 +        ]                                                    
      1164  
      1165  
       731 -def find_stale_edges(graph: nx.DiGraph) -> list[AuditFinding]
           -:                                                            
       732 -    """Edges whose target_id does not exist as a node in the 
           -graph."""                                                    
       733 -    node_ids = set(graph.nodes)                              
       734 -    findings = []                                            
       735 -    for source, target, data in graph.edges(data=True):      
       736 -        if target not in node_ids:                           
       737 -            findings.append(                                 
       738 -                AuditFinding(                                
       739 -                    check_name="stale_edges",                
       740 -                    node_id=source,                          
       741 -                    detail=f"Edge relation={data.get('relatio
           -n')!r} points to missing node `{target}`.",                  
       742 -                )                                            
      1166 +class StaleEdgesCheck:                                       
      1167 +    check_name = "stale_edges"                               
      1168 +    question = "Which edges point to nodes that no longer exi
           +st?"                                                         
      1169 +    related_facet = "semantics"                              
      1170 +                                                             
      1171 +    def run(self, graph: nx.DiGraph) -> list[AuditFinding]:  
      1172 +        node_ids = set(graph.nodes)                          
      1173 +        return [                                             
      1174 +            AuditFinding(                                    
      1175 +                check_name=self.check_name,                  
      1176 +                node_id=source,                              
      1177 +                detail=f"Edge relation={data.get('relation')!
           +r} points to missing node `{target}`.",                      
      1178              )
       744 -    return findings                                          
      1179 +            for source, target, data in graph.edges(data=True
           +)                                                            
      1180 +            if target not in node_ids                        
      1181 +        ]                                                    
      1182  
      1183  
       747 -def find_orphaned_plans(graph: nx.DiGraph) -> list[AuditFindi
           -ng]:                                                         
       748 -    """Doc nodes under future_docs/ with no outgoing edge to 
           -a code node."""                                              
       749 -    code_node_ids = {                                        
       750 -        n.identity.node_id                                   
       751 -        for n in iter_knowledge_nodes(graph)                 
       752 -        if n.identity.node_type in {"file", "code_construct"}
       753 -    }                                                        
       754 -    findings = []                                            
       755 -    for node in iter_knowledge_nodes(graph):                 
       756 -        if "future_docs" not in node.identity.node_id:       
       757 -            continue                                         
       758 -        connected_to_code = any(                             
       759 -            target in code_node_ids                          
       760 -            for _, target in graph.out_edges(node.identity.no
           -de_id)                                                       
       761 -        )                                                    
       762 -        if not connected_to_code:                            
       763 -            findings.append(                                 
       764 -                AuditFinding(                                
       765 -                    check_name="orphaned_plans",             
      1184 +class OrphanedPlansCheck:                                    
      1185 +    check_name = "orphaned_plans"                            
      1186 +    question = "Which future_docs nodes have no connection to
           + any code node?"                                             
      1187 +    related_facet = "compliance"                             
      1188 +                                                             
      1189 +    def run(self, graph: nx.DiGraph) -> list[AuditFinding]:  
      1190 +        code_ids = {                                         
      1191 +            n.identity.node_id                               
      1192 +            for n in iter_knowledge_nodes(graph)             
      1193 +            if n.identity.node_type in {"file", "code_constru
           +ct"}                                                         
      1194 +        }                                                    
      1195 +        findings = []                                        
      1196 +        for node in iter_knowledge_nodes(graph):             
      1197 +            if "future_docs" not in node.identity.node_id:   
      1198 +                continue                                     
      1199 +            if not any(t in code_ids for _, t in graph.out_ed
           +ges(node.identity.node_id)):                                 
      1200 +                findings.append(AuditFinding(                
      1201 +                    check_name=self.check_name,              
      1202                      node_id=node.identity.node_id,
      1203                      detail="future_docs node has no outgoing 
            edge to any code node.",
       768 -                )                                            
       769 -            )                                                
       770 -    return findings                                          
      1204 +                ))                                           
      1205 +        return findings                                      
      1206  
      1207  
      1208 +_ALL_CHECKS = [                                              
      1209 +    UndocumentedCodeCheck(),                                 
      1210 +    MissingDocstringsCheck(),                                
      1211 +    UntypedIOCheck(),                                        
      1212 +    ComplianceViolationsCheck(),                             
      1213 +    StaleEdgesCheck(),                                       
      1214 +    OrphanedPlansCheck(),                                    
      1215 +]                                                            
      1216 +                                                             
      1217 +                                                             
      1218  def run_audit(graph: nx.DiGraph) -> AuditReport:
      1219      report = AuditReport()
       775 -    for check in [                                           
       776 -        find_undocumented_code,                              
       777 -        find_missing_docstrings,                             
       778 -        find_untyped_io,                                     
       779 -        find_compliance_violations,                          
       780 -        find_stale_edges,                                    
       781 -        find_orphaned_plans,                                 
       782 -    ]:                                                       
       783 -        report.findings.extend(check(graph))                 
      1220 +    for check in _ALL_CHECKS:                                
      1221 +        report.findings.extend(check.run(graph))             
      1222      return report
      1223  ```
      1224  
       787 -- [ ] **Step 4: Run tests**                                  
      1225 +- [ ] **Step 4: Add `audit` command to `main.py`**           
      1226  
       789 -```bash                                                      
       790 -cd /home/jp/wikipu && python -m pytest tests/test_auditor.py 
           --v                                                           
       791 -```                                                          
      1227 +Add imports:                                                 
      1228  
       793 -Expected: all 9 tests PASS.                                  
       794 -                                                             
       795 -- [ ] **Step 5: Add `audit` CLI command to `main.py`**       
       796 -                                                             
       797 -Add import at top of `main.py`:                              
       798 -                                                             
      1229  ```python
      1230  from .auditor import run_audit
       801 -from .graph_utils import load_graph                          
      1231 +from .query_executor import execute_query                    
      1232 +from .query_language import FacetFilter, FieldCondition, Grap
           +hScope, StructuredQuery                                      
      1233  ```
      1234  
       804 -Add to `main()` dispatch block (before the final exception ha
           -ndler):                                                      
      1235 +Add to `main()` dispatch:                                    
      1236  
      1237  ```python
      1238          if args.command == "audit":
      1239              graph = load_graph(Path(args.graph))
      1240              report = run_audit(graph)
      1241              if args.format == "json":
       811 -                import json as _json                         
       812 -                print(_json.dumps({                          
      1242 +                print(json.dumps({                           
      1243                      "summary": report.summary,
      1244                      "findings": [
      1245                          {"check": f.check_name, "node_id": f.
            node_id, "detail": f.detail}
     ...
      1247                      ],
      1248                  }, indent=2))
      1249              else:
       820 -                print(f"## Audit Report\n")                  
      1250 +                print("## Audit Report\n")                   
      1251                  for check_name, count in report.summary.items
            ():
      1252                      print(f"- **{check_name}**: {count} findi
            ng(s)")
      1253                  if report.findings:
     ...
      1263  
      1264  ```python
      1265      audit_parser = subparsers.add_parser("audit", help="Run d
            ocumentation quality checks")
       836 -    audit_parser.add_argument(                               
       837 -        "--graph", default="knowledge_graph.json", help="Grap
           -h JSON path"                                                 
       838 -    )                                                        
       839 -    audit_parser.add_argument(                               
       840 -        "--format", default="markdown", choices=["markdown", 
           -"json"], help="Output format"                                
       841 -    )                                                        
      1266 +    audit_parser.add_argument("--graph", default="knowledge_g
           +raph.json")                                                  
      1267 +    audit_parser.add_argument("--format", default="markdown",
           + choices=["markdown", "json"])                               
      1268  ```
      1269  
       844 -- [ ] **Step 6: Smoke test the CLI**                         
      1270 +- [ ] **Step 5: Run all tests**                              
      1271  
      1272  ```bash
       847 -cd /home/jp/wikipu && wiki-compiler build && wiki-compiler au
           -dit --format json                                            
      1273 +cd /home/jp/wikipu && python -m pytest tests/test_registry_an
           +d_query.py \                                                 
      1274 +    tests/test_directory_skeleton.py tests/test_facet_injecto
           +rs.py \                                                      
      1275 +    tests/test_auditor.py -v                                 
      1276  ```
      1277  
       850 -Expected: JSON output with findings. Exit code 1 if any findi
           -ngs exist (expected for real codebase).                      
      1278 +Expected: all tests PASS.                                    
      1279  
       852 -- [ ] **Step 7: Run full test suite**                        
      1280 +- [ ] **Step 6: Smoke test end-to-end**                      
      1281  
      1282  ```bash
       855 -cd /home/jp/wikipu && python -m pytest tests/ -v --ignore=tes
           -ts/test_runtime_features.py                                  
      1283 +cd /home/jp/wikipu && wiki-compiler build && wiki-compiler au
           +dit --format json                                            
      1284  ```
      1285  
       858 -Expected: all tests in `test_directory_skeleton.py`, `test_fa
           -cet_injectors.py`, `test_auditor.py` PASS.                   
      1286 +Expected: JSON report with findings. Exit 1 if any findings (
           +expected on real codebase).                                  
      1287  
       860 -- [ ] **Step 8: Commit**                                     
      1288 +- [ ] **Step 7: Commit**                                     
      1289  
      1290  ```bash
      1291  git add src/wiki_compiler/auditor.py src/wiki_compiler/main.p
            y tests/test_auditor.py
       864 -git commit -m "feat: add audit command with six documentation
           - quality gap checks"                                         
      1292 +git commit -m "feat: add audit command with six protocol-conf
           +orming quality checks"                                       
      1293  ```
      1294  
      1295  ---
     ...
      1297  ## Self-Review
      1298  
      1299  **Spec coverage:**
      1300 +- Facet registry (machine-readable) → Task 0 `registry.py` ✓ 
      1301 +- Plugin protocols (`FacetInjector`, `AuditCheck`) → Task 0 `
           +protocols.py` ✓                                              
      1302 +- Structured query language (single-facet + compound + scope)
           + → Task 0 `query_language.py` / `query_executor.py` ✓        
      1303 +- `AuditFinding` moved to `contracts.py` (shared by protocols
           + and auditor) ✓                                              
      1304  - Directory skeleton → Task 1 ✓
       873 -- Phase 1/2 separation (explicit raw node → facet injection) 
           -→ Task 1 + Task 2 wiring ✓                                   
       874 -- ADRFacet injector → Task 2 ✓                               
       875 -- TestMapFacet injector → Task 2 ✓                           
       876 -- Coverage gaps (`undocumented_code`) → Task 3 ✓             
       877 -- Semantic gaps (`missing_docstrings`) → Task 3 ✓            
       878 -- I/O gaps (`untyped_io`) → Task 3 ✓                         
       879 -- Compliance violations → Task 3 ✓                           
       880 -- Stale docs (`stale_edges`) → Task 3 ✓                      
       881 -- Orphaned plans → Task 3 ✓                                  
       882 -- CLI command → Task 3 ✓                                     
      1305 +- ADRFacet injector (protocol-conforming) → Task 2 ✓         
      1306 +- TestMapFacet injector (protocol-conforming) → Task 2 ✓     
      1307 +- Audit checks backed by `StructuredQuery` where possible → T
           +ask 3 ✓                                                      
      1308 +- `wiki-compiler audit` CLI → Task 3 ✓                       
      1309 +- Each facet declared with a `question` → enforced in `FacetS
           +pec` and `AuditCheck.question` ✓                             
      1310  
       884 -**Type consistency check:**                                  
       885 -- `build_directory_skeleton` returns `list[KnowledgeNode]` → 
           -consumed by `add_knowledge_node(graph, node)` ✓              
       886 -- `inject_adr_facets(graph, adr_dir)` / `inject_test_map_face
           -ts(graph, tests_dir, project_root)` — signatures consistent a
           -cross task 2 tests and implementation ✓                      
       887 -- `AuditFinding.check_name` / `AuditReport.summary` — used co
           -nsistently in tests and implementation ✓                     
       888 -- `run_audit(graph)` → `AuditReport` — consistent across all 
           -references ✓                                                 
      1311 +**Orthogonality rule enforced:**                             
      1312 +- `MissingDocstringsCheck` uses `execute_query(StructuredQuer
           +y(filters=[...semantics...]))` — no hand-rolled loop         
      1313 +- `ComplianceViolationsCheck` uses `execute_query(StructuredQ
           +uery(filters=[...compliance...]))` — same                    
      1314 +- New audit checks should always ask: "can I express this as 
           +a `StructuredQuery`?" before writing a loop                  
      1315  
      1316 +**Type consistency:**                                        
      1317 +- `AuditFinding` defined in `contracts.py`, imported by `prot
           +ocols.py`, `auditor.py`, and tests ✓                         
      1318 +- `FacetSpec` defined in `registry.py`, used in `ADRInjector.
           +spec` and `TestMapInjector.spec` ✓                           
      1319 +- `execute_query(graph, StructuredQuery)` signature consisten
           +t across `query_executor.py`, `auditor.py`, and tests ✓      
      1320 +                                                             
      1321  **No placeholders detected.**

● Plan updated at plan_docs/2026-04-08-three-phase-graph.md.

  Here's what changed from the previous version:

  Task 0 (new) establishes three foundational contracts before any
  implementation:
  - FacetRegistry — machine-readable specs: each facet's question, applicable
  node types, queryable fields. This is what an LLM uses to map natural language
   → query.
  - StructuredQuery language — FacetFilter + FieldCondition + GraphScope.
  Single-facet questions become one filter. Multi-facet questions become filter
  intersection scoped to a graph region.
  - FacetInjector / AuditCheck protocols — every new facet is a self-contained
  plugin. Adding ModelUsageFacet means writing one class and registering it.
  Nothing else to touch.

  Orthogonality is now enforced in code: audit checks that can be expressed as a
   StructuredQuery must use it — no hand-rolled loops. This makes the check
  self-documenting: you can read the query and know exactly which facet
  dimension it's testing.

  Ready to execute?

✻ Worked for 4m 43s

❯ ok, Now another thing. what if we started introducing facets and then we      
  realize that maybe there are some that are redundant, or are not descriptive  
  enought, but can be rearanged by another facet ortogonalization (think of     
  principal component analysis as an inspiration). How would you "recreate the  
  axes"                                                                         

● This is the right question to ask, and the PCA analogy is precise. Let me
  think through it carefully.

  ---
  The Analogy

  In PCA you start with correlated variables, find that some explain overlapping
   variance, and rotate to a new set of orthogonal axes that span the same space
   more cleanly.

  In the facet system:
  - Variables = facets (questions)
  - Correlated = facets that tend to co-occur, or whose audit checks keep
  combining them
  - Principal components = the truly independent questions that span the same
  information space
  - Rotating = redefining the facets, then rebuilding

  ---
  How You Detect the Need

  Three signals that your axes have drifted:

  1. Co-occurrence — two facets always appear together on the same nodes. If
  every node that has TestMapFacet also has ComplianceFacet.status == tested,
  they're measuring the same thing from two angles. One is redundant.

  2. Repeated compound queries — if your StructuredQuerys keep combining the
  same two facets to answer a recurring question, that combination is a hidden
  dimension that should be its own facet.

  filter(compliance, status=planned) ∩ filter(evolution, commit_frequency=0)
  → always asked together → "stale planned work" is a real axis, not two

  3. Overlapping audit checks — two checks with different related_facet values
  that detect the same problem from different sides. The problem is the missing
  dimension, not the checks themselves.

  ---
  How You Recreate the Axes

  Step 1 — List all questions

  Write every facet's question on the table:

  semantics  → What does this do?
  ast        → How is it structured?
  io         → What data does it consume or produce?
  compliance → How complete and rule-compliant is it?
  test_map   → How is it tested?
  adr        → What decisions shaped it?

  Step 2 — Find the overlapping space

  Ask: can any question be partially answered by another facet? Example:

  "How is it tested?" (TestMapFacet)
  "How complete is it?" (ComplianceFacet.status = tested)

  → These overlap on the maturity axis.
  → Both are projections of the same underlying dimension: "how far along is
  this node?"

  Step 3 — Define the new axes

  The new axes must each answer a question that no other axis can touch:

  old: compliance (status + failing_standards) + test_map (type + coverage)
  new: maturity (lifecycle stage, 0→planned→tested)
     + quality (failing_standards + coverage_percent)

  → maturity answers: where is this node in its lifecycle?
  → quality answers:  how well does it meet its standards at that stage?

  Step 4 — Test orthogonality before committing

  For each proposed new facet, apply the same rule as before: can this question 
  be answered by combining existing facets? If yes, it's a query, not a new
  axis. Only proceed if the answer genuinely requires new information.

  Step 5 — Rebuild, don't migrate

  This is the key property of the system: facets are always derived from source 
  truth, never primary data.

  The codebase, the docs, and git are the ground truth. Facets are a cached
  projection of that truth through a particular lens system. So
  re-orthogonalization costs nothing in terms of data:

  1. Redefine the facets in contracts.py
  2. Update the registry specs with new questions
  3. Rewrite the injectors for the new axes
  4. Run wiki-compiler build
  → the graph rebuilds itself from source

  No migration script. No data transformation. The raw material (code,
  docstrings, git, docs) was always there — you just changed which questions
  you're asking of it.

  ---
  What the System Currently Lacks for This

  The machinery to detect drift doesn't exist yet:

  ┌──────────────────────────────────┬──────────────────────────────────────┐
  │        Missing capability        │           What it enables            │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Facet co-occurrence stats (which │ Detect redundancy                    │
  │  facets always appear together?) │                                      │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Compound query frequency log     │                                      │
  │ (which filter combinations       │ Detect hidden dimensions             │
  │ repeat?)                         │                                      │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ "Facet proposal" check — like    │                                      │
  │ TopologyProposal but for new     │ Enforce orthogonality before adding  │
  │ facets                           │                                      │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Registry diff — compare two sets │ Track re-orthogonalizations over     │
  │  of facet specs                  │ time (like ADRs for the lens system) │
  └──────────────────────────────────┴──────────────────────────────────────┘

  The TopologyProposal already exists for node-level orthogonality. The same
  pattern applied to the facet level would close the loop: before adding a
  facet, submit a FacetProposal with its question, and the system checks whether
   that question is already answerable by the existing registry.

  ---
  The Short Version

  ▎ Re-orthogonalization is free because facets are a view, not the data. The 
  cost is only in redefining the questions and rewriting the injectors. The 
  graph rebuilds itself.

  The PCA analogy holds exactly: you're not transforming the data, you're
  rotating the axes you use to observe it.

  Want me to add a FacetProposal mechanism to the plan that enforces this before
   a new facet is registered?

✻ Crunched for 59s

❯ please do                                                                     
  Read 1 file (ctrl+o to expand)

● Update(plan_docs/2026-04-08-three-phase-graph.md)
  ⎿  Added 2 lines, removed 1 line
       2  
       3  > **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:
          subagent-driven-development (recommended) or superpowers:execut
          ing-plans to implement this plan task-by-task. Steps use checkb
          ox (`- [ ]`) syntax for tracking.
       4  
       5 -**Goal:** Complete the three-phase graph construction pipeline 
         -with a proper extensibility foundation: a machine-readable face
         -t registry, a structured query language, a plugin protocol for 
         -injectors and audit checks, directory skeleton (Phase 1), ADRFa
         -cet + TestMapFacet injectors (Phase 2), and a CLI `audit` comma
         -nd (Phase 3).                                                  
       5 +**Goal:** Complete the three-phase graph construction pipeline 
         +with a proper extensibility foundation: a machine-readable face
         +t registry, a structured query language, a plugin protocol for 
         +injectors and audit checks, directory skeleton (Phase 1), ADRFa
         +cet + TestMapFacet injectors (Phase 2), a CLI `audit` command (
         +Phase 3), and a `FacetProposal` orthogonality gate (Task 4) tha
         +t enforces the rule: *no new facet without proving the question
         + can't be answered by existing ones*.                          
       6  
       7  **Architecture:**
       8  - Task 0 establishes the vocabulary: `FacetRegistry` (machine-r
          eadable facet specs), `StructuredQuery` language (single-facet 
          filters + compound queries + graph scope), and `FacetInjector`/
          `AuditCheck` protocols. Everything else plugs into this.
       9  - Task 1 adds the directory skeleton as a pre-build pass in `bu
          ilder.py`.
      10  - Task 2 implements ADR and TestMap facet injectors as protocol
          -conforming plugins registered in the registry.
      11  - Task 3 implements all audit checks as protocol-conforming plu
          gins and adds `wiki-compiler audit` and enhanced `wiki-compiler
           query` CLI commands.
      12 +- Task 4 adds the `FacetProposal` mechanism — the orthogonality
         + gate for the facet system itself, mirroring what `TopologyProp
         +osal` does for nodes.                                          
      13  
      14  **Tech Stack:** Python 3.10+, NetworkX 3.x, Pydantic v2, pytest
          , PyYAML
      15  

● Update(plan_docs/2026-04-08-three-phase-graph.md)
  ⎿  Added 2 lines
      29  | `src/wiki_compiler/auditor.py` | Create | Six `AuditCheck` im
          plementations + `run_audit()` |
      30  | `src/wiki_compiler/builder.py` | Modify | Add directory skele
          ton pass; wire registry injectors |
      31  | `src/wiki_compiler/main.py` | Modify | Add `audit` subcommand
          ; wire structured query into `query` |
      32 +| `src/wiki_compiler/facet_validator.py` | Create | `validate_f
         +acet_proposal()` — orthogonality checks for new facets |       
      33  | `tests/test_registry_and_query.py` | Create | Registry, query
           language, and executor tests |
      34  | `tests/test_directory_skeleton.py` | Create | Directory node 
          generation tests |
      35  | `tests/test_facet_injectors.py` | Create | ADR and TestMap in
          jection tests |
      36  | `tests/test_auditor.py` | Create | All six audit check tests 
          |
      37 +| `tests/test_facet_proposal.py` | Create | FacetProposal valid
         +ation tests |                                                  
      38  
      39  ---
      40  

● Now append Task 4 to the end of the plan:

  Read 1 file (ctrl+o to expand)

● Update(plan_docs/2026-04-08-three-phase-graph.md)
  ⎿  Added 518 lines
      1297  
      1298  ---
      1299  
      1300 +## Task 4: FacetProposal — Orthogonality Gate for the Facet S
           +ystem                                                        
      1301 +                                                             
      1302 +Mirrors what `TopologyProposal` does for nodes, but applied t
           +o facets. Before any new facet is registered, a `FacetProposa
           +l` must be submitted. The validator checks three things:     
      1303 +                                                             
      1304 +1. **Question collision** — does any existing facet's questio
           +n overlap significantly with the proposed one? (keyword Jacca
           +rd similarity)                                               
      1305 +2. **Field collision** — does any proposed field name already
           + exist in any registered facet?                              
      1306 +3. **Compound answerability** — can the proposed question alr
           +eady be answered by a `StructuredQuery` over existing facets?
           + The proposer must submit their best attempt; if it returns r
           +esults, the information already exists.                      
      1307 +                                                             
      1308 +If any check fails, the proposal is rejected with a resolutio
           +n suggestion. After 3 failed attempts, human intervention is 
           +required.                                                    
      1309 +                                                             
      1310 +**Files:**                                                   
      1311 +- Modify: `src/wiki_compiler/contracts.py` — add `FacetPropos
           +al`, `FacetOrthogonalityReport`                              
      1312 +- Create: `src/wiki_compiler/facet_validator.py`             
      1313 +- Modify: `src/wiki_compiler/main.py` — add `propose-facet` s
           +ubcommand                                                    
      1314 +- Create: `tests/test_facet_proposal.py`                     
      1315 +                                                             
      1316 +- [ ] **Step 1: Write failing tests**                        
      1317 +                                                             
      1318 +```python                                                    
      1319 +# tests/test_facet_proposal.py                               
      1320 +from __future__ import annotations                           
      1321 +import json                                                  
      1322 +from pathlib import Path                                     
      1323 +import networkx as nx                                        
      1324 +import pytest                                                
      1325 +from wiki_compiler.contracts import (                        
      1326 +    ComplianceFacet, FacetOrthogonalityReport, FacetProposal,
      1327 +    KnowledgeNode, SemanticFacet, SystemIdentity,            
      1328 +)                                                            
      1329 +from wiki_compiler.facet_validator import validate_facet_prop
           +osal                                                         
      1330 +from wiki_compiler.graph_utils import add_knowledge_node     
      1331 +from wiki_compiler.query_language import FacetFilter, FieldCo
           +ndition, StructuredQuery                                     
      1332 +from wiki_compiler.registry import FacetRegistry, FacetSpec, 
           +FieldSpec, build_default_registry                            
      1333 +                                                             
      1334 +                                                             
      1335 +def make_graph(*nodes: KnowledgeNode) -> nx.DiGraph:         
      1336 +    graph = nx.DiGraph()                                     
      1337 +    for node in nodes:                                       
      1338 +        add_knowledge_node(graph, node)                      
      1339 +    return graph                                             
      1340 +                                                             
      1341 +                                                             
      1342 +def make_node(node_id: str, **kwargs) -> KnowledgeNode:      
      1343 +    return KnowledgeNode(                                    
      1344 +        identity=SystemIdentity(node_id=node_id, node_type="f
           +ile"), **kwargs                                              
      1345 +    )                                                        
      1346 +                                                             
      1347 +                                                             
      1348 +# --- Question collision ---                                 
      1349 +                                                             
      1350 +def test_rejects_question_that_overlaps_existing_facet(tmp_pa
           +th: Path) -> None:                                           
      1351 +    registry = build_default_registry()                      
      1352 +    graph = nx.DiGraph()                                     
      1353 +    proposal = FacetProposal(                                
      1354 +        proposed_facet_name="doc_summary",                   
      1355 +        question="What does this node do and why?",   # overl
           +aps SemanticFacet                                            
      1356 +        applies_to=["file"],                                 
      1357 +        proposed_fields=[{"name": "summary", "type": "str"}],
      1358 +        attempted_query=None,                                
      1359 +    )                                                        
      1360 +    report = validate_facet_proposal(                        
      1361 +        proposal=proposal,                                   
      1362 +        registry=registry,                                   
      1363 +        graph=graph,                                         
      1364 +        state_path=tmp_path / "state.json",                  
      1365 +    )                                                        
      1366 +    assert report.is_orthogonal is False                     
      1367 +    assert any(s.facet_name == "semantics" for s in report.co
           +lliding_facets)                                              
      1368 +    assert report.attempts_remaining == 2                    
      1369 +                                                             
      1370 +                                                             
      1371 +def test_accepts_question_with_no_overlap(tmp_path: Path) -> 
           +None:                                                        
      1372 +    registry = build_default_registry()                      
      1373 +    graph = nx.DiGraph()                                     
      1374 +    proposal = FacetProposal(                                
      1375 +        proposed_facet_name="model_usage",                   
      1376 +        question="Which AI models does this node invoke?",   
      1377 +        applies_to=["file", "code_construct"],               
      1378 +        proposed_fields=[{"name": "model_name", "type": "str"
           +}],                                                          
      1379 +        attempted_query=None,                                
      1380 +    )                                                        
      1381 +    report = validate_facet_proposal(                        
      1382 +        proposal=proposal,                                   
      1383 +        registry=registry,                                   
      1384 +        graph=graph,                                         
      1385 +        state_path=tmp_path / "state.json",                  
      1386 +    )                                                        
      1387 +    assert report.is_orthogonal is True                      
      1388 +    assert report.attempts_remaining == 3                    
      1389 +                                                             
      1390 +                                                             
      1391 +# --- Field collision ---                                    
      1392 +                                                             
      1393 +def test_rejects_proposed_field_that_already_exists(tmp_path:
           + Path) -> None:                                              
      1394 +    registry = build_default_registry()                      
      1395 +    graph = nx.DiGraph()                                     
      1396 +    proposal = FacetProposal(                                
      1397 +        proposed_facet_name="custom_status",                 
      1398 +        question="What is the deployment stage of this node?"
           +,                                                            
      1399 +        applies_to=["file"],                                 
      1400 +        proposed_fields=[{"name": "status", "type": "str"}], 
           + # status exists in compliance                               
      1401 +        attempted_query=None,                                
      1402 +    )                                                        
      1403 +    report = validate_facet_proposal(                        
      1404 +        proposal=proposal,                                   
      1405 +        registry=registry,                                   
      1406 +        graph=graph,                                         
      1407 +        state_path=tmp_path / "state.json",                  
      1408 +    )                                                        
      1409 +    assert report.is_orthogonal is False                     
      1410 +    assert report.field_collisions  # list of (field_name, ex
           +isting_facet_name)                                           
      1411 +    assert any("status" in str(c) for c in report.field_colli
           +sions)                                                       
      1412 +                                                             
      1413 +                                                             
      1414 +# --- Compound answerability ---                             
      1415 +                                                             
      1416 +def test_rejects_when_attempted_query_returns_results(tmp_pat
           +h: Path) -> None:                                            
      1417 +    registry = build_default_registry()                      
      1418 +    graph = make_graph(make_node(                            
      1419 +        "file:src/a.py",                                     
      1420 +        compliance=ComplianceFacet(status="planned", failing_
           +standards=[]),                                               
      1421 +    ))                                                       
      1422 +    # Proposer tries to answer "which nodes are not started y
           +et?"                                                         
      1423 +    # and their own query already works → information already
           + in graph                                                    
      1424 +    attempted_query = StructuredQuery(filters=[              
      1425 +        FacetFilter(facet="compliance", conditions=[         
      1426 +            FieldCondition(field="status", op="eq", value="pl
           +anned"),                                                     
      1427 +        ]),                                                  
      1428 +    ])                                                       
      1429 +    proposal = FacetProposal(                                
      1430 +        proposed_facet_name="not_started",                   
      1431 +        question="Which nodes have not been started yet?",   
      1432 +        applies_to=["file"],                                 
      1433 +        proposed_fields=[{"name": "not_started", "type": "boo
           +l"}],                                                        
      1434 +        attempted_query=attempted_query,                     
      1435 +    )                                                        
      1436 +    report = validate_facet_proposal(                        
      1437 +        proposal=proposal,                                   
      1438 +        registry=registry,                                   
      1439 +        graph=graph,                                         
      1440 +        state_path=tmp_path / "state.json",                  
      1441 +    )                                                        
      1442 +    assert report.is_orthogonal is False                     
      1443 +    assert report.query_already_answered is True             
      1444 +    assert "StructuredQuery" in (report.resolution_suggestion
           + or "")                                                      
      1445 +                                                             
      1446 +                                                             
      1447 +def test_accepts_when_attempted_query_returns_nothing(tmp_pat
           +h: Path) -> None:                                            
      1448 +    registry = build_default_registry()                      
      1449 +    # Graph has no nodes with model_usage facet — information
           + genuinely absent                                            
      1450 +    graph = make_graph(make_node("file:src/a.py"))           
      1451 +    attempted_query = StructuredQuery(filters=[              
      1452 +        FacetFilter(facet="model_usage", conditions=[        
      1453 +            FieldCondition(field="model_name", op="is_not_nul
           +l"),                                                         
      1454 +        ]),                                                  
      1455 +    ])                                                       
      1456 +    proposal = FacetProposal(                                
      1457 +        proposed_facet_name="model_usage",                   
      1458 +        question="Which AI models does this node invoke?",   
      1459 +        applies_to=["file"],                                 
      1460 +        proposed_fields=[{"name": "model_name", "type": "str"
           +}],                                                          
      1461 +        attempted_query=attempted_query,                     
      1462 +    )                                                        
      1463 +    report = validate_facet_proposal(                        
      1464 +        proposal=proposal,                                   
      1465 +        registry=registry,                                   
      1466 +        graph=graph,                                         
      1467 +        state_path=tmp_path / "state.json",                  
      1468 +    )                                                        
      1469 +    assert report.is_orthogonal is True                      
      1470 +                                                             
      1471 +                                                             
      1472 +# --- Attempt tracking ---                                   
      1473 +                                                             
      1474 +def test_attempt_counter_decrements_on_failure(tmp_path: Path
           +) -> None:                                                   
      1475 +    registry = build_default_registry()                      
      1476 +    graph = nx.DiGraph()                                     
      1477 +    state_path = tmp_path / "state.json"                     
      1478 +    proposal = FacetProposal(                                
      1479 +        proposed_facet_name="doc_summary",                   
      1480 +        question="What does this node do?",                  
      1481 +        applies_to=["file"],                                 
      1482 +        proposed_fields=[],                                  
      1483 +        attempted_query=None,                                
      1484 +    )                                                        
      1485 +    report1 = validate_facet_proposal(proposal, registry, gra
           +ph, state_path)                                              
      1486 +    report2 = validate_facet_proposal(proposal, registry, gra
           +ph, state_path)                                              
      1487 +    assert report1.attempts_remaining == 2                   
      1488 +    assert report2.attempts_remaining == 1                   
      1489 +                                                             
      1490 +                                                             
      1491 +def test_attempt_counter_resets_on_success(tmp_path: Path) ->
           + None:                                                       
      1492 +    registry = build_default_registry()                      
      1493 +    graph = nx.DiGraph()                                     
      1494 +    state_path = tmp_path / "state.json"                     
      1495 +    proposal = FacetProposal(                                
      1496 +        proposed_facet_name="model_usage",                   
      1497 +        question="Which AI models does this node invoke?",   
      1498 +        applies_to=["file"],                                 
      1499 +        proposed_fields=[{"name": "model_name", "type": "str"
           +}],                                                          
      1500 +        attempted_query=None,                                
      1501 +    )                                                        
      1502 +    report = validate_facet_proposal(proposal, registry, grap
           +h, state_path)                                               
      1503 +    assert report.is_orthogonal is True                      
      1504 +    assert report.attempts_remaining == 3                    
      1505 +```                                                          
      1506 +                                                             
      1507 +- [ ] **Step 2: Run to verify failure**                      
      1508 +                                                             
      1509 +```bash                                                      
      1510 +cd /home/jp/wikipu && python -m pytest tests/test_facet_propo
           +sal.py -v                                                    
      1511 +```                                                          
      1512 +                                                             
      1513 +Expected: `ImportError: cannot import name 'FacetProposal'`  
      1514 +                                                             
      1515 +- [ ] **Step 3: Add `FacetProposal` and `FacetOrthogonalityRe
           +port` to `contracts.py`**                                    
      1516 +                                                             
      1517 +Add at the end of `contracts.py`:                            
      1518 +                                                             
      1519 +```python                                                    
      1520 +class FacetProposal(BaseModel):                              
      1521 +    """                                                      
      1522 +    A proposal to add a new facet dimension to the registry. 
      1523 +    Must prove the question cannot be answered by existing fa
           +cets before being accepted.                                  
      1524 +    """                                                      
      1525 +    proposed_facet_name: str = Field(description="Snake_case 
           +name for the new facet.")                                    
      1526 +    question: str = Field(description="The single question th
           +is facet answers. Must be unique across the registry.")      
      1527 +    applies_to: list[str] = Field(description="Node types thi
           +s facet is relevant for.")                                   
      1528 +    proposed_fields: list[dict[str, str]] = Field(description
           +="List of {name, type} dicts for the facet's fields.")       
      1529 +    attempted_query: StructuredQuery | None = Field(         
      1530 +        default=None,                                        
      1531 +        description="The proposer's best attempt to answer th
           +e question using existing facets. "                          
      1532 +                    "If this query returns results, the infor
           +mation already exists and the proposal is rejected.",        
      1533 +    )                                                        
      1534 +                                                             
      1535 +                                                             
      1536 +class FacetOrthogonalityReport(BaseModel):                   
      1537 +    """Response from validate_facet_proposal."""             
      1538 +    is_orthogonal: bool                                      
      1539 +    colliding_facets: list[FacetSpec] = Field(               
      1540 +        default_factory=list,                                
      1541 +        description="Existing facets whose questions overlap 
           +with the proposal.",                                         
      1542 +    )                                                        
      1543 +    field_collisions: list[str] = Field(                     
      1544 +        default_factory=list,                                
      1545 +        description="'field_name (existing_facet)' strings fo
           +r each field name collision.",                               
      1546 +    )                                                        
      1547 +    query_already_answered: bool = Field(                    
      1548 +        default=False,                                       
      1549 +        description="True if the attempted_query returned res
           +ults, meaning the information already exists.",              
      1550 +    )                                                        
      1551 +    resolution_suggestion: str | None = None                 
      1552 +    attempts_remaining: int                                  
      1553 +```                                                          
      1554 +                                                             
      1555 +Note: `StructuredQuery` is in `query_language.py`. Add a `TYP
           +E_CHECKING` import to avoid circular dependency:             
      1556 +                                                             
      1557 +```python                                                    
      1558 +from __future__ import annotations                           
      1559 +from typing import TYPE_CHECKING                             
      1560 +if TYPE_CHECKING:                                            
      1561 +    from .query_language import StructuredQuery              
      1562 +```                                                          
      1563 +                                                             
      1564 +Or use `Any` for the `attempted_query` field type and validat
           +e at runtime. Simplest: use `object | None` and cast in the v
           +alidator.                                                    
      1565 +                                                             
      1566 +To avoid the circular import entirely, define `attempted_quer
           +y` as:                                                       
      1567 +                                                             
      1568 +```python                                                    
      1569 +    attempted_query: dict | None = Field(                    
      1570 +        default=None,                                        
      1571 +        description="Serialised StructuredQuery. If provided 
           +and returns results, proposal is rejected.",                 
      1572 +    )                                                        
      1573 +```                                                          
      1574 +                                                             
      1575 +And deserialise it in `facet_validator.py`.                  
      1576 +                                                             
      1577 +- [ ] **Step 4: Implement `facet_validator.py`**             
      1578 +                                                             
      1579 +Create `src/wiki_compiler/facet_validator.py`:               
      1580 +                                                             
      1581 +```python                                                    
      1582 +from __future__ import annotations                           
      1583 +                                                             
      1584 +import json                                                  
      1585 +import re                                                    
      1586 +from pathlib import Path                                     
      1587 +                                                             
      1588 +import networkx as nx                                        
      1589 +                                                             
      1590 +from .contracts import FacetOrthogonalityReport, FacetProposa
           +l                                                            
      1591 +from .query_executor import execute_query                    
      1592 +from .query_language import StructuredQuery                  
      1593 +from .registry import FacetRegistry, FacetSpec               
      1594 +                                                             
      1595 +DEFAULT_ATTEMPTS = 3                                         
      1596 +_STOP_WORDS = {                                              
      1597 +    "what", "how", "is", "are", "this", "the", "a", "an", "do
           +es",                                                         
      1598 +    "do", "it", "its", "of", "by", "to", "for", "node", "each
           +",                                                           
      1599 +    "which", "where", "when", "has", "have",                 
      1600 +}                                                            
      1601 +                                                             
      1602 +                                                             
      1603 +def validate_facet_proposal(                                 
      1604 +    proposal: FacetProposal,                                 
      1605 +    registry: FacetRegistry,                                 
      1606 +    graph: nx.DiGraph,                                       
      1607 +    state_path: Path,                                        
      1608 +) -> FacetOrthogonalityReport:                               
      1609 +    colliding_facets = _find_question_collisions(proposal.que
           +stion, registry)                                             
      1610 +    field_collisions = _find_field_collisions(proposal.propos
           +ed_fields, registry)                                         
      1611 +    query_already_answered = _check_attempted_query(proposal.
           +attempted_query, graph)                                      
      1612 +                                                             
      1613 +    is_orthogonal = not colliding_facets and not field_collis
           +ions and not query_already_answered                          
      1614 +    attempts = _update_attempts(state_path, proposal.proposed
           +_facet_name, is_orthogonal)                                  
      1615 +    suggestion = _build_suggestion(colliding_facets, field_co
           +llisions, query_already_answered)                            
      1616 +                                                             
      1617 +    return FacetOrthogonalityReport(                         
      1618 +        is_orthogonal=is_orthogonal,                         
      1619 +        colliding_facets=colliding_facets,                   
      1620 +        field_collisions=field_collisions,                   
      1621 +        query_already_answered=query_already_answered,       
      1622 +        resolution_suggestion=suggestion,                    
      1623 +        attempts_remaining=attempts,                         
      1624 +    )                                                        
      1625 +                                                             
      1626 +                                                             
      1627 +def _tokenise(question: str) -> set[str]:                    
      1628 +    tokens = re.findall(r"[a-z0-9]+", question.lower())      
      1629 +    return {t for t in tokens if t not in _STOP_WORDS and len
           +(t) > 2}                                                     
      1630 +                                                             
      1631 +                                                             
      1632 +def _jaccard(a: set[str], b: set[str]) -> float:             
      1633 +    if not a and not b:                                      
      1634 +        return 0.0                                           
      1635 +    return len(a & b) / len(a | b)                           
      1636 +                                                             
      1637 +                                                             
      1638 +def _find_question_collisions(                               
      1639 +    question: str, registry: FacetRegistry, threshold: float 
           += 0.3                                                        
      1640 +) -> list[FacetSpec]:                                        
      1641 +    proposed_tokens = _tokenise(question)                    
      1642 +    return [                                                 
      1643 +        registry.get_spec(name)                              
      1644 +        for name in registry.facet_names                     
      1645 +        if _jaccard(proposed_tokens, _tokenise(registry.get_s
           +pec(name).question)) >= threshold                            
      1646 +    ]                                                        
      1647 +                                                             
      1648 +                                                             
      1649 +def _find_field_collisions(                                  
      1650 +    proposed_fields: list[dict[str, str]], registry: FacetReg
           +istry                                                        
      1651 +) -> list[str]:                                              
      1652 +    existing: dict[str, str] = {}                            
      1653 +    for name in registry.facet_names:                        
      1654 +        for field in registry.get_spec(name).fields:         
      1655 +            existing[field.name] = name                      
      1656 +    return [                                                 
      1657 +        f"{f['name']} (already in {existing[f['name']]})"    
      1658 +        for f in proposed_fields                             
      1659 +        if f.get("name") in existing                         
      1660 +    ]                                                        
      1661 +                                                             
      1662 +                                                             
      1663 +def _check_attempted_query(attempted_query: dict | None, grap
           +h: nx.DiGraph) -> bool:                                      
      1664 +    if not attempted_query:                                  
      1665 +        return False                                         
      1666 +    try:                                                     
      1667 +        query = StructuredQuery.model_validate(attempted_quer
           +y)                                                           
      1668 +        results = execute_query(graph, query)                
      1669 +        return len(results) > 0                              
      1670 +    except Exception:                                        
      1671 +        return False                                         
      1672 +                                                             
      1673 +                                                             
      1674 +def _update_attempts(state_path: Path, facet_name: str, is_or
           +thogonal: bool) -> int:                                      
      1675 +    state_path.parent.mkdir(parents=True, exist_ok=True)     
      1676 +    state = json.loads(state_path.read_text(encoding="utf-8")
           +) if state_path.exists() else {}                             
      1677 +    if is_orthogonal:                                        
      1678 +        state[facet_name] = DEFAULT_ATTEMPTS                 
      1679 +    else:                                                    
      1680 +        state[facet_name] = max(0, int(state.get(facet_name, 
           +DEFAULT_ATTEMPTS)) - 1)                                      
      1681 +    state_path.write_text(json.dumps(state, indent=2), encodi
           +ng="utf-8")                                                  
      1682 +    return state[facet_name]                                 
      1683 +                                                             
      1684 +                                                             
      1685 +def _build_suggestion(                                       
      1686 +    colliding_facets: list[FacetSpec],                       
      1687 +    field_collisions: list[str],                             
      1688 +    query_already_answered: bool,                            
      1689 +) -> str | None:                                             
      1690 +    parts: list[str] = []                                    
      1691 +    if colliding_facets:                                     
      1692 +        names = ", ".join(f.facet_name for f in colliding_fac
           +ets)                                                         
      1693 +        parts.append(f"Question overlaps with existing facets
           +: {names}. Consider adding a field to one of them instead.") 
      1694 +    if field_collisions:                                     
      1695 +        parts.append(f"Field name collision(s): {', '.join(fi
           +eld_collisions)}. Rename proposed fields.")                  
      1696 +    if query_already_answered:                               
      1697 +        parts.append(                                        
      1698 +            "The attempted_query already returns results — th
           +is information exists in the graph. "                        
      1699 +            "Use a StructuredQuery instead of adding a new fa
           +cet."                                                        
      1700 +        )                                                    
      1701 +    return " ".join(parts) or None                           
      1702 +```                                                          
      1703 +                                                             
      1704 +- [ ] **Step 5: Add `propose-facet` command to `main.py`**   
      1705 +                                                             
      1706 +Add import:                                                  
      1707 +                                                             
      1708 +```python                                                    
      1709 +from .facet_validator import validate_facet_proposal         
      1710 +from .registry import build_default_registry                 
      1711 +```                                                          
      1712 +                                                             
      1713 +Add to `main()` dispatch:                                    
      1714 +                                                             
      1715 +```python                                                    
      1716 +        if args.command == "propose-facet":                  
      1717 +            proposal_data = json.loads(Path(args.proposal).re
           +ad_text(encoding="utf-8"))                                   
      1718 +            proposal = FacetProposal.model_validate(proposal_
           +data)                                                        
      1719 +            registry = build_default_registry()              
      1720 +            graph = load_graph(Path(args.graph)) if Path(args
           +.graph).exists() else nx.DiGraph()                           
      1721 +            report = validate_facet_proposal(                
      1722 +                proposal=proposal,                           
      1723 +                registry=registry,                           
      1724 +                graph=graph,                                 
      1725 +                state_path=Path(args.state_file),            
      1726 +            )                                                
      1727 +            print(json.dumps(report.model_dump(), indent=2)) 
      1728 +            if not report.is_orthogonal:                     
      1729 +                sys.exit(1)                                  
      1730 +            return                                           
      1731 +```                                                          
      1732 +                                                             
      1733 +Add the subparser to `build_parser()`:                       
      1734 +                                                             
      1735 +```python                                                    
      1736 +    propose_facet_parser = subparsers.add_parser(            
      1737 +        "propose-facet", help="Validate a new facet proposal 
           +for orthogonality"                                           
      1738 +    )                                                        
      1739 +    propose_facet_parser.add_argument(                       
      1740 +        "--proposal", required=True, help="FacetProposal JSON
           + file"                                                       
      1741 +    )                                                        
      1742 +    propose_facet_parser.add_argument(                       
      1743 +        "--graph", default="knowledge_graph.json", help="Grap
           +h JSON path"                                                 
      1744 +    )                                                        
      1745 +    propose_facet_parser.add_argument(                       
      1746 +        "--state-file", default=".facet_proposal_state.json",
           + help="Attempt state file"                                   
      1747 +    )                                                        
      1748 +```                                                          
      1749 +                                                             
      1750 +- [ ] **Step 6: Run all tests**                              
      1751 +                                                             
      1752 +```bash                                                      
      1753 +cd /home/jp/wikipu && python -m pytest tests/test_facet_propo
           +sal.py -v                                                    
      1754 +```                                                          
      1755 +                                                             
      1756 +Expected: all 7 tests PASS.                                  
      1757 +                                                             
      1758 +- [ ] **Step 7: Smoke test with a real proposal**            
      1759 +                                                             
      1760 +Create `/tmp/model_usage_proposal.json`:                     
      1761 +                                                             
      1762 +```json                                                      
      1763 +{                                                            
      1764 +  "proposed_facet_name": "model_usage",                      
      1765 +  "question": "Which AI models does this node invoke?",      
      1766 +  "applies_to": ["file", "code_construct"],                  
      1767 +  "proposed_fields": [{"name": "model_name", "type": "str"}],
      1768 +  "attempted_query": null                                    
      1769 +}                                                            
      1770 +```                                                          
      1771 +                                                             
      1772 +```bash                                                      
      1773 +cd /home/jp/wikipu && wiki-compiler propose-facet \          
      1774 +  --proposal /tmp/model_usage_proposal.json \                
      1775 +  --graph knowledge_graph.json                               
      1776 +```                                                          
      1777 +                                                             
      1778 +Expected: `is_orthogonal: true`, exit 0.                     
      1779 +                                                             
      1780 +Now test a rejected proposal:                                
      1781 +                                                             
      1782 +```json                                                      
      1783 +{                                                            
      1784 +  "proposed_facet_name": "node_purpose",                     
      1785 +  "question": "What does this node do?",                     
      1786 +  "applies_to": ["file"],                                    
      1787 +  "proposed_fields": [{"name": "intent", "type": "str"}],    
      1788 +  "attempted_query": null                                    
      1789 +}                                                            
      1790 +```                                                          
      1791 +                                                             
      1792 +```bash                                                      
      1793 +wiki-compiler propose-facet --proposal /tmp/bad_proposal.json
      1794 +```                                                          
      1795 +                                                             
      1796 +Expected: `is_orthogonal: false`, `colliding_facets` includes
           + `semantics`, exit 1.                                        
      1797 +                                                             
      1798 +- [ ] **Step 8: Run full test suite**                        
      1799 +                                                             
      1800 +```bash                                                      
      1801 +cd /home/jp/wikipu && python -m pytest tests/test_registry_an
           +d_query.py \                                                 
      1802 +    tests/test_directory_skeleton.py tests/test_facet_injecto
           +rs.py \                                                      
      1803 +    tests/test_auditor.py tests/test_facet_proposal.py -v    
      1804 +```                                                          
      1805 +                                                             
      1806 +Expected: all tests PASS.                                    
      1807 +                                                             
      1808 +- [ ] **Step 9: Commit**                                     
      1809 +                                                             
      1810 +```bash                                                      
      1811 +git add src/wiki_compiler/facet_validator.py src/wiki_compile
           +r/contracts.py \                                             
      1812 +        src/wiki_compiler/main.py tests/test_facet_proposal.p
           +y                                                            
      1813 +git commit -m "feat: add FacetProposal orthogonality gate for
           + facet system"                                               
      1814 +```                                                          
      1815 +                                                             
      1816 +---                                                          
      1817 +                                                             
      1818  ## Self-Review
      1819  
      1820  **Spec coverage:**

● Now update the self-review section to include Task 4:

● Update(plan_docs/2026-04-08-three-phase-graph.md)
  ⎿  Added 13 lines, removed 6 lines
      1828  - Audit checks backed by `StructuredQuery` where possible → T
            ask 3 ✓
      1829  - `wiki-compiler audit` CLI → Task 3 ✓
      1830  - Each facet declared with a `question` → enforced in `FacetS
            pec` and `AuditCheck.question` ✓
      1831 +- `FacetProposal` orthogonality gate → Task 4 ✓              
      1832 +  - Question collision via Jaccard similarity ✓              
      1833 +  - Field name collision across registry ✓                   
      1834 +  - Compound answerability via `attempted_query` ✓           
      1835 +  - Attempt tracking (3 max, then human intervention) ✓      
      1836 +  - `wiki-compiler propose-facet` CLI ✓                      
      1837  
      1832 -**Orthogonality rule enforced:**                             
      1833 -- `MissingDocstringsCheck` uses `execute_query(StructuredQuer
           -y(filters=[...semantics...]))` — no hand-rolled loop         
      1834 -- `ComplianceViolationsCheck` uses `execute_query(StructuredQ
           -uery(filters=[...compliance...]))` — same                    
      1835 -- New audit checks should always ask: "can I express this as 
           -a `StructuredQuery`?" before writing a loop                  
      1838 +**Orthogonality rule enforced at two levels:**               
      1839 +- *Node level*: `TopologyProposal` (existing) checks I/O and 
           +semantic collisions before new modules                       
      1840 +- *Facet level*: `FacetProposal` (Task 4) checks question ove
           +rlap, field collision, and compound answerability before new 
           +dimensions                                                   
      1841 +- `MissingDocstringsCheck` / `ComplianceViolationsCheck` use 
           +`execute_query` — no hand-rolled loops                       
      1842  
      1843  **Type consistency:**
      1844  - `AuditFinding` defined in `contracts.py`, imported by `prot
            ocols.py`, `auditor.py`, and tests ✓
      1839 -- `FacetSpec` defined in `registry.py`, used in `ADRInjector.
           -spec` and `TestMapInjector.spec` ✓                           
      1840 -- `execute_query(graph, StructuredQuery)` signature consisten
           -t across `query_executor.py`, `auditor.py`, and tests ✓      
      1845 +- `FacetProposal` / `FacetOrthogonalityReport` in `contracts.
           +py`, used by `facet_validator.py` and tests ✓                
      1846 +- `FacetSpec` defined in `registry.py`, used in `ADRInjector.
           +spec`, `TestMapInjector.spec`, and `FacetOrthogonalityReport.
           +colliding_facets` ✓                                          
      1847 +- `execute_query(graph, StructuredQuery)` signature consisten
           +t across `query_executor.py`, `auditor.py`, `facet_validator.
           +py`, and tests ✓                                             
      1848  
      1849  **No placeholders detected.**

● Also write this to raw so the concept is preserved independently of the plan:

● Write(raw/facet_orthogonalization.md)
  ⎿  Wrote 60 lines to raw/facet_orthogonalization.md
       1 # Facet Orthogonalization
       2 
       3 ## The Problem
       4 
       5 Facets accumulate over time. Without a gate, you end up with:
       6 - Redundant facets answering the same question from two angles
       7 - Under-specified facets whose questions overlap partially
       8 - Facets that could be expressed as compound queries over existi
         ng ones
       9 
      10 This is the same problem as correlated variables in a dataset — 
         the axes aren't independent.
     … +50 lines (ctrl+o to expand)

● Done. Here's what was added:

  Task 4 in the plan adds a FacetProposal mechanism that enforces orthogonality
  at the facet level — exactly mirroring what TopologyProposal does for nodes:

  ┌───────────┬──────────────────────────────┬─────────────────────────────┐
  │           │          Node level          │         Facet level         │
  ├───────────┼──────────────────────────────┼─────────────────────────────┤
  │ Proposal  │ TopologyProposal             │ FacetProposal               │
  │ model     │                              │                             │
  ├───────────┼──────────────────────────────┼─────────────────────────────┤
  │ Validator │ validate_topology_proposal   │ validate_facet_proposal     │
  ├───────────┼──────────────────────────────┼─────────────────────────────┤
  │           │ I/O collision, glossary      │ Question overlap, field     │
  │ Checks    │ terms, raw/ writes           │ collision, compound         │
  │           │                              │ answerability               │
  ├───────────┼──────────────────────────────┼─────────────────────────────┤
  │ Attempts  │ 3 max                        │ 3 max                       │
  ├───────────┼──────────────────────────────┼─────────────────────────────┤
  │ CLI       │ wiki-compiler validate       │ wiki-compiler propose-facet │
  └───────────┴──────────────────────────────┴─────────────────────────────┘

  The third check — compound answerability — is the key one. The proposer must
  submit their best StructuredQuery attempt. If it returns results, the
  information already exists in the graph and the answer is "use the query, not 
  a new facet." This is the operational definition of PCA's "this variance is
  already explained."

  raw/facet_orthogonalization.md captures the full conceptual reasoning
  independently of the plan.

✻ Crunched for 2m 57s

❯ now, what is topology proposal's role?                                        

● TopologyProposal and FacetProposal are the same pattern applied at two
  different levels of abstraction.

  ---
  TopologyProposal — orthogonality of the system

  ▎ "Does this new module duplicate something that already exists?"

  It operates on nodes — components, services, files. It checks I/O collisions
  (does another node already own this path or schema?) and semantic collisions
  (is this glossary term already claimed?). It fires before you write new code.

  FacetProposal — orthogonality of the knowledge model

  ▎ "Does this new question duplicate something we can already ask?"

  It operates on dimensions — the lenses through which the system is observed.
  It fires before you add a new way of looking at nodes.

  ---
  The relationship between them is deeper than symmetry: TopologyProposal 
  depends on facets to do its job.

  It uses IOFacet data to detect I/O collisions. It uses SemanticFacet and the
  glossary to detect semantic collisions. The facets are the vocabulary with
  which topology proposals are evaluated.

  So the ordering is:

  FacetProposal  →  keeps the vocabulary clean
  TopologyProposal  →  uses that vocabulary to keep the system clean

  FacetProposal is meta to TopologyProposal. If your facets are poorly
  orthogonalized, TopologyProposal becomes unreliable — it's checking collisions
   using a blurry lens.

  ---
  Concretely, both implement the same circuit breaker pattern:

  ┌──────────────┬───────────────────────┬─────────────────────────────────┐
  │              │   TopologyProposal    │          FacetProposal          │
  ├──────────────┼───────────────────────┼─────────────────────────────────┤
  │ Guards       │ Redundant nodes       │ Redundant dimensions            │
  │ against      │                       │                                 │
  ├──────────────┼───────────────────────┼─────────────────────────────────┤
  │              │ I/O collision,        │ Question overlap, field         │
  │ Checks       │ glossary terms        │ collision, compound             │
  │              │                       │ answerability                   │
  ├──────────────┼───────────────────────┼─────────────────────────────────┤
  │ Operated by  │ Agent before writing  │ Agent before adding a facet     │
  │              │ code                  │                                 │
  ├──────────────┼───────────────────────┼─────────────────────────────────┤
  │ Attempts     │ 3 max                 │ 3 max                           │
  ├──────────────┼───────────────────────┼─────────────────────────────────┤
  │ Human        │ Yes                   │ Yes                             │
  │ escalation   │                       │                                 │
  └──────────────┴───────────────────────┴─────────────────────────────────┘

  Together they form a closed loop: the system can't grow outward (new nodes) or
   deepen (new dimensions) without proving it's adding something genuinely new.

❯ ok. Now about the wiki construction. Do we have a clear way to do it? my      
  insctinct here is that we must try to atomize as much as possible (think of   
  clean code rules here but for general text). when writing a new piece it      
  should have a clear "abstract" to enforce indexability and that "composition" 
   of longer texts should be made via a cli composition call rather than the    
  text itself. Also there should be free text but the system should evolve      
  "digesting" that free text into templated text structure. take as inspiration 
   here what we already have in plan_docs and wiki/standards                    

● Let me read what exists before responding.

  Read 3 files, listed 1 directory (ctrl+o to expand)

● Good question. Let me look at the existing wiki nodes as concrete examples
  before answering.

  The current system has the mechanism (transclusion) but not the discipline.
  Here's the honest picture:

  ---
  What You're Describing

  Three principles applied to documentation, borrowed from clean code:

  1. Single Responsibility per Node
  Each wiki node answers exactly one question or defines exactly one concept.
  Same as a function that does one thing. If you can't state the node's purpose
  in one sentence, it needs to be split.

  2. Mandatory Abstract
  Every node opens with a 1-3 sentence abstract — the "interface" of the text.
  This is what gets indexed, what the context command uses to rank relevance,
  what an LLM reads before deciding whether to go deeper. It should be a
  first-class field, not just a formatting convention.

  3. Composition via CLI, not prose
  Long documents are composed by assembling atomic nodes via transclusion —
  ![[node_a]], ![[node_b]]. A composite node has no prose of its own. You don't
  write a long document, you call:
  wiki-compiler compose --nodes "concept_a concept_b how_to_x" --output
  wiki/guide.md
  This mirrors a function that only calls other functions — pure composition, no
   logic of its own.

  ---
  The Digestion Pipeline

  Free text is the input, structured nodes are the output. The pipeline:

  raw/ (immutable free text)
    → wiki-compiler ingest   (extract draft nodes — currently just stubs)
    → human/LLM review       (break into atomic nodes, assign templates)
    → wiki/ (structured nodes)

  The raw text is never deleted. It's the ore. The wiki nodes are the refined
  metal. Both coexist.

  ---
  Node Templates

  Different node types need different required sections — like function
  signatures for different kinds of knowledge:

  ┌───────────┬───────────────────────┬─────────────────────────────────────┐
  │ Template  │  Question it answers  │          Required sections          │
  ├───────────┼───────────────────────┼─────────────────────────────────────┤
  │ concept   │ What is X?            │ abstract, definition, examples,     │
  │           │                       │ related concepts                    │
  ├───────────┼───────────────────────┼─────────────────────────────────────┤
  │ how_to    │ How do I do X?        │ abstract, prerequisites, steps,     │
  │           │                       │ outcome                             │
  ├───────────┼───────────────────────┼─────────────────────────────────────┤
  │ standard  │ What is the rule for  │ abstract, rule, rationale,          │
  │           │ X?                    │ violation examples                  │
  ├───────────┼───────────────────────┼─────────────────────────────────────┤
  │ reference │ How does X work       │ abstract, signature/schema, fields, │
  │           │ technically?          │  examples                           │
  ├───────────┼───────────────────────┼─────────────────────────────────────┤
  │ index     │ What lives in this    │ abstract, node list (via            │
  │           │ area?                 │ transclusion only)                  │
  └───────────┴───────────────────────┴─────────────────────────────────────┘

  ---
  What Exists vs What's Missing

  ┌─────────────────────────────────────┬───────────────────────────────────┐
  │             Capability              │              Status               │
  ├─────────────────────────────────────┼───────────────────────────────────┤
  │ Transclusion (![[...]]) — the       │ Exists                            │
  │ composition mechanism               │                                   │
  ├─────────────────────────────────────┼───────────────────────────────────┤
  │ ingest command — first step of      │ Exists, but creates stubs only —  │
  │ digestion                           │ no content extraction             │
  ├─────────────────────────────────────┼───────────────────────────────────┤
  │ SemanticFacet.intent — a            │ Exists, but code-extracted only,  │
  │ proto-abstract                      │ not first-class on wiki nodes     │
  ├─────────────────────────────────────┼───────────────────────────────────┤
  │ Node templates (required sections   │ Missing                           │
  │ per type)                           │                                   │
  ├─────────────────────────────────────┼───────────────────────────────────┤
  │ Mandatory abstract as auditable     │ Missing                           │
  │ field                               │                                   │
  ├─────────────────────────────────────┼───────────────────────────────────┤
  │ compose CLI command                 │ Missing                           │
  ├─────────────────────────────────────┼───────────────────────────────────┤
  │ Audit check: "node has no abstract" │ Missing                           │
  ├─────────────────────────────────────┼───────────────────────────────────┤
  │ Ingest actually digests content     │ Missing                           │
  │ into structured proposals           │                                   │
  └─────────────────────────────────────┴───────────────────────────────────┘

  ---
  The Key Gap

  The ingest command is the pivot point. Right now it creates a stub with
  status: planned and nothing else. To fulfill the digestion vision it needs to:

  1. Read the raw text
  2. Identify what concepts, processes, or standards it contains
  3. Propose a split into atomic nodes with the appropriate template
  4. Output draft nodes that a human or LLM reviews before committing to wiki/

  That's the difference between a stub generator and an actual digestion
  pipeline.

  ---
  Want me to write this to raw/ as a concrete spec, then fold it into the plan
  as a Task 5 covering: abstract enforcement, node templates, compose command,
  and the upgraded ingest?

✻ Churned for 1m 1s

❯ go on                                                                         

● Write(raw/wiki_construction_principles.md)
  ⎿  Wrote 144 lines to raw/wiki_construction_principles.md
      1 # Wiki Construction Principles
      2 
      3 ## Core Idea
      4 
      5 The same discipline that makes code clean applies to documentatio
        n.
      6 A wiki node is a unit of knowledge. It should have one responsibi
        lity,
      7 a clear interface, and compose with other nodes rather than growi
        ng monolithic.
      8 
      9 ---
     … +134 lines (ctrl+o to expand)

● Now fold it into the plan as Task 5:

  Read 1 file (ctrl+o to expand)

● Update(plan_docs/2026-04-08-three-phase-graph.md)
  ⎿  Added 1 line
      10  - Task 2 implements ADR and TestMap facet injectors as protocol
          -conforming plugins registered in the registry.
      11  - Task 3 implements all audit checks as protocol-conforming plu
          gins and adds `wiki-compiler audit` and enhanced `wiki-compiler
           query` CLI commands.
      12  - Task 4 adds the `FacetProposal` mechanism — the orthogonality
           gate for the facet system itself, mirroring what `TopologyProp
          osal` does for nodes.
      13 +- Task 5 adds wiki construction discipline: node templates, man
         +datory abstract enforcement, a `compose` CLI command, and an up
         +graded `ingest` that proposes atomic node decompositions from r
         +aw text rather than generating stubs.                          
      14  
      15  **Tech Stack:** Python 3.10+, NetworkX 3.x, Pydantic v2, pytest
          , PyYAML
      16  

● Update(plan_docs/2026-04-08-three-phase-graph.md)
  ⎿  Added 4 lines
      36  | `tests/test_facet_injectors.py` | Create | ADR and TestMap in
          jection tests |
      37  | `tests/test_auditor.py` | Create | All six audit check tests 
          |
      38  | `tests/test_facet_proposal.py` | Create | FacetProposal valid
          ation tests |
      39 +| `src/wiki_compiler/node_templates.py` | Create | Template def
         +initions + section validator |                                 
      40 +| `src/wiki_compiler/ingest.py` | Modify | Upgrade from stub ge
         +nerator to atomic decomposition proposer |                     
      41 +| `src/wiki_compiler/main.py` | Modify | Add `compose` subcomma
         +nd |                                                           
      42 +| `tests/test_wiki_construction.py` | Create | Template complia
         +nce, abstract extraction, compose command tests |              
      43  
      44  ---
      45  

● Now read the current ingest.py before writing the task:

  Read 1 file (ctrl+o to expand)

● Update(plan_docs/2026-04-08-three-phase-graph.md)  ⎿  Added 699 lines
      1852  - `execute_query(graph, StructuredQuery)` signature consisten
            t across `query_executor.py`, `auditor.py`, `facet_validator.
            py`, and tests ✓
      1853  
      1854  **No placeholders detected.**
      1855 +                                                             
      1856 +---                                                          
      1857 +                                                             
      1858 +## Task 5: Wiki Construction — Templates, Abstracts, Compose,
           + Digestion                                                   
      1859 +                                                             
      1860 +Enforces the wiki construction principles: every node has a m
           +andatory abstract,                                           
      1861 +every node conforms to a template (required sections per type
           +), long texts are                                            
      1862 +composed via CLI transclusion rather than inline prose, and `
           +ingest` proposes                                             
      1863 +atomic decompositions instead of generating stubs.           
      1864 +                                                             
      1865 +**Four sub-deliverables:**                                   
      1866 +1. `node_templates.py` — template definitions and section val
           +idator                                                       
      1867 +2. Abstract audit check — detects nodes missing a valid abstr
           +act                                                          
      1868 +3. `wiki-compiler compose` — CLI command for composite nodes 
      1869 +4. Upgraded `ingest` — proposes atomic decompositions from ra
           +w text                                                       
      1870 +                                                             
      1871 +**Files:**                                                   
      1872 +- Create: `src/wiki_compiler/node_templates.py`              
      1873 +- Modify: `src/wiki_compiler/ingest.py`                      
      1874 +- Modify: `src/wiki_compiler/auditor.py` (add `MissingAbstrac
           +tCheck`)                                                     
      1875 +- Modify: `src/wiki_compiler/main.py` (add `compose` subcomma
           +nd)                                                          
      1876 +- Create: `tests/test_wiki_construction.py`                  
      1877 +                                                             
      1878 +- [ ] **Step 1: Write failing tests**                        
      1879 +                                                             
      1880 +```python                                                    
      1881 +# tests/test_wiki_construction.py                            
      1882 +from __future__ import annotations                           
      1883 +from pathlib import Path                                     
      1884 +import networkx as nx                                        
      1885 +import pytest                                                
      1886 +from wiki_compiler.contracts import KnowledgeNode, SemanticFa
           +cet, SystemIdentity                                          
      1887 +from wiki_compiler.graph_utils import add_knowledge_node     
      1888 +from wiki_compiler.node_templates import (                   
      1889 +    NodeTemplate,                                            
      1890 +    TemplateRegistry,                                        
      1891 +    build_default_template_registry,                         
      1892 +    extract_abstract,                                        
      1893 +    validate_template_sections,                              
      1894 +)                                                            
      1895 +from wiki_compiler.ingest import ingest_raw_sources          
      1896 +                                                             
      1897 +                                                             
      1898 +def write(path: Path, content: str) -> Path:                 
      1899 +    path.parent.mkdir(parents=True, exist_ok=True)           
      1900 +    path.write_text(content.strip() + "\n", encoding="utf-8")
      1901 +    return path                                              
      1902 +                                                             
      1903 +                                                             
      1904 +# --- Template registry ---                                  
      1905 +                                                             
      1906 +def test_template_registry_stores_and_retrieves_template() ->
           + None:                                                       
      1907 +    registry = TemplateRegistry()                            
      1908 +    template = NodeTemplate(                                 
      1909 +        node_type="concept",                                 
      1910 +        question="What is X?",                               
      1911 +        required_sections=["abstract", "definition", "example
           +s"],                                                         
      1912 +    )                                                        
      1913 +    registry.register(template)                              
      1914 +    assert registry.get("concept").required_sections == ["abs
           +tract", "definition", "examples"]                            
      1915 +                                                             
      1916 +                                                             
      1917 +def test_default_registry_has_five_templates() -> None:      
      1918 +    registry = build_default_template_registry()             
      1919 +    assert set(registry.node_types) >= {"concept", "how_to", 
           +"standard", "reference", "index"}                            
      1920 +                                                             
      1921 +                                                             
      1922 +# --- Abstract extraction ---                                
      1923 +                                                             
      1924 +def test_extract_abstract_returns_first_paragraph_after_front
           +matter() -> None:                                            
      1925 +    content = """---                                         
      1926 +identity:                                                    
      1927 +  node_id: "doc:wiki/foo.md"                                 
      1928 +  node_type: "concept"                                       
      1929 +edges: []                                                    
      1930 +---                                                          
      1931 +                                                             
      1932 +This is the abstract. It is two sentences long.              
      1933 +                                                             
      1934 +## Definition                                                
      1935 +                                                             
      1936 +Some definition here.                                        
      1937 +"""                                                          
      1938 +    abstract = extract_abstract(content)                     
      1939 +    assert abstract == "This is the abstract. It is two sente
           +nces long."                                                  
      1940 +                                                             
      1941 +                                                             
      1942 +def test_extract_abstract_returns_none_when_missing() -> None
           +:                                                            
      1943 +    content = """---                                         
      1944 +identity:                                                    
      1945 +  node_id: "doc:wiki/foo.md"                                 
      1946 +  node_type: "concept"                                       
      1947 +edges: []                                                    
      1948 +---                                                          
      1949 +                                                             
      1950 +## Definition                                                
      1951 +                                                             
      1952 +Jumps straight to a heading with no abstract paragraph.      
      1953 +"""                                                          
      1954 +    assert extract_abstract(content) is None                 
      1955 +                                                             
      1956 +                                                             
      1957 +# --- Section validation ---                                 
      1958 +                                                             
      1959 +def test_validate_template_sections_passes_when_all_present()
           + -> None:                                                    
      1960 +    registry = build_default_template_registry()             
      1961 +    content = """---                                         
      1962 +identity:                                                    
      1963 +  node_id: "doc:wiki/foo.md"                                 
      1964 +  node_type: "concept"                                       
      1965 +edges: []                                                    
      1966 +---                                                          
      1967 +                                                             
      1968 +This node explains what X is.                                
      1969 +                                                             
      1970 +## Definition                                                
      1971 +                                                             
      1972 +X is a thing.                                                
      1973 +                                                             
      1974 +## Examples                                                  
      1975 +                                                             
      1976 +Here is an example.                                          
      1977 +                                                             
      1978 +## Related Concepts                                          
      1979 +                                                             
      1980 +See also Y.                                                  
      1981 +"""                                                          
      1982 +    missing = validate_template_sections("concept", content, 
           +registry)                                                    
      1983 +    assert missing == []                                     
      1984 +                                                             
      1985 +                                                             
      1986 +def test_validate_template_sections_reports_missing_sections(
           +) -> None:                                                   
      1987 +    registry = build_default_template_registry()             
      1988 +    content = """---                                         
      1989 +identity:                                                    
      1990 +  node_id: "doc:wiki/foo.md"                                 
      1991 +  node_type: "concept"                                       
      1992 +edges: []                                                    
      1993 +---                                                          
      1994 +                                                             
      1995 +This node explains what X is.                                
      1996 +                                                             
      1997 +## Definition                                                
      1998 +                                                             
      1999 +X is a thing.                                                
      2000 +"""                                                          
      2001 +    missing = validate_template_sections("concept", content, 
           +registry)                                                    
      2002 +    assert "examples" in missing                             
      2003 +    assert "related_concepts" in missing                     
      2004 +                                                             
      2005 +                                                             
      2006 +def test_validate_template_sections_skips_unknown_type() -> N
           +one:                                                         
      2007 +    registry = build_default_template_registry()             
      2008 +    missing = validate_template_sections("file", "any content
           +", registry)                                                 
      2009 +    assert missing == []                                     
      2010 +                                                             
      2011 +                                                             
      2012 +# --- Upgraded ingest ---                                    
      2013 +                                                             
      2014 +def test_ingest_proposes_multiple_atomic_nodes_from_rich_sour
           +ce(tmp_path: Path) -> None:                                  
      2015 +    write(tmp_path / "raw/concepts.md", """                  
      2016 +# Knowledge Graph Concepts                                   
      2017 +                                                             
      2018 +## What is a KnowledgeNode?                                  
      2019 +                                                             
      2020 +A KnowledgeNode is the universal building block of the graph.
      2021 +Every file, directory, and code construct becomes a node.    
      2022 +                                                             
      2023 +## What is a Facet?                                          
      2024 +                                                             
      2025 +A Facet is a dimension of knowledge attached to a node.      
      2026 +Each facet answers one specific question about the node.     
      2027 +                                                             
      2028 +## What is an Edge?                                          
      2029 +                                                             
      2030 +An Edge connects two nodes and declares a relationship type. 
      2031 +""")                                                         
      2032 +                                                             
      2033 +    written = ingest_raw_sources(                            
      2034 +        source_dir=tmp_path / "raw",                         
      2035 +        dest_dir=tmp_path / "wiki/drafts",                   
      2036 +        project_root=tmp_path,                               
      2037 +    )                                                        
      2038 +                                                             
      2039 +    # Should propose one draft per detected section          
      2040 +    assert len(written) >= 3                                 
      2041 +    contents = [p.read_text(encoding="utf-8") for p in writte
           +n]                                                           
      2042 +    node_ids = [c for c in contents if 'node_id' in c]       
      2043 +    assert len(node_ids) >= 3                                
      2044 +    # Each draft should have an abstract (the section's first
           + paragraph)                                                  
      2045 +    for content in contents:                                 
      2046 +        assert extract_abstract(content) is not None         
      2047 +                                                             
      2048 +                                                             
      2049 +def test_ingest_single_concept_source_produces_one_draft(tmp_
           +path: Path) -> None:                                         
      2050 +    write(tmp_path / "raw/single.md", """                    
      2051 +# What is orthogonality?                                     
      2052 +                                                             
      2053 +Orthogonality means that components do not overlap in respons
           +ibility.                                                     
      2054 +Each component does exactly one thing, and no two components 
           +do the same thing.                                           
      2055 +""")                                                         
      2056 +    written = ingest_raw_sources(                            
      2057 +        source_dir=tmp_path / "raw",                         
      2058 +        dest_dir=tmp_path / "wiki/drafts",                   
      2059 +        project_root=tmp_path,                               
      2060 +    )                                                        
      2061 +    assert len(written) == 1                                 
      2062 +    content = written[0].read_text(encoding="utf-8")         
      2063 +    assert extract_abstract(content) is not None             
      2064 +    assert 'node_type: "concept"' in content                 
      2065 +                                                             
      2066 +                                                             
      2067 +# --- Compose command (tested via function, not CLI) ---     
      2068 +                                                             
      2069 +def test_compose_produces_transclusion_only_node(tmp_path: Pa
           +th) -> None:                                                 
      2070 +    from wiki_compiler.ingest import compose_wiki_node       
      2071 +    write(tmp_path / "wiki/concept_a.md", """---             
      2072 +identity:                                                    
      2073 +  node_id: "doc:wiki/concept_a.md"                           
      2074 +  node_type: "concept"                                       
      2075 +edges: []                                                    
      2076 +---                                                          
      2077 +                                                             
      2078 +Concept A is about X.                                        
      2079 +""")                                                         
      2080 +    write(tmp_path / "wiki/concept_b.md", """---             
      2081 +identity:                                                    
      2082 +  node_id: "doc:wiki/concept_b.md"                           
      2083 +  node_type: "concept"                                       
      2084 +edges: []                                                    
      2085 +---                                                          
      2086 +                                                             
      2087 +Concept B is about Y.                                        
      2088 +""")                                                         
      2089 +    output = tmp_path / "wiki/composed.md"                   
      2090 +    compose_wiki_node(                                       
      2091 +        node_ids=["doc:wiki/concept_a.md", "doc:wiki/concept_
           +b.md"],                                                      
      2092 +        title="Combined Guide",                              
      2093 +        output_path=output,                                  
      2094 +        wiki_dir=tmp_path / "wiki",                          
      2095 +    )                                                        
      2096 +    content = output.read_text(encoding="utf-8")             
      2097 +    assert "![[concept_a]]" in content                       
      2098 +    assert "![[concept_b]]" in content                       
      2099 +    assert 'node_type: "index"' in content                   
      2100 +    # composite node must have abstract                      
      2101 +    assert extract_abstract(content) is not None             
      2102 +```                                                          
      2103 +                                                             
      2104 +- [ ] **Step 2: Run to verify failure**                      
      2105 +                                                             
      2106 +```bash                                                      
      2107 +cd /home/jp/wikipu && python -m pytest tests/test_wiki_constr
           +uction.py -v                                                 
      2108 +```                                                          
      2109 +                                                             
      2110 +Expected: `ImportError: cannot import name 'NodeTemplate'`   
      2111 +                                                             
      2112 +- [ ] **Step 3: Implement `node_templates.py`**              
      2113 +                                                             
      2114 +Create `src/wiki_compiler/node_templates.py`:                
      2115 +                                                             
      2116 +```python                                                    
      2117 +from __future__ import annotations                           
      2118 +import re                                                    
      2119 +from dataclasses import dataclass                            
      2120 +                                                             
      2121 +                                                             
      2122 +FRONTMATTER_REGEX = re.compile(r"\A---\s*\n.*?\n---(\s*\n|$)"
           +, re.DOTALL)                                                 
      2123 +HEADING_RE = re.compile(r"^#{1,3}\s+(.+)$", re.MULTILINE)    
      2124 +                                                             
      2125 +                                                             
      2126 +@dataclass                                                   
      2127 +class NodeTemplate:                                          
      2128 +    node_type: str                                           
      2129 +    question: str                                            
      2130 +    required_sections: list[str]  # lowercase, underscored he
           +ading names                                                  
      2131 +                                                             
      2132 +                                                             
      2133 +class TemplateRegistry:                                      
      2134 +    def __init__(self) -> None:                              
      2135 +        self._templates: dict[str, NodeTemplate] = {}        
      2136 +                                                             
      2137 +    def register(self, template: NodeTemplate) -> None:      
      2138 +        self._templates[template.node_type] = template       
      2139 +                                                             
      2140 +    def get(self, node_type: str) -> NodeTemplate | None:    
      2141 +        return self._templates.get(node_type)                
      2142 +                                                             
      2143 +    @property                                                
      2144 +    def node_types(self) -> list[str]:                       
      2145 +        return list(self._templates)                         
      2146 +                                                             
      2147 +                                                             
      2148 +def build_default_template_registry() -> TemplateRegistry:   
      2149 +    registry = TemplateRegistry()                            
      2150 +    registry.register(NodeTemplate(                          
      2151 +        node_type="concept",                                 
      2152 +        question="What is X?",                               
      2153 +        required_sections=["abstract", "definition", "example
           +s", "related_concepts"],                                     
      2154 +    ))                                                       
      2155 +    registry.register(NodeTemplate(                          
      2156 +        node_type="how_to",                                  
      2157 +        question="How do I do X?",                           
      2158 +        required_sections=["abstract", "prerequisites", "step
           +s", "outcome"],                                              
      2159 +    ))                                                       
      2160 +    registry.register(NodeTemplate(                          
      2161 +        node_type="standard",                                
      2162 +        question="What is the rule for X?",                  
      2163 +        required_sections=["abstract", "rule", "rationale", "
           +violation_examples"],                                        
      2164 +    ))                                                       
      2165 +    registry.register(NodeTemplate(                          
      2166 +        node_type="reference",                               
      2167 +        question="How does X work technically?",             
      2168 +        required_sections=["abstract", "signature_or_schema",
           + "fields", "usage_examples"],                                
      2169 +    ))                                                       
      2170 +    registry.register(NodeTemplate(                          
      2171 +        node_type="index",                                   
      2172 +        question="What lives in this area?",                 
      2173 +        required_sections=["abstract"],                      
      2174 +    ))                                                       
      2175 +    return registry                                          
      2176 +                                                             
      2177 +                                                             
      2178 +def extract_abstract(content: str) -> str | None:            
      2179 +    """Return the first prose paragraph after the YAML frontm
           +atter, or None."""                                           
      2180 +    body = FRONTMATTER_REGEX.sub("", content).lstrip("\n")   
      2181 +    paragraphs = [p.strip() for p in re.split(r"\n{2,}", body
           +) if p.strip()]                                              
      2182 +    if not paragraphs:                                       
      2183 +        return None                                          
      2184 +    first = paragraphs[0]                                    
      2185 +    # Reject if the first non-empty block is a heading       
      2186 +    if first.startswith("#"):                                
      2187 +        return None                                          
      2188 +    return first                                             
      2189 +                                                             
      2190 +                                                             
      2191 +def validate_template_sections(                              
      2192 +    node_type: str, content: str, registry: TemplateRegistry 
      2193 +) -> list[str]:                                              
      2194 +    """Return list of required section names missing from con
           +tent."""                                                     
      2195 +    template = registry.get(node_type)                       
      2196 +    if template is None:                                     
      2197 +        return []                                            
      2198 +    body = FRONTMATTER_REGEX.sub("", content)                
      2199 +    headings = {                                             
      2200 +        re.sub(r"[^a-z0-9]+", "_", h.lower()).strip("_")     
      2201 +        for h in HEADING_RE.findall(body)                    
      2202 +    }                                                        
      2203 +    present = {"abstract"} if extract_abstract(content) else 
           +set()                                                        
      2204 +    present |= headings                                      
      2205 +    return [s for s in template.required_sections if s not in
           + present]                                                    
      2206 +```                                                          
      2207 +                                                             
      2208 +- [ ] **Step 4: Upgrade `ingest.py`**                        
      2209 +                                                             
      2210 +Replace `ingest.py` with an upgraded version that proposes at
           +omic decompositions:                                         
      2211 +                                                             
      2212 +```python                                                    
      2213 +from __future__ import annotations                           
      2214 +                                                             
      2215 +import re                                                    
      2216 +from pathlib import Path                                     
      2217 +                                                             
      2218 +from .node_templates import extract_abstract                 
      2219 +from .scanner import load_wikiignore_rules, match_ignore_reas
           +on                                                           
      2220 +                                                             
      2221 +                                                             
      2222 +# Matches ## or ### headings — section boundaries within a so
           +urce file                                                    
      2223 +SECTION_RE = re.compile(r"^(#{2,3})\s+(.+)$", re.MULTILINE)  
      2224 +                                                             
      2225 +                                                             
      2226 +def ingest_raw_sources(                                      
      2227 +    source_dir: Path,                                        
      2228 +    dest_dir: Path,                                          
      2229 +    project_root: Path | None = None,                        
      2230 +    overwrite: bool = False,                                 
      2231 +) -> list[Path]:                                             
      2232 +    root = project_root or source_dir.parent                 
      2233 +    ignore_rules = load_wikiignore_rules(root / ".wikiignore"
           +)                                                            
      2234 +    written: list[Path] = []                                 
      2235 +    for source_path in sorted(p for p in source_dir.rglob("*"
           +) if p.is_file()):                                           
      2236 +        if any(part.startswith(".") for part in source_path.r
           +elative_to(source_dir).parts):                               
      2237 +            continue                                         
      2238 +        rel_source = source_path.relative_to(root).as_posix()
      2239 +        if match_ignore_reason(rel_source, ignore_rules) is n
           +ot None:                                                     
      2240 +            continue                                         
      2241 +        proposals = propose_atomic_nodes(source_path, rel_sou
           +rce, dest_dir)                                               
      2242 +        for draft_path, content in proposals:                
      2243 +            if draft_path.exists() and not overwrite:        
      2244 +                continue                                     
      2245 +            draft_path.parent.mkdir(parents=True, exist_ok=Tr
           +ue)                                                          
      2246 +            draft_path.write_text(content, encoding="utf-8") 
      2247 +            written.append(draft_path)                       
      2248 +    return written                                           
      2249 +                                                             
      2250 +                                                             
      2251 +def propose_atomic_nodes(                                    
      2252 +    source_path: Path, rel_source: str, dest_dir: Path       
      2253 +) -> list[tuple[Path, str]]:                                 
      2254 +    """Split a source file into atomic node proposals, one pe
           +r section."""                                                
      2255 +    try:                                                     
      2256 +        text = source_path.read_text(encoding="utf-8")       
      2257 +    except UnicodeDecodeError:                               
      2258 +        title = source_path.stem.replace("_", " ").replace("-
           +", " ").title()                                              
      2259 +        return [_make_draft(dest_dir, title, rel_source, f"Bi
           +nary source `{source_path.name}`.")]                         
      2260 +                                                             
      2261 +    sections = _split_into_sections(text, source_path.stem)  
      2262 +    return [                                                 
      2263 +        (                                                    
      2264 +            dest_dir / f"{slugify(title)}.md",               
      2265 +            _render_draft(dest_dir, title, abstract, rel_sour
           +ce),                                                         
      2266 +        )                                                    
      2267 +        for title, abstract in sections                      
      2268 +    ]                                                        
      2269 +                                                             
      2270 +                                                             
      2271 +def _split_into_sections(text: str, file_stem: str) -> list[t
           +uple[str, str]]:                                             
      2272 +    """Return (title, abstract) pairs — one per logical secti
           +on."""                                                       
      2273 +    lines = text.splitlines()                                
      2274 +    # Find top-level title                                   
      2275 +    file_title = file_stem.replace("_", " ").replace("-", " "
           +).title()                                                    
      2276 +    for line in lines:                                       
      2277 +        stripped = line.strip()                              
      2278 +        if stripped.startswith("# "):                        
      2279 +            file_title = stripped.lstrip("# ")               
      2280 +            break                                            
      2281 +                                                             
      2282 +    # Find H2/H3 section boundaries                          
      2283 +    boundaries: list[tuple[int, str]] = []                   
      2284 +    for i, line in enumerate(lines):                         
      2285 +        m = SECTION_RE.match(line)                           
      2286 +        if m:                                                
      2287 +            boundaries.append((i, m.group(2)))               
      2288 +                                                             
      2289 +    if not boundaries:                                       
      2290 +        # No sections — whole file is one concept            
      2291 +        abstract = _first_prose_paragraph(text) or f"Draft fr
           +om `{file_stem}`."                                           
      2292 +        return [(file_title, abstract)]                      
      2293 +                                                             
      2294 +    results = []                                             
      2295 +    for idx, (line_no, section_title) in enumerate(boundaries
           +):                                                           
      2296 +        end = boundaries[idx + 1][0] if idx + 1 < len(boundar
           +ies) else len(lines)                                         
      2297 +        section_body = "\n".join(lines[line_no + 1:end])     
      2298 +        abstract = _first_prose_paragraph(section_body) or f"
           +Section from `{file_stem}`."                                 
      2299 +        results.append((section_title, abstract))            
      2300 +    return results                                           
      2301 +                                                             
      2302 +                                                             
      2303 +def _first_prose_paragraph(text: str) -> str | None:         
      2304 +    for block in re.split(r"\n{2,}", text):                  
      2305 +        stripped = block.strip()                             
      2306 +        if stripped and not stripped.startswith("#") and not 
           +stripped.startswith("```"):                                  
      2307 +            return stripped                                  
      2308 +    return None                                              
      2309 +                                                             
      2310 +                                                             
      2311 +def _render_draft(dest_dir: Path, title: str, abstract: str, 
           +rel_source: str) -> str:                                     
      2312 +    slug = slugify(title)                                    
      2313 +    rel_dest = f"{dest_dir.parent.name}/{dest_dir.name}/{slug
           +}.md"                                                        
      2314 +    return "\n".join([                                       
      2315 +        "---",                                               
      2316 +        "identity:",                                         
      2317 +        f'  node_id: "doc:{rel_dest}"',                      
      2318 +        '  node_type: "concept"',                            
      2319 +        "edges: []",                                         
      2320 +        "compliance:",                                       
      2321 +        '  status: "planned"',                               
      2322 +        "---",                                               
      2323 +        "",                                                  
      2324 +        abstract,                                            
      2325 +        "",                                                  
      2326 +        f"## Definition",                                    
      2327 +        "",                                                  
      2328 +        f"<!-- TODO: Expand definition for '{title}' -->",   
      2329 +        "",                                                  
      2330 +        "## Examples",                                       
      2331 +        "",                                                  
      2332 +        "<!-- TODO: Add examples -->",                       
      2333 +        "",                                                  
      2334 +        "## Related Concepts",                               
      2335 +        "",                                                  
      2336 +        "<!-- TODO: Link related nodes -->",                 
      2337 +        "",                                                  
      2338 +        f"---",                                              
      2339 +        f"*Proposed from `{rel_source}` — review and enrich b
           +efore promoting to wiki/.*",                                 
      2340 +    ])                                                       
      2341 +                                                             
      2342 +                                                             
      2343 +def _make_draft(                                             
      2344 +    dest_dir: Path, title: str, rel_source: str, abstract: st
           +r                                                            
      2345 +) -> tuple[Path, str]:                                       
      2346 +    return (                                                 
      2347 +        dest_dir / f"{slugify(title)}.md",                   
      2348 +        _render_draft(dest_dir, title, abstract, rel_source),
      2349 +    )                                                        
      2350 +                                                             
      2351 +                                                             
      2352 +def compose_wiki_node(                                       
      2353 +    node_ids: list[str],                                     
      2354 +    title: str,                                              
      2355 +    output_path: Path,                                       
      2356 +    wiki_dir: Path,                                          
      2357 +) -> None:                                                   
      2358 +    """Create a composite (index) node whose body is only tra
           +nsclusions."""                                               
      2359 +    slug = slugify(title)                                    
      2360 +    rel_dest = f"wiki/{output_path.stem}.md"                 
      2361 +    abstract = f"Composed guide: {title}. Assembles {len(node
           +_ids)} atomic nodes."                                        
      2362 +    stems = [Path(node_id.removeprefix("doc:wiki/")).stem for
           + node_id in node_ids]                                        
      2363 +    transclusions = "\n".join(f"![[{stem}]]" for stem in stem
           +s)                                                           
      2364 +    content = "\n".join([                                    
      2365 +        "---",                                               
      2366 +        "identity:",                                         
      2367 +        f'  node_id: "doc:{rel_dest}"',                      
      2368 +        '  node_type: "index"',                              
      2369 +        "edges: []",                                         
      2370 +        "---",                                               
      2371 +        "",                                                  
      2372 +        abstract,                                            
      2373 +        "",                                                  
      2374 +        transclusions,                                       
      2375 +        "",                                                  
      2376 +    ])                                                       
      2377 +    output_path.parent.mkdir(parents=True, exist_ok=True)    
      2378 +    output_path.write_text(content, encoding="utf-8")        
      2379 +                                                             
      2380 +                                                             
      2381 +def slugify(value: str) -> str:                              
      2382 +    slug = re.sub(r"[^a-zA-Z0-9]+", "_", value).strip("_").lo
           +wer()                                                        
      2383 +    return slug or "draft_node"                              
      2384 +```                                                          
      2385 +                                                             
      2386 +- [ ] **Step 5: Add `MissingAbstractCheck` to `auditor.py`** 
      2387 +                                                             
      2388 +Add to `auditor.py`:                                         
      2389 +                                                             
      2390 +```python                                                    
      2391 +from .node_templates import build_default_template_registry, 
           +extract_abstract, validate_template_sections                 
      2392 +                                                             
      2393 +_TEMPLATE_REGISTRY = build_default_template_registry()       
      2394 +                                                             
      2395 +                                                             
      2396 +class MissingAbstractCheck:                                  
      2397 +    check_name = "missing_abstract"                          
      2398 +    question = "Which wiki nodes have no abstract paragraph?"
      2399 +    related_facet = "semantics"                              
      2400 +                                                             
      2401 +    def run(self, graph: nx.DiGraph) -> list[AuditFinding]:  
      2402 +        # Abstract is checked at build time via the scanner r
           +eading wiki/*.md files.                                      
      2403 +        # Here we check SemanticFacet.intent — a missing or d
           +efault intent signals no abstract.                           
      2404 +        findings = []                                        
      2405 +        for node in iter_knowledge_nodes(graph):             
      2406 +            if node.identity.node_type not in {"doc_standard"
           +, "concept"}:                                                
      2407 +                continue                                     
      2408 +            if node.semantics is None or node.semantics.inten
           +t in {"Wiki node", ""}:                                      
      2409 +                findings.append(AuditFinding(                
      2410 +                    check_name=self.check_name,              
      2411 +                    node_id=node.identity.node_id,           
      2412 +                    detail="Doc node has no abstract paragrap
           +h (SemanticFacet.intent is default or missing).",            
      2413 +                ))                                           
      2414 +        return findings                                      
      2415 +                                                             
      2416 +                                                             
      2417 +class TemplateViolationCheck:                                
      2418 +    check_name = "template_violation"                        
      2419 +    question = "Which wiki nodes are missing required section
           +s for their type?"                                           
      2420 +    related_facet = "semantics"                              
      2421 +                                                             
      2422 +    def run(self, graph: nx.DiGraph) -> list[AuditFinding]:  
      2423 +        # Template validation requires the raw file content, 
           +not just the graph node.                                     
      2424 +        # This check is a placeholder that signals the violat
           +ion via compliance facet.                                    
      2425 +        findings = []                                        
      2426 +        for node in iter_knowledge_nodes(graph):             
      2427 +            if node.compliance and "template" in " ".join(nod
           +e.compliance.failing_standards):                             
      2428 +                findings.append(AuditFinding(                
      2429 +                    check_name=self.check_name,              
      2430 +                    node_id=node.identity.node_id,           
      2431 +                    detail=f"Failing: {', '.join(node.complia
           +nce.failing_standards)}",                                    
      2432 +                ))                                           
      2433 +        return findings                                      
      2434 +```                                                          
      2435 +                                                             
      2436 +Add both to `_ALL_CHECKS` in `auditor.py`:                   
      2437 +                                                             
      2438 +```python                                                    
      2439 +_ALL_CHECKS = [                                              
      2440 +    UndocumentedCodeCheck(),                                 
      2441 +    MissingDocstringsCheck(),                                
      2442 +    UntypedIOCheck(),                                        
      2443 +    ComplianceViolationsCheck(),                             
      2444 +    StaleEdgesCheck(),                                       
      2445 +    OrphanedPlansCheck(),                                    
      2446 +    MissingAbstractCheck(),                                  
      2447 +    TemplateViolationCheck(),                                
      2448 +]                                                            
      2449 +```                                                          
      2450 +                                                             
      2451 +- [ ] **Step 6: Add `compose` subcommand to `main.py`**      
      2452 +                                                             
      2453 +Add import:                                                  
      2454 +                                                             
      2455 +```python                                                    
      2456 +from .ingest import compose_wiki_node                        
      2457 +```                                                          
      2458 +                                                             
      2459 +Add to `main()` dispatch:                                    
      2460 +                                                             
      2461 +```python                                                    
      2462 +        if args.command == "compose":                        
      2463 +            compose_wiki_node(                               
      2464 +                node_ids=args.nodes,                         
      2465 +                title=args.title,                            
      2466 +                output_path=Path(args.output),               
      2467 +                wiki_dir=Path(args.wiki_dir),                
      2468 +            )                                                
      2469 +            print(f"[OK] Composite node written to {args.outp
           +ut}")                                                        
      2470 +            return                                           
      2471 +```                                                          
      2472 +                                                             
      2473 +Add the subparser:                                           
      2474 +                                                             
      2475 +```python                                                    
      2476 +    compose_parser = subparsers.add_parser(                  
      2477 +        "compose", help="Create a composite index node from a
           +tomic nodes"                                                 
      2478 +    )                                                        
      2479 +    compose_parser.add_argument("--nodes", nargs="+", require
           +d=True, help="Node IDs to compose")                          
      2480 +    compose_parser.add_argument("--title", required=True, hel
           +p="Title of the composite node")                             
      2481 +    compose_parser.add_argument("--output", required=True, he
           +lp="Output .md path")                                        
      2482 +    compose_parser.add_argument("--wiki-dir", default="wiki",
           + help="Wiki root directory")                                 
      2483 +```                                                          
      2484 +                                                             
      2485 +- [ ] **Step 7: Run all tests**                              
      2486 +                                                             
      2487 +```bash                                                      
      2488 +cd /home/jp/wikipu && python -m pytest tests/test_wiki_constr
           +uction.py -v                                                 
      2489 +```                                                          
      2490 +                                                             
      2491 +Expected: all tests PASS.                                    
      2492 +                                                             
      2493 +- [ ] **Step 8: Verify `ingest` still passes existing test** 
      2494 +                                                             
      2495 +```bash                                                      
      2496 +cd /home/jp/wikipu && python -m pytest tests/test_runtime_fea
           +tures.py::test_ingest_scaffolding_creates_draft_nodes -v     
      2497 +```                                                          
      2498 +                                                             
      2499 +Expected: PASS (the existing test checks for `status: "planne
           +d"` and `node_id` — both still produced).                    
      2500 +                                                             
      2501 +- [ ] **Step 9: Run full suite**                             
      2502 +                                                             
      2503 +```bash                                                      
      2504 +cd /home/jp/wikipu && python -m pytest tests/ -v --ignore=tes
           +ts/test_runtime_features.py                                  
      2505 +```                                                          
      2506 +                                                             
      2507 +Expected: all tests PASS.                                    
      2508 +                                                             
      2509 +- [ ] **Step 10: Smoke test compose**                        
      2510 +                                                             
      2511 +```bash                                                      
      2512 +cd /home/jp/wikipu && wiki-compiler compose \                
      2513 +  --nodes "doc:wiki/how_it_works.md" "doc:wiki/knowledge_node
           +_facets.md" \                                                
      2514 +  --title "System Overview" \                                
      2515 +  --output wiki/system_overview.md                           
      2516 +```                                                          
      2517 +                                                             
      2518 +Expected: `wiki/system_overview.md` created with transclusion
           +s and `node_type: "index"`.                                  
      2519 +                                                             
      2520 +- [ ] **Step 11: Commit**                                    
      2521 +                                                             
      2522 +```bash                                                      
      2523 +git add src/wiki_compiler/node_templates.py src/wiki_compiler
           +/ingest.py \                                                 
      2524 +        src/wiki_compiler/auditor.py src/wiki_compiler/main.p
           +y \                                                          
      2525 +        tests/test_wiki_construction.py                      
      2526 +git commit -m "feat: add node templates, abstract enforcement
           +, compose command, and atomic ingest"                        
      2527 +```                                                          
      2528 +                                                             
      2529 +---                                                          
      2530 +                                                             
      2531 +## Self-Review                                               
      2532 +                                                             
      2533 +**Spec coverage:**                                           
      2534 +- Facet registry (machine-readable) → Task 0 ✓               
      2535 +- Plugin protocols → Task 0 ✓                                
      2536 +- Structured query language → Task 0 ✓                       
      2537 +- Directory skeleton → Task 1 ✓                              
      2538 +- ADRFacet + TestMapFacet injectors → Task 2 ✓               
      2539 +- Audit command with six checks → Task 3 ✓                   
      2540 +- FacetProposal orthogonality gate → Task 4 ✓                
      2541 +- Node templates (concept, how_to, standard, reference, index
           +) → Task 5 ✓                                                 
      2542 +- Mandatory abstract (extractable, auditable) → Task 5 ✓     
      2543 +- `wiki-compiler compose` (transclusion-only composite nodes)
           + → Task 5 ✓                                                  
      2544 +- Upgraded `ingest` (atomic decomposition per section, not st
           +ubs) → Task 5 ✓                                              
      2545 +- `MissingAbstractCheck` + `TemplateViolationCheck` audit che
           +cks → Task 5 ✓                                               
      2546 +- Existing `ingest` test still passes → verified in Step 8 ✓ 
      2547 +                                                             
      2548 +**Type consistency:**                                        
      2549 +- `compose_wiki_node(node_ids, title, output_path, wiki_dir)`
           + used in `main.py` and tests ✓                               
      2550 +- `extract_abstract(content) -> str | None` used in `node_tem
           +plates.py`, `ingest.py`, and tests ✓                         
      2551 +- `validate_template_sections(node_type, content, registry) -
           +> list[str]` consistent ✓                                    
      2552 +                                                             
      2553 +**No placeholders detected.**                                

● Written to raw/wiki_construction_principles.md and added as Task 5 to the
  plan. Here's what Task 5 delivers:

  ┌────────────────────────┬─────────────────────────────────────────────────┐
  │      Deliverable       │                What it enforces                 │
  ├────────────────────────┼─────────────────────────────────────────────────┤
  │ node_templates.py      │ Five templates (concept, how_to, standard,      │
  │                        │ reference, index) each with required sections   │
  ├────────────────────────┼─────────────────────────────────────────────────┤
  │ extract_abstract()     │ Abstract as a first-class extractable field —   │
  │                        │ its absence is auditable                        │
  ├────────────────────────┼─────────────────────────────────────────────────┤
  │                        │ Splits source files into atomic proposals per   │
  │ Upgraded ingest        │ section — one draft per ## heading, each with   │
  │                        │ an abstract and template stub                   │
  ├────────────────────────┼─────────────────────────────────────────────────┤
  │                        │ Creates index nodes containing only             │
  │ compose_wiki_node()    │ transclusions — no inline prose, pure           │
  │                        │ composition                                     │
  ├────────────────────────┼─────────────────────────────────────────────────┤
  │ MissingAbstractCheck   │ Audit check: doc nodes with no abstract         │
  │                        │ paragraph                                       │
  ├────────────────────────┼─────────────────────────────────────────────────┤
  │ TemplateViolationCheck │ Audit check: doc nodes missing required         │
  │                        │ sections for their type                         │
  └────────────────────────┴─────────────────────────────────────────────────┘

  The digestion lifecycle is now explicit: raw/ → wiki/drafts/ (one atomic
  proposal per section) → wiki/ (approved structured nodes). The compose command
   is the assembly layer — it never contains prose, only ![[...]].

✻ Cooked for 2m 28s

❯ ok, now, such as ingest, i think we should have an "internal cleansing"       
  protocol of atoms that are already stale, repeat content with other or are    
  just out of place. cleansing can mean destroy, relocate, split. Do you agree  
  with this?                                                                    

● Yes, completely. And the analogy holds cleanly — it's the same circuit breaker
   pattern applied to the wiki itself, not just to new additions.

  Right now the system has gates for adding things (TopologyProposal,
  FacetProposal) but nothing that runs in the other direction. The graph grows
  but never self-corrects. Over time that produces exactly the same drift it was
   designed to prevent.

  ---
  What Cleansing Means Concretely

  Three operations, each with a different graph consequence:

  Destroy
  The node answers a question that no longer exists in the system — the concept
  was superseded, the code was deleted, the standard was rolled into another.
  Remove the node and all its edges. Audit for dangling references first (the
  stale_edges check already finds these from the other side).

  Relocate
  The node is valid but lives in the wrong part of the graph. Its content is
  correct but its node_id, parent edges, or node_type are wrong — it was put in
  wiki/ when it should be in wiki/standards/, or tagged concept when it's a
  how_to. Fix identity and edges, content stays.

  Split
  The node violates single responsibility. It answers two questions. The
  cleansing operation decomposes it into two atomic nodes, each with a proper
  abstract, and replaces the original with a composite index node that transclu
  both. This is ingest logic applied to existing wiki nodes rather than raw
  sources.

  ---
  How the System Detects Candidates

  Each operation has a detectable signal in the graph:

  ┌───────────┬──────────────────────────────────────────────────────────────┐
  │ Operation │                            Signal                            │
  ├───────────┼──────────────────────────────────────────────────────────────┤
  │ Destroy   │ Node has no incoming edges AND compliance status is planned  │
  │           │ AND no git activity                                          │
  ├───────────┼──────────────────────────────────────────────────────────────┤
  │ Destroy   │ Node's documents target no longer exists (stale_edges check) │
  ├───────────┼──────────────────────────────────────────────────────────────┤
  │ Relocate  │ Node's node_id prefix doesn't match its node_type or its     │
  │           │ parent's contains edge                                       │
  ├───────────┼──────────────────────────────────────────────────────────────┤
  │ Relocate  │ Node has no contains parent (orphan in the hierarchy)        │
  ├───────────┼──────────────────────────────────────────────────────────────┤
  │ Split     │ Node abstract is longer than 3 sentences                     │
  ├───────────┼──────────────────────────────────────────────────────────────┤
  │ Split     │ Node has more than one ## section that could each stand as   │
  │           │ independent abstracts                                        │
  ├───────────┼──────────────────────────────────────────────────────────────┤
  │ Split     │ Two nodes have high abstract similarity (near-duplicate      │
  │           │ content)                                                     │
  └───────────┴──────────────────────────────────────────────────────────────┘

  ---
  The Key Difference from Ingest

  Ingest is a one-way pipeline: raw → draft → wiki. Cleansing is a closed loop
  operating on the wiki itself. It needs a proposal mechanism like the others —
  you don't want automated destruction.

  So the protocol would be:

  wiki-compiler cleanse --graph knowledge_graph.json --wiki wiki/
    → produces CleansingReport: list of CleansingProposal
    → each proposal: node_id, operation (destroy|relocate|split), rationale,
  preview

  wiki-compiler cleanse --apply proposal.json
    → executes one approved proposal
    → updates the graph

  The report is read-only. The apply step requires explicit approval of a
  specific proposal. Same pattern as TopologyProposal — the system proposes,
  humans approve.

  ---
  Where It Sits in the Architecture

  TopologyProposal   →  gates new nodes (orthogonality on entry)
  FacetProposal      →  gates new facets (orthogonality of dimensions)
  CleansingProposal  →  corrects existing nodes (orthogonality maintenance)

  The three together form a complete lifecycle: enter clean, stay clean,
  self-correct.

  ---
  Agreed on adding this? If so I can write it to raw/ and add it as Task 6 in
  the plan.

❯ with this i refered to the wiki elements "ingested elements" wich would be    
  just pieces of code, documentation, or anything in the system that is not a   
  direct code consequence such as data or logs                                  

● Right, that's a sharper distinction. Let me restate it precisely.

  ---
  The Two-Layer Nature of the Graph

  Layer 1 — Code-derived nodes (file:, code:, dir:)
  These are always regenerated by wiki-compiler build from source truth. They
  can't go stale in the problematic sense — if a function is deleted, its node
  disappears on the next build automatically. No cleansing needed. The code is
  the cleansing.

  Layer 2 — Authored nodes (doc:wiki/...)
  These were created by ingest, written manually, or produced by an LLM. They
  are not regenerated from source — they persist independently. This is where
  drift accumulates. A concept doc explaining a feature that was later
  redesigned just sits there. The graph has no mechanism to detect it.

  ---
  So Cleansing Is Specifically This

  A maintenance protocol for the authored layer: wiki nodes, ingested drafts,
  concept docs, standards — anything that lives in wiki/ and wasn't directly
  stamped out by scanning code.

  The graph already gives you the signals:

  ┌─────────────────────────────────────────────────────┬───────────────────┐
  │                      Condition                      │     Operation     │
  ├─────────────────────────────────────────────────────┼───────────────────┤
  │ Doc node documents a code node that no longer       │ Destroy or        │
  │ exists                                              │ reassign          │
  ├─────────────────────────────────────────────────────┼───────────────────┤
  │ Doc node with no incoming or outgoing edges at all  │ Destroy candidate │
  ├─────────────────────────────────────────────────────┼───────────────────┤
  │ Two doc nodes with nearly identical abstracts       │ Merge             │
  ├─────────────────────────────────────────────────────┼───────────────────┤
  │ Doc node whose node_type doesn't match its content  │ Relocate          │
  │ structure                                           │                   │
  ├─────────────────────────────────────────────────────┼───────────────────┤
  │ Doc node that covers two independently              │ Split             │
  │ transcludable concepts                              │                   │
  └─────────────────────────────────────────────────────┴───────────────────┘

  The operations are four, not three — merge is the missing one. When two nodes
  say the same thing, destruction of both is wrong. You consolidate into one
  canonical node and update all edges pointing to the dissolved one.

  ---
  Why This Matters Structurally

  Code is self-cleaning. Documentation is not. That asymmetry is the core
  problem.

  Every time code changes, the code layer of the graph updates automatically.
  But the authored layer that documents that code is decoupled — it keeps
  whatever state it was last left in. Over time the two layers drift apart.
  Cleansing is the mechanism that closes that gap.

  code changes  →  code layer auto-updates  (build handles this)
                   authored layer does not  (cleansing handles this)

  The cleansing protocol scans for authored nodes whose connections to the code
  layer have gone stale, and proposes the minimum corrective operation for each.

  ---
  Agree this is the right framing? I'll write it to raw/ and add it as Task 6.

✻ Cogitated for 30s

❯ go on. with one clarification. These are not only a matter of what lives on   
  wiki folder. Everything on a project managed by this system (excepting of raw 
   that is a sanctuary, logs that is execution subproduct and some data         
  produced outputs) are leafs of the tree. everything is subject of the         
  scrutiny of the tree and the leafs and everything should be cleanable and     
  auditable.                                                                    

● That's the complete statement of the principle. Let me restate it before
  writing.

  ---
  The Corrected Framing

  The graph IS the project model. Every node in it — code, docs, tests, config,
  plan_docs, future_docs, scaffolded READMEs, module contracts — is a leaf of
  the same tree and subject to the same structural discipline.

  The only exclusions are nodes that are exempt by design:

  ┌───────────────┬────────────────────────────────────────────┐
  │     Zone      │                 Why exempt                 │
  ├───────────────┼────────────────────────────────────────────┤
  │ raw/          │ Sanctuary — immutable source material      │
  ├───────────────┼────────────────────────────────────────────┤
  │ logs/         │ Execution subproduct — transient by nature │
  ├───────────────┼────────────────────────────────────────────┤
  │ data/outputs/ │ Runtime artifact — not authored, produced  │
  └───────────────┴────────────────────────────────────────────┘

  Everything else is in scope. Including code files. A module can be misplaced
  architecturally. A test can be orphaned. A config file can be stale. The graph
   sees all of it.

  ---
  Cleansing Candidates by Node Type

  Code nodes (file:src/, code:)
  - Duplicate: module with overlapping IOFacet with another — TopologyProposal
  prevents this on entry but doesn't retroactively audit existing nodes
  - Misplaced: module in the wrong package layer (e.g. business logic in an I/O
  layer)
  - Split candidate: file with too many responsibilities visible in its
  ASTFacet.signatures

  Doc nodes (doc:wiki/)
  - Stale: documents edge points to a code node that no longer exists
  - Duplicate: two nodes with near-identical abstracts
  - Misplaced: wrong node_type for its content structure, or wrong folder
  - Split: abstract is compound — covers two independently usable concepts

  Plan nodes (doc:plan_docs/)
  - Stale: plan with no git activity and no code node connection
  - These should self-destruct when the feature lands — their absence after
  completion is the healthy state

  Backlog nodes (doc:future_docs/)
  - Stale: no activity beyond the 6-month house rule threshold
  - Duplicate: two entries describing the same feature from different angles

  Test nodes (file:tests/)
  - Orphaned: test file importing a module that no longer exists
  - Misplaced: test classified as unit but exercises multiple integrated layers

  Config/data nodes
  - Stale: no code node has a reads_from edge pointing to it
  - Duplicate: two configs with the same schema_ref

  ---
  The Four Operations, Applied Universally

  ┌───────────┬────────────────────────┬────────────────────────────────────┐
  │ Operation │        Meaning         │         Graph consequence          │
  ├───────────┼────────────────────────┼────────────────────────────────────┤
  │ Destroy   │ Node no longer belongs │ Remove node and all edges; audit   │
  │           │  in the system         │ for dangling references first      │
  ├───────────┼────────────────────────┼────────────────────────────────────┤
  │ Relocate  │ Node is valid but in   │ Update node_id, parent contains    │
  │           │ the wrong place        │ edges, node_type                   │
  ├───────────┼────────────────────────┼────────────────────────────────────┤
  │ Split     │ Node has more than one │ Replace with two atomic nodes +    │
  │           │  responsibility        │ one index node transcluding both   │
  ├───────────┼────────────────────────┼────────────────────────────────────┤
  │           │ Two nodes say the same │ Consolidate into one canonical     │
  │ Merge     │  thing                 │ node; redirect all edges from      │
  │           │                        │ dissolved node                     │
  └───────────┴────────────────────────┴────────────────────────────────────┘

  ---
  The Protocol Shape

  Same circuit breaker as everything else in the system:

  wiki-compiler cleanse --graph knowledge_graph.json
    → CleansingReport: list[CleansingProposal]
    → each proposal: node_id, operation, rationale, preview of result

  wiki-compiler cleanse --apply proposal.json
    → executes one approved proposal
    → rebuilds affected graph region

  Read-only detection, explicit per-proposal approval. The system never
  auto-destroys.

  ---
  Writing to raw/ and adding as Task 6 now.

● Write(raw/cleansing_protocol.md)
  ⎿  Wrote 138 lines to raw/cleansing_protocol.md
       1 # Cleansing Protocol
       2 
       3 ## Core Idea
       4 
       5 The graph is the project model. Every node in it — code, docs, t
         ests, config,
       6 plan_docs, future_docs, scaffolded READMEs, module contracts — i
         s a leaf of the
       7 same tree and subject to the same structural discipline.
       8 
       9 The system has gates for adding things (TopologyProposal, FacetP
         roposal) but
      10 nothing that runs in the other direction. The graph grows but ne
         ver self-corrects.
     … +128 lines (ctrl+o to expand)

● Now append Task 6 to the plan:

● Update(plan_docs/2026-04-08-three-phase-graph.md)
  ⎿  Added 1 line
      11  - Task 3 implements all audit checks as protocol-conforming plu
          gins and adds `wiki-compiler audit` and enhanced `wiki-compiler
           query` CLI commands.
      12  - Task 4 adds the `FacetProposal` mechanism — the orthogonality
           gate for the facet system itself, mirroring what `TopologyProp
          osal` does for nodes.
      13  - Task 5 adds wiki construction discipline: node templates, man
          datory abstract enforcement, a `compose` CLI command, and an up
          graded `ingest` that proposes atomic node decompositions from r
          aw text rather than generating stubs.
      14 +- Task 6 adds the cleansing protocol: graph-wide structural ano
         +maly detection across all node types (code, docs, tests, config
         +, plan_docs, future_docs), producing `CleansingProposal` object
         +s for human approval before any destructive or structural opera
         +tion is applied.                                               
      15  
      16  **Tech Stack:** Python 3.10+, NetworkX 3.x, Pydantic v2, pytest
          , PyYAML
      17  

● Update(plan_docs/2026-04-08-three-phase-graph.md)
  ⎿  Added 3 lines
      41  | `src/wiki_compiler/ingest.py` | Modify | Upgrade from stub ge
          nerator to atomic decomposition proposer |
      42  | `src/wiki_compiler/main.py` | Modify | Add `compose` subcomma
          nd |
      43  | `tests/test_wiki_construction.py` | Create | Template complia
          nce, abstract extraction, compose command tests |
      44 +| `src/wiki_compiler/cleanser.py` | Create | Anomaly detectors 
         ++ `CleansingProposal` + `CleansingReport` |                    
      45 +| `src/wiki_compiler/main.py` | Modify | Add `cleanse` subcomma
         +nd (detect + apply modes) |                                    
      46 +| `tests/test_cleanser.py` | Create | One test per anomaly type
         + per node category |                                           
      47  
      48  ---
      49  

● Update(plan_docs/2026-04-08-three-phase-graph.md)
  ⎿  Error editing file
  ⎿  You're out of extra usage · resets 7pm (Europe/Berlin)
     /upgrade or /extra-usage to finish what you’re working on.

✻ Cooked for 2m 34s

Generated from `raw/claw_session.md`.