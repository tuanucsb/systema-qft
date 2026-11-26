# Systema Camporum — Design System & Pedagogical Architecture (`DESIGN.md`)

**Systema Camporum** (*System of Fields: Graduate Quantum Field Theory & The Standard Model*) applies the natural-history architecture and learning principles of **Systema Intelligentiae** and **Systema Ratio** to build a step-by-step graduate QFT learning system synthesizing the strongest pedagogical insights of six canonical texts:
1. **David Tong** — *Lectures on QFT*, *Gauge Theory*, & *The Standard Model* (Cambridge Part III, free PDFs): physical intuition, geometric clarity, clean derivations.
2. **Matthew D. Schwartz** — *Quantum Field Theory and the Standard Model*: modern Wilsonian Effective Field Theory (EFT) viewpoint, physical spin-1 redundancy motivation, collider observables, precision QED/QCD/EW.
3. **Mark Srednicki** — *Quantum Field Theory* (UCSB official prepublication draft, free PDF): modular **Spin-0 → Spin-1/2 → Spin-1** progression, functional path integrals, \(\overline{\text{MS}}\) loop mechanics.
4. **Michael E. Peskin & Daniel V. Schroeder** — *An Introduction to Quantum Field Theory*: calculation craftsmanship, Dirac trace technology, Feynman diagram rules, Callan–Symanzik RG, Yang–Mills quantization.
5. **Steven Weinberg** — *The Quantum Theory of Fields (Vols. 1–2)*: inevitability of quantum fields from Poincaré representations \(ISO(1,3)\), cluster decomposition, causality, and little-group spin/helicity structure.
6. **Timo Weigand** — *Quantum Field Theory I + II* (Heidelberg Lecture Notes): mathematical precision bridging canonical operator methods, LSZ reduction, and electroweak symmetry breaking.

---

## 1. Seven *Systema Intelligentiae* Principles Adapted for Graduate QFT

1. **Intuition First, Grad Proof & Derivation on Demand**: Every stop and equation opens with a plain-English physical sentence (*what physical crisis forced this step, and what the equation actually says*), paired with a 1-click **Grad Derivation Mode (`Expert`)** revealing complete index-explicit steps (Wick contractions, Feynman parameters, DimReg poles \(\frac{2}{\epsilon} - \gamma_E + \ln 4\pi\), Ward identities, Faddeev–Popov determinants, Goldstone eaten modes).
2. **One Picture That Repeats (The 8-Part Field Spec-Board)**: Just as *Systema Intelligentiae* gives every organism the same 10-part board, **Systema Camporum** gives every field theory across all 24 stops the **same 8-Part Field Board** (`dof` Field & Spin, `sym` Symmetry Group, `lag` Action & Lagrangian, `prop` Propagator, `vert` Vertices & Couplings, `rg` Loops & RG Flow, `vac` Vacuum & Phases, `obs` Experimental Observable). Students learn the board once at Stop 01 and watch each slot upgrade all the way to \(\mathcal{L}_{\text{SM}}\).
3. **Everything Rests on Something Older (32-Node Dependency Tree)**: Interactive cladogram across 7 Acts × 8 Board Lanes where every QFT concept links backward (`rests_on`) and forward (`powers`).
4. **Interactive Term-by-Term Equation Dissector + Live Metric Signature Switch**: Every master equation breaks into clickable color-coded anatomical chunks showing natural-units mass dimension \([E]^d\), Lorentz/spinor/gauge index structure, physical job, and common sign traps. A global **Metric Switch** toggles live between **West Coast `(+ − − −)`** (Schwartz, Tong, Peskin, Weigand) and **East Coast `(− + + +)`** (Srednicki, Weinberg) so merging textbooks never causes sign confusion.
5. **One Spine**: 5 Architectural Floors on Overview → 24 Sequenced Grad Stops across 7 Acts → 16 Master Decoded Equations → 6 Live Interactive Physics Simulators → 12 Standalone Vector Plates.
6. **Colour Carries Meaning**: Each Act and equation role owns one WCAG-compliant semantic color across Light (`#f6f4ee`) and Dark (`#090c15`) Studio themes; crimson (`--c-crisis`) marks theoretical breakdowns (acausality, negative norm ghosts, UV/IR divergences, gauge anomalies).
7. **Empirical Honesty ("How We Know")**: Every abstract formalism connects directly to precision measurements (12-digit electron \(g-2\), running \(\alpha_{\text{em}}(M_Z)\) and \(\alpha_s(Q)\), \(\pi^0 \to \gamma\gamma\) proving \(N_c = 3\), \(M_W/M_Z\cos\theta_W\), Higgs \(125.10\text{ GeV}\)).

---

## 2. Semantic Color & Typography System

| Domain / Act | Token | Light Hex | Dark Hex | Meaning |
|---|---|---|---|---|
| Theoretical Crisis / Trap | `--c-crisis` | `#c81e3a` | `#ff6b84` | Causality leaks, ghosts, anomalies, sign traps |
| Act I · Spacetime & Symmetry | `--c-act1` | `#155e75` | `#38bdf8` | Poincaré group, Noether currents, action principle |
| Act II · Spin-0 & Path Integrals | `--c-act2` | `#0f766e` | `#2dd4bf` | Scalar oscillators, \(i\epsilon\) poles, \(\mathcal{Z}[J]\) |
| Act III · Perturbation & S-Matrix | `--c-act3` | `#b45309` | `#fbbf24` | Wick's theorem, LSZ amputation, \(d\sigma/d\Omega\) |
| Act IV · Spin-1/2 Fermions | `--c-act4` | `#4338ca` | `#818cf8` | Weyl/Dirac spinors, Pauli statistics, traces |
| Act V · Spin-1 & QED | `--c-act5` | `#1d4ed8` | `#60a5fa` | Gauge redundancy, Ward identities, QED scattering |
| Act VI · Loops, RG & EFT | `--c-act6` | `#7e22ce` | `#c084fc` | DimReg, counterterms, Wilsonian EFT, \(\beta(g)\) |
| Act VII · Yang–Mills & SM | `--c-act7` | `#be185d` | `#f472b6` | QCD, ghosts, Higgs SSB, EW mixing, anomalies, CKM |

- **Display**: `Fraunces` (`600..900`, optical size `9..144`)
- **UI & Body**: `Plus Jakarta Sans` (`400..800`, 16px base, `tabular-nums`)
- **Code, Dimensions & Indices**: `JetBrains Mono` (`500/700`, `>= 12px` floor)
- **Mathematics**: `KaTeX` (`0.16.11`) with instant client rendering and semantic fallback markup
