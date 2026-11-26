# -*- coding: utf-8 -*-
"""Renders the complete standalone HTML edition of Systema Camporum (Graduate QFT & The Standard Model)."""
import html
import json
from src.template_css import APP_CSS
from src.template_js import APP_JS


def esc(s: str) -> str:
    return html.escape(str(s), quote=True)


def render_app(acts, lanes, floors, traps, spec_rows, threads, stops, equations, tree_nodes, myths, ledger, books, plates) -> str:
    plates_by_id = {p["id"]: p for p in plates}
    acts_by_id = {a["id"]: a for a in acts}

    # 1. Five Floors buttons (DOM order 1..5, visually stacked ground-up via column-reverse!)
    floors_btns_html = ""
    for i, fl in enumerate(floors):
        pr = "true" if i == 0 else "false"
        floors_btns_html += (
            f'<button type="button" class="floor-btn" data-floor="{i}" aria-pressed="{pr}" style="--fc:{fl["color"]}" onclick="selectFloor({i})">'
            f'<span class="floor-bar" aria-hidden="true"></span>'
            f'<span><strong style="display:block;font-size:16px;margin-block-end:2px;">{esc(fl["name"])}</strong>'
            f'<span style="font-size:14px;color:var(--ink-2);">{esc(fl["one_line"])}</span></span>'
            f'<span style="font-family:var(--mono);font-size:12px;color:var(--ink-3);white-space:nowrap;">{esc(fl["badge"])}</span>'
            f'</button>'
        )

    # 2. Cold-Open QM Intuition Traps
    traps_html = ""
    for idx, tr in enumerate(traps):
        traps_html += (
            f'<article class="trap-quiz-card">'
            f'<div>'
            f'<span class="pill-tag"><strong style="color:var(--c-crisis);">{esc(tr["num"])}</strong> {esc(tr["tag"])}</span>'
            f'<h3 style="font-size:17.5px;margin-block-end:6px;">{esc(tr["title"])}</h3>'
            f'<p style="font-size:14px;color:var(--ink-2);">{esc(tr["q"])}</p>'
            f'</div>'
            f'<div>'
            f'<div class="quiz-choices">'
            f'<button type="button" class="quiz-opt" onclick="answerMirrorTrap({idx}, \'trap\')">{esc(tr["opt_trap"])}</button>'
            f'<button type="button" class="quiz-opt" onclick="answerMirrorTrap({idx}, \'wise\')">{esc(tr["opt_wise"])}</button>'
            f'</div>'
            f'<div id="trap-rev-{idx}" class="quiz-reveal" hidden style="margin-block-start:10px;"></div>'
            f'</div></article>'
        )

    # 3. 8-Part Field Spec-Sheet Comparison Table
    spec_rows_html = ""
    for r in spec_rows:
        spec_rows_html += (
            f'<tr>'
            f'<th scope="row">{esc(r["part"])}</th>'
            f'<td>{esc(r["free_kg"])}</td>'
            f'<td>{esc(r["phi4"])}</td>'
            f'<td>{esc(r["qed"])}</td>'
            f'<td>{esc(r["qcd"])}</td>'
            f'<td>{esc(r["sm"])}</td>'
            f'</tr>'
        )

    # 4. Six Threads buttons
    threads_btns_html = ""
    for i, th in enumerate(threads):
        pr = "true" if i == 0 else "false"
        threads_btns_html += (
            f'<button type="button" class="thread-btn" data-thread="{i}" aria-pressed="{pr}" onclick="selectThread({i})">'
            f'<span style="display:block;font-family:var(--mono);font-size:11.5px;color:var(--ink-3);margin-block-end:3px;">{esc(th["tag"])}</span>'
            f'{esc(th["q"])}</button>'
        )

    # 5. Journey Act Rail, Stop Scrubber & 7-Act Staircase Syllabus
    act_rail_html = ""
    for i, ac in enumerate(acts):
        pr = "true" if i == 0 else "false"
        act_rail_html += (
            f'<button type="button" class="act-pill" data-act="{ac["id"]}" aria-pressed="{pr}" style="--ac:{ac["color"]}" onclick="jumpActFirstStop(\'{ac["id"]}\')">'
            f'<span style="display:block;font-family:var(--mono);font-size:11.5px;font-weight:800;color:{ac["color"]};">Act {ac["roman"]} · {esc(ac["stops_span"])}</span>'
            f'<strong style="font-size:12.5px;">{esc(ac["name"])}</strong></button>'
        )

    stop_dots_html = ""
    for idx, st in enumerate(stops):
        ac = acts_by_id[st["act"]]
        cur = ' aria-current="step"' if idx == 0 else ""
        cr_cls = " is-crisis" if st["crisis_flag"] else ""
        stop_dots_html += (
            f'<button type="button" class="stop-dot{cr_cls}" data-sidx="{idx}"{cur} style="--sc:{ac["color"]}" '
            f'title="Stop {st["num"]}: {esc(st["title"])}" onclick="goToStop({idx})">{st["num"]:02d}</button>'
        )

    stairs_html = ""
    for ac in acts:
        ac_stops = [s for s in stops if s["act"] == ac["id"]]
        cards = ""
        for s in ac_stops:
            s_idx = s["num"] - 1
            cr_badge = '<span class="pill-tag" style="margin:0;color:var(--c-crisis);">CRISIS</span>' if s["crisis_flag"] else ""
            cards += (
                f'<article class="eq-meta-box" style="cursor:pointer;border-color:color-mix(in srgb, {ac["color"]} 35%, var(--line));" onclick="goToStop({s_idx})">'
                f'<div style="display:flex;justify-content:space-between;align-items:center;gap:6px;margin-block-end:4px;">'
                f'<span style="font-family:var(--mono);font-size:12px;font-weight:800;color:{ac["color"]};">Stop {s["num"]:02d}</span>'
                f'{cr_badge}</div>'
                f'<strong style="display:block;font-size:15px;margin-block-end:4px;">{esc(s["title"])}</strong>'
                f'<p style="font-size:13px;color:var(--ink-2);margin:0;">{esc(s["eq_plain_read"])}</p>'
                f'</article>'
            )
        stairs_html += (
            f'<div class="sec-card" style="border-block-start:4px solid {ac["color"]};">'
            f'<span class="eyebrow" style="color:{ac["color"]};">Act {ac["roman"]} · {esc(ac["stops_span"])} · {esc(ac["lead_books"])}</span>'
            f'<h3 style="font-size:22px;margin-block-end:4px;">{esc(ac["name"])}</h3>'
            f'<p style="color:var(--ink-2);font-size:14.5px;margin-block-end:14px;">{esc(ac["summary"])}</p>'
            f'<div class="cards-3">{cards}</div>'
            f'</div>'
        )

    # 6. Equation Dissector Picker Buttons
    eq_btns_html = ""
    for idx, eq in enumerate(equations):
        ac = acts_by_id[eq["act"]]
        pr = "true" if idx == 0 else "false"
        eq_btns_html += (
            f'<button type="button" class="tool-pill eq-pick-btn" data-eqidx="{idx}" aria-pressed="{pr}" onclick="selectEquation({idx})">'
            f'<span style="font-family:var(--mono);color:{ac["color"]};">#{eq["num"]}</span> '
            f'<span>{esc(eq["title"].split("(")[0].strip())}</span></button>'
        )

    # 7. How We Know: 10 Myths & Sign Traps + Empirical Table + 6 Books + 12 Vector Plates
    myths_html = ""
    for m in myths:
        myths_html += (
            f'<article class="sec-card" style="margin-block-end:0;padding:20px;border-color:color-mix(in srgb, var(--c-crisis) 30%, var(--line));">'
            f'<div style="display:flex;justify-content:space-between;align-items:center;gap:8px;margin-block-end:6px;">'
            f'<span class="pill-tag" style="margin:0;color:var(--c-crisis);">Trap #{m["num"]:02d} · {esc(m["cat"])}</span>'
            f'<button type="button" class="tool-pill" onclick="switchView(\'journey\', \'{m["stop"]}\', true)">{m["stop"].upper()} →</button>'
            f'</div>'
            f'<p style="font-weight:800;font-size:15.5px;color:var(--c-crisis);margin-block-end:6px;">{esc(m["myth"])}</p>'
            f'<p style="font-weight:700;font-size:14.5px;color:var(--c-act2);margin-block-end:6px;">✓ QFT Reality: {esc(m["truth"])}</p>'
            f'<p style="font-size:13.5px;color:var(--ink-2);margin:0;">{esc(m["detail"])}</p>'
            f'</article>'
        )

    ledger_rows_html = ""
    for row in ledger:
        ledger_rows_html += (
            f'<tr>'
            f'<th scope="row">{esc(row["observable"])}</th>'
            f'<td>{esc(row["sector"])}</td>'
            f'<td style="font-family:var(--mono);font-size:13px;">{esc(row["theory"])}</td>'
            f'<td style="font-family:var(--mono);font-size:13px;">{esc(row["exp"])}</td>'
            f'<td><strong style="color:var(--c-act2);">{esc(row["precision"])}</strong></td>'
            f'<td><a href="{esc(row["url"])}" target="_blank" rel="noopener noreferrer">{esc(row["ref_label"])} ↗</a></td>'
            f'</tr>'
        )

    books_html = ""
    for bk in books:
        extra_link = ""
        if "url2" in bk:
            extra_link = f' <a class="tool-pill" href="{esc(bk["url2"])}" target="_blank" rel="noopener noreferrer">Standard Model Notes PDF ↗</a>'
        books_html += (
            f'<article class="sec-card" style="margin-block-end:0;padding:20px;border-block-start:4px solid {bk["color"]};">'
            f'<div style="display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap;margin-block-end:6px;">'
            f'<span class="pill-tag" style="margin:0;color:{bk["color"]};">{esc(bk["metric"])}</span>'
            f'<span class="pill-tag" style="margin:0;">{esc(bk["access"])}</span>'
            f'</div>'
            f'<h3 style="font-size:19px;margin-block-end:4px;">{esc(bk["title"])}</h3>'
            f'<p style="font-family:var(--mono);font-size:12.5px;color:var(--ink-3);margin-block-end:8px;">{esc(bk["author"])}</p>'
            f'<p style="font-size:14px;color:var(--ink-2);margin-block-end:12px;"><strong>What we took for Systema Camporum:</strong> {esc(bk["best_for"])}</p>'
            f'<div style="display:flex;flex-wrap:wrap;gap:8px;">'
            f'<a class="tool-pill" href="{esc(bk["url"])}" target="_blank" rel="noopener noreferrer">Open Official Resource / PDF ↗</a>'
            f'{extra_link}</div></article>'
        )

    plates_gallery_html = ""
    for p in plates:
        svg_href = f'plates/{p["slug"]}.svg'
        plates_gallery_html += (
            f'<figure class="sec-card" style="margin-block-end:16px;">'
            f'<div style="display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap;margin-block-end:8px;">'
            f'<div><span class="eyebrow" style="margin:0;">{esc(p["act"])}</span>'
            f'<h3 style="font-size:19px;margin:0;">{esc(p["title"])}</h3></div>'
            f'<a class="tool-pill" href="{esc(svg_href)}" download="{esc(p["slug"])}.svg">Download Print SVG ↓</a>'
            f'</div>'
            f'<div class="plate-svg-wrap">{p["svg"]}</div>'
            f'<figcaption style="font-size:14px;color:var(--ink-2);margin-block-start:8px;">{esc(p["say"])}</figcaption>'
            f'</figure>'
        )

    payload = json.dumps({
        "acts": acts,
        "lanes": lanes,
        "floors": floors,
        "traps": traps,
        "threads": threads,
        "stops": stops,
        "equations": equations,
        "tree": tree_nodes,
        "plates": plates,
    }, ensure_ascii=False)

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="color-scheme" content="light dark">
  <script>
    try {{
      document.querySelector('meta[name="color-scheme"]').content = localStorage.getItem("sc-color-scheme") ?? "light dark";
    }} catch (e) {{}}
  </script>
  <title>Systema Camporum · Graduate Quantum Field Theory &amp; The Standard Model</title>
  <meta name="description" content="A Systema Intelligentiae step-by-step architecture for mastering graduate Quantum Field Theory and the Standard Model—merging Tong, Schwartz, Srednicki, Peskin &amp; Schroeder, and Weinberg.">
  <meta property="og:title" content="Systema Camporum · Graduate QFT &amp; The Standard Model">
  <meta property="og:description" content="24 step-by-step graduate lessons, 10 interactive decoded equations, live (+−−−) ↔ (−+++) metric translator, 8-part repeating field board, and 5 physics simulators.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://tuanucsb.github.io/systema-qft/">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600..900;1,9..144,600..800&family=JetBrains+Mono:wght@500;700&family=Plus+Jakarta+Sans:wght@400..800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" crossorigin="anonymous">
  <style>{APP_CSS}</style>
