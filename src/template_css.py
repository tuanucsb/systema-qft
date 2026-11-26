# -*- coding: utf-8 -*-
"""Kinetic Editorial CSS for Systema Camporum (Light/Dark Studio, Equation Dissector, 5-Floor Stack, Responsive Tables & Simulators)."""

APP_CSS = r"""
:root {
  color-scheme: light dark;
  --target-size: 44px;

  --bg-light: #f6f4ee;
  --bg-dark: #090c15;
  --surface-light: #ffffff;
  --surface-dark: #121726;
  --surface-2-light: #eeeae0;
  --surface-2-dark: #192036;
  --surface-3-light: #e2dccf;
  --surface-3-dark: #232c48;

  --ink-light: #11141c;
  --ink-dark: #eff3fc;
  --ink-2-light: #363e4d;
  --ink-2-dark: #c4cde8;
  --ink-3-light: #555e70;
  --ink-3-dark: #94a0c4;

  --line-light: #d5cfc2;
  --line-dark: #283152;
  --line-2-light: #b3aa99;
  --line-2-dark: #3e4b7a;

  --accent-light: #0b7a72;
  --accent-dark: #2ee6c5;
  --accent-ink-light: #ffffff;
  --accent-ink-dark: #04241e;

  --c-crisis-l: #c81e3a;  --c-crisis-d: #ff6b84;
  --c-act1-l: #155e75;    --c-act1-d: #38bdf8;
  --c-act2-l: #0f766e;    --c-act2-d: #2dd4bf;
  --c-act3-l: #b45309;    --c-act3-d: #fbbf24;
  --c-act4-l: #4338ca;    --c-act4-d: #818cf8;
  --c-act5-l: #1d4ed8;    --c-act5-d: #60a5fa;
  --c-act6-l: #7e22ce;    --c-act6-d: #c084fc;
  --c-act7-l: #be185d;    --c-act7-d: #f472b6;

  /* Fallback tokens before light-dark() */
  --bg: var(--bg-light);
  --surface: var(--surface-light);
  --surface-2: var(--surface-2-light);
  --surface-3: var(--surface-3-light);
  --ink: var(--ink-light);
  --ink-2: var(--ink-2-light);
  --ink-3: var(--ink-3-light);
  --line: var(--line-light);
  --line-2: var(--line-2-light);
  --accent: var(--accent-light);
  --accent-ink: var(--accent-ink-light);
  --c-crisis: var(--c-crisis-l);
  --c-act1: var(--c-act1-l);
  --c-act2: var(--c-act2-l);
  --c-act3: var(--c-act3-l);
  --c-act4: var(--c-act4-l);
  --c-act5: var(--c-act5-l);
  --c-act6: var(--c-act6-l);
  --c-act7: var(--c-act7-l);
  --scrollbar-thumb: #6f6a5e;
  --scrollbar-track: #ece7dc;

  @media (prefers-color-scheme: dark) {
    --bg: var(--bg-dark);
    --surface: var(--surface-dark);
    --surface-2: var(--surface-2-dark);
    --surface-3: var(--surface-3-dark);
    --ink: var(--ink-dark);
    --ink-2: var(--ink-2-dark);
    --ink-3: var(--ink-3-dark);
    --line: var(--line-dark);
    --line-2: var(--line-2-dark);
    --accent: var(--accent-dark);
    --accent-ink: var(--accent-ink-dark);
    --c-crisis: var(--c-crisis-d);
    --c-act1: var(--c-act1-d);
    --c-act2: var(--c-act2-d);
    --c-act3: var(--c-act3-d);
    --c-act4: var(--c-act4-d);
    --c-act5: var(--c-act5-d);
    --c-act6: var(--c-act6-d);
    --c-act7: var(--c-act7-d);
    --scrollbar-thumb: #7580b0;
    --scrollbar-track: #101526;
  }

  &:has(> head > meta[name="color-scheme"][content="dark"]) {
    color-scheme: dark;
    --bg: var(--bg-dark);
    --surface: var(--surface-dark);
    --surface-2: var(--surface-2-dark);
    --surface-3: var(--surface-3-dark);
    --ink: var(--ink-dark);
    --ink-2: var(--ink-2-dark);
    --ink-3: var(--ink-3-dark);
    --line: var(--line-dark);
    --line-2: var(--line-2-dark);
    --accent: var(--accent-dark);
    --accent-ink: var(--accent-ink-dark);
    --c-crisis: var(--c-crisis-d);
    --c-act1: var(--c-act1-d);
    --c-act2: var(--c-act2-d);
    --c-act3: var(--c-act3-d);
    --c-act4: var(--c-act4-d);
    --c-act5: var(--c-act5-d);
    --c-act6: var(--c-act6-d);
    --c-act7: var(--c-act7-d);
    --scrollbar-thumb: #7580b0;
    --scrollbar-track: #101526;
  }

  &:has(> head > meta[name="color-scheme"][content="light"]) {
    color-scheme: light;
    --bg: var(--bg-light);
    --surface: var(--surface-light);
    --surface-2: var(--surface-2-light);
    --surface-3: var(--surface-3-light);
    --ink: var(--ink-light);
    --ink-2: var(--ink-2-light);
    --ink-3: var(--ink-3-light);
    --line: var(--line-light);
    --line-2: var(--line-2-light);
    --accent: var(--accent-light);
    --accent-ink: var(--accent-ink-light);
    --c-crisis: var(--c-crisis-l);
    --c-act1: var(--c-act1-l);
    --c-act2: var(--c-act2-l);
    --c-act3: var(--c-act3-l);
    --c-act4: var(--c-act4-l);
    --c-act5: var(--c-act5-l);
    --c-act6: var(--c-act6-l);
    --c-act7: var(--c-act7-l);
    --scrollbar-thumb: #6f6a5e;
    --scrollbar-track: #ece7dc;
  }

  @supports (color: light-dark(white, black)) {
    --bg: light-dark(var(--bg-light), var(--bg-dark));
    --surface: light-dark(var(--surface-light), var(--surface-dark));
    --surface-2: light-dark(var(--surface-2-light), var(--surface-2-dark));
    --surface-3: light-dark(var(--surface-3-light), var(--surface-3-dark));
    --ink: light-dark(var(--ink-light), var(--ink-dark));
    --ink-2: light-dark(var(--ink-2-light), var(--ink-2-dark));
    --ink-3: light-dark(var(--ink-3-light), var(--ink-3-dark));
    --line: light-dark(var(--line-light), var(--line-dark));
    --line-2: light-dark(var(--line-2-light), var(--line-2-dark));
    --accent: light-dark(var(--accent-light), var(--accent-dark));
    --accent-ink: light-dark(var(--accent-ink-light), var(--accent-ink-dark));
    --c-crisis: light-dark(var(--c-crisis-l), var(--c-crisis-d));
    --c-act1: light-dark(var(--c-act1-l), var(--c-act1-d));
    --c-act2: light-dark(var(--c-act2-l), var(--c-act2-d));
    --c-act3: light-dark(var(--c-act3-l), var(--c-act3-d));
    --c-act4: light-dark(var(--c-act4-l), var(--c-act4-d));
    --c-act5: light-dark(var(--c-act5-l), var(--c-act5-d));
    --c-act6: light-dark(var(--c-act6-l), var(--c-act6-d));
    --c-act7: light-dark(var(--c-act7-l), var(--c-act7-d));
    --scrollbar-thumb: light-dark(#6f6a5e, #7580b0);
    --scrollbar-track: light-dark(#ece7dc, #101526);
  }

  accent-color: var(--accent);
  scrollbar-color: var(--scrollbar-thumb) var(--scrollbar-track);

  --display: 'Fraunces', Georgia, serif;
  --body: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;

  --r-sm: 8px;
  --r-md: 12px;
  --r-lg: 16px;
}

@supports not (scrollbar-color: auto) {
  ::-webkit-scrollbar { width: 10px; height: 10px; }
  ::-webkit-scrollbar-thumb { background: var(--scrollbar-thumb); border-radius: 999px; }
  ::-webkit-scrollbar-track { background: var(--scrollbar-track); }
}

/* Directional View Transitions */
@keyframes slide-to-left { to { transform: translateX(-36px); opacity: 0; } }
@keyframes slide-from-right { from { transform: translateX(36px); opacity: 0; } }
@keyframes slide-to-right { to { transform: translateX(36px); opacity: 0; } }
@keyframes slide-from-left { from { transform: translateX(-36px); opacity: 0; } }

::view-transition-group(root) {
  animation: 0.28s cubic-bezier(0.22, 1, 0.36, 1) both;
}
html:active-view-transition-type(forward)::view-transition-old(root) { animation-name: slide-to-left; }
html:active-view-transition-type(forward)::view-transition-new(root) { animation-name: slide-from-right; }
html:active-view-transition-type(backward)::view-transition-old(root) { animation-name: slide-to-right; }
html:active-view-transition-type(backward)::view-transition-new(root) { animation-name: slide-from-left; }

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(root) { animation: none !important; }
  *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; scroll-behavior: auto !important; }
}

*, *::before, *::after { box-sizing: border-box; }
[hidden] { display: none !important; }

body {
  margin: 0;
  background-color: var(--bg);
  background-image: radial-gradient(var(--line) 0.85px, transparent 0.85px);
  background-size: 24px 24px;
  color: var(--ink);
  font-family: var(--body);
  font-size: 16px;
  line-height: 1.6;
  font-variant-numeric: tabular-nums;
  padding-block-end: 84px;
}

h1, h2, h3, h4 {
  font-family: var(--display);
  line-height: 1.18;
  margin-block: 0 0.45em;
  text-wrap: balance;
}
p { margin-block: 0 0.85em; text-wrap: pretty; }
a { color: var(--accent); text-underline-offset: 3px; }
a:visited { color: var(--c-act6); }

.visually-hidden {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0, 0, 0, 0); white-space: nowrap; border: 0;
}
.skip-link:focus {
  position: fixed; inset-block-start: 10px; inset-inline-start: 10px; z-index: 9999;
  width: auto; height: auto; clip: auto; padding: 10px 16px;
  background: var(--accent); color: var(--accent-ink); border-radius: var(--r-sm); font-weight: 700;
}

:focus-visible {
  outline: 2.5px solid var(--accent);
  outline-offset: 2px;
}

/* Header & Navigation */
.site-head {
  position: sticky;
  inset-block-start: 0;
  z-index: 100;
  background: color-mix(in srgb, var(--surface) 92%, transparent);
  backdrop-filter: blur(10px);
  border-block-end: 1.5px solid var(--line);
}
.head-wrap {
  max-width: 1380px;
  margin-inline: auto;
  padding: 8px 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
}
.brand {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  color: var(--ink) !important;
  font-family: var(--display);
  font-weight: 800;
  font-size: 19px;
}
.brand-mark {
  display: inline-grid;
  grid-template-columns: repeat(7, 4px);
  gap: 2px;
  height: 22px;
  align-items: stretch;
}
.brand-mark i { display: block; border-radius: 2px; }
.brand-sub {
  font-family: var(--mono);
  font-size: 12px;
  font-weight: 700;
  color: var(--ink-3);
  padding-inline-start: 8px;
  border-inline-start: 1px solid var(--line);
}

.site-nav {
  display: flex;
  align-items: center;
  gap: 4px;
  overflow-x: auto;
}
.nav-link {
  position: relative;
  min-block-size: 40px;
  padding: 6px 12px;
  border: 1px solid transparent;
  border-radius: var(--r-sm);
  background: transparent;
  color: var(--ink-2);
  font-family: var(--body);
  font-size: 13.5px;
  font-weight: 700;
  cursor: pointer;
  white-space: nowrap;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.nav-link:hover { background: var(--surface-2); color: var(--ink); }
.nav-link[aria-current="page"] {
  color: var(--ink);
  background: var(--surface-2);
  border-color: var(--line-2);
}
.nav-link[aria-current="page"]::after {
  content: "";
  position: absolute;
  inset: auto 8px 3px;
  border-block-end: 2.5px solid var(--accent);
}
.nav-count {
  font-family: var(--mono);
  font-size: 11.5px;
  padding: 1px 6px;
  border-radius: 999px;
  background: var(--surface-3);
  color: var(--ink-2);
}

.head-tools {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-wrap: wrap;
}

.tool-pill {
  min-block-size: 38px;
  padding: 6px 11px;
  border-radius: var(--r-sm);
  border: 1.5px solid var(--line-2);
  background: var(--surface);
  color: var(--ink);
  font-family: var(--body);
  font-size: 12.5px;
  font-weight: 700;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  text-decoration: none;
  transition: transform 0.12s ease, border-color 0.15s ease;
}
.tool-pill:hover { border-color: var(--accent); }
.tool-pill:active { transform: translateY(1px); }
.tool-pill[aria-pressed="true"] {
  background: color-mix(in srgb, var(--accent) 16%, var(--surface));
  border-color: var(--accent);
}

.btn-primary {
  min-block-size: var(--target-size);
  padding: 10px 18px;
  border-radius: var(--r-md);
  border: 2px solid var(--accent);
  background: var(--accent);
  color: var(--accent-ink) !important;
  font-family: var(--body);
  font-size: 14.5px;
  font-weight: 800;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
}
.btn-ghost {
  min-block-size: var(--target-size);
  padding: 10px 16px;
  border-radius: var(--r-md);
  border: 1.5px solid var(--line-2);
  background: var(--surface);
  color: var(--ink) !important;
  font-family: var(--body);
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
}
.btn-ghost:hover { border-color: var(--accent); }

.wrap {
  max-width: 1320px;
  margin-inline: auto;
  padding: 24px 18px 40px;
}

.eyebrow {
  display: block;
  font-family: var(--mono);
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.03em;
  color: var(--accent);
  margin-block-end: 6px;
}

.sec-card {
  background: var(--surface);
  border: 1.5px solid var(--line);
  border-radius: var(--r-lg);
  padding: 24px;
  margin-block-end: 24px;
  box-shadow: 0 10px 28px -12px rgba(0, 0, 0, 0.14);
}

.pill-tag {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-family: var(--mono);
  font-size: 12px;
  font-weight: 700;
  padding: 3px 9px;
  border-radius: 999px;
  background: var(--surface-2);
  border: 1px solid var(--line);
  margin-block-end: 8px;
}

.hero-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 28px;
  align-items: center;
  margin-block-end: 26px;
}
.hero-title {
  font-size: clamp(2.1rem, 4.2vw, 3.35rem);
  font-weight: 850;
  margin-block-end: 10px;
}
.hero-accent {
  color: var(--accent);
  font-style: italic;
}
.spectrum-bar {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 4px;
  block-size: 5px;
  max-inline-size: 420px;
  margin-block-end: 14px;
}
.spectrum-bar span { border-radius: 999px; display: block; }
.lede {
  font-size: 17px;
  color: var(--ink-2);
  max-width: 66ch;
}
.edition-ledger {
  display: flex;
  flex-wrap: wrap;
  gap: 8px 12px;
  font-size: 13.5px;
  color: var(--ink-2);
  padding: 10px 14px;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--r-md);
  margin-block-end: 16px;
}
.cta-row { display: flex; flex-wrap: wrap; gap: 10px; }

.plate-svg-wrap svg {
  display: block;
  inline-size: 100%;
  block-size: auto;
  border-radius: var(--r-md);
  border: 1px solid var(--line);
}

/* 5-Floor Building (Systema Intelligentiae signature: column-reverse ground-up!) */
.floors-building {
  display: flex;
  flex-direction: column-reverse;
  gap: 8px;
  margin-block: 16px;
}
.floor-btn {
  display: grid;
  grid-template-columns: 8px 1fr auto;
  gap: 14px;
  align-items: center;
  text-align: start;
  padding: 14px 16px;
  border-radius: var(--r-md);
  border: 1.5px solid var(--line);
  background: var(--surface-2);
  color: var(--ink);
  cursor: pointer;
  min-block-size: 62px;
  transition: border-color 0.15s ease, background 0.15s ease;
}
.floor-btn .floor-bar {
  align-self: stretch;
  border-radius: 4px;
  background: var(--fc);
}
.floor-btn[aria-pressed="true"] {
  background: color-mix(in srgb, var(--fc) 11%, var(--surface));
  border-color: var(--fc);
  box-shadow: inset 0 -2.5px 0 var(--fc);
}
.floor-detail {
  padding: 20px;
  border-radius: var(--r-md);
  background: var(--surface-2);
  border: 1.5px solid var(--line-2);
}

/* Cold-Open Mirror Traps */
.mirror-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
  margin-block-start: 16px;
}
.trap-quiz-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 18px;
  border-radius: var(--r-md);
  background: var(--surface-2);
  border: 1.5px solid var(--line);
  gap: 12px;
}
.quiz-choices { display: grid; gap: 8px; }
.quiz-opt {
  text-align: start;
  padding: 10px 12px;
  min-block-size: var(--target-size);
  border-radius: var(--r-sm);
  border: 1.5px solid var(--line-2);
  background: var(--surface);
  color: var(--ink);
  font-family: var(--body);
  font-size: 13.5px;
  font-weight: 600;
  cursor: pointer;
}
.quiz-opt:hover { border-color: var(--accent); }
.quiz-reveal {
  padding: 12px;
  border-radius: var(--r-sm);
  background: var(--surface);
  border: 1px solid var(--line-2);
  font-size: 13.5px;
}

/* Journey Act Rail & Stop Card */
.act-rail {
  display: grid;
  grid-template-columns: repeat(7, minmax(120px, 1fr));
  gap: 6px;
  overflow-x: auto;
  margin-block-end: 14px;
}
.act-pill {
  padding: 8px 10px;
  border-radius: var(--r-sm);
  border: 1.5px solid var(--line);
  background: var(--surface);
  color: var(--ink);
  text-align: start;
  cursor: pointer;
  min-block-size: var(--target-size);
}
.act-pill[aria-pressed="true"] {
  border-color: var(--ac);
  background: color-mix(in srgb, var(--ac) 12%, var(--surface));
  box-shadow: inset 0 -3px 0 var(--ac);
}

.stop-scrubber {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
  margin-block-end: 16px;
}
.stop-dot {
  min-inline-size: 38px;
  min-block-size: 38px;
  border-radius: var(--r-sm);
  border: 1.5px solid var(--line);
  background: var(--surface);
  color: var(--ink-2);
  font-family: var(--mono);
  font-size: 12px;
  font-weight: 700;
  cursor: pointer;
}
.stop-dot.is-crisis { border-color: color-mix(in srgb, var(--c-crisis) 55%, var(--line)); }
.stop-dot[aria-current="step"] {
  background: var(--sc);
  color: #fff;
  border-color: var(--sc);
}

/* 8-Part Field Spec-Board */
.field-board {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 10px;
  margin-block: 14px;
}
.board-slot {
  padding: 12px;
  border-radius: var(--r-sm);
  background: var(--surface-2);
  border: 1.5px solid var(--line);
}
.board-slot.is-upgraded {
  background: color-mix(in srgb, var(--bc) 11%, var(--surface));
  border-color: var(--bc);
}

/* Interactive Term-by-Term Equation Dissector */
.eq-stage {
  padding: 20px;
  border-radius: var(--r-md);
  background: var(--surface-2);
  border: 1.5px solid var(--line-2);
  margin-block: 14px;
}
.eq-bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  padding: 14px;
  border-radius: var(--r-md);
  background: var(--surface);
  border: 1.5px solid var(--line);
  overflow-x: auto;
}
.eq-lhs {
  font-size: 1.15rem;
  padding-inline: 4px;
}
.eq-chunk {
  position: relative;
  padding: 8px 12px;
  min-block-size: var(--target-size);
  border-radius: var(--r-sm);
  border: 1.5px solid color-mix(in srgb, var(--tc) 45%, var(--line));
  background: color-mix(in srgb, var(--tc) 8%, var(--surface));
  color: var(--ink);
  cursor: pointer;
  font-size: 1.08rem;
  transition: transform 0.12s ease, border-color 0.15s ease, background 0.15s ease;
}
.eq-chunk:hover {
  transform: translateY(-2px);
  border-color: var(--tc);
}
.eq-chunk[aria-pressed="true"] {
  background: color-mix(in srgb, var(--tc) 18%, var(--surface));
  border-color: var(--tc);
  box-shadow: inset 0 -3.5px 0 var(--tc);
}
.eq-inspector {
  margin-block-start: 14px;
  padding: 18px;
  border-radius: var(--r-md);
  background: var(--surface);
  border: 2px solid var(--tc, var(--accent));
}
.eq-meta-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
  margin-block-start: 12px;
}
.eq-meta-box {
  padding: 12px;
  border-radius: var(--r-sm);
  background: var(--surface-2);
  border: 1px solid var(--line);
  font-size: 14px;
}

/* Expert / Grad Derivation Blocks */
.grad-drawer {
  margin-block: 14px;
  border-radius: var(--r-md);
  border: 1.5px solid color-mix(in srgb, var(--c-act6) 40%, var(--line));
  background: color-mix(in srgb, var(--c-act6) 6%, var(--surface));
  padding: 14px 18px;
}
.grad-drawer summary {
  cursor: pointer;
  font-weight: 800;
  font-size: 15px;
  color: var(--c-act6);
  min-block-size: 32px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* Simulators / Labs */
.labs-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-block-end: 18px;
}
.sim-grid {
  display: grid;
  grid-template-columns: 340px 1fr;
  gap: 20px;
  align-items: start;
}
.sim-controls {
  padding: 18px;
  border-radius: var(--r-md);
  background: var(--surface-2);
  border: 1.5px solid var(--line);
  display: grid;
  gap: 14px;
}
.sim-controls label {
  display: grid;
  gap: 4px;
  font-size: 13.5px;
  font-weight: 700;
}
.sim-controls input[type="range"] { inline-size: 100%; min-block-size: 32px; }
.sim-stage {
  padding: 18px;
  border-radius: var(--r-md);
  background: var(--surface-2);
  border: 1.5px solid var(--line);
}

/* Responsive Data Tables (modern-web-guidance @container pattern!) */
.table-wrapper {
  overflow: auto;
  max-inline-size: 100%;
  container-type: inline-size;
  border: 1.5px solid var(--line);
  border-radius: var(--r-md);
  background: var(--surface);
}
.data-table {
  inline-size: 100%;
  border-collapse: separate;
  border-spacing: 0;
  font-size: 14px;
}
.data-table caption {
  text-align: start;
  padding: 12px 16px;
  font-weight: 800;
  font-size: 15px;
  background: var(--surface-2);
  border-block-end: 1px solid var(--line);
}
.data-table thead {
  position: sticky;
  inset-block-start: 0;
  z-index: 2;
}
.data-table th, .data-table td {
  padding: 11px 14px;
  text-align: start;
  border-block-end: 1px solid var(--line);
  vertical-align: top;
}
.data-table thead th {
  background: var(--surface-2);
  font-family: var(--mono);
  font-size: 12px;
  color: var(--ink-2);
}
.data-table tbody th {
  position: sticky;
  inset-inline-start: 0;
  z-index: 1;
  background: var(--surface);
  font-weight: 800;
}

@container (width < 680px) {
  .data-table, .data-table thead, .data-table tbody, .data-table tr, .data-table th, .data-table td {
    display: block;
  }
  .data-table caption { display: block; }
  .data-table thead { display: none; }
  .data-table tr {
    margin: 10px;
    border: 1px solid var(--line-2);
    border-radius: var(--r-sm);
    overflow: hidden;
  }
  .data-table tbody th {
    position: static;
    background: var(--surface-2);
  }
  .data-table td:nth-child(2)::before { content: var(--label-2) ": "; font-weight: 700; color: var(--ink-2); }
  .data-table td:nth-child(3)::before { content: var(--label-3) ": "; font-weight: 700; color: var(--ink-2); }
  .data-table td:nth-child(4)::before { content: var(--label-4) ": "; font-weight: 700; color: var(--ink-2); }
  .data-table td:nth-child(5)::before { content: var(--label-5) ": "; font-weight: 700; color: var(--ink-2); }
  .data-table td:nth-child(6)::before { content: var(--label-6) ": "; font-weight: 700; color: var(--ink-2); }
}

/* Native Light-Dismiss Dialog */
dialog {
  max-inline-size: min(720px, 94vw);
  inline-size: 100%;
  border: 2px solid var(--line-2);
  border-radius: var(--r-lg);
  background: var(--surface);
  color: var(--ink);
  padding: 24px;
  box-shadow: 0 24px 60px rgba(0, 0, 0, 0.45);
}
dialog::backdrop {
  background-color: rgba(5, 8, 18, 0.62);
  backdrop-filter: blur(3px);
}

/* Grids */
.cards-2 { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px; }
.cards-3 { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; }
.threads-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px; }
.thread-btn {
  text-align: start; padding: 12px 14px; border-radius: var(--r-md);
  border: 1.5px solid var(--line); background: var(--surface-2); color: var(--ink);
  font-family: var(--body); font-size: 14px; font-weight: 700; cursor: pointer;
}
.thread-btn[aria-pressed="true"] {
  border-color: var(--accent);
  background: color-mix(in srgb, var(--accent) 12%, var(--surface));
  box-shadow: inset 0 -3px 0 var(--accent);
}

/* Mobile Bottom Nav */
.mob-bar { display: none; }

@media (max-width: 1080px) {
  .site-nav { display: none; }
  .hero-grid, .sim-grid, .cards-3, .mirror-grid, .threads-grid { grid-template-columns: 1fr; }
  .field-board, .cards-2, .eq-meta-grid { grid-template-columns: 1fr; }
  .mob-bar {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    position: fixed;
    inset: auto 0 0 0;
    z-index: 120;
    background: var(--surface);
    border-block-start: 1.5px solid var(--line-2);
    padding: 4px 6px calc(4px + env(safe-area-inset-bottom));
  }
  .mob-btn {
    min-block-size: 46px;
    border: 0;
    background: transparent;
    color: var(--ink-2);
    font-family: var(--body);
    font-size: 11.5px;
    font-weight: 700;
    cursor: pointer;
    border-radius: var(--r-sm);
  }
  .mob-btn[aria-current="page"] {
    color: var(--accent);
    background: var(--surface-2);
    box-shadow: inset 0 -2.5px 0 var(--accent);
  }
}
"""
