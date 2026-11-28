#!/usr/bin/env python3
"""3.2.2: accepted study-aid roles, Arabic emphasis, and immutable predecessor."""
from __future__ import annotations

from hashlib import sha1
from html import unescape
from pathlib import Path
import json
import re

SRC = Path(__file__).resolve().parents[1]
raw = (SRC/'chapters/subtopic-3-2.html').read_text(encoding='utf-8')
start = '<section class="chapter rtl" id="ch3-2-2" lang="ar" style="--hue:348;">'
assert raw.count(start) == 1
chapter = raw[raw.index(start):].split('\n</section>',1)[0]
front, rest = chapter.split('<div class="chapter-body">',1)
body = rest.split('<nav class="chapter-endnav"',1)[0]
visible = re.sub(r'<details class="hikam-source-depth-inline"[\s\S]*?</details>','',body)

def plain(html):
    return ' '.join(unescape(re.sub(r'<[^>]+>','',html)).split())

def words(html):
    return len(plain(html).split())

def one_card(kind):
    pattern = (r'<div class="box '+kind+r'"><div class="box-label">'
               r'[\s\S]*?</div><p>([\s\S]*?)</p></div>')
    return re.findall(pattern,visible)

opening=one_card('concept')
assert len(opening)==1 and 40<=words(opening[0])<=75,('Opening thesis',list(map(words,opening)))
memory=one_card('memory')
mistake=one_card('mistake')
assert len(memory)==1 and words(memory[0])<=30,('Memory',list(map(words,memory)))
assert len(mistake)==1 and words(mistake[0])<=35,('Misreading',list(map(words,mistake)))
assert not one_card('highyield') and 'class="box highyield"' not in visible
assert 'class="box tip"' not in visible and 'class="checkpoint"' not in visible

definitions=re.findall(
    r'<div class="box definition"><div class="box-label">[\s\S]*?</div>'
    r'((?:<p>[\s\S]*?</p>){1,2})</div>',visible)
assert len(definitions)==1
entries=re.findall(r'<p>([\s\S]*?)</p>',definitions[0])
assert len(entries)==2 and sum(map(words,entries))<=40
assert all(0<words(e)<=20 and e.count('.')<=2 for e in entries),list(map(words,entries))

eli10=re.findall(
    r'<div class="analogy">[\s\S]*?<div class="box-label">[\s\S]*?</div>'
    r'<p>([\s\S]*?)</p></div></div>',visible)
assert len(eli10)==1 and 20<=words(eli10[0])<=30,('Compiler analogy',list(map(words,eli10)))
assert 'تقريب تعليمي من صياغة الملاحظات' in visible

tables=re.findall(r'<table class="comparison">([\s\S]*?)</table>',chapter)
assert len(tables)==5,'Four main comparisons and an independent revision table'
for table in tables:
    for cell in re.findall(r'<(?:th|td)[^>]*>([\s\S]*?)</(?:th|td)>',table):
        assert words(cell)<=20,('Table cell',words(cell),plain(cell))
assert visible.count('scope="col"')==12 and visible.count('scope="row"')==12

roadmap=re.search(r'<div class="in-this-chapter">([\s\S]*?)</ol></div>',front)
assert roadmap
points=re.findall(r'<li>([\s\S]*?)</li>',roadmap.group(1))
assert len(points)==5
for point in points:
    assert re.match(r'<b>[^<]+</b>',point) and 7<=words(point)<=15,('Roadmap',words(point),point)

assert visible.count('class="hierarchy"')==4
assert not re.search(r'class="h-node l[23]"',visible),'Parallel items are not subordinate categories'
assert visible.count('class="concept-rel"')==1
assert visible.count('class="section-objective"')==5
assert chapter.count('class="endh"')==6 and chapter.count('class="examq-cat"')==5

paragraphs=re.findall(r'(?m)^\s*<p>(.*?)</p>\s*$',visible)
assert len(paragraphs)==10,('Ordinary teaching paragraphs',len(paragraphs))
for paragraph in paragraphs:
    bold=re.findall(r'<b>([^<>]+)</b>',paragraph)
    assert bold and all(1<=words(x)<=12 for x in bold),('Selective emphasis missing',plain(paragraph)[:90])
    assert sum(map(words,bold))<words(paragraph),'Whole paragraph emphasized'
    assert '<b><b>' not in paragraph

manifest=json.loads((SRC/'reading_companions.json').read_text(encoding='utf-8'))
cues=[x for x in manifest['companions'] if x['chapter']=='ch3-2-2']
assert len(cues)==5
for cue in cues:
    matched=[p for p in paragraphs if plain(p)==plain(cue['passage'])]
    assert len(matched)==1,('Companion exact passage changed',cue['id'])
    nodes=re.split(r'<[^>]+>',matched[0])
    assert sum(cue['text'] in node for node in nodes)==1,('Companion cue split',cue['id'])

file=SRC/'archive/pre-redevelopment-2026-11-21/dossier-3.2.2-before-2026-11-29-corpus-role-and-prose-emphasis.html'
data=file.read_bytes()
digest=sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
assert digest=='d35f9150e6728b2ba4f85d051fe3579c98bb6fff',digest
assert data.count(b'class="checkpoint"')==2
assert 'الاعتراض البيولوجي الخامس' in visible and 'ثلاثة افتراضات' in visible
assert 'لا يتضمن المقتطف تتمة تفنيده لها' in visible,'Do not reconstruct unassigned response'
print(f'PASS 3.2.2 roles: opening {words(opening[0])}, memory {words(memory[0])}, '
      f'mistake {words(mistake[0])}, definitions {list(map(words,entries))}, '
      f'EL10 {words(eli10[0])}; 4 true main tables, 5 previews, '
      f'10 selectively emphasized paragraphs, 5 exact Companions, 6 revisions and immutable archive',
      flush=True)
