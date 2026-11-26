#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds Systema Camporum: standalone interactive HTML atlas, favicon.svg, .nojekyll + 12 print-ready SVG plates."""
from pathlib import Path
from src.data_overview import ACTS, BOARD_LANES, FIVE_FLOORS, MIRROR_TRAPS, SPEC_COMPARISON_ROWS, SIX_THREADS
from src.data_journey import JOURNEY_STOPS
from src.data_equations import MASTER_EQUATIONS
from src.data_tree_and_how import TREE_NODES, MYTHS_AND_TRAPS, EMPIRICAL_LEDGER, BOOKS_COMPENDIUM
from src.svg_plates import build_plates
from src.template_app import render_app

ROOT = Path(__file__).resolve().parent

FAVICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="14" fill="#121726"/>
  <polygon points="28,12 12,50 44,50" fill="#192036" stroke="#eff3fc" stroke-width="2.5"/>
  <line x1="35" y1="24" x2="54" y2="15" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
  <line x1="37" y1="29" x2="54" y2="24" stroke="#2dd4bf" stroke-width="3" stroke-linecap="round"/>
  <line x1="39" y1="34" x2="54" y2="33" stroke="#fbbf24" stroke-width="3" stroke-linecap="round"/>
  <line x1="41" y1="39" x2="54" y2="42" stroke="#818cf8" stroke-width="3" stroke-linecap="round"/>
  <line x1="42" y1="44" x2="54" y2="51" stroke="#f472b6" stroke-width="3" stroke-linecap="round"/>
</svg>
"""


def main():
    plates_inline = build_plates(standalone=False)
    plates_print = build_plates(standalone=True)

    out_plates = ROOT / "plates"
    out_plates.mkdir(parents=True, exist_ok=True)
    for p in plates_print:
        (out_plates / f'{p["slug"]}.svg').write_text(p["svg"], encoding="utf-8")

    html_doc = render_app(
        ACTS,
        BOARD_LANES,
        FIVE_FLOORS,
        MIRROR_TRAPS,
        SPEC_COMPARISON_ROWS,
        SIX_THREADS,
        JOURNEY_STOPS,
        MASTER_EQUATIONS,
        TREE_NODES,
        MYTHS_AND_TRAPS,
        EMPIRICAL_LEDGER,
        BOOKS_COMPENDIUM,
        plates_inline,
    )
    (ROOT / "index.html").write_text(html_doc, encoding="utf-8")
    (ROOT / "favicon.svg").write_text(FAVICON_SVG, encoding="utf-8")
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Built {ROOT / 'index.html'} ({len(html_doc):,} bytes), favicon.svg, .nojekyll, and {len(plates_print)} standalone SVG plates.")


if __name__ == "__main__":
    main()
