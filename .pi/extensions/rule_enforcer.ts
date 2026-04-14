import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { appendFileSync } from "node:fs";
import { join } from "node:path";
import { isToolCallEventType } from "@mariozechner/pi-coding-agent";

export default function (pi: ExtensionAPI) {
  let cliQueried = false;

  pi.on("agent_start", () => {
    cliQueried = false;
  });

  pi.on("tool_call", async (event, ctx) => {
    if (isToolCallEventType("bash", event)) {
      const cmd = event.input.command;
      if (cmd.includes("wiki-compiler query")) {
        cliQueried = true;
      }
      if (!cliQueried && (cmd.startsWith("cat ") || cmd.startsWith("grep ") || cmd.startsWith("ls "))) {
        logViolation(ctx.cwd, "Used bash inspection before wiki-compiler query");
        ctx.ui.notify("Rule Violation: Used bash inspection before wiki-compiler query", "error");
      }
    }

    if (isToolCallEventType("read", event)) {
      if (!cliQueried) {
        logViolation(ctx.cwd, `Used read tool on ${event.input.path} before wiki-compiler query`);
        ctx.ui.notify("Rule Violation: Used read tool before wiki-compiler query", "error");
      }
    }
  });

  function logViolation(cwd: string, detail: string) {
    try {
      const logPath = join(cwd, "desk", "agent_violations.log");
      const timestamp = new Date().toISOString();
      appendFileSync(logPath, `[${timestamp}] ${detail}\n`, "utf8");
    } catch (e) {
      // Ignore
    }
  }
}
