---
identity:
  node_id: "doc:wiki/adrs/004_workflow_as_ontology.md"
  node_type: "adr"
adr:
  decision_id: "004"
  status: "proposed"
  context_summary: "The portable workflow/ template and wikipu's own standards exist in parallel. This ADR proposes modeling the workflow as an OWL ontology integrated into wikipu's knowledge graph."
edges:
  - {target_id: "doc:wiki/adrs/Index.md", relation_type: "documents"}
  - {target_id: "doc:wiki/adrs/003_owl_integration.md", relation_type: "extends"}
compliance:
  status: "planned"
  failing_standards: []
---

# ADR 004: Workflow as OWL Ontology

Models workflow rules and task management as an OWL ontology, unifying wikipu's standards with the portable workflow template.

## Context

Wikipu has two parallel workflow representations:

1. **Generic portable workflow/** — `workflow/AGENTS.md`, `workflow/STANDARDS.md`, rituals, pills
2. **Wikipu-specific standards** — `wiki/standards/house_rules.md` with OP-1 through OP-10, WK rules

These overlap in concept (roles, tasks, rituals, commits) but use different vocabularies and structures.

Additionally, the task system uses ad-hoc file formats:
- Task files in `desk/tasks/*.md` with custom frontmatter
- Board.md as a hand-maintained table
- Pills as unbound context

OWL provides a formal way to unify these into a single coherent model.

## Decision

Model the workflow itself as an OWL ontology, integrated into wikipu's knowledge graph.

### Workflow Concepts as OWL Classes

```turtle
@prefix wikipu: <http://wikipu.org/ontology/> .
@prefix workflow: <http://wikipu.org/workflow/> .

# === ROLES ===
workflow:Agent           a  owl:Class .
workflow:Supervisor      a  owl:Class ; rdfs:subClassOf workflow:Agent .
workflow:Executor         a  owl:Class ; rdfs:subClassOf workflow:Agent .
workflow:ContextCompiler  a  owl:Class ; rdfs:subClassOf workflow:Agent .

# === TASKS ===
workflow:Task            a  owl:Class .
workflow:Pill            a  owl:Class .  # Context bound to task
workflow:Board           a  owl:Class .

# === WORKFLOW PROCESS ===
workflow:Ritual          a  owl:Class .
workflow:InitializationRitual  a  workflow:Ritual .
workflow:ExecutionRitual        a  workflow:Ritual .
workflow:PhaseCompletionRitual   a  workflow:Ritual .

# === ARTIFACTS ===
workflow:CommitTrigger   a  owl:Class .
workflow:TaskFile        a  owl:Class ; rdfs:subClassOf :Document .
workflow:BoardArtifact   a  owl:Class ; rdfs:subClassOf :Document .

# === PROPERTIES ===
workflow:performs       a  owl:ObjectProperty ;
                        rdfs:domain workflow:Agent ;
                        rdfs:range  workflow:Ritual .

workflow:hasTask         a  owl:ObjectProperty ;
                        rdfs:domain workflow:Board ;
                        rdfs:range  workflow:Task .

workflow:hasPill         a  owl:ObjectProperty ;
                        rdfs:domain workflow:Task ;
                        rdfs:range  workflow:Pill .

workflow:hasStatus       a  owl:DatatypeProperty ;
                        rdfs:domain workflow:Task ;
                        rdfs:range  xsd:string .

workflow:hasPriority     a  owl:DatatypeProperty ;
                        rdfs:domain workflow:Task ;
                        rdfs:range  xsd:string .

workflow:dependsOn       a  owl:ObjectProperty ;
                        rdfs:domain workflow:Task ;
                        rdfs:range  workflow:Task .

workflow:boundTo         a  owl:ObjectProperty ;
                        rdfs:domain workflow:Pill ;
                        rdfs:range  workflow:Task .
```

### Rituals as OWL Individuals

```turtle
# Initialization Ritual
workflow:InitializationRitual
    workflow:hasStep  "ATOMIZE" , "DEDUPE" , "CLEAN" , "AUDIT" , "RESOLVE" , "BIND" , "INDEX" , "EXECUTE" ;
    workflow:enforces  "Do not mark task complete without auditing git history" ;
    rdfs:comment       "Before starting any work: break into smallest child tasks, merge overlapping, delete legacy, verify existing work, resolve contradictions, link pills, regenerate board, begin execution." .

# Execution Ritual
workflow:ExecutionRitual
    workflow:hasStep  "INVALIDATE" , "VERIFY" , "TEST" , "CHANGELOG" , "AUDIT" , "DELETE" , "BOARD" , "COMMIT" ;
    workflow:enforces  "One task = one resolving commit" ;
    rdfs:comment       "When task is done: check tests, add tests, run tests, update changelog, audit pills, delete task, update board, commit." .
```

### Tasks as OWL Individuals

```turtle
# Example task individual
workflow:task_owl_phase1
    a                workflow:Task ;
    workflow:hasID   "owl-phase1" ;
    workflow:hasStatus  "open" ;
    workflow:hasPriority "p2" ;
    workflow:hasTitle  "Phase 1: Owlready2 Parallel Run" ;
    workflow:hasObjective  "Add owlready2 as dependency and export wiki graph to OWL" ;
    workflow:dependsOn  workflow:task_owl_phase2 , workflow:task_owl_phase3 , workflow:task_owl_phase4 ;
    workflow:boundTo  workflow:pill_owl_phase1_context ;
    workflow:locatedIn  "desk/tasks/owl-phase1-parallel-run.md" .

workflow:pill_owl_phase1_context
    a                workflow:Pill ;
    workflow:pillType "context" ;
    workflow:scope    "component" ;
    workflow:boundTo  workflow:task_owl_phase1 ;
    rdfs:comment      "OWL integration details from ADR-003" .
```

### Roles with Permissions

```turtle
# Supervisor permissions
workflow:Supervisor
    workflow:canPerform  "Atomize" , "Audit" , "Dispatch" , "Verify" ;
    workflow:canNotPerform "Implement" ;
    rdfs:comment          "Orchestrates atomization, audits pills, verifies commits, dispatches subagents. Never implements src/ code directly." .

# Executor permissions
workflow:Executor
    workflow:canPerform  "Fix" , "Test" , "Commit" ;
    workflow:canNotPerform "Atomize" , "Audit" ;
    rdfs:comment          "Solves exactly one task. Never touches desk/ except to link pills or update Board.md." .
```

### SWRL Rules for Workflow

```python
# Rule: A task must have all its dependencies completed before execution
task_can_execute(?t) :-
    workflow:Task(?t),
    workflow:dependsOn(?t, ?d),
    workflow:hasStatus(?d, "closed").

# Rule: Executor must not modify desk/ except for pills/board
executor_can_modify(?path) :-
    workflow:Executor(?agent),
    workflow:isModifying(?agent, ?path),
    (str(?path, "desk/pills/") ; str(?path, "desk/tasks/Board.md")).

# Rule: Every closed task must have a matching commit
task_has_commit(?t) :-
    workflow:Task(?t),
    workflow:hasStatus(?t, "closed"),
    workflow:hasCommit(?t, ?c).
```

## Integration with Wikipu

| Workflow Concept | Wikipu Mapping |
|-----------------|----------------|
| Agent | Person or Agent node |
| Task | Individual in quadstore |
| Pill | Context annotation on task |
| Board | SPARQL query result |
| Ritual | Named process annotation |
| Commit | Git history link |
| Standard | Rule in `wiki/standards/` |

### Existing Wikipu Nodes to Extend

- `wiki/standards/house_rules.md` → `workflow:Standard` class
- `wiki/adrs/*.md` → `workflow:DecisionRecord` class
- `wiki/concepts/facet.md` → `workflow:Facet` class

## Consequences

**Positive:**
- Single source of truth for workflow concepts
- Queries replace manual board maintenance
- SWRL rules enforce workflow constraints
- Roles and permissions formally defined
- Task dependencies trackable via SPARQL

**Negative:**
- More complex initial setup
- Board.md becomes a generated artifact, not hand-edited
- Learning curve for OWL workflow modeling

**Neutral:**
- Existing task files become export targets, not source
- Git history still the commit boundary

## Alternatives Considered

1. **Keep workflow/ separate** — Already exists, works. But duplicates wikipu's standards.

2. **Merge workflow/ into wiki/standards/** — Keeps flat file structure, loses OWL modeling benefits.

3. **Full workflow in OWL only** — No human-editable task files. Requires tooling investment first.

## Implementation Phases

**Phase A: Model Only**
- Create `workflow.owl` ontology file
- Model roles, rituals, tasks as classes
- Query board via SPARQL (parallel run)

**Phase B: Dual Source**
- Task files AND OWL individuals
- Sync between formats via SyncGate

**Phase C: OWL Primary**
- Task files become generated exports
- OWL quadstore is write-side
- Markdown files for human readability

## References

- `workflow/AGENTS.md` (current generic workflow)
- `wiki/standards/house_rules.md` (wikipu-specific standards)
- `wiki/adrs/003_owl_integration.md` (OWL integration foundation)
