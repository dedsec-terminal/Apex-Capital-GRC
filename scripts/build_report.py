"""Build a static, full-text reader from report-manifest.json.

Run from any directory with Python and the pinned Markdown dependency:
    python scripts/build_report.py
The script only writes generated report artifacts and its build record.
"""
from __future__ import annotations

import hashlib
import html
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit

import markdown

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "report-manifest.json"
OUT = ROOT / "site" / "report"
REPORT_CSS = """*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;color:#17221d;background:#f4f5f2;font:16px/1.68 Inter,ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif}a{color:#245743}button,input{font:inherit}.shell{min-height:100vh}.top{height:60px;background:#fff;border-bottom:1px solid #dce2dd;display:flex;align-items:center;justify-content:space-between;padding:0 max(24px,calc((100vw - 1460px)/2));position:sticky;top:0;z-index:4}.brand{font-size:13px;font-weight:750;letter-spacing:.025em;text-decoration:none;color:#183c2d}.toplinks{display:flex;gap:18px;font-size:12px}.layout{max-width:1460px;margin:auto;display:grid;grid-template-columns:275px minmax(0,1fr);gap:36px;padding:28px 24px}.side{position:sticky;top:84px;align-self:start;height:calc(100vh - 105px);overflow:auto;background:#fff;border:1px solid #e0e5df;border-radius:7px;padding:15px}.search{width:100%;padding:10px;border:1px solid #ccd5cd;border-radius:4px;font-size:13px}.result{font-size:12px;color:#52635a;max-height:210px;overflow:auto}.group{margin:20px 0 5px;font-size:10px;letter-spacing:.09em;text-transform:uppercase;color:#728078}.chapter-link{display:block;text-decoration:none;font-size:12px;line-height:1.4;padding:6px 8px;border-radius:3px;color:#35463c}.chapter-link:hover,.chapter-link.active{background:#edf2ed;color:#174a34}.main{min-width:0}.status{padding:10px 13px;margin-bottom:20px;background:#fff8e8;border:1px solid #ead9b6;color:#705b31;font-size:12px}.crumb{font-size:11px;color:#78847d;margin:4px 0 18px}.article{background:white;border:1px solid #e0e5df;border-radius:7px;padding:clamp(24px,5vw,64px);max-width:1000px;margin:auto;box-shadow:0 5px 24px #20312608}.article h1{font-size:clamp(30px,4vw,44px);line-height:1.15;letter-spacing:-.035em;margin:0 0 18px}.article h2{font-size:25px;line-height:1.3;margin:2.1em 0 .7em;border-bottom:1px solid #e3e8e3;padding-bottom:.35em}.article h3{font-size:19px;margin:1.7em 0 .5em}.article h4{font-size:16px}.article p,.article li{max-width:78ch}.article table{border-collapse:collapse;display:block;overflow:auto;width:100%;font-size:13px;margin:1.2em 0 1.8em}.article th,.article td{border:1px solid #dce3dc;text-align:left;vertical-align:top;padding:9px 11px;min-width:110px}.article th{background:#f1f4f0}.article blockquote{border-left:3px solid #7b9b84;margin:1em 0;padding:2px 18px;color:#59685f;background:#f7f9f6}.article pre{overflow:auto;background:#17231d;color:#e9f0e9;padding:17px;border-radius:5px;font-size:12px;line-height:1.55}.article code{font-family:ui-monospace,SFMono-Regular,Consolas,monospace;font-size:.9em}.article :not(pre)>code{background:#eef1ed;padding:.1em .32em;border-radius:3px}.article img{max-width:100%;height:auto}.article .toc{border:1px solid #e0e5df;background:#f8faf7;padding:16px 22px;margin:1em 0 2em}.article .toc ul{margin:.25em 0}.article hr{border:0;border-top:1px solid #dce3dc;margin:2em 0}.navrow{max-width:1000px;margin:18px auto;display:flex;justify-content:space-between;gap:12px}.navrow a,.action{display:inline-block;border:1px solid #cfd8d0;border-radius:4px;padding:9px 13px;text-decoration:none;background:#fff;font-size:12px}.navrow a:hover,.action:hover{background:#edf3ed}.book-intro{padding:40px;background:white;border:1px solid #e0e5df;border-radius:7px;margin-bottom:20px}.book-intro h1{font-size:38px;line-height:1.15}.book-intro p{max-width:76ch}.book-list{list-style:none;padding:0}.book-list li{padding:10px 0;border-bottom:1px solid #e4e8e4}.book-list small{display:block;color:#748078}.no-results{padding:8px;color:#846b3e;font-size:12px}.footer-note{max-width:1000px;margin:18px auto 40px;font-size:11px;color:#77827a}.raw-link{font-size:11px;margin-left:10px}@media(max-width:850px){.layout{grid-template-columns:1fr;padding:14px}.side{position:relative;top:auto;height:auto;max-height:45vh}.top{padding:0 14px}.toplinks{gap:10px}.article{padding:24px}}@media print{body{background:#fff;font-size:11pt}.top,.side,.crumb,.navrow,.footer-note,.status{display:none!important}.layout{display:block;padding:0;max-width:none}.article{border:0;box-shadow:none;padding:0;max-width:none}.article h1,.article h2,.article h3{break-after:avoid}.article pre,.article table{break-inside:avoid}.article a{color:inherit;text-decoration:none}.article a[href]:after{content:' (' attr(href) ')';font-size:8pt;overflow-wrap:anywhere}.book-list li{break-inside:avoid}}"""
SEARCH_JS = r"""(()=>{const q=document.querySelector('#search'),box=document.querySelector('#results');if(!q||!box)return;const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));q.addEventListener('input',()=>{const term=q.value.trim().toLowerCase();if(!term){box.innerHTML='';return}const hits=(window.REPORT_INDEX||[]).map(x=>({x,score:(x.text.toLowerCase().split(term).length-1)})).filter(y=>y.score).sort((a,b)=>b.score-a.score).slice(0,12);box.innerHTML=hits.length?hits.map(({x})=>`<a class="chapter-link" href="${esc(x.url)}">${esc(x.title)}<small> · ${esc(x.section)}</small><br><span>${esc(x.snippet)}</span></a>`).join(''):'<div class="no-results">No matching chapters. Try a broader term.</div>'})})();"""


