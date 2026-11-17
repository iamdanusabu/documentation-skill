# Research protocol

The writer gives you a PDF and perhaps a line of context. Everything else in the article comes from here. Run this every time; do not wait to be asked, and do not ask the writer for facts a connected source can supply.

## 1. Connect: find and load the sources

The sources are MCP connectors. Their tool names differ between installs (`mcp__claude_ai_Brain__ask_brain`, `mcp__plugin_..._atlassian__...`, or plain names in the Claude apps), so match on the server and the short tool name, not the full name.

If the session defers tools (Claude Code shows them by name only), load them first with ToolSearch, all in one go:

| Source | ToolSearch keywords | Short tool names you need |
| --- | --- | --- |
| Brain | `brain` | `files_for`, `code_slice`, `resolve_symbol`, `ask_brain`, `custom_docs_search`, `custom_docs_article`, `support_search`, `table_schema` |
| Jira and Confluence | `jira`, `confluence`, `atlassian` | `searchJiraIssuesUsingJql`, `getJiraIssue`, `search`, `getConfluenceContent`, `getAccessibleAtlassianResources` |
| Google Drive | `drive` | `search_files`, `read_file_content` |
| Support desk | `desk`, `ticket` | `searchTickets`, `getTicket`, `getTicketConversations` |
| Meetings | `meeting` | `list_meetings`, `get_meeting` |

Then make one cheap call to each to confirm it answers (Brain `brain_status` is large, so prefer a small `custom_docs_search`; Atlassian `getAccessibleAtlassianResources`; Drive a one-result `search_files`).

Tell the writer the result in one line, for example: "Connected: Brain, Jira, Confluence, Drive. Not available: support desk." Then carry on. Do not stop for a missing source. If a core source (Brain, Jira, Drive) is missing, add one sentence on how to connect it:

- In the Claude apps and Claude Code signed in with the retailcloud account: **Settings > Connectors**, turn the connector on, and sign in when asked. Connectors turned on there are available in Claude Code automatically.
- If a connector shows "needs authentication", the writer signs in once; in Claude Code, `/mcp` lists the servers and starts the sign-in.

Jira and Confluence calls need the site: `retailcloud.atlassian.net`.

## 2. Turn the PDF into search terms

From the flow you set out in SKILL.md step 2, list:

- the **page and section names** on screen ("Setup", "Login Options", "Delivery Method"),
- every **control label** ("Enable Fan Guest Login", "Configure Pickup Time"),
- any **message text** shown,
- the **feature words** a developer or product manager would use for it ("branding", "pickup time", "subdomain", "suite management").

These are your queries. Exact on-screen labels in quotes are the most productive search you can run.

## 3. Run the searches

Send each group together. Read the results, then follow up on anything that names a rule, a default, a limit or an error.

### A. Brain: the code behind the screen

This is how you learn what the recorder did not capture: the fields above and below the screenshot, which are required, and the real validation rules.

1. `files_for` with the feature words plus likely field names in camelCase ("FanVista branding title1 primaryColor subdomain"). Look for an entity, model or service file in the results.
2. `code_slice` on that file (entities are short; services, read the `validate...` methods). The entity's columns are the full field list. The validation methods are the real rules and error conditions.
3. For an option list (triggers, statuses, types), `resolve_symbol` on the enum name, then `code_slice`.
4. `ask_brain` for behaviour questions, one narrow question per call, phrased as "How does X work" or "What happens when Y". Broad or list-style questions are misrouted to a design review; if the reply is a verdict rather than an answer, narrow the question and ask again. Use `depth: fast` first.

Take behaviour from the code. Never copy class, table or column names into the article.

### B. Jira: the rules and the release status

1. `searchJiraIssuesUsingJql` with the labels: `text ~ "\"Enable Fan Guest Login\"" OR text ~ "\"Configure Pickup Time\"" ORDER BY updated DESC`, fields `summary, status, description`, about 10 results.
2. A feature search: `text ~ "fanvista" AND (summary ~ "<feature word>" OR text ~ "<feature word>") ORDER BY updated DESC`, fields `summary, status` first; then fetch the descriptions of the ones that matter with `key in (...)`.
3. Planning items for the product: `project = CP AND summary ~ "fanvista" ORDER BY updated DESC`.

