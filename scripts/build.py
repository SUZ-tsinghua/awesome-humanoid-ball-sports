#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Render the generated parts of README.md from data/papers.toml and data/labs.toml.

Generated parts sit between `<!-- gen:KEY -->` and `<!-- /gen -->` markers;
everything else in README.md is hand-written and left alone.

    uv run scripts/build.py          # rewrite README.md
    uv run scripts/build.py --check  # exit 1 if README.md is out of date (CI)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
PAPERS = ROOT / "data" / "papers.toml"
LABS = ROOT / "data" / "labs.toml"

SPORTS = {
  "table-tennis": ("🏓", "Table Tennis"),
  "tennis": ("🎾", "Tennis"),
  "badminton": ("🏸", "Badminton"),
  "soccer": ("⚽", "Soccer"),
  "basketball": ("🏀", "Basketball"),
}
STATUSES = ("released", "announced")

BLOCK = re.compile(r"(<!-- gen:(\S+) -->\n).*?(<!-- /gen -->)", re.DOTALL)
DATE = re.compile(r"^\d{4}\.(0[1-9]|1[0-2])$")
EMPTY = "_Nothing yet. [Add one?](CONTRIBUTING.md)_\n"


def load() -> tuple[list[dict], dict[str, dict], dict[str, dict]]:
  papers = tomllib.loads(PAPERS.read_text())["paper"]
  lab_data = tomllib.loads(LABS.read_text())
  institutions = lab_data["institutions"]
  errors = []

  for name, inst in institutions.items():
    for key in ("lat", "lon"):
      if not isinstance(inst.get(key), float):
        errors.append(f"institution {name!r}: {key} must be a float")

  labs = {}
  for lab in lab_data["labs"]:
    where = f"lab {lab.get('id')!r}"
    if lab.get("id") in labs:
      errors.append(f"{where}: duplicate id")
    if lab.get("institution") not in institutions:
      errors.append(f"{where}: unknown institution {lab.get('institution')!r}")
    labs[lab.get("id")] = lab

  for p in papers:
    where = f"paper {p.get('title', '?')[:60]!r}"
    p.setdefault("status", "released")
    if isinstance(p.get("sport"), str):
      p["sport"] = [p["sport"]]
    for key in ("date", "title", "sport", "paper"):
      if key not in p:
        errors.append(f"{where}: missing {key}")
    if not DATE.match(p.get("date", "")):
      errors.append(f"{where}: date must be YYYY.MM")
    if not p.get("sport") or not set(p["sport"]) <= SPORTS.keys():
      errors.append(f"{where}: sport must be one or a list of {list(SPORTS)}")
    if p["status"] not in STATUSES:
      errors.append(f"{where}: status must be one of {STATUSES}")
    if p["status"] == "released" and "venue" not in p:
      errors.append(f"{where}: missing venue")
    if not isinstance(p.get("real"), bool):
      errors.append(f"{where}: real must be true or false")
    code = p.get("code")
    if code is not None and code != "soon" and not code.startswith("https://"):
      errors.append(f"{where}: code must be a URL or 'soon'")
    if "lab" in p and p["lab"] not in labs:
      errors.append(f"{where}: unknown lab {p['lab']!r}")

  used_labs = {p["lab"] for p in papers if "lab" in p}
  for lab_id in labs.keys() - used_labs:
    errors.append(f"lab {lab_id!r}: not referenced by any paper")
  used_institutions = {labs[i]["institution"] for i in used_labs if i in labs}
  for name in institutions.keys() - used_institutions:
    errors.append(f"institution {name!r}: not referenced by any lab")

  if errors:
    sys.exit("data errors:\n  " + "\n  ".join(errors))
  papers.sort(key=lambda p: (p["date"], p["title"]))
  return papers, labs, institutions


def cell(text: str) -> str:
  return text.replace("|", "\\|")


def short_name(p: dict) -> str:
  if "short" in p:
    return p["short"]
  head = p["title"].split(":")[0]
  return head if len(head) <= 45 else head[:42] + "…"


def group_label(lab: dict) -> str:
  parts = [x for x in (lab.get("name"), lab.get("pi")) if x]
  return " — ".join(parts) or "—"


