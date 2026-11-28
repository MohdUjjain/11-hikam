#!/usr/bin/env python3
"""Only 3.2.5: real Arabic reading, contextual access and complete A4 printing."""
from __future__ import annotations

from io import BytesIO
from pathlib import Path
import json
import unicodedata

from pypdf import PdfReader
from playwright.sync_api import sync_playwright
from browser_quality import ARTIFACTS, context, launch, load, no_errors, site

ID = 'ch3-2-5'
SRC = Path(__file__).resolve().parents[1]
CUES = [c for c in json.loads((SRC / 'reading_companions.json').read_text(encoding='utf-8'))['companions'] if c['chapter'] == ID]
TITLE_STAMP_AUDIT = r'''root => {
  const stamp=root.querySelector('.chapter-stamp'), rects=[];
  for(const selector of ['.chapter-title','.chapter-source']) {
    const walker=document.createTreeWalker(root.querySelector(selector),NodeFilter.SHOW_TEXT);
    while(walker.nextNode()) {
      if(!walker.currentNode.textContent.trim()) continue;
      const range=document.createRange(); range.selectNodeContents(walker.currentNode);
      for(const r of range.getClientRects()) if(r.width && r.height)
        rects.push({selector,left:r.left,right:r.right,top:r.top,bottom:r.bottom});
    }
  }
  const s=stamp.getBoundingClientRect(), style=getComputedStyle(stamp);
  const visible=style.display!=='none' && style.visibility!=='hidden' && s.width>0 && s.height>0;
  return {stampVisible:visible,
    titleTextRects:rects.filter(r=>r.selector==='.chapter-title').length,
    sourceTextRects:rects.filter(r=>r.selector==='.chapter-source').length,
    overlaps:visible ? rects.filter(r=>
    Math.min(r.right,s.right)-Math.max(r.left,s.left)>1 &&
    Math.min(r.bottom,s.bottom)-Math.max(r.top,s.top)>1) : []};
}'''


