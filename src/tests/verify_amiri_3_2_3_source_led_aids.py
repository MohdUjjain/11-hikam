#!/usr/bin/env python3
"""Source-faithful fine-tuning 3.2.3: semantics, archival Git blobs and exact Companions."""
from __future__ import annotations
from hashlib import sha1
from html.parser import HTMLParser
from html import unescape
from pathlib import Path
import json
import re

SRC = Path(__file__).resolve().parents[1]
raw = (SRC / 'chapters/subtopic-3-2.html').read_text(encoding='utf-8')
start_tag = '<section class="chapter rtl" id="ch3-2-3" lang="ar" style="--hue:8;">'
assert raw.count(start_tag) == 1
start = raw.index(start_tag)
chapter = raw[start:raw.index('\n</section>', start) + len('\n</section>')]
front = chapter.split('<div class="chapter-body">',1)[0]
body = chapter.split('<div class="chapter-body">',1)[1].split('<nav class="chapter-endnav"',1)[0]
depth_regex = r'<details class="hikam-source-depth-inline"[^>]*>[\s\S]*?</details>'
visible = re.sub(depth_regex, '', body)
assert 'سامي عامري' in front and 'برهان الضبط الدقيق' in front
assert '--hue:8' in chapter and 'lang="ar"' in chapter
assert 'href="#ch3-2-4"' in chapter
assert chapter.count('class="sec"') == 5
assert chapter.count('class="endh"') == 6
assert chapter.count('class="examq-cat"') == 5
assert len(re.findall(depth_regex, body)) == 5
assert 'ص 441 و443–461' in front

def git_blob(path: Path) -> str:
    raw_bytes = path.read_bytes()
    return sha1(f'blob {len(raw_bytes)}\0'.encode()+raw_bytes).hexdigest()

archive = SRC / 'archive/pre-redevelopment-2026-11-21/dossier-3.2.3-before-2026-11-28-pedagogical-rework.html'
old_original = SRC / 'archive/pre-redevelopment-2026-11-21/dossier-3.2.3.html'
assert git_blob(archive) == '5b7dfde49d5a2c08518f37c73b6ff573a2f24d26'
assert git_blob(old_original) == 'fcedc9256c33f26c8034fc27fe3799063dec84d7'
archived = archive.read_text(encoding='utf-8')
assert archived.count('class="comparison"') == 6
assert archived.count('class="endh"') == 6
assert archived.count('class="examq-cat"') == 5
assert (SRC / 'docs/editorial/READING_3_2_3_AMERI_FINE_TUNING_SOURCE_AUDIT.md').exists()

AIDS=set('box checkpoint comparison tbl-wrap section-objective golden-quote hierarchy analogy concept-rel'.split())
class WordCount(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.count = [], [0, 0]
    def handle_starttag(self, tag, attrs):
        if tag not in {'br','hr','input','img','link','meta'}:
            self.stack.append((tag, bool(AIDS & set(dict(attrs).get('class','').split()))))
    def handle_endtag(self, tag):
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i][0] == tag:
                self.stack = self.stack[:i]
                break
    def handle_data(self, text):
        self.count[int(any(is_aid for _,is_aid in self.stack))] += len(text.split())

# Rules adopted for this source-led corpus refinement.
opening = re.findall(r'<div class="box concept">([\s\\S]*?)</p></div>', body)
assert len(opening) == 1
central = re.sub(r'<[^>]+>', ' ', opening[0])
assert 40 <= len(central.split()) <= 75, ('Central concept out of range', central)
for aid,limit in (('memory',30),('highyield',40),('mistake',35)):
    for m in re.finditer(r'<div class="box '+aid+r'">([\s\\S]*?)</p></div>',body):
        par = re.search(r'<p>([\s\\S]*?)</p>',m.group(0))
        assert par
        content=re.sub(r'<[^>]+>', '', par.group(1))
        assert len(content.split()) <= limit, (aid,len(content.split()))
definitions=re.findall(r'<div class="box definition">([\s\\S]*?)</div>',body)
assert len(definitions)==1
entries=re.findall(r'<p>([\s\\S]*?)</p>',definitions[0])
assert len(entries)==2 and all(0 < len(re.sub(r'<[^>]+>','',x).split()) <= 20 for x in entries)
assert all('class="h-node l1"' in line for line in [line for line in visible.split('\n') if 'الصيغة الرباعية' in line or 'أدلة انتظام البداية' in line])
roadmap=re.search(r'<div class="in-this-chapter">([\s\\S]*?)</ol></div>',front)
assert roadmap
points=re.findall(r'<li>([\s\\S]*?)</li>',roadmap.group(1))
assert len(points)==5
for point in points:
    assert re.match(r'<b>[^<]{3,40}</b>',point), ('Roadmap lead-in not bold',point)
    assert 7 <= len(re.sub(r'<[^>]+>','',point).split()) <= 15, ('Roadmap length',point)
