/* 11AM Hikam — source-grounded Reading Companions.
 * Exact-match inline cues in main prose teach the immediate context first.
 * Further original-source details use adjacent native disclosures in the
 * reading HTML. Print clones omit that optional material and unwrap cues.
 * Data is embedded in the canonical single-file publication for offline use.
 */
(function () {
  'use strict';

  var root = document.body;
  var manifest = document.getElementById('hikamReadingCompanionsData');
  if (!root || !manifest) return;
  var dataset;
  try { dataset = JSON.parse(manifest.textContent); }
  catch (error) { console.warn('Hikam Reading Companions: invalid manifest'); return; }
  if (!dataset || dataset.version !== 1 || !Array.isArray(dataset.companions)) return;

  var records = new Map();
  var failed = [];
  var current = null;
  var pinned = false;
  var restoringTriggerFocus = false;
  var popup = document.createElement('div');
  popup.id = 'hikamCompanionPopup';
  popup.className = 'hikam-companion-popup';
  popup.setAttribute('role', 'region');
  popup.setAttribute('aria-labelledby', 'hikamCompanionPopupTitle');
  popup.hidden = true;
  var kind = document.createElement('span');
  kind.className = 'hikam-companion-kind';
  var heading = document.createElement('strong');
  heading.className = 'hikam-companion-title';
  heading.id = 'hikamCompanionPopupTitle';
  var detail = document.createElement('span');
  detail.className = 'hikam-companion-explanation';
  // Context-first Companions clarify the nearby idea; the source-depth appendix
  // holds optional further source information without interrupting the reading.
  function contextField(labelText, className) {
    var container = document.createElement('div');
    container.className = 'hikam-companion-context-field ' + className;
    container.hidden = true;
    var label = document.createElement('span');
    label.className = 'hikam-companion-field-label';
    label.textContent = labelText;
    var value = document.createElement('span');
    value.className = 'hikam-companion-field-value';
    container.append(label, value);
    return {container:container, value:value};
  }
  var simpleField = contextField('In simple words', 'hikam-companion-simple');
  var whyField = contextField('Why this appears here', 'hikam-companion-why');
  var rememberField = contextField('Remember', 'hikam-companion-remember');
  var closeButton = document.createElement('button');
  closeButton.type = 'button';
  closeButton.className = 'hikam-companion-close';
  closeButton.setAttribute('aria-label', 'Close reading companion');
  closeButton.textContent = '×';
  closeButton.hidden = true;
  popup.append(kind, heading, detail,
    simpleField.container, whyField.container, rememberField.container, closeButton);
  root.appendChild(popup);
  var selector = '.hikam-companion-trigger';

  function normalized(text) { return (text || '').replace(/\s+/g, ' ').trim(); }
  function targetFor(node) {
    return node && node.closest ? node.closest(selector) : null;
  }
  function dismiss(restoreFocus) {
    var previous = current;
    if (previous) {
      previous.setAttribute('aria-expanded', 'false');
      previous.removeAttribute('aria-describedby');
    }
    current = null; pinned = false; popup.hidden = true;
    popup.dataset.pinned = 'false';
    closeButton.hidden = true;
    if (restoreFocus && previous && previous.isConnected) {
      // Suppress only the synthetic focusin caused by closing the popup.
      // Otherwise our accessible focus-to-explain behavior would re-open it.
      restoringTriggerFocus = true;
      previous.focus();
      restoringTriggerFocus = false;
    }
  }
  function place() {
    if (!current || popup.hidden) return;
    var rect = current.getBoundingClientRect();
    var w = document.documentElement.clientWidth;
    var h = document.documentElement.clientHeight;
    if (!current.isConnected || rect.bottom < 0 || rect.top > h) {
      dismiss(); return;
    }
    var gap = 10, edge = 12;
    var size = popup.getBoundingClientRect();
    var left = Math.min(Math.max(rect.left, edge), Math.max(edge, w - size.width - edge));
    var below = rect.bottom + gap;
    var above = rect.top - size.height - gap;
    var y = below + size.height <= h - edge ? below : above;
    popup.style.left = Math.round(left) + 'px';
    popup.style.top = Math.round(Math.max(edge, Math.min(y, h - size.height - edge))) + 'px';
  }
  function show(button, keepOpen) {
    var item = records.get(button);
    if (!item) return;
    if (current && current !== button) dismiss();
    current = button; pinned = !!keepOpen;
    popup.dataset.pinned = pinned ? 'true' : 'false';
    closeButton.hidden = !pinned;
    kind.textContent = item.kind;
    heading.textContent = item.title;
    var isContextual = !!(item.simple && item.why_here && item.remember);
    detail.hidden = isContextual;
    detail.textContent = isContextual ? '' : item.explanation;
    simpleField.container.hidden = !isContextual;
    whyField.container.hidden = !isContextual;
    rememberField.container.hidden = !isContextual;
    if (isContextual) {
      simpleField.value.textContent = item.simple;
      whyField.value.textContent = item.why_here;
      rememberField.value.textContent = item.remember;
    }
    var chapter = button.closest('.chapter');
    var hue = chapter && chapter.style.getPropertyValue('--hue').trim();
    if (hue && /^\d{1,3}$/.test(hue))
      popup.style.setProperty('--hikam-companion-accent', 'hsl(' + hue + ' 47% 34%)');
    else popup.style.removeProperty('--hikam-companion-accent');
    popup.dir = chapter && (chapter.dir === 'rtl' || chapter.classList.contains('rtl')) ? 'rtl' : 'ltr';
    popup.lang = chapter && chapter.getAttribute('lang') || 'en';
    button.setAttribute('aria-expanded', 'true');
    button.setAttribute('aria-describedby', popup.id);
    popup.hidden = false;
    place();
  }
  function findSingleTextNode(scope, phrase) {
    var walker = document.createTreeWalker(scope, NodeFilter.SHOW_TEXT);
    var matches = [];
    for (var node = walker.nextNode(); node; node = walker.nextNode()) {
      var first = node.nodeValue.indexOf(phrase);
      if (first < 0) continue;
      matches.push({node:node, start:first});
      if (node.nodeValue.indexOf(phrase, first + phrase.length) >= 0) return null;
    }
    return matches.length === 1 ? matches[0] : null;
  }
  function attach(item) {
    if (!item || !/^h\d{3}-[a-z0-9-]+$/.test(item.id || '') ||
        !/^ch\d+-\d+-\d+$/.test(item.chapter || '') ||
        !item.passage || !item.text || !item.kind || !item.title ||
        !item.explanation || !item.source || !item.source.printedPages ||
        !item.added_value) return false;
    var chapter = document.getElementById(item.chapter);
    if (!chapter || !chapter.matches('section.chapter')) return false;
    var body = chapter.querySelector('.chapter-body');
    if (!body) return false;
    var paragraphs = Array.from(body.querySelectorAll('p')).filter(function (p) {
      return !p.closest('.box, .analogy, .checkpoint, .tbl-wrap, .hierarchy, .concept-rel, .golden-quote, .end-block, .hikam-source-depth-inline') &&
        normalized(p.textContent).includes(normalized(item.passage));
    });
    if (paragraphs.length !== 1) return false;
    var hit = findSingleTextNode(paragraphs[0], item.text);
    if (!hit) return false;
    var after = hit.node.splitText(hit.start);
    after.splitText(item.text.length);
    var trigger = document.createElement('span');
    trigger.className = 'hikam-companion-trigger';
    trigger.setAttribute('role', 'button');
    trigger.tabIndex = 0;
    trigger.textContent = after.nodeValue;
    trigger.dataset.companionId = item.id;
    trigger.setAttribute('aria-label', item.text + ', reading companion available');
    trigger.setAttribute('aria-controls', popup.id);
    trigger.setAttribute('aria-expanded', 'false');
    after.parentNode.replaceChild(trigger, after);
    records.set(trigger, item);
    return true;
  }
  function onKey(event) {
    var button = targetFor(event.target);
    if (button && (event.key === 'Enter' || event.key === ' ')) {
      event.preventDefault();
      button.click();
    } else if (event.key === 'Escape' && current) {
      event.preventDefault();
      dismiss(true);
    } else if (button && event.key === 'ArrowDown' && current === button && pinned) {
      event.preventDefault();
      closeButton.focus();
    }
  }
  function install() {
    closeButton.addEventListener('click', function () { dismiss(true); });
    var seen = new Set();
    dataset.companions.forEach(function (item) {
      if (!item || seen.has(item.id) || !attach(item)) {
        failed.push(item && item.id || 'invalid');
      } else seen.add(item.id);
    });
    if (failed.length) console.warn('Hikam Reading Companions: missing or ambiguous anchors', failed);
    document.addEventListener('keydown', onKey);
    document.addEventListener('click', function (event) {
      var button = targetFor(event.target);
      if (button) {
        if (current === button && pinned) dismiss();
        else show(button, true);
      } else if (current && !popup.contains(event.target)) dismiss();
    });
    var hover = window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)');
    document.addEventListener('pointerover', function (event) {
      var button = targetFor(event.target);
      if (button && !pinned && hover && hover.matches &&
          !button.contains(event.relatedTarget)) show(button, false);
    });
    document.addEventListener('pointerout', function (event) {
      if (pinned || !current || !hover || !hover.matches) return;
      if (current.contains(event.relatedTarget)) return;
      if (targetFor(event.target) === current) dismiss();
    });
    document.addEventListener('focusin', function (event) {
      if (restoringTriggerFocus) return;
      var button = targetFor(event.target);
      if (button) show(button, false);
    });
    document.addEventListener('focusout', function (event) {
      var previous = current;
      if (!previous || previous !== event.target || pinned) return;
      requestAnimationFrame(function () {
        if (current === previous && document.activeElement !== previous) dismiss();
      });
    });
    window.addEventListener('scroll', function () { if (current) place(); }, {passive:true});
    window.addEventListener('resize', function () { if (current) place(); });
    window.addEventListener('hashchange', dismiss);
    window.addEventListener('beforeprint', dismiss);
    window.__hikamReadingCompanions = {
      attached: function () { return records.size; },
      failed: function () { return failed.slice(); }
    };
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', install, {once:true});
  else install();
}());
