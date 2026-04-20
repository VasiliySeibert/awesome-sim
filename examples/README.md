# examples/

## `minimal_example.py`

A single self-contained script. Simulates 2D heat diffusion of a centred
Gaussian hot spot on a 200x200 grid with Dirichlet-0 walls, runs 500 explicit
Euler steps (~1-2 minutes on a laptop), and writes three figures to `out/`:

| File                       | What you see                                                        |
|----------------------------|---------------------------------------------------------------------|
| `out/heat.gif`             | Animated evolution of the temperature field, one frame per 10 steps |
| `out/snapshots.png`        | Four-panel snapshot grid at t = 0, ~1/3, ~2/3, end                  |
| `out/energy_decay.png`     | Total field energy (`sum(u**2)*dx*dy`) plotted against time         |

### Run it

```bash
pip install "git+https://github.com/VasiliySeibert/awesome-sim@v1.0.0"
python examples/minimal_example.py
```

### What should I see?

- In `heat.gif` and `snapshots.png`: the initially-sharp Gaussian hot spot
  **spreads radially** and **fades**. Near the walls it drops to zero
  (Dirichlet boundary).
- In `energy_decay.png`: a **monotonically non-increasing** curve — the
  physical expectation for heat diffusion with absorbing walls.

If the energy curve is non-monotonic, your `dt` likely violates the CFL
condition; the solver will also refuse to construct in that case.