Use only **Released** items (also written RELEASED, Completed, Done, PASS on a test execution). Open, Discovery, Dev, Awaiting QA or UAT, On Hold, Partially Released and Discarded mean the feature does not exist for the reader. Ticket descriptions usually hold the exact rules: defaults, combinations that are not allowed, the wording of error messages, what a switch hides. Take those. Leave behind keys, customer names and investigation notes.

### C. Google Drive: the playbook and guides

1. `search_files` with `fullText contains 'FanVista' and fullText contains '<feature word>'`, without snippets, then read the best two or three.
2. Always check the standing documents below for the topic; reread any whose modified date is later than the snapshot date at the top of `fanvista-knowledge.md`.

| Document | ID | Use it for |
| --- | --- | --- |
| Fanvista Playbook v2 | `1LiXEBJVt3HSG0kHdFGhwmu2xnvbySUo-R-qBs2HvSGk` | Main reference for setup and operations |
| FanGuest quick start | `1eqZOJ5IgQSU92Pcmpldcvt169QFAHUQXHpcvC8Zydqs` | Shortest correct setup path for fan events |
| Suite retail quick start | `1Q-qG0qV0ZrLt57J4cV78Zxj7xIdSm-Xhdyy3ijdmGzY` | Suite setup, per-suite stores, suite order flow |
| FanVista_Setup_Wizard_PRD | `1fohnXDSeGfYjN2m0g7m3a_BxJ6g5UjyK3CaAWt7DVTY` | Step dependencies, field detail, test checklists. A spec; the released product may differ |
| Fanvista feature documentation (2025) | `1x4yRPohPEs_ab5lP97YtUFvngjUaNEhWeYzGTS7Lm30` | Fan-side behaviour |
| Open Items for FanVista | `1iRwpA8I0Ay--WBChcbXuIz4NRfHYjvjFbd7GfMtWYqE` | What is not built. Use only to keep unreleased features out |
| Print Job Setup for Fanvista | `1RcVhtURcSjmsNLCDv5TwPY1ktrZTEwI79DU0i1Kw2cA` | Internal printer procedure. Contains credentials. Never publish |

Meeting notes and recordings in Drive are internal discussion. Use them only to understand intent, never as a statement of what shipped.

### D. Problems customers actually hit

For the "If something goes wrong" and "Common questions" sections:

1. Brain `support_search` with the topic in plain words. If it answers "access is none", say so in your notes and move on.
2. Brain `custom_docs_search` for internal solution notes and workarounds.
3. The support desk connector, if present: search tickets by the feature words and read what was asked and how it ended.
4. Confluence `search` for a QA note or knowledge-base page on the feature.

Support tickets and desk conversations contain customers' names and data. Take the pattern ("fans did not receive the code"), never the customer, the wording or the details.

### E. Anything else connected

Look at what other connectors the session has. If one plainly holds material on this topic (design files, a wiki, a chat workspace), run one targeted search there. Do not trawl sources that have nothing to do with the product.

## 4. Know when you are done

For **every setting, option and step** in the flow, you can state:

- what it is for,
- what it changes for the fan or for staff,
- its default and its limits (sizes, counts, required or optional),
- what depends on it elsewhere,
- what goes wrong and what the reader sees when it does,
- that it is released.

If a point is still open after the code, Jira and Drive, it goes on your list of things to word generally (SKILL.md step 6), not into another round of searching.

## 5. Weigh what you found

| Question | Trust, in order |
| --- | --- |
| What the screen looks like, labels, order of steps | The PDF |
| What fields exist, what is required, validation | Code via Brain, then released Jira |
| How it behaves, defaults, what a switch hides | Released Jira, current playbook, code |
| Whether customers can use it yet | Jira status |
| What goes wrong | Support history, internal solution notes, then validation rules in code |
| Older documents | Only where nothing newer speaks |

When two sources disagree and the newer one is released, follow the newer one. When you cannot tell, write only what both agree on.

## 6. Report it

In your chat notes, list each source with what it gave you and each source you could not reach. One line each. This is how the writer knows how far to trust the article.

## 7. Update the knowledge file

When a search confirms or changes something in `fanvista-knowledge.md`:

1. Change the fact in the relevant section; keep it short and customer-oriented.
2. Tag it correctly: no tag (confirmed), `[VERIFY]` (unconfirmed, internal to this file only), `[INTERNAL]` (true, never published).
3. If a feature moved from unreleased to released, remove it from section 18.
4. Update the snapshot date at the top.
5. Add any new standing document to the table in section C above.
