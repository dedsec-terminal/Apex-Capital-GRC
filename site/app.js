const $ = (selector) => document.querySelector(selector);

function addText(parent, tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  node.textContent = text;
  parent.append(node);
  return node;
}

async function loadChapters() {
  const host = $('#chapter-explorer');
  try {
    const response = await fetch('../report-manifest.json');
    if (!response.ok) throw new Error('Chapter manifest is not available');
    const manifest = await response.json();
    const columns = document.createElement('div');
    columns.className = 'chapter-columns';
    for (const section of manifest.sections || []) {
      const card = document.createElement('article'); card.className = 'chapter-group';
      addText(card, 'h3', '', section.title);
      const list = document.createElement('ol');
      for (const chapter of section.chapters || []) {
        const item = document.createElement('li');
        const link = document.createElement('a'); link.textContent = chapter.title;
        const path = String(chapter.path || chapter.source_file || '').replace(/\\/g, '/').replace(/\.md$/i, '.html');
        link.href = `report/${path}`;
        item.append(link); addText(item, 'small', '', chapter.status || 'Chapter'); list.append(item);
      }
      card.append(list); columns.append(card);
    }
    host.replaceChildren(columns);
    const chapterCount = (manifest.sections || []).reduce((n, section) => n + (section.chapters || []).length, 0);
    const originals = manifest.source_count || chapterCount;
    addText(host, 'p', 'report-footnote', `Index: ${manifest.sections?.length || 0} numbered sections · ${chapterCount} chapters (${originals} original Markdown files plus any supplemental chapters). The reader preserves full content.`);
    const featuredHost = $('#featured-chapters');
    const featuredSpecs = [
      {pattern: /capability-evaluation/i, label: 'Capability evaluation', description: 'Evidence-led review of documented controls and current maturity.'},
      {pattern: /incident-response-plan/i, label: 'Incident response plan', description: 'Response roles, decisions, escalation and evidence expectations.'},
      {pattern: /tabletop-exercise/i, label: 'Incident response tabletop', description: 'A proposed exercise scenario; not yet conducted.'}
    ];
    const allChapters = (manifest.sections || []).flatMap(section => section.chapters || []);
    const featureSection = document.createElement('div');
    featureSection.className = 'featured-grid';
    for (const spec of featuredSpecs) {
      const chapter = allChapters.find(item => spec.pattern.test(item.source_file || '') || spec.pattern.test(item.path || ''));
      if (!chapter) continue;
      const link = document.createElement('a');
      link.className = 'featured-card';
      link.href = `report/${String(chapter.path || chapter.source_file).replace(/\\/g, '/').replace(/\.md$/i, '.html')}`;
      addText(link, 'small', '', 'FEATURED CHAPTER');
      addText(link, 'b', '', spec.label);
      addText(link, 'span', '', spec.description);
      featureSection.append(link);
    }
    if (featureSection.childElementCount) {
      addText(featuredHost, 'h3', 'featured-heading', 'Incident readiness & capability');
      featuredHost.append(featureSection);
    }
  } catch {
    host.replaceChildren(); addText(host, 'p', 'loading', 'The chapter manifest is not available in this copy yet. Open the full report reader for chapter navigation.');
  }
}

async function loadRegisters() {
  const riskGrid = $('#risk-grid'), testList = $('#test-list');
  try {
    const response = await fetch('../data/register.json');
    if (!response.ok) throw new Error('Register unavailable');
    const data = await response.json();
    for (const risk of data.risks || []) {
      const card = document.createElement('article'); card.className = 'risk-card';
      const top = document.createElement('div'); top.className = 'risk-top';
      addText(top, 'span', 'risk-id', risk.id); addText(top, 'span', `badge ${String(risk.rating).toLowerCase()}`, risk.rating); card.append(top);
      addText(card, 'h3', '', risk.title);
      addText(card, 'div', 'risk-meta', `L ${risk.likelihood} × I ${risk.impact} = ${risk.inherentScore} / 25 · Inherent`);
      addText(card, 'div', 'risk-owner', `Proposed owner: ${risk.ownerRole}`); riskGrid.append(card);
    }
    for (const test of data.tests || []) {
      const row = document.createElement('div'); row.className = 'test-row';
      addText(row, 'span', 'test-number', test.id); addText(row, 'span', '', test.title); addText(row, 'span', 'test-state', 'PLANNED · NOT RUN'); testList.append(row);
    }
  } catch {
    riskGrid.textContent = 'Risk register data could not be loaded.'; testList.textContent = 'Test register data could not be loaded.';
  }
}

function addFlowFilter() {
  const panel = document.querySelector('img[src="assets/diagrams/flows.svg"]')?.closest('.diagram');
  if (!panel) return;
  const filters = [
    {label:'All paths', key:'all'}, {label:'Administrative', key:'admin'},
    {label:'Telemetry', key:'telemetry'}, {label:'Denied by intent', key:'denied'}
  ];
  const paths = [
    {key:'admin', text:'Management → Ubuntu DMZ · SSH TCP 22 · approved source only'},
    {key:'admin', text:'Management → Windows internal · RDP TCP 3389 · approved source only'},
    {key:'telemetry', text:'Ubuntu / Windows agents → Wazuh · TCP 1514; TCP 1515 only for controlled enrollment'},
    {key:'telemetry', text:'pfSense → Wazuh · UDP 514 only if syslog is explicitly enabled'},
    {key:'denied', text:'DMZ subnet → Internal subnet · any service · deny by default'}
  ];
  const wrap = document.createElement('div'); wrap.className = 'flow-explorer';
  addText(wrap, 'b', '', 'Inspect proposed paths');
  const bar = document.createElement('div'); bar.className = 'flow-filters';
  const list = document.createElement('ul'); list.className = 'flow-list';
  const buttons = filters.map((filter, index) => {
    const button = document.createElement('button'); button.type = 'button'; button.textContent = filter.label; button.dataset.filter = filter.key;
    if (index === 0) button.setAttribute('aria-pressed', 'true');
    button.addEventListener('click', () => {
      buttons.forEach((b) => b.setAttribute('aria-pressed', String(b === button)));
      [...list.children].forEach((item) => { item.hidden = filter.key !== 'all' && item.dataset.kind !== filter.key; });
    });
    bar.append(button); return button;
  });
  paths.forEach((path) => { const item = document.createElement('li'); item.dataset.kind = path.key; item.textContent = path.text; list.append(item); });
  wrap.append(bar, list); panel.append(wrap);
}

const menuButton = $('.menu-toggle'), nav = $('#primary-nav');
menuButton?.addEventListener('click', () => { const open = nav.classList.toggle('open'); menuButton.setAttribute('aria-expanded', String(open)); });
nav?.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => { nav.classList.remove('open'); menuButton?.setAttribute('aria-expanded', 'false'); }));
loadChapters(); loadRegisters(); addFlowFilter();
