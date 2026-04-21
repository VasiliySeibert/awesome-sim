"""awesome-sim: a tiny 2D heat-diffusion reference simulation.

This package is the running example for NFDI4ING RDM Basics Lecture 4
(Research Software). It is intentionally small, well-documented, and FAIR
so that participants can read it end-to-end in a few minutes.
"""

from awesome_sim.solver import HeatDiffusion2D
from awesome_sim.viz import animate, plot_energy_decay, plot_snapshot

__version__ = "1.1.0"

__all__ = [
    "HeatDiffusion2D",
    "animate",
    "plot_energy_decay",
    "plot_snapshot",
    "__version__",
]