def slugify(value: str) -> str:
    value = re.sub(r"[^\w\- ]", "", value, flags=re.UNICODE).strip().lower()
    return re.sub(r"[\s\-]+", "-", value) or "section"


def rel_url(from_dir: Path, target: Path) -> str:
    return Path(__import__("os").path.relpath(target, from_dir)).as_posix()


def rebase_markdown_links(text: str, source: Path) -> str:
    """Rebase source-relative links for the root-level combined Markdown book."""
    pattern = re.compile(r"(!?\[[^\]]*\]\()([^\s)]+)([^)]*\))")

    def replace(match):
        raw = match.group(2)
        parsed = urlsplit(raw)
        if parsed.scheme or parsed.netloc or not parsed.path or parsed.path.startswith("/"):
            return match.group(0)
        if match.group(1).startswith("![") and Path(unquote(parsed.path)).name.casefold() == "mermaid-diagram.png":
            target = ROOT / "site" / "assets" / "network.svg"
        else:
            target = (source.parent / unquote(parsed.path)).resolve()
        if not target.is_relative_to(ROOT.resolve()):
            return match.group(0)
        new_path = Path(os.path.relpath(target, ROOT)).as_posix()
        new_raw = new_path + (("?" + parsed.query) if parsed.query else "") + (("#" + parsed.fragment) if parsed.fragment else "")
        return match.group(1) + new_raw + match.group(3)

    return pattern.sub(replace, text)


def prefix_local_html_ids(fragment: str, prefix: str) -> str:
    """Make heading and in-page TOC anchors unique in the concatenated HTML book."""
    def replace(match):
        attr, value = match.group(1), match.group(2)
        if attr == "id":
            return f'{attr}="{prefix}{value}"'
        if attr == "href" and value.startswith("#"):
            return f'{attr}="#{prefix}{value[1:]}"'
        return match.group(0)
    return re.sub(r'\b(id|href)="([^"]+)"', replace, fragment)


