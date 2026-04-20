"""Plotting helpers for awesome-sim.

All functions use Matplotlib's ``Agg`` backend implicitly via ``matplotlib.use``
guards in callers, so they are safe to use in headless environments (CI,
Jupyter on a server, etc.).
"""

from __future__ import annotations

from pathlib import Path
from typing import Sequence

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter
from numpy.typing import NDArray


def plot_snapshot(
    field: NDArray[np.float64],
    outfile: str | Path,
    title: str = "",
    vmin: float | None = 0.0,
    vmax: float | None = 1.0,
) -> None:
    """Save a single heatmap PNG of ``field``."""
    fig, ax = plt.subplots(figsize=(5, 4))
    im = ax.imshow(field, origin="lower", cmap="inferno", vmin=vmin, vmax=vmax)
    ax.set_title(title)
    ax.set_xlabel("x [grid]")
    ax.set_ylabel("y [grid]")
    fig.colorbar(im, ax=ax, label="temperature")
    fig.tight_layout()
    fig.savefig(outfile, dpi=120)
    plt.close(fig)


def plot_snapshot_grid(
    snapshots: Sequence[NDArray[np.float64]],
    times: Sequence[float],
    outfile: str | Path,
    vmin: float | None = 0.0,
    vmax: float | None = 1.0,
) -> None:
    """Save a 2x2 panel of the first four snapshots passed in."""
    if len(snapshots) < 4 or len(times) < 4:
        raise ValueError("plot_snapshot_grid needs at least 4 snapshots/times")
    fig, axes = plt.subplots(2, 2, figsize=(9, 8))
    for ax, frame, t in zip(axes.ravel(), snapshots[:4], times[:4]):
        im = ax.imshow(frame, origin="lower", cmap="inferno", vmin=vmin, vmax=vmax)
        ax.set_title(f"t = {t:.4f}")
        ax.set_xticks([])
        ax.set_yticks([])
    fig.colorbar(im, ax=axes.ravel().tolist(), label="temperature", shrink=0.8)
    fig.savefig(outfile, dpi=120, bbox_inches="tight")
    plt.close(fig)


def animate(
    snapshots: Sequence[NDArray[np.float64]],
    outfile: str | Path,
    fps: int = 20,
    vmin: float | None = 0.0,
    vmax: float | None = 1.0,
) -> None:
    """Write an animated GIF stepping through ``snapshots`` at ``fps``."""
    if not snapshots:
        raise ValueError("no snapshots to animate")
    fig, ax = plt.subplots(figsize=(5, 4))
    im = ax.imshow(snapshots[0], origin="lower", cmap="inferno", vmin=vmin, vmax=vmax)
    ax.set_xlabel("x [grid]")
    ax.set_ylabel("y [grid]")
    fig.colorbar(im, ax=ax, label="temperature")

    def _update(frame_idx: int):
        im.set_array(snapshots[frame_idx])
        ax.set_title(f"frame {frame_idx}/{len(snapshots) - 1}")
        return (im,)

    anim = FuncAnimation(fig, _update, frames=len(snapshots), interval=1000 / fps, blit=False)
    anim.save(outfile, writer=PillowWriter(fps=fps))
    plt.close(fig)


def plot_energy_decay(
    energies: Sequence[float],
    times: Sequence[float],
    outfile: str | Path,
) -> None:
    """Save a line plot of total field energy vs simulated time."""
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(times, energies, marker="o", markersize=3)
    ax.set_xlabel("time")
    ax.set_ylabel("total field energy")
    ax.set_title("Energy decay (Dirichlet-0 walls)")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(outfile, dpi=120)
    plt.close(fig)
