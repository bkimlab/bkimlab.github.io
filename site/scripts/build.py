"""Static-site generator for the Kim Lab website.

Reads Markdown from content/ and writes flat HTML pages at the site root.

Publications are authored as BibTeX inside content/publications.md so the file
stays a valid, copy-pasteable bibliography, but they are rendered on the site as
compact, human-readable citations.
"""

import os
import re

# ---------------------------------------------------------------------------
# Inline Markdown (bold / italic / code / links)
# ---------------------------------------------------------------------------

def inline(text):
    """Convert inline Markdown to HTML.

    Handles [text](url) links, `code`, **bold**, *italic* and _italic_ with
    properly paired open/close tags (the old build replaced both delimiters
    with the same opening tag, producing invalid, never-closed HTML).
    """
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', text)
    text = re.sub(r'_(.+?)_', r'<em>\1</em>', text)
    return text


# ---------------------------------------------------------------------------
# BibTeX -> compact citation
# ---------------------------------------------------------------------------

def parse_bibtex(entry):
    """Parse a single @type{...} BibTeX record into a dict of fields."""
    fields = {}
    # Match `key = {value}` allowing the value to contain balanced-ish braces.
    for key, value in re.findall(r'(\w+)\s*=\s*\{(.*?)\}\s*,?\s*(?:\n|$)', entry, re.DOTALL):
        fields[key.lower().strip()] = ' '.join(value.split())
    return fields


def format_authors(raw, highlight="Kim"):
    """Format a BibTeX author string into a compact, readable list.

    "Kim, BY and Huber, CD and others" -> "Kim BY, Huber CD, et al."
    The lab PI's surname is wrapped in <strong> so it stands out.
    """
    parts = [a.strip() for a in raw.split(' and ') if a.strip()]
    out = []
    for author in parts:
        if author.lower() == 'others':
            out.append('et al.')
            continue
        if ',' in author:
            last, first = [p.strip() for p in author.split(',', 1)]
            name = f'{last} {first}'.strip()
        else:
            name = author
            last = author.split()[-1] if author.split() else author
        if last == highlight:
            name = f'<strong>{name}</strong>'
        out.append(name)

    if not out:
        return ''
    # Join with commas; "et al." should not get a leading comma-space oddity.
    text = ''
    for i, name in enumerate(out):
        if i == 0:
            text = name
        elif name == 'et al.':
            text += ', et al.'
        else:
            text += f', {name}'
    return text


def format_citation(fields):
    """Render parsed BibTeX fields as one compact HTML citation."""
    authors = format_authors(fields.get('author', ''))
    year = fields.get('year', '')
    title = inline(fields.get('title', '')).rstrip('.')
    journal = fields.get('journal', '')

    # Volume(Number): Pages — omit gracefully whatever is missing.
    vol = fields.get('volume', '')
    num = fields.get('number', '')
    pages = fields.get('pages', '')
    locator = vol
    if num:
        locator += f'({num})'
    if pages:
        locator = f'{locator}: {pages}' if locator else pages

    bits = []
    if authors:
        bits.append(f'<span class="pub-authors">{authors}</span>')
    if year:
        bits.append(f'({year}).')
    citation = ' '.join(bits)
    if title:
        citation += f' {title}.'
    if journal:
        citation += f' <span class="pub-journal">{journal}</span>'
        if locator:
            citation += f' {locator}'
        citation += '.'
    elif locator:
        citation += f' {locator}.'

    note = fields.get('note', '')
    if note:
        citation += f' <span class="pub-tag">{inline(note)}</span>'

    return f'<p class="pub">{citation.strip()}</p>'


# ---------------------------------------------------------------------------
# @member -> member card
# ---------------------------------------------------------------------------

def render_member(fields):
    """Render a parsed @member{...} block as a member card.

    Fields: name (required), email, bio, photo (optional image path). Email is
    intentionally rendered as plain text (no mailto link) to reduce scraping.
    """
    name = fields.get('name', '')
    email = fields.get('email', '')
    bio = fields.get('bio', '')
    photo = fields.get('photo', '')

    if photo:
        img = f'<img class="member-photo" src="{photo}" alt="{name}">'
    else:
        img = '<div class="image-placeholder">PHOTO</div>'

    info = [f'<h3>{inline(name)}</h3>']
    if email:
        info.append(f'<p class="contact">Email: {inline(email)}</p>')
    if bio:
        info.append(f'<p class="research-desc">{inline(bio)}</p>')

    return (
        '<div class="member-card">'
        '<div class="member-flex">'
        f'{img}'
        f'<div class="member-info">{"".join(info)}</div>'
        '</div></div>'
    )


# ---------------------------------------------------------------------------
# Block-level Markdown
# ---------------------------------------------------------------------------

