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
    assert item['source']['author'] in ('Dermot Moran', 'Rowland Stout', 'David Papineau', 'Gary Gutting', 'Simon Critchley', 'Colin Bird', 'Jonathan Wolff', 'W. D. Ross', 'Hugh Lawson-Tancred', 'James Kellenberger', 'Keith E. Yandell', 'Anthony Kenny', 'سامر توفيق عجمي', 'سلطان بن عبد الرحمن العميري', 'سامي عامري', 'عبد الله بن صالح العجيري', 'هشام عزمي', 'محمد باقر السيستاني', 'مركز المعارف للمناهج والمتون التعليمية', 'Karen Armstrong', 'أحمد إبراهيم', 'علي آل محسن', 'سامي عامري', 'أيمن المصري', 'Alister E. McGrath and Joanna Collicutt McGrath', 'John C. Lennox', 'Michael J. Behe', 'مصطفى عزيزي', 'عبد الحسين خسروپناه', 'حسين أحمد الخشن', 'محمد محمد رضائي وحسين رهنمائي', 'المؤلف غير مذكور في النص المقرر'), ident
    assert 20 <= len(item['explanation'].split()) <= 110, f'Explanation out of pilot range: {ident}'
    assert item['added_value'].strip(), ident
    # Arabic chapters are existing "chapter rtl" sections; match both
    # established spellings without changing any chapter markup.
    open_match = re.search(
        r'<section class="chapter(?: rtl)?" id="' + re.escape(item["chapter"]) + r'"',
        chapters,
    )
    start = open_match.start() if open_match else -1
    assert start >= 0, item['chapter']
    next_match = re.search(r'<section class="chapter(?: rtl)?" id="', chapters[start + 20:])
    end = (start + 20 + next_match.start()) if next_match else len(chapters)
    assert end > start, item['chapter']
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
assert len(seen) == 512  # Includes Yandell's 3.1.2 cues and three new Kenny 3.1.3 cues
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
# Critchley 1.1.5: all local cues must resolve in visible prose, and the
# five optional records remain adjacent to the correct explanatory paragraphs.
begin = chapters.index('<section class="chapter" id="ch1-1-5"')
html = chapters[begin:]
body = html[html.index('<div class="chapter-body">'):html.index('<nav class="chapter-endnav"')]
critchley = [x for x in manifest['companions'] if x['chapter'] == 'ch1-1-5']
assert len(critchley) == 9
assert 'style="--hue:288;"' in html
assert 'Simon Critchley' in html
blocks = list(re.finditer(r'<details class="hikam-source-depth-inline"[\s\S]*?</details>', body))
assert len(blocks) == 5
assert body.count('class="hikam-source-depth-item"') == 5
assert all(' open' not in b.group(0).split('>', 1)[0] for b in blocks)
for item in critchley:
    assert item['source']['author'] == 'Simon Critchley'
    assert all(item.get(k) for k in ('simple','why_here','remember'))
    assert all(1 <= pg <= 8 for pg in item['source']['printedPages'])
    if item.get('sourceDepthId'):
        assert body.count('id="' + item['sourceDepthId'] + '"') == 1
for block in blocks:
    assert 'Simon Critchley' in block.group(0)
    assert body[:block.start()].rstrip().endswith('</p>'), 'Critchley depth is not paragraph-adjacent'
    assert 'hikam-source-depth-citation' in block.group(0)
# Bird 2.1.1: original title and author; eleven cues with six
# independent, closed paragraph-adjacent source-detail records.
begin = chapters.index('<section class="chapter" id="ch2-1-1"')
after = chapters.find('<section class="chapter" id="', begin + 15)
html = chapters[begin:after if after >= 0 else len(chapters)]
body = html[html.index('<div class="chapter-body">'):html.index('<nav class="chapter-endnav"')]
bird = [x for x in manifest['companions'] if x['chapter'] == 'ch2-1-1']
assert len(bird) == 11
assert 'style="--hue:308;"' in html
assert 'Original author: <strong>Colin Bird</strong>' in html
assert '<h1 class="chapter-title">Introduction</h1>' in html
blocks = list(re.finditer(r'<details class="hikam-source-depth-inline"[\s\S]*?</details>', body))
assert len(blocks) == 6
assert body.count('class="hikam-source-depth-item"') == 6
for item in bird:
    assert item['source']['author'] == 'Colin Bird'
    assert all(item.get(k) for k in ('simple','why_here','remember'))
    assert all(1 <= pg <= 11 for pg in item['source']['printedPages'])
    if item.get('sourceDepthId'):
        assert body.count('id="' + item['sourceDepthId'] + '"') == 1
