---
identity:
  node_id: "doc:wiki/standards/languages/typescript.md"
  node_type: "doc_standard"
edges:
  - {target_id: "doc:wiki/standards/house_rules.md", relation_type: "implements"}
compliance:
  status: "implemented"
  failing_standards: []
---

TypeScript-specific encoding of the CS-1 through CS-9 code style rules. All rules are supplemented by TypeScript idioms, interface/Zod-first data handling, and enforcement via `tsc --strict`, ESLint, and JSDoc tooling. These rules apply to every `.ts` and `.tsx` file in any project using this system.

---

## Rule Mapping

| CS Rule | TypeScript Equivalent | Example |
|---|---|---|
| **CS-1** — Module header comment | JSDoc `/** ... */` block at the top of every `.ts` file. One paragraph stating the module's role. | `/** Ingests raw ore files and emits structured WikiNode records. */` |
| **CS-2** — Public symbol doc comment | JSDoc on every exported `function`, `class`, `interface`, and `type`. At minimum: one-line summary + `@param` + `@returns` / `@throws` tags where applicable. | See snippet below |
| **CS-3** — Typed contracts at boundaries | All cross-module data uses `interface` or `type` declarations, or Zod schemas when runtime validation is needed. No `object`, no `any`, no plain `string` carrying structured data. `unknown` is the safe fallback, never `any`. | `function process(node: WikiNode): BuildResult` |
| **CS-4** — Semantic field descriptions | Every Zod field carries `.describe("...")`. Interface fields carry a JSDoc comment above the property. Descriptions must be sentences explaining intent. | `z.string().describe("Unique identifier in format 'doc:<relative_path>'.")` |
| **CS-5** — Domain error classes | Custom `Error` subclasses defined at the top of the relevant file or in a dedicated `errors.ts`. Never `throw new Error("some generic string")` for flow control. | `export class IngestError extends Error { constructor(path: string, cause?: Error) { super(\`Failed to ingest ${path}\`, { cause }); } }` |
| **CS-6** — No silent errors | Always log with context before re-throwing. Use `new DomainError("context", { cause: e })` (native ES2022 `cause` option). Never `catch (e) {}`. | `catch (e) { logger.error("Failed to parse", { path, error: e }); throw new IngestError(path, e as Error); }` |
| **CS-7** — Non-obvious comments only | Comments explain invariants (`// node_id must be unique within the graph`) or non-obvious decisions (`// zod parse here: upstream sends unvalidated JSON`). Never comments restating what the code obviously does. | — |
| **CS-8** — Changelog on every change | Update `changelog.md` in the same commit as any significant change to module behavior, exported API shape, or schema definition. | — |
| **CS-9** — Classes when functions grow complex | If a function accumulates more than ~4 local variables or requires multiple internal passes, extract it into a class with named stage methods. Private helpers go on the class, not as nested closures. | `class NodeBuilder { build(): WikiNode { ... } private validate(): void { ... } }` |

### CS-2 JSDoc snippet

```typescript
/**
 * Convert a raw document into a structured wiki node.
 *
 * @param source - Parsed raw document with frontmatter and body.
 * @param config - Build-time configuration controlling output paths and validation level.
 * @returns A fully validated WikiNode ready for graph insertion.
 * @throws {BuildError} If the source document is missing required frontmatter fields.
 */
export function buildNode(source: RawDoc, config: BuildConfig): WikiNode {
```

---

## Toolchain

### tsc (type checker)

```json
// tsconfig.json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "useUnknownInCatchVariables": true
  }
}
```

Run: `tsc --noEmit`

### ESLint

```json
// eslint.config.js (flat config)
import tseslint from "typescript-eslint";
import jsdoc from "eslint-plugin-jsdoc";

export default tseslint.config(
  tseslint.configs.strictTypeChecked,
  tseslint.configs.stylisticTypeChecked,
  {
    plugins: { jsdoc },
    rules: {
      // CS-2: JSDoc on all exports
      "jsdoc/require-jsdoc": ["error", {
        "publicOnly": true,
        "require": { "FunctionDeclaration": true, "ClassDeclaration": true, "MethodDefinition": true }
      }],
      "jsdoc/require-param": "error",
      "jsdoc/require-returns": "error",
      "jsdoc/require-description": "error",
      // CS-3: ban any and object
      "@typescript-eslint/no-explicit-any": "error",
      "@typescript-eslint/no-unsafe-assignment": "error",
      // CS-6: no empty catch
      "no-empty": ["error", { "allowEmptyCatch": false }],
      "@typescript-eslint/no-unused-vars": "error",
    }
  }
);
```