def strip_md(text: str) -> str:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[#>*_|~-]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def main() -> None:
    if not MANIFEST.is_file():
        raise SystemExit(f"Required manifest not found: {MANIFEST}")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    sections = manifest.get("sections")
    if not isinstance(sections, list) or len(sections) != 13:
        raise SystemExit("Manifest must define the 13 numbered report sections.")
    chapters = []
    for section in sections:
        for chapter in section.get("chapters", []):
            source_path = ROOT / Path(chapter.get("path", ""))
            if not source_path.is_file() or source_path.suffix.lower() != ".md":
                raise SystemExit(f"Missing Markdown chapter: {chapter.get('path')}")
            route = OUT / Path(chapter["path"]).with_suffix(".html")
            chapters.append({"section": section, "meta": chapter, "source": source_path, "route": route,
                             "text": source_path.read_text(encoding="utf-8-sig")})
    expected = manifest.get("source_count", len(chapters))
    if len(chapters) < expected:
        raise SystemExit(f"Manifest source_count={expected}, but found only {len(chapters)} chapters.")
    md_to_chapter = {x["source"].resolve(): x for x in chapters}
    # Also support relative Markdown links whose targets resolve from their source chapter.
    route_by_title = {}
    for x in chapters:
        route_by_title[slugify(x["meta"].get("title", x["source"].stem))] = x
        route_by_title[slugify(x["source"].stem)] = x

    def render(ch: dict, view_dir: Path | None = None) -> str:
        view_dir = view_dir or ch["route"].parent
        source = ch["source"]
        text = ch["text"]
        # Link [[chapter name]] references to the corresponding report page when known.
        def wiki(m):
            key = slugify(m.group(1).split("|", 1)[0].split("#", 1)[0])
            target = route_by_title.get(key)
            label = html.escape(m.group(1).split("|", 1)[-1] if "|" in m.group(1) else m.group(1))
            if not target:
                return label
            href = rel_url(view_dir, target["route"])
            return f"[{label}]({href})"
        text = re.sub(r"\[\[([^\]]+)\]\]", wiki, text)
        # Link Markdown files to their rendered chapter page, retaining non-chapter asset links.
        link_re = re.compile(r"(!?\[[^\]]*\]\()([^\s)]+)([^)]*\))")
        def mdlink(m):
            raw = m.group(2)
            parsed = urlsplit(raw)
            if parsed.scheme or raw.startswith(("#", "//")):
                return m.group(0)
            candidate = (source.parent / unquote(parsed.path)).resolve()
            if parsed.path.lower().endswith(".md"):
                target = md_to_chapter.get(candidate)
                if target:
                    href = rel_url(view_dir, target["route"])
                elif candidate.is_file() and candidate.is_relative_to(ROOT.resolve()):
                    href = rel_url(view_dir, candidate)
                else:
                    return m.group(0)
            elif m.group(1).startswith("![") and not candidate.is_file():
                # The legacy source name is absent in this organized edition; its supplied
                # architecture SVG is the maintained equivalent and is publishable offline.
                if Path(parsed.path).name.casefold() == "mermaid-diagram.png":
                    asset = ROOT / "site" / "assets" / "network.svg"
                    if asset.is_file():
                        href = rel_url(view_dir, asset)
                    else:
                        return m.group(0)
                else:
                    return m.group(0)
            elif candidate.is_file() and candidate.is_relative_to(ROOT.resolve()):
                href = rel_url(view_dir, candidate)
                if parsed.fragment:
                    href += "#" + parsed.fragment
            else:
                return m.group(0)
            if parsed.fragment:
                href += "#" + parsed.fragment
            return m.group(1) + href + m.group(3)
        text = link_re.sub(mdlink, text)
        md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "sane_lists", "attr_list"],
                               extension_configs={"toc": {"permalink": True, "toc_depth": "2-4"}})
        body = md.convert(text)
        toc = f'<details class="toc" open><summary>On this page</summary>{md.toc}</details>' if md.toc else ""
        title = html.escape(ch["meta"].get("title") or source.stem)
        sec = html.escape(ch["section"].get("title", "Report"))
        status = html.escape(ch["meta"].get("status", ""))
        raw_url = rel_url(view_dir, source)
        return f'<div class="crumb"><a href="{html.escape(rel_url(view_dir, OUT / "index.html"), quote=True)}">Full report reader</a> / {sec}</div><article class="article"><h1>{title}</h1><p class="crumb">{sec} · <a class="raw-link" href="{html.escape(raw_url, quote=True)}">View source Markdown</a></p><p class="crumb"><strong>Chapter status:</strong> {status}</p>{toc}{body}</article>'

    def sidebar(active: str | None = None, view_dir: Path = OUT) -> str:
        pieces = ['<aside class="side"><label for="search"><strong>Search all chapters</strong></label><input class="search" id="search" type="search" placeholder="Search terms, controls, evidence…" autocomplete="off"><div id="results" class="result" aria-live="polite"></div>']
        for sec in sections:
            pieces.append(f'<div class="group">{html.escape(sec.get("title", "Section"))}</div>')
            for item in sec.get("chapters", []):
                route = OUT / Path(item["path"]).with_suffix(".html")
                url = rel_url(view_dir, route)
                selected = " active" if item["path"] == active else ""
                pieces.append(f'<a class="chapter-link{selected}" href="{html.escape(url, quote=True)}">{html.escape(item.get("title", Path(item["path"]).stem))}</a>')
        pieces.append("</aside>")
        return "".join(pieces)

    def page(content: str, active: str | None = None, title="Apex Capital GRC | Full Report", view_dir: Path = OUT) -> str:
        base = rel_url(view_dir, OUT)
        return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Security design, risk assessment and incident response report for the fictional Apex Capital lab scenario."><title>' + html.escape(title) + '</title><link rel="stylesheet" href="' + html.escape(base + '/styles.css', quote=True) + '"></head><body><header class="top"><a class="brand" href="' + html.escape(base + '/index.html', quote=True) + '">APEX CAPITAL · GRC REPORT</a><nav class="toplinks"><a href="' + html.escape(base + '/index.html', quote=True) + '">Reader</a><a href="' + html.escape(base + '/complete.html', quote=True) + '">Complete report</a><a href="' + html.escape(base + '/../../COMPLETE-REPORT.md', quote=True) + '">Download Markdown</a><button class="action" onclick="window.print()">Print</button></nav></header><div class="layout">' + sidebar(active, view_dir) + '<main class="main"><div class="status"><strong>Publication status:</strong> This is a designed assessment and synthetic evidence pack. VM validation scenarios are planned; no VM execution results are claimed.</div>' + content + '</main></div><script>window.REPORT_BASE=' + json.dumps(base + '/') + ';</script><script src="' + html.escape(base + '/search-index.js', quote=True) + '"></script><script src="' + html.escape(base + '/search.js', quote=True) + '"></script></body></html>'

    OUT.mkdir(parents=True, exist_ok=True)
    mobile_header = "@media(max-width:600px){.top{height:auto;min-height:60px;padding:8px 12px;flex-wrap:wrap;gap:4px 12px}.brand{flex:1 0 100%;font-size:11px}.toplinks{width:100%;justify-content:space-between;flex-wrap:wrap;gap:6px}.toplinks a:nth-child(3){display:none}}"
    (OUT / "styles.css").write_text(REPORT_CSS + mobile_header, encoding="utf-8")
    search_js = SEARCH_JS.replace('href="${esc(x.url)}"', 'href="${esc((window.REPORT_BASE||"")+x.url)}"')
    (OUT / "search.js").write_text(search_js, encoding="utf-8")
    # Build a searchable, plain-text index; no external service or CDN is used.
    search_rows = []
    for ch in chapters:
        txt = strip_md(ch["text"])
        route = ch["route"]
        search_rows.append({"title": ch["meta"].get("title", ch["source"].stem),
                            "section": ch["section"].get("title", "Report"),
                            "url": rel_url(OUT, route), "text": txt,
                            "snippet": txt[:190] + ("…" if len(txt) > 190 else "")})
    (OUT / "search-index.js").write_text("window.REPORT_INDEX=" + json.dumps(search_rows, ensure_ascii=False).replace("</", "<\\/") + ";", encoding="utf-8")

    flat = [(s, c) for s in sections for c in s.get("chapters", [])]
    for ix, ch in enumerate(chapters):
        prev = chapters[ix - 1] if ix else None
        nxt = chapters[ix + 1] if ix + 1 < len(chapters) else None
        nav = '<nav class="navrow">' + (f'<a href="{html.escape(rel_url(ch["route"].parent, prev["route"]), quote=True)}">← {html.escape(prev["meta"].get("title", "Previous"))}</a>' if prev else '<span></span>') + (f'<a href="{html.escape(rel_url(ch["route"].parent, nxt["route"]), quote=True)}">{html.escape(nxt["meta"].get("title", "Next"))} →</a>' if nxt else '') + '</nav><p class="footer-note">Chapter ' + str(ix + 1) + ' of ' + str(len(chapters)) + '. Content is provided in full from its Markdown source.</p>'
        dest = ch["route"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(page(render(ch) + nav, ch["meta"]["path"], f'{ch["meta"].get("title", ch["source"].stem)} | Apex Capital GRC', ch["route"].parent), encoding="utf-8")

    listing = '<section class="book-intro"><div class="crumb">Apex Capital · Security design and incident response</div><h1>Full report reader</h1><p>Browse all ' + str(len(chapters)) + ' Markdown chapters in their published order. The reader keeps each source chapter intact, adds chapter navigation and a search index, and supports printing from the complete report page.</p><p><a class="action" href="complete.html">Read or print complete report</a> <a class="action" href="../../COMPLETE-REPORT.md">Download complete Markdown</a></p></section><section class="article"><h2>Report contents</h2>'
    for s in sections:
        listing += f'<h3>{html.escape(s.get("title", "Section"))}</h3><ul class="book-list">'
        for item in s.get("chapters", []):
            route = OUT / Path(item["path"]).with_suffix(".html")
            listing += f'<li><a href="{html.escape(rel_url(OUT, route), quote=True)}">{html.escape(item.get("title", Path(item["path"]).stem))}</a><small>{html.escape(item.get("status", ""))}</small></li>'
        listing += '</ul>'
    listing += '</section><p class="footer-note">Chapter pages preserve the complete Markdown body. Use the source link on each chapter to review the Markdown version.</p>'
    (OUT / "index.html").write_text(page(listing, title="Full Report Reader | Apex Capital GRC"), encoding="utf-8")

    # Full report book: render every chapter with page breaks for convenient printing.
    complete = '<section class="book-intro"><div class="crumb">Apex Capital · Complete report</div><h1>Complete Report</h1><p>All ' + str(len(chapters)) + ' published Markdown chapters, rendered in order. Use the browser print dialog to save as PDF.</p><p><a class="action" href="../../COMPLETE-REPORT.md">Download complete Markdown</a></p></section>'
    for i, ch in enumerate(chapters):
        complete += f'<section class="book-chapter" id="chapter-{i+1}">{prefix_local_html_ids(render(ch, OUT), f"c{i+1}-")}</section>'
    complete_page = page(complete, title="Complete Report | Apex Capital GRC")
    complete_page = complete_page.replace("</head>", "<style>@media print{.book-chapter{break-before:page}.book-chapter:first-of-type{break-before:auto}}</style></head>")
    (OUT / "complete.html").write_text(complete_page, encoding="utf-8")

    # Source Markdown compilation keeps all prose and original section order.
    md_parts = ["# Apex Capital GRC — Complete Report", "", "> Full Markdown compilation of all chapters listed in `report-manifest.json`. The individual Markdown files remain canonical.", "", "**Publication status:** VM validation scenarios are planned; no VM execution results are claimed.", ""]
    for s in sections:
        md_parts += ["# " + s.get("title", "Section"), ""]
        for ch in chapters:
            if ch["section"] is s:
                md_parts += ["## " + ch["meta"].get("title", ch["source"].stem), "", rebase_markdown_links(ch["text"].strip(), ch["source"]), "", "---", ""]
    complete_md = "\n".join(md_parts).rstrip() + "\n"
    (ROOT / "COMPLETE-REPORT.md").write_text(complete_md, encoding="utf-8")
    markdown_link_errors = []
    markdown_link_count = 0
    for raw in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", complete_md):
        raw = raw.split(None, 1)[0]
        parsed = urlsplit(raw)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        target = (ROOT / unquote(parsed.path)).resolve()
        markdown_link_count += 1
        if not target.is_relative_to(ROOT.resolve()) or not target.exists():
            markdown_link_errors.append(raw)
    if markdown_link_errors:
        raise SystemExit("Combined Markdown contains broken or escaping local links: " + json.dumps(markdown_link_errors[:25]))

    # Deterministic relative-link audit for all chapter pages and source routes.
    link_errors = []
    for file in set([OUT / "index.html", OUT / "complete.html", *OUT.rglob("*.html")]):
        for raw in re.findall(r'(?:href|src)="([^"]+)"', file.read_text(encoding="utf-8")):
            if raw.startswith(("http:", "https:", "mailto:", "data:", "#", "javascript:")):
                continue
            target = (file.parent / unquote(urlsplit(raw).path)).resolve()
            if not target.is_relative_to(ROOT.resolve()) or not target.exists():
                link_errors.append({"file": file.relative_to(ROOT).as_posix(), "target": raw})
    if link_errors:
        raise SystemExit("Generated report contains broken or escaping links: " + json.dumps(link_errors[:25], ensure_ascii=False))
    build = {"built_at_utc": datetime.now(timezone.utc).isoformat(), "manifest": "report-manifest.json",
             "source_count": expected, "rendered_chapters": len(chapters), "sections": len(sections),
             "markdown_version": markdown.__version__, "search_entries": len(search_rows),
             "generated_pages": len(list(OUT.rglob("*.html"))), "broken_html_links": 0,
             "compiled_markdown_links_checked": markdown_link_count, "broken_markdown_links": 0,
             "complete_markdown_sha256": hashlib.sha256(complete_md.encode()).hexdigest(),
             "validation_scope": "Manifest chapter count and generated local HTML href/src targets; no application or VM security tests."}
    (ROOT / "report-build.json").write_text(json.dumps(build, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(build, indent=2))


if __name__ == "__main__":
    main()