for disclosure in blocks:
    assert 'Colin Bird' in disclosure.group(0)
    assert body[:disclosure.start()].rstrip().endswith('</p>')
    assert ' open' not in disclosure.group(0).split('>',1)[0]
    assert 'hikam-source-depth-citation' in disclosure.group(0)
# Bird 2.1.2: twelve source-grounded contextual cues and six native,
# paragraph-adjacent optional disclosures, separate from the prior introduction.
begin = chapters.index('<section class="chapter" id="ch2-1-2"')
after = chapters.index('<section class="chapter" id="ch2-1-3"', begin)
html = chapters[begin:after]
body = html[html.index('<div class="chapter-body">'):html.index('<nav class="chapter-endnav"')]
common_good = [x for x in manifest['companions'] if x['chapter'] == 'ch2-1-2']
assert len(common_good) == 12
assert 'style="--hue:328;"' in html
assert 'Original author: <strong>Colin Bird</strong>' in html
assert '<h1 class="chapter-title">The Common Good</h1>' in html
blocks = list(re.finditer(r'<details class="hikam-source-depth-inline"[\s\S]*?</details>', body))
assert len(blocks) == 6
assert body.count('class="hikam-source-depth-item"') == 6
for item in common_good:
    assert item['source']['author'] == 'Colin Bird'
    assert all(item.get(k) for k in ('simple', 'why_here', 'remember'))
    assert all(1 <= pg <= 10 for pg in item['source']['printedPages'])
    if item.get('sourceDepthId'):
        assert body.count('id="' + item['sourceDepthId'] + '"') == 1
for disclosure in blocks:
    assert body[:disclosure.start()].rstrip().endswith('</p>'), "2.1.2 depth must be adjacent"
    assert ' open' not in disclosure.group(0).split('>',1)[0]
    assert 'Colin Bird' in disclosure.group(0)
    assert 'hikam-source-depth-citation' in disclosure.group(0)
# Bird 2.1.3: source-proportionate 30-page War edition, with nineteen
# contextual cues and fourteen grouped source records inside ten disclosures.
begin = chapters.index('<section class="chapter" id="ch2-1-3"')
after = chapters.index('<section class="chapter" id="ch2-1-4"', begin)
html = chapters[begin:after]
body = html[html.index('<div class="chapter-body">'):html.index('<nav class="chapter-endnav"')]
war = [item for item in manifest['companions'] if item['chapter'] == 'ch2-1-3']
assert len(war) == 19
assert 'style="--hue:348;"' in html
assert 'Original author: <strong>Colin Bird</strong>' in html
assert 'Chapter 11, “War,”' in html and '2nd ed.' in html
blocks = list(re.finditer(r'<details class="hikam-source-depth-inline"[\s\S]*?</details>', body))
assert len(blocks) == 10
assert body.count('class="hikam-source-depth-item"') == 14
assert sum(int(m.group(1)) for b in blocks for m in re.finditer(r'data-depth-count="(\d+)"', b.group(0))) == 14
for item in war:
    assert item['source']['author'] == 'Colin Bird'
    assert '2019' in item['source']['work']
    assert all(item.get(k) for k in ('simple', 'why_here', 'remember'))
    assert all(1 <= pg <= 30 for pg in item['source']['printedPages'])
    if item.get('sourceDepthId'):
        assert body.count('id="' + item['sourceDepthId'] + '"') == 1, item['id']
for disclosure in blocks:
    assert body[:disclosure.start()].rstrip().endswith('</p>'), 'War depth is not paragraph adjacent'
    assert ' open' not in disclosure.group(0).split('>',1)[0], 'War depth starts open'
    assert 'Colin Bird' in disclosure.group(0)
    assert 'hikam-source-depth-citation' in disclosure.group(0)
