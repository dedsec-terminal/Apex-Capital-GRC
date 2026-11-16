"""Validate the publication's links, risk arithmetic and honest test statuses."""
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []
checked_links = 0
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
for test in data["tests"]:
    if test["status"] != "planned_not_executed":
        errors.append(f"Unsubstantiated execution status: {test['id']}")
summary = {"passed": not errors, "links_checked": checked_links, "risks_checked": len(data["risks"]),
           "planned_scenarios": len(data["tests"]), "errors": errors,
           "scope": "Publication structure and data consistency only; no VM security test was executed."}
print(json.dumps(summary, indent=2))
raise SystemExit(bool(errors))
