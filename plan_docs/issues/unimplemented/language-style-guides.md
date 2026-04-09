# Per-Language Style Guides

**Explanation:** Layer 5 (Code Style) defines language-agnostic conventions, but each language has its own idioms, toolchain, and enforcement mechanisms. These need to be spelled out so that an agent working in TypeScript, Go, or any other language knows exactly what the CS rules mean in that context — without reading Python-specific tooling and having to mentally translate. The hausordnung already points to `wiki/standards/languages/` as the home for these guides.

**Reference:** `wiki/standards/00_house_rules.md` (Layer 5), `wiki/standards/languages/` (to be created)

**What to fix:** Create `wiki/standards/languages/` with one file per language the project uses. Each file is a translation of the Layer 5 CS rules into that language's idioms and tooling.

**Structure per language file:**
- Abstract: which CS rules this guide covers and the language's key constraints
- Rule-by-rule mapping: CS-1 through CS-9, stated in terms of the language's conventions
- Toolchain: linter, formatter, type checker, doc generator with recommended config
- Enforcement: which checks are automated vs. manual

**Languages to cover (at minimum):**
- `python.md` — extract and expand the Python section already in the hausordnung
- `typescript.md` — extract and expand the TypeScript section already in the hausordnung

**Add new language files** whenever a new language is introduced to the project. The language file is required before any code in that language is merged.

**Depends on:** none (pure documentation work, parallel with Phase 2)