# Wolff 2.1.4: both original selections, nine adjacent native disclosures,
# seventeen source records and 23 independently anchored contextual cues.
begin = chapters.index('<section class="chapter" id="ch2-1-4"')
after = chapters.index('<section class="chapter" id="ch2-1-5"', begin)
html = chapters[begin:after]
body = html[html.index('<div class="chapter-body">'):html.index('<nav class="chapter-endnav"')]
wolff = [item for item in manifest['companions'] if item['chapter'] == 'ch2-1-4']
assert len(wolff) == 23
assert 'style="--hue:8;"' in html
assert 'Original author: <strong>Jonathan Wolff</strong>' in html
assert 'Oxford University Press' in html and '2006' in html
assert '<h1 class="chapter-title">Introduction &amp; Who Should Rule?</h1>' in html
blocks = list(re.finditer(r'<details class="hikam-source-depth-inline"[\s\S]*?</details>', body))
assert len(blocks) == 9
assert body.count('class="hikam-source-depth-item"') == 17
assert sum(int(m.group(1)) for b in blocks for m in re.finditer(r'data-depth-count="(\d+)"', b.group(0))) == 17
for item in wolff:
    assert item['source']['author'] == 'Jonathan Wolff'
    assert '2006' in item['source']['work']
    assert all(item.get(k) for k in ('simple', 'why_here', 'remember'))
    assert all((1 <= pg <= 5) or (62 <= pg <= 77) for pg in item['source']['printedPages'])
    if item.get('sourceDepthId'):
        assert body.count('id="' + item['sourceDepthId'] + '"') == 1, item['id']
for disclosure in blocks:
    assert body[:disclosure.start()].rstrip().endswith('</p>'), 'Wolff depth is not adjacent'
    assert ' open' not in disclosure.group(0).split('>', 1)[0]
    assert 'Jonathan Wolff' in disclosure.group(0)
    assert 'hikam-source-depth-citation' in disclosure.group(0)
# Wolff 2.1.5: 22 new source-specific contextual Companions and
# 16 independently cited records immediately after eight prose paragraphs.
begin = chapters.index('<section class="chapter" id="ch2-1-5"')
after = chapters.index('<section class="chapter" id="ch2-1-6"', begin)
html = chapters[begin:after]
body = html[html.index('<div class="chapter-body">'):html.index('<nav class="chapter-endnav"')]
liberty = [item for item in manifest['companions'] if item['chapter'] == 'ch2-1-5']
assert len(liberty) == 22
assert 'style="--hue:28;"' in html
assert 'Original author: <strong>Jonathan Wolff</strong>' in html
assert 'pp. 104–117' in html
blocks = list(re.finditer(r'<details class="hikam-source-depth-inline"[\s\S]*?</details>', body))
assert len(blocks) == 8
assert body.count('class="hikam-source-depth-item"') == 16
assert sum(int(m.group(1)) for b in blocks for m in re.finditer(r'data-depth-count="(\d+)"', b.group(0))) == 16
for item in liberty:
    assert item['source']['author'] == 'Jonathan Wolff'
    assert '2006' in item['source']['work']
    assert all(item.get(k) for k in ('simple', 'why_here', 'remember'))
    assert all(104 <= pg <= 117 for pg in item['source']['printedPages'])
    if item.get('sourceDepthId'):
        assert body.count('id="' + item['sourceDepthId'] + '"') == 1, item['id']
for disclosure in blocks:
    assert body[:disclosure.start()].rstrip().endswith('</p>')
    assert ' open' not in disclosure.group(0).split('>', 1)[0]
    assert 'Jonathan Wolff' in disclosure.group(0)
    assert 'hikam-source-depth-citation' in disclosure.group(0)
