#!/usr/bin/env python3
"""Source/anchor/edition checks for the Hikam Reading Companion pilot."""
from __future__ import annotations

from html import unescape
from html.parser import HTMLParser
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'src'
manifest = json.loads((SRC / 'reading_companions.json').read_text(encoding='utf-8'))
chapters = '\n'.join(p.read_text(encoding='utf-8') for p in sorted((SRC/'chapters').glob('subtopic-*.html')))
main = (SRC/'main.html').read_text(encoding='utf-8')
built = (ROOT/'index.html').read_text(encoding='utf-8')
ref = (SRC/'philosophy_study_notes.html').read_text(encoding='utf-8')
reader = (SRC/'reading_companions.js').read_text(encoding='utf-8')
assert manifest['version'] == 1
assert '<!-- HIKAM_READING_COMPANIONS_DATA -->' in main
assert 'id="hikamReadingCompanionsData"' in built
assert 'id="hikamReadingCompanionsData"' in ref
assert '<script src="reading_companions.js"></script>' not in built
assert 'window.__hikamReadingCompanions' in built
assert 'fetch(' not in reader, 'Companions must not depend on a network request'
assert all(k not in main for k in ('lit-companion-trigger', 'lit-evidence-trigger'))

def normalized(text: str) -> str:
    return ' '.join(unescape(text).split())

def get_paragraphs(html: str) -> list[tuple[str, str, list[str]]]:
    paragraphs = []
    for p in re.finditer(r'<p(?:\s[^>]*)?>([\s\S]*?)</p>', html):
        raw = p.group(1)
        plain = normalized(re.sub(r'<[^>]+>', '', raw))
        pieces = [unescape(x) for x in re.split(r'<[^>]+>', raw)]
        paragraphs.append((raw, plain, pieces))
    return paragraphs

seen = set()
for item in manifest['companions']:
    ident = item['id']
    assert ident not in seen, f'Duplicate ID {ident}'
    seen.add(ident)
    assert re.fullmatch(r'ch\d+-\d+-\d+', item['chapter']), ident
    assert item['source']['printedPages'], f'No primary page reference: {ident}'
    assert item['source']['author'] in ('Dermot Moran', 'Rowland Stout', 'David Papineau', 'Gary Gutting'), ident
    assert 20 <= len(item['explanation'].split()) <= 110, f'Explanation out of pilot range: {ident}'
    assert item['added_value'].strip(), ident
    start = chapters.find(f'<section class="chapter" id="{item["chapter"]}"')
    end = chapters.find('<section class="chapter" id="', start + 20)
    if end < 0:
        end = len(chapters)
    assert start >= 0 and end > start, item['chapter']
    body = chapters[start:end]
    body = body[body.index('<div class="chapter-body">'):]
    # Exclude intentionally hidden optional Source Depth before checking prose
    # anchors. Its citations and supplementary text cannot become cue targets.
    body = re.sub(r'<details class="hikam-source-depth-inline"[\s\S]*?</details>', '', body)
    # Exact prose anchors must remain unique without relying on callout text.
    matches = [p for p in get_paragraphs(body) if normalized(item['passage']) in p[1]]
    assert len(matches) == 1, f'Missing/ambiguous paragraph for {ident}: {len(matches)}'
    hits = [node for node in matches[0][2] if item['text'] in node]
    assert len(hits) == 1 and hits[0].count(item['text']) == 1, f'Missing/ambiguous text node: {ident}'
    assert ident in built, f'Manifest item not published: {ident}'
assert len(seen) == len(manifest['companions']), f'Missing manifest entries: {len(seen)} vs {len(manifest["companions"])}'
# Preserve the 34 Moran/Stout source records; verify Papineau independently.
moran = [x for x in manifest['companions'] if x['chapter'] == 'ch1-1-1']
stout = [x for x in manifest['companions'] if x['chapter'] == 'ch1-1-2']
papineau = [x for x in manifest['companions'] if x['chapter'] == 'ch1-1-3']
gutting = [x for x in manifest['companions'] if x['chapter'] == 'ch1-1-4']
assert len(moran) == 10 and len(stout) == 24 and len(papineau) == 12 and len(gutting) == 12
assert len(seen) == 58
assert 'class="historical-timeline"' in chapters
assert 'The One Thread to Follow' in chapters
assert 'The four thinkers below are not four unrelated stories.' in chapters
for chapter_id, items in [('ch1-1-1', moran), ('ch1-1-2', stout)]:
    begin = chapters.index(f'<section class="chapter" id="{chapter_id}"')
    after = chapters.find('<section class="chapter" id="', begin + 15)
    html = chapters[begin:after if after >= 0 else len(chapters)]
    body = html[html.index('<div class="chapter-body">'):html.index('<!-- ================= END OF CHAPTER BLOCK')]
    blocks = list(re.finditer(r'<details class="hikam-source-depth-inline"[\s\S]*?</details>', body))
    assert len(blocks) >= 1, chapter_id
    assert all(' open' not in x.group(0).split('>', 1)[0] for x in blocks), chapter_id
    assert body.count('class="hikam-source-depth-item"') == len(items)
    assert 'hikam-source-depth-ch1-1-1' not in body
    for item in items:
        assert all(isinstance(item.get(k), str) and item[k].strip()
                   for k in ('simple', 'why_here', 'remember', 'sourceDepthId')), item['id']
        assert item['sourceDepthId'] == 'source-depth-' + item['id']
        assert body.count('id="' + item['sourceDepthId'] + '"') == 1, item['id']
        # An inline source disclosure follows the exact source paragraph,
        # rather than being a detached appendix or a cue popup.
        callout = next(x.group(0) for x in blocks if 'id="' + item['sourceDepthId'] + '"' in x.group(0))
        assert item['source']['author'] in unescape(callout), item['id']
        for pg in item['source']['printedPages']:
            assert str(pg) in callout, (item['id'], pg)
        source_text = normalized(re.sub('<[^>]+>', '', unescape(callout)))
        assert len(source_text.split()) >= 25, item['id']
        if chapter_id == 'ch1-1-2':
            assert normalized(item['explanation']) in source_text, item['id']