def who(p: dict, labs: dict) -> str:
  if "lab" not in p:
    return "—"
  lab = labs[p["lab"]]
  return ", ".join(x for x in (lab.get("pi"), lab["institution"]) if x)


def render_papers(sport: str, papers: list[dict], labs: dict) -> str:
  rows = [p for p in papers if sport in p["sport"]]
  if not rows:
    return EMPTY
  out = [
    "| Date | Paper | Venue | Robot | Real | Group | Links |",
    "|---|---|---|---|---|---|---|",
  ]
  for p in rows:
    links = []
    if p.get("project"):
      links.append(f"[project]({p['project']})")
    if p.get("code") == "soon":
      links.append("code (soon)")
    elif p.get("code"):
      links.append(f"[code]({p['code']})")
    venue = "📣 Announced" if p["status"] == "announced" else cell(p["venue"])
    row = [
      p["date"],
      f"[{cell(p['title'])}]({p['paper']})",
      venue,
      cell(p.get("robot", "—")),
      "✅" if p["real"] else "🖥️",
      cell(who(p, labs)),
      " · ".join(links) or "—",
    ]
    out.append("| " + " | ".join(row) + " |")
  return "\n".join(out) + "\n"


def works_of(lab_ids: set[str], papers: list[dict]) -> list[dict]:
  return [p for p in papers if p.get("lab") in lab_ids]


def render_map(papers: list[dict], labs: dict, institutions: dict) -> str:
  features = []
  for name, inst in sorted(institutions.items()):
    inst_labs = sorted(
      (lab for lab in labs.values() if lab["institution"] == name),
      key=group_label,
    )
    works = works_of({lab["id"] for lab in inst_labs}, papers)
    sports = {s for p in works for s in p["sport"]}
    properties = {
      "Institution": name,
      "Sports": " · ".join(f"{e} {n}" for key, (e, n) in SPORTS.items() if key in sports),
    }
    for lab in inst_labs:
      properties[group_label(lab)] = " · ".join(
        f"{short_name(p)} ({p['date']})" for p in works_of({lab["id"]}, papers)
      )
    features.append({
      "type": "Feature",
      "geometry": {"type": "Point", "coordinates": [inst["lon"], inst["lat"]]},
      "properties": properties,
    })
  body = ",\n".join(json.dumps(f, ensure_ascii=False) for f in features)
  return f'```geojson\n{{"type": "FeatureCollection", "features": [\n{body}\n]}}\n```\n'


def render_stats(papers: list[dict], labs: dict, institutions: dict) -> str:
  return f"**{len(papers)}** works · **{len(labs)}** groups · **{len(institutions)}** institutions\n"


def render(text: str, papers: list[dict], labs: dict, institutions: dict) -> str:
  covered = set()

  def replace(match: re.Match) -> str:
    key = match.group(2)
    if key.startswith("papers/") and key.removeprefix("papers/") in SPORTS:
      sport = key.removeprefix("papers/")
      covered.add(sport)
      body = render_papers(sport, papers, labs)
    elif key == "map":
      body = render_map(papers, labs, institutions)
    elif key == "stats":
      body = render_stats(papers, labs, institutions)
    else:
      sys.exit(f"README.md: unknown block <!-- gen:{key} -->")
    return match.group(1) + body + match.group(3)

  result = BLOCK.sub(replace, text)
  orphans = [p["title"] for p in papers if not set(p["sport"]) <= covered]
  if orphans:
    sys.exit("no README block renders these papers:\n  " + "\n  ".join(orphans))
  return result


def main() -> None:
  parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
  parser.add_argument("--check", action="store_true", help="fail if README.md is out of date")
  args = parser.parse_args()

  papers, labs, institutions = load()
  current = README.read_text()
  rendered = render(current, papers, labs, institutions)
  if args.check:
    if rendered != current:
      sys.exit("README.md is out of date: run `uv run scripts/build.py`")
    print("README.md is up to date")
  else:
    README.write_text(rendered)
    print(f"wrote {README.relative_to(ROOT)}")


if __name__ == "__main__":
  main()