# Wolff 2.1.6: source-bound introductory extract pp. 177–182.
begin = chapters.index('<section class="chapter" id="ch2-1-6"')
after = chapters.index('<section class="chapter rtl" id="ch2-1-7"', begin)
html = chapters[begin:after]
body = html[html.index('<div class="chapter-body">'):html.index('<nav class="chapter-endnav"')]
items = [item for item in manifest['companions'] if item['chapter'] == 'ch2-1-6']
assert len(items) == 4
assert 'style="--hue:48;"' in html
assert 'Original author: <strong>Jonathan Wolff</strong>' in html
assert 'pp. 177–182' in html
assert 'the promised feminist arguments' in body
blocks = list(re.finditer(r'<details class="hikam-source-depth-inline"[\s\S]*?</details>', body))
assert len(blocks) == 2
assert body.count('class="hikam-source-depth-item"') == 2
assert sum(int(m.group(1)) for b in blocks for m in re.finditer(r'data-depth-count="(\d+)"', b.group(0))) == 2
for item in items:
    assert item['source']['author'] == 'Jonathan Wolff'
    assert all(177 <= pg <= 182 for pg in item['source']['printedPages'])
    assert all(item.get(k) for k in ('simple', 'why_here', 'remember'))
for disclosure in blocks:
    assert body[:disclosure.start()].rstrip().endswith('</p>')
    assert ' open' not in disclosure.group(0).split('>', 1)[0]
    assert 'Jonathan Wolff' in disclosure.group(0)
    assert 'hikam-source-depth-citation' in disclosure.group(0)
# Arabic 2.1.7: source-led chapter, eight contextual explanations and nine optional records.
begin = chapters.index('<section class="chapter rtl" id="ch2-1-7"')
after = chapters.index('<section class="chapter rtl" id="ch2-1-8"', begin)
arabic = chapters[begin:after]
arabic_body = arabic[arabic.index('<div class="chapter-body">'):arabic.index('<nav class="chapter-endnav"')]
arabic_companions = [item for item in manifest['companions'] if item['chapter'] == 'ch2-1-7']
assert len(arabic_companions) == 8
assert 'lang="ar"' in arabic.split('>', 1)[0]
assert 'style="--hue:68;"' in arabic
assert '<h1 class="chapter-title">تطور علم السياسة</h1>' in arabic
assert 'اسم المؤلف غير مذكور' in arabic
assert len(re.findall(r'<h2 class="endh">', arabic)) == 6
assert len(re.findall(r'class="examq-cat"', arabic)) == 5
arabic_depths = list(re.finditer(r'<details class="hikam-source-depth-inline"[\s\S]*?</details>', arabic_body))
assert len(arabic_depths) == 7, len(arabic_depths)
assert arabic_body.count('class="hikam-source-depth-item"') == 9
assert sum(int(m.group(1)) for block in arabic_depths for m in re.finditer(r'data-depth-count="(\d+)"', block.group(0))) == 9
for item in arabic_companions:
    assert item['source']['author'] == 'المؤلف غير مذكور في النص المقرر'
    assert all(1 <= page <= 16 for page in item['source']['printedPages'])
    assert all(item.get(k) for k in ('simple', 'why_here', 'remember'))
for disclosure in arabic_depths:
    assert arabic_body[:disclosure.start()].rstrip().endswith('</p>'), "Arabic detail not adjacent to paragraph"
    assert ' open' not in disclosure.group(0).split('>', 1)[0]
    assert 'class="hikam-source-depth-citation"' in disclosure.group(0)
# Arabic Plato 2.1.8: nine contextual explanations, eleven source records.
plato_begin = chapters.index('<section class="chapter rtl" id="ch2-1-8"')
plato = chapters[plato_begin:chapters.index('\n</section>', plato_begin) + len('\n</section>')]  # chapter-closing tag at column zero
plato_body = plato[plato.index('<div class="chapter-body">'):plato.index('<nav class="chapter-endnav"')]
plato_items = [item for item in manifest['companions'] if item['chapter'] == 'ch2-1-8']
assert len(plato_items) == 9
assert 'lang="ar"' in plato.split('>', 1)[0]
assert 'style="--hue:88;"' in plato
assert '<h1 class="chapter-title">أفلاطون: المدينة الفاضلة</h1>' in plato
assert 'اسم المؤلف غير مذكور' in plato
assert len(re.findall(r'<h2 class="endh">', plato)) == 6
assert len(re.findall(r'class="examq-cat"', plato)) == 5
plato_depths = list(re.finditer(r'<details class="hikam-source-depth-inline"[\s\S]*?</details>', plato_body))
assert len(plato_depths) == 8, len(plato_depths)
assert plato_body.count('class="hikam-source-depth-item"') == 11
assert sum(map(int, re.findall(r'data-depth-count="(\d+)"', plato_body))) == 11
for item in plato_items:
    assert item['source']['author'] == 'المؤلف غير مذكور في النص المقرر'
    assert all(1 <= page <= 12 for page in item['source']['printedPages'])
    assert all(item.get(k) for k in ('simple', 'why_here', 'remember'))
