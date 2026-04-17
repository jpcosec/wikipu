---
status: open
priority: p2
depends_on: [owl-roundtrip]
created: 2026-04-17
assigned_to: self
---

# OWL Deconstruction → Reconstruction Test

## Task

Verify that Markdown content can be extracted from OWL (round-trip validation).

## Test Commands

### 1. Get current file hash (baseline)
```bash
cd /home/jp/wikipu
md5sum wiki/reference/owl_integration.md
```

### 2. Build OWL
```bash
wiki-compiler build --owl 2>&1
```

### 3. Export from OWL to temp location
```bash
python -c "
from pathlib import Path
from wiki_compiler.owl_backend.import_export import export_ontology_to_markdown

exported = export_ontology_to_markdown(
    Path('/tmp/owl_export'),
    force=True
)
print(f'Exported {len(exported)} files')
"
```

### 4. Check exported content
```bash
ls /tmp/owl_export/wiki/reference/
head /tmp/owl_export/wiki/reference/owl_integration.md
```

### 5. Compare with original
```bash
diff wiki/reference/owl_integration.md /tmp/owl_export/wiki/reference/owl_integration.md
```

## Success Criteria

- Export completes without errors
- Exported file contains same node_id
- Frontmatter is preserved

## Proof of Success

Capture:
- Original file hash
- Export command output
- Diff output (should show minimal differences)
- Commit as proof

## Alternative Test (SPARQL → Markdown)

```bash
# Query node from OWL
wiki-compiler query --owl "
PREFIX wikipu: <https://wikipu.ai/ontology/>
SELECT ?id ?type ?status
WHERE {
  wikipu:Reference wikipu:node_id ?id .
  wikipu:Reference wikipu:node_type ?type .
  wikipu:Reference wikipu:status ?status .
}
"
```

Expected: Returns the reference node's metadata

## References

- `src/wiki_compiler/owl_backend/import_export.py`
- `wiki/reference/owl_integration.md`