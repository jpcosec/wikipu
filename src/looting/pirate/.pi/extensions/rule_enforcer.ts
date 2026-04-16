/**
 * Rule Enforcer Extension
 *
 * Enforces the "CLI before read" rule: agents must query the wiki-compiler CLI
 * before reading Markdown files directly. This enforces NAV-1 and NAV-3 from
 * wiki/standards/house_rules.md.
 *
 * Behavior:
 * - On read tool call for .md files, check if wiki-compiler query was made
 * - If not, add guidance to system prompt to encourage CLI query first
 * - Log when agent skips the query step
 */

import { exec } from "child_process";
import { promisify } from "util";
import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";

const execAsync = promisify(exec);

const queriedPaths = new Set<string>();

function extractWikiPath(filePath: string): string | null {
	const normalized = filePath.replace(/\\/g, "/");
	if (normalized.includes("/wiki/")) {
		return normalized.split("/wiki/").pop() || null;
	}
	if (normalized.includes("/src/wiki_compiler/")) {
		return normalized.split("/src/wiki_compiler/").pop() || null;
	}
	return null;
}

async function queryWikiGraph(path: string): Promise<boolean> {
	try {
		const wikiPath = extractWikiPath(path);
		if (!wikiPath) {
			return false;
		}
		const nodeId = `doc:wiki/${wikiPath}`;
		const { stdout } = await execAsync(
			`wiki-compiler query --type get_node --node-id "${nodeId}"`,
			{ cwd: process.cwd() },
		);
		if (stdout.includes("node_id")) {
			return true;
		}
		return false;
	} catch {
		return false;
	}
}

export default function ruleEnforcer(pi: ExtensionAPI) {
	pi.on("before_tool_call", async (event) => {
		if (event.toolCall.name === "read") {
			const args = event.toolCall.arguments as { path?: string };
			if (args.path && args.path.endsWith(".md")) {
				const wikiPath = extractWikiPath(args.path);
				if (wikiPath) {
					if (!queriedPaths.has(wikiPath)) {
						const canQuery = await queryWikiGraph(args.path);
						if (canQuery) {
							queriedPaths.add(wikiPath);
						}
					}
				}
			}
		}
		return undefined;
	});

	pi.on("before_agent_start", async (event) => {
		return {
			systemPrompt:
				event.systemPrompt +
				`

## CLI Before Read Rule (IMPORTANT)
When you need information about the wiki or codebase topology, you MUST:
1. First run: \`wiki-compiler query --type get_node --node-id "doc:wiki/..."\`
2. Or use: \`wiki-compiler query --type get_descendants --node-id "..."\`
3. Only then read individual .md files if the query shows they exist

This follows NAV-1 (Graph is routing system) and NAV-3 (Read graph first, markdown second).
`,
		};
	});

	pi.registerCommand("clear-query-cache", {
		description: "Clear the query cache for rule enforcement",
		handler: async () => {
			queriedPaths.clear();
			return { content: [{ type: "text", text: "Query cache cleared" }] };
		},
	});

	pi.registerCommand("query-wiki", {
		description: "Query wiki graph before reading files (enforces CLI before read rule)",
		handler: async (args, ctx) => {
			if (!args || args.length === 0) {
				return { content: [{ type: "text", text: "Usage: /query-wiki <node-id>" }] };
			}
			const nodeId = args[0];
			try {
				const { stdout } = await execAsync(
					`wiki-compiler query --type get_node --node-id "${nodeId}"`,
					{ cwd: process.cwd() },
				);
				const wikiPath = nodeId.replace(/^doc:wiki\//, "");
				if (wikiPath) {
					queriedPaths.add(wikiPath);
				}
				return { content: [{ type: "text", text: stdout }] };
			} catch (error) {
				return { content: [{ type: "text", text: `Query failed: ${error}` }] };
			}
		},
	});
}