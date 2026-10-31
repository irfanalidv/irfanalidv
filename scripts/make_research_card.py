"""Generate assets/research.svg: key results from the two published papers.

All numbers are quoted from the published abstracts (Crossref records for the DOIs below).
Static content, so this is run by hand, not by the daily workflow.
"""

from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets" / "research.svg"
SANS = "ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"

PAPERS = [
    {
        "kicker": "IJAINN  ·  DEC 2025  ·  SOLE AUTHOR",
        "title": ["Mental-health conversation AI,", "benchmarked on MentalChat16K"],
        "data": "16,084 therapy conversations  ·  6,338 real clinical",
        "stats": [
            ("86.7%", "BERT accuracy"),
            ("86.1%", "BERT F1 score"),
            ("p < 0.05", "McNemar + bootstrap CIs"),
            ("5-fold", "stratified cross-validation"),
        ],
        "doi": "doi.org/10.54105/ijainn.a1112.06011225",
    },
    {
        "kicker": "IJAINN  ·  OCT 2025  ·  SOLE AUTHOR",
        "title": ["How customer topics change over", "time, on Yelp restaurant reviews"],
        "data": "3,000 reviews  ·  1,467 businesses  ·  248 metros  ·  2005–2018",
        "stats": [
            ("97.2%", "entity recognition F1"),
            ("87.5%", "topic diversity, 8 topics"),
            ("17.9%", "sentiment forecast error (MAE)"),
            ("p < 0.05", "regional differences, 10 cities"),
        ],
        "doi": "doi.org/10.54105/ijainn.F1106.05061025",
    },
]


def text(x, y, s, size, fill, *, weight="400", family=SANS, spacing=None):
    ls = f' letter-spacing="{spacing}"' if spacing else ""
    return (
        f'<text x="{x}" y="{y}" fill="{fill}" font-family="{family}" font-size="{size}" '
        f'font-weight="{weight}"{ls}>{escape(s)}</text>'
    )


def main() -> None:
    width, height, pad, col_w, gutter = 1200, 470, 48, 540, 24
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="t d">',
        '<title id="t">Published research</title>',
        '<desc id="d">Two sole-author journal papers. MentalChat16K: BERT 86.7% accuracy, 86.1% F1 on '
        "16,084 conversations, significance-tested. Yelp topic evolution: 97.2% entity recognition F1, "
        "87.5% topic diversity, 17.9% forecast error, significant regional differences.</desc>",
        "<defs>",
        '<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#0B132B"/><stop offset="1" stop-color="#13203F"/></linearGradient>',
        '<pattern id="grid" width="48" height="48" patternUnits="userSpaceOnUse">'
        '<path d="M48 0H0V48" fill="none" stroke="#FFFFFF" stroke-opacity="0.045"/></pattern>',
        "</defs>",
        f'<rect width="{width}" height="{height}" rx="14" fill="url(#bg)"/>',
        f'<rect width="{width}" height="{height}" rx="14" fill="url(#grid)"/>',
        f'<rect x="0" y="14" width="6" height="{height - 28}" fill="#00D1D1"/>',
        text(pad + 24, 58, "PUBLISHED RESEARCH  ·  PEER-REVIEWED  ·  OPEN ACCESS  ·  IISER TIRUPATI", 14, "#00D1D1",
             family=MONO, spacing="2.4"),
    ]
    for i, p in enumerate(PAPERS):
        x0 = pad + 24 + i * (col_w + gutter)
        y0 = 84
        parts.append(
            f'<rect x="{x0 - 20}" y="{y0}" width="{col_w}" height="{height - y0 - 32}" rx="12" '
            'fill="#FFFFFF" fill-opacity="0.04" stroke="#FFFFFF" stroke-opacity="0.08"/>'
        )
        parts.append(text(x0, y0 + 36, p["kicker"], 12, "#94A3B8", family=MONO, spacing="1.6"))
        parts.append(text(x0, y0 + 70, p["title"][0], 22, "#FFFFFF", weight="700"))
        parts.append(text(x0, y0 + 98, p["title"][1], 22, "#FFFFFF", weight="700"))
        parts.append(text(x0, y0 + 128, p["data"], 14, "#CBD5E1"))
        for j, (value, label) in enumerate(p["stats"]):
            sx = x0 + (j % 2) * 255
            sy = y0 + 178 + (j // 2) * 82
            parts.append(f'<rect x="{sx}" y="{sy - 34}" width="3" height="52" rx="1.5" fill="#00D1D1"/>')
            parts.append(text(sx + 14, sy, value, 30, "#FFFFFF", weight="700"))
            parts.append(text(sx + 14, sy + 22, label, 13, "#94A3B8"))
        parts.append(text(x0, height - 56, p["doi"], 12, "#64748B", family=MONO))
    parts.append("</svg>")
    OUT.write_text("\n".join(parts) + "\n")


if __name__ == "__main__":
    main()