for disclosure in plato_depths:
    assert plato_body[:disclosure.start()].rstrip().endswith('</p>'), "2.1.8 optional detail not adjacent to paragraph"
    assert ' open' not in disclosure.group(0).split('>', 1)[0]
    assert 'hikam-source-depth-citation' in disclosure.group(0)
# Arabic metaphysics 2.2.1 — 12 contextual Companions, 11 optional source records.
m_begin = chapters.index('<section class="chapter rtl" id="ch2-2-1"')
m_chapter = chapters[m_begin:chapters.index('\n</section>', m_begin) + len('\n</section>')]
m_body = m_chapter[m_chapter.index('<div class="chapter-body">'):m_chapter.index('<nav class="chapter-endnav"')]
m_items = [x for x in manifest['companions'] if x['chapter'] == 'ch2-2-1']
assert len(m_items) == 12
assert 'lang="ar"' in m_chapter.split('>',1)[0]
assert 'style="--hue:108;"' in m_chapter
assert '<h1 class="chapter-title">ما الميتافيزيقا...؟</h1>' in m_chapter
assert 'اسم المؤلف غير مذكور' in m_chapter
assert len(re.findall(r'<h2 class="endh">', m_chapter)) == 6
assert len(re.findall(r'class="examq-cat"', m_chapter)) == 5
m_depths = list(re.finditer(r'<details class="hikam-source-depth-inline"[\s\S]*?</details>', m_body))
assert len(m_depths) == 7, len(m_depths)
assert m_body.count('class="hikam-source-depth-item"') == 11
assert sum(map(int, re.findall(r'data-depth-count="(\d+)"', m_body))) == 11
for item in m_items:
    assert item['source']['author'] == 'المؤلف غير مذكور في النص المقرر'
    assert all(1 <= page <= 16 for page in item['source']['printedPages'])
    assert all(item.get(k) for k in ('simple','why_here','remember'))
for disclosure in m_depths:
    assert m_body[:disclosure.start()].rstrip().endswith('</p>'), "2.2.1 Source Depth not paragraph adjacent"
    assert ' open' not in disclosure.group(0).split('>',1)[0]
    assert 'hikam-source-depth-citation' in disclosure.group(0)
# Arabic 2.2.2 — thirteen contextual Companions and 11 cited Source Depth records.
d222_start = chapters.index('<section class="chapter rtl" id="ch2-2-2"')
d222 = chapters[d222_start:chapters.index('\n</section>', d222_start) + len('\n</section>')]
d222_body = d222[d222.index('<div class="chapter-body">'):d222.index('<nav class="chapter-endnav"')]
d222_items = [item for item in manifest['companions'] if item['chapter'] == 'ch2-2-2']
assert len(d222_items) == 13
assert 'lang="ar"' in d222.split('>', 1)[0]
assert 'style="--hue:128;"' in d222
assert '<h1 class="chapter-title">التقسيم التقليدي للميتافيزيقا</h1>' in d222
assert 'لم يرد اسم المؤلف' in d222
assert len(re.findall(r'<h2 class="endh">', d222)) == 6
assert len(re.findall(r'class="examq-cat"', d222)) == 5
d222_depths = list(re.finditer(r'<details class="hikam-source-depth-inline"[\s\S]*?</details>', d222_body))
assert len(d222_depths) == 7
assert d222_body.count('class="hikam-source-depth-item"') == 11
assert sum(map(int, re.findall(r'data-depth-count="(\d+)"', d222_body))) == 11
for entry in d222_items:
    assert entry['source']['author'] == 'المؤلف غير مذكور في النص المقرر'
    assert all(1 <= pg <= 8 for pg in entry['source']['printedPages'])
    assert all(entry.get(k) for k in ('simple', 'why_here', 'remember'))
