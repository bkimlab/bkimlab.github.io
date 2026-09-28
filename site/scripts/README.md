# build.py: content syntax

Edit `content/<page>.md`, then run `python3 scripts/build.py`. Never edit the
generated `*.html` directly; `python3 scripts/build.py --check` exits 1 if any
page is out of date. `--serve [PORT]` builds and serves on 127.0.0.1
(use `--bind 0.0.0.0` to expose it on the network).

While editing, leave this running and just refresh the browser after saving:

    python3 scripts/build.py --watch --serve

`--watch` rebuilds whenever a `content/*.md` file is saved, added, or removed.
It polls file timestamps every `--interval` seconds (default 1) because
inotify does not work under WSL for files on Windows drives or synced by
Dropbox. A half-saved file with a syntax error is reported and skipped; the
next good save rebuilds. Changes to `build.py` itself need a restart.

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

    @selected{}    # on its own line: lists every record in this file that has
                   # selected={true}, in file order (used for "Selected Publications")

    @hero{set=home}  # on its own line: banner showing one photo of the named set,
                     # chosen at random on each load, from content/hero.md.
                     # Sets: home (Home page), group (Members). This is the site's
                     # only JavaScript; <noscript> shows the set's first photo.

    @member{..., photo={assets/images/people/x/y.jpg}, focus={50% 30%}}
                     # focus = which point of the photo stays in the 120x150 box

To add a new record type, write a `render_x(fields)` function in build.py and
register it in `BLOCK_RENDERERS`.

## Themes
`STYLESHEETS` in build.py: `base.css` (layout) plus one theme file.
`theme-refined.css` is the default. `theme-mono.css` is the original all-Courier look.

## Photos
Originals live in `photos/<folder>/` at the repo root (gitignored: large,
and phone photos carry GPS). `python3 scripts/make_images.py` writes web
copies with metadata stripped into `assets/images/`: `lab_theme/` -> `hero/`,
`group_photos/` -> `group/`, any other folder -> `people/<folder>/`. Commit
the copies. Then reference them from `content/hero.md` or an `@member{}`.

## Favicon
`assets/favicon.svg` is a 16x16 pixel-art Drosophila drawn from
`scripts/favicon_map.txt` (one character per pixel: `B` body, `D` dark
stripe, `E` eye, `W` wing, `L` leg, `.` background). To change it, edit the
map and regenerate:

    python3 scripts/make_favicon.py