Run: `eslint src/`

### Zod (runtime contract enforcement)

Use Zod when a module receives data from an external boundary (API response, file parse, CLI args). Use plain `interface` for internal-only types that never cross a runtime boundary. All Zod schemas live in a `contracts.ts` file within their module.

```typescript
import { z } from "zod";

export const WikiNodeSchema = z.object({
  node_id: z.string().describe("Unique identifier in format 'doc:<relative_path>'."),
  node_type: z.string().describe("Artifact type: concept, doc_standard, adr, how_to, etc."),
  body: z.string().describe("Full markdown body of the node, excluding frontmatter."),
});

export type WikiNode = z.infer<typeof WikiNodeSchema>;
```

Parse at the boundary, propagate typed values internally:

```typescript
const node = WikiNodeSchema.parse(rawInput); // throws ZodError with field path if invalid
```

### Prettier (formatter)

```json
// .prettierrc
{
  "singleQuote": false,
  "trailingComma": "all",
  "printWidth": 100,
  "semi": true
}
```

Run: `prettier --check src/`

---

## Enforcement

| Check | Tool | Automated (CI) | Manual (Review) |
|---|---|---|---|
| CS-1 module header | ESLint `jsdoc/require-file-overview` | Yes — enable rule to require file-level JSDoc | — |
| CS-2 public JSDoc | ESLint `jsdoc/require-jsdoc`, `require-param`, `require-returns` | Yes — fails CI on missing JSDoc | Reviewer checks prose quality |
| CS-3 typed boundaries | `tsc --noEmit` with `noImplicitAny` + `@typescript-eslint/no-explicit-any` | Yes | Reviewer checks `contracts.ts` structure and Zod usage at boundaries |
| CS-4 field descriptions | ESLint `jsdoc/require-description` + Zod `.describe()` audit | Partial — JSDoc descriptions enforced; Zod `.describe()` requires custom lint rule | Reviewer checks semantic accuracy |
| CS-5 domain errors | Custom ESLint rule or `@typescript-eslint/no-throw-literal` | Partial — `no-throw-literal` prevents non-Error throws; custom rule for bare `new Error()` | Reviewer checks error class hierarchy |
| CS-6 no silent errors | ESLint `no-empty` (allowEmptyCatch: false) | Yes — empty catch blocks fail CI | Reviewer checks every catch for logging + re-throw |
| CS-7 comment discipline | — | Not automated | Reviewer flags narrative comments |
| CS-8 changelog | pre-commit hook | Planned — hook warns if `changelog.md` not modified in branch with `.ts` changes | Reviewer checks on PR |
| CS-9 function complexity | ESLint `complexity` rule | Yes — `"complexity": ["error", 10]` | Reviewer checks class extraction opportunities |
| No `any` | `@typescript-eslint/no-explicit-any` | Yes | — |
| Zod at external boundaries | — | Not automated | Reviewer checks entry points for `Schema.parse()` |

### Recommended CI snippet

```yaml
# .github/workflows/ci.yml (relevant steps)
- name: Type check
  run: tsc --noEmit

- name: Lint
  run: eslint src/

- name: Format check
  run: prettier --check src/

- name: Test
  run: vitest run
```

## Rule Schema

Each rule maps a CS rule ID to its TypeScript-specific equivalent, the enforcement tool, and whether it is automated in CI. The Rule Mapping table above is the authoritative schema for this document.

## Fields

| Field | Description |
|---|---|
| CS Rule | The code-style rule identifier from `house_rules.md` Layer 5 |
| TypeScript Equivalent | How the rule manifests in TypeScript idioms and tooling |
| Enforcement Tool | The tool (tsc, ESLint, Zod, Prettier) that checks this rule |

## Usage Examples

_See the Rule Mapping and Toolchain sections above for concrete enforcement configuration._