for disclosure in d222_depths:
    assert d222_body[:disclosure.start()].rstrip().endswith('</p>'), "2.2.2 disclosure not immediately paragraph-adjacent"
    assert ' open' not in disclosure.group(0).split('>', 1)[0]
    assert 'hikam-source-depth-citation' in disclosure.group(0)
# Arabic 2.2.3 — both source chapters, thirteen Companions, thirteen Depth records.
d223_start = chapters.index('<section class="chapter rtl" id="ch2-2-3"')
d223 = chapters[d223_start:chapters.index('\n</section>', d223_start) + len('\n</section>')]
d223_body = d223[d223.index('<div class="chapter-body">'):d223.index('<nav class="chapter-endnav"')]
d223_items = [x for x in manifest['companions'] if x['chapter'] == 'ch2-2-3']
assert len(d223_items) == 13
assert 'lang="ar"' in d223.split('>', 1)[0]
assert 'style="--hue:148;"' in d223
assert '<h1 class="chapter-title">الميتافيزيقا عند فلاسفة الإسلام والمسيحية</h1>' in d223
assert "اسم المؤلف غير مثبت" in d223
assert len(re.findall(r'<h2 class="endh">', d223)) == 6
assert len(re.findall(r'class="examq-cat"', d223)) == 5
d223_depths = list(re.finditer(r'<details class="hikam-source-depth-inline"[\s\S]*?</details>', d223_body))
assert len(d223_depths) == 7
assert d223_body.count('class="hikam-source-depth-item"') == 13
assert sum(map(int, re.findall(r'data-depth-count="(\d+)"', d223_body))) == 13
for entry in d223_items:
    assert entry['source']['author'] == 'المؤلف غير مذكور في النص المقرر'
    assert all(1 <= page <= 8 for page in entry['source']['printedPages'])
    assert all(entry.get(k) for k in ('simple', 'why_here', 'remember'))
for disclosure in d223_depths:
    assert d223_body[:disclosure.start()].rstrip().endswith('</p>'), "2.2.3 Source Depth must immediately follow prose"
    assert ' open' not in disclosure.group(0).split('>', 1)[0]
    assert 'hikam-source-depth-citation' in disclosure.group(0)
# English 2.2.5 — critical introduction to the composite Metaphysics
# (not the general Aristotle textbook summaries supplied as planning aids).
d225_start = chapters.index('<section class="chapter" id="ch2-2-5"')
d225 = chapters[d225_start:chapters.index('\n</section>', d225_start) + len('\n</section>')]
d225_body = d225[d225.index('<div class="chapter-body">'):d225.index('<nav class="chapter-endnav"')]
d225_items = [x for x in manifest['companions'] if x['chapter'] == 'ch2-2-5']
assert len(d225_items) == 10, "Expected ten exact local 2.2.5 cues"
assert 'style="--hue:188;"' in d225
assert '<h1 class="chapter-title">The Structure of Aristotle’s Metaphysics</h1>' in d225
assert len(re.findall(r'<h2 class="endh">', d225)) == 6
assert d225.count('class="examq-cat"') == 5
d225_disclosures = list(re.finditer(
    r'<details class="hikam-source-depth-inline"[\s\S]*?</details>', d225_body
))
assert len(d225_disclosures) == 4, "2.2.5 has four paragraph-adjacent optional disclosures"
assert sum(int(re.search(r'data-depth-count="(\d+)"', block.group()).group(1))
           for block in d225_disclosures) == 7
assert d225_body.count('class="hikam-source-depth-item"') == 7
assert all(item['source']['author'] == 'W. D. Ross'
           and item['source']['printedPages'] and item.get('simple')
           and item.get('why_here') and item.get('remember')
           for item in d225_items)
for disclosure in d225_disclosures:
    assert d225_body[:disclosure.start()].rstrip().endswith('</p>'), (
        "2.2.5 Source Depth must follow its source paragraph"
    )
    assert ' open' not in disclosure.group().split('>', 1)[0]
    assert 'hikam-source-depth-citation' in disclosure.group()
