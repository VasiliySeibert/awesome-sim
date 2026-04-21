"""Regenerate the ``docs/snapshots.png`` figure used in the README.

This runs a smaller, faster version of the minimal example (the README is
static documentation, not a benchmark, so we do not need the full 800x800
run here) and writes the resulting 4-panel grid next to this script.

Usage::

    python docs/generate_hero_image.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

from awesome_sim import HeatDiffusion2D
from awesome_sim.viz import plot_snapshot_grid

GRID = 400
N_STEPS = 8000
SNAPSHOT_EVERY = 200
ALPHA = 1.0e-2
DT = 5.0e-5


def main() -> None:
    out = Path(__file__).resolve().parent / "snapshots.png"
    sim = HeatDiffusion2D(nx=GRID, ny=GRID, alpha=ALPHA, dt=DT)
    snapshots = [sim.u.copy()]
    for i in range(1, N_STEPS + 1):
        sim.step()
        if i % SNAPSHOT_EVERY == 0:
            snapshots.append(sim.u.copy())
    n = len(snapshots)
    idx = [0, n // 3, (2 * n) // 3, n - 1]
    plot_snapshot_grid(
        [snapshots[i] for i in idx],
        [i * SNAPSHOT_EVERY * DT for i in idx],
        out,
    )
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
