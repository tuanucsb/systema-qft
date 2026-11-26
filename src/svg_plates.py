# -*- coding: utf-8 -*-
"""Generates 12 standalone & inline publication-grade SVG vector plates for Systema Camporum."""

STANDALONE_STYLE = """<style>
  :root {
    --bg: #f6f4ee; --surface: #ffffff; --surface-2: #eeeae0;
    --ink: #11141c; --ink-2: #3b4352; --ink-3: #596273;
    --line: #d4cec0; --line-2: #aca493; --accent: #0b7a72;
    --c-crisis: #c81e3a; --c-act1: #155e75; --c-act2: #0f766e;
    --c-act3: #b45309; --c-act4: #4338ca; --c-act5: #1d4ed8;
    --c-act6: #7e22ce; --c-act7: #be185d;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #090c15; --surface: #121726; --surface-2: #192036;
      --ink: #eff3fc; --ink-2: #c2cbe6; --ink-3: #94a0c4;
      --line: #283152; --line-2: #3d4978; --accent: #2ee6c5;
      --c-crisis: #ff6b84; --c-act1: #38bdf8; --c-act2: #2dd4bf;
      --c-act3: #fbbf24; --c-act4: #818cf8; --c-act5: #60a5fa;
      --c-act6: #c084fc; --c-act7: #f472b6;
    }
  }
  text { font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif; fill: var(--ink); }
  .mono { font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace; }
  .serif { font-family: 'Fraunces', Georgia, serif; }
</style>"""


def wrap_svg(viewbox: str, label: str, body: str, standalone: bool) -> str:
    w, h = viewbox.split()[2], viewbox.split()[3]
    st = STANDALONE_STYLE if standalone else ""
    bg = f'<rect width="{w}" height="{h}" rx="14" fill="var(--surface)"/>'
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}" role="img" aria-label="{label}">'
        f"{st}{bg}{body}</svg>"
    )


