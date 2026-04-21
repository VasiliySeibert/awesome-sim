# RDM Basics 4 · slides (GitHub Pages branch of `awesome-sim`)

**Live:** <https://vasiliyseibert.github.io/awesome-sim/>

This branch is a static Reveal.js site — the slide deck for **NFDI4ING RDM
Basics Lecture 4 — _Research Software / FAIR4RS_**. It lives on the `gh-pages`
branch of [`VasiliySeibert/awesome-sim`](https://github.com/VasiliySeibert/awesome-sim)
so that the lecture slides and the lecture's running-example code are published
from the same repo.

---

## Context (for a future LLM walking in cold)

- **Parent project:** `RDM-Basics` — a meta-repo under
  `/Users/vasiliy/Desktop/RDM-Basics/RDM-Basics` that collects source material
  (earlier lectures, the Betty workflow, FAIR4RS, raw PDFs) and coordinates
  preparation of the four lectures.
- **Target lecture:** `RDM-Basics-4/Agenda.md` — the _authoritative_ agenda
  document. ~50 slides, 90 minutes, English, structured as 3 × 13-min theory
  blocks (F+A, I, R) alternating with 3 × 14-min practicals (Betty Research
  Engine, Terminology Service, Jupyter Service), plus opening and wrap-up.
  **Always re-read `Agenda.md` when in doubt about scope, ordering, or tone.**
- **Running example:** [`awesome-sim`](https://github.com/VasiliySeibert/awesome-sim)
  — a deliberately small 2D heat-diffusion simulator prepared so every
  FAIR4RS principle can be pointed to a concrete artefact (Zenodo DOI,
  `CITATION.cff`, `codemeta.json`, SPDX licence, pinned `pyproject.toml`,
  CI). This branch (`gh-pages`) is the slide deck _for_ that repo's `main`
  branch.
- **FAIR4RS source text:** `../fair4rs/fair4rs.md` in the parent meta-repo
  (`RDM-Basics/fair4rs/fair4rs.md`). Verbatim quotes of principles on slides
  come from there. Do not paraphrase the principle text without checking.
- **Design template:** `../DesignTemplate.pptx` — extracted colour palette
  (`#2839CC` primary blue, `#0C113D` navy, `#F3F051` yellow accent,
  `#D5763D` orange) and the low-poly geometric backgrounds used on title and
  divider slides. Typography is IBM Plex Sans / Mono, matching the template.

## What's in this repo (branch)

```
.
├── index.html                  # all 51 slides inline — single entry point
├── css/
│   ├── nfdi4ing-theme.css      # brand palette, typography, header/footer,
│   │                           #   title/divider layouts, slide number,
│   │                           #   Reveal control tinting
│   └── slides.css              # content layout primitives:
│                               #   .two-col .three-col .card .callout
│                               #   .task-list .service-chip .fair-grid
│                               #   .artefact (code card) .chip-link
│                               #   .principle-quote .gloss .check
├── assets/
│   ├── logos/                  # brand-mark-1.jpg (CC BY 4.0 badge)
│   │                           # brand-mark-2.png (blue circle motif)
│   │                           # small-mark.png  (outlined circle motif)
│   └── img/
│       ├── heat-hero.png       # copied from awesome-sim/docs/snapshots.png
│       ├── image3.jpg image4.jpg image5.jpg   # low-poly blue hero backgrounds
│       ├── image7.png … image13.png           # low-poly character portraits
│                                               #   (from DesignTemplate.pptx)
├── .nojekyll                   # tells GH Pages to serve files verbatim
├── LICENSE                     # MIT (copied from awesome-sim main)
└── README.md                   # this file
```

## Slide structure (51 total, mirrors `Agenda.md`)

For each theory block, slides alternate `… · Principle` (verbatim FAIR4RS
quote + plain-English gloss + mapping to `awesome-sim`) with `… · In practice`
(concrete artefact / code / screenshot). The chip in the slide header says
which of the two you're on.

| Block | Count | Notes |
|---|---:|---|
| 0 · Opening                   | 5  | Title, series recap, agenda table, software ≠ data, running examples |
| 1 · Findable & Accessible     | 13 | Divider + 5 Principle + 6 In-practice + Recap (F1, F1.1/F1.2, F2/F3/F4, A1/A1.1, A1.2, A2) |
| 2 · Practical 1               | 3  | Divider, Betty Research Engine task list, reflection |
| 3 · Interoperable             | 10 | Divider + 2 Principle + 5 In-practice + Recap (I1, I2) |
| 4 · Practical 2               | 3  | Divider, Terminology Service task list, reflection |
| 5 · Reusable                  | 11 | Divider + 3 Principle + 6 In-practice + Sustainability + Recap (R1/R1.1/R1.2, R2, R3) |
| 6 · Practical 3               | 3  | Divider, Jupyter Service task list, reflection |
| 7 · Wrap-up                   | 3  | FAIR4RS checklist grid, service map, thank-you |

## Run locally

```bash
git clone -b gh-pages https://github.com/VasiliySeibert/awesome-sim awesome-sim-pages
cd awesome-sim-pages
python3 -m http.server 8000
# open http://localhost:8000
```

Keyboard: `← / →` navigate · `S` speaker view · `F` fullscreen · `?` help.

**PDF export:** append `?print-pdf` to the URL, then *Print → Save as PDF* in
Chrome. 51 landscape pages.

## Develop & deploy

This is a pure static site, **no build step**. To edit:

1. Check out the branch:
   ```bash
   git worktree add ../awesome-sim-pages gh-pages   # from awesome-sim main
   cd ../awesome-sim-pages
   ```
2. Edit `index.html` (all slides inline), `css/nfdi4ing-theme.css`, or
   `css/slides.css`.
3. Preview locally: `python3 -m http.server 8000`.
4. Commit + push:
   ```bash
   git add -A
   git commit -m "…"
   git push origin gh-pages
   ```
5. GitHub Pages auto-rebuilds the site within ~30 s of every push to
   `gh-pages`. No Actions workflow needed — Pages is configured to serve the
   `gh-pages` branch root (`/`).

## Design system (summary)

| Token          | Hex       | Usage                                |
|----------------|-----------|--------------------------------------|
| `--n4i-blue`   | `#2839CC` | primary, links, headings accent      |
| `--n4i-blue-2` | `#202EA3` | gradient partner                     |
| `--n4i-navy`   | `#0C113D` | deep headings, code-card background  |
| `--n4i-yellow` | `#F3F051` | highlights, divider rule, principle-quote accent |
| `--n4i-orange` | `#D5763D` | I-block accents                      |
| `--n4i-pink`   | `#E60C61` | R-block accents                      |
| `--n4i-green`  | `#1B8044` | A-block accents                      |

Typography: **IBM Plex Sans** (body), **IBM Plex Mono** (code, DOIs,
service chips) — both loaded from Google Fonts.

## Reveal.js configuration

Loaded from `cdn.jsdelivr.net/npm/reveal.js@5.1.0`. Plugins: Highlight,
Notes, Search, Math (KaTeX).

- `controlsLayout: 'edges'` — navigation arrows live on the viewport edges,
  not the bottom-right corner, so they don't collide with the slide number.
- `slideNumber: 'c/t'` — current / total, bottom-right, monospace.
- `transition: 'fade'` / `backgroundTransition: 'fade'` — no flashy spins.
- `width: 1280, height: 800` — 16:10 base, fits both 1920×1080 projectors
  and laptop screens via Reveal's built-in scaling.

## Slide layout conventions (when editing)

Every content slide should have this skeleton:

```html
<section class="content">
  <div class="slide-header">
    <span class="brand">Block name</span>
    <span class="chip">Sub-topic · Principle | In practice</span>
  </div>

  <h1>Slide title<span class="fair-pill F">F1</span></h1>

  <div class="two-col mt">
    <div class="col">…</div>
    <div class="col">…</div>
  </div>

  <div class="slide-footer">
    <span class="fair">Block N · Name</span>
    <span>Sub-topic</span>
  </div>
</section>
```

For a **principle-explainer** slide (FAIR4RS quote + `awesome-sim` mapping),
use:

```html
<div class="principle-quote">
  <span class="label">FAIR4RS · F1</span>
  <q>Software is assigned a globally unique and persistent identifier.</q>
</div>
<p class="gloss">In plain English: …</p>
```

Then mirror on the right column with `<div class="mapping-title">In awesome-sim</div>`
followed by `<ul class="check">` (✓ bulleted list).

## Licence

- Code (HTML, CSS, JS glue): **MIT** — same as `awesome-sim` main.
- Content (prose, figures, principle explanations): **CC BY 4.0** —
  NFDI4ING / Vasiliy Seibert, 2026. Reuse freely with attribution.

## Who & when

Prepared for the **NFDI4ING RDM Basics for Engineers** lecture series,
Lecture 4 (of 4), by [Vasiliy Seibert](https://orcid.org/0000-0002-7121-6816)
(TU Clausthal) with Claude Code assistance.
