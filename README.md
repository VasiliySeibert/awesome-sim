# RDM Basics 4 · slides (GitHub Pages branch)

Slide deck for **NFDI4ING RDM Basics Lecture 4 — Research Software / FAIR4RS**.
Lives on the `gh-pages` branch of
[`awesome-sim`](https://github.com/VasiliySeibert/awesome-sim); built with
[Reveal.js 5](https://revealjs.com) as a pure static site (no build step).

Live: <https://vasiliyseibert.github.io/awesome-sim/>

## Run locally

```bash
git clone -b gh-pages https://github.com/VasiliySeibert/awesome-sim awesome-sim-pages
cd awesome-sim-pages
python -m http.server 8000
# open http://localhost:8000
```

Keyboard: `←` / `→` navigate · `S` speaker view · `F` fullscreen · `?` help.

PDF export: append `?print-pdf` to the URL, then use the browser's *Print → Save as PDF*.

## Layout

```
/
├── index.html                  # all ~40 slides inline
├── css/
│   ├── nfdi4ing-theme.css      # brand colors + typography
│   └── slides.css              # layout primitives
├── assets/
│   ├── logos/                  # brand marks (from DesignTemplate.pptx)
│   └── img/                    # heat-hero, low-poly backgrounds
└── .nojekyll                   # serve plugin assets verbatim on Pages
```

## Design system

Palette extracted from `RDM-Basics-4/DesignTemplate.pptx`:

| Token          | Hex       | Usage                    |
|----------------|-----------|--------------------------|
| `--n4i-blue`   | `#2839CC` | primary, links, accents  |
| `--n4i-navy`   | `#0C113D` | headings, code cards     |
| `--n4i-yellow` | `#F3F051` | highlights, divider rule |
| `--n4i-orange` | `#D5763D` | I-block accents          |
| `--n4i-pink`   | `#E60C61` | R-block accents          |

Typography: **IBM Plex Sans** / **IBM Plex Mono** via Google Fonts.

## License

Code (HTML/CSS): MIT.
Content (prose, figures): CC BY 4.0 — NFDI4ING / Vasiliy Seibert, 2026.
