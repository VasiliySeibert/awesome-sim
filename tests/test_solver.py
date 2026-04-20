"""Smoke + sanity tests for awesome-sim."""

from __future__ import annotations

import numpy as np
import pytest

from awesome_sim import HeatDiffusion2D


def test_constructs_and_shape_preserved() -> None:
    sim = HeatDiffusion2D(nx=50, ny=50, alpha=1e-2, dt=1e-4)
    assert sim.u.shape == (50, 50)
    sim.step()
    assert sim.u.shape == (50, 50)
    assert sim.step_count == 1


def test_initial_peak_at_center() -> None:
    sim = HeatDiffusion2D(nx=51, ny=51, alpha=1e-2, dt=1e-4)
    # center indices
    peak_idx = np.unravel_index(np.argmax(sim.u), sim.u.shape)
    assert peak_idx == (25, 25)


def test_walls_stay_zero() -> None:
    sim = HeatDiffusion2D(nx=40, ny=40, alpha=1e-2, dt=1e-4)
    sim.run(20)
    assert np.all(sim.u[0, :] == 0.0)
    assert np.all(sim.u[-1, :] == 0.0)
    assert np.all(sim.u[:, 0] == 0.0)
    assert np.all(sim.u[:, -1] == 0.0)


def test_no_nan_or_inf_after_run() -> None:
    sim = HeatDiffusion2D(nx=50, ny=50, alpha=1e-2, dt=1e-4)
    sim.run(50)
    assert np.all(np.isfinite(sim.u))


def test_energy_monotonically_nonincreasing() -> None:
    sim = HeatDiffusion2D(nx=50, ny=50, alpha=1e-2, dt=1e-4)
    energies = [sim.total_energy()]
    for _ in range(50):
        sim.step()
        energies.append(sim.total_energy())
    # Strict non-increase (tiny numerical wiggle at float64: allow 1e-12 slack)
    diffs = np.diff(energies)
    assert np.all(diffs <= 1e-12), f"energy increased: max delta={diffs.max():.3e}"


def test_cfl_violation_rejected() -> None:
    # dx = 1/(9) ≈ 0.111; CFL: dt <= dx^2 / (4*alpha) = 0.111^2/(4*0.1) ≈ 0.031
    with pytest.raises(ValueError, match="CFL"):
        HeatDiffusion2D(nx=10, ny=10, alpha=0.1, dt=1.0)