def build_plates(standalone: bool = False) -> list:
    plates = []

    # PLATE 01: Cover — The Poincaré–Gauge Prism
    p01_body = """
    <defs>
      <pattern id="p01grid" width="24" height="24" patternUnits="userSpaceOnUse">
        <circle cx="12" cy="12" r="1" fill="var(--line-2)" opacity="0.45"/>
      </pattern>
    </defs>
    <rect x="12" y="12" width="736" height="456" rx="10" fill="url(#p01grid)" stroke="var(--line)" stroke-width="1.5"/>
    <text x="36" y="44" class="mono" font-size="11.5" font-weight="700" fill="var(--accent)">TABULA I · SYSTEMA CAMPORUM · POINCARÉ × GAUGE PRISM</text>
    <text x="36" y="74" class="serif" font-size="23" font-weight="800">From Vacuum Fluctuations to the Standard Model Spectrum</text>

    <!-- Left tangled vacuum loops -->
    <g fill="none" stroke="var(--c-crisis)" stroke-width="2.2" opacity="0.9">
      <path d="M 42 220 C 95 160, 130 285, 195 235 C 220 215, 240 245, 274 245"/>
      <path d="M 42 270 C 102 325, 145 190, 205 255 C 232 280, 250 255, 274 252" stroke-dasharray="5 4"/>
      <circle cx="118" cy="244" r="24" stroke="var(--ink-3)" stroke-width="1.8"/>
      <path d="M 94 244 Q 118 225 142 244 Q 118 263 94 244" stroke="var(--c-act5)" stroke-dasharray="3 3"/>
    </g>
    <text x="42" y="160" font-size="12.5" font-weight="700" fill="var(--c-crisis)">Raw Relativistic Vacuum</text>
    <text x="42" y="178" font-size="11.5" fill="var(--ink-2)">Off-shell loops &amp; gauge redundancy</text>

    <!-- Central Symmetry Prism -->
    <polygon points="345,118 258,368 432,368" fill="var(--surface-2)" stroke="var(--ink)" stroke-width="2.6"/>
    <polygon points="345,142 278,354 412,354" fill="none" stroke="var(--line-2)" stroke-width="1.2" stroke-dasharray="4 3"/>
    <text x="345" y="258" text-anchor="middle" class="mono" font-size="12" font-weight="700">ISO(1,3)</text>
    <text x="345" y="278" text-anchor="middle" class="mono" font-size="11.5" font-weight="700" fill="var(--accent)">× SU(3)×SU(2)×U(1)</text>
    <text x="345" y="302" text-anchor="middle" font-size="11.5" fill="var(--ink-2)">Locality + Unitarity</text>
    <text x="345" y="320" text-anchor="middle" font-size="11.5" fill="var(--ink-2)">+ Renormalization</text>

    <!-- 7 Refracted Act Beams -->
    <g stroke-width="3.2" fill="none" stroke-linecap="round">
      <line x1="382" y1="196" x2="515" y2="122" stroke="var(--c-act1)"/>
      <line x1="388" y1="214" x2="515" y2="168" stroke="var(--c-act2)"/>
      <line x1="394" y1="232" x2="515" y2="214" stroke="var(--c-act3)"/>
      <line x1="400" y1="250" x2="515" y2="260" stroke="var(--c-act4)"/>
      <line x1="406" y1="268" x2="515" y2="306" stroke="var(--c-act5)"/>
      <line x1="412" y1="286" x2="515" y2="352" stroke="var(--c-act6)"/>
      <line x1="418" y1="304" x2="515" y2="398" stroke="var(--c-act7)"/>
    </g>

    <g font-size="12.5" font-weight="700">
      <text x="526" y="126" fill="var(--c-act1)">I · Spacetime, Noether &amp; Little Groups</text>
      <text x="526" y="172" fill="var(--c-act2)">II · Spin-0 Fock Modes &amp; Path Integral Z[J]</text>
      <text x="526" y="218" fill="var(--c-act3)">III · Wick, LSZ &amp; Cross Sections dσ/dΩ</text>
      <text x="526" y="264" fill="var(--c-act4)">IV · Spin-1/2 Chiral Spinors &amp; Traces</text>
      <text x="526" y="310" fill="var(--c-act5)">V · Spin-1 Gauge Redundancy &amp; QED</text>
      <text x="526" y="356" fill="var(--c-act6)">VI · DimReg Loops, EFT &amp; RG β(g)</text>
      <text x="526" y="402" fill="var(--c-act7)">VII · Yang–Mills, Higgs &amp; Standard Model</text>
    </g>
    <text x="36" y="446" class="mono" font-size="11.5" fill="var(--ink-3)">Synthesizing Tong · Schwartz · Srednicki · Peskin &amp; Schroeder · Weinberg · Weigand</text>
    """
    plates.append({
        "id": "p01", "slug": "01-cover-systema-camporum", "act": "Act I–VII",
        "title": "The Poincaré–Gauge Prism of Quantum Field Theory",
        "say": "Locality, Lorentz symmetry, and quantum unitarity refract raw vacuum fluctuations into the 7 structured acts of graduate QFT.",
        "svg": wrap_svg("0 0 760 480", "Poincaré Gauge Prism refracting into 7 Acts of QFT", p01_body, standalone),
    })

    # PLATE 02: Lightcone Causality & Antiparticle Cancellation
    p02_body = """
    <text x="32" y="38" class="mono" font-size="11.5" font-weight="700" fill="var(--c-act1)">PLATE 02 · STOP 01 · MICROCAUSALITY &amp; ANTIPARTICLES</text>
    <text x="32" y="64" class="serif" font-size="20" font-weight="800">Why 1-Particle Relativistic QM Leaks Outside the Lightcone—and How QFT Fixes It</text>

    <!-- Left Panel: 1-Particle Failure -->
    <rect x="32" y="84" width="332" height="296" rx="10" fill="var(--surface-2)" stroke="var(--line)"/>
    <text x="48" y="110" font-size="13.5" font-weight="800" fill="var(--c-crisis)">A. 1-Particle Wavepacket (Fails!)</text>
    <line x1="198" y1="330" x2="198" y2="128" stroke="var(--ink-3)" stroke-width="1.5"/>
    <line x1="64" y1="250" x2="332" y2="250" stroke="var(--ink-3)" stroke-width="1.5"/>
    <polygon points="198,250 96,144 300,144" fill="var(--c-act1)" opacity="0.12"/>
    <line x1="198" y1="250" x2="96" y2="144" stroke="var(--c-act1)" stroke-width="2"/>
    <line x1="198" y1="250" x2="300" y2="144" stroke="var(--c-act1)" stroke-width="2"/>
    <text x="205" y="138" class="mono" font-size="11.5">t</text>
    <text x="336" y="254" class="mono" font-size="11.5">x</text>
    <!-- Leaking wave outside lightcone -->
    <path d="M 198 250 Q 250 232 292 232" fill="none" stroke="var(--c-crisis)" stroke-width="2.6" stroke-dasharray="5 3"/>
    <circle cx="292" cy="232" r="5" fill="var(--c-crisis)"/>
    <text x="226" y="274" class="mono" font-size="11.5" font-weight="700" fill="var(--c-crisis)">D(x−y) ~ e^{−mr} ≠ 0!</text>
    <text x="48" y="356" font-size="12" fill="var(--ink-2)">Spacelike leak violates Einstein causality.</text>

    <!-- Right Panel: QFT Antiparticle Cancellation -->
    <rect x="396" y="84" width="332" height="296" rx="10" fill="var(--surface-2)" stroke="var(--line)"/>
    <text x="412" y="110" font-size="13.5" font-weight="800" fill="var(--c-act2)">B. Quantum Field [φ(x), φ(y)] = 0 (Exact!)</text>
    <line x1="562" y1="330" x2="562" y2="128" stroke="var(--ink-3)" stroke-width="1.5"/>
    <line x1="428" y1="250" x2="696" y2="250" stroke="var(--ink-3)" stroke-width="1.5"/>
    <polygon points="562,250 460,144 664,144" fill="var(--c-act2)" opacity="0.14"/>
    <line x1="562" y1="250" x2="460" y2="144" stroke="var(--c-act2)" stroke-width="2"/>
    <line x1="562" y1="250" x2="664" y2="144" stroke="var(--c-act2)" stroke-width="2"/>
    <path d="M 562 250 Q 612 222 658 232" fill="none" stroke="var(--c-act5)" stroke-width="2.4"/>
    <path d="M 658 232 Q 612 258 562 250" fill="none" stroke="var(--c-act7)" stroke-width="2.4" stroke-dasharray="5 3"/>
    <circle cx="562" cy="250" r="4.5" fill="var(--ink)"/>
    <circle cx="658" cy="232" r="4.5" fill="var(--ink)"/>
    <text x="582" y="214" font-size="11.5" font-weight="700" fill="var(--c-act5)">Particle y → x (+)</text>
    <text x="572" y="276" font-size="11.5" font-weight="700" fill="var(--c-act7)">Antiparticle x → y (−)</text>
    <text x="412" y="356" font-size="12" font-weight="700" fill="var(--c-act2)">Sum = D(x−y) − D(y−x) = 0 outside cone!</text>
    """
    plates.append({
        "id": "p02", "slug": "02-lightcone-causality-cancellation", "act": "Act I · Stop 01",
        "title": "Lightcone Microcausality & Antiparticle Cancellation",
        "say": "A Lorentz boost can swap the time order of spacelike points, so causality requires every particle to have an antiparticle of equal mass that cancels spacelike propagation.",
        "svg": wrap_svg("0 0 760 400", "Lightcone causality and antiparticle cancellation", p02_body, standalone),
    })

    # PLATE 03: Complex p^0 Contour & Wick Rotation
    p03_body = """
    <text x="32" y="38" class="mono" font-size="11.5" font-weight="700" fill="var(--c-act2)">PLATE 03 · STOPS 05 &amp; 14 · COMPLEX p⁰ PLANE &amp; WICK ROTATION</text>
    <text x="32" y="64" class="serif" font-size="20" font-weight="800">How +iε Routes Forward/Backward Time—and Unlocks 90° Euclidean Wick Rotation</text>

    <!-- Axes -->
    <line x1="90" y1="230" x2="670" y2="230" stroke="var(--ink-2)" stroke-width="2"/>
    <line x1="380" y1="92" x2="380" y2="372" stroke="var(--ink-2)" stroke-width="2"/>
    <text x="646" y="218" class="mono" font-size="12.5" font-weight="700">Re(p⁰)</text>
    <text x="392" y="106" class="mono" font-size="12.5" font-weight="700">Im(p⁰) = p_E⁰</text>

    <!-- Lower half-plane arc (t > 0) -->
    <path d="M 140 230 A 240 132 0 0 0 620 230" fill="none" stroke="var(--c-act2)" stroke-width="2.6" stroke-dasharray="6 4"/>
    <text x="380" y="352" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--c-act2)">Close LOWER for x⁰ &gt; y⁰ → encircles +ω_p − iε (Particle forward in t)</text>

    <!-- Upper half-plane arc (t < 0) -->
    <path d="M 140 230 A 240 124 0 0 1 620 230" fill="none" stroke="var(--c-act4)" stroke-width="2.4" stroke-dasharray="4 4"/>
    <text x="380" y="128" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--c-act4)">Close UPPER for x⁰ &lt; y⁰ → encircles −ω_p + iε (Antiparticle backward in t)</text>

    <!-- Two shifted poles -->
    <circle cx="235" cy="196" r="7" fill="var(--c-crisis)"/>
    <text x="150" y="182" class="mono" font-size="12" font-weight="700" fill="var(--c-crisis)">×  −ω_p + iε (Q II)</text>

    <circle cx="525" cy="264" r="7" fill="var(--c-crisis)"/>
    <text x="478" y="290" class="mono" font-size="12" font-weight="700" fill="var(--c-crisis)">×  +ω_p − iε (Q IV)</text>

    <!-- Wick rotation 90 deg arrow in Q1 & Q3 (pole-free!) -->
    <path d="M 455 224 A 75 75 0 0 0 386 155" fill="none" stroke="var(--c-act6)" stroke-width="3"/>
    <polygon points="386,155 397,160 392,169" fill="var(--c-act6)"/>
    <text x="458" y="176" font-size="12" font-weight="700" fill="var(--c-act6)">Wick Rotation (+90°)</text>
    <text x="458" y="193" font-size="11.5" fill="var(--ink-2)">Zero poles in Q I &amp; Q III!</text>
    """
    plates.append({
        "id": "p03", "slug": "03-feynman-contour-poles", "act": "Act II & VI · Stops 05, 14",
        "title": "Feynman Pole Prescription (+iε) & Wick Rotation Geometry",
        "say": "Because +iε places poles strictly in Quadrants II and IV, closing contours yields causal propagation AND allows pole-free 90° counterclockwise rotation to Euclidean space.",
        "svg": wrap_svg("0 0 760 400", "Complex p0 plane Feynman poles and Wick rotation", p03_body, standalone),
    })

    # PLATE 04: Feynman Calculus Rosetta Stone
    p04_body = """
    <text x="32" y="38" class="mono" font-size="11.5" font-weight="700" fill="var(--c-act3)">PLATE 04 · STOPS 07–09, 13 · THE FEYNMAN ROSETTA STONE</text>
    <text x="32" y="64" class="serif" font-size="20" font-weight="800">Every Graphical Piece of a Scattering Diagram Maps 1-to-1 onto Algebra</text>

    <!-- Incoming fermions -->
    <line x1="95" y1="135" x2="255" y2="225" stroke="var(--c-act4)" stroke-width="3"/>
    <polygon points="182,184 166,182 173,170" fill="var(--c-act4)"/>
    <line x1="95" y1="315" x2="255" y2="225" stroke="var(--c-act4)" stroke-width="3"/>
    <polygon points="168,274 184,272 177,260" fill="var(--c-act4)"/>

    <!-- Virtual wavy photon -->
    <path d="M 255 225 Q 275 205 295 225 T 335 225 T 375 225 T 415 225 T 455 225 T 495 225" fill="none" stroke="var(--c-act5)" stroke-width="3.2"/>

    <!-- Outgoing muons -->
    <line x1="495" y1="225" x2="655" y2="135" stroke="var(--c-act2)" stroke-width="3"/>
    <polygon points="582,176 566,178 573,190" fill="var(--c-act2)"/>
    <line x1="495" y1="225" x2="655" y2="315" stroke="var(--c-act2)" stroke-width="3"/>
    <polygon points="568,266 584,268 577,280" fill="var(--c-act2)"/>

    <!-- Vertices -->
    <circle cx="255" cy="225" r="7.5" fill="var(--c-crisis)"/>
    <circle cx="495" cy="225" r="7.5" fill="var(--c-crisis)"/>

    <!-- Callout boxes -->
    <rect x="40" y="92" width="165" height="36" rx="6" fill="var(--surface-2)" stroke="var(--c-act4)"/>
    <text x="50" y="114" class="mono" font-size="12" font-weight="700" fill="var(--c-act4)">e⁻(p₁): u^s(p₁)</text>

    <rect x="40" y="324" width="165" height="36" rx="6" fill="var(--surface-2)" stroke="var(--c-act4)"/>
    <text x="50" y="346" class="mono" font-size="12" font-weight="700" fill="var(--c-act4)">e⁺(p₂): v̄^{s'}(p₂)</text>

    <rect x="195" y="256" width="132" height="44" rx="6" fill="var(--surface-2)" stroke="var(--c-crisis)"/>
    <text x="206" y="275" class="mono" font-size="12" font-weight="700" fill="var(--c-crisis)">Vertex: −ieγ^μ</text>
    <text x="206" y="292" font-size="11" fill="var(--ink-2)">δ⁴(p₁+p₂−q)</text>

    <rect x="304" y="132" width="152" height="50" rx="6" fill="var(--surface-2)" stroke="var(--c-act5)"/>
    <text x="315" y="153" class="mono" font-size="12" font-weight="700" fill="var(--c-act5)">−iη_{μν} / (q² + iε)</text>
    <text x="315" y="171" font-size="11" fill="var(--ink-2)">Off-shell q² = s &gt; 0</text>

    <rect x="548" y="92" width="172" height="36" rx="6" fill="var(--surface-2)" stroke="var(--c-act2)"/>
    <text x="558" y="114" class="mono" font-size="12" font-weight="700" fill="var(--c-act2)">μ⁻(k₁): ū^r(k₁)</text>

    <rect x="548" y="324" width="172" height="36" rx="6" fill="var(--surface-2)" stroke="var(--c-act2)"/>
    <text x="558" y="346" class="mono" font-size="12" font-weight="700" fill="var(--c-act2)">μ⁺(k₂): v^{r'}(k₂)</text>

    <text x="380" y="382" text-anchor="middle" class="mono" font-size="12" font-weight="700" fill="var(--ink-2)">Read spinor lines BACKWARD against arrow: [v̄(p₂)(−ieγ^μ)u(p₁)] · [−iη_{μν}/s] · [ū(k₁)(−ieγ^ν)v(k₂)]</text>
    """
    plates.append({
        "id": "p04", "slug": "04-feynman-calculus-anatomy", "act": "Act III & V · Stops 07–13",
        "title": "Feynman Diagram-to-Amplitude Rosetta Stone (e⁺e⁻ → μ⁺μ⁻)",
        "say": "Follow each fermion arrow backward from head to tail, insert −ieγ^μ at vertices, and bridge currents with −iη_{μν}/q².",
        "svg": wrap_svg("0 0 760 400", "Feynman diagram algebraic anatomy for e+e- to mu+mu-", p04_body, standalone),
    })

    # PLATE 05: Chiral Spinors & Dirac Mass Ping-Pong
    p05_body = """
    <text x="32" y="38" class="mono" font-size="11.5" font-weight="700" fill="var(--c-act4)">PLATE 05 · STOPS 03 &amp; 10 · CHIRAL WEYL SPINORS &amp; MASS PING-PONG</text>
    <text x="32" y="64" class="serif" font-size="20" font-weight="800">A Massive Dirac Electron Is a Left + Right Weyl Pair Flipping at Rate m</text>

    <rect x="44" y="108" width="210" height="210" rx="14" fill="var(--surface-2)" stroke="var(--c-act4)" stroke-width="2.4"/>
    <text x="149" y="142" text-anchor="middle" class="mono" font-size="14" font-weight="800" fill="var(--c-act4)">ψ_L ∈ (1/2, 0)</text>
    <text x="149" y="166" text-anchor="middle" font-size="12.5" font-weight="700">Left-Handed Weyl (2 comp.)</text>
    <text x="149" y="194" text-anchor="middle" class="mono" font-size="12" fill="var(--ink-2)">i ψ_L† σ̄^μ ∂_μ ψ_L</text>
    <text x="149" y="224" text-anchor="middle" font-size="12" fill="var(--c-act7)" font-weight="700">Feels SU(2)_L Weak W±!</text>
    <text x="149" y="250" text-anchor="middle" font-size="11.5" fill="var(--ink-2)">γ⁵ ψ_L = −ψ_L (Lorentz inv.)</text>

    <rect x="506" y="108" width="210" height="210" rx="14" fill="var(--surface-2)" stroke="var(--c-act5)" stroke-width="2.4"/>
    <text x="611" y="142" text-anchor="middle" font-size="14" font-weight="800" fill="var(--c-act5)">ψ_R ∈ (0, 1/2)</text>
    <text x="611" y="166" text-anchor="middle" font-size="12.5" font-weight="700">Right-Handed Weyl (2 comp.)</text>
    <text x="611" y="194" text-anchor="middle" font-size="12" fill="var(--ink-2)">i ψ_R† σ^μ ∂_μ ψ_R</text>
    <text x="611" y="224" text-anchor="middle" font-size="12" fill="var(--ink-3)" font-weight="700">SU(2)_L Singlet (blind to W±!)</text>
    <text x="611" y="250" text-anchor="middle" font-size="11.5" fill="var(--ink-2)">γ⁵ ψ_R = +ψ_R (Lorentz inv.)</text>

    <!-- Mass coupling arrows -->
    <path d="M 262 184 C 330 140, 430 140, 498 184" fill="none" stroke="var(--c-act3)" stroke-width="3"/>
    <polygon points="498,184 484,185 489,173" fill="var(--c-act3)"/>
    <path d="M 498 242 C 430 286, 330 286, 262 242" fill="none" stroke="var(--c-act3)" stroke-width="3"/>
    <polygon points="262,242 276,241 271,253" fill="var(--c-act3)"/>

    <rect x="302" y="190" width="156" height="46" rx="8" fill="var(--surface)" stroke="var(--c-act3)" stroke-width="2"/>
    <text x="380" y="210" text-anchor="middle" class="mono" font-size="12.5" font-weight="700" fill="var(--c-act3)">m = y_f v / √2</text>
    <text x="380" y="227" text-anchor="middle" font-size="11.5" fill="var(--ink-2)">Higgs Yukawa Bridge</text>

    <text x="380" y="362" text-anchor="middle" font-size="12.5" fill="var(--ink-2)">Vector gauge bosons (γ, g, W, Z) NEVER cross the middle—only mass/Higgs flips L ↔ R!</text>
    """
    plates.append({
        "id": "p05", "slug": "05-chiral-spinors-mass-pingpong", "act": "Act IV · Stop 10",
        "title": "Chiral Weyl Spinors & Higgs Yukawa Chirality Flip",
        "say": "Gauge bosons preserve chirality (keeping ψ_L and ψ_R decoupled), whereas Dirac mass continuously flips left into right via the Higgs condensate.",
        "svg": wrap_svg("0 0 760 390", "Chiral Weyl spinors coupled by Dirac Yukawa mass", p05_body, standalone),
    })

    # PLATE 06: 1-Loop QED Trio
    p06_body = """
    <text x="32" y="38" class="mono" font-size="11.5" font-weight="700" fill="var(--c-act6)">PLATE 06 · STOPS 14–16 · THE THREE 1-LOOP QED RADIATIVE DIAGRAMS</text>
    <text x="32" y="64" class="serif" font-size="20" font-weight="800">Vacuum Polarization (Z₃), Electron Self-Energy (Z₂) &amp; Schwinger’s Vertex (Z₁ = Z₂)</text>

    <!-- Card 1: Vacuum Polarization -->
    <rect x="28" y="88" width="224" height="278" rx="10" fill="var(--surface-2)" stroke="var(--line)"/>
    <text x="140" y="114" text-anchor="middle" font-size="13.5" font-weight="800" fill="var(--c-act5)">1. Vacuum Polarization Π^{μν}</text>
    <path d="M 48 195 Q 60 182 72 195 T 96 195" fill="none" stroke="var(--c-act5)" stroke-width="2.8"/>
    <circle cx="140" cy="195" r="42" fill="none" stroke="var(--c-act4)" stroke-width="3"/>
    <polygon points="140,153 130,147 130,159" fill="var(--c-act4)"/>
    <polygon points="140,237 150,231 150,243" fill="var(--c-act4)"/>
    <path d="M 184 195 Q 196 182 208 195 T 232 195" fill="none" stroke="var(--c-act5)" stroke-width="2.8"/>
    <text x="140" y="274" text-anchor="middle" class="mono" font-size="11.5" font-weight="700">q_μ Π^{μν}(q) = 0</text>
    <text x="140" y="296" text-anchor="middle" font-size="12" fill="var(--ink-2)">Photon stays m_γ = 0!</text>
    <text x="140" y="318" text-anchor="middle" font-size="12" font-weight="700" fill="var(--c-act5)">Drives β(e) = +e³/(12π²)</text>
    <text x="140" y="340" text-anchor="middle" font-size="11.5" fill="var(--ink-3)">α(M_Z)⁻¹ ≈ 127.95</text>

    <!-- Card 2: Electron Self-Energy -->
    <rect x="268" y="88" width="224" height="278" rx="10" fill="var(--surface-2)" stroke="var(--line)"/>
    <text x="380" y="114" text-anchor="middle" font-size="13.5" font-weight="800" fill="var(--c-act4)">2. Electron Self-Energy Σ(p̸)</text>
    <line x1="288" y1="215" x2="472" y2="215" stroke="var(--c-act4)" stroke-width="3"/>
    <path d="M 326 215 A 54 54 0 0 1 434 215" fill="none" stroke="var(--c-act5)" stroke-width="2.8" stroke-dasharray="5 3"/>
    <circle cx="326" cy="215" r="5" fill="var(--c-crisis)"/>
    <circle cx="434" cy="215" r="5" fill="var(--c-crisis)"/>
    <text x="380" y="274" text-anchor="middle" class="mono" font-size="11.5" font-weight="700">δm ∝ m ln(Λ/m)</text>
    <text x="380" y="296" text-anchor="middle" font-size="12" fill="var(--ink-2)">Chiral symmetry protects m!</text>
    <text x="380" y="318" text-anchor="middle" font-size="12" font-weight="700" fill="var(--c-act4)">Sets residue Z₂ = 1 + δ₂</text>
    <text x="380" y="340" text-anchor="middle" font-size="11.5" fill="var(--ink-3)">Dresses external spinors</text>

    <!-- Card 3: Vertex Correction -->
    <rect x="508" y="88" width="224" height="278" rx="10" fill="var(--surface-2)" stroke="var(--line)"/>
    <text x="620" y="114" text-anchor="middle" font-size="13.5" font-weight="800" fill="var(--c-act6)">3. Schwinger Vertex Γ^μ</text>
    <path d="M 620 135 Q 628 145 620 155 T 620 175" fill="none" stroke="var(--c-act5)" stroke-width="2.8"/>
    <line x1="620" y1="175" x2="552" y2="242" stroke="var(--c-act4)" stroke-width="3"/>
    <line x1="620" y1="175" x2="688" y2="242" stroke="var(--c-act4)" stroke-width="3"/>
    <path d="M 572 222 Q 620 234 668 222" fill="none" stroke="var(--c-act5)" stroke-width="2.6" stroke-dasharray="4 3"/>
    <circle cx="620" cy="175" r="5.5" fill="var(--c-crisis)"/>
    <text x="620" y="274" text-anchor="middle" class="mono" font-size="11.5" font-weight="700">Z₁ = Z₂ (Ward Identity!)</text>
    <text x="620" y="296" text-anchor="middle" font-size="12" fill="var(--ink-2)">UV + IR poles cancel/renorm.</text>
    <text x="620" y="318" text-anchor="middle" font-size="12.5" font-weight="800" fill="var(--c-act6)">F₂(0) = α/(2π) ≈ 0.0011614</text>
    <text x="620" y="340" text-anchor="middle" font-size="11.5" fill="var(--ink-3)">Verified to 12 digits!</text>
    """
    plates.append({
        "id": "p06", "slug": "06-qed-one-loop-trio", "act": "Act VI · Stops 14–16",
        "title": "The Three 1-Loop QED Divergences & Schwinger’s Finite Anomaly",
        "say": "Because Ward’s identity enforces Z₁ = Z₂, electron wavefunction and vertex renormalization cancel identically, leaving running charge controlled solely by photon Z₃!",
        "svg": wrap_svg("0 0 760 390", "Three 1-loop QED radiative diagrams", p06_body, standalone),
    })

    # PLATE 07: Wilsonian EFT Shell Integration & RG Flow
    p07_body = """
    <text x="32" y="38" class="mono" font-size="11.5" font-weight="700" fill="var(--c-act6)">PLATE 07 · STOP 17 · WILSONIAN EFFECTIVE FIELD THEORY &amp; RG FLOW</text>
    <text x="32" y="64" class="serif" font-size="20" font-weight="800">Integrating Out UV Momentum Shells Funnels Every Microscopic Theory to d ≤ 4</text>

    <!-- Left: Euclidean Momentum Shell -->
    <circle cx="190" cy="228" r="118" fill="var(--c-crisis)" opacity="0.16" stroke="var(--c-crisis)" stroke-width="2.4" stroke-dasharray="6 4"/>
    <circle cx="190" cy="228" r="76" fill="var(--surface-2)" stroke="var(--c-act2)" stroke-width="2.6"/>
    <text x="190" y="222" text-anchor="middle" font-size="13" font-weight="800" fill="var(--c-act2)">Slow IR Modes φ_L</text>
    <text x="190" y="242" text-anchor="middle" class="mono" font-size="11.5" fill="var(--ink-2)">|k_E| &lt; Λ / b</text>
    <text x="190" y="132" text-anchor="middle" font-size="12" font-weight="700" fill="var(--c-crisis)">Integrate Out Shell φ_H</text>
    <text x="190" y="368" text-anchor="middle" font-size="12" fill="var(--ink-2)">∫ Dφ_H exp(−S[φ_L + φ_H]) = exp(−S_eff[φ_L])</text>

    <!-- Right: RG Theory Space -->
    <rect x="372" y="96" width="352" height="256" rx="10" fill="var(--surface-2)" stroke="var(--line)"/>
    <line x1="412" y1="316" x2="696" y2="316" stroke="var(--ink-2)" stroke-width="2"/>
    <line x1="412" y1="316" x2="412" y2="122" stroke="var(--ink-2)" stroke-width="2"/>
    <text x="556" y="340" text-anchor="middle" class="mono" font-size="11.5" font-weight="700">Marginal Renormalizable Axis g₄ (d = 4)</text>
    <text x="424" y="138" class="mono" font-size="11.5" font-weight="700" fill="var(--c-crisis)">Irrelevant c₆/Λ² (d &gt; 4)</text>

    <!-- Different UV theories flowing down onto d=4 manifold -->
    <path d="M 450 144 Q 470 280 575 312" fill="none" stroke="var(--c-act6)" stroke-width="2.6"/>
    <path d="M 535 138 Q 545 275 615 312" fill="none" stroke="var(--c-act5)" stroke-width="2.6"/>
    <path d="M 645 148 Q 625 278 655 312" fill="none" stroke="var(--c-act2)" stroke-width="2.6"/>
    <circle cx="450" cy="144" r="5" fill="var(--c-act6)"/>
    <circle cx="535" cy="138" r="5" fill="var(--c-act5)"/>
    <circle cx="645" cy="148" r="5" fill="var(--c-act2)"/>
    <line x1="412" y1="316" x2="696" y2="316" stroke="var(--accent)" stroke-width="4"/>
    <text x="564" y="218" font-size="12" font-weight="700" fill="var(--ink)">Shrinking as (E / Λ)^{d−4}</text>
    <text x="564" y="236" font-size="11.5" fill="var(--ink-2)">Universality: distinct UV completions</text>
    <text x="564" y="252" font-size="11.5" fill="var(--ink-2)">land on the SAME IR renormalizable line!</text>
    """
    plates.append({
        "id": "p07", "slug": "07-wilsonian-eft-rg-flow", "act": "Act VI · Stop 17",
        "title": "Wilsonian Momentum-Shell Integration & RG Universality",
        "say": "Renormalizability is not an arbitrary axiom—any UV theory looks renormalizable at energies E ≪ Λ because d > 4 operators decay as (E/Λ)^{d−4}.",
        "svg": wrap_svg("0 0 760 390", "Wilsonian momentum shell integration and RG flow", p07_body, standalone),
    })

    # PLATE 08: QED Screening vs QCD Anti-Screening
    p08_body = """
    <text x="32" y="38" class="mono" font-size="11.5" font-weight="700" fill="var(--c-act7)">PLATE 08 · STOPS 18 &amp; 20 · VACUUM SCREENING VS. ASYMPTOTIC FREEDOM</text>
    <text x="32" y="64" class="serif" font-size="20" font-weight="800">Why QED Grows Stronger at Short Distances (β &gt; 0) While QCD Grows Weaker (β &lt; 0)</text>

    <!-- Left: QED Screening -->
    <rect x="32" y="88" width="332" height="278" rx="10" fill="var(--surface-2)" stroke="var(--c-act5)" stroke-width="1.8"/>
    <text x="198" y="114" text-anchor="middle" font-size="14" font-weight="800" fill="var(--c-act5)">Abelian QED · Dielectric Screening</text>
    <circle cx="198" cy="212" r="24" fill="var(--c-crisis)"/>
    <text x="198" y="217" text-anchor="middle" class="mono" font-size="14" font-weight="800" fill="#fff">e⁻</text>
    <!-- Screening dipoles: + closer to e-, - further -->
    <g font-size="12" class="mono" font-weight="700">
      <circle cx="144" cy="212" r="11" fill="var(--c-act5)"/><text x="144" y="216" text-anchor="middle" fill="#fff">+</text>
      <circle cx="118" cy="212" r="11" fill="var(--ink-3)"/><text x="118" y="216" text-anchor="middle" fill="#fff">−</text>
      <circle cx="252" cy="212" r="11" fill="var(--c-act5)"/><text x="252" y="216" text-anchor="middle" fill="#fff">+</text>
      <circle cx="278" cy="212" r="11" fill="var(--ink-3)"/><text x="278" y="216" text-anchor="middle" fill="#fff">−</text>
      <circle cx="198" cy="158" r="11" fill="var(--c-act5)"/><text x="198" y="162" text-anchor="middle" fill="#fff">+</text>
      <circle cx="198" cy="266" r="11" fill="var(--c-act5)"/><text x="198" y="270" text-anchor="middle" fill="#fff">+</text>
    </g>
    <text x="198" y="314" text-anchor="middle" class="mono" font-size="12" font-weight="700" fill="var(--c-act5)">Photons carry Q = 0 · Only e⁺e⁻ screen</text>
    <text x="198" y="338" text-anchor="middle" font-size="12" fill="var(--ink-2)">Closer probe (high Q²) sees LARGER bare charge!</text>

    <!-- Right: QCD Anti-Screening -->
    <rect x="396" y="88" width="332" height="278" rx="10" fill="var(--surface-2)" stroke="var(--c-act7)" stroke-width="1.8"/>
    <text x="562" y="114" text-anchor="middle" font-size="14" font-weight="800" fill="var(--c-act7)">Non-Abelian SU(3) QCD · Anti-Screening</text>
    <circle cx="562" cy="212" r="24" fill="var(--c-act7)"/>
    <text x="562" y="217" text-anchor="middle" class="mono" font-size="14" font-weight="800" fill="#fff">q_R</text>
    <!-- Gluon cloud spreading red color outward -->
    <circle cx="562" cy="212" r="68" fill="none" stroke="var(--c-act7)" stroke-width="3" stroke-dasharray="7 5"/>
    <circle cx="494" cy="212" r="13" fill="var(--c-act7)"/><text x="494" y="216" text-anchor="middle" class="mono" font-size="11" font-weight="700" fill="#fff">g_{Rb̄}</text>
    <circle cx="630" cy="212" r="13" fill="var(--c-act7)"/><text x="630" y="216" text-anchor="middle" class="mono" font-size="11" font-weight="700" fill="#fff">g_{Rḡ}</text>
    <circle cx="562" cy="144" r="13" fill="var(--c-act7)"/><text x="562" y="148" text-anchor="middle" class="mono" font-size="11" font-weight="700" fill="#fff">g</text>
    <text x="562" y="314" text-anchor="middle" class="mono" font-size="12" font-weight="700" fill="var(--c-act7)">β₀ = +11 (gluons) − ⅔ n_f (quarks) = +7 &gt; 0</text>
    <text x="562" y="338" text-anchor="middle" font-size="12" fill="var(--ink-2)">Closer probe penetrates cloud → α_s(Q²) → 0!</text>
    """
    plates.append({
        "id": "p08", "slug": "08-qed-screening-vs-qcd-antiscreening", "act": "Act VII · Stops 18, 20",
        "title": "QED Vacuum Screening vs. QCD Gluon Anti-Screening",
        "say": "Self-interacting spin-1 gluons spread color charge into a diffuse halo, so probing deep inside at high LHC momentum sees a weak, asymptotically free quark.",
        "svg": wrap_svg("0 0 760 390", "QED screening versus QCD gluon anti-screening", p08_body, standalone),
    })

    # PLATE 09: Faddeev-Popov Gauge Orbits & Ghosts
    p09_body = """
    <text x="32" y="38" class="mono" font-size="11.5" font-weight="700" fill="var(--c-act5)">PLATE 09 · STOPS 12 &amp; 19 · GAUGE ORBITS &amp; FADDEEV–POPOV GHOSTS</text>
    <text x="32" y="64" class="serif" font-size="20" font-weight="800">Slicing Redundant Gauge Fibers Without Overcounting or Breaking Unitarity</text>

    <!-- Fiber bundle vertical orbits -->
    <g stroke="var(--ink-3)" stroke-width="2" fill="none">
      <path d="M 110 110 C 95 195, 125 265, 108 335"/>
      <path d="M 195 110 C 180 195, 215 265, 192 335"/>
      <path d="M 280 110 C 265 195, 300 265, 278 335"/>
      <path d="M 365 110 C 350 195, 385 265, 362 335"/>
    </g>
    <text x="235" y="102" text-anchor="middle" font-size="12" font-weight="700" fill="var(--ink-2)">Infinite Gauge-Equivalent Fibers A_μ^U</text>

    <!-- Gauge-fixing slice G(A) = 0 -->
    <path d="M 72 238 Q 235 190 405 232" fill="none" stroke="var(--c-act2)" stroke-width="4"/>
    <circle cx="111" cy="227" r="5.5" fill="var(--c-act2)"/>
    <circle cx="196" cy="214" r="5.5" fill="var(--c-act2)"/>
    <circle cx="281" cy="214" r="5.5" fill="var(--c-act2)"/>
    <circle cx="366" cy="225" r="5.5" fill="var(--c-act2)"/>
    <text x="235" y="362" text-anchor="middle" class="mono" font-size="12" font-weight="700" fill="var(--c-act2)">Slice G^a(A) = ∂^μ A_μ^a = 0 picks 1 representative / orbit</text>

    <!-- Right box: Ghost cancellation -->
    <rect x="442" y="106" width="286" height="248" rx="10" fill="var(--surface-2)" stroke="var(--c-crisis)" stroke-width="1.8"/>
    <text x="585" y="134" text-anchor="middle" font-size="13.5" font-weight="800" fill="var(--c-crisis)">Jacobian det(∂^μ D_μ^{ab}) = Ghost Loop</text>
    <circle cx="585" cy="204" r="38" fill="none" stroke="var(--c-crisis)" stroke-width="2.8" stroke-dasharray="4 4"/>
    <text x="585" y="208" text-anchor="middle" class="mono" font-size="12" font-weight="700" fill="var(--c-crisis)">c^a / c̄^a (−1)</text>
    <text x="585" y="268" text-anchor="middle" font-size="12" font-weight="700">4 Gluon Comps (A₀, A₁, A₂, A₃)</text>
    <text x="585" y="290" text-anchor="middle" font-size="12" fill="var(--c-crisis)" font-weight="700">− 2 Anticommuting Ghosts (c, c̄)</text>
    <text x="585" y="316" text-anchor="middle" font-size="13" font-weight="800" fill="var(--c-act2)">= 2 Physical Transverse Helicities!</text>
    """
    plates.append({
        "id": "p09", "slug": "09-faddeev-popov-gauge-orbits", "act": "Act V & VII · Stops 12, 19",
        "title": "Gauge-Orbit Slicing & Faddeev–Popov Ghost Unitarity",
        "say": "Because non-Abelian gauge fibers intersect the gauge-fixing surface at field-dependent angles, the path-integral Jacobian requires (−1) Grassmann ghost loops.",
        "svg": wrap_svg("0 0 760 390", "Faddeev Popov gauge orbits and ghost cancellation", p09_body, standalone),
    })

    # PLATE 10: Mexican-Hat Higgs Potential & Eaten Goldstones
    p10_body = """
    <text x="32" y="38" class="mono" font-size="11.5" font-weight="700" fill="var(--c-act7)">PLATE 10 · STOPS 21–22 · MEXICAN-HAT HIGGS CONDENSATE &amp; EATEN GOLDSTONES</text>
    <text x="32" y="64" class="serif" font-size="20" font-weight="800">Spontaneous Symmetry Breaking: V(H) = −μ²|H|² + λ|H|⁴ at v = 246.2 GeV</text>

    <!-- Left: W-shaped cross section & trough -->
    <line x1="215" y1="96" x2="215" y2="338" stroke="var(--ink-3)" stroke-width="1.6"/>
    <line x1="48" y1="286" x2="382" y2="286" stroke="var(--ink-3)" stroke-width="1.6"/>
    <!-- Symmetric dashed parabola -->
    <path d="M 88 122 Q 215 430 342 122" fill="none" stroke="var(--ink-3)" stroke-width="1.8" stroke-dasharray="5 4"/>
    <!-- Broken W curve -->
    <path d="M 62 112 C 92 340, 152 345, 215 198 C 278 345, 338 340, 368 112" fill="none" stroke="var(--c-act7)" stroke-width="3.4"/>
    <!-- Trough ellipse -->
    <ellipse cx="215" cy="292" rx="92" ry="22" fill="none" stroke="var(--c-act2)" stroke-width="2.4" stroke-dasharray="5 3"/>
    <circle cx="215" cy="198" r="6" fill="var(--c-crisis)"/>
    <circle cx="307" cy="292" r="7.5" fill="var(--c-act2)"/>
    <text x="215" y="184" text-anchor="middle" font-size="11.5" font-weight="700" fill="var(--c-crisis)">Unstable H = 0</text>
    <text x="324" y="328" font-size="12" font-weight="700" fill="var(--c-act2)">True VEV v = 246 GeV</text>
    <text x="128" y="348" font-size="11.5" fill="var(--c-act2)">Flat trough π^a → Goldstones</text>

    <!-- Right: Degree of Freedom Accounting -->
    <rect x="412" y="96" width="316" height="264" rx="10" fill="var(--surface-2)" stroke="var(--line)"/>
    <text x="570" y="124" text-anchor="middle" font-size="13.5" font-weight="800">Exact Degree-of-Freedom Conservation</text>
    <text x="430" y="154" class="mono" font-size="12" font-weight="700" fill="var(--c-act5)">BEFORE SSB (Symmetric UV):</text>
    <text x="430" y="176" font-size="12" fill="var(--ink-2)">• Complex Doublet H: 4 real scalars</text>
    <text x="430" y="196" font-size="12" fill="var(--ink-2)">• Massless W¹,W²,W³,B: 4 × 2 = 8 dof</text>
    <line x1="430" y1="212" x2="708" y2="212" stroke="var(--line-2)"/>
    <text x="430" y="236" class="mono" font-size="12" font-weight="700" fill="var(--c-act7)">AFTER SSB (SU(2)_L×U(1)_Y → U(1)_em):</text>
    <text x="430" y="258" font-size="12" fill="var(--ink-2)">• 3 Goldstones eaten → W_L⁺, W_L⁻, Z_L⁰!</text>
    <text x="430" y="278" font-size="12" fill="var(--ink-2)">• Massive W± (80.4) &amp; Z⁰ (91.2): 3×3 = 9 dof</text>
    <text x="430" y="298" font-size="12" fill="var(--ink-2)">• Massless Photon γ (Q = T³+Y): 2 dof</text>
    <text x="430" y="318" font-size="12" font-weight="700" fill="var(--c-act2)">• Physical Radial Higgs h (125.1 GeV): 1 dof</text>
    <text x="570" y="344" text-anchor="middle" class="mono" font-size="12" font-weight="700">Total: 4 + 8 = 12 = 9 + 2 + 1</text>
    """
    plates.append({
        "id": "p10", "slug": "10-mexican-hat-higgs-mechanism", "act": "Act VII · Stops 21–22",
        "title": "The Mexican-Hat Higgs Potential & Longitudinal Boson Eating",
        "say": "Three would-be massless Goldstone modes become the longitudinal s_z = 0 components of W⁺, W⁻, and Z⁰, while Q⟨H⟩ = 0 keeps the photon strictly massless.",
        "svg": wrap_svg("0 0 760 390", "Mexican hat Higgs potential and degree of freedom accounting", p10_body, standalone),
    })

    # PLATE 11: Chiral Triangle Anomaly Cancellation
    p11_body = """
    <text x="32" y="38" class="mono" font-size="11.5" font-weight="700" fill="var(--c-crisis)">PLATE 11 · STOP 23 · CHIRAL TRIANGLE ANOMALIES &amp; QUARK–LEPTON MIRACLE</text>
    <text x="32" y="64" class="serif" font-size="20" font-weight="800">Quarks Alone Fail. Leptons Alone Fail. Together (with N_c = 3) Every Anomaly Vanishes!</text>

    <!-- Left: Triangle Diagram -->
    <path d="M 52 215 Q 68 202 84 215 T 116 215" fill="none" stroke="var(--c-act5)" stroke-width="3"/>
    <polygon points="116,215 236,132 236,298" fill="var(--surface-2)" stroke="var(--c-act4)" stroke-width="3"/>
    <path d="M 236 132 Q 256 122 272 136 T 308 136" fill="none" stroke="var(--c-act7)" stroke-width="3"/>
    <path d="M 236 298 Q 256 288 272 302 T 308 302" fill="none" stroke="var(--c-act7)" stroke-width="3"/>
    <circle cx="116" cy="215" r="6" fill="var(--c-crisis)"/>
    <circle cx="236" cy="132" r="6" fill="var(--c-crisis)"/>
    <circle cx="236" cy="298" r="6" fill="var(--c-crisis)"/>
    <text x="195" y="218" text-anchor="middle" class="mono" font-size="12" font-weight="700" fill="var(--c-act4)">ψ_L, ψ_R</text>
    <text x="72" y="192" class="mono" font-size="12" font-weight="700">T^a γ^μ P_L</text>
    <text x="275" y="118" class="mono" font-size="12" font-weight="700">T^b γ^ν</text>
    <text x="275" y="330" class="mono" font-size="12" font-weight="700">T^c γ^ρ</text>

    <!-- Right: Cancellation Balance Ledger -->
    <rect x="356" y="96" width="372" height="264" rx="10" fill="var(--surface-2)" stroke="var(--line)"/>
    <text x="542" y="124" text-anchor="middle" font-size="13.5" font-weight="800">1-Generation Anomaly Audit (N_c = 3)</text>
    <g class="mono" font-size="12">
      <text x="376" y="158" font-weight="700" fill="var(--c-act7)">1. [SU(3)_c]² U(1)_Y:</text>
      <text x="376" y="178" fill="var(--ink-2)">   2(1/6) − (2/3) − (−1/3) = 0  ✓</text>

      <text x="376" y="210" font-weight="700" fill="var(--c-act5)">2. [SU(2)_L]² U(1)_Y (Locks N_c = 3!):</text>
      <text x="376" y="230" fill="var(--ink-2)">   Quarks +3(1/6) + Leptons (−1/2) = 0  ✓</text>

      <text x="376" y="262" font-weight="700" fill="var(--c-act6)">3. [U(1)_Y]³ Cubic Trace:</text>
      <text x="376" y="282" fill="var(--ink-2)">   Quarks (−3/4) + Leptons (+3/4) = 0  ✓</text>

      <text x="376" y="314" font-weight="700" fill="var(--c-act2)">4. [Gravity]² U(1)_Y:</text>
      <text x="376" y="334" fill="var(--ink-2)">   6(1/6)−3(2/3)−3(−1/3)+2(−1/2)−(−1) = 0 ✓</text>
    </g>
    """
    plates.append({
        "id": "p11", "slug": "11-chiral-anomaly-triangle", "act": "Act VII · Stop 23",
        "title": "Triangle Gauge Anomaly Cancellation Across Quarks & Leptons",
        "say": "Quantum consistency of the Standard Model mathematically ties fractional quark charges (+2/3, −1/3) and N_c = 3 colors to integer lepton charges (−1, 0).",
        "svg": wrap_svg("0 0 760 390", "Chiral triangle gauge anomaly cancellation across quarks and leptons", p11_body, standalone),
    })

    # PLATE 12: Taxonomic Periodic Plate of the Standard Model
    p12_body = """
    <text x="32" y="36" class="mono" font-size="11.5" font-weight="700" fill="var(--accent)">TABULA XII · STOP 24 · LINNAEAN ARCHITECTURE OF THE STANDARD MODEL</text>
    <text x="32" y="62" class="serif" font-size="20" font-weight="800">Classified by Lorentz Spin (j_L, j_R) &amp; Gauge Quantum Numbers SU(3)_c × SU(2)_L × U(1)_Y</text>

    <!-- Column 1: Matter Fermions Spin 1/2 -->
    <rect x="28" y="82" width="336" height="316" rx="10" fill="var(--surface-2)" stroke="var(--c-act4)" stroke-width="2"/>
    <text x="44" y="108" font-size="13.5" font-weight="800" fill="var(--c-act4)">SPIN 1/2 · Chiral Matter (× 3 Generations)</text>

    <rect x="44" y="122" width="144" height="74" rx="8" fill="var(--surface)" stroke="var(--line)"/>
    <text x="56" y="144" class="mono" font-size="13" font-weight="800" fill="var(--c-act7)">Q_L = (u_L, d_L)</text>
    <text x="56" y="164" class="mono" font-size="11.5" fill="var(--ink-2)">(3, 2, +1/6)</text>
    <text x="56" y="182" font-size="11" fill="var(--ink-3)">Feels g, W±, Z, γ</text>

    <rect x="204" y="122" width="144" height="74" rx="8" fill="var(--surface)" stroke="var(--line)"/>
    <text x="216" y="144" class="mono" font-size="13" font-weight="800" fill="var(--c-act7)">u_R , d_R</text>
    <text x="216" y="164" class="mono" font-size="11.5" fill="var(--ink-2)">(3,1,+2/3) · (3,1,−1/3)</text>
    <text x="216" y="182" font-size="11" fill="var(--ink-3)">SU(2)_L singlets!</text>

    <rect x="44" y="210" width="144" height="74" rx="8" fill="var(--surface)" stroke="var(--line)"/>
    <text x="56" y="232" class="mono" font-size="13" font-weight="800" fill="var(--c-act5)">L_L = (ν_L, e_L)</text>
    <text x="56" y="252" class="mono" font-size="11.5" fill="var(--ink-2)">(1, 2, −1/2)</text>
    <text x="56" y="270" font-size="11" fill="var(--ink-3)">Colorless; feels W±, Z</text>

    <rect x="204" y="210" width="144" height="74" rx="8" fill="var(--surface)" stroke="var(--line)"/>
    <text x="216" y="232" class="mono" font-size="13" font-weight="800" fill="var(--c-act5)">e_R  [+ ν_R?]</text>
    <text x="216" y="252" class="mono" font-size="11.5" fill="var(--ink-2)">(1,1,−1) · [(1,1,0)]</text>
    <text x="216" y="270" font-size="11" fill="var(--ink-3)">Hypercharge only</text>

    <text x="44" y="314" font-size="12" font-weight="700" fill="var(--ink)">3 Families: (u,d,e,ν_e) · (c,s,μ,ν_μ) · (t,b,τ,ν_τ)</text>
    <text x="44" y="336" font-size="11.5" fill="var(--ink-2)">Misaligned Yukawas → V_CKM (3 angles + 1 CP phase)</text>
    <text x="44" y="356" font-size="11.5" fill="var(--ink-2)">Weinberg d=5 (LH)²/Λ → Majorana seesaw m_ν</text>

    <!-- Column 2: Spin 1 Gauge Bosons -->
    <rect x="380" y="82" width="196" height="316" rx="10" fill="var(--surface-2)" stroke="var(--c-act5)" stroke-width="2"/>
    <text x="396" y="108" font-size="13.5" font-weight="800" fill="var(--c-act5)">SPIN 1 · Gauge Connections</text>

    <rect x="396" y="122" width="164" height="74" rx="8" fill="var(--surface)" stroke="var(--line)"/>
    <text x="408" y="144" class="mono" font-size="13" font-weight="800" fill="var(--c-act7)">G_μ^a (8 Gluons)</text>
    <text x="408" y="164" class="mono" font-size="11.5" fill="var(--ink-2)">(8, 1, 0) · m = 0</text>
    <text x="408" y="182" font-size="11" fill="var(--ink-3)">β₀ &gt; 0 · Confining</text>

    <rect x="396" y="210" width="164" height="74" rx="8" fill="var(--surface)" stroke="var(--line)"/>
    <text x="408" y="232" class="mono" font-size="13" font-weight="800" fill="var(--c-act5)">W_μ^i (3 Weak)</text>
    <text x="408" y="252" class="mono" font-size="11.5" fill="var(--ink-2)">(1, 3, 0) → W± (80.4)</text>
    <text x="408" y="270" font-size="11" fill="var(--ink-3)">Mixes with B_μ via θ_W</text>

    <rect x="396" y="298" width="164" height="78" rx="8" fill="var(--surface)" stroke="var(--line)"/>
    <text x="408" y="320" class="mono" font-size="13" font-weight="800" fill="var(--c-act1)">B_μ (Hypercharge)</text>
    <text x="408" y="340" class="mono" font-size="11.5" fill="var(--ink-2)">(1, 1, 0) → Z⁰ &amp; γ</text>
    <text x="408" y="358" font-size="11" fill="var(--ink-3)">Q = T³ + Y unbroken</text>

    <!-- Column 3: Spin 0 Higgs Condensate -->
    <rect x="592" y="82" width="140" height="316" rx="10" fill="var(--surface-2)" stroke="var(--c-act2)" stroke-width="2"/>
    <text x="606" y="108" font-size="13.5" font-weight="800" fill="var(--c-act2)">SPIN 0 · Scalar</text>
    <circle cx="662" cy="196" r="46" fill="var(--surface)" stroke="var(--c-act2)" stroke-width="2.6"/>
    <text x="662" y="192" text-anchor="middle" class="mono" font-size="15" font-weight="800" fill="var(--c-act2)">H</text>
    <text x="662" y="212" text-anchor="middle" class="mono" font-size="11.5" fill="var(--ink-2)">(1, 2, +1/2)</text>
    <text x="662" y="272" text-anchor="middle" class="mono" font-size="12" font-weight="700">v = 246.2 GeV</text>
    <text x="662" y="294" text-anchor="middle" class="mono" font-size="12" fill="var(--c-act2)">m_h = 125.1 GeV</text>
    <text x="662" y="324" text-anchor="middle" font-size="11" fill="var(--ink-2)">Feeds W±, Z⁰</text>
    <text x="662" y="342" text-anchor="middle" font-size="11" fill="var(--ink-2)">&amp; Yukawa m_f</text>
    """
    plates.append({
        "id": "p12", "slug": "12-standard-model-taxonomic-plate", "act": "Act VII · Stop 24",
        "title": "Systema Camporum: Taxonomic Architecture of the Standard Model",
        "say": "Every elementary field in nature sits in a unique slot determined by Poincaré spin (0, 1/2, 1) and gauge representation under SU(3)_c × SU(2)_L × U(1)_Y.",
        "svg": wrap_svg("0 0 760 416", "Taxonomic architecture of the 17 Standard Model fields", p12_body, standalone),
    })

    return plates