def screen(browser, url):
    for width in (390, 1366):
        ctx = context(browser, width)
        page = load(ctx, url)
        chapter = page.locator('#'+ID)
        assert chapter.get_attribute('lang') == 'ar'
        assert chapter.get_attribute('style') == '--hue:48;'
        assert chapter.evaluate('(e)=>getComputedStyle(e).direction') == 'rtl'
        title_stamp = chapter.evaluate(TITLE_STAMP_AUDIT)
        assert title_stamp['titleTextRects'] and title_stamp['sourceTextRects'] and not title_stamp['overlaps'], ('Title and citation text must clear the visible stamp', width, title_stamp)
        # Match the actual shared component contracts. Narrative, table cells,
        # hierarchy values, revision content and local source prose inherit the
        # Arabic stacks. Existing chrome has explicit sans/display stacks; a
        # chapter-only editorial pass must not redefine those shared selectors.
        fonts = chapter.evaluate(r'''(root) => {
          const norm=s=>s.split(',').map(x=>x.trim().replace(/['"]/g,'').toLowerCase()).join(',');
          const style=getComputedStyle(root);
          const token=n=>norm(style.getPropertyValue(n));
          const arabic=[token('--font-arabic'),token('--font-arabic-sans')];
          const chrome=[
            ['.box-label .ico','--font-display'],
            ['.chapter-stamp, .toc-back, .chapter-source, .chapter-endnav .endnav-btn, .hikam-source-depth-mini, .hikam-source-depth-hint, .hikam-source-depth-item h4, .historical-timeline-title, .historical-timeline-date','--font-sans']
          ];
          const report={readingNodes:0,chromeNodes:0,failures:[]};
          for(const e of root.querySelectorAll('*')) {
            if(![...e.childNodes].some(n=>n.nodeType===3 && /[\u0600-\u06ff]/.test(n.textContent))) continue;
            const rule=chrome.find(([selector])=>e.closest(selector));
            const expected=rule ? [token(rule[1])] : arabic;
            report[rule ? 'chromeNodes' : 'readingNodes']++;
            const actual=norm(getComputedStyle(e).fontFamily);
            if(!expected.includes(actual)) report.failures.push({tag:e.tagName,cls:e.className,actual,expected});
          }
          return report;
        }''')
        assert fonts['readingNodes'] > 25 and not fonts['failures'], (width, fonts)
        tables = chapter.locator(':scope > .chapter-body .tbl-wrap:visible')
        assert tables.count() > 0
        for i in range(tables.count()):
            wrap = tables.nth(i)
            table = wrap.locator('table.comparison')
            cols = table.locator('thead th[scope="col"]').count()
            assert 3 <= cols <= 4
            assert table.locator('tbody tr').count() == table.locator('tbody th[scope="row"]').count()
            assert wrap.evaluate('(e)=>getComputedStyle(e).overflowX') == 'auto'
            assert table.evaluate('(e)=>getComputedStyle(e).direction') == 'rtl'
            assert wrap.evaluate('(e)=>e.getBoundingClientRect().width <= e.closest(".chapter-body").getBoundingClientRect().width+2')
        timeline_clearances = chapter.locator(':scope > .chapter-body .historical-timeline-event').evaluate_all('''events => events.map(e =>
          e.getBoundingClientRect().right-e.querySelector('.historical-timeline-date').getBoundingClientRect().right)''')
        assert timeline_clearances and all(gap >= 12 for gap in timeline_clearances), ('RTL timeline dates must clear their markers', width, timeline_clearances)
        details = chapter.locator(':scope > .chapter-body details.hikam-source-depth-inline')
        assert details.count() > 0
        assert all(details.nth(i).get_attribute('open') is None for i in range(details.count()))
        assert chapter.locator(':scope > .end-block .endh').count() == 6
        assert chapter.locator(':scope > .end-block .examq-cat').count() == 5
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth+2'), width
        page.wait_for_function('(n)=>document.querySelectorAll("#ch3-2-5 .hikam-companion-trigger").length===n', arg=len(CUES))
        assert chapter.locator('.hikam-source-depth-inline .hikam-companion-trigger').count() == 0
        cue = chapter.locator('.hikam-companion-trigger').first
        cue.scroll_into_view_if_needed()
        cue.focus()
        page.keyboard.press('Enter')
        popup = page.locator('#hikamCompanionPopup')
        assert popup.is_visible() and popup.get_attribute('dir') == 'rtl'
        assert popup.get_attribute('lang') == 'ar' and popup.get_attribute('role') == 'region'
        assert cue.get_attribute('aria-expanded') == 'true'
        for selector in ('.hikam-companion-simple', '.hikam-companion-why', '.hikam-companion-remember'):
            assert popup.locator(selector).is_visible()
        rect = popup.bounding_box()
        assert rect and rect['x'] >= -1 and rect['x']+rect['width'] <= width+1, rect
        page.keyboard.press('Escape')
        assert popup.is_hidden() and cue.get_attribute('aria-expanded') == 'false'
        assert cue.evaluate('(e)=>document.activeElement===e')
        if width == 390:
            for i in range(tables.count()):
                tables.nth(i).scroll_into_view_if_needed()
                tables.nth(i).screenshot(path=str(ARTIFACTS / f'azmi-325-comparison-{i+1}-mobile-rtl.png'))
        else:
            chapter.locator('.chapter-banner').screenshot(path=str(ARTIFACTS / 'azmi-325-title-desktop.png'))
            hierarchies = chapter.locator(':scope > .chapter-body .hierarchy:visible')
            for i in range(hierarchies.count()):
                hierarchies.nth(i).screenshot(path=str(ARTIFACTS / f'azmi-325-hierarchy-{i+1}-desktop.png'))
            timelines = chapter.locator(':scope > .chapter-body .historical-timeline:visible')
            for i in range(timelines.count()):
                timelines.nth(i).screenshot(path=str(ARTIFACTS / f'azmi-325-timeline-{i+1}-rtl.png'))
        no_errors(page, f'3.2.5 RTL {width}px')
        ctx.close()
    print('PASS 3.2.5 mobile/desktop RTL, Arabic fonts, comparable tables and keyboard Companion access', flush=True)


