#!/usr/bin/env python3
"""Targeted real-Chromium checks for 3.2.3 fine-tuning: Arabic tables, Source Depth and A4."""
from __future__ import annotations
from io import BytesIO
from pypdf import PdfReader
from playwright.sync_api import sync_playwright
from browser_quality import ARTIFACTS, context, launch, load, no_errors, site

ID = "ch3-2-3"

def screen(browser, url):
    for width in (390,1366):
        ctx=context(browser,width)
        page=load(ctx,url)
        chapter=page.locator("#"+ID)
        assert chapter.count()==1
        assert chapter.get_attribute("lang")=="ar"
        assert "--hue:8" in (chapter.get_attribute("style") or "")
        assert chapter.evaluate("(e)=>getComputedStyle(e).direction")=="rtl"
        tables=chapter.locator(":scope > .chapter-body .tbl-wrap")
        assert tables.count()==4,(width,tables.count())
        for i,expected_rows in enumerate((3,3,4,3)):
            wrap=tables.nth(i)
            table=wrap.locator("table.comparison")
            assert table.locator('thead th[scope="col"]').count()==3
            assert table.locator('tbody th[scope="row"]').count()==expected_rows,(i,width)
            assert wrap.evaluate("(e)=>getComputedStyle(e).overflowX")=="auto"
            assert table.evaluate("(e)=>getComputedStyle(e).direction")=="rtl"
        for selector,n in ((".hierarchy",3),(".box.mistake",1),
                           (".box.definition",1),(".box.memory",2),
                           (".box.tip",0),(".analogy",1),
                           (".concept-rel",1),(".checkpoint",0)):
            got=chapter.locator(":scope > .chapter-body "+selector).count()
            assert got==n,(selector,width,got)
        details=chapter.locator(":scope > .chapter-body details.hikam-source-depth-inline")
        assert details.count()==5
        assert all(details.nth(i).get_attribute("open") is None for i in range(5))
        assert chapter.locator(":scope > .end-block .endh").count()==6
        assert chapter.locator(":scope > .end-block .examq-cat").count()==5
        assert page.evaluate("document.documentElement.scrollWidth<=innerWidth+2"), width
        if width==390:
            tables.last.scroll_into_view_if_needed()
            tables.last.screenshot(path=str(ARTIFACTS/"amiri-323-water-carbon-mobile-rtl.png"))
        no_errors(page,f"3.2.3 fine-tuning RTL {width}")
        ctx.close()
    print("PASS 3.2.3 scoped mobile/desktop RTL, 4 accessible comparisons and 5 optional Source Depth",flush=True)

def print_a4(browser,url):
    ctx=context(browser,1024)
    page=load(ctx,url)
    ids=page.evaluate("Array.from(document.querySelectorAll('section.chapter')).map(e=>e.id)")
    page.evaluate("""() => {
        window.__printControl.setFilter(['ch3-2-3']);
        window.__printControl.includeRevision(true);
        window.dispatchEvent(new Event('beforeprint'));
    }""")
    page.emulate_media(media="print")
    parts=page.locator("#ch3-2-3 > .js-print-page")
    n=parts.count()
    assert n>=3,n
    overflow=page.evaluate("""() =>
      [...document.querySelectorAll('#ch3-2-3 > .js-print-page .js-page-content')]
      .map(e=>e.scrollWidth-e.clientWidth)""")
    assert len(overflow)==n and max(overflow)<=3,overflow
    assert page.locator("#ch3-2-3 .js-print-page .end-block").count()>=1
    assert page.locator("#ch3-2-3 .js-print-page .hikam-source-depth-inline").count()==0
    data=page.pdf(print_background=True,prefer_css_page_size=True)
    assert data.startswith(b"%PDF") and len(data)>10000
    pages=PdfReader(BytesIO(data)).pages
    assert len(pages)>=n,(len(pages),n)
    (ARTIFACTS/"amiri-323-fine-tuning-a4.pdf").write_bytes(data)
    page.evaluate("window.dispatchEvent(new Event('afterprint'))")
    assert page.locator(".js-print-page").count()==0
    assert page.evaluate("Array.from(document.querySelectorAll('section.chapter')).map(e=>e.id)")==ids
    no_errors(page,"3.2.3 fine-tuning A4 print restoration")
    ctx.close()
    print(f"PASS 3.2.3 real Chromium RTL A4 ({len(pages)} pages), no overflow and no optional depth printed",flush=True)

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
