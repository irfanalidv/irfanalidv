"""Refresh the open-source section of the profile README and the impact card.

Run daily by .github/workflows/stats.yml. Standard library only.

- Pulls per-package numbers from PyPI (versions, releases, first upload),
  pepy.tech (all-time downloads), pypistats.org (last 30 days) and GitHub (stars).
- Writes assets/impact.svg and the table between the LIBS markers in README.md.
- If a source is unreachable, the last known value in assets/stats.json is kept,
  so a flaky API never zeroes out the profile.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import urllib.request
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
CARD = ROOT / "assets" / "impact.svg"
CACHE = ROOT / "assets" / "stats.json"
OWNER = "irfanalidv"

# (display name, PyPI name, GitHub repo, one-line description)
LIBRARIES = [
    (
        "RAGNav",
        "ragnav",
        "RAGNav",
        "Search that combines keyword matching with meaning-based matching, so a question can be "
        "found either way. Answers cite the passage they came from",
    ),
    (
        "ragfallback",
        "ragfallback",
        "ragfallback",
        "Stops a search-and-answer system failing quietly. Rewrites weak queries, scores how "
        "confident the results are, and falls back when they're poor",
    ),
    (
        "AgentEnsemble",
        "agentensemble",
        "AgentEnsemble",
        "Running several AI agents together: routing work between them, planning, and tracking "
        "what it costs. Works with OpenAI or Mistral",
    ),
    (
        "nepal-gov-agent",
        "nepal-gov-agent",
        "Nepal-Gov-Agent",
        "Answers questions about Nepal government policy and legal documents, in Nepali and "
        "English, citing the sentence each answer came from",
    ),
    (
        "AgentCare",
        "agentcare",
        "AgentCare",
        "Voice AI for healthcare: call intake, pulling out the details that matter, chasing "
        "missing information, booking appointments",
    ),
    (
        "AskPandas",
        "askpandas",
        "AskPandas",
        "Ask questions about a CSV in plain English. Runs on a local model by default, so nothing "
        "leaves your computer, or on OpenAI / Mistral",
    ),
    (
        "lingo-nlp-toolkit",
        "lingo-nlp-toolkit",
        "lingo-nlp-toolkit",
        "Text-processing toolkit on Hugging Face models: classification, entities, sentiment, "
        "question answering, summarisation, embeddings",
    ),
    (
        "PyroChain",
        "pyrochain",
        "PyroChain",
        "Using AI agents and a fine-tuned language model to work out which features matter in a "
        "dataset",
    ),
    (
        "toxic-comment-classifier",
        "toxic_comment_classifier",
        "toxic_comment_classifier",
        "Detects toxic comments, with a score per category (toxic, insult, threat and more)",
    ),
]


def fetch(url: str, *, raw: bool = False, headers: dict | None = None):
    req = urllib.request.Request(url, headers={"User-Agent": f"{OWNER}-profile-stats", **(headers or {})})
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = resp.read().decode()
    return body if raw else json.loads(body)


def parse_count(text: str) -> int:
    """'16k' -> 16000, '1.2M' -> 1200000, '987' -> 987."""
    m = re.fullmatch(r"([\d.,]+)\s*([kKmM]?)", text.strip())
    if not m:
        raise ValueError(text)
    value = float(m.group(1).replace(",", ""))
    return int(value * {"": 1, "k": 1_000, "m": 1_000_000}[m.group(2).lower()])


def human(n: int) -> str:
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M".replace(".0M", "M")
    if n >= 1_000:
        return f"{n / 1_000:.1f}k".replace(".0k", "k")
    return str(n)


def collect() -> list[dict]:
    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    gh_headers = {"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"} if os.getenv("GITHUB_TOKEN") else {}
    rows = []
    for name, pkg, repo, desc in LIBRARIES:
        old = cache.get(pkg, {})
        row = {"name": name, "pkg": pkg, "repo": repo, "desc": desc, **{k: old.get(k) for k in
               ("downloads", "monthly", "releases", "first", "version", "stars")}}
        try:
            info = fetch(f"https://pypi.org/pypi/{pkg}/json")
            uploads = [f["upload_time_iso_8601"] for files in info["releases"].values() for f in files]
            row["first"] = min(uploads)[:10]
            row["releases"] = sum(1 for files in info["releases"].values() if files)
            row["version"] = info["info"]["version"]
        except Exception as exc:  # keep cached values
            print(f"pypi {pkg}: {exc}")
        try:
            svg = fetch(f"https://static.pepy.tech/badge/{pkg}", raw=True)
            row["downloads"] = parse_count(re.findall(r">([\d.,]+\s*[kKmM]?)</text>", svg)[-1])
        except Exception as exc:
            print(f"pepy {pkg}: {exc}")
        try:
            row["monthly"] = fetch(f"https://pypistats.org/api/packages/{pkg}/recent")["data"]["last_month"]
        except Exception as exc:
            print(f"pypistats {pkg}: {exc}")
        try:
            row["stars"] = fetch(f"https://api.github.com/repos/{OWNER}/{repo}", headers=gh_headers)[
                "stargazers_count"
            ]
        except Exception as exc:
            print(f"github {repo}: {exc}")
        rows.append(row)
    rows.sort(key=lambda r: r["downloads"] or 0, reverse=True)
    CACHE.parent.mkdir(exist_ok=True)
    CACHE.write_text(json.dumps({r["pkg"]: {k: v for k, v in r.items() if k != "desc"} for r in rows}, indent=2) + "\n")
    return rows


# ── impact card ──────────────────────────────────────────────────────────────

SANS = "ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"


def render_card(rows: list[dict], today: dt.date) -> str:
    total = sum(r["downloads"] or 0 for r in rows)
    releases = sum(r["releases"] or 0 for r in rows)
    first_year = min(r["first"] for r in rows if r["first"])[:4]

    width, bar_top, bar_h, gap = 1200, 250, 22, 14
    height = bar_top + len(rows) * (bar_h + gap) + 56
    label_x, bar_x, bar_max = 72, 330, 720
    peak = max(r["downloads"] or 0 for r in rows) or 1

    stats = [
        (f"{human(total)}+", "total downloads"),
        (str(len(rows)), "libraries on PyPI"),
        (str(releases), "releases shipped"),
        ("3.10–3.13", "CI-tested Python versions"),
    ]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="t d">',
        '<title id="t">Open-source impact</title>',
        f'<desc id="d">{len(rows)} Python libraries on PyPI, {human(total)}+ total downloads, '
        f"{releases} releases, maintained since {first_year}.</desc>",
        "<defs>",
        '<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#0B132B"/><stop offset="1" stop-color="#13203F"/></linearGradient>',
        '<linearGradient id="bar" x1="0" y1="0" x2="1" y2="0">'
        '<stop offset="0" stop-color="#00D1D1"/><stop offset="1" stop-color="#3B82F6"/></linearGradient>',
        '<pattern id="grid" width="48" height="48" patternUnits="userSpaceOnUse">'
        '<path d="M48 0H0V48" fill="none" stroke="#FFFFFF" stroke-opacity="0.045"/></pattern>',
        "</defs>",
        f'<rect width="{width}" height="{height}" rx="14" fill="url(#bg)"/>',
        f'<rect width="{width}" height="{height}" rx="14" fill="url(#grid)"/>',
        f'<rect x="0" y="14" width="6" height="{height - 28}" fill="#00D1D1"/>',
        f'<text x="72" y="62" fill="#00D1D1" font-family="{MONO}" font-size="14" letter-spacing="2.4">'
        "OPEN-SOURCE IMPACT  &#183;  PYTHON LIBRARIES ON PYPI</text>",
    ]
    for i, (value, label) in enumerate(stats):
        x = 72 + i * 270
        parts.append(
            f'<text x="{x}" y="132" fill="#FFFFFF" font-family="{SANS}" font-size="46" font-weight="700">'
            f"{escape(value)}</text>"
        )
        parts.append(
            f'<text x="{x}" y="162" fill="#94A3B8" font-family="{SANS}" font-size="16">{escape(label)}</text>'
        )
    parts.append(f'<rect x="72" y="192" width="{width - 144}" height="1" fill="#FFFFFF" fill-opacity="0.12"/>')
    parts.append(
        f'<text x="72" y="228" fill="#E2E8F0" font-family="{SANS}" font-size="15" font-weight="600">'
        "All-time downloads by library</text>"
    )
    for i, r in enumerate(rows):
        y = bar_top + i * (bar_h + gap)
        w = max(4, round(bar_max * (r["downloads"] or 0) / peak))
        parts.append(
            f'<text x="{label_x}" y="{y + 16}" fill="#E2E8F0" font-family="{MONO}" font-size="14">'
            f"{escape(r['name'])}</text>"
        )
        parts.append(f'<rect x="{bar_x}" y="{y}" width="{bar_max}" height="{bar_h}" rx="5" fill="#FFFFFF" fill-opacity="0.05"/>')
        parts.append(f'<rect x="{bar_x}" y="{y}" width="{w}" height="{bar_h}" rx="5" fill="url(#bar)"/>')
        parts.append(
            f'<text x="{bar_x + bar_max + 16}" y="{y + 16}" fill="#FFFFFF" font-family="{SANS}" '
            f'font-size="14" font-weight="600">{human(r["downloads"] or 0)}'
            f'<tspan fill="#94A3B8" font-weight="400">  &#183;  v{escape(r["version"] or "?")}</tspan></text>'
        )
    parts.append(
        f'<text x="72" y="{height - 24}" fill="#64748B" font-family="{SANS}" font-size="13">'
        f"Maintained since {first_year}  &#183;  updated {today.isoformat()} by a daily GitHub "
        "Action  &#183;  all-time downloads from pepy.tech</text>"
    )
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


# ── README table ─────────────────────────────────────────────────────────────


def badge(image_url: str, link: str, alt: str) -> str:
    return f"[![{alt}]({image_url})]({link})"


def render_table(rows: list[dict]) -> str:
    lines = [
        "| Library | What it does | Live stats |",
        "| --- | --- | --- |",
    ]
    for r in rows:
        pkg, repo = r["pkg"], r["repo"]
        stats = " ".join(
            [
                badge(f"https://img.shields.io/pypi/v/{pkg}?style=flat-square&logo=pypi&logoColor=white&label=PyPI&color=3775A9",
                      f"https://pypi.org/project/{pkg}/", "PyPI version"),
                badge(f"https://img.shields.io/pepy/dt/{pkg}?style=flat-square&label=downloads&color=00A3A3",
                      f"https://pepy.tech/projects/{pkg}", "Total downloads"),
            ]
        )
        lines.append(f"| [**{r['name']}**](https://github.com/{OWNER}/{repo}) | {r['desc']} | {stats} |")
    return "\n".join(lines)


def main() -> None:
    today = dt.datetime.now(dt.timezone.utc).date()
    rows = collect()
    CARD.write_text(render_card(rows, today))
    text = README.read_text()
    new = re.sub(
        r"(<!-- LIBS:START -->\n).*?(<!-- LIBS:END -->)",
        lambda m: m.group(1) + render_table(rows) + "\n" + m.group(2),
        text,
        flags=re.S,
    )
    if new == text and "<!-- LIBS:START -->" not in text:
        raise SystemExit("README is missing the <!-- LIBS:START --> / <!-- LIBS:END --> markers")
    README.write_text(new)
    for r in rows:
        print(f"{r['name']:26} {human(r['downloads'] or 0):>6}  {r['monthly']}/mo  v{r['version']}  ★{r['stars']}")


if __name__ == "__main__":
    main()
