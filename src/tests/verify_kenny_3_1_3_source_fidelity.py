#!/usr/bin/env python3
"""Regress the source-led Anthony Kenny 'God' dossier and its preserved predecessor."""
from __future__ import annotations

import hashlib
import json
import re
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
fragment = (SRC / "chapters/subtopic-3-1.html").read_text(encoding="utf-8")
start = fragment.index('<section class="chapter" id="ch3-1-3"')
end = fragment.index("\n</section>", start) + len("\n</section>")
chapter = fragment[start:end]
assert fragment.count('id="ch3-1-3"') == 1
assert chapter.startswith('<section class="chapter" id="ch3-1-3" style="--hue:268;">')
assert 'Anthony Kenny' in chapter and 'Philosophy in the Modern World' in chapter
assert 'pp. 294 and 300 absent' in chapter
assert chapter.count('<h2 class="endh">') == 6
assert chapter.count('class="examq-cat"') == 5
for kind in ('Short Answer', 'Long Answer', 'Comparison', 'Conceptual', 'Application'):
    assert f'<div class="examq-cat">{kind}</div>' in chapter
assert chapter.count('class="end-block"') == 1
assert 'href="#ch3-1-4"' in chapter

archive_path = SRC / "archive/pre-redevelopment-2026-11-21/dossier-3.1.3-before-2026-11-27-refinement.html"
archive = archive_path.read_bytes()
blob = hashlib.sha1(b"blob " + str(len(archive)).encode() + b"\0" + archive).hexdigest()
assert blob == "783ef089b31252a077dd5257fae81d7501ec8a61", blob
assert archive.startswith(b'<section class="chapter" id="ch3-1-3"')
assert archive.count(b'<h2 class="endh">') == 6
assert archive.endswith(b'</section>\n')
assert b'Kierkegaard also gives <strong>three reasons</strong>' not in archive


# Second, independent preservation point: the published source-refined edition
# as it existed before this pedagogical pass, including every existing aid.
prior_aid_archive = (SRC / "archive/pre-redevelopment-2026-11-21/dossier-3.1.3-before-2026-11-27-pedagogical-rework.html").read_bytes()
aid_blob = hashlib.sha1(b"blob " + str(len(prior_aid_archive)).encode() + b"\0" + prior_aid_archive).hexdigest()
assert aid_blob == "a43c12574a1843c9a74f9fa57765a342e6ccedc6", aid_blob
assert prior_aid_archive.startswith(b'<section class="chapter" id="ch3-1-3"')
assert prior_aid_archive.endswith(b"</section>")
assert prior_aid_archive.count(b'<h2 class="endh">') == 6
assert prior_aid_archive.count(b'<table class="comparison">') == 6  # five main-body + one revision
assert b"What Kenny" in prior_aid_archive

body = chapter.split('<div class="chapter-body">', 1)[1].split('<nav class="chapter-endnav"', 1)[0]
depth = list(re.finditer(r'<details class="hikam-source-depth-inline"[\s\S]*?</details>', body))
assert len(depth) == 7
assert body.count('class="hikam-source-depth-item"') == 7
assert body.count('class="hikam-source-depth-citation"') == 7
for d in depth:
    assert body[:d.start()].rstrip().endswith("</p>")
    assert " open" not in d.group().split(">", 1)[0]
    assert "Anthony Kenny" in d.group()
visible = re.sub(r'<details class="hikam-source-depth-inline"[\s\S]*?</details>', "", body)
# Source-dependent teaching operations, not an arbitrary chapter template.
assert visible.count('<table class="comparison">') == 2
assert visible.count('<div class="hierarchy">') == 2
assert visible.count('<div class="concept-rel">') == 1
assert visible.count('<div class="box mistake">') == 2
assert visible.count('<div class="box memory">') == 1
assert visible.count('<div class="box tip">') == 1
assert all(phrase in visible for phrase in (
    "How Hegel’s account draws opposing responses",
    "Two standpoints on a sacrifice",
    "Levels of explanation — what selection presupposes",
    "Three different examinations of religious belief",
    "Plantinga’s modal inference — locate the indispensable premise",
    "Common Mistake — Private Conviction Is Not a Public Criterion",
    "Examination Method — Separate Two Objections",
    "Memory Aid — Three Questions, Three Tests",
))
assert "What Kenny’s account distinguishes" not in visible
assert "Four questions not to collapse into one" not in visible
main_tables = re.findall(r'<table class="comparison">[\s\S]*?</table>', visible)
for table in main_tables:
    assert "<caption>" in table
    assert table.count('scope="col"') >= 3
    assert table.count('scope="row"') >= 3
