# build.py: content syntax

Edit `content/<page>.md`, then run `python3 scripts/build.py`. Never edit the
generated `*.html` directly; `python3 scripts/build.py --check` exits 1 if any
page is out of date. `--serve [PORT]` builds and serves on 127.0.0.1
(use `--bind 0.0.0.0` to expose it on the network).

## Front matter (optional, first lines of the file)
    ---
    title: Our Research            # <title> tag; default is the nav label
    subtitle: Shown under the H1   # header subtitle
    description: One sentence.     # <meta name="description">
    ---

## Blocks
| Syntax | Output |
|---|---|
| `# Title` | ignored (the template supplies the H1) |
| `## Section` / `### Subsection` | section headings |
| `- item` or `* item` | bullet list |
| `1. item` | numbered list |
| `![alt](path)` alone on a line | full-width banner image |
| any other non-blank line | paragraph (one line = one paragraph) |

## Inline
`**bold**`, `*italic*`, `_italic_`, `` `code` ``, `[text](url)`.
Text is HTML-escaped, so `&` and `<` are safe. URLs and code are never touched
by the emphasis rules, so underscores in links are fine.

## Records (BibTeX-style, may span lines, nested braces OK)
    @article{key, title={...}, author={Kim, BY and Doe, J and others},
             journal={...}, volume={..}, number={..}, pages={..}, year={..},
             note={Preprint}}          # any unknown @type renders as a citation

    @member{name={...}, email={name [at] princeton -dot- edu},
            bio={...}, photo={assets/images/name.jpg}}

    @grant{title={...}, funder={...}, years={2026-2029}, role={PI}, note={...}}

To add a new record type, write a `render_x(fields)` function in build.py and
register it in `BLOCK_RENDERERS`.

## Themes
`STYLESHEETS` in build.py: `base.css` (layout) plus one theme file.
`theme-refined.css` is the default. `theme-mono.css` is the original all-Courier look.
