# Kim Lab website

Source for the Kim Lab (Princeton EEB) website. Pages are written in Markdown
and compiled to plain HTML/CSS by a small Python script; no JavaScript,
frameworks, or trackers. Published with GitHub Pages at https://bkimlab.github.io/.

## Editing a page

1. Edit the Markdown in `site/content/` (`index.md`, `research.md`,
   `publications.md`, `members.md`, `join-us.md`). Syntax reference:
   [`site/scripts/README.md`](site/scripts/README.md).
2. Preview locally (optional): `python3 site/scripts/build.py --watch --serve`
   then open http://127.0.0.1:8000 and refresh after each save.
3. Rebuild the HTML: `python3 site/scripts/build.py`
4. Commit both the `.md` and the regenerated `.html`, and push.

Pushing to the default branch triggers `.github/workflows/pages.yml`, which
rebuilds from the Markdown on GitHub's servers and publishes `site/`. Editing
a `.md` file directly in the GitHub web editor also works; the workflow
rebuilds, so you never have to touch HTML.

`python3 site/scripts/build.py --check` reports whether the committed HTML
matches the Markdown.

## Layout

```
site/              published directory (GitHub Pages root)
  content/*.md     page sources
  *.html           generated; do not edit by hand
  css/             base.css + one theme file
  assets/images/
  scripts/build.py generator (standard library only)
grants/            source PDFs, gitignored, never published
```

## One-time GitHub setup

In the repository: Settings -> Pages -> Build and deployment -> Source:
**GitHub Actions**. No branch or folder selection is needed.
