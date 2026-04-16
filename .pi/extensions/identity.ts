import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { readFileSync } from "node:fs";
import { join } from "node:path";

export default function (pi: ExtensionAPI) {
  pi.on("before_agent_start", async (event, ctx) => {
    try {
      // Read the true identity from the autopoietic knowledge base
      const whoAmIPath = join(ctx.cwd, "wiki/selfDocs/WhoAmI.md");
      const identity = readFileSync(whoAmIPath, "utf-8");

      // Replace or append to the system prompt
      return {
        systemPrompt: event.systemPrompt + "\n\n# Identity Override\n\n" + identity,
      };
    } catch (e) {
      // If the file doesn't exist or can't be read, just proceed normally
      return {};
    }
  });
}
