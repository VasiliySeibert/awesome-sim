"""Minimal runnable example for awesome-sim.

Run time target: ~1-2 minutes on a laptop. Writes three figures under ``out/``:

- ``heat.gif``         : animated evolution of the hot-spot
- ``snapshots.png``    : 2x2 panel at t = 0, 25 %, 50 %, 100 %
- ``energy_decay.png`` : total field energy vs time

Usage::

    python examples/minimal_example.py
"""

from __future__ import annotations

import time
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless-safe

from awesome_sim import HeatDiffusion2D
from awesome_sim.viz import animate, plot_energy_decay, plot_snapshot_grid

N_STEPS = 30000
SNAPSHOT_EVERY = 600
GRID = 800
ALPHA = 1.0e-2
DT = 2.0e-5
# Downsample frames for the GIF so the output file stays reasonable
GIF_DOWNSAMPLE = 5


def main() -> None:
    out_dir = Path(__file__).resolve().parent / "out"
    out_dir.mkdir(exist_ok=True)

    print(f"[awesome-sim] grid={GRID}x{GRID}, steps={N_STEPS}, alpha={ALPHA}, dt={DT}")
    sim = HeatDiffusion2D(nx=GRID, ny=GRID, alpha=ALPHA, dt=DT)

    energies: list[float] = [sim.total_energy()]
    times: list[float] = [sim.t]

    t0 = time.perf_counter()
    snapshots = [sim.u.copy()]
    for i in range(1, N_STEPS + 1):
        sim.step()
        if i % SNAPSHOT_EVERY == 0:
            snapshots.append(sim.u.copy())
            energies.append(sim.total_energy())
            times.append(sim.t)
    wall = time.perf_counter() - t0

    print(f"[awesome-sim] simulation wall-clock: {wall:.2f} s")
    print(f"[awesome-sim] peak temperature now:  {sim.u.max():.4f}")
    print(f"[awesome-sim] snapshots captured:    {len(snapshots)}")

    # Pick 4 panels: start, 1/3, 2/3, end
    n = len(snapshots)
    idx = [0, n // 3, (2 * n) // 3, n - 1]
    plot_snapshot_grid(
        [snapshots[i] for i in idx],
        [i * SNAPSHOT_EVERY * DT for i in idx],
        out_dir / "snapshots.png",
    )
    plot_energy_decay(energies, times, out_dir / "energy_decay.png")
    gif_snapshots = [s[::GIF_DOWNSAMPLE, ::GIF_DOWNSAMPLE] for s in snapshots]
    animate(gif_snapshots, out_dir / "heat.gif", fps=20)

    print(f"[awesome-sim] wrote outputs to: {out_dir}")


if __name__ == "__main__":
    main()
