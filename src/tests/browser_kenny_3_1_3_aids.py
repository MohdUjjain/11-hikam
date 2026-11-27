#!/usr/bin/env python3
"""Chromium screen/print regression for Kenny 3.1.3's source-led study-aid architecture."""
from __future__ import annotations

from io import BytesIO

from playwright.sync_api import sync_playwright
from pypdf import PdfReader

from browser_quality import ARTIFACTS, context, launch, load, no_errors, site

CHAPTER = "ch3-1-3"


def screen(browser, url):
    for width in (390, 1366):
        ctx = context(browser, width)
        page = load(ctx, url)
        chapter = page.locator(f"#{CHAPTER}")
        assert chapter.count() == 1
        wrappers = chapter.locator(":scope > .chapter-body .tbl-wrap")
        assert wrappers.count() == 2, "Two pedagogically genuine comparison tables are expected"
        for index, columns in ((0, 3), (1, 4)):
            wrap = wrappers.nth(index)
            table = wrap.locator("table.comparison")
            assert table.count() == 1
            assert table.locator("caption").count() == 1
            assert table.locator('thead th[scope="col"]').count() == columns
            assert table.locator('tbody th[scope="row"]').count() == 3
            assert wrap.evaluate("(e) => getComputedStyle(e).overflowX") == "auto"
            assert table.evaluate("(e) => Number.parseFloat(getComputedStyle(e).fontSize)") >= 14
        assert chapter.locator(":scope > .chapter-body .concept-rel").count() == 1
        assert chapter.locator(":scope > .chapter-body .hierarchy").count() == 2
        for name, amount in (("mistake", 2), ("memory", 1), ("tip", 1)):
            assert chapter.locator(f":scope > .chapter-body .box.{name}").count() == amount
        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth + 2"), f"Page overflow at {width}px"
        if width == 390:
            wrappers.last.scroll_into_view_if_needed()
            wrappers.last.screenshot(path=str(ARTIFACTS / "kenny-313-comparison-mobile.png"))
        no_errors(page, f"Kenny aid layout at {width}px")
        ctx.close()
    print("PASS Kenny 3.1.3: authentic, scoped comparisons and diverse responsive aids")


def print_dossier(browser, url):
    ctx = context(browser, 1024)
    page = load(ctx, url)
    original_ids = page.evaluate("Array.from(document.querySelectorAll('section.chapter')).map(x=>x.id)")
    page.evaluate("""() => {
        window.__printControl.setFilter(['ch3-1-3']);
        window.__printControl.includeRevision(true);
        window.dispatchEvent(new Event('beforeprint'));
    }""")
    page.emulate_media(media="print")
    pages = page.locator(f"#{CHAPTER} > .js-print-page")
    count = pages.count()
    assert count >= 4, count
    overflows = page.evaluate("""() => [...document.querySelectorAll('#ch3-1-3 > .js-print-page .js-page-content')].map(
      el => ({width: el.scrollWidth-el.clientWidth, height: el.scrollHeight-el.clientHeight}))""")
    assert len(overflows) == count
    assert all(item["width"] <= 3 for item in overflows), ("A4 page horizontal overflow", overflows)
    pdf = page.pdf(print_background=True, prefer_css_page_size=True)
    assert pdf.startswith(b"%PDF") and len(pdf) > 10000
    parsed = PdfReader(BytesIO(pdf))
    assert len(parsed.pages) >= count, (len(parsed.pages), count)
    text = " ".join(" ".join(p.extract_text() or "" for p in parsed.pages).split())
    for term in ("Tragic hero", "Nietzsche", "Plantinga", "Possible Examination Questions"):
        assert term in text, ("Missing in real A4 PDF", term)
    (ARTIFACTS / "kenny-313-pedagogical-aids-A4.pdf").write_bytes(pdf)
    page.evaluate("window.dispatchEvent(new Event('afterprint'))")
    assert page.locator(".js-print-page").count() == 0
    assert page.evaluate("Array.from(document.querySelectorAll('section.chapter')).map(x=>x.id)") == original_ids
    no_errors(page, "Kenny A4 print")
    ctx.close()
    print(f"PASS Kenny 3.1.3: real A4 PDF ({len(parsed.pages)} pages), no horizontal overflow and reversible print")


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