def no_javascript(browser, url):
    ctx = browser.new_context(viewport={'width': 390, 'height': 844}, java_script_enabled=False, service_workers='block')
    ctx.route('https://fonts.googleapis.com/**', lambda route: route.abort())
    ctx.route('https://fonts.gstatic.com/**', lambda route: route.abort())
    page = ctx.new_page()
    page.goto(url, wait_until='domcontentloaded', timeout=60000)
    detail = page.locator('#'+ID+' > .chapter-body details.hikam-source-depth-inline').first
    assert detail.get_attribute('open') is None
    detail.locator('summary').click()
    assert detail.get_attribute('open') is not None
    assert detail.locator('.hikam-source-depth-item p').first.is_visible()
    detail.locator('summary').click()
    assert detail.get_attribute('open') is None
    assert page.locator('#'+ID+' > .end-block .endh').count() == 6
    ctx.close()
    print('PASS 3.2.5 native Source Depth remains accessible without JavaScript', flush=True)


def normalized_pdf_text(text):
    text = ''.join(c for c in unicodedata.normalize('NFKC', text)
                   if not unicodedata.combining(c) and unicodedata.category(c) != 'Cf' and c != 'ـ')
    return ' '.join(text.split())


def pdf_revision_heading_locations(reader, geometry, headings):
    # The mandatory embedded Amiri font maps these headings to logical Unicode.
    # Plain extraction recovers every complete line with both pypdf 5.9.0 and
    # 6.21.4. Version 5.9.0's layout mode invents gaps inside Amiri words, so do
    # not reconstruct them by deleting spaces or matching scattered tokens.
    lines = []
    for i, item in enumerate(geometry):
        if item['dark']:
            for line_no, line in enumerate(reader.pages[i+1].extract_text().splitlines()):
                lines.append((i+2, line_no, normalized_pdf_text(line)))
    locations = []
    for heading in headings:
        matches = [(page_no, line_no) for page_no, line_no, line in lines if normalized_pdf_text(heading) == line]
        assert len(matches) == 1, ('PDF must contain the complete revision heading exactly once', heading, matches)
        locations.append(matches[0])
    assert locations == sorted(locations), ('PDF revision headings are out of order', locations)
    return [{'heading': heading, 'page': page_no, 'line': line_no}
            for heading, (page_no, line_no) in zip(headings, locations)]


def pdf_font_inventory(reader):
    fonts = {}
    for page_no, page in enumerate(reader.pages, 1):
        font_map = page['/Resources'].get('/Font')
        if not font_map:
            continue
        for ref in font_map.get_object().values():
            font = ref.get_object()
            variants = [font] + [child.get_object() for child in font.get('/DescendantFonts', [])]
            descriptors = [item['/FontDescriptor'] for item in variants if item.get('/FontDescriptor')]
            name = str(font.get('/BaseFont') or next((d.get('/FontName') for d in descriptors if d.get('/FontName')), 'unknown'))
            embedding = sorted({key for d in descriptors for key in ('/FontFile', '/FontFile2', '/FontFile3') if d.get(key)})
            if font.get('/Subtype') == '/Type3' and font.get('/CharProcs'):
                embedding.append('/CharProcs')
            key = (name, str(font.get('/Subtype')), tuple(embedding))
            entry = fonts.setdefault(key, {'name': name, 'subtype': key[1], 'embedded': bool(embedding), 'embedding': embedding, 'pages': []})
            entry['pages'].append(page_no)
    return list(fonts.values())


