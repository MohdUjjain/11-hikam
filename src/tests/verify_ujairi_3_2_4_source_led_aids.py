#!/usr/bin/env python3
"""Bounded 3.2.4 checks: preservation, visible pedagogy and exact local anchors.

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

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'src'
ID = 'ch3-2-4'
AUTHOR = 'عبد الله بن صالح العجيري'
BASELINE = 'beae14901b4dbc9bcdd6f214f2a5cea981463b18'
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
matches = list(re.finditer(r'<section class="chapter rtl" id="ch3-2-4"[^>]*>.*?\n</section>', module, re.S))
assert len(matches) == 1, 'Missing or duplicated target chapter'
match = matches[0]
chapter = Tree(match[0]).root.elements()[0]
assert chapter.attrs.get('lang') == 'ar' and chapter.attrs.get('style') == '--hue:28;'
parts = chapter.elements()
assert len(parts) == 4 and [p.attrs.get('class') for p in parts] == [
    'chapter-frontmatter', 'chapter-body', 'chapter-endnav', 'end-block'
], 'Print flows must remain separate direct siblings'
front, body, nav, revision = parts
assert AUTHOR in front.text() and 'الدلالة العقلية الأولى' in front.text()
assert any(n.attrs.get('href') == '#ch3-2-5' for n in nav.walk())
assert len([n for n in body.walk() if n.has('sec')]) == 5
ids = [n.attrs['id'] for n in chapter.walk() if 'id' in n.attrs]
assert len(ids) == len(set(ids)), 'Duplicate chapter/depth identifier'

archives = {
    'pre-redevelopment-2026-11-21/dossier-3.2.4-before-2026-11-28-pedagogical-rework.html': '0e83f0c55c87e47b6436cf030f17127c4c125dd4',
    'pre-redevelopment-2026-11-21/dossier-3.2.4.html': 'd278e05012c13fe7d59a40896af1ba431fe77646',
    'pre-prepared-source-2026-11-26/dossier-3.2.4.html': '1af846b7b57f8427f765955d760e0687b38c3ce1',
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
for name in ('concept', 'definition', 'highyield', 'mistake', 'memory', 'hierarchy', 'analogy', 'concept-rel'):
    assert any(n.has(name) for n in body.walk()), ('Lost established aid type', name)

# Current corpus rules supplement legacy source-coverage checks.
assert len([n for n in body.walk() if n.has('concept')]) == 1, 'One opening thesis per dossier'
assert not any(n.has('tip') or n.has('checkpoint') for n in body.walk()), 'Retired main-reading aids remain'
frontmap = next(n for n in front.walk() if n.has('in-this-chapter'))
for point in [n for n in frontmap.walk() if n.tag == 'li']:
    assert any(n.tag == 'b' for n in point.elements()), 'Roadmap bold lead-in missing'
    assert 7 <= len(point.text().split()) <= 15, ('Roadmap preview length', point.text())
for family, limit in (('memory', 30), ('highyield', 40), ('mistake', 35)):
    for entry in [n for n in body.walk() if n.has(family)]:
        paras = [n for n in entry.walk() if n.tag == 'p']
        count = sum(len(p.text().split()) for p in paras)
        assert count <= limit, ('Aid over current whole-box cap', family, count)
for definition in [n for n in body.walk() if n.has('definition')]:
    paras = [n for n in definition.elements() if n.tag == 'p']
    assert 1 <= len(paras) <= 2
    assert all(len(p.text().split()) <= 20 and len(re.findall(r'[.؟!]', p.text())) <= 2 for p in paras)
    assert sum(len(p.text().split()) for p in paras) <= 40
for tbl in [n for n in body.walk() if n.tag == 'table']:
    for cell in [n for n in tbl.walk() if n.tag in ('td', 'th')]:
        assert len(cell.text().split()) <= 20, ('Table cell exceeds hard limit', cell.text())
assert '١.٤ · كلاهما معدوم' in body.text(), 'Ibn Hazm nested subcases lost'
assert 'ممتنع' in body.text() and 'واجب' in body.text() and 'ممكن' in body.text()

tables = [n for n in body.walk() if n.tag == 'table' and n.has('comparison')]
assert len(tables) >= 2, 'The source needs genuine same-axis comparisons'
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

prose, aids = words(body)
assert 650 <= prose <= 850 and 850 <= aids <= 1150 and 1500 <= prose+aids <= 2000, (prose, aids)
# Coverage sentinels guard against losing major source units, not their correctness.
visible_text = ''.join(n.text() for n in body.elements() if not n.has('hikam-source-depth-inline'))
for term in ('ابن حزم', 'ابن كثير', 'جنس الحوادث', 'السببية', 'التعادل الحراري'):
    assert term in visible_text, ('Essential source unit missing from visible layer', term)

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
    assert any(n.has('hikam-source-depth-citation') and AUTHOR in n.text() for n in detail.walk())
for cue in cues:
    assert all(cue.get(k) for k in ('simple', 'why_here', 'remember', 'sourceDepthId'))
    assert cue['source']['author'] == AUTHOR
    assert set(cue['source'].get('printedPages', [])) <= set(range(95, 120)), 'Do not invent a page number for the final leaf'
    paragraphs = [n for n in body_elements if n.tag == 'p' and normalized(n.text()) == normalized(cue['passage'])]
    assert len(paragraphs) == 1, ('Companion paragraph missing/ambiguous', cue['id'])
    paragraph = paragraphs[0]
    assert paragraph.text().count(cue['text']) == 1, ('Companion cue ambiguous', cue['id'])
    following = body_elements[body_elements.index(paragraph)+1]
    assert following.has('hikam-source-depth-inline')
    assert any(n.attrs.get('id') == cue['sourceDepthId'] for n in following.walk()), cue['id']

if '--isolation' in sys.argv:
    unchanged = module[:match.start()] + '<!-- TARGET 3.2.4 -->' + module[match.end():]
    assert sha256(unchanged.encode()).hexdigest() == '689d4e6d89cbb92f511b23d6b2a952b5edeb441a0a874d33892c4fed43fdf659', 'Neighboring chapters or module divider changed'
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
    assert sha256(encoded).hexdigest() == '206cc72a79579331ffc88b367f3de88d590195578192fdc00e361f9129d31cec', 'Unrelated Companion records changed'
    print(f'PASS 3.2.4 release isolation against {BASELINE}', flush=True)

print(f'PASS 3.2.4: {prose} prose + {aids} aids = {prose+aids}; {len(tables)} accessible comparisons; {len(cues)} exact cues / {len(depths)} adjacent closed Depth groups; 3 immutable editions; complete revision', flush=True)