def md_to_html(text):
    lines = text.split('\n')
    html = []
    list_type = None  # None | 'ul' | 'ol'

    def close_list():
        nonlocal list_type
        if list_type:
            html.append(f'</{list_type}>')
            list_type = None

    i = 0
    while i < len(lines):
        raw = lines[i]
        line = raw.strip()

        if not line:
            close_list()
            i += 1
            continue

        # @-block: accumulate until braces balance. @member{...} renders a
        # member card; any other @type{...} is treated as a BibTeX citation.
        if line.startswith('@'):
            close_list()
            block = raw
            depth = raw.count('{') - raw.count('}')
            while depth > 0 and i + 1 < len(lines):
                i += 1
                block += '\n' + lines[i]
                depth += lines[i].count('{') - lines[i].count('}')
            fields = parse_bibtex(block)
            if line.startswith('@member'):
                html.append(render_member(fields))
            else:
                html.append(format_citation(fields))
            i += 1
            continue

        # Standalone image line (`![alt](src)`) -> full-width banner image.
        img_match = re.match(r'^!\[([^\]]*)\]\(([^)]+)\)\s*$', line)
        if img_match:
            close_list()
            alt, src = img_match.group(1), img_match.group(2)
            html.append(f'<img class="banner" src="{src}" alt="{alt}">')
            i += 1
            continue

        # Headings. H1 is reserved for the site header (the page template
        # already emits one), so a leading `# Title` in content is skipped to
        # avoid a duplicate top-level heading.
        if line.startswith('# '):
            close_list()
        elif line.startswith('### '):
            close_list()
            html.append(f'<h3 class="subsection-head">{inline(line[4:])}</h3>')
        elif line.startswith('## '):
            close_list()
            html.append(f'<h2 class="section-head">{inline(line[3:])}</h2>')
        # List items.
        elif re.match(r'^[-*] ', line):
            if list_type != 'ul':
                close_list()
                html.append('<ul>')
                list_type = 'ul'
            html.append(f'<li>{inline(line[2:])}</li>')
        elif re.match(r'^\d+\.\s', line):
            if list_type != 'ol':
                close_list()
                html.append('<ol>')
                list_type = 'ol'
            item = re.sub(r'^\d+\.\s', '', line)
            html.append(f'<li>{inline(item)}</li>')
        else:
            close_list()
            html.append(f'<p>{inline(line)}</p>')
        i += 1

    close_list()
    return '\n'.join(html)


# ---------------------------------------------------------------------------
# Page assembly
# ---------------------------------------------------------------------------

# Active theme. Set to 'style.css' to revert to the original monospace
# ("old CS professor") look; 'classic-refined.css' keeps that identity but
# refines the type, adds a phylogeny/Drosophila header mark, and drops the
# offset shadow. If you change this, update the <link> in members.html to match.
STYLESHEET = 'classic-refined.css'

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | The Kim Lab @ Princeton EEB</title>
    <link rel="stylesheet" href="css/{stylesheet}">
</head>
<body>
    <div id="container">
        <header>
            <h1>{h1_title}</h1>
            <p class="subtitle">{subtitle}</p>
            <nav>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="research.html">Research</a></li>
                    <li><a href="publications.html">Publications</a></li>
                    <li><a href="members.html">Members</a></li>
                    <li><a href="join-us.html">Join Us</a></li>
                </ul>
            </nav>
        </header>
        <main>
{content}
        </main>
        <footer>
            <hr>
            <p>&copy; 2026 Bernard Y. Kim. Last updated: July 18, 2026.</p>
        </footer>
    </div>
</body>
</html>
"""

# page -> (title, h1 shown in header, subtitle)
PAGES = {
    'index': ('Home', 'The Kim Lab @ Princeton EEB', 'Computational Biology &amp; Evolutionary Genomics'),
    'research': ('Our Research', 'The Kim Lab @ Princeton EEB', 'Computational Biology &amp; Evolutionary Genomics'),
    'publications': ('Publications', 'The Kim Lab @ Princeton EEB', 'Peer-reviewed research'),
    'members': ('Members', 'The Kim Lab @ Princeton EEB', 'People contributing to the research'),
    'join-us': ('Join Us', 'The Kim Lab @ Princeton EEB', 'Openings &amp; how to apply'),
}


def generate_site(root):
    content_dir = os.path.join(root, 'content')
    for page, (title, h1_title, subtitle) in PAGES.items():
        md_path = os.path.join(content_dir, f'{page}.md')
        if not os.path.exists(md_path):
            continue
        with open(md_path, 'r', encoding='utf-8') as f:
            body = md_to_html(f.read())
        html = TEMPLATE.format(
            title=title,
            h1_title=h1_title,
            subtitle=subtitle,
            content=body,
            stylesheet=STYLESHEET,
        )
        with open(os.path.join(root, f'{page}.html'), 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'built {page}.html')


if __name__ == "__main__":
    # Site root is the parent of this script's directory, regardless of the
    # working directory the script is invoked from.
    site_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    generate_site(site_root)
