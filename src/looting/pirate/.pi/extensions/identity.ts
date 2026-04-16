import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { readFileSync } from "node:fs";
import { join } from "node:path";

export default function identityExtension(pi: ExtensionAPI) {
	pi.on("before_agent_start", async (event, ctx) => {
		try {
			const whoAmIPath = join(ctx.cwd, "wiki/selfDocs/WhoAmI.md");
			const identity = readFileSync(whoAmIPath, "utf-8");

			return {
				systemPrompt: event.systemPrompt + "\n\n# Identity Override\n\n" + identity,
			};
		} catch {
			return {};
		}
	});
}