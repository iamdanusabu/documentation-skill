# Research

Your job, every time. The writer supplies a PDF; the facts come from here.

## 1. Connect

Tool names vary by install, so match on server and short name. If tools are deferred, load them in one ToolSearch call:

| Source | Search | Tools you need |
| --- | --- | --- |
| Brain | `brain` | `files_for`, `code_slice`, `resolve_symbol`, `ask_brain`, `custom_docs_search`, `custom_docs_article`, `support_search` |
| Jira, Confluence | `atlassian jira` | `searchJiraIssuesUsingJql`, `search`, `getConfluenceContent` |
| Drive | `drive` | `search_files`, `read_file_content` |
| Support desk (optional) | `desk` | `searchTickets`, `getTicketConversations` |

Atlassian site: `retailcloud.atlassian.net`. A tool that loads is connected; do not spend calls testing. Report one line ("Connected: Brain, Jira, Drive. Not available: support desk.") and carry on. If Brain, Jira or Drive is missing, add: "Turn it on under Settings > Connectors, or run /mcp to sign in."

## 2. Search terms

From the PDF: page and section names, every control label, any message text, and the words a developer would use for the feature. Exact labels in quotes are the best query you have.

## 3. Searches

Send A to D together in one turn. Then at most one follow-up round for fact-sheet gaps.

**A. Brain, the code behind the screen.** `files_for` with feature words plus likely camelCase field names, limit 8. `code_slice` the entity (its columns are the full field list, including what the recorder missed) and only the `validate...` methods of the service (the real rules and errors). For an option list, `resolve_symbol` the enum. `ask_brain` only for a behaviour question the code did not answer: one narrow "How does X work" per call, `depth: fast`; a reply that is a verdict means the question was too broad. Never put class, table or column names in the article.

**B. Jira.** One query on the labels: `text ~ "\"<Label one>\"" OR text ~ "\"<Label two>\"" ORDER BY updated DESC`, `maxResults` 8, fields `summary,status,description`. One on the feature: `text ~ "<product>" AND summary ~ "<feature word>"`, `maxResults` 15, fields `summary,status` only; then fetch descriptions for at most three with `key in (...)`. Use only Released items (Released, Completed, Done, PASS). Descriptions carry defaults, forbidden combinations, error wording and what a switch hides.

**C. Drive.** The pack lists the product's standing documents. Read one only if its modified date is later than the pack's snapshot date (check with a `search_files` on the title, `excludeContentSnippets: true`); otherwise the pack already holds it. For a topic the pack does not cover, one search `fullText contains '<product>' and fullText contains '<feature word>'` without snippets, and read the best one.

**D. Problems customers hit.** Brain `support_search` and `custom_docs_search`, limit 3, in plain words. If support history answers "access is none", note it and move on. Take the pattern of a problem, never the customer or their details.

**E. Other connectors.** One targeted search, only if a connector plainly holds material on this topic.

## 4. Done when

Every fact-sheet row has a source for: purpose, effect, default and limits, dependencies, failure, and released status. Remaining gaps become "general" or "omit". Do not start a third round.

## 5. Trust

| Question | Trust, in order |
| --- | --- |
| Labels, paths, order of steps | The PDF |
| Fields, required, validation | Code, then released Jira |
| Behaviour, defaults | Released Jira, current playbook, code |
| Available to customers | Jira status |
| What goes wrong | Support history, internal notes, validation in code |

Newer and released beats older. If you cannot tell, write only what both agree on.

## 6. Updating a pack

Change the fact in the relevant section of `knowledge.md`, tag it (none, `[VERIFY]`, `[INTERNAL]`), move released features out of the not-released section, update the snapshot date, and add any new standing document to `product.md`.
