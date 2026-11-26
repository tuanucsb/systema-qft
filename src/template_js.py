# -*- coding: utf-8 -*-
"""Client-side JavaScript engine for Systema Camporum (Routing, Metric Switch, KaTeX Renderer, Equation Dissector, Dependency Tree & 5 Physics Labs)."""

APP_JS = r"""
(() => {
  const DATA = JSON.parse(document.getElementById('sc-data').textContent);
  const VIEW_ORDER = ['overview', 'journey', 'equations', 'tree', 'labs', 'how'];

  const state = {
    view: 'overview',
    floorIdx: 0,
    threadIdx: 0,
    stopIdx: 0,
    journeyMode: 'card',
    eqIdx: 0,
    chunkIdx: 0,
    treeNodeId: 'nd-lightcone',
    labId: 'units',
    metric: 'west', // 'west' (+---) or 'east' (-+++)
    expertOpen: false,
    trapsTested: {},
  };

  try {
    const savedMetric = localStorage.getItem('sc-metric');
    if (savedMetric === 'west' || savedMetric === 'east') state.metric = savedMetric;
    const savedStop = parseInt(localStorage.getItem('sc-stop') || '0', 10);
    if (!Number.isNaN(savedStop) && savedStop >= 0 && savedStop < DATA.stops.length) {
      state.stopIdx = savedStop;
    }
  } catch (e) {}

  function esc(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function texHTML(tex, display = false) {
    if (window.katex && typeof window.katex.renderToString === 'function') {
      try {
        return window.katex.renderToString(tex, { displayMode: display, throwOnError: false, strict: false });
      } catch (e) {}
    }
    return `<code style="font-family:var(--mono);font-size:0.95em;">${esc(tex)}</code>`;
  }

  function renderInlineMathIn(root) {
    if (!root || !window.renderMathInElement) return;
    try {
      window.renderMathInElement(root, {
        delimiters: [
          { left: '\\(', right: '\\)', display: false },
          { left: '\\[', right: '\\]', display: true }
        ],
        throwOnError: false
      });
    } catch (e) {}
  }

  function announce(msg) {
    const el = document.getElementById('srAnnouncer');
    if (el) el.textContent = msg;
  }

  /* Color scheme toggle following modern-web-guidance dark-mode-toggle */
  const sysDarkMQ = window.matchMedia('(prefers-color-scheme: dark)');
  function currentRenderedDark() {
    const meta = document.querySelector('meta[name="color-scheme"]');
    if (meta.content === 'dark') return true;
    if (meta.content === 'light') return false;
    return sysDarkMQ.matches;
  }
  function syncThemeButton() {
    const isDark = currentRenderedDark();
    const lbl = document.getElementById('themeBtnLabel');
    if (lbl) lbl.textContent = isDark ? 'Light' : 'Dark';
    const btn = document.getElementById('themeBtn');
    if (btn) btn.setAttribute('aria-label', isDark ? 'Switch to light color scheme' : 'Switch to dark color scheme');
  }
  window.toggleColorScheme = function () {
    const meta = document.querySelector('meta[name="color-scheme"]');
    const target = currentRenderedDark() ? 'light' : 'dark';
    const sys = sysDarkMQ.matches ? 'dark' : 'light';
    if (target === sys) {
      try { localStorage.removeItem('sc-color-scheme'); } catch (e) {}
      meta.content = 'light dark';
    } else {
      try { localStorage.setItem('sc-color-scheme', target); } catch (e) {}
      meta.content = target;
    }
    syncThemeButton();
  };
  sysDarkMQ.addEventListener('change', syncThemeButton);
  window.addEventListener('storage', (ev) => {
    if (ev.key === 'sc-color-scheme') {
      document.querySelector('meta[name="color-scheme"]').content = ev.newValue ?? 'light dark';
      syncThemeButton();
    }
  });

  /* Metric Signature Switch: West (+---) vs East (-+++) */
  function syncMetricUI() {
    const btn = document.getElementById('metricBtn');
    if (btn) {
      btn.innerHTML = state.metric === 'west'
        ? '<span style="font-family:var(--mono);color:var(--c-act5);">(+ − − −)</span> <span>Tong / Schwartz</span>'
        : '<span style="font-family:var(--mono);color:var(--c-act2);">(− + + +)</span> <span>Srednicki / Weinberg</span>';
      btn.setAttribute('aria-pressed', state.metric === 'east' ? 'true' : 'false');
    }
    renderFloorDetail();
    renderStopCard();
    renderEquationDissector();
  }
  window.toggleMetric = function () {
    state.metric = state.metric === 'west' ? 'east' : 'west';
    try { localStorage.setItem('sc-metric', state.metric); } catch (e) {}
    syncMetricUI();
    announce(state.metric === 'west'
      ? 'Switched to West Coast mostly-minus metric (+ - - -)'
      : 'Switched to East Coast mostly-plus metric (- + + +)');
  };

  /* Grad Proof / Expert Mode Switch */
  window.toggleExpertMode = function () {
    state.expertOpen = !state.expertOpen;
    const btn = document.getElementById('expertBtn');
    if (btn) {
      btn.setAttribute('aria-pressed', state.expertOpen ? 'true' : 'false');
      btn.querySelector('span').textContent = state.expertOpen ? 'Grad Proofs: Open' : 'Grad Proofs';
    }
    document.querySelectorAll('details.grad-drawer').forEach((d) => { d.open = state.expertOpen; });
  };

  /* Directional View Navigation */
  window.switchView = function (targetView, subTarget = null, pushHash = false) {
    if (!VIEW_ORDER.includes(targetView)) targetView = 'overview';
    const oldIdx = VIEW_ORDER.indexOf(state.view);
    const newIdx = VIEW_ORDER.indexOf(targetView);
    const direction = newIdx >= oldIdx ? 'forward' : 'backward';

    const applyUpdate = () => {
      state.view = targetView;
      VIEW_ORDER.forEach((v) => {
        const sec = document.getElementById('view-' + v);
        if (sec) sec.hidden = (v !== targetView);
      });
      document.querySelectorAll('[data-nav-view]').forEach((b) => {
        if (b.dataset.navView === targetView) b.setAttribute('aria-current', 'page');
        else b.removeAttribute('aria-current');
      });

      if (targetView === 'journey' && subTarget) {
        const sIdx = DATA.stops.findIndex((s) => s.id === subTarget);
        if (sIdx >= 0) state.stopIdx = sIdx;
        renderStopCard();
      } else if (targetView === 'equations' && subTarget) {
        const eIdx = DATA.equations.findIndex((e) => e.id === subTarget);
        if (eIdx >= 0) { state.eqIdx = eIdx; state.chunkIdx = 0; }
        renderEquationDissector();
      } else if (targetView === 'tree' && subTarget) {
        if (DATA.tree.some((n) => n.id === subTarget)) state.treeNodeId = subTarget;
        renderTreeGraph();
      } else if (targetView === 'labs' && subTarget) {
        state.labId = subTarget === 'anomaly' ? 'higgs' : subTarget;
        renderLabs();
      }

      if (pushHash) {
        const h = subTarget ? `#${targetView}/${subTarget}` : `#${targetView}`;
        history.pushState(null, '', h);
      }
      window.scrollTo({ top: 0, behavior: 'instant' });
    };

    if (!document.startViewTransition || oldIdx === newIdx) {
      applyUpdate();
    } else {
      document.startViewTransition({ update: applyUpdate, types: [direction] });
    }
  };

  /* 1. OVERVIEW: 5 Floors, 3 Cold-Open Traps & 6 Threads */
  window.selectFloor = function (idx) {
    state.floorIdx = idx;
    document.querySelectorAll('.floor-btn').forEach((b) => {
      b.setAttribute('aria-pressed', Number(b.dataset.floor) === idx ? 'true' : 'false');
    });
    renderFloorDetail();
  };

  function renderFloorDetail() {
    const box = document.getElementById('floorDetail');
    if (!box) return;
    const fl = DATA.floors[state.floorIdx];
    const eq = state.metric === 'west' ? fl.eq_west : fl.eq_east;
    const nextIdx = (state.floorIdx + 1) % DATA.floors.length;
    box.innerHTML = `
      <div style="display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap;margin-block-end:8px;">
        <span class="pill-tag" style="margin:0;color:${fl.color};">Floor ${fl.num} of 5 · ${esc(fl.badge)}</span>
        <span style="font-family:var(--mono);font-size:12px;color:var(--ink-3);">Metric: ${state.metric === 'west' ? '(+ − − −)' : '(− + + +)'}</span>
      </div>
      <h3 style="font-size:21px;margin-block-end:8px;">${esc(fl.name)}</h3>
      <p style="font-size:15px;margin-block-end:10px;"><strong style="color:var(--c-crisis);">What broke below:</strong> ${esc(fl.crisis)}</p>
      <p style="font-size:15px;margin-block-end:12px;"><strong style="color:${fl.color};">How this floor solves it:</strong> ${esc(fl.breakthrough)}</p>
      <div style="padding:12px 14px;border-radius:10px;background:var(--surface);border:1px solid var(--line);overflow-x:auto;margin-block-end:12px;">
        ${texHTML(eq, true)}
      </div>
      <p style="font-size:13.5px;color:var(--ink-2);margin-block-end:14px;"><strong>Best Textbook Synthesis:</strong> ${esc(fl.books)}</p>
      <div style="display:flex;gap:10px;flex-wrap:wrap;">
        <button type="button" class="btn-primary" onclick="switchView('journey', '${fl.first_stop}', true)">Open ${fl.first_stop.toUpperCase()} in Journey →</button>
        <button type="button" class="btn-ghost" onclick="selectFloor(${nextIdx})">${state.floorIdx < 4 ? 'Climb to Floor ' + (fl.num + 1) + ' ↑' : 'Back to Ground Floor 1 ↺'}</button>
      </div>
    `;
  }

  window.answerMirrorTrap = function (idx, choice) {
    const tr = DATA.traps[idx];
    state.trapsTested[idx] = choice;
    const rev = document.getElementById('trap-rev-' + idx);
    if (!rev) return;
    const wise = choice === 'wise';
    rev.hidden = false;
    rev.style.borderColor = wise ? 'var(--c-act2)' : 'var(--c-crisis)';
    rev.innerHTML = `
      <strong style="display:block;color:${wise ? 'var(--c-act2)' : 'var(--c-crisis)'};margin-block-end:4px;">
        ${esc(wise ? tr.passed : tr.caught)}
      </strong>
      <p style="margin-block-end:8px;color:var(--ink-2);">${esc(tr.explain)}</p>
      <button type="button" class="tool-pill" onclick="switchView('${tr.target_view}', '${tr.target_sub}', true)">${esc(tr.cta)}</button>
    `;
    const count = Object.keys(state.trapsTested).length;
    const badge = document.getElementById('mirrorScoreBadge');
    if (badge) badge.textContent = `QFT Intuition Checked: ${count} / 3`;
  };

  window.selectThread = function (idx) {
    state.threadIdx = idx;
    document.querySelectorAll('.thread-btn').forEach((b) => {
      b.setAttribute('aria-pressed', Number(b.dataset.thread) === idx ? 'true' : 'false');
    });
    const out = document.getElementById('threadOut');
    if (!out) return;
    const th = DATA.threads[idx];
    const chips = th.stops.map((sid) => {
      const st = DATA.stops.find((x) => x.id === sid);
      return `<button type="button" class="tool-pill" onclick="switchView('journey', '${sid}', true)">Stop ${String(st.num).padStart(2, '0')}: ${esc(st.title.split(':')[0])} →</button>`;
    }).join('');
    out.innerHTML = `
      <div class="floor-detail" style="margin-block-start:12px;">
        <span class="eyebrow">${esc(th.tag)}</span>
        <h3 style="font-size:20px;margin-block-end:8px;">${esc(th.q)}</h3>
        <p style="font-size:15px;color:var(--ink-2);margin-block-end:12px;">${esc(th.answer)}</p>
        <div style="display:flex;flex-wrap:wrap;gap:8px;">${chips}</div>
      </div>
    `;
  };

  /* 2. JOURNEY: 24 Graduate Stops + 7-Act Staircase */
  window.setJourneyMode = function (mode) {
    state.journeyMode = mode;
    document.getElementById('jmode-card').setAttribute('aria-pressed', mode === 'card' ? 'true' : 'false');
    document.getElementById('jmode-stairs').setAttribute('aria-pressed', mode === 'stairs' ? 'true' : 'false');
    document.getElementById('journeyCardWrap').hidden = (mode !== 'card');
    document.getElementById('journeyStairsWrap').hidden = (mode !== 'stairs');
  };

  window.goToStop = function (idx) {
    if (idx < 0) idx = 0;
    if (idx >= DATA.stops.length) idx = DATA.stops.length - 1;
    state.stopIdx = idx;
    try { localStorage.setItem('sc-stop', String(idx)); } catch (e) {}
    if (state.journeyMode !== 'card') window.setJourneyMode('card');
    renderStopCard();
    const resumeBtn = document.getElementById('resumeStopBtn');
    if (resumeBtn) {
      const st = DATA.stops[idx];
      resumeBtn.hidden = false;
      resumeBtn.textContent = `Resume Stop ${String(st.num).padStart(2, '0')} →`;
    }
  };

  window.jumpActFirstStop = function (actId) {
    const idx = DATA.stops.findIndex((s) => s.act === actId);
    if (idx >= 0) window.goToStop(idx);
  };

  function renderStopCard() {
    const container = document.getElementById('stopCardMount');
    if (!container) return;
    const st = DATA.stops[state.stopIdx];
    const act = DATA.acts.find((a) => a.id === st.act);
    const plate = DATA.plates.find((p) => p.id === st.plate_id);
    const eqTex = state.metric === 'west' ? st.eq_west : st.eq_east;

    document.querySelectorAll('.act-pill').forEach((b) => {
      b.setAttribute('aria-pressed', b.dataset.act === st.act ? 'true' : 'false');
    });
    document.querySelectorAll('.stop-dot').forEach((d) => {
      if (Number(d.dataset.sidx) === state.stopIdx) d.setAttribute('aria-current', 'step');
      else d.removeAttribute('aria-current');
    });

    const crisisBanner = st.crisis_flag
      ? `<div style="padding:10px 14px;border-radius:8px;background:color-mix(in srgb, var(--c-crisis) 12%, var(--surface));border:1.5px solid var(--c-crisis);margin-block-end:14px;font-size:14px;">
           <strong style="color:var(--c-crisis);">THEORETICAL CRISIS &amp; RESOLUTION:</strong> Naive single-particle or classical intuition breaks at this step—forcing a structural upgrade to quantum field theory.
         </div>`
      : '';

    const termRows = st.eq_terms.map(([sym, dim, desc]) => `
      <div class="eq-meta-box">
        <div style="display:flex;justify-content:space-between;align-items:center;gap:8px;margin-block-end:4px;">
          <span>${texHTML(sym, false)}</span>
          <span class="pill-tag" style="margin:0;">${esc(dim)}</span>
        </div>
        <div style="color:var(--ink-2);font-size:13.5px;">${esc(desc)}</div>
      </div>
    `).join('');

    const derivList = st.grad_derivation.map((line) => `<li style="margin-block-end:8px;">${esc(line)}</li>`).join('');

    const boardHTML = DATA.lanes.map((ln) => {
      const isUp = st.upgraded.includes(ln.key);
      return `
        <div class="board-slot${isUp ? ' is-upgraded' : ''}" style="--bc:${ln.color}">
          <div style="display:flex;justify-content:space-between;align-items:center;gap:6px;margin-block-end:4px;">
            <span style="font-family:var(--mono);font-size:11.5px;font-weight:700;color:${ln.color};">${esc(ln.name)}</span>
            ${isUp ? '<span class="pill-tag" style="margin:0;padding:1px 6px;font-size:10.5px;">UPGRADED</span>' : ''}
          </div>
          <div style="font-size:13px;color:var(--ink);">${esc(st.board[ln.key])}</div>
        </div>
      `;
    }).join('');

    container.innerHTML = `
      <article class="sec-card" style="border-block-start:4px solid ${act.color};">
        <div style="display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap;margin-block-end:8px;">
          <span class="eyebrow" style="color:${act.color};margin:0;">Act ${act.roman} · ${esc(act.name)} · Stop ${String(st.num).padStart(2, '0')} of 24</span>
          <div style="display:flex;gap:8px;align-items:center;">
            <button type="button" class="tool-pill" ${state.stopIdx === 0 ? 'disabled' : ''} onclick="goToStop(${state.stopIdx - 1})">← Prev</button>
            <span style="font-family:var(--mono);font-size:12.5px;font-weight:700;">${st.num} / 24</span>
            <button type="button" class="tool-pill" ${state.stopIdx === 23 ? 'disabled' : ''} onclick="goToStop(${state.stopIdx + 1})">Next →</button>
          </div>
        </div>

        <h2 style="font-size:clamp(1.5rem,2.6vw,2.05rem);margin-block-end:10px;">${st.num}. ${esc(st.title)}</h2>
        ${crisisBanner}

        <p style="font-size:16px;color:var(--ink);margin-block-end:12px;">${esc(st.plain_hook)}</p>

        <div style="padding:10px 14px;border-radius:8px;background:var(--surface-2);border:1px solid var(--line);font-size:13.5px;color:var(--ink-2);margin-block-end:18px;">
          <strong style="color:${act.color};">Merged Best-of-Books Source:</strong> ${esc(st.book_merge)}
        </div>

        <!-- Master Equation Box -->
        <div class="eq-stage">
          <div style="display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap;margin-block-end:8px;">
            <strong style="font-size:15px;">Master Equation · ${esc(st.eq_title)}</strong>
            <span style="font-family:var(--mono);font-size:12px;color:var(--ink-3);">Active Metric: ${state.metric === 'west' ? '(+ − − −) West' : '(− + + +) East'}</span>
          </div>
          <div style="padding:14px;border-radius:10px;background:var(--surface);border:1.5px solid var(--line);overflow-x:auto;margin-block-end:10px;">
            ${texHTML(eqTex, true)}
          </div>
          <p style="font-size:14.5px;margin-block-end:12px;"><strong>In plain words:</strong> ${esc(st.eq_plain_read)}</p>
          <div class="cards-3">${termRows}</div>
        </div>

        <!-- Grad-Level Derivation Drawer -->
        <details class="grad-drawer" ${state.expertOpen ? 'open' : ''}>
          <summary>
            <span>Step-by-Step Graduate Mathematical Derivation (4 Steps)</span>
            <span style="font-family:var(--mono);font-size:12px;">Click to toggle</span>
          </summary>
          <ol class="grad-math-scope" style="margin-block:12px 0;padding-inline-start:20px;font-size:14.5px;color:var(--ink);">
            ${derivList}
          </ol>
        </details>

        <!-- Vector Illustration Plate -->
        <figure style="margin:18px 0;">
          <div class="plate-svg-wrap">${plate.svg}</div>
          <figcaption style="font-size:13.5px;color:var(--ink-2);margin-block-start:6px;">
            <strong>${esc(plate.title)}:</strong> ${esc(plate.say)}
          </figcaption>
        </figure>

        <!-- Repeating 8-Part Field Board -->
        <div style="margin-block-start:18px;">
          <div style="display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap;">
            <h3 style="font-size:18px;margin-block-end:4px;">The 8-Part Field Spec-Board at Stop ${String(st.num).padStart(2, '0')}</h3>
            <button type="button" class="tool-pill" onclick="switchView('labs', '${st.lab_id}', true)">Open Matching Physics Lab →</button>
          </div>
          <div class="field-board">${boardHTML}</div>
        </div>

        <!-- Worked Graduate Checkpoint Exercise -->
        <div style="margin-block-start:18px;padding:16px;border-radius:12px;background:var(--surface-2);border:1.5px solid var(--line-2);">
          <span class="eyebrow" style="color:var(--c-act3);">Graduate Checkpoint Problem · Active Mastery</span>
          <p style="font-weight:700;font-size:15px;margin-block-end:10px;">${esc(st.exercise.prompt)}</p>
          <div style="display:flex;gap:8px;flex-wrap:wrap;">
            <button type="button" class="tool-pill" onclick="document.getElementById('ex-hint-${st.num}').hidden = !document.getElementById('ex-hint-${st.num}').hidden">Show Hint</button>
            <button type="button" class="tool-pill" onclick="const el=document.getElementById('ex-sol-${st.num}');el.hidden=!el.hidden;renderInlineMathIn(el);">Reveal Worked Solution</button>
          </div>
          <div id="ex-hint-${st.num}" hidden style="margin-block-start:10px;padding:10px 12px;border-radius:8px;background:var(--surface);border:1px solid var(--line);font-size:14px;">
            <strong>Hint:</strong> ${esc(st.exercise.hint)}
          </div>
          <div id="ex-sol-${st.num}" class="grad-math-scope" hidden style="margin-block-start:10px;padding:12px 14px;border-radius:8px;background:var(--surface);border:1.5px solid var(--c-act2);font-size:14.5px;">
            <strong style="color:var(--c-act2);">Worked Solution:</strong> ${esc(st.exercise.solution)}
          </div>
        </div>

        <div style="display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-block-start:20px;padding-block-start:16px;border-block-start:1px solid var(--line);">
          <button type="button" class="btn-ghost" ${state.stopIdx === 0 ? 'disabled' : ''} onclick="goToStop(${state.stopIdx - 1})">← Previous Stop</button>
          <button type="button" class="btn-primary" ${state.stopIdx === 23 ? 'disabled' : ''} onclick="goToStop(${state.stopIdx + 1})">Next Stop →</button>
        </div>
      </article>
    `;
    renderInlineMathIn(container);
  }

  /* 3. EQUATION DISSECTOR */
  window.selectEquation = function (idx) {
    state.eqIdx = idx;
    state.chunkIdx = 0;
    document.querySelectorAll('.eq-pick-btn').forEach((b) => {
      b.setAttribute('aria-pressed', Number(b.dataset.eqidx) === idx ? 'true' : 'false');
    });
    renderEquationDissector();
  };

  window.selectChunk = function (cidx) {
    state.chunkIdx = cidx;
    renderEquationDissector();
  };

  function renderEquationDissector() {
    const mount = document.getElementById('eqDissectorMount');
    if (!mount) return;
    const eq = DATA.equations[state.eqIdx];
    const lhs = state.metric === 'west' ? eq.lhs_west : eq.lhs_east;
    const ch = eq.chunks[state.chunkIdx] || eq.chunks[0];

    const chunksHTML = eq.chunks.map((ck, i) => {
      const cTex = state.metric === 'west' ? ck.west : ck.east;
      const pressed = i === state.chunkIdx ? 'true' : 'false';
      return `<button type="button" class="eq-chunk" style="--tc:${ck.color}" aria-pressed="${pressed}" onclick="selectChunk(${i})">${texHTML(cTex, false)}</button>`;
    }).join('');

    mount.innerHTML = `
      <div class="sec-card">
        <div style="display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap;margin-block-end:6px;">
          <span class="eyebrow" style="margin:0;">Master Equation #${eq.num} · ${esc(eq.books)}</span>
          <button type="button" class="tool-pill" onclick="switchView('journey', '${eq.stop_id}', true)">Open Full Lesson (${eq.stop_id.toUpperCase()}) →</button>
        </div>
        <h2 style="font-size:24px;margin-block-end:6px;">${esc(eq.title)}</h2>
        <p style="font-size:15.5px;color:var(--ink-2);margin-block-end:14px;"><strong>In one breath:</strong> ${esc(eq.one_breath)}</p>

        <div style="font-family:var(--mono);font-size:12px;color:var(--ink-3);margin-block-end:6px;">
          Click any colored term below to dissect its physical meaning, mass dimension, hidden indices, and metric sign behavior:
        </div>
        <div class="eq-bar" role="group" aria-label="Clickable equation terms">
          <span class="eq-lhs">${texHTML(lhs, false)}</span>
          ${chunksHTML}
        </div>

        <div class="eq-inspector" style="--tc:${ch.color}">
          <div style="display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap;margin-block-end:8px;">
            <span class="pill-tag" style="margin:0;color:${ch.color};">Term ${state.chunkIdx + 1} of ${eq.chunks.length} · ${esc(ch.name)}</span>
            <span class="pill-tag" style="margin:0;">Natural Units: ${esc(ch.dim)}</span>
          </div>
          <div style="padding:10px 14px;border-radius:8px;background:var(--surface-2);margin-block-end:12px;overflow-x:auto;">
            ${texHTML(state.metric === 'west' ? ch.west : ch.east, false)}
          </div>
          <p style="font-size:15.5px;margin-block-end:10px;"><strong>Physical Job in Plain Words:</strong> ${esc(ch.plain)}</p>
          <div class="eq-meta-grid">
            <div class="eq-meta-box">
              <strong style="display:block;margin-block-end:4px;color:var(--c-act4);">Hidden Indices &amp; Matrix Structure</strong>
              <span>${esc(ch.indices)}</span>
            </div>
            <div class="eq-meta-box">
              <strong style="display:block;margin-block-end:4px;color:var(--c-act2);">West (+−−−) vs. East (−+++) Metric Sign</strong>
              <span>${esc(ch.metric_note)}</span>
            </div>
          </div>
          <div style="margin-block-start:12px;padding:11px 14px;border-radius:8px;background:color-mix(in srgb, var(--c-crisis) 9%, var(--surface-2));border:1px solid color-mix(in srgb, var(--c-crisis) 38%, var(--line));font-size:14px;">
            <strong style="color:var(--c-crisis);">Grad Qualifying-Exam Pitfall:</strong> ${esc(ch.pitfall)}
          </div>
        </div>
      </div>
    `;
  }

  /* 4. DEPENDENCY TREE OF QFT INVENTIONS */
  const powersMap = {};
  DATA.tree.forEach((n) => { powersMap[n.id] = []; });
  DATA.tree.forEach((n) => {
    n.rests_on.forEach((pid) => {
      if (powersMap[pid]) powersMap[pid].push(n.id);
    });
  });

  window.selectTreeNode = function (nid, openModal = false) {
    state.treeNodeId = nid;
    renderTreeGraph();
    if (openModal) window.openNodeModal(nid);
  };

  window.openNodeModal = function (nid) {
    const nd = DATA.tree.find((x) => x.id === nid);
    if (!nd) return;
    const dlg = document.getElementById('nodeDialog');
    const act = DATA.acts[nd.act - 1];
    const lane = DATA.lanes[nd.lane];
    const parents = nd.rests_on.map((id) => DATA.tree.find((x) => x.id === id)).filter(Boolean);
    const children = (powersMap[nd.id] || []).map((id) => DATA.tree.find((x) => x.id === id)).filter(Boolean);

    document.getElementById('nodeDialogTitle').textContent = nd.title;
    document.getElementById('nodeDialogBody').innerHTML = `
      <div style="display:flex;gap:8px;flex-wrap:wrap;margin-block-end:10px;">
        <span class="pill-tag" style="margin:0;color:${act.color};">Act ${act.roman}</span>
        <span class="pill-tag" style="margin:0;color:${lane.color};">${esc(lane.name)}</span>
      </div>
      <p style="font-size:15px;color:var(--ink-2);">${esc(nd.plain)}</p>
      <div style="padding:12px;border-radius:8px;background:var(--surface-2);border:1px solid var(--line);margin-block:12px;overflow-x:auto;">
        ${texHTML(nd.eq, true)}
      </div>
      <div class="cards-2" style="margin-block-end:14px;">
        <div class="eq-meta-box">
          <strong>← Rests On (Prerequisites):</strong>
          <div style="display:flex;flex-wrap:wrap;gap:6px;margin-block-start:6px;">
            ${parents.length ? parents.map((p) => `<button type="button" class="tool-pill" onclick="selectTreeNode('${p.id}', true)">${esc(p.short)}</button>`).join('') : '<span style="color:var(--ink-3);">Foundational axiom</span>'}
          </div>
        </div>
        <div class="eq-meta-box">
          <strong>→ Powers (Unlocks Next):</strong>
          <div style="display:flex;flex-wrap:wrap;gap:6px;margin-block-start:6px;">
            ${children.length ? children.map((c) => `<button type="button" class="tool-pill" onclick="selectTreeNode('${c.id}', true)">${esc(c.short)}</button>`).join('') : '<span style="color:var(--ink-3);">Standard Model culmination</span>'}
          </div>
        </div>
      </div>
      <button type="button" class="btn-primary" onclick="document.getElementById('nodeDialog').close();switchView('journey', '${nd.stop}', true)">Study Full Lesson (${nd.stop.toUpperCase()}) →</button>
    `;
    if (!dlg.open) dlg.showModal();
  };

  function renderTreeGraph() {
    const svgEl = document.getElementById('treeSvgMount');
    const inspEl = document.getElementById('treeInspectorMount');
    if (!svgEl || !inspEl) return;

    const sel = DATA.tree.find((n) => n.id === state.treeNodeId) || DATA.tree[0];
    const relSet = new Set([sel.id, ...sel.rests_on, ...(powersMap[sel.id] || [])]);

    const colX = (act) => 155 + (act - 1) * 132;
    const rowY = (lane) => 66 + lane * 52;
    const pos = {};
    DATA.tree.forEach((n) => { pos[n.id] = { x: colX(n.act), y: rowY(n.lane) }; });

    let parts = `<rect width="980" height="480" rx="12" fill="var(--surface)"/>`;
    // Lane horizontal guides
    DATA.lanes.forEach((ln, idx) => {
      const y = rowY(idx);
      parts += `<line x1="138" y1="${y}" x2="958" y2="${y}" stroke="var(--line)" stroke-dasharray="3 4"/>`;
      parts += `<text x="14" y="${y + 4}" font-size="11" font-weight="700" fill="${ln.color}">${esc(ln.name)}</text>`;
    });
    // Act column headers
    DATA.acts.forEach((ac, idx) => {
      const x = colX(idx + 1);
      parts += `<text x="${x}" y="28" text-anchor="middle" class="mono" font-size="11.5" font-weight="800" fill="${ac.color}">Act ${ac.roman}</text>`;
    });
    // Edges
    DATA.tree.forEach((n) => {
      const p2 = pos[n.id];
      n.rests_on.forEach((pid) => {
        const p1 = pos[pid];
        const active = (n.id === sel.id || pid === sel.id);
        const col = active ? 'var(--accent)' : 'var(--line-2)';
        const w = active ? 2.6 : 1.2;
        const op = active ? 1 : 0.35;
        const mx = (p1.x + p2.x) / 2;
        parts += `<path d="M ${p1.x} ${p1.y} C ${mx} ${p1.y}, ${mx} ${p2.y}, ${p2.x} ${p2.y}" fill="none" stroke="${col}" stroke-width="${w}" opacity="${op}"/>`;
      });
    });
    // Nodes
    DATA.tree.forEach((n) => {
      const p = pos[n.id];
      const act = DATA.acts[n.act - 1];
      const isSel = n.id === sel.id;
      const inRel = relSet.has(n.id);
      const op = inRel ? 1 : 0.42;
      const r = isSel ? 9.5 : 6.8;
      parts += `
        <g style="cursor:pointer" opacity="${op}" onclick="selectTreeNode('${n.id}', false)" ondblclick="openNodeModal('${n.id}')">
          <circle cx="${p.x}" cy="${p.y}" r="${r}" fill="${isSel ? act.color : 'var(--surface-2)'}" stroke="${act.color}" stroke-width="${isSel ? 3 : 2.2}"/>
          <rect x="${p.x - 56}" y="${p.y + 11}" width="112" height="18" rx="4" fill="var(--surface)" opacity="0.88"/>
          <text x="${p.x}" y="${p.y + 23}" text-anchor="middle" font-size="10.5" font-weight="${isSel ? '800' : '600'}" fill="var(--ink)">${esc(n.short)}</text>
        </g>
      `;
    });

    svgEl.innerHTML = `<svg viewBox="0 0 980 480" role="img" aria-label="Interactive QFT dependency tree across 7 acts and 8 field lanes">${parts}</svg>`;

    const parents = sel.rests_on.map((id) => DATA.tree.find((x) => x.id === id)).filter(Boolean);
    const children = (powersMap[sel.id] || []).map((id) => DATA.tree.find((x) => x.id === id)).filter(Boolean);
    const act = DATA.acts[sel.act - 1];
    inspEl.innerHTML = `
      <div style="display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap;margin-block-end:6px;">
        <span class="pill-tag" style="margin:0;color:${act.color};">Act ${act.roman} · ${esc(DATA.lanes[sel.lane].name)}</span>
        <button type="button" class="tool-pill" onclick="switchView('journey', '${sel.stop}', true)">Go to ${sel.stop.toUpperCase()} →</button>
      </div>
      <h3 style="font-size:20px;margin-block-end:6px;">${esc(sel.title)}</h3>
      <p style="font-size:14.5px;color:var(--ink-2);margin-block-end:10px;">${esc(sel.plain)}</p>
      <div style="padding:10px 12px;border-radius:8px;background:var(--surface);border:1px solid var(--line);margin-block-end:12px;overflow-x:auto;">
        ${texHTML(sel.eq, true)}
      </div>
      <div class="cards-2">
        <div>
          <strong style="font-size:13px;display:block;margin-block-end:6px;">← Rests On (${parents.length}):</strong>
          <div style="display:flex;flex-wrap:wrap;gap:6px;">
            ${parents.length ? parents.map((p) => `<button type="button" class="tool-pill" onclick="selectTreeNode('${p.id}')">${esc(p.short)}</button>`).join('') : '<span style="font-size:13px;color:var(--ink-3);">Root spacetime principle</span>'}
          </div>
        </div>
        <div>
          <strong style="font-size:13px;display:block;margin-block-end:6px;">→ Powers Next (${children.length}):</strong>
          <div style="display:flex;flex-wrap:wrap;gap:6px;">
            ${children.length ? children.map((c) => `<button type="button" class="tool-pill" onclick="selectTreeNode('${c.id}')">${esc(c.short)}</button>`).join('') : '<span style="font-size:13px;color:var(--ink-3);">Culminating SM prediction</span>'}
          </div>
        </div>
      </div>
    `;
  }

  /* 5. INTERACTIVE QFT PHYSICS SIMULATORS (5 LIVE LABS) */
  const labState = {
    nScalar: 4, nFermion: 0, nFieldStrength: 0, nDeriv: 0,
    poleType: 'feynman', eps: 0.28, wickAngle: 0,
    feynProc: 0, feynPiece: 0,
    rgLogMu: 2.0, rgNf: 6,
    higgsMu2: -7800, anomalyNc: 3,
  };

  window.selectLab = function (id) {
    state.labId = id;
    renderLabs();
  };

  window.setEFTPreset = function (ns, nf, nfs, nd) {
    labState.nScalar = ns; labState.nFermion = nf; labState.nFieldStrength = nfs; labState.nDeriv = nd;
    renderLabs();
  };

  window.updateLabVal = function (key, val) {
    labState[key] = Number.isNaN(Number(val)) ? val : Number(val);
    renderLabs();
  };

  function renderLabs() {
    document.querySelectorAll('.lab-tab-btn').forEach((b) => {
      b.setAttribute('aria-pressed', b.dataset.lab === state.labId ? 'true' : 'false');
    });
    const mount = document.getElementById('labMount');
    if (!mount) return;

    if (state.labId === 'units') {
      const d = labState.nScalar * 1 + labState.nFermion * 1.5 + labState.nFieldStrength * 2 + labState.nDeriv * 1;
      const gDim = 4 - d;
      let clsName = 'Marginal / Strictly Renormalizable (d = 4)';
      let clsCol = 'var(--c-act2)';
      let clsNote = 'Dimensionless coupling [g] = E⁰! Runs logarithmically with energy μ; survives across all scales.';
      if (d < 4) {
        clsName = d === 0 ? 'Vacuum Energy Constant (d = 0)' : 'Super-Renormalizable / Relevant (d < 4)';
        clsCol = 'var(--c-act5)';
        clsNote = `Positive mass-dimension coupling [g] = E^{+${gDim}}: dominates in the IR (long distances) and becomes negligible in the UV!`;
      } else if (d > 4) {
        clsName = `Non-Renormalizable / Irrelevant EFT Operator (d = ${d})`;
        clsCol = 'var(--c-crisis)';
        clsNote = `Negative mass-dimension coupling [c/Λ^{${d - 4}}] = E^{${gDim}}: suppressed at low energy by (E / Λ)^{${d - 4}}, signaling new heavy physics around scale Λ!`;
      }
      const pieces = [];
      if (labState.nDeriv > 0) pieces.push(`D^{${labState.nDeriv}}`);
      if (labState.nScalar > 0) pieces.push(`\\phi^{${labState.nScalar}}`);
      if (labState.nFermion > 0) pieces.push(`(\\bar{\\psi}\\psi)^{${labState.nFermion / 2}}`);
      if (labState.nFieldStrength > 0) pieces.push(`F_{\\mu\\nu}^{${labState.nFieldStrength}}`);
      const opTex = pieces.length ? `\\mathcal{O} \\sim ` + pieces.join('\\,') : `\\mathcal{O} = \\mathbf{1}`;

      mount.innerHTML = `
        <div class="sim-grid">
          <div class="sim-controls">
            <h3 style="font-size:18px;margin:0;">Build Any Local 4D Operator</h3>
            <div style="display:flex;flex-wrap:wrap;gap:6px;">
              <button type="button" class="tool-pill" onclick="setEFTPreset(4,0,0,0)">φ⁴ (d=4)</button>
              <button type="button" class="tool-pill" onclick="setEFTPreset(1,2,0,0)">Yukawa Hψ̄ψ (d=4)</button>
              <button type="button" class="tool-pill" onclick="setEFTPreset(0,2,1,0)">Pauli g−2 (d=5)</button>
              <button type="button" class="tool-pill" onclick="setEFTPreset(2,2,0,0)">Weinberg m_ν (d=5)</button>
              <button type="button" class="tool-pill" onclick="setEFTPreset(0,4,0,0)">Fermi G_F (d=6)</button>
            </div>
            <label>Scalars φ or H ([φ] = E¹): <strong>${labState.nScalar}</strong>
              <input type="range" min="0" max="6" step="1" value="${labState.nScalar}" oninput="updateLabVal('nScalar', this.value)">
            </label>
            <label>Fermion Pairs ψ̄ψ (2 × E^{3/2} = E³): <strong>${labState.nFermion} fermions</strong>
              <input type="range" min="0" max="6" step="2" value="${labState.nFermion}" oninput="updateLabVal('nFermion', this.value)">
            </label>
            <label>Field Strengths F_{μν} ([F] = E²): <strong>${labState.nFieldStrength}</strong>
              <input type="range" min="0" max="4" step="1" value="${labState.nFieldStrength}" oninput="updateLabVal('nFieldStrength', this.value)">
            </label>
            <label>Covariant Derivatives D_μ ([D] = E¹): <strong>${labState.nDeriv}</strong>
              <input type="range" min="0" max="4" step="1" value="${labState.nDeriv}" oninput="updateLabVal('nDeriv', this.value)">
            </label>
          </div>
          <div class="sim-stage">
            <span class="pill-tag" style="color:${clsCol};">${esc(clsName)}</span>
            <div style="padding:14px;border-radius:10px;background:var(--surface);border:1.5px solid var(--line);margin-block-end:12px;">
              ${texHTML(opTex + ` \\qquad [\\mathcal{O}] = E^{${d}}, \\qquad [g] = E^{${gDim}}`, true)}
            </div>
            <p style="font-size:15px;color:var(--ink-2);">${esc(clsNote)}</p>
            <div class="cards-3" style="margin-block-start:12px;">
              <div class="eq-meta-box"><strong>Operator Dim d:</strong> <span style="font-family:var(--mono);font-size:18px;color:${clsCol};">${d}</span></div>
              <div class="eq-meta-box"><strong>Coupling Dim 4−d:</strong> <span style="font-family:var(--mono);font-size:18px;">${gDim >= 0 ? '+' + gDim : gDim}</span></div>
              <div class="eq-meta-box"><strong>Amplitude Scaling:</strong> <span style="font-family:var(--mono);">${d === 4 ? '(E/Λ)⁰ = const' : `(E / Λ)^{${d - 4}}`}</span></div>
            </div>
          </div>
        </div>
      `;
    } else if (state.labId === 'poles') {
      const epsPx = labState.eps * 95;
      let leftPoleY = 190 - epsPx;
      let rightPoleY = 190 + epsPx;
      let modeDesc = 'Feynman (+iε): −ω_p sits in Upper Half-Plane (antiparticles t < 0); +ω_p sits in Lower Half-Plane (particles t > 0). Allows 90° counterclockwise Wick rotation!';
      if (labState.poleType === 'retarded') {
        leftPoleY = 190 + epsPx; rightPoleY = 190 + epsPx;
        modeDesc = 'Retarded (p⁰ + iε)² − ω²: BOTH poles sit in the Lower Half-Plane! Closing in Upper Half-Plane for t < 0 gives ZERO—strictly causal classical Green’s function!';
      } else if (labState.poleType === 'advanced') {
        leftPoleY = 190 - epsPx; rightPoleY = 190 - epsPx;
        modeDesc = 'Advanced (p⁰ − iε)² − ω²: BOTH poles sit in the Upper Half-Plane! Non-zero only for t < 0.';
      }
      const rad = (labState.wickAngle * Math.PI) / 180;
      const wx = Math.cos(rad) * 230;
      const wy = Math.sin(rad) * 145;

      mount.innerHTML = `
        <div class="sim-grid">
          <div class="sim-controls">
            <h3 style="font-size:18px;margin:0;">Complex p⁰ Contour &amp; Wick Lab</h3>
            <div style="display:grid;gap:6px;">
              <button type="button" class="tool-pill" aria-pressed="${labState.poleType === 'feynman'}" onclick="updateLabVal('poleType', 'feynman')">Feynman Propagator (+iε)</button>
              <button type="button" class="tool-pill" aria-pressed="${labState.poleType === 'retarded'}" onclick="updateLabVal('poleType', 'retarded')">Retarded Causal G_R</button>
              <button type="button" class="tool-pill" aria-pressed="${labState.poleType === 'advanced'}" onclick="updateLabVal('poleType', 'advanced')">Advanced G_A</button>
            </div>
            <label>Pole Displacement ε (exaggerated): <strong>${labState.eps.toFixed(2)}</strong>
              <input type="range" min="0.06" max="0.65" step="0.02" value="${labState.eps}" oninput="updateLabVal('eps', this.value)">
            </label>
            <label>Wick Rotation Angle θ (0° → 90° Euclidean): <strong>${labState.wickAngle}°</strong>
              <input type="range" min="0" max="90" step="5" value="${labState.wickAngle}" oninput="updateLabVal('wickAngle', this.value)">
            </label>
          </div>
          <div class="sim-stage">
            <p style="font-size:14.5px;color:var(--ink-2);margin-block-end:10px;">${esc(modeDesc)}</p>
            <div class="plate-svg-wrap">
              <svg viewBox="0 0 680 380" role="img" aria-label="Interactive complex p0 plane poles">
                <rect width="680" height="380" rx="12" fill="var(--surface)"/>
                <line x1="60" y1="190" x2="620" y2="190" stroke="var(--line-2)" stroke-width="1.8"/>
                <line x1="340" y1="36" x2="340" y2="344" stroke="var(--line-2)" stroke-width="1.8"/>
                <text x="565" y="180" class="mono" font-size="12" fill="var(--ink-2)">Re(p⁰)</text>
                <text x="350" y="54" class="mono" font-size="12" fill="var(--ink-2)">Im(p⁰)</text>

                <!-- Rotated Integration Contour -->
                <line x1="${340 - wx}" y1="${190 + wy}" x2="${340 + wx}" y2="${190 - wy}" stroke="var(--c-act6)" stroke-width="3.4"/>
                <text x="${348 + wx * 0.7}" y="${182 - wy * 0.7}" class="mono" font-size="12" font-weight="700" fill="var(--c-act6)">Contour (${labState.wickAngle}°)</text>

                <!-- Poles -->
                <circle cx="200" cy="${leftPoleY}" r="8" fill="var(--c-crisis)"/>
                <text x="125" y="${leftPoleY - 12}" class="mono" font-size="12" font-weight="700" fill="var(--c-crisis)">−ω_p Pole</text>

                <circle cx="480" cy="${rightPoleY}" r="8" fill="var(--c-act2)"/>
                <text x="435" y="${rightPoleY + 22}" class="mono" font-size="12" font-weight="700" fill="var(--c-act2)">+ω_p Pole</text>
              </svg>
            </div>
          </div>
        </div>
      `;
    } else if (state.labId === 'feynman') {
      const procs = [
        {
          name: 'QED: e⁻e⁺ → μ⁻μ⁺ (s-channel)',
          amp: String.raw`i\mathcal{M} = \bar{v}(p_2)(-ie\gamma^\mu)u(p_1)\,\frac{-i\eta_{\mu\nu}}{s + i\epsilon}\,\bar{u}(k_1)(-ie\gamma^\nu)v(k_2)`,
          pieces: [
            ['Incoming e⁻(p₁) & e⁺(p₂)', String.raw`\bar{v}^{s'}(p_2)\;\cdots\;u^s(p_1)`, 'External spinors: follow arrow backward from positron head v̄(p₂) to electron tail u(p₁).'],
            ['Left QED Vertex', String.raw`-ie\gamma^\mu`, 'Universal vector coupling preserving chirality; enforces q = p₁ + p₂.'],
            ['Virtual Photon Propagator', String.raw`\frac{-i\eta_{\mu\nu}}{s + i\epsilon}`, 'Timelike off-shell photon of invariant mass squared q² = s = 4E_cm² > 0.'],
            ['Right Muon Current', String.raw`\bar{u}^r(k_1)(-ie\gamma^\nu)v^{r'}(k_2)`, 'Identical coupling strength −ie to muons (lepton universality!).'],
          ]
        },
        {
          name: 'QED Møller: e⁻e⁻ → e⁻e⁻ (t − u Fermi Minus!)',
          amp: String.raw`i\mathcal{M} = (-ie)^2\left[\frac{\bar{u}(k_1)\gamma^\mu u(p_1)\,\bar{u}(k_2)\gamma_\mu u(p_2)}{t} \;-\; \frac{\bar{u}(k_2)\gamma^\mu u(p_1)\,\bar{u}(k_1)\gamma_\mu u(p_2)}{u}\right]\!(-i)`,
          pieces: [
            ['Direct t-Channel Exchange', String.raw`\mathcal{M}_t \propto \frac{1}{t} = \frac{1}{(p_1-k_1)^2}`, 'Spacelike virtual photon (t < 0) exchanged without swapping final labels.'],
            ['Crossed u-Channel Exchange', String.raw`-\,\mathcal{M}_u \propto -\frac{1}{u} = -\frac{1}{(p_1-k_2)^2}`, 'MANDATORY MINUS SIGN from swapping identical anticommuting final electrons k₁ ↔ k₂!'],
            ['Pauli Interference Check', String.raw`\theta_{\text{cm}} = 90^\circ \implies t = u`, 'Same-helicity electrons destructively interfere thanks to the relative minus sign!'],
          ]
        },
        {
          name: 'Scalar φ⁴: 1-Loop Bubble (Symmetry Factor 1/2)',
          amp: String.raw`i\mathcal{M}_{1\text{-loop}}(s) = \frac{1}{2}\,(-i\lambda)^2 \int \frac{d^dk}{(2\pi)^d}\,\frac{i}{k^2-m^2+i\epsilon}\,\frac{i}{(k+p)^2-m^2+i\epsilon}`,
          pieces: [
            ['Symmetry Factor 1/S = 1/2', String.raw`\frac{1}{2}`, 'Swapping the two identical internal scalar propagators leaves the graph unchanged!'],
            ['Two Quartic Vertices', String.raw`(-i\lambda)^2 = -\lambda^2`, 'Each 4-leg scalar vertex contributes −iλ after canceling 1/4!.'],
            ['UV Log Integral', String.raw`\frac{i}{16\pi^2}\left(\frac{2}{\epsilon} + \int_0^1 dx\ln\frac{\tilde{\mu}^2}{m^2-x(1-x)s}\right)`, 'Cancelled by −iδ_λ counterterm, leaving finite ln(s/μ²) running!'],
          ]
        },
      ];
      const pr = procs[labState.feynProc] || procs[0];
      const pc = pr.pieces[labState.feynPiece] || pr.pieces[0];

      mount.innerHTML = `
        <div class="sim-grid">
          <div class="sim-controls">
            <h3 style="font-size:18px;margin:0;">Select Scattering Process</h3>
            ${procs.map((p, idx) => `<button type="button" class="tool-pill" aria-pressed="${labState.feynProc === idx}" onclick="labState_pickProc(${idx})">${esc(p.name)}</button>`).join('')}
            <hr style="border:0;border-block-start:1px solid var(--line);inline-size:100%;">
            <strong style="font-size:13.5px;">Inspect Diagram Building Block:</strong>
            ${pr.pieces.map((item, idx) => `<button type="button" class="tool-pill" aria-pressed="${labState.feynPiece === idx}" onclick="updateLabVal('feynPiece', ${idx})">${idx + 1}. ${esc(item[0])}</button>`).join('')}
          </div>
          <div class="sim-stage">
            <h3 style="font-size:20px;margin-block-end:8px;">${esc(pr.name)}</h3>
            <div style="padding:14px;border-radius:10px;background:var(--surface);border:1.5px solid var(--line);overflow-x:auto;margin-block-end:14px;">
              ${texHTML(pr.amp, true)}
            </div>
            <div class="eq-inspector" style="--tc:var(--c-act3);margin-block-start:0;">
              <span class="pill-tag" style="color:var(--c-act3);">Selected Factor · ${esc(pc[0])}</span>
              <div style="padding:10px;background:var(--surface-2);border-radius:8px;margin-block:8px;overflow-x:auto;">
                ${texHTML(pc[1], false)}
              </div>
              <p style="margin:0;color:var(--ink-2);">${esc(pc[2])}</p>
            </div>
          </div>
        </div>
      `;
    } else if (state.labId === 'rg') {
      const logMz = Math.log10(91.1876);
      // 1-loop GUT-normalized SM beta coefficients: d(alpha_i^-1)/d(ln mu) = - b_i / (2pi)
      // b_1 = +41/10 (grows in UV -> alpha_1^-1 shrinks), b_2 = -19/6, b_3 = -(11 - 2*nf/3)
      const b1 = (4 / 3) * (labState.rgNf / 2) + 0.1; // approx flavor scaling around SM 4.1 at nf=6
      const b1_exact = labState.rgNf === 6 ? 4.1 : (4.0 * (labState.rgNf / 6) + 0.1);
      const b2 = -(22 / 3 - (2 / 3) * labState.rgNf - 1 / 6); // -19/6 at nf=6
      const b3 = -(11 - (2 / 3) * labState.rgNf); // -7 at nf=6

      const invA = (invMz, b, logMu) => {
        const dln = (logMu - logMz) * Math.LN10;
        return Math.max(1, invMz - (b / (2 * Math.PI)) * dln);
      };

      const pts1 = [], pts2 = [], pts3 = [];
      for (let lm = 0; lm <= 17; lm += 0.5) {
        const x = 65 + (lm / 17) * 575;
        const y = (v) => 320 - Math.min(68, Math.max(0, v)) * 4.0;
        pts1.push(`${x.toFixed(1)},${y(invA(59.0, b1_exact, lm)).toFixed(1)}`);
        pts2.push(`${x.toFixed(1)},${y(invA(29.6, b2, lm)).toFixed(1)}`);
        pts3.push(`${x.toFixed(1)},${y(invA(8.47, b3, lm)).toFixed(1)}`);
      }
      const curX = 65 + (labState.rgLogMu / 17) * 575;
      const curA1 = invA(59.0, b1_exact, labState.rgLogMu);
      const curA2 = invA(29.6, b2, labState.rgLogMu);
      const curA3 = invA(8.47, b3, labState.rgLogMu);
      const asymFree = (11 - (2 / 3) * labState.rgNf) > 0;

      mount.innerHTML = `
        <div class="sim-grid">
          <div class="sim-controls">
            <h3 style="font-size:18px;margin:0;">1-Loop SM Running Couplings</h3>
            <label>Energy Scale log₁₀(μ / GeV): <strong>10^{${labState.rgLogMu.toFixed(1)}} GeV</strong>
              <input type="range" min="0" max="17" step="0.2" value="${labState.rgLogMu}" oninput="updateLabVal('rgLogMu', this.value)">
            </label>
            <label>Number of Quark Flavors n_f: <strong>${labState.rgNf}</strong> (SM = 6; flips at 17!)
              <input type="range" min="0" max="18" step="1" value="${labState.rgNf}" oninput="updateLabVal('rgNf', this.value)">
            </label>
            <div class="eq-meta-box">
              <strong style="color:${asymFree ? 'var(--c-act2)' : 'var(--c-crisis)'};">
                ${asymFree ? `QCD Asymptotically Free! (β₀ = ${(11 - 2 * labState.rgNf / 3).toFixed(2)} > 0)` : `ASYMPTOTIC FREEDOM LOST! (n_f = ${labState.rgNf} ≥ 17 screens gluons!)`}
              </strong>
            </div>
          </div>
          <div class="sim-stage">
            <div class="cards-3" style="margin-block-end:10px;">
              <div class="eq-meta-box"><strong style="color:var(--c-act1);">α₁⁻¹(μ) U(1)_Y:</strong> ${curA1.toFixed(2)}</div>
              <div class="eq-meta-box"><strong style="color:var(--c-act5);">α₂⁻¹(μ) SU(2)_L:</strong> ${curA2.toFixed(2)}</div>
              <div class="eq-meta-box"><strong style="color:var(--c-act7);">α₃⁻¹(μ) SU(3)_c:</strong> ${curA3.toFixed(2)} (α_s ≈ ${(1 / curA3).toFixed(3)})</div>
            </div>
            <div class="plate-svg-wrap">
              <svg viewBox="0 0 680 365" role="img" aria-label="1-loop RG running of inverse gauge couplings">
                <rect width="680" height="365" rx="12" fill="var(--surface)"/>
                <line x1="65" y1="320" x2="645" y2="320" stroke="var(--ink-2)" stroke-width="1.8"/>
                <line x1="65" y1="40" x2="65" y2="320" stroke="var(--ink-2)" stroke-width="1.8"/>
                <text x="355" y="352" text-anchor="middle" class="mono" font-size="12" fill="var(--ink-2)">log₁₀(μ / GeV)  [0 = 1 GeV · 2 = M_Z · 15 ≈ M_GUT]</text>
                <text x="20" y="60" class="mono" font-size="11.5" fill="var(--ink-2)">αᵢ⁻¹</text>

                <polyline fill="none" stroke="var(--c-act1)" stroke-width="3" points="${pts1.join(' ')}"/>
                <polyline fill="none" stroke="var(--c-act5)" stroke-width="3" points="${pts2.join(' ')}"/>
                <polyline fill="none" stroke="var(--c-act7)" stroke-width="3.2" points="${pts3.join(' ')}"/>

                <line x1="${curX}" y1="44" x2="${curX}" y2="320" stroke="var(--accent)" stroke-width="2" stroke-dasharray="5 4"/>
              </svg>
            </div>
          </div>
        </div>
      `;
    } else {
      // Lab 5: Higgs SSB & Anomaly Cancellation Auditor
      const lam = 0.129;
      const broken = labState.higgsMu2 < 0;
      const v = broken ? Math.sqrt(-labState.higgsMu2 / lam) : 0;
      const mh = broken ? Math.sqrt(2 * lam) * v : Math.sqrt(labState.higgsMu2);
      const mw = 0.326 * v;
      const mz = 0.370 * v;

      // Anomaly audit for Nc colors
      const Nc = labState.anomalyNc;
      const a_su3 = 2 * (1 / 6) - (2 / 3) - (-1 / 3);
      const a_su2 = Nc * (1 / 6) + (-1 / 2);
      const a_u1 = 2 * Nc * Math.pow(1 / 6, 3) - Nc * Math.pow(2 / 3, 3) - Nc * Math.pow(-1 / 3, 3) + 2 * Math.pow(-1 / 2, 3) - Math.pow(-1, 3);
      const allZero = Math.abs(a_su2) < 1e-9 && Math.abs(a_u1) < 1e-9;

      // Potential curve
      const potPts = [];
      for (let x = -1.6; x <= 1.6; x += 0.08) {
        const px = 210 + x * 95;
        const val = (labState.higgsMu2 / 8000) * (x * x) + 0.65 * Math.pow(x, 4);
        const py = 215 - val * 85;
        potPts.push(`${px.toFixed(1)},${Math.max(45, Math.min(310, py)).toFixed(1)}`);
      }

      mount.innerHTML = `
        <div class="sim-grid">
          <div class="sim-controls">
            <h3 style="font-size:18px;margin:0;">Higgs SSB &amp; Anomaly Auditor</h3>
            <label>Quadratic Parameter μ²_eff (GeV²): <strong>${labState.higgsMu2} GeV²</strong>
              <input type="range" min="-10000" max="6000" step="200" value="${labState.higgsMu2}" oninput="updateLabVal('higgsMu2', this.value)">
            </label>
            <hr style="border:0;border-block-start:1px solid var(--line);inline-size:100%;">
            <label>Number of Quark Colors N_c: <strong>${Nc}</strong> (Test Anomaly Cancellation!)
              <input type="range" min="1" max="5" step="1" value="${Nc}" oninput="updateLabVal('anomalyNc', this.value)">
            </label>
            <div class="eq-meta-box" style="border-color:${allZero ? 'var(--c-act2)' : 'var(--c-crisis)'}">
              <strong style="color:${allZero ? 'var(--c-act2)' : 'var(--c-crisis)'}">
                ${allZero ? 'ANOMALY-FREE! Every gauge triangle = 0 (N_c = 3)' : `FATAL GAUGE ANOMALY for N_c = ${Nc}! Unitarity breaks at 1-loop!`}
              </strong>
              <div style="font-family:var(--mono);font-size:12px;margin-block-start:6px;">
                [SU(2)_L]²U(1)_Y = ${a_su2.toFixed(3)}<br>
                [U(1)_Y]³ = ${a_u1.toFixed(3)}<br>
                [SU(3)_c]²U(1)_Y = ${a_su3.toFixed(3)}
              </div>
            </div>
          </div>
          <div class="sim-stage">
            <div class="cards-3" style="margin-block-end:10px;">
              <div class="eq-meta-box"><strong>Vacuum VEV v:</strong> <span class="mono">${v.toFixed(1)} GeV</span></div>
              <div class="eq-meta-box"><strong>W± / Z⁰ Mass:</strong> <span class="mono">${mw.toFixed(1)} / ${mz.toFixed(1)} GeV</span></div>
              <div class="eq-meta-box"><strong>Scalar Mass m_h:</strong> <span class="mono">${mh.toFixed(1)} GeV</span></div>
            </div>
            <div class="plate-svg-wrap">
              <svg viewBox="0 0 420 290" role="img" aria-label="Live Higgs potential V(H)">
                <rect width="420" height="290" rx="12" fill="var(--surface)"/>
                <line x1="210" y1="30" x2="210" y2="260" stroke="var(--line-2)"/>
                <line x1="40" y1="215" x2="380" y2="215" stroke="var(--line-2)"/>
                <polyline fill="none" stroke="${broken ? 'var(--c-act7)' : 'var(--c-act5)'}" stroke-width="3.5" points="${potPts.join(' ')}"/>
                <text x="210" y="278" text-anchor="middle" class="mono" font-size="11.5" fill="var(--ink-2)">${broken ? 'Spontaneously Broken Mexican-Hat Phase (v > 0)' : 'Symmetric Phase (v = 0: W±, Z⁰ & fermions MASSLESS!)'}</text>
              </svg>
            </div>
          </div>
        </div>
      `;
    }
  }

  window.labState_pickProc = function (idx) {
    labState.feynProc = idx;
    labState.feynPiece = 0;
    renderLabs();
  };

  /* Safari Light-Dismiss Fallback for <dialog closedby="any"> */
  const dlg = document.getElementById('nodeDialog');
  if (dlg && !('closedBy' in HTMLDialogElement.prototype)) {
    dlg.addEventListener('click', (event) => {
      if (event.target !== dlg) return;
      const rect = dlg.getBoundingClientRect();
      const inside = rect.top <= event.clientY && event.clientY <= rect.top + rect.height &&
                     rect.left <= event.clientX && event.clientX <= rect.left + rect.width;
      if (!inside) dlg.close();
    });
  }

  /* Keyboard navigation for Journey */
  window.addEventListener('keydown', (ev) => {
    if (ev.target && ['INPUT', 'TEXTAREA', 'SELECT'].includes(ev.target.tagName)) return;
    if (state.view === 'journey' && state.journeyMode === 'card') {
      if (ev.key === 'ArrowRight') window.goToStop(state.stopIdx + 1);
      if (ev.key === 'ArrowLeft') window.goToStop(state.stopIdx - 1);
    }
  });

  /* Hash Router Init */
  function applyHash() {
    const raw = (location.hash || '').replace(/^#/, '');
    if (!raw) {
      syncMetricUI();
      selectThread(0);
      renderTreeGraph();
      renderLabs();
      return;
    }
    const [v, sub] = raw.split('/');
    syncMetricUI();
    selectThread(0);
    renderTreeGraph();
    renderLabs();
    if (VIEW_ORDER.includes(v)) window.switchView(v, sub || null, false);
  }
  window.addEventListener('hashchange', applyHash);

  /* Boot */
  syncThemeButton();
  applyHash();
  if (state.stopIdx > 0) {
    const rb = document.getElementById('resumeStopBtn');
    if (rb) {
      rb.hidden = false;
      rb.textContent = `Resume Stop ${String(DATA.stops[state.stopIdx].num).padStart(2, '0')} →`;
    }
  }

  /* Re-render math cleanly once KaTeX CDN script finishes if async */
  window.__onKatexReady = function () {
    syncMetricUI();
    renderTreeGraph();
    renderLabs();
    renderInlineMathIn(document.body);
  };
})();
"""
