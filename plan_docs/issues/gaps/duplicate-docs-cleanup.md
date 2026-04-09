# Missing Canonical House Rules Document

**Explanation:** ADR 002 declared `wiki/standards/00_house_rules.md` as the sole authority for ecosystem laws and directed that content from the Spanish draft (`raw/sourcetalk_artifacts/00_hausordnung_draft.md`) be incorporated into it. Neither the target file nor the source draft exist. The `agents/librarian/intro.md` also references `wiki/standards/00_house_rules.md` directly. Any agent following the librarian protocol will try to read a file that doesn't exist.

**Reference:** `wiki/adrs/002_documentation_consolidation.md`, `agents/librarian/intro.md`

**What to fix:** Create `wiki/standards/00_house_rules.md` as the canonical ecosystem law document — the identity rules for the autopoietic network. This is not just a human-readable reference; it must declare rules in a form that the autopoiesis loop coordinator can enforce.

**How to do it:**
1. Read `agents/librarian/intro.md`, `wiki/concepts/wiki_construction_principles.md`, `raw/cleansing_protocol.md`, and the four `raw/methodology_synthesis*.md` files to extract all identity rules.
2. Read `raw/autopoiesis_system.md` for the minimal energy rule and the three-layer framework.
3. Write `wiki/standards/00_house_rules.md` as a numbered law list, each law with: a machine-readable `rule_id`, a human-readable description, the layer it governs (identity / perception / response), and the enforcement mechanism (which process checks it).
4. Each law should declare its check: orthogonality is checked by `submit_topology_proposal`; zone separation is checked by `build_wiki()`; minimal energy is checked by the loop coordinator before any proposal.
5. Update `agents/librarian/intro.md` to point to the new file (it already does by convention).

**Depends on:** none (this is the precondition for all other autopoiesis work)
