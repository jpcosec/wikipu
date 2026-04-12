# Index: drafts

- **doc:wiki/drafts/unimplemented_ideas_from_sourcetalk_txt.md** — Unimplemented Ideas from sourcetalk.txt: These concepts were discussed in the original conversation but never made it into the implementation.
- **doc:wiki/drafts/1_ci_cd_enforcement.md** — 1. CI/CD Enforcement: **Idea:** The wiki_compiler runs as a required check in every Pull Request. If the compliance score decreases, the merge is blocked.
- **doc:wiki/drafts/2_domain_glossary.md** — 2. Domain Glossary: **Idea:** A central file (e.g., `docs/domain_glossary.yaml`) that unifies synonyms across modules. If module A calls it "JobPosting" and module B calls it "Vacancy", the graph should know they're the same concept.
- **doc:wiki/drafts/3_minimal_energy_as_active_constraint.md** — 3. Minimal Energy as Active Constraint: **Idea:** Before any TopologyProposal is generated, first query the graph to see if a simpler structure already exists that satisfies the requirement. If a match exists, extend it rather than creating new elements.
- **doc:wiki/drafts/4_librarian_agent_skill_prompt.md** — 4. Librarian Agent Skill Prompt: **Idea:** A concrete system prompt that gives the LLM the "librarian" role — telling it how to navigate the graph, synthesize answers, and audit compliance.
- **doc:wiki/drafts/tu_misi_n.md** — 🎯 Tu Misión: 1. **Navegar:** Cuando el usuario pregunte sobre arquitectura, flujo de datos o estado de un módulo, consulta los `KnowledgeNode` y sigue sus `edges` (aristas).
- **doc:wiki/drafts/c_mo_leer_el_grafo.md** — 🗂️ Cómo leer el Grafo: - Todo es un `KnowledgeNode` con una `SystemIdentity` única (ej. `file:src/ai/graph.py`).
- **doc:wiki/drafts/reglas_de_interacci_n.md** — 🛠️ Reglas de Interacción: - **Si el usuario quiere crear un feature nuevo:** Busca nodos con `status="planned"` en el `ComplianceFacet` para ver si ya hay trabajo previo, o pide crear la entrada en `future_docs/` primero.
- **doc:wiki/drafts/summary.md** — Summary: | Item | Proposed | Implemented |
