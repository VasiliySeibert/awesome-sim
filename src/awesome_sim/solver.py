"""2D heat-equation solver on a unit square with Dirichlet-0 boundaries.

The governing PDE is ``du/dt = alpha * laplacian(u)`` discretised with a
five-point finite-difference stencil and integrated forward in time with
explicit Euler. The implementation is pure NumPy and vectorised, so a
200x200 grid runs in ~1 minute on a laptop.

References
----------
Standard finite-difference scheme; see e.g. LeVeque, "Finite Difference
Methods for Ordinary and Partial Differential Equations" (SIAM, 2007).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray


@dataclass
class HeatDiffusion2D:
    """Explicit-Euler finite-difference solver for the 2D heat equation.

    Parameters
    ----------
    nx, ny:
        Grid size in the x and y directions.
    alpha:
        Thermal diffusivity. Larger values spread heat faster.
    dt:
        Time step. Must satisfy the CFL condition ``dt <= dx**2 / (4*alpha)``
        for stability; otherwise the solver raises at construction time.
    length:
        Physical side length of the (square) domain. Defaults to 1.0.
    """

    nx: int = 200
    ny: int = 200
    alpha: float = 1.0e-2
    dt: float = 5.0e-5
    length: float = 1.0

    def __post_init__(self) -> None:
        if self.nx < 3 or self.ny < 3:
            raise ValueError("grid must be at least 3x3")
        self.dx = self.length / (self.nx - 1)
        self.dy = self.length / (self.ny - 1)
        cfl = min(self.dx, self.dy) ** 2 / (4.0 * self.alpha)
        if self.dt > cfl:
            raise ValueError(
                f"dt={self.dt} violates 2D CFL limit {cfl:.3e} "
                f"for alpha={self.alpha}, dx={self.dx:.3e}"
            )
        self.u = self._gaussian_hot_spot()
        self.t = 0.0
        self.step_count = 0

    def _gaussian_hot_spot(self, sigma: float = 0.08, amplitude: float = 1.0) -> NDArray[np.float64]:
        x = np.linspace(0.0, self.length, self.nx)
        y = np.linspace(0.0, self.length, self.ny)
        xx, yy = np.meshgrid(x, y, indexing="xy")
        cx = cy = 0.5 * self.length
        u = amplitude * np.exp(-((xx - cx) ** 2 + (yy - cy) ** 2) / (2.0 * sigma**2))
        # Dirichlet-0 walls
        u[0, :] = u[-1, :] = u[:, 0] = u[:, -1] = 0.0
        return u

    def step(self) -> None:
        """Advance the solution by one time step."""
        u = self.u
        lap = np.zeros_like(u)
        lap[1:-1, 1:-1] = (
            (u[1:-1, 2:] - 2.0 * u[1:-1, 1:-1] + u[1:-1, :-2]) / self.dx**2
            + (u[2:, 1:-1] - 2.0 * u[1:-1, 1:-1] + u[:-2, 1:-1]) / self.dy**2
        )
        u_new = u + self.dt * self.alpha * lap
        u_new[0, :] = u_new[-1, :] = u_new[:, 0] = u_new[:, -1] = 0.0
        self.u = u_new
        self.t += self.dt
        self.step_count += 1

    def run(
        self,
        n_steps: int,
        snapshot_every: int | None = None,
    ) -> list[NDArray[np.float64]]:
        """Advance ``n_steps`` steps, optionally recording snapshots.

        Parameters
        ----------
        n_steps:
            Number of Euler steps to take.
        snapshot_every:
            If given, append a copy of ``self.u`` every ``snapshot_every``
            steps (the initial state is always recorded as snapshot 0).
            If ``None``, no snapshots are kept and an empty list is returned.
        """
        snapshots: list[NDArray[np.float64]] = []
        if snapshot_every is not None:
            snapshots.append(self.u.copy())
        for i in range(1, n_steps + 1):
            self.step()
            if snapshot_every is not None and i % snapshot_every == 0:
                snapshots.append(self.u.copy())
        return snapshots

    def total_energy(self) -> float:
        """Integrated field energy ``sum(u**2) * dx * dy`` (proxy for heat)."""
        return float(np.sum(self.u**2) * self.dx * self.dy)
