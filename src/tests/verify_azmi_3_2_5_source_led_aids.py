#!/usr/bin/env python3
"""Bounded 3.2.5 checks: preservation, visible pedagogy and exact local anchors.

This does not replace reading the original source or an Arabic editorial review.
Use --isolation for this release's comparison with its pinned upstream baseline;
omit it when running this chapter test after later authorized chapter revisions.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from hashlib import sha1, sha256
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'src'
ID = 'ch3-2-5'
AUTHOR = 'هشام عزمي'
BASELINE = 'f2d277d154f1a616f5b2d8a9bbe84df5b9556575'
SOURCE_PAGES = {*range(14, 36), *range(91, 98)}
AIDS = set('box checkpoint comparison tbl-wrap section-objective golden-quote hierarchy analogy concept-rel historical-timeline'.split())
VOID = set('area base br col embed hr img input link meta param source track wbr'.split())


@dataclass
class Node:
    tag: str
    attrs: dict = field(default_factory=dict)
    children: list = field(default_factory=list)

    def has(self, name):
        return name in self.attrs.get('class', '').split()

    def text(self):
        return ''.join(c.text() if isinstance(c, Node) else c for c in self.children)

    def walk(self):
        yield self
        for child in self.children:
            if isinstance(child, Node):
                yield from child.walk()

    def elements(self):
        return [c for c in self.children if isinstance(c, Node)]


class Tree(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.root = Node('root')
        self.stack = [self.root]
        self.feed(html)
        assert len(self.stack) == 1, 'Unclosed chapter element'

    def handle_starttag(self, tag, attrs):
        node = Node(tag, dict(attrs))
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].children.append(Node(tag, dict(attrs)))

    def handle_endtag(self, tag):
        assert self.stack[-1].tag == tag, ('Mismatched HTML', tag, self.stack[-1].tag)
        self.stack.pop()

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def blob(path):
    data = path.read_bytes()
    return sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()


def normalized(value):
    return ' '.join(value.split())


def visible_nodes(node):
    if node.has('hikam-source-depth-inline'):
        return
    yield node
    for child in node.elements():
        yield from visible_nodes(child)


def unvocalized(value):
    return ''.join(c for c in unicodedata.normalize('NFKC', value)
                   if not unicodedata.combining(c) and c != 'ـ')


def words(node, aid=False):
    if node.has('hikam-source-depth-inline'):
        return [0, 0]
    aid = aid or bool(AIDS & set(node.attrs.get('class', '').split()))
    result = [0, 0]
    for child in node.children:
        if isinstance(child, Node):
            part = words(child, aid)
            result = [a+b for a, b in zip(result, part)]
        else:
            result[int(aid)] += len(child.split())
    return result


module = (SRC / 'chapters/subtopic-3-2.html').read_text(encoding='utf-8')
matches = list(re.finditer(r'<section class="chapter rtl" id="ch3-2-5"[^>]*>.*?\n</section>', module, re.S))
assert len(matches) == 1, 'Missing or duplicated target chapter'
match = matches[0]
chapter = Tree(match[0]).root.elements()[0]
assert chapter.attrs.get('lang') == 'ar' and chapter.attrs.get('style') == '--hue:48;'
parts = chapter.elements()
assert len(parts) == 4 and [p.attrs.get('class') for p in parts] == [
    'chapter-frontmatter', 'chapter-body', 'chapter-endnav', 'end-block'
], 'Print flows must remain separate direct siblings'
front, body, nav, revision = parts
titles = [n for n in front.walk() if n.has('chapter-title')]
assert len(titles) == 1 and normalized(titles[0].text()) == 'الإلحاد الجديد'
assert any(n.tag == 'strong' and normalized(n.text()) == AUTHOR for n in front.walk())
assert any(n.attrs.get('href') == '#toc' for n in nav.walk())
assert any(n.attrs.get('href') == '#ch3-2-6' for n in nav.walk())
assert len([n for n in body.walk() if n.has('sec')]) == 5
ids = [n.attrs['id'] for n in chapter.walk() if 'id' in n.attrs]
assert len(ids) == len(set(ids)), 'Duplicate chapter/depth identifier'

archives = {
    'pre-redevelopment-2026-11-21/dossier-3.2.5-before-2026-11-28-pedagogical-rework.html': '44b81a54e4b158a159e368a80154756daa195559',
    'pre-redevelopment-2026-11-21/dossier-3.2.5.html': '2b03c83ef8fa35078655c1dee6bec9708c1a37f3',
    'pre-prepared-source-2026-11-26/dossier-3.2.5.html': '35fc0954d8e44f2bc37ea7eea73bae1864853e38',
}
for path, expected in archives.items():
    assert blob(SRC / 'archive' / path) == expected, ('Changed historical edition', path)

headings = [normalized(n.text()) for n in revision.walk() if n.has('endh')]
assert headings == ['خلاصة الدرس', 'ورقة المراجعة المختصرة', 'التعريفات الأساسية',
                    'الجدول الجامع', 'مفاتيح الاستذكار', 'أسئلة محتملة للامتحان']
categories = [n for n in revision.walk() if n.has('examq-cat')]
assert len(categories) == 5 and all(n.text().strip() for n in categories)
assert any(n.has('revision-sheet') and n.text().strip() for n in revision.walk())
assert len([n for n in revision.walk() if n.has('keydef-item')]) >= 4
assert any(n.has('comparison') and n.text().strip() for n in revision.walk())
assert any(n.has('memlist') and len(n.elements()) >= 3 for n in revision.walk())
exam = next(n for n in revision.walk() if n.has('examq')).elements()
for category in categories:
    following = exam[exam.index(category)+1]
    assert following.tag == 'ol' and any(n.tag == 'li' and n.text().strip() for n in following.elements())
visible = list(visible_nodes(body))
for name in ('concept', 'definition', 'highyield', 'tip', 'golden-quote', 'hierarchy', 'analogy', 'concept-rel', 'checkpoint'):
    assert any(n.has(name) for n in visible), ('Lost established visible aid type', name)

tables = [n for n in visible if n.tag == 'table' and n.has('comparison')]
assert tables, 'The source needs genuine same-axis comparisons'
for table in tables:
    assert any(n.tag == 'caption' and n.text().strip() for n in table.elements())
    head = next(n for n in table.elements() if n.tag == 'thead')
    headers = [n for n in head.walk() if n.tag == 'th']
    assert 3 <= len(headers) <= 4, 'Do not restore generic two-column paragraph tables'
    assert all(n.attrs.get('scope') == 'col' for n in headers)
    rows = [n for n in next(n for n in table.elements() if n.tag == 'tbody').elements() if n.tag == 'tr']
    assert len(rows) >= 2
    for row in rows:
        cells = row.elements()
        assert len(cells) == len(headers), 'Comparison dimensions must align'
        assert cells[0].tag == 'th' and cells[0].attrs.get('scope') == 'row'
        assert all(c.text().strip() for c in cells), 'Empty comparison dimension'

# Pascal's source argument is a two-choice/two-hypothesis matrix, rather than
# a paragraph placed in one table cell. Check its four populated outcomes.
wagers = [table for table in tables if any(n.tag == 'caption' and 'باسكال' in n.text() for n in table.elements())]
assert len(wagers) == 1, 'Pascal needs one identifiable outcome matrix'
wager_rows = [n for n in next(n for n in wagers[0].elements() if n.tag == 'tbody').elements() if n.tag == 'tr']
assert len(wager_rows) == 2 and all(len(row.elements()) == 3 for row in wager_rows), 'Pascal must retain both choices under both hypotheses'

# Chronological order is the component's function. Dates still require the
# original-source audit; there is no prescribed total of events or tables.
timelines = [n for n in visible if n.has('historical-timeline')]
assert timelines, 'The dated works must retain their source-led chronology'
for timeline in timelines:
    assert timeline.attrs.get('role') == 'group' and timeline.attrs.get('aria-label', '').strip()
    assert any(n.has('historical-timeline-title') and n.text().strip() for n in timeline.elements())
    events = [n for n in timeline.walk() if n.has('historical-timeline-event')]
    assert len(events) >= 2, 'A historical timeline must contain a sequence'
    years = []
    for event in events:
        assert event.tag == 'li'
        date = next(n for n in event.elements() if n.has('historical-timeline-date'))
        assert re.fullmatch(r'\d{4}', normalized(date.text())), 'Book chronology needs a clear source year'
        years.append(int(normalized(date.text())))
        assert any(n.has('historical-timeline-description') and n.text().strip() for n in event.elements())
    assert years == sorted(years), 'Historical events must remain chronological'

prose, aids = words(body)
assert 650 <= prose <= 850 and 850 <= aids <= 1150 and 1500 <= prose+aids <= 2000, (prose, aids)
# Coverage sentinels guard against losing major source units, not their correctness.
visible_text = ''.join(n.text() for n in body.elements() if not n.has('hikam-source-depth-inline'))
for term in ('اللاأدري', 'القابلية', 'التأزم', 'باسكال'):
    assert unvocalized(term) in unvocalized(visible_text), ('Essential source unit missing from visible layer', term)
assert re.search(r'(?:ال)?مرجحات\s+(?:ال)?خارجية', unvocalized(visible_text)), 'The external-considerations distinction must remain visible'

manifest = json.loads((SRC / 'reading_companions.json').read_text(encoding='utf-8'))
cues = [c for c in manifest['companions'] if c['chapter'] == ID]
assert cues and len({c['id'] for c in cues}) == len(cues)
body_elements = body.elements()
depths = [n for n in body_elements if n.has('hikam-source-depth-inline')]
assert depths, 'Local optional source detail must remain available'
for detail in depths:
    index = body_elements.index(detail)
    assert index and body_elements[index-1].tag == 'p', 'Source Depth must immediately follow its prose paragraph'
    assert detail.tag == 'details' and 'open' not in detail.attrs
    assert detail.elements()[0].tag == 'summary' and detail.elements()[0].text().strip()
    records = [n for n in detail.walk() if n.has('hikam-source-depth-item')]
    assert records and detail.attrs.get('data-depth-count') == str(len(records)), 'Disclosure count must describe its actual source records'
    for record in records:
        assert record.attrs.get('id', '').startswith('source-depth-')
        assert any(n.tag == 'h4' and n.text().strip() for n in record.elements())
        citations = [n for n in record.walk() if n.has('hikam-source-depth-citation')]
        assert citations and all(AUTHOR in n.text() for n in citations)
        for citation in citations:
            locator = re.search(r'\bص\s+(.+)', citation.text())
            assert locator, ('Missing printed source locator', record.attrs['id'])
            ranges = re.findall(r'(\d+)(?:\s*[–-]\s*(\d+))?', locator[1])
            pages = {p for first, last in ranges for p in range(int(first), int(last or first)+1)}
            assert pages and pages <= SOURCE_PAGES, ('Depth citation leaves the assigned extract', record.attrs['id'], pages)
depth_records = [n for detail in depths for n in detail.walk() if n.has('hikam-source-depth-item')]
for cue in cues:
    assert all(cue.get(k) for k in ('simple', 'why_here', 'remember'))
    assert cue['source']['author'] == AUTHOR
    pages = cue['source'].get('printedPages', [])
    assert pages and set(pages) <= SOURCE_PAGES, 'Cite only the assigned discontinuous extract'
    paragraphs = [n for n in body_elements if n.tag == 'p' and normalized(n.text()) == normalized(cue['passage'])]
    assert len(paragraphs) == 1, ('Companion paragraph missing/ambiguous', cue['id'])
    paragraph = paragraphs[0]
    assert paragraph.text().count(cue['text']) == 1, ('Companion cue ambiguous', cue['id'])
    # A contextual explanation does not manufacture an optional source record.
    # If it links one, that record must belong to this same local disclosure.
    if cue.get('sourceDepthId'):
        following = body_elements[body_elements.index(paragraph)+1]
        assert following.has('hikam-source-depth-inline')
        assert any(n.attrs.get('id') == cue['sourceDepthId'] for n in following.walk()), cue['id']

if '--isolation' in sys.argv:
    unchanged = module[:match.start()] + '<!-- TARGET 3.2.5 -->' + module[match.end():]
    assert sha256(unchanged.encode()).hexdigest() == '12390cabd87900474dddd83fbc70b7fa3f2193099e19f5c76d60f65bd6f1804b', 'Neighboring chapters or module divider changed'
    stable = {
        'src/chapters/subtopic-1-1.html': 'aa1c9b91dbbc4aeb2da8a7c8413d9a7c605ffa0c',
        'src/chapters/subtopic-2-1.html': '7a4b778e1f379c7325bf9d8659d1bba2737ef892',
        'src/chapters/subtopic-2-2.html': '563bd7adcef2171dd8a8a205a3211fdc61edf251',
        'src/chapters/subtopic-3-1.html': '5a4663dd1b2514f04dd12d6ffd38995dc079383b',
        'src/chapters/subtopic-3-3.html': 'ab2ff7aaf340cf572c47c0fb2385a8cf6cddeb3d',
        'src/chapters/subtopic-3-4.html': 'c1bf9e5b7766767229ce105659cd182bc460a05a',
        'src/chapters/subtopic-3-5.html': '053bbb2931cfe8220a1244df5d5412d6509af01a',
        'src/chapters/subtopic-3-6.html': 'fe5167eecca1322604c276c454cb798e9be89abb',
        'src/chapters/subtopic-3-7.html': '70038fce8a832fef9ccc1a4a5faf191819f98050',
        'src/chapters/subtopic-3-8.html': '65c8d5f39d2a84752d6e06f3c79d2cd38eca8d49',
        'src/main.html': 'ba9bf9218be742cde9bfaae6aec09bb63cb8646e',
        'src/philosophy_notes.css': 'ea7666d2f661c594bbdf3b531362737f70d3609a',
        'src/philosophy_notes.js': '2dd4be6fda24f5d00d902fd253a1262c7e8aca97',
        'src/reading_companions.js': '2e678c16451fda5f9e2c9ef42a6bed55ca446a3d',
        'src/offline-reader.js': '2d16a7ecb4b99adeded7678e36dfa6b9512be805',
        'src/build.py': '4a384f34f0a4a733676f4a1a17d426ca15c80779',
        'src/service-worker.template.js': 'bee8aa76b739187bdfae7fb31da438d749b9b8e9',
    }
    for path, expected in stable.items():
        assert blob(ROOT / path) == expected, ('Outside authorized release scope', path)
    other = {**manifest, 'companions': [c for c in manifest['companions'] if c['chapter'] != ID]}
    encoded = json.dumps(other, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
    assert sha256(encoded).hexdigest() == 'bed65123b89729996f044cdbc71c5e6b57cd8e59ef87ac18a55512355794acae', 'Unrelated Companion records changed'
    print(f'PASS 3.2.5 release isolation against {BASELINE}', flush=True)

print(f'PASS 3.2.5: {prose} prose + {aids} aids = {prose+aids}; {len(tables)} accessible comparisons / {len(timelines)} source chronologies; {len(cues)} exact cues / {len(depths)} adjacent closed Depth groups / {len(depth_records)} independent records; 3 immutable editions; complete revision', flush=True)
