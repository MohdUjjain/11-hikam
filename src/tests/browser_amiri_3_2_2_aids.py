#!/usr/bin/env python3
"""Real Chromium: 3.2.2 moral proof, mobile Arabic RTL, true table axes and A4 printing."""
from __future__ import annotations

from io import BytesIO
from pypdf import PdfReader
from playwright.sync_api import sync_playwright
from browser_quality import ARTIFACTS, context, launch, load, no_errors, site

CHAPTER = "ch3-2-2"

def screen(browser, url):
    for width in (390, 1366):
        ctx = context(browser, width)
        page = load(ctx, url)
        chapter = page.locator("#" + CHAPTER)
        assert chapter.count() == 1
        assert chapter.get_attribute("lang") == "ar"
        assert chapter.evaluate("(e) => getComputedStyle(e).direction") == "rtl"
        assert "--hue:348" in (chapter.get_attribute("style") or "")
        tables = chapter.locator(":scope > .chapter-body .tbl-wrap")
        assert tables.count() == 4, (width, tables.count())
        for i, expected_rows in enumerate((4, 3, 3, 2)):
            wrap = tables.nth(i)
            table = wrap.locator("table.comparison")
            assert table.locator('thead th[scope="col"]').count() == 3
            assert table.locator('tbody th[scope="row"]').count() == expected_rows
            assert wrap.evaluate("(e) => getComputedStyle(e).overflowX") == "auto"
            assert table.evaluate("(e) => getComputedStyle(e).direction") == "rtl"
        for selector, count in (
            (".hierarchy",4), (".box.definition",1), (".box.mistake",1),
            (".box.memory",1), (".box.tip",0), (".concept-rel",1),
            (".analogy",1), (".checkpoint",0), (".box.concept",1),
        ):
            found = chapter.locator(":scope > .chapter-body " + selector).count()
            assert found == count, (selector, width, found)
        assert chapter.locator(":scope > .end-block .endh").count() == 6
        assert chapter.locator(":scope > .end-block .examq-cat").count() == 5
        details = chapter.locator(':scope > .chapter-body details.hikam-source-depth-inline')
        assert details.count() == 5
        assert details.last.get_attribute("data-depth-count") == "2"
        assert details.last.locator('.hikam-source-depth-item').count() == 2
        assert details.last.get_attribute("open") is None
        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth+2"), (
            "Arabic horizontal overflow", width)
        if width == 390:
            tables.first.scroll_into_view_if_needed()
            tables.first.screenshot(path=str(ARTIFACTS / "amiri-322-worldview-rtl-mobile.png"))
            tables.nth(1).scroll_into_view_if_needed()
            tables.nth(1).screenshot(path=str(ARTIFACTS / "amiri-322-moral-objectivity-rtl-mobile.png"))
        no_errors(page, f"Amiri 3.2.2 RTL at {width}px")
        ctx.close()
    print("PASS 3.2.2 authentic Arabic comparisons, semantic aids, grouped no-JS Source Depth and RTL/mobile", flush=True)

def print_a4(browser,url):
    ctx = context(browser,1024)
    page = load(ctx,url)
    original = page.evaluate(
        "Array.from(document.querySelectorAll('section.chapter')).map(e=>e.id)")
    page.evaluate("""() => {
        window.__printControl.setFilter(['ch3-2-2']);
        window.__printControl.includeRevision(true);
        window.dispatchEvent(new Event('beforeprint'));
    }""")
    page.emulate_media(media="print")
    printed = page.locator("#ch3-2-2 > .js-print-page")
    n = printed.count()
    assert n >= 4, n
    over = page.evaluate("""() =>
       [...document.querySelectorAll('#ch3-2-2 > .js-print-page .js-page-content')]
         .map(e=>e.scrollWidth-e.clientWidth)""")
    assert len(over)==n and max(over)<=3,("A4 page horizontal overflow",over)
    assert page.locator("#ch3-2-2 .js-print-page .end-block").count()>=1
    assert page.locator("#ch3-2-2 .js-print-page .hikam-source-depth-inline").count()==0
    data = page.pdf(print_background=True,prefer_css_page_size=True)
    assert data.startswith(b"%PDF") and len(data)>10000
    pdfpages = PdfReader(BytesIO(data)).pages
    assert len(pdfpages)>=n,(len(pdfpages),n)
    (ARTIFACTS/"amiri-322-moral-rtl-a4.pdf").write_bytes(data)
    page.evaluate("window.dispatchEvent(new Event('afterprint'))")
    assert page.locator(".js-print-page").count()==0
    assert page.evaluate(
        "Array.from(document.querySelectorAll('section.chapter')).map(e=>e.id)")==original
    no_errors(page,"Amiri 3.2.2 A4 page restoration")
    ctx.close()
    print(f"PASS 3.2.2 real RTL A4 PDF ({len(pdfpages)} pages); Source Depth excluded, full revision present",flush=True)

def main():
    with site() as url,sync_playwright() as playwright:
        browser=launch(playwright)
        try:
            screen(browser,url)
            print_a4(browser,url)
        finally:
            browser.close()

if __name__=="__main__":
    main()
