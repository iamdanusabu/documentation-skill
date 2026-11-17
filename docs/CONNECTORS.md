# Connecting the sources

The skill does its own research. When you start it, it loads the connectors below, checks that each one answers, and tells you in one line which are connected. You do not need to open or prepare anything first, as long as the connectors are turned on for your Claude account.

## What it uses

| Connector | What the skill gets from it | If it is missing |
| --- | --- | --- |
| **Brain** | The fields, rules and validation behind each screen (from the code), internal solution notes, and past support tickets | Articles lose the detail the PDF does not show. The most important one to have. |
| **Atlassian** (Jira and Confluence) | Rules, defaults and error messages from released tickets, and whether a feature is released at all | The skill cannot tell released from unreleased, so it stays with the bundled knowledge |
| **Google Drive** | Each product's playbook and guides | Falls back to the knowledge snapshot bundled with the skill |
| Support desk (optional) | What customers actually ask about | Troubleshooting sections are thinner |

## Turn them on (once per person)

The connectors belong to your Claude account, not to this skill. Once they are on, they are available everywhere you use Claude, including Claude Code.

1. Open Claude (desktop app or claude.ai) signed in with your retailcloud account.
2. Go to **Settings > Connectors**.
3. Turn on **Brain**, **Atlassian**, and **Google Drive**. Sign in to each when asked.
4. In Claude Code, run `/mcp` to see the list. Anything marked as needing authentication can be signed in from there.

If you do not see Brain in the list, ask your workspace admin to add it for the organization.

## Access levels inside Brain

Brain's support-ticket history has its own permission. If the skill reports "support history: access is none", ask a Brain admin to grant your account anonymised access. Everything else in Brain works without it.

## Long-running Brain questions

Some Brain questions take minutes. If you see timeouts in Claude Code, raise the tool timeout in `~/.claude/settings.json` and restart:

```json
{
  "env": { "MCP_TOOL_TIMEOUT": "900000" }
}
```

## Checking by hand

Ask Claude: "Check which help article sources are connected." The skill runs its connection check and reports the result without writing anything.
