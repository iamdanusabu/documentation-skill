# Maintaining the skill

This repository is the master copy. Each writer's installed skill is a copy of it. Changes made in an installed copy reach nobody else until they are committed here.

## Who changes what

| File | Change it when | Who decides |
| --- | --- | --- |
| `references/voice-and-tone.md` | The team agrees a wording rule | The documentation owner. A change here changes every future article, so review it as a team. |
| `references/fanvista-knowledge.md` | A workflow PDF, a release or the live console confirms or changes a fact | Any writer, with the source noted in the commit message |
| `references/article-catalog.md` | An article is added, renamed or retired | Any writer |
| `references/document360.md` | Document360 formatting is confirmed or changes | Any writer |
| `references/research.md` | A source document is replaced or moved, a connector changes, or a better search is found | Any writer |
| `examples/` | A published article is a better model than a current example | The documentation owner |
| `SKILL.md` | The workflow itself changes | The documentation owner |

## Bringing back a change Claude made

During a session Claude may update its own copy of `fanvista-knowledge.md` (for example, after a PDF confirms a screen label) and will tell you it did.

1. Find the installed copy: `~/.claude/skills/fanvista-help-articles/references/fanvista-knowledge.md`.
2. Copy the changed lines into `skills/fanvista-help-articles/references/fanvista-knowledge.md` in this repository.
3. Update the snapshot date at the top of the file.
4. Follow the release steps below.

## Rules for the knowledge file

- Record what is **released** to customers. Unreleased work goes in section 18 or stays out.
- Tag every statement correctly: no tag (confirmed), `[VERIFY]` (unconfirmed), `[INTERNAL]` (true, never published).
- When a `[VERIFY]` is settled, remove the tag and the matching line in section 17.
- No credentials, no customer names, no Jira keys.

## Releasing a change

1. Edit the files under `skills/fanvista-help-articles/`.
2. Run `bash build.sh` to rebuild `dist/fanvista-help-articles.skill`.
3. Bump `version` in `.claude-plugin/plugin.json` and add a line to `CHANGELOG.md`.
4. Commit and push.
5. Tell the writers. Plugin users run `/plugin marketplace update retailcloud-docs`; copy-install users pull and rerun the installer; app users upload the new `.skill` file.

## Testing a change

Give Claude a workflow PDF you have used before and compare the new article with the old one. For a voice change, also ask it to rewrite one of the files in `examples/` and check that only the intended wording moved.
