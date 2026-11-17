# Publishing to Document360

Each article is delivered in three forms.

| File | Use |
| --- | --- |
| `<slug>.docx` | **Publish from this.** Word file with all images embedded. In Document360, create the article by importing the Word file; the text, tables and images arrive together. Callouts arrive as shaded boxes; convert them to Document360 callouts if wanted. |
| `<slug>.html` | Self-contained preview with all images embedded. Open it in a browser to review, or send it for sign-off. |
| `<slug>.md` + `images/<slug>/` | The source. Edit this when the article changes, then run `build_article.py` again. For the Markdown editor: upload the images folder to Document360 Drive, paste the Markdown body, and re-point each image. |

Copy the title, slug, category, description and tags from the top of the `.md` file into the article settings.

## Not yet confirmed in a live project

- That Document360's Word import carries the embedded images across.
- The callout syntax in the Markdown source (`:::(Warning) (Warning)`).
- Pipe tables render in the Markdown editor but not in the Advanced WYSIWYG editor, and an article converted from Markdown to WYSIWYG cannot be converted back.

If either of the first two misbehaves, correct `references/article-template.md` in the skill and note it here.
