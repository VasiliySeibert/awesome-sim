# Changelog

All notable changes to this project are documented in this file.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Zenodo DOIs recorded in `CITATION.cff`, `codemeta.json`, and README badge.
  Concept DOI: `10.5281/zenodo.19677548`. Version DOIs: v1.0.0
  `10.5281/zenodo.19677549`, v1.1.0 `10.5281/zenodo.19677552`.

## [1.1.0] - 2026-04-21

### Added
- README section explaining the mathematical model (2D heat equation,
  boundary and initial conditions, finite-difference discretisation, CFL
  stability, energy monotonicity) with rendered LaTeX via GitHub math.
- `docs/snapshots.png` hero image and `docs/generate_hero_image.py` that
  reproduces it.

### Notes
- This is the version pinned by Practical 3 of the RDM Basics Lecture 4.
  Install with:
  `pip install "git+https://github.com/VasiliySeibert/awesome-sim@v1.1.0"`.
- First release archived on Zenodo via the GitHub ↔ Zenodo integration.

## [1.0.0] - 2026-04-20

### Added
- Stable public API: `HeatDiffusion2D`, `plot_snapshot`, `plot_snapshot_grid`,
  `animate`, `plot_energy_decay`.
- Minimal runnable example under `examples/minimal_example.py` producing a
  heatmap grid, an animated GIF, and an energy-decay plot.
- GitHub Actions CI on Python 3.11 and 3.12.
- FAIR metadata: `CITATION.cff` (CFF 1.2.0) and `codemeta.json` (CodeMeta 2.0).

### Notes
- This is the version pinned by Practical 3 of the RDM Basics Lecture 4.
  Install with:
  `pip install "git+https://github.com/VasiliySeibert/awesome-sim@v1.0.0"`.

## [0.1.0] - 2026-04-20

### Added
- Initial scaffold: package layout, MIT license, pyproject, gitignore.
- First working 2D heat-diffusion solver on a unit square with Dirichlet-0
  boundaries and a Gaussian hot-spot initial condition.
- Headless-safe Matplotlib plotting helpers.
- Smoke + energy-decay tests.