for m in re.finditer(r'<table class="comparison">([\s\\S]*?)</table>',chapter):
    for cell in re.findall(r'<(?:td|th)[^>]*>([\s\\S]*?)</(?:td|th)>',m.group(1)):
        assert len(re.sub(r'<[^>]+>','',cell).split()) <= 20, ('Table cell too long',cell)

word_count=WordCount()
word_count.feed(visible)
prose,aids=word_count.count
assert 650<=prose<=850, word_count.count
assert 850<=aids<=1150, word_count.count
assert 1500<=prose+aids<=2000, word_count.count
assert visible.count('class="comparison"') == 4
assert chapter.count('class="comparison"') == 5   # independent revision key table
assert visible.count('scope="col"') == 12
assert visible.count('scope="row"') == 13
assert visible.count('class="hierarchy"') == 3
assert visible.count('class="box mistake"') == 1
assert visible.count('class="box memory"') == 2
assert visible.count('class="box definition"') == 1
assert visible.count('class="box tip"') == 0
assert visible.count('class="checkpoint"') == 0
assert visible.count('class="box concept"') == 1
assert visible.count('class="concept-rel"') == 1
assert visible.count('class="analogy"') == 1

for required in (
    'دليل العناية', 'الصيغة الرباعية', 'الضرورة المادية',
    'تفسيرًا', 'الصدفة', 'الحكمة', '١٩', '٣٧', '١٥٠',
    'القوة النووية الكبرى', 'القوة الكهرومغناطيسية',
    'مبدأ التكميم', 'الثابت الكوني',
    'بنروز', 'فن وايلن', 'هاوكنغ', 'مارتن ريس',
    'ستة', 'الماء', 'الكربون', 'هندرسون', 'دينتون'
):
    assert required in visible, (required, word_count.count)
assert 'مباحث الاعتراض' in chapter
for label in ('خلاصة الدرس','ورقة المراجعة المختصرة','التعريفات الأساسية',
              'الجدول الجامع','مفاتيح الاستذكار','أسئلة محتملة للامتحان'):
    assert label in chapter
assert 'الاستبعاد في حدود العادة' in chapter
assert 'الإنتروبيا' in chapter.split('<div class="end-block">')[1]

cues = [item for item in json.loads((SRC/'reading_companions.json').read_text(encoding='utf-8'))['companions']
        if item['chapter'] == 'ch3-2-3']
assert len(cues)==5
depths=re.findall(depth_regex,body)
for cue in cues:
    passage=cue['passage']
    # Bold emphasis changes HTML text-node boundaries but not the exact
    # source-grounded paragraph. Require unique equal visible text.
    def plain(fragment):
        return ' '.join(unescape(re.sub(r'<[^>]+>', '', fragment)).split())
    paragraphs = re.findall(r'<p>([\s\S]*?)</p>', body)
    exact = [paragraph for paragraph in paragraphs if plain(paragraph) == plain(passage)]
    assert len(exact) == 1, (cue['id'], len(exact))
    assert sum(cue['text'] in part for part in re.split(r'<[^>]+>', exact[0])) == 1, cue['id']
    assert cue['text'] in passage, cue['id']
    assert cue['source']['author'] == 'سامي عامري'
    assert all(p==441 or 443<=p<=461 for p in cue['source']['printedPages'])
    assert all(cue.get(k) for k in ('simple','why_here','remember','sourceDepthId'))
    matches=[x for x in depths if cue['sourceDepthId'] in x]
    assert len(matches)==1, cue['id']
    detail=matches[0]
    assert '<summary>' in detail and ' open' not in detail.split('>',1)[0]
    preceding=body[:body.index(detail)].rstrip()
    assert preceding.endswith('</p>'), cue['id']
    assert cue['text'] in preceding[preceding.rfind('<p>'):], cue['id']

print(f'PASS 3.2.3: {prose} prose + {aids} aids = {prose+aids}; 4 true comparisons, 3 hierarchies, 5 exact cues/Depth, immutable predecessor, all six revision sections',flush=True)
