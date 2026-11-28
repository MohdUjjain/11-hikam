#!/usr/bin/env python3
"""Scoped prose-emphasis and archive-fidelity regressions for 3.2.3–3.2.5."""
from __future__ import annotations
from html import unescape
from pathlib import Path
from html.parser import HTMLParser
import re
import json

SRC=Path(__file__).resolve().parents[1]
MODULE=(SRC/'chapters/subtopic-3-2.html').read_text(encoding='utf-8')
PATH=SRC/'archive/pre-redevelopment-2026-11-21'

def chapter(num):
    marker=f'<section class="chapter rtl" id="ch3-2-{num}"'
    assert MODULE.count(marker)==1
    return MODULE[MODULE.index(marker):].split('\n</section>',1)[0]+'\n</section>'

def plain(s):
    return ' '.join(unescape(re.sub(r'<[^>]+>', '', s)).split())

for number in (3,4,5):
    c=chapter(number)
    main=c.split('<div class="chapter-body">',1)[1].split('<nav class="chapter-endnav"',1)[0]
    paragraphs=re.findall(r'(?m)^\s*<p>(.*?)</p>\s*$',main)
    assert len(paragraphs)>=10,(number,len(paragraphs))
    selected=[x for x in paragraphs if re.search(r'<(?:b|strong)>',x)]
    assert len(selected)>=8,(number,'Main prose needs selective key-phrase emphasis',len(selected))
    phrases=[y for para in selected for y in re.findall(r'<b>([^<>]+)</b>',para)]
    assert all(1<=len(plain(p).split())<=12 for p in phrases),('Oversized main-prose bold span',number,phrases)
    assert all(len(plain(x).split())>sum(len(plain(p).split()) for p in re.findall(r'<b>([^<>]+)</b>',x)) for x in selected),('Entire paragraph bolded',number)
    assert all('<b><b>' not in para for para in selected)
    assert '<div class="box tip">' not in main and '<div class="checkpoint">' not in main
    archived=PATH/('dossier-3.2.%s-before-2026-11-28-main-prose-emphasis.html'%number)
    if number in (4,5):
        assert archived.exists(),archived
        assert plain(archived.read_text(encoding='utf-8'))==plain(c),('Unexpected prose mutation',number)
    print(f'PASS 3.2.{number}: {len(selected)}/{len(paragraphs)} ordinary paragraphs have selective exact emphasis; no retired main-body aids',flush=True)

j=json.loads((SRC/'reading_companions.json').read_text(encoding='utf-8'))
for number in (3,4,5):
    c=chapter(number)
    body=c.split('<div class="chapter-body">',1)[1].split('<nav class="chapter-endnav"',1)[0]
    for entry in (x for x in j['companions'] if x['chapter']==f'ch3-2-{number}'):
        candidates=[x for x in re.findall(r'<p>(.*?)</p>',body) if plain(x)==plain(entry['passage'])]
        assert len(candidates)==1,('Missing exact passage',number,entry['id'])
        assert sum(entry['text'] in part for part in re.split(r'<[^>]+>',candidates[0]))==1,('Cue split across emphasis',entry['id'])
print('PASS scoped Companion text nodes, semantic emphasis and 3.2.4/3.2.5 text identity',flush=True)
