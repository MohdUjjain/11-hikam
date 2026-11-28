#!/usr/bin/env python3
"""Focused checks for the Arabic source-led Unit 3.2 batch."""
from html.parser import HTMLParser
from hashlib import sha1
import json
import re
from pathlib import Path

SRC = Path(__file__).resolve().parents[1]
MODULE = (SRC / "chapters/subtopic-3-2.html").read_text()
TOC = (SRC / "main.html").read_text()
CUES = json.loads((SRC / "reading_companions.json").read_text())["companions"]
ARCHIVE = SRC / "archive/pre-redevelopment-2026-11-21"
SPEC = {
    1: (328, "سامي عامري", set(range(165, 186)), "a26bbc4b7bea93e810f1cc43875bf64087a9feb3", ("أداء الواجبات", "المقتطف هناك", "علم حصولي")),
    2: (348, "سامي عامري", set(range(221, 263)), "05249cfd2c67cac97204d426a82f719a69ba20b7", ("الاعتراض البيولوجي", "آخر صفحة", "فرانك تورك")),
    3: (8, "سامي عامري", {441, *range(443, 462)}, "fcedc9256c33f26c8034fc27fe3799063dec84d7", ("الضرورة المادية أو الصدفة أو الحكمة", "بنروز", "دينتون")),
    4: (28, "عبد الله بن صالح العجيري", set(range(95, 120)), "d278e05012c13fe7d59a40896af1ba431fe77646", ("أولية كوننا", "ابن حزم", "التعادل الحراري")),
    5: (48, "هشام عزمي", {*range(14, 36), *range(91, 98)}, "2b03c83ef8fa35078655c1dee6bec9708c1a37f3", ("مواقف نهائية من القضية", "القابلية والتأزم", "مرجّحات خارجية")),
    6: (68, "محمد باقر السيستاني", {*range(5, 57), *range(59, 71)}, "5b46e8fb8930fd6fe37145e0843db114e43bbb78", ("تفسير المجموع", "إنضاج الموقف", "لمجرد التباسها")),
}
AIDS = set("box checkpoint comparison tbl-wrap section-objective golden-quote hierarchy analogy concept-rel historical-timeline".split())
DEPTH = re.compile(r'<details class="hikam-source-depth-inline"[^>]*>[\s\S]*?</details>')

class Words(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.count = [], [0, 0]

    def handle_starttag(self, tag, attrs):
        if tag not in {"br", "hr", "img", "input"}:
            self.stack.append((tag, bool(AIDS & set(dict(attrs).get("class", "").split()))))

    def handle_endtag(self, tag):
        for i in reversed(range(len(self.stack))):
            if self.stack[i][0] == tag:
                self.stack = self.stack[:i]
                break

    def handle_data(self, data):
        self.count[any(flag for _, flag in self.stack)] += len(data.split())

for n, (hue, author, pages, pinned, anchors) in SPEC.items():
    key = f"ch3-2-{n}"
    opening = f'<section class="chapter rtl" id="{key}" lang="ar" style="--hue:{hue};">'
    assert MODULE.count(opening) == 1
    chap = MODULE[MODULE.index(opening):].split("\n</section>", 1)[0]
    old = (ARCHIVE / f"dossier-3.2.{n}.html").read_bytes()
    assert sha1(f"blob {len(old)}\0".encode() + old).hexdigest() == pinned
    assert author in chap and re.search(r'<strong>' + author + r'</strong>', chap)
    assert author in next(line for line in TOC.splitlines() if f'href="#{key}"' in line)
    assert chap.count('class="endh"') == 6 and chap.count('class="examq-cat"') == 5
    assert f'href="#ch3-2-{n+1}"' in chap
    body = chap.split('<div class="chapter-body">', 1)[1].split('<nav class="chapter-endnav"', 1)[0]
    visible = DEPTH.sub("", body)
    assert all(anchor in visible for anchor in anchors)
    for c in re.findall(r'class="((?:box |hierarchy|analogy|golden-quote|concept-rel|checkpoint)[^"]*)"', old.decode().split('<nav class="chapter-endnav"')[0]):
        assert f'class="{c}"' in visible, (key, c)
    w = Words()
    w.feed(visible)
    p, a = w.count
    assert 650 <= p <= 850 and 850 <= a <= 1150 and 1500 <= p+a <= 2000, (key, w.count)
    cues = [c for c in CUES if c["chapter"] == key]
    records = list(DEPTH.finditer(body))
    if n == 4:
        # Contextual cues and optional source expansions have distinct jobs.
        # The source-led second pass selects them independently, not in pairs.
        assert len(cues) == 7 and len(records) == 11
    elif n == 5:
        # 3.2.5 also selects local clarification and optional expansion independently.
        # Exact anchor, record and source contracts are in its dedicated scoped test.
        assert cues and records
        assert "لا يضم الدرس ص 36–90" in chap
    else:
        assert len(cues) == len(records) == (6 if n == 6 else 5)
    for c in cues:
        required = ("simple", "why_here", "remember") if n == 5 else ("simple", "why_here", "remember", "sourceDepthId")
        assert all(c.get(k) for k in required)
        assert c["source"]["author"] == author and set(c["source"]["printedPages"]) <= pages
        if n == 5 and not c.get("sourceDepthId"):
            continue
        r = next(x for x in records if c["sourceDepthId"] in x[0])
        assert " open" not in r[0].split(">", 1)[0] and author in r[0]
        pstart = body.rfind("<p>", 0, r.start())
        assert c["text"] in body[pstart:r.start()] and body[:r.start()].rstrip().endswith("</p>")
    print(f"PASS {key}: scoped content, Arabic RTL, {len(cues)} Companions/Depth, 6 revisions, 5 exam classes; {w.count} visible words")