def print_a4(browser, url):
    ctx = context(browser, 1024)
    page = load(ctx, url)
    original_ids = page.evaluate('Array.from(document.querySelectorAll("section.chapter")).map(e=>e.id)')
    revision_headings = page.locator('#'+ID+' > .end-block .endh').all_text_contents()
    page.evaluate('''() => {
      const titleStampAudit = ''' + TITLE_STAMP_AUDIT + ''';
      // The application removes generated pages on afterprint. Capture each
      // completed beforeprint layout after its registered paginator, including
      // Chromium's actual PDF event, instead of inspecting removed nodes later.
      window.addEventListener('beforeprint', () => {
        const pages=[...document.querySelectorAll('#ch3-2-5 > .js-print-page')];
        window.__azmiPrintAudit={
          count:pages.length,
          titleStamp:titleStampAudit(document.querySelector('#ch3-2-5')),
          depthAndCues:pages.reduce((n,p)=>n+p.querySelectorAll('.hikam-source-depth-inline, .hikam-companion-trigger').length,0),
          revisionHeadings:pages.reduce((n,p)=>n+p.querySelectorAll('.endh').length,0),
          timelineDateClearances:pages.flatMap(p=>[...p.querySelectorAll('.historical-timeline-event')].map(e=>
            e.getBoundingClientRect().right-e.querySelector('.historical-timeline-date').getBoundingClientRect().right)),
          geometry:pages.map(e=>{
            const content=e.querySelector('.js-page-content');
            const footer=e.querySelector('.js-page-footer').getBoundingClientRect();
            const bottom=Math.max(content.getBoundingClientRect().top,...[...content.children].map(c=>c.getBoundingClientRect().bottom));
            return {overflow:content.scrollWidth-content.clientWidth,clearance:footer.top-bottom,dark:e.classList.contains('js-dark')};
          })
        };
      });
      window.__printControl.setFilter(['ch3-2-5']);
      window.__printControl.includeRevision(true);
      window.dispatchEvent(new Event('beforeprint'));
    }''')
    page.emulate_media(media='print')
    pdf = page.pdf(print_background=True, prefer_css_page_size=True)
    (ARTIFACTS / 'azmi-325-new-atheism-a4.pdf').write_bytes(pdf)
    audit = page.evaluate('window.__azmiPrintAudit')
    (ARTIFACTS / 'azmi-325-print-audit.json').write_text(json.dumps(audit, indent=2), encoding='utf-8')
    count = audit['count']
    assert count >= 3
    assert audit['titleStamp']['titleTextRects'] and audit['titleStamp']['sourceTextRects'] and not audit['titleStamp']['overlaps'], ('Printed title and citation text must clear the visible stamp', audit['titleStamp'])
    geometry = audit['geometry']
    assert all(g['overflow'] <= 3 and g['clearance'] >= -1 for g in geometry), geometry
    assert any(g['dark'] for g in geometry) and any(not g['dark'] for g in geometry)
    assert audit['depthAndCues'] == 0
    assert audit['revisionHeadings'] == 6
    assert audit['timelineDateClearances'] and all(gap >= 12 for gap in audit['timelineDateClearances']), ('Printed RTL timeline dates must clear their markers', audit['timelineDateClearances'])
    reader = PdfReader(BytesIO(pdf))
    assert len(reader.pages) == count+1, ('A4 must contain the frontmatter and every generated page', len(reader.pages), count)
    assert all(abs(float(p.mediabox.width)-595.28) < 2 and abs(float(p.mediabox.height)-841.89) < 2 for p in reader.pages)
    # Inspect the emitted PDF, not just the CSS stack or pre-print DOM. The
    # runner installs the intended Arabic fonts locally; remote fonts stay
    # blocked, so a fallback-only artifact must not silently pass.
    fonts = pdf_font_inventory(reader)
    (ARTIFACTS / 'azmi-325-pdf-fonts.json').write_text(json.dumps(fonts, indent=2), encoding='utf-8')
    assert any('amiri' in font['name'].lower() and font['embedded'] for font in fonts), ('The actual PDF must embed Amiri', fonts)
    # Check dark revision material actually reached the PDF, including all six
    # complete headings in order, rather than scattered matching word tokens.
    heading_locations = pdf_revision_heading_locations(reader, geometry, revision_headings)
    (ARTIFACTS / 'azmi-325-pdf-headings.json').write_text(json.dumps(heading_locations, ensure_ascii=False, indent=2), encoding='utf-8')
    page.evaluate('window.dispatchEvent(new Event("afterprint"))')
    assert page.locator('.js-print-page').count() == 0
    assert page.evaluate('Array.from(document.querySelectorAll("section.chapter")).map(e=>e.id)') == original_ids
    no_errors(page, '3.2.5 A4 print and restoration')
    ctx.close()
    print(f'PASS 3.2.5 actual A4 PDF: {len(reader.pages)} pages, six revision headings, no overflow, optional depth omitted, original DOM restored', flush=True)


def main():
    with site() as url, sync_playwright() as playwright:
        browser = launch(playwright)
        try:
            screen(browser, url)
            no_javascript(browser, url)
            print_a4(browser, url)
        finally:
            browser.close()


if __name__ == '__main__':
    main()