assert '<h2 class="endh">Key Table</h2>' in chapter
endblock = chapter.split('<div class="end-block">', 1)[1]
assert 'Questions at distinct levels' in endblock
assert endblock.count('scope="row"') == 3


required = (
    "Hegel", "Feuerbach", "Marx", "Kierkegaard", "three reasons",
    "historical research yields probability", "Mill", "some evidential weight",
    "special creation", "selection among breeding populations",
    "rather than nothing", "why it came into existence", "monotheistic religion",
    "revealed by God", "antecedent", "emotional colouring of conscience",
    "Frege", "Nietzsche", "qualified defence", "pragmatist test",
    "wish-shaped illusion", "primal father", "Wittgenstein", "Ayer",
    "maximal greatness", "possible worlds", "possibility premise"
)
plain = " ".join(unescape(re.sub(r"<[^>]+>", " ", visible)).split())
for claim in required:
    assert claim.casefold() in plain.casefold(), claim

AIDS = {"box", "section-objective", "tbl-wrap", "hierarchy", "checkpoint",
        "concept-rel", "analogy", "golden-quote"}
class WordPool(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.words = {"prose": 0, "aids": 0}
    def handle_starttag(self, tag, attrs):
        if tag not in {"br", "hr", "img", "input", "meta", "link"}:
            self.tags.append((tag, bool(set(dict(attrs).get("class", "").split()) & AIDS)))
    def handle_endtag(self, tag):
        for i in range(len(self.tags)-1, -1, -1):
            if self.tags[i][0] == tag:
                self.tags = self.tags[:i]
                return
    def handle_data(self, value):
        n = len(re.findall(r"[^\W_]+(?:['’\-][^\W_]+)*", value, re.UNICODE))
        self.words["aids" if any(flag for _,flag in self.tags) else "prose"] += n

wc = WordPool()
wc.feed(visible)
counts = wc.words
assert 650 <= counts["prose"] <= 950, counts
assert 850 <= counts["aids"] <= 1150, counts
assert 1500 <= sum(counts.values()) <= 2000, counts

manifest = json.loads((SRC / "reading_companions.json").read_text(encoding="utf-8"))
companions = [c for c in manifest["companions"] if c["chapter"] == "ch3-1-3"]
assert len(companions) == 10 and len({c["id"] for c in companions}) == 10
paragraphs = [
    " ".join(unescape(re.sub(r"<[^>]+>", "", raw)).split())
    for raw in re.findall(r"<p(?:\s[^>]*)?>([\s\S]*?)</p>", visible)
]
for c in companions:
    assert c["source"]["author"] == "Anthony Kenny" and c["source"]["printedPages"]
    assert all(291 <= page <= 318 and page not in (294, 300)
               for page in c["source"]["printedPages"])
    assert all(c.get(key) for key in ("explanation", "simple", "why_here", "remember", "added_value"))
    assert c["passage"].count(c["text"]) == 1, c["id"]
    assert sum(p == c["passage"] for p in paragraphs) == 1, c["id"]

audit = (SRC / "docs/editorial/READING_3_1_3_KENNY_GOD_SOURCE_COVERAGE.md").read_text(encoding="utf-8")
ledger = [int(x) for x in re.findall(r"^\| (\d+) \|", audit, re.M)]
assert ledger == list(range(1, 27)), ledger
assert "**Absent from the supplied PDF.**" in audit
assert "783ef089b31252a077dd5257fae81d7501ec8a61" in audit
print("PASS: Kenny 3.1.3 source, both pinned editions, diverse source-led aids, semantic comparisons, 10 companions, 7 local depth records and six revisions:", counts)
