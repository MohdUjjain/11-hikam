#!/usr/bin/env python3
"""Papineau 1.1.3 editorial integrity and adopted concise-format regression.

Primary-source judgments are documented separately in the editorial coverage
register; automated checks prevent loss of verified structures/claims.
"""
from __future__ import annotations
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
source = (ROOT / "src/chapters/subtopic-1-1.html").read_text(encoding="utf-8")
begin = source.index('<section class="chapter" id="ch1-1-3"')
end = source.index('<section class="chapter" id="ch1-1-4"', begin)
chapter = source[begin:end]
start_body = chapter.index('<div class="chapter-body">')
end_body = chapter.index('<nav class="chapter-endnav"', start_body)
body = chapter[start_body:end_body]
revision = chapter[chapter.index('<div class="end-block">'):]

class CountLayers(HTMLParser):
    classes = {"box", "analogy", "tbl-wrap", "golden-quote", "checkpoint",
               "section-objective", "concept-rel", "hierarchy"}
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.counts = {"prose":0, "aids":0, "depth":0}
    def handle_starttag(self, tag, attrs):
        props = dict(attrs)
        classes = set(props.get("class", "").split())
        depth = "hikam-source-depth-inline" in classes
        aid = bool(self.classes.intersection(classes))
        self.stack.append((tag, depth, aid))
    def handle_endtag(self, tag):
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i][0] == tag:
                self.stack = self.stack[:i]
                break
    def handle_data(self, text):
        words = re.findall(r"[\w’'-]+", text, flags=re.UNICODE)
        if any(depth for _,depth,_ in self.stack):
            self.counts["depth"] += len(words)
        elif any(aid for _,_,aid in self.stack):
            self.counts["aids"] += len(words)
        else:
            self.counts["prose"] += len(words)

parser = CountLayers()
parser.feed(body)
counts = parser.counts
assert 650 <= counts["prose"] <= 850, f"Prose count outside adopted band: {counts}"
assert 850 <= counts["aids"] <= 1150, f"Aid count outside adopted band: {counts}"
assert 1500 <= counts["prose"] + counts["aids"] <= 2000, counts
assert counts["depth"] > 300, "Further source details not retained"
assert 'id="ch1-1-3" style="--hue:248;"' in chapter
assert 'Original author: <strong>David Papineau</strong>' in chapter
assert 'Blackwell Companion to Philosophy' in chapter
assert "In This Chapter — Two Questions About Science" in chapter
assert len(re.findall(r'<h3 class="subsec">', body)) == 15
assert len(re.findall(r'<details class="hikam-source-depth-inline"', body)) == 9
assert len(re.findall(r' class="hikam-source-depth-item"', body)) == 9

# The three source quotations are exact excerpts from printed pp. 286, 288, 306.
for quote in [
    "The epistemologists wonder whether we should believe what the scientists tell us.",
    "A single contrary example suffices for a conclusive disproof",
    "consequences of those propositions which we should take as axioms",
]:
    assert quote in unescape(body), f"Missing original quotation: {quote}"

# Required source moves must be intelligible before opening optional details.
visible = re.sub(r'<details class="hikam-source-depth-inline"[\s\S]*?</details>', "", body)
visible_plain = unescape(re.sub(r'<[^>]+>', " ", visible)).lower()
for term in [
    "induction", "popper", "bayesian", "positive knowledge", "realists",
    "instrumentalists", "hanson", "kuhn", "feyerabend",
    "underdetermination", "duhem", "meta-induction",
    "naturalized epistemology", "hypothetical prescription",
    "covering-law", "flagpole", "ramsey", "armstrong",
    "causal direction", "reichenbach", "smoking",
    "barometer", "screening off", "propensity",
    "measurement problem", "teleological", "token",
]:
    assert term in visible_plain, f"Source argument not taught visibly: {term}"

# Existing chapter pedagogical formats remain distinct.
for cls in ['box concept', 'box definition', 'box mistake', 'box highyield',
            'box tip', 'analogy', 'tbl-wrap', 'comparison',
            'concept-rel', 'hierarchy', 'checkpoint', 'golden-quote']:
    assert f'class="{cls}"' in body, f"Missing established study aid: {cls}"
revision_heads = [
    "Chapter Summary", "One-Page Revision Sheet", "Key Definitions",
    "Key Table", "Memory Aids Collected", "Possible Examination Questions"
]
positions = [revision.index(s) for s in revision_heads]
assert positions == sorted(positions)
for category in ["Short Answer","Long Answer","Comparison","Conceptual","Application"]:
    assert f'<div class="examq-cat">{category}</div>' in revision
assert '<table class="comparison">' in revision, "Revision Key Table must be independent"
assert 'No Miracles Argument' not in chapter, "Unverified external label remains"

manifest = json.loads((ROOT/"src/reading_companions.json").read_text(encoding="utf-8"))
papineau = [x for x in manifest["companions"] if x["chapter"] == "ch1-1-3"]
assert len(papineau) == 12
assert all(x["source"]["author"] == "David Papineau" for x in papineau)
assert all(all(286 <= p <= 315 for p in x["source"]["printedPages"]) for x in papineau)
all_sources = '\n'.join(p.read_text(encoding="utf-8")
                        for p in sorted((ROOT/"src/chapters").glob("subtopic-*.html")))
assert len(re.findall(r'<section class="chapter(?: [^"]+)?" id="ch\d', all_sources)) == 39

print("PASS: Papineau source structure; 39 chapters; 15 subsections; "
      f"{len(papineau)} contextual cues; prose={counts['prose']}, "
      f"aids={counts['aids']}, optional-depth={counts['depth']} words; "
      "all six revision zones preserved.")
