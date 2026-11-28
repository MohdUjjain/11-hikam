#!/usr/bin/env python3
"""Real Chromium RTL/mobile/semantic table and A4 print audit for Ajami 3.1.4."""
from __future__ import annotations

from io import BytesIO

from pypdf import PdfReader
from playwright.sync_api import sync_playwright

from browser_quality import ARTIFACTS, context, launch, load, no_errors, site

IDENT = "ch3-1-4"


def screen(browser, url):
    for width in (390, 1366):
        ctx = context(browser, width)
        page = load(ctx, url)
        chapter = page.locator("#" + IDENT)
        assert chapter.count() == 1
        assert chapter.get_attribute("lang") == "ar"
        assert chapter.evaluate("(e) => getComputedStyle(e).direction") == "rtl"
        tables = chapter.locator(":scope > .chapter-body .tbl-wrap")
        assert tables.count() == 3, (width, tables.count())
        for i in range(3):
            wrap = tables.nth(i)
            table = wrap.locator("table.comparison")
            assert table.locator("caption").count() == 1
            assert table.locator('thead th[scope="col"]').count() == 3
            assert table.locator('tbody th[scope="row"]').count() == 3
            assert wrap.evaluate("(e) => getComputedStyle(e).overflowX") == "auto"
            assert table.evaluate("(e) => getComputedStyle(e).direction") == "rtl"
        assert tables.first.locator('tbody td[rowspan="3"]').count() == 1
        for selector, count in (
            (".hierarchy", 2), (".concept-rel", 1),
            (".box.mistake", 2), (".box.memory", 2),
            (".box.tip", 1), (".box.definition", 1),
        ):
            assert chapter.locator(":scope > .chapter-body " + selector).count() == count, selector
        assert chapter.locator(":scope > .end-block .examq-cat").count() == 5
        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth+2"), (
            "Arabic chapter causes horizontal page overflow", width)
        if width == 390:
            tables.last.scroll_into_view_if_needed()
            tables.last.screenshot(path=str(ARTIFACTS / "ajami-314-marx-comparison-mobile.png"))
        no_errors(page, f"Ajami RTL screen {width}px")
        ctx.close()
    print("PASS Ajami 3.1.4 semantic RTL comparisons, new aids and mobile layout", flush=True)


def print_dossier(browser, url):
    ctx = context(browser, 1024)
    page = load(ctx, url)
    original = page.evaluate(
        "Array.from(document.querySelectorAll('section.chapter')).map(e => e.id)")
    page.evaluate("""() => {
      window.__printControl.setFilter(['ch3-1-4']);
      window.__printControl.includeRevision(true);
      window.dispatchEvent(new Event('beforeprint'));
    }""")
    page.emulate_media(media="print")
    sheets = page.locator(f"#{IDENT} > .js-print-page")
    expected = sheets.count()
    assert expected >= 4, expected
    overflow = page.evaluate("""() =>
      [...document.querySelectorAll('#ch3-1-4 > .js-print-page .js-page-content')]
        .map(e => e.scrollWidth - e.clientWidth)""")
    assert len(overflow) == expected
    assert max(overflow) <= 3, ("A4 page horizontal overflow", overflow)
    assert page.locator(f"#{IDENT} .js-print-page .end-block, #{IDENT} .js-print-page .revision-sheet").count() >= 1
    pdf = page.pdf(print_background=True, prefer_css_page_size=True)
    assert pdf.startswith(b"%PDF") and len(pdf) > 10000
    pages = PdfReader(BytesIO(pdf)).pages
    assert len(pages) >= expected, (len(pages), expected)
    (ARTIFACTS / "ajami-314-rtl-a4.pdf").write_bytes(pdf)
    page.evaluate("window.dispatchEvent(new Event('afterprint'))")
    assert page.locator(".js-print-page").count() == 0
    assert page.evaluate(
        "Array.from(document.querySelectorAll('section.chapter')).map(e => e.id)") == original
    no_errors(page, "Ajami A4 print")
    ctx.close()
    print(f"PASS Ajami RTL A4 PDF ({len(pages)} pages), no overflow and print restore", flush=True)


def main():
    with site() as url, sync_playwright() as playwright:
        browser = launch(playwright)
        try:
            screen(browser, url)
            print_dossier(browser, url)
        finally:
            browser.close()


if __name__ == "__main__":
    main()
