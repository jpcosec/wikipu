# Unimplemented Ideas from sourcetalk.txt

These concepts were discussed in the original conversation but never made it into the implementation.

---

## 1. CI/CD Enforcement

**Idea:** The wiki_compiler runs as a required check in every Pull Request. If the compliance score decreases, the merge is blocked.

**Current state:** Not implemented. No GitHub Actions workflow or pre-commit hook for this.

**Reference (sourcetalk.txt line ~792):**
> "Añadir una 'Ley de Bloqueo de Integración'. El wiki_compiler debe ejecutarse como un paso obligatorio en los Pull/Merge Requests (GitHub Actions, etc.). Si la 'puntuación de cumplimiento' (Compliance Score) del Grafo baja, el código no se puede fusionar a main."

---

## 2. Domain Glossary

**Idea:** A central file (e.g., `docs/domain_glossary.yaml`) that unifies synonyms across modules. If module A calls it "JobPosting" and module B calls it "Vacancy", the graph should know they're the same concept.

**Current state:** Not implemented. No glossary file exists. No "semantic collision" check in the validator.

**Reference (sourcetalk.txt line ~780):**
> "Todo sustantivo central debe estar registrado en `docs/domain_glossary.yaml`. El compilador fusionará conceptos semánticos basándose en este archivo."

---

## 3. Minimal Energy as Active Constraint

**Idea:** Before any TopologyProposal is generated, first query the graph to see if a simpler structure already exists that satisfies the requirement. If a match exists, extend it rather than creating new elements.

**Current state:** Not implemented as an automated check. The orthogonality validator checks for I/O collisions but doesn't query for existing nodes with overlapping intent.

**Reference (autopoiesis_system.md line ~196):**
> "Minimal energy is not just a design principle — it must be an active check in the coordinator. Before any proposal is generated, the coordinator asks: is there a simpler structure that satisfies this requirement? This is a graph query (find nodes with overlapping intent or IO), not a heuristic."

---

## 4. Librarian Agent Skill Prompt

**Idea:** A concrete system prompt that gives the LLM the "librarian" role — telling it how to navigate the graph, synthesize answers, and audit compliance.

**Current state:** Not captured as a standalone artifact. The skill concept exists but no dedicated prompt file.

**Reference (sourcetalk.txt lines ~541-558):**
```markdown
# 🧠 Skill: Arquitecto de Conocimiento (Librarian Agent)

Eres el Bibliotecario de este repositorio. No asumes cómo funciona el código; lees el **Grafo de Conocimiento (Knowledge Graph)** generado por nuestro `wiki_compiler`.

## 🎯 Tu Misión
1. **Navegar:** Cuando el usuario pregunte sobre arquitectura, flujo de datos o estado de un módulo, consulta los `KnowledgeNode` y sigue sus `edges` (aristas).
2. **Sintetizar:** Transforma el JSON puro de los nodos en explicaciones claras, diagramas en texto o advertencias de cumplimiento.
3. **Auditar:** Si notas que un nodo tiene un `ComplianceFacet` fallando (ej. falta de docstrings), recuérdaselo al usuario proactivamente al sugerir refactors.

## 🗂️ Cómo leer el Grafo
- Todo es un `KnowledgeNode` con una `SystemIdentity` única (ej. `file:src/ai/graph.py`).
- Las dependencias se expresan en la lista `edges`. Busca `relation_type="depends_on"` o `reads_from` para trazar el impacto de un cambio.
- Nunca inventes flujos de datos. Si un nodo no tiene un `IOFacet`, asume que no realiza I/O o que el parser aún no lo ha escaneado.

## 🛠️ Reglas de Interacción
- **Si el usuario quiere crear un feature nuevo:** Busca nodos con `status="planned"` en el `ComplianceFacet` para ver si ya hay trabajo previo, o pide crear la entrada en `future_docs/` primero.
- **Respuestas técnicas:** Basa tus respuestas en el `ASTFacet` (firmas reales) y `SemanticFacet` (intenciones documentadas).
```

---

## Summary

| Item | Proposed | Implemented |
|------|----------|------------|
| CI/CD enforcement | Yes | No |
| Domain glossary | Yes | No |
| Minimal energy check | Yes | No |
| Librarian prompt | Yes | No |