# New Papineau cues resolve local source concepts; optional depth records have
# independent selection, not one depth box per Companion.
begin = chapters.index('<section class="chapter" id="ch1-1-3"')
after = chapters.find('<section class="chapter" id="', begin + 15)
html = chapters[begin:after if after >= 0 else len(chapters)]
body = html[html.index('<div class="chapter-body">'):html.index('<nav class="chapter-endnav"')]
blocks = list(re.finditer(r'<details class="hikam-source-depth-inline"[\s\S]*?</details>', body))
assert len(blocks) == 9, f'Papineau: source disclosures {len(blocks)} != 9'
assert body.count('class="hikam-source-depth-item"') == 9
assert all(' open' not in block.group(0).split('>', 1)[0] for block in blocks)
assert 'Original author: <strong>David Papineau</strong>' in html
assert 'style="--hue:248;"' in html
for item in papineau:
    assert all(item.get(k) for k in ('simple', 'why_here', 'remember')), item['id']
    if item.get('sourceDepthId'):
        assert body.count('id="' + item['sourceDepthId'] + '"') == 1, item['id']
    assert item['source']['author'] == 'David Papineau'
for block in blocks:
    assert 'David Papineau' in block.group(0)
    assert body[:block.start()].rstrip().endswith('</p>'), 'Depth is not paragraph-adjacent'
    assert 'hikam-source-depth-citation' in block.group(0)
# Gutting 1.1.4: 12 context-first explanations, nine independent local
# source-depth records, author's exact attribution, correct hue and citations.
begin = chapters.index('<section class="chapter" id="ch1-1-4"')
after = chapters.find('<section class="chapter" id="', begin + 15)
html = chapters[begin:after if after >= 0 else len(chapters)]
body = html[html.index('<div class="chapter-body">'):html.index('<nav class="chapter-endnav"')]
blocks = list(re.finditer(r'<details class="hikam-source-depth-inline"[\s\S]*?</details>', body))
assert len(blocks) == 9, f'Gutting source disclosures {len(blocks)} != 9'
assert body.count('class="hikam-source-depth-item"') == 9
assert all(' open' not in block.group(0).split('>', 1)[0] for block in blocks)
assert 'Original author: <strong>Gary Gutting</strong>' in html
assert 'style="--hue:268;"' in html
for item in gutting:
    assert all(item.get(k) for k in ('simple', 'why_here', 'remember')), item['id']
    assert item['source']['author'] == 'Gary Gutting'
    assert all(860 <= pg <= 871 for pg in item['source']['printedPages']), item['id']
    if item.get('sourceDepthId'):
        assert body.count('id="' + item['sourceDepthId'] + '"') == 1, item['id']
for block in blocks:
    assert 'Gary Gutting' in block.group(0)
    assert body[:block.start()].rstrip().endswith('</p>'), 'Gutting depth is not paragraph-adjacent'
    assert 'hikam-source-depth-citation' in block.group(0)
assert 'hikam-companion-context-field' in reader
assert 'item.simple && item.why_here && item.remember' in reader
assert "'.hikam-source-depth-inline'" in (SRC/'philosophy_notes.js').read_text(encoding='utf-8') or '.hikam-source-depth-inline' in (SRC/'philosophy_notes.js').read_text(encoding='utf-8')
assert '.hikam-source-depth-inline {display:none!important;}' in (SRC/'philosophy_notes.css').read_text(encoding='utf-8')
assert 'class="hikam-source-depth-inline"' in built
assert 'class="historical-timeline"' in built

print(f'PASS: {len(seen)} source-anchored Companions, source anchors intact, single-file offline embedding')
