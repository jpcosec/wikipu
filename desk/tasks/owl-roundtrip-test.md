---
status: open
priority: p2
depends_on: []
created: 2026-04-17
assigned_to: self
---

# OWL Build → Query Round-Trip Test

## Task

Verify that data extracted during `build --owl` can be queried via `query --owl` with exact match.

## Test Commands

### 1. Build with OWL
```bash
cd /home/jp/wikipu
wiki-compiler build --owl 2>&1
```

### 2. Query for known node
```bash
wiki-compiler query --owl "SELECT ?o WHERE { <https://wikipu.ai/ontology/energy> <https://wikipu.ai/ontology/node_id> ?o }"
```

**Expected output:**
```json
{
  "results": [["doc:wiki/concepts/energy.md"]],
  "count": 1
}
```

### 3. Query for references
```bash
wiki-compiler query --owl "SELECT ?ref WHERE { <https://wikipu.ai/ontology/energy> <https://wikipu.ai/ontology/references> ?ref }"
```

**Expected output:**
```json
{
  "results": [
    ["autopoiesis"],
    ["topology"]
  ],
  "count": 2
}
```

### 4. Query node type
```bash
wiki-compiler query --owl "SELECT ?t WHERE { <https://wikipu.ai/ontology/energy> <https://wikipu.ai/ontology/node_type> ?t }"
```

**Expected output:**
```json
{
  "results": [["concept"]],
  "count": 1
}
```

### 5. Count all triples
```bash
wiki-compiler query --owl "SELECT (COUNT(*) as ?c) WHERE { ?s ?p ?o }"
```

**Expected output:**
```json
{
  "results": [[868]],
  "count": 1
}
```

## Success Criteria

- All 5 queries return valid JSON
- Node IDs match expected values
- Triple count is consistent

## Troubleshooting

If queries fail, check:
- `wikipu.owl` exists: `ls -la wikipu.owl`
- Graph loaded: `python -c "from wiki_compiler.owl_backend import get_world; g = get_world(); print(len(g))"`

## Proof of Success

Capture outputs and commit as proof.