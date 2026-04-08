# Missing Canonical House Rules Document

**Explanation:** ADR 002 declared `wiki/standards/00_house_rules.md` as the sole authority for ecosystem laws and directed that content from the Spanish draft (`raw/sourcetalk_artifacts/00_hausordnung_draft.md`) be incorporated into it. Neither the target file nor the source draft exist. The `agents/librarian/intro.md` also references `wiki/standards/00_house_rules.md` directly. Any agent following the librarian protocol will try to read a file that doesn't exist.

**Reference:** `wiki/adrs/002_documentation_consolidation.md`, `agents/librarian/intro.md`

**What to fix:** Create `wiki/standards/00_house_rules.md` as the canonical ecosystem law document, incorporating relevant rules from `raw/cleansing_protocol.md`, `wiki/concepts/wiki_construction_principles.md`, and the librarian protocol in `agents/librarian/intro.md`.

**How to do it:**
1. Read `agents/librarian/intro.md` to extract the rules it references.
2. Read `wiki/concepts/wiki_construction_principles.md` and `raw/cleansing_protocol.md` for additional laws.
3. Write `wiki/standards/00_house_rules.md` as a consolidated, numbered law list.
4. Update `agents/librarian/intro.md` to point to the new file (it already does by convention).

**Depends on:** none