</head>
<body>
  <a href="#main-heading" class="skip-link visually-hidden">Skip to main content</a>
  <div id="srAnnouncer" class="visually-hidden" aria-live="polite"></div>

  <header class="site-head">
    <div class="head-wrap">
      <a class="brand" href="#overview" onclick="switchView('overview', null, true);return false;">
        <span class="brand-mark" aria-hidden="true">
          <i style="background:var(--c-act1)"></i><i style="background:var(--c-act2)"></i><i style="background:var(--c-act3)"></i>
          <i style="background:var(--c-act4)"></i><i style="background:var(--c-act5)"></i><i style="background:var(--c-act6)"></i>
          <i style="background:var(--c-act7)"></i>
        </span>
        <span lang="la">Systema Camporum</span>
        <span class="brand-sub">Grad QFT &amp; SM</span>
      </a>

      <nav class="site-nav" aria-label="Primary sections">
        <button type="button" class="nav-link" data-nav-view="overview" aria-current="page" onclick="switchView('overview', null, true)">Overview</button>
        <button type="button" class="nav-link" data-nav-view="journey" onclick="switchView('journey', null, true)">Journey <span class="nav-count">24</span></button>
        <button type="button" class="nav-link" data-nav-view="equations" onclick="switchView('equations', null, true)">Equations <span class="nav-count">10</span></button>
        <button type="button" class="nav-link" data-nav-view="tree" onclick="switchView('tree', null, true)">Tree <span class="nav-count">28</span></button>
        <button type="button" class="nav-link" data-nav-view="labs" onclick="switchView('labs', null, true)">5 Labs</button>
        <button type="button" class="nav-link" data-nav-view="how" onclick="switchView('how', null, true)">How &amp; Books</button>
      </nav>

      <div class="head-tools">
        <button type="button" id="metricBtn" class="tool-pill" aria-pressed="false" onclick="toggleMetric()" title="Toggle between West Coast (+---) and East Coast (-+++) metric conventions">
          <span style="font-family:var(--mono);color:var(--c-act5);">(+ − − −)</span> <span>Tong / Schwartz</span>
        </button>
        <button type="button" id="expertBtn" class="tool-pill" aria-pressed="false" onclick="toggleExpertMode()">
          <span>Grad Proofs</span>
        </button>
        <button type="button" id="themeBtn" class="tool-pill" onclick="toggleColorScheme()" aria-label="Switch color scheme">
          <span id="themeBtnLabel">Dark</span>
        </button>
      </div>
    </div>
  </header>

  <main class="wrap">
    <!-- ================================================================
         VIEW 1: OVERVIEW (5 FLOORS, 3 TRAPS, 8-PART SPEC TABLE, 6 THREADS)
         ================================================================ -->
    <section id="view-overview">
      <div class="hero-grid">
        <div>
          <span class="eyebrow">Systema Intelligentiae Architecture · Graduate QFT &amp; Standard Model Synthesis</span>
          <h1 id="main-heading" tabindex="-1" class="hero-title">
            How spacetime learned to <em class="hero-accent">weave particles &amp; forces</em>
          </h1>
          <div class="spectrum-bar" aria-hidden="true">
            <span style="background:var(--c-act1)"></span><span style="background:var(--c-act2)"></span>
            <span style="background:var(--c-act3)"></span><span style="background:var(--c-act4)"></span>
            <span style="background:var(--c-act5)"></span><span style="background:var(--c-act6)"></span>
            <span style="background:var(--c-act7)"></span>
          </div>
          <p class="lede">
            Graduate Quantum Field Theory often feels like drinking from a firehose of gamma matrices and sign conventions.
            <strong lang="la">Systema Camporum</strong> merges the clearest intuition of <strong>Tong</strong>, the modern EFT vision of <strong>Schwartz</strong>, the path-integral modularity of <strong>Srednicki</strong>, the calculation craft of <strong>Peskin &amp; Schroeder</strong>, and the symmetry inevitability of <strong>Weinberg</strong> into one step-by-step system.
          </p>
          <div class="edition-ledger">
            <span><strong>24</strong> Grad Curriculum Stops</span><span>·</span>
            <span><strong>7</strong> Acts</span><span>·</span>
            <span><strong>10</strong> Interactive Decoded Equations</span><span>·</span>
            <span><strong>8-Part</strong> Repeating Field Board</span><span>·</span>
            <span><strong>5</strong> Live Simulators</span><span>·</span>
            <span><strong>Live</strong> (+−−−) ↔ (−+++) Switch</span>
          </div>
          <div class="cta-row">
            <button type="button" class="btn-primary" onclick="switchView('journey', 'stop-01', true)">Start Step-by-Step Journey (Stop 01) →</button>
            <button type="button" class="btn-ghost" onclick="switchView('equations', 'eq-sm', true)">Decode the Equations →</button>
            <button type="button" class="btn-ghost" onclick="switchView('labs', 'units', true)">Open 5 Physics Labs →</button>
            <button type="button" id="resumeStopBtn" class="tool-pill" hidden onclick="switchView('journey', null, true)"></button>
          </div>
        </div>
        <div>
          <div class="plate-svg-wrap">{plates_by_id["p01"]["svg"]}</div>
        </div>
      </div>

      <!-- 5-FLOOR ARCHITECTURAL BUILDING (Read from Ground Floor 1 up to Floor 5!) -->
      <div class="sec-card">
        <span class="eyebrow">Principle 1 · One Architectural Spine Read from the Ground Up</span>
        <h2 style="font-size:26px;margin-block-end:4px;">Five floors of Quantum Field Theory: each floor solves what broke below</h2>
        <p style="color:var(--ink-2);max-width:76ch;">
          Click any floor from Ground Floor 1 (Relativistic Causality) up to Floor 5 (The Standard Model). Notice how flipping the <strong>(+−−−) / (−+++) Metric Switch</strong> in the top bar updates every equation automatically.
        </p>
        <div class="floors-building" role="group" aria-label="Five architectural floors of QFT">
          {floors_btns_html}
        </div>
        <div id="floorDetail" class="floor-detail" aria-live="polite"></div>
      </div>

      <!-- COLD-OPEN INTUITION TRAPS -->
      <div class="sec-card">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:12px;flex-wrap:wrap;">
          <div>
            <span class="eyebrow" style="color:var(--c-crisis);">Prologue · Test Your Non-Relativistic QM Intuition First</span>
            <h2 style="font-size:25px;margin-block-end:4px;">Three 15-second paradoxes that force Quantum Field Theory to exist</h2>
            <p style="color:var(--ink-2);max-width:74ch;">Pick your honest first instinct on each card below before diving into the 24-stop graduate syllabus.</p>
          </div>
          <span id="mirrorScoreBadge" class="pill-tag" style="padding:6px 12px;">QFT Intuition Checked: 0 / 3</span>
        </div>
        <div class="mirror-grid">{traps_html}</div>
      </div>

      <!-- ONE PICTURE THAT REPEATS: THE 8-PART FIELD SPEC-SHEET -->
      <div class="sec-card">
        <span class="eyebrow">Principle 2 · One Picture That Repeats Across Every Theory</span>
        <h2 style="font-size:25px;margin-block-end:6px;">The 8-Part Field Board: learn the board once, watch it upgrade to the Standard Model</h2>
        <p style="color:var(--ink-2);max-width:76ch;margin-block-end:14px;">
          Every stop in the 24-lesson Journey tracks the exact same eight slots—from a free spin-0 scalar all the way to chiral SU(3) × SU(2) × U(1).
        </p>
        <div tabindex="0" role="region" aria-labelledby="spec-table-caption" class="table-wrapper">
          <table class="data-table" style="--label-2:'Free Scalar';--label-3:'φ⁴ Theory';--label-4:'Spinor QED';--label-5:'SU(3) QCD';--label-6:'Standard Model';">
            <caption id="spec-table-caption">Comparative 8-Part Architecture Across Five Milestone Quantum Field Theories</caption>
            <thead>
              <tr>
                <th>Field Board Slot</th>
                <th>1. Free Scalar</th>
                <th>2. Interacting φ⁴</th>
                <th>3. Spinor QED</th>
                <th>4. Yang–Mills QCD</th>
                <th>5. Standard Model</th>
              </tr>
            </thead>
            <tbody>{spec_rows_html}</tbody>
          </table>
        </div>
      </div>

      <!-- SIX CROSS-CUTTING CONCEPTUAL THREADS -->
      <div class="sec-card">
        <span class="eyebrow">Principle 3 · Follow a Question Through the Entire Syllabus</span>
        <h2 style="font-size:25px;margin-block-end:6px;">Six deep questions—answered without hand-waving</h2>
        <div class="threads-grid">{threads_btns_html}</div>
        <div id="threadOut" aria-live="polite"></div>
      </div>
    </section>

    <!-- ================================================================
         VIEW 2: 24-STOP GRADUATE JOURNEY (STOP-BY-STOP + STAIRCASE)
         ================================================================ -->
    <section id="view-journey" hidden>
      <div style="display:flex;justify-content:space-between;align-items:flex-end;gap:12px;flex-wrap:wrap;margin-block-end:14px;">
        <div>
          <span class="eyebrow">Complete 2-Semester PhD / Graduate Core Sequence</span>
          <h2 style="font-size:30px;margin:0;">7 Acts · 24 Step-by-Step Stops (Use ← / → Arrow Keys)</h2>
        </div>
        <div style="display:flex;gap:8px;">
          <button type="button" id="jmode-card" class="tool-pill" aria-pressed="true" onclick="setJourneyMode('card')">Stop-by-Stop Lesson</button>
          <button type="button" id="jmode-stairs" class="tool-pill" aria-pressed="false" onclick="setJourneyMode('stairs')">7-Act Syllabus Map</button>
        </div>
      </div>

      <div id="journeyCardWrap">
        <div class="act-rail" role="group" aria-label="Jump to Act">{act_rail_html}</div>
        <div class="stop-scrubber" role="group" aria-label="24 curriculum stops">{stop_dots_html}</div>
        <div id="stopCardMount" aria-live="polite"></div>
      </div>

      <div id="journeyStairsWrap" hidden>
        {stairs_html}
      </div>
    </section>

    <!-- ================================================================
         VIEW 3: INTERACTIVE TERM-BY-TERM EQUATION DISSECTOR
         ================================================================ -->
    <section id="view-equations" hidden>
      <span class="eyebrow">Equation Anatomy Workspace · Click Every Symbol &amp; Flip Metric Signatures Live</span>
      <h2 style="font-size:30px;margin-block-end:6px;">10 Master Equations of QFT &amp; The Standard Model—Decoded Piece by Piece</h2>
      <p style="color:var(--ink-2);max-width:78ch;margin-block-end:16px;">
        Select any master equation below, then click each colored term to unpack its plain-English physical job, natural-units mass dimension <code>[E]^d</code>, suppressed Lorentz/spinor/color/weak indices, and how signs change between <strong>Tong/Schwartz/Peskin (+−−−)</strong> and <strong>Srednicki/Weinberg (−+++)</strong>.
      </p>
      <div style="display:flex;flex-wrap:wrap;gap:8px;margin-block-end:18px;" role="group" aria-label="Select master equation">
        {eq_btns_html}
      </div>
      <div id="eqDissectorMount" aria-live="polite"></div>
    </section>

    <!-- ================================================================
         VIEW 4: DEPENDENCY TREE OF QFT INVENTIONS (28 NODES × 8 LANES)
         ================================================================ -->
    <section id="view-tree" hidden>
      <span class="eyebrow">Everything Rests on Something Older · 7 Acts × 8 Field Board Lanes</span>
      <h2 style="font-size:30px;margin-block-end:6px;">Interactive Dependency Cladogram of Quantum Field Theory</h2>
      <p style="color:var(--ink-2);max-width:78ch;margin-block-end:14px;">
        Click any invention node on the map to trace what earlier concepts made it possible (<strong>← Rests On</strong>) and what advanced machinery it unlocks (<strong>→ Powers</strong>). Double-click a node for its modal dossier.
      </p>
      <div class="sec-card" style="padding:16px;">
        <div id="treeSvgMount" class="plate-svg-wrap" style="overflow-x:auto;"></div>
      </div>
      <div id="treeInspectorMount" class="sec-card" aria-live="polite"></div>
    </section>

    <!-- ================================================================
         VIEW 5: 5 LIVE INTERACTIVE PHYSICS SIMULATORS
         ================================================================ -->
    <section id="view-labs" hidden>
      <span class="eyebrow">Hands-On Mathematical Intuition · Manipulate Parameters in Real Time</span>
      <h2 style="font-size:30px;margin-block-end:8px;">Five Live Graduate QFT &amp; Standard Model Laboratories</h2>
      <div class="labs-nav" role="group" aria-label="Select simulator">
        <button type="button" class="tool-pill lab-tab-btn" data-lab="units" aria-pressed="true" onclick="selectLab('units')">1 · EFT Power Counting [E]^d</button>
        <button type="button" class="tool-pill lab-tab-btn" data-lab="poles" aria-pressed="false" onclick="selectLab('poles')">2 · Complex p⁰ Poles &amp; Wick</button>
        <button type="button" class="tool-pill lab-tab-btn" data-lab="feynman" aria-pressed="false" onclick="selectLab('feynman')">3 · Feynman Amplitude Builder</button>
        <button type="button" class="tool-pill lab-tab-btn" data-lab="rg" aria-pressed="false" onclick="selectLab('rg')">4 · Running α_i(μ) &amp; Asymptotic Freedom</button>
        <button type="button" class="tool-pill lab-tab-btn" data-lab="higgs" aria-pressed="false" onclick="selectLab('higgs')">5 · Mexican-Hat Higgs &amp; N_c=3 Anomaly Audit</button>
      </div>
      <div class="sec-card" id="labMount" aria-live="polite"></div>
    </section>

    <!-- ================================================================
         VIEW 6: HOW WE KNOW, 10 MYTHS/TRAPS, 6 MERGED BOOKS & 12 PLATES
         ================================================================ -->
    <section id="view-how" hidden>
      <span class="eyebrow">Skeptics, Qualifying-Exam Guardrails &amp; Source Compendium</span>
      <h2 style="font-size:30px;margin-block-end:6px;">How We Know QFT Works to 12 Decimal Places—and Where Every Book Shines</h2>
      <p style="color:var(--ink-2);max-width:78ch;margin-block-end:20px;">
        Cross-check empirical tests against world averages, inoculate yourself against the 10 most dangerous QFT misconceptions and minus-sign traps, and jump directly to the free PDF textbooks behind each module.
      </p>

      <!-- EMPIRICAL LEDGER -->
      <div class="sec-card">
        <h3 style="font-size:22px;margin-block-end:10px;">1 · Eight Landmark Experimental Verifications of QFT &amp; The Standard Model</h3>
        <div tabindex="0" role="region" aria-labelledby="emp-caption" class="table-wrapper">
          <table class="data-table" style="--label-2:'QFT Sector';--label-3:'Theory';--label-4:'Experiment';--label-5:'Precision';--label-6:'Primary Source';">
            <caption id="emp-caption">Quantitative Agreement Between Perturbative/Non-Perturbative QFT and Experiment</caption>
            <thead>
              <tr>
                <th>Observable</th>
                <th>QFT Mechanism</th>
                <th>Theoretical Prediction</th>
                <th>Experimental Measurement</th>
                <th>Precision / Verdict</th>
                <th>Source</th>
              </tr>
            </thead>
            <tbody>{ledger_rows_html}</tbody>
          </table>
        </div>
      </div>

      <!-- 6 MERGED TEXTBOOKS -->
      <div class="sec-card">
        <h3 style="font-size:22px;margin-block-end:6px;">2 · The Six Merged Canonical Texts (Including Official Free PDFs)</h3>
        <p style="color:var(--ink-2);margin-block-end:14px;">Use this map whenever you want 50 pages of extra homework problems or full multi-page derivations on any stop.</p>
        <div class="cards-2">{books_html}</div>
      </div>

      <!-- 10 MYTHS & GRAD SIGN TRAPS -->
      <div class="sec-card">
        <h3 style="font-size:22px;margin-block-end:6px;color:var(--c-crisis);">3 · Ten Popular Myths &amp; Graduate Calculation Sign Traps</h3>
        <p style="color:var(--ink-2);margin-block-end:14px;">Every grad student loses hours to at least three of these traps—bookmark them before doing loop homework.</p>
        <div class="cards-2">{myths_html}</div>
      </div>

      <!-- 12 PRINTABLE VECTOR PLATES -->
      <div>
        <h3 style="font-size:24px;margin-block-end:12px;">4 · Complete Gallery of 12 Standalone Vector Plates (SVG)</h3>
        {plates_gallery_html}
      </div>
    </section>
  </main>

  <!-- Mobile Bottom Navigation Bar -->
  <nav class="mob-bar" aria-label="Mobile sections">
    <button type="button" class="mob-btn" data-nav-view="overview" aria-current="page" onclick="switchView('overview', null, true)">Overview</button>
    <button type="button" class="mob-btn" data-nav-view="journey" onclick="switchView('journey', null, true)">24 Stops</button>
    <button type="button" class="mob-btn" data-nav-view="equations" onclick="switchView('equations', null, true)">Equations</button>
    <button type="button" class="mob-btn" data-nav-view="tree" onclick="switchView('tree', null, true)">Tree</button>
    <button type="button" class="mob-btn" data-nav-view="labs" onclick="switchView('labs', null, true)">5 Labs</button>
    <button type="button" class="mob-btn" data-nav-view="how" onclick="switchView('how', null, true)">How/PDFs</button>
  </nav>

  <!-- Native Light-Dismiss Modal Dialog -->
  <dialog id="nodeDialog" closedby="any" aria-labelledby="nodeDialogTitle">
    <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:12px;margin-block-end:10px;">
      <h3 id="nodeDialogTitle" style="font-size:22px;margin:0;"></h3>
      <button type="button" class="tool-pill" onclick="document.getElementById('nodeDialog').close()">Close ✕</button>
    </div>
    <div id="nodeDialogBody"></div>
  </dialog>

  <script id="sc-data" type="application/json">{payload}</script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" crossorigin="anonymous"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" crossorigin="anonymous" onload="if(window.__onKatexReady)window.__onKatexReady()"></script>
  <script>{APP_JS}</script>
</body>
</html>
"""
