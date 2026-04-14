---
identity:
  node_id: doc:wiki/drafts/1_ci_cd_enforcement.md
  node_type: concept
edges:
- target_id: raw:raw/unimplemented_from_sourcetalk.md
  relation_type: documents
compliance:
  status: implemented
  failing_standards: []
source:
  source_path: raw/unimplemented_from_sourcetalk.md
  source_hash: 1a7f8c9ba485c0342c7bddb0d133479345f1edd3e7047103e0544db195914f61
  compiled_at: '2026-04-14T16:50:28.666169'
  compiled_from: wiki-compiler
---

**Idea:** The wiki_compiler runs as a required check in every Pull Request. If the compliance score decreases, the merge is blocked.

## Definition

**Idea:** The wiki_compiler runs as a required check in every Pull Request.

## Examples

- Idea:
- Current state:
- Reference (sourcetalk.txt line ~792):

## Related Concepts

- [[Index]]
- [[core_philosophy]]

## Details

**Idea:** The wiki_compiler runs as a required check in every Pull Request. If the compliance score decreases, the merge is blocked.

**Current state:** Not implemented. No GitHub Actions workflow or pre-commit hook for this.

**Reference (sourcetalk.txt line ~792):**
> "Añadir una 'Ley de Bloqueo de Integración'. El wiki_compiler debe ejecutarse como un paso obligatorio en los Pull/Merge Requests (GitHub Actions, etc.). Si la 'puntuación de cumplimiento' (Compliance Score) del Grafo baja, el código no se puede fusionar a main."

---

Generated from `raw/unimplemented_from_sourcetalk.md`.
