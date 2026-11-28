#!/usr/bin/env python3
"""3.2.2 Samy Ameri: primary-source distinctions, aid semantics, unchanged anchors & archives."""
from __future__ import annotations

from hashlib import sha1
from html.parser import HTMLParser
from html import unescape
import json
import re
from pathlib import Path

SRC = Path(__file__).resolve().parents[1]
module = (SRC / "chapters/subtopic-3-2.html").read_text(encoding="utf-8")
opening = '<section class="chapter rtl" id="ch3-2-2" lang="ar" style="--hue:348;">'
assert module.count(opening) == 1
ch = module[module.index(opening):].split("\n</section>", 1)[0]
body = ch.split('<div class="chapter-body">', 1)[1].split('<nav class="chapter-endnav"', 1)[0]
depth_regex = r'<details class="hikam-source-depth-inline"[^>]*>[\s\S]*?</details>'
visible = re.sub(depth_regex, "", body)
front = ch.split('<div class="chapter-body">', 1)[0]
assert "سامي عامري" in front and '<h1 class="chapter-title">البرهان الأخلاقي</h1>' in front
assert 'href="#ch3-2-3"' in ch
assert ch.count('class="endh"') == 6 and ch.count('class="examq-cat"') == 5
assert ch.count('class="sec"') == 5
assert len(re.findall(depth_regex, body)) == 5

archive = SRC / 'archive/pre-redevelopment-2026-11-21/dossier-3.2.2-before-2026-11-28-pedagogical-rework.html'
old = archive.read_bytes()
blob = sha1(f"blob {len(old)}\0".encode() + old).hexdigest()
assert blob == '79cd9e6cd383eeb33c238bc5a9c843d9996e95b9', blob
original = SRC / 'archive/pre-redevelopment-2026-11-21/dossier-3.2.2.html'
oldest = original.read_bytes()
assert sha1(f"blob {len(oldest)}\0".encode() + oldest).hexdigest() == '05249cfd2c67cac97204d426a82f719a69ba20b7'
assert old.decode("utf-8").count('class="comparison"') == 6
assert old.decode("utf-8").count('class="endh"') == 6
assert (SRC / 'docs/editorial/READING_3_2_2_AMERI_MORAL_SOURCE_PEDAGOGY_AUDIT.md').exists()

AIDS = set('box checkpoint comparison tbl-wrap section-objective golden-quote hierarchy analogy concept-rel'.split())
class Words(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.count = [], [0, 0]
    def handle_starttag(self, tag, attrs):
        if tag not in {'hr', 'br', 'img', 'input', 'meta', 'link'}:
            self.stack.append((tag, bool(AIDS.intersection(dict(attrs).get('class','').split()))))
    def handle_endtag(self, tag):
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i][0] == tag:
                self.stack = self.stack[:i]
                break
    def handle_data(self, data):
        self.count[int(any(flag for _, flag in self.stack))] += len(data.split())

words = Words()
words.feed(visible)
p, a = words.count
assert 650 <= p <= 850, words.count
assert 850 <= a <= 1150, words.count
assert 1500 <= p + a <= 2000, words.count

assert visible.count('class="comparison"') == 4
assert ch.count('class="comparison"') == 5  # four main + independent revision key table
assert visible.count('scope="col"') == 12
assert visible.count('scope="row"') == 12
assert visible.count('class="hierarchy"') == 4
assert visible.count('class="box definition"') == 1
assert visible.count('class="box concept"') == 1
assert visible.count('class="box mistake"') == 1
assert visible.count('class="box memory"') == 1
assert visible.count('class="box tip"') == 0
assert visible.count('class="analogy"') == 1
assert visible.count('class="concept-rel"') == 1
assert visible.count('class="checkpoint"') == 0

# Seven distinct intellectual nodes of this specific reading, not artificial checklist fillers.
for required in (
    'الصيغة التفصيلية: خمس حلقات', 'الموضوعية والإطلاقية',
    'مصدر شخصي', 'كاي نيلسون',
    'العدمية: ليست شكًا', 'الأنطولوجيا', 'الإبستيمولوجيا',
    'روزنبرغ', 'ماكي', 'داوكنز', 'سي. إس. لويس',
    'شون كارول', 'العواقبية', 'أخلاق الواجب',
    'مايكل روس', 'الاعتراض البيولوجي', 'ص 262',
    'ثلاثة افتراضات', 'الوحي', 'الترغيب', 'التحذير',
):
    assert required in visible, (required, words.count)
assert 'لا يكون «صالحًا» داخل منظومة مادية' in visible
assert 'ما الذي لا يُستغنى به عنه؟' in ch
assert 'الإطلاقية' in ch.split('<div class="end-block">', 1)[1]

cues = [x for x in json.loads((SRC / "reading_companions.json").read_text(encoding="utf-8"))["companions"]
        if x["chapter"] == "ch3-2-2"]
assert len(cues) == 5
recs = re.findall(depth_regex, body)
for cue in cues:
    # Bold markup may divide the HTML text without changing its exact passage.
    def plain(fragment):
        return ' '.join(unescape(re.sub(r'<[^>]+>', '', fragment)).split())
    paragraphs = re.findall(r'<p>([\s\S]*?)</p>', visible)
    matches = [p for p in paragraphs if plain(p) == plain(cue["passage"])]
    assert len(matches) == 1, (cue["id"], len(matches))
    pieces = re.split(r'<[^>]+>', matches[0])
    assert sum(cue["text"] in piece for piece in pieces) == 1, cue["id"]
    assert cue["text"] in cue["passage"], cue["id"]
    assert all(cue.get(k) for k in ("simple","why_here","remember","sourceDepthId"))
    assert cue["source"]["author"] == "سامي عامري"
    assert all(221 <= page <= 262 for page in cue["source"]["printedPages"])
    related = [r for r in recs if cue["sourceDepthId"] in r]
    assert len(related) == 1, cue["id"]
    r = related[0]
    assert " open" not in r.split('>',1)[0]
    assert "سامي عامري" in r and "<summary>" in r
    preceding = body[:body.index(r)].rstrip()
    assert preceding.endswith("</p>"), cue["id"]
    assert cue["text"] in preceding[preceding.rfind("<p>"):], cue["id"]

grouped = next(r for r in recs if 'source-depth-h322-welfare' in r)
assert 'data-depth-count="2"' in grouped.split('>',1)[0]
assert grouped.count('class="hikam-source-depth-item"') == 2
assert 'ص 259–261' in grouped and 'ص 262' in grouped
assert 'source-depth-h322-biology-opening' in grouped
print(f"PASS 3.2.2: {p} prose + {a} aids = {p+a} visible; four true comparisons, four argument/witness structures, five exact Companions, source Depth grouped by page, original archived and six revision sections", flush=True)