assert 'Socrates, Plato, and the Platonists' in d225
# English 2.2.6 — Hugh Lawson-Tancred, full 42-page introduction.
d226_start = chapters.index('<section class="chapter" id="ch2-2-6"')
d226 = chapters[d226_start:chapters.index('\n</section>', d226_start) + len('\n</section>')]
d226_body = d226[d226.index('<div class="chapter-body">'):d226.index('<nav class="chapter-endnav"')]
d226_items = [x for x in manifest['companions'] if x['chapter'] == 'ch2-2-6']
assert len(d226_items) == 13
assert 'Hugh Lawson-Tancred' in d226
assert 'style="--hue:208;"' in d226
assert '<h1 class="chapter-title">Substance, Change and Intelligibility: An Introduction to Aristotle’s Metaphysics</h1>' in d226
assert len(re.findall(r'<h2 class="endh">', d226)) == 6
assert d226.count('class="examq-cat"') == 5
d226_depth = list(re.finditer(r'<details class="hikam-source-depth-inline"[\s\S]*?</details>', d226_body))
assert len(d226_depth) == 5
assert [int(re.search(r'data-depth-count="(\d+)"', block.group()).group(1))
        for block in d226_depth] == [2, 2, 2, 3, 3]
assert d226_body.count('class="hikam-source-depth-item"') == 12
assert all(item['source']['author'] == 'Hugh Lawson-Tancred'
           and item['source']['printedPages'] and all(1 <= p <= 42 for p in item['source']['printedPages'])
           and item.get('simple') and item.get('why_here') and item.get('remember')
           for item in d226_items)
for block in d226_depth:
    assert d226_body[:block.start()].rstrip().endswith('</p>'), "226 Source Depth must follow source paragraph"
    assert ' open' not in block.group().split('>', 1)[0]
    assert 'hikam-source-depth-citation' in block.group()
# English 3.1.1 — Kellenberger's Philosophy and Religion opening.
d311_start=chapters.index('<section class="chapter" id="ch3-1-1"')
d311=chapters[d311_start:chapters.index('\n</section>', d311_start)+len('\n</section>')]
d311_body=d311[d311.index('<div class="chapter-body">'):d311.index('<nav class="chapter-endnav"')]
d311_items=[x for x in manifest['companions'] if x['chapter']=='ch3-1-1']
assert len(d311_items)==12
assert 'James Kellenberger' in d311
assert 'style="--hue:228;"' in d311
assert '<h1 class="chapter-title">Introduction: Philosophy and Religion</h1>' in d311
assert len(re.findall(r'<h2 class="endh">', d311))==6
assert d311.count('class="examq-cat"')==5
d311_depth=list(re.finditer(r'<details class="hikam-source-depth-inline"[\s\S]*?</details>', d311_body))
assert len(d311_depth)==7
assert [int(re.search(r'data-depth-count="(\d+)"',d.group()).group(1)) for d in d311_depth]==[2,1,2,1,2,1,2]
assert d311_body.count('class="hikam-source-depth-item"')==11
assert all(item['source']['author']=='James Kellenberger'
           and all(2<=p<=6 for p in item['source']['printedPages'])
           and all(item.get(k) for k in ('simple','why_here','remember'))
           for item in d311_items)
for d in d311_depth:
    assert d311_body[:d.start()].rstrip().endswith('</p>'), '3.1.1 Source Depth must follow prose'
    assert ' open' not in d.group().split('>',1)[0]
    assert 'hikam-source-depth-citation' in d.group()

assert 'hikam-companion-context-field' in reader
assert 'item.simple && item.why_here && item.remember' in reader
assert "'.hikam-source-depth-inline'" in (SRC/'philosophy_notes.js').read_text(encoding='utf-8') or '.hikam-source-depth-inline' in (SRC/'philosophy_notes.js').read_text(encoding='utf-8')
assert '.hikam-source-depth-inline {display:none!important;}' in (SRC/'philosophy_notes.css').read_text(encoding='utf-8')
assert 'class="hikam-source-depth-inline"' in built
assert 'class="historical-timeline"' in built

print(f'PASS: {len(seen)} source-anchored Companions, source anchors intact, single-file offline embedding')
