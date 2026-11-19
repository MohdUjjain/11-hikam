#!/usr/bin/env python3
"""Dossier 1.1.4 Gutting: source structure, concise layers and unchanged teaching system."""
from __future__ import annotations
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
content = (ROOT / "src/chapters/subtopic-1-1.html").read_text(encoding="utf-8")
begin = content.index('<section class="chapter" id="ch1-1-4"')
end = content.index('<!-- CHAPTER 1.1.5', begin)
chapter = content[begin:end]
body = chapter[chapter.index('<div class="chapter-body">'):chapter.index('<nav class="chapter-endnav"')]
revision = chapter[chapter.index('<div class="end-block">'):]

class CountLayers(HTMLParser):
    aids = {"box", "analogy", "tbl-wrap", "golden-quote", "checkpoint",
            "section-objective", "concept-rel", "hierarchy", "historical-timeline"}
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.counts = {"prose": 0, "aids": 0, "depth": 0}
    def handle_starttag(self, tag, attrs):
        classes = set(dict(attrs).get("class", "").split())
        self.stack.append((tag, "hikam-source-depth-inline" in classes,
                           bool(classes & self.aids)))
    def handle_endtag(self, tag):
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i][0] == tag:
                self.stack = self.stack[:i]
                break
    def handle_data(self, text):
        n = len(re.findall(r"[\w’'-]+", text))
        if any(depth for _, depth, _ in self.stack):
            self.counts["depth"] += n
        elif any(aid for _, _, aid in self.stack):
            self.counts["aids"] += n
        else:
            self.counts["prose"] += n

parser = CountLayers()
parser.feed(body)
counts = parser.counts
assert 650 <= counts["prose"] <= 850, counts
assert 850 <= counts["aids"] <= 1150, counts
assert 1500 <= counts["prose"] + counts["aids"] <= 2000, counts
assert counts["depth"] >= 400, counts
assert 'id="ch1-1-4" style="--hue:268;"' in chapter
assert 'Original author: <strong>Gary Gutting</strong>' in chapter
assert 'Blackwell Companion to Philosophy' in chapter
assert 'Sartre, Foucault and Derrida' in chapter
assert len(re.findall(r'<h3 class="subsec">', body)) == 11
assert body.count('class="hikam-source-depth-inline"') == 9
assert body.count('class="hikam-source-depth-item"') == 9
assert body.count('class="historical-timeline-event"') == 3

# Exact source quotation fragments, with correct scholarly attribution.
for quote in [
    "that it is always of something, but that it itself is not something.",
    "not so much to punish less as to punish better.",
    "The instant of decision is a madness",
]:
    assert quote in unescape(body), f"Source quotation absent: {quote}"
for label in ("Gary Gutting describing Sartre", "Foucault's formulation, quoted by Gutting",
              "Kierkegaard, cited by Derrida and reported by Gutting"):
    assert label in body, f"Quotation attribution absent: {label}"

# No indispensable claim may exist solely in optional Source Depth.
visible = re.sub(r'<details class="hikam-source-depth-inline"[\s\S]*?</details>', "", body)
plain = unescape(re.sub(r"<[^>]+>", " ", visible)).lower()
for term in [
    "intentionality", "being-for-itself", "being-in-itself", "psychological self",
    "nihilation", "pierre", "freedom", "meaning of events", "bad faith",
    "authenticity", "atheism", "summum bonum", "structuralism", "poststructuralism",
    "centrifugal", "madness", "unreason", "moral imprisonment",
    "archaeology", "episteme", "grammar", "genealogy", "knowledge can be objective",
    "discipline", "surveillance", "self-scrutiny", "greek and roman",
    "centripetal", "presence to itself", "logocentrism",
    "opposition", "logical exclusion", "priority", "deconstruction",
    "writing in the soul", "différance", "defer", "law", "justice",
    "new, rational formulation",
]:
    assert term in plain, f"Gutting source-essential topic not visible: {term}"

for klass in [
    "box concept", "box definition", "box highyield", "box mistake",
    "box tip", "analogy", "tbl-wrap", "comparison", "concept-rel",
    "hierarchy", "checkpoint", "golden-quote", "historical-timeline",
]:
    assert f'class="{klass}"' in body or f'class="{klass}"' in chapter, f"Lost study aid: {klass}"

revision_headings = [
    "Chapter Summary", "One-Page Revision Sheet", "Key Definitions",
    "Key Table", "Memory Aids Collected", "Possible Examination Questions"
]
places = [revision.index(label) for label in revision_headings]
assert places == sorted(places), places
for typ in ("Short Answer", "Long Answer", "Comparison", "Conceptual", "Application"):
    assert f'<div class="examq-cat">{typ}</div>' in revision, typ
assert '<table class="comparison">' in revision, "Key Table must be independently usable"

manifest = json.loads((ROOT/"src/reading_companions.json").read_text(encoding="utf-8"))
items = [x for x in manifest["companions"] if x["chapter"] == "ch1-1-4"]
assert len(items) == 12
assert all(x["source"]["author"] == "Gary Gutting" for x in items)
assert all(x.get("simple") and x.get("why_here") and x.get("remember") for x in items)
assert all(all(860 <= n <= 871 for n in x["source"]["printedPages"]) for x in items)
all_sources = "\n".join(p.read_text(encoding="utf-8")
    for p in sorted((ROOT/"src/chapters").glob("subtopic-*.html")))
assert len(re.findall(r'<section class="chapter(?: [^"]+)?" id="ch\d', all_sources)) == 39

print("PASS: Gutting source argument, three exact quotations, eleven subsections,"
      f" 12 contextual cues and nine source records; prose={counts['prose']},"
      f" aids={counts['aids']}, optional depth={counts['depth']} words;"
      " all six revision sections and all 39 chapters retained")
