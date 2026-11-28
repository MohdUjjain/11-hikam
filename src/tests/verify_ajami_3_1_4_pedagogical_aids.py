#!/usr/bin/env python3
"""Ajami 3.1.4: source-preserving Arabic pedagogy, semantic tables and pinned predecessor."""
from __future__ import annotations

import hashlib
import json
import re
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

SRC = Path(__file__).resolve().parents[1]
chapter_file = (SRC / "chapters/subtopic-3-1.html").read_text(encoding="utf-8")
start_tag = '<section class="chapter rtl" id="ch3-1-4" lang="ar" style="--hue:288;">'
assert chapter_file.count(start_tag) == 1
chapter_start = chapter_file.index(start_tag)
chapter_end = chapter_file.index("\n</section>", chapter_start) + len("\n</section>")
chapter = chapter_file[chapter_start:chapter_end]
assert chapter.count('class="endh"') == 6
assert chapter.count('class="examq-cat"') == 5
assert 'href="#ch3-1-5"' in chapter
assert '<h1 class="chapter-title">نظريات حول نشوء الدين: دراسة تحليلية نقدية</h1>' in chapter
assert "سامر توفيق عجمي" in chapter

historic_path = SRC / "archive/pre-redevelopment-2026-11-21/dossier-3.1.4-before-2026-11-28-pedagogical-rework.html"
historic = historic_path.read_bytes()
sha = hashlib.sha1(b"blob " + str(len(historic)).encode() + b"\0" + historic).hexdigest()
assert sha == "ce82a1403643f4d17443377eb57400eed5404fc1", sha
old = historic.decode("utf-8")
assert old.startswith(start_tag) and old.endswith("</section>")
assert old.count('class="endh"') == 6
assert old.count('class="examq-cat"') == 5
assert old.count('<table class="comparison">') == 6, "Complete five-table predecessor and revision must be archived"
assert old.count('<details class="hikam-source-depth-inline"') == 5

source_depth = r'<details class="hikam-source-depth-inline"[\s\S]*?</details>'
def main_body(section: str) -> str:
    body = section.split('<div class="chapter-body">', 1)[1].split('<nav class="chapter-endnav"', 1)[0]
    return re.sub(source_depth, "", body)

body = chapter.split('<div class="chapter-body">', 1)[1].split('<nav class="chapter-endnav"', 1)[0]
depths = re.findall(source_depth, body)
assert len(depths) == 5
assert all("سامر توفيق عجمي" in x and " open" not in x.split(">", 1)[0] for x in depths)
assert body.count('class="hikam-source-depth-item"') == 5
visible = main_body(chapter)
original_visible = main_body(old)

AIDS = {"box", "tbl-wrap", "golden-quote", "section-objective", "hierarchy",
        "concept-rel", "checkpoint", "analogy"}
class TextOutsideAids(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack: list[tuple[str, bool]] = []
        self.text: list[str] = []
    def handle_starttag(self, tag, attrs):
        if tag not in {"br", "hr", "img", "input", "meta", "link"}:
            self.stack.append((tag, bool(AIDS & set(dict(attrs).get("class", "").split()))))
    def handle_endtag(self, tag):
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i][0] == tag:
                self.stack = self.stack[:i]
                return
    def handle_data(self, value):
        if not any(flag for _, flag in self.stack) and value.strip():
            self.text.append(value)

def prose_text(fragment: str) -> str:
    collector = TextOutsideAids()
    collector.feed(fragment)
    return " ".join(" ".join(collector.text).split())

assert prose_text(visible) == prose_text(original_visible), "Ajami's visible intellectual prose changed unexpectedly"

# Chapter-specific learning operations, not a universal prescribed quota.
assert visible.count('<table class="comparison">') == 3
assert visible.count('<div class="hierarchy">') == 2
assert visible.count('<div class="concept-rel">') == 1
assert visible.count('<div class="box mistake">') == 2
assert visible.count('<div class="box memory">') == 2
assert visible.count('<div class="box tip">') == 1
assert visible.count('<div class="box definition">') == 1
assert visible.count('<div class="box highyield">') == 0
assert visible.count('<div class="section-objective">') == 5
assert visible.count('<div class="checkpoint">') == 1
for title in (
    "فحوص ثلاثة قبل تعميم تفسير نشوء الدين",
    "مراحل كونت الثلاث: ما الذي يحلّ محلّ ماذا؟",
    "مثال النار والماء: مستويان من الإسناد",
    "كيف يناقش عجمي دعوى أن الخوف أصل الدين؟",
    "فويرباخ وعجمي: المقدّمة المشتركة والنتيجة المختلفة",
    "صورتا التفسير الطبقي: من أين يأتي العزاء الديني؟",
    "مفتاح الاستذكار — استعمال، عزاء، منشأ",
    "تمييز مفهومي — القابلية والفعلية",
):
    assert title in visible, title
assert "وجه النظر</th><th>بيانه في القراءة" not in visible
tables = re.findall(r'<table class="comparison">[\s\S]*?</table>', visible)
assert len(tables) == 3
for table in tables:
    assert "<caption>" in table
    assert table.count('scope="col"') == 3
    assert table.count('scope="row"') == 3
assert 'rowspan="3"' in tables[0], "Comte critique spans all three stages"
assert '<div class="end-block">' in chapter
revision_table = re.findall(r'<table class="comparison">[\s\S]*?</table>', chapter.split('<div class="end-block">', 1)[1])
assert len(revision_table) == 1
assert revision_table[0].count('scope="col"') == 3
assert revision_table[0].count('scope="row"') == 3
for term in ("اللاهوتية", "الميتافيزيقية", "الوضعية", "علية طولية", "العلة التامة", "ماركس"):
    assert term in visible, term

manifest = json.loads((SRC / "reading_companions.json").read_text(encoding="utf-8"))["companions"]
companions = [entry for entry in manifest if entry["chapter"] == "ch3-1-4"]
assert len(companions) == 5 and len({entry["id"] for entry in companions}) == 5
paragraphs = [
    " ".join(unescape(re.sub(r"<[^>]+>", "", p)).split())
    for p in re.findall(r"<p(?:\s[^>]*)?>([\s\S]*?)</p>", visible)
]
for entry in companions:
    assert entry["source"]["author"] == "سامر توفيق عجمي", entry["id"]
    assert all(19 <= p <= 46 for p in entry["source"]["printedPages"]), entry["id"]
    assert entry["passage"].count(entry["text"]) == 1, entry["id"]
    assert sum(p == entry["passage"] for p in paragraphs) == 1, entry["id"]
    assert all(entry.get(field) for field in ("explanation", "simple", "remember", "added_value")), entry["id"]

audit = (SRC / "docs/editorial/READINGS_3_1_4_3_1_5_ARABIC_SOURCE_COVERAGE.md").read_text(encoding="utf-8")
assert "104 nonempty paragraphs" in audit and "printed pp. 19–46" in audit
assert "ce82a1403643f4d17443377eb57400eed5404fc1" in audit
assert "Feuerbach/Ajami matrix" in audit
assert "3.1.5" in audit
print("PASS Ajami 3.1.4: original intellectual prose unchanged; five exact cues, five depth records, three real comparisons, diverse Arabic teaching aids, both archival stages and six revision sections")
