# awesome-sim

[![CI](https://github.com/VasiliySeibert/awesome-sim/actions/workflows/ci.yml/badge.svg)](https://github.com/VasiliySeibert/awesome-sim/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Python: 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)

> A tiny, deliberately small, **FAIR** 2D heat-diffusion simulation —
> the running example for
> [NFDI4ING RDM Basics Lecture 4 (Research Software)](https://nfdi4ing.de/).

`awesome-sim` exists for one reason: to be **read end-to-end in a few
minutes**, so that a lecture audience can see how each
[FAIR4RS principle](https://www.rd-alliance.org/group/fair-principles-research-software-working-group)
is realised in a concrete artefact. It solves the 2D heat equation on a unit
square with Dirichlet-0 walls using an explicit finite-difference scheme. The
minimal example runs in ~1–2 minutes on a laptop and produces a heatmap
animation, a 4-panel snapshot grid, and an energy-decay plot.

## Install

From a git tag (the path we use in the lecture's Practical 3):

```bash
pip install "git+https://github.com/VasiliySeibert/awesome-sim@v1.0.0"
```

From a local clone (for development):

```bash
git clone https://github.com/VasiliySeibert/awesome-sim
cd awesome-sim
pip install -e ".[dev]"
```

## Quick start

```python
from awesome_sim import HeatDiffusion2D, animate, plot_energy_decay

sim = HeatDiffusion2D(nx=200, ny=200, alpha=1e-2, dt=5e-5)
snapshots = sim.run(n_steps=500, snapshot_every=10)
animate(snapshots, "heat.gif", fps=20)
```

Or run the full example:

```bash
python examples/minimal_example.py
# writes out/heat.gif, out/snapshots.png, out/energy_decay.png
```

## How this repository maps to FAIR4RS

| Principle | Evidence here |
|-----------|---------------|
| **F1 / F1.2** persistent identifier, version IDs | git tags `v0.1.0`, `v1.0.0`; Zenodo DOIs once the GitHub↔Zenodo integration is enabled |
| **F2 / F3 / F4** rich, discoverable metadata | [`CITATION.cff`](./CITATION.cff), [`codemeta.json`](./codemeta.json), `pyproject.toml`, this README |
| **A1 / A1.1** open retrieval | public GitHub over HTTPS, `pip install git+…` |
| **A1.2** auth where needed | only for private forks (PAT); this repo is public |
| **A2** metadata persists | Zenodo deposit + [Software Heritage](https://archive.softwareheritage.org/) archive |
| **I1 / I2** standards, qualified refs | JSON-LD metadata, SPDX license id, ORCID-qualified authorship, pinned dependencies |
| **R1.1** clear license | [`LICENSE`](./LICENSE) (SPDX: `MIT`) |
| **R1.2** provenance | git history + [`CHANGELOG.md`](./CHANGELOG.md) |
| **R2** qualified refs to other software | version-pinned `dependencies` in [`pyproject.toml`](./pyproject.toml) |
| **R3** community standards | PEP 621, CFF 1.2.0, CodeMeta 2.0, GitHub Actions CI |

## Repository layout

```
awesome-sim/
├── README.md                 # you are here
├── LICENSE                   # MIT
├── CITATION.cff              # how to cite
├── codemeta.json             # JSON-LD metadata
├── pyproject.toml            # build + pinned deps
├── CHANGELOG.md              # versioned provenance
├── .github/workflows/ci.yml  # automated build + test
├── src/awesome_sim/          # the package
│   ├── solver.py             # 2D heat FD solver
│   └── viz.py                # matplotlib helpers
├── examples/
│   └── minimal_example.py    # 1–2 minute runnable demo
└── tests/                    # smoke + energy-decay checks
```

## Citing this software

See [`CITATION.cff`](./CITATION.cff) — GitHub renders a "Cite this
repository" button on the sidebar that reads this file. Once the Zenodo
deposit exists, the file includes the version DOI as well.

## License

`awesome-sim` is released under the [MIT License](./LICENSE) — SPDX
identifier `MIT`.

## Acknowledgement

Developed for NFDI4ING, RDM Basics lecture series, by Vasiliy Seibert
([ORCID](https://orcid.org/0000-0002-7121-6816), TU Clausthal).
