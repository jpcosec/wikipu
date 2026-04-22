---
status: open
priority: p3
depends_on: []
created: 2026-04-22
assigned_to: self
---

# Migrate Existing Wiki Docs to SLDB Format

Migrate existing wiki documents to use SLDB StructuredNLDoc models for consistency and validation.

## Why

- Enforce required sections at creation time, not audit time
- All new docs created via `wiki-compiler scaffold` use SLDB
- Existing docs should also benefit from structure validation

## Approach

1. Run `sldb validate` on all existing wiki docs to find non-compliant ones
2. Update models if needed (currently list fields render as `[]`)
3. Batch migrate or create migration script
4. Verify audit still passes after migration

## Node Types to Migrate

- `concept` → ConceptDoc
- `how_to` → HowToDoc
- `doc_standard` → DocStandardDoc
- `reference` → ReferenceDoc
- `index` → IndexDoc
- `adr` → ADRDoc
- `selfDoc` → SelfDocDoc

## Verification

```bash
# Validate all docs
for f in wiki/**/*.md; do
  sldb validate wiki_compiler.contracts.wiki_nodes:$(basename $f .md)Doc --input $f --pythonpath src
done

# Should pass without errors
```
