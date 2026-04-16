---
identity:
  node_id: "doc:wiki/concepts/pirate_curriculum.md"
  node_type: "concept"
edges:
  - {target_id: "doc:wiki/system/pirate.md", relation_type: "implements"}
  - {target_id: "doc:wiki/reference/cli/query.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/cli/context.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/cli/status.md", relation_type: "contains"}
compliance:
  status: "implemented"
  failing_standards: []
---

# Pirate Curriculum

Pirate is a looted coding agent running on a small model (gemma 4b) with a fast but limited context window. This curriculum teaches Pirate to use wiki-compiler as a precision instrument for overcoming context limitations.

## Core Principle

**Precision over volume.** Instead of flooding context with entire files, use wiki-compiler to extract exactly what's needed. The graph is the router; CLI is the scalpel.

## Curriculum Structure

Tasks are ordered by complexity. Complete each task before proceeding.

### Task 1: Index Navigation
**Goal:** Verify Pirate can query the wiki structure without reading files.

**Assignment:**
```bash
wiki-compiler query --type get_descendants --node-id "doc:wiki/Index.md"
```

**Success criteria:**
- Output shows child nodes of Index
- No direct file reads of wiki/*.md files for navigation

**Common failure modes:**
- Reading Index.md directly instead of querying
- Not understanding the `doc:wiki/` node ID prefix

---

### Task 2: Finding a Concept
**Goal:** Find all nodes related to a specific concept.

**Assignment:**
Query for nodes related to "energy" — find the concept node and its neighbors.

**Commands to try:**
```bash
wiki-compiler query --search "energy"
wiki-compiler query --type get_node --node-id "doc:wiki/concepts/energy.md"
wiki-compiler query --type get_descendants --node-id "doc:wiki/concepts/energy.md"
```

**Success criteria:**
- Identifies the energy concept node
- Understands its relationships (edges)
- Can explain what energy measures in this system

**Common failure modes:**
- Not using `--search` for initial discovery
- Missing that edges define relationships, not content

---

### Task 3: Reading Efficiently
**Goal:** Only read files after confirming they exist via query.

**Assignment:**
Find and read the house_rules.md node.

**Steps:**
1. Query for the node
2. Confirm it exists via graph
3. Then read the file
4. Report what the read added beyond the graph query

**Success criteria:**
- Uses CLI query before read tool call
- Can articulate what graph returns vs. what file contains

**Common failure modes:**
- Jumping straight to read tool
- Not understanding the distinction between graph metadata and prose content

---

### Task 4: Context Extraction
**Goal:** Use `context` command to extract focused subgraphs.

**Assignment:**
Get the context around the "autopoiesis" concept — what it relates to and how.

**Command:**
```bash
wiki-compiler context --node-id "doc:wiki/concepts/autopoiesis.md" --depth 2
```

**Success criteria:**
- Understands context output format
- Can trace relationships without reading all connected files

---

### Task 5: Self-Assessment
**Goal:** Use status and energy commands to assess system state.

**Assignment:**
Run the following and interpret results:
```bash
wiki-compiler status
wiki-compiler energy
```

**Success criteria:**
- Reports any drift or untracked files
- Reports energy score and its meaning
- Identifies if system is in high-energy state

**Common failure modes:**
- Ignoring status/energy output
- Not understanding what a "dirty" tree means for a small model

---

### Task 6: Iterative Query Practice
**Goal:** Learn to iterate on queries when results are incomplete.

**Assignment:**
Find all nodes related to CLI commands. Start broad, narrow down.

**Exercise:**
1. First query: `--search "cli"`
2. Second query: `--type get_node` for specific nodes
3. Third query: `--type get_descendants` for command families
4. Report: Which CLI commands exist, categorized by function

**Success criteria:**
- Shows iterative query strategy
- Can narrow results progressively
- Articulates why multiple queries beat one broad read

---

### Task 7: Synthesize — Answer a Question
**Goal:** Use wiki-compiler to answer a question without flooding context.

**Assignment:**
Answer: "What are the six zones of this system?"

**Strategy:**
1. Query for zone-related nodes
2. Extract minimal necessary information
3. Answer concisely

**Success criteria:**
- Answer is correct and complete
- Used targeted queries, not full file reads
- Context usage is minimal

---

### Task 8: Diagnose a Failure
**Goal:** Use wiki-compiler to understand why something isn't working.

**Assignment:**
The system audit is failing. Use wiki-compiler to:
1. Find the audit command documentation
2. Query for any nodes tagged as compliance violations
3. Identify what needs fixing

**Success criteria:**
- Can navigate from symptom (failed audit) to cause (compliance nodes)
- Proposes specific fix without reading entire codebase

---

## Anti-Patterns to Avoid

1. **Guessing file paths** — Always query the graph first
2. **Reading before querying** — NAV-1: The graph is the routing system
3. **Dumping entire files** — Extract only what's needed
4. **Ignoring status/energy** — These are self-awareness tools
5. **Single-shot queries** — Iterate when results are incomplete

## Success Metric

Pirate has mastered wiki-compiler when:
- 90% of information retrieval uses CLI queries
- File reads are preceded by graph confirmation
- Status/energy are checked before major operations
- Context is used for understanding topology before reading content

## Related Concepts

- [[wiki/system/pirate.md]] — Pirate's identity
- [[wiki/reference/cli/query.md]] — Query command reference
- [[wiki/reference/cli/context.md]] — Context command reference
- [[wiki/concepts/topology.md]] — The invariant structure
- [[wiki/concepts/energy.md]] — The health metric
