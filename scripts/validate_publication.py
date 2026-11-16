"""Validate the publication's links, risk arithmetic and honest test statuses."""
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []
checked_links = 0
manifest = json.loads((ROOT / "report-manifest.json").read_text(encoding="utf-8"))
chapters = [chapter for section in manifest["sections"] for chapter in section["chapters"]]
originals = [chapter for chapter in chapters if chapter.get("source_kind") != "supplemental"]
if len(manifest["sections"]) != 13:
    errors.append("Expected the 13 numbered report sections")
if len(originals) != manifest["source_count"] or manifest["source_count"] != 29:
    errors.append("The manifest must preserve all 29 original chapters separately from supplemental chapters")
paths = [chapter["path"] for chapter in chapters]
if len(paths) != len(set(paths)):
    errors.append("Duplicate chapter path in manifest")
source_names = [chapter["source_file"] for chapter in originals]
if len(source_names) != len(set(source_names)):
    errors.append("Duplicate original chapter in manifest")
for chapter in chapters:
    target = (ROOT / chapter["path"]).resolve()
    if not target.is_relative_to(ROOT) or not target.is_file():
        errors.append(f"Missing or escaping chapter: {chapter['path']}")
    rendered = ROOT / "site" / "report" / Path(chapter["path"]).with_suffix(".html")
    if not rendered.is_file():
        errors.append(f"Chapter not rendered: {chapter['path']}")
    if target.is_file():
        lines = target.read_text(encoding="utf-8").splitlines()
        fenced = False
        table_width = None
        for index, line in enumerate(lines):
            if line.lstrip().startswith("```"):
                fenced = not fenced
                table_width = None
                continue
            if fenced:
                continue
            if re.fullmatch(r"\s*\|[\s:|\-]+\|\s*", line) and index and lines[index - 1].strip().startswith("|"):
                table_width = len(re.split(r"(?<!\\)\|", lines[index - 1].strip().strip("|")))
                continue
            if table_width and line.strip().startswith("|"):
                width = len(re.split(r"(?<!\\)\|", line.strip().strip("|")))
                if width != table_width:
                    errors.append(f"Table column mismatch: {chapter['path']}:{index + 1} ({width} instead of {table_width})")
            else:
                table_width = None
for file in [*ROOT.rglob("*.md"), *ROOT.rglob("*.html")]:
    if ".git" in file.parts:
        continue
    source = file.read_text(encoding="utf-8")
    matches = re.findall(r'(?:href|src)=["\']([^"\']+)', source) if file.suffix == ".html" else re.findall(r'\]\(([^)]+)\)', source)
    for value in matches:
        if value.startswith(("http:", "https:", "mailto:", "data:", "#")):
            continue
        path = unquote(urlsplit(value).path)
        if not path:
            continue
        target = (file.parent / path).resolve()
        if not target.is_relative_to(ROOT):
            errors.append(f"Link leaves publication: {file.relative_to(ROOT)} -> {path}")
        elif not target.exists():
            errors.append(f"Missing target: {file.relative_to(ROOT)} -> {path}")
        checked_links += 1
data = json.loads((ROOT / "data/register.json").read_text(encoding="utf-8"))
for risk in data["risks"]:
    if risk["likelihood"] * risk["impact"] != risk["inherentScore"]:
        errors.append(f"Risk arithmetic mismatch: {risk['id']}")
    register = (ROOT / "04-Risk-Assessment/risk-register.md").read_text(encoding="utf-8")
    master = register.split("## Master Risk Register", 1)[1].split("## Detailed Risk Register", 1)[0]
    row = next((line for line in master.splitlines() if line.startswith(f"| {risk['id']} |")), "")
    cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
    expected = [str(risk["likelihood"]), str(risk["impact"]), str(risk["inherentScore"]), risk["rating"]]
    if cells[2:6] != expected:
        errors.append(f"Full report and website risk register differ: {risk['id']}")
for test in data["tests"]:
    if test["status"] != "planned_not_executed":
        errors.append(f"Unsubstantiated execution status: {test['id']}")
summary = {"passed": not errors, "links_checked": checked_links, "risks_checked": len(data["risks"]),
           "original_chapters": len(originals), "total_chapters": len(chapters),
           "planned_scenarios": len(data["tests"]), "errors": errors,
           "scope": "Publication structure and data consistency only; no VM security test was executed."}
print(json.dumps(summary, indent=2))
raise SystemExit(bool(errors))
