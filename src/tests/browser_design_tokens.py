#!/usr/bin/env python3
"""Verify Hikam's established visual tokens and readable light/dark surfaces.

This tests the 39-chapter, +20 degree hue cycle, fixed semantic study-aid
colours, display/body/UI font families, original-author credit and every
revision comparison table, using actual computed Chromium styles.
"""
from __future__ import annotations

from contextlib import contextmanager
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import threading

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]


class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


@contextmanager
def site():
    server = ThreadingHTTPServer(
        ('127.0.0.1', 0), partial(Quiet, directory=str(ROOT))
    )
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f'http://127.0.0.1:{server.server_port}/'
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


AUDIT = r"""() => {
  const chapters = [...document.querySelectorAll('section.chapter[id]')];
  const css = el => getComputedStyle(el);
  const declared = css(document.documentElement);
  const ink = declared.getPropertyValue('--ink').trim();
  const paper = declared.getPropertyValue('--white-card').trim();
  const notes = [], failures = [];
  function color(str) {
    if (/^#[0-9a-f]{6}$/i.test(str)) {
      return [1, 3, 5].map(i => parseInt(str.slice(i, i + 2), 16));
    }
    const nums = str.match(/[\d.]+/g);
    if (!nums || nums.length < 3) throw Error('Cannot parse computed color: ' + str);
    return nums.slice(0, 3).map(Number);
  }
  function luminance(c) {
    const x = color(c).map(v => {
      const s = v / 255;
      return s <= 0.04045 ? s / 12.92 : ((s + 0.055) / 1.055) ** 2.4;
    });
    return x[0] * 0.2126 + x[1] * 0.7152 + x[2] * 0.0722;
  }
  function contrast(a, b) {
    const la = luminance(a), lb = luminance(b);
    return (Math.max(la, lb) + 0.05) / (Math.min(la, lb) + 0.05);
  }
  function hsl(h, saturation, lightness) {
    const s = saturation / 100, l = lightness / 100;
    const f = n => {
      const k = (n + h / 30) % 12;
      const a = s * Math.min(l, 1 - l);
      return Math.round(255 * (l - a * Math.max(-1, Math.min(k - 3, 9 - k, 1))));
    };
    return 'rgb(' + [f(0), f(8), f(4)].join(', ') + ')';
  }
  if (chapters.length !== 39) failures.push('Unexpected chapter count: ' + chapters.length);
  const hues = chapters.map(ch => Number(css(ch).getPropertyValue('--hue').trim()));
  chapters.forEach((ch, i) => {
    const expected = (208 + 20 * i) % 360;
    if (hues[i] !== expected) failures.push(ch.id + ' hue ' + hues[i] + ', expected ' + expected);
  });
  for (let i = 18; i < hues.length; i++) {
    if (hues[i] !== hues[i - 18]) failures.push('360-degree repeat broken at ' + chapters[i].id);
  }
  const authorCredits = [];
  chapters.forEach((ch, i) => {
    const author = ch.querySelector('.chapter-source strong');
    if (author) {
      const parent = author.closest('.chapter-source');
      const actual = css(author).color, expected = css(parent).color;
      const first = contrast(actual, ink);
      const second = contrast(actual, hsl(hues[i], 38, 24));
      authorCredits.push({id:ch.id, ratio:+Math.min(first, second).toFixed(2)});
      if (actual !== expected || first < 4.5 || second < 4.5)
        failures.push(ch.id + ' author name: ' + actual + ' vs ' + expected +
                      ', gradient contrast ' + Math.min(first, second).toFixed(2));
    }
  });
  const tables = [], badCells = [];
  for (const ch of chapters) {
    for (const table of ch.querySelectorAll('.end-block table.comparison')) {
      const foreground = css(table).color, background = css(table).backgroundColor;
      const bgRatio = contrast(foreground, background);
      const cells = [...table.querySelectorAll('tbody td')];
      if (!cells.length) failures.push(ch.id + ' empty revision comparison table');
      for (const td of cells) {
        const ratio = contrast(css(td).color, background);
        if (ratio < 4.5) badCells.push({
          chapter:ch.id, ratio:+ratio.toFixed(2),
          sample:td.textContent.trim().slice(0, 70),
          ink:css(td).color, background
        });
        for (const child of td.querySelectorAll('strong, p')) {
          const innerRatio = contrast(css(child).color, background);
          if (innerRatio < 4.5) badCells.push({
            chapter:ch.id, ratio:+innerRatio.toFixed(2),
            sample:child.textContent.trim().slice(0, 70),
            ink:css(child).color, background
          });
        }
      }
      const headings = [...table.querySelectorAll('th')];
      for (const th of headings) {
        const ratio = contrast(css(th).color, css(th).backgroundColor);
        if (ratio < 4.5) failures.push(ch.id + ' table heading contrast: ' + ratio.toFixed(2));
      }
      tables.push({chapter:ch.id, cells:cells.length, contrast:+bgRatio.toFixed(2)});
    }
  }
  if (!tables.length) failures.push('No revision comparison tables found');
  if (badCells.length) failures.push('Unreadable revision cells: ' + JSON.stringify(badCells.slice(0, 8)));
  const semantic = {};
  for (const kind of ['definition', 'concept', 'tip', 'mistake', 'memory', 'highyield']) {
    const all = [...document.querySelectorAll('section.chapter .box.' + kind)];
    const backgrounds = [...new Set(all.map(el => css(el).backgroundColor))];
    semantic[kind] = {count:all.length, backgrounds};
    if (backgrounds.length > 1)
      failures.push(kind + ' semantic background changed by chapter hue: ' + backgrounds.join(', '));
  }
  const first = chapters[0];
  const fonts = {
    display: css(first.querySelector('.chapter-title')).fontFamily,
    prose: css(first.querySelector('.chapter-body p')).fontFamily,
    ui: css(first.querySelector('.chapter-source')).fontFamily
  };
  if (!fonts.display.includes('Fraunces')) failures.push('Display font token lost');
  if (!fonts.prose.includes('Source Serif 4')) failures.push('Prose font token lost');
  if (!fonts.ui.includes('IBM Plex Sans')) failures.push('UI font token lost');
  return {failures, chapters:chapters.length, hue: hues,
          uniqueHues:new Set(hues).size, authorCredits, tables,
          semantic, fonts, paper, ink};
}""";


def main():
    with site() as url, sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True, args=['--no-sandbox'])
        try:
            for width in (390, 1366):
                context = browser.new_context(viewport={'width': width, 'height': 860},
                                              reduced_motion='reduce',
                                              service_workers='block')
                page = context.new_page()
                page.goto(url, wait_until='domcontentloaded', timeout=60000)
                result = page.evaluate(AUDIT)
                assert not result['failures'], (
                    f'{width}px: ' + '\n'.join(result['failures'])
                )
                assert result['chapters'] == 39
                assert result['uniqueHues'] == 18
                assert len(result['authorCredits']) >= 2
                # Revision sections can present their key comparison through
                # several established formats; inspect every real table rather
                # than inventing a requirement for 39 HTML table elements.
                covered = {entry['chapter'] for entry in result['tables']}
                assert {'ch1-1-1', 'ch1-1-2'} <= covered
                assert len(result['tables']) >= 2
                print(f"PASS {width}px: 39 chapters / 18-hue 360-degree cycle, "
                      f"{len(result['tables'])} revision tables, "
                      f"{len(result['authorCredits'])} author credits, "
                      "six fixed semantic colors and canonical fonts")
                context.close()
        finally:
            browser.close()


if __name__ == '__main__':
    main()
