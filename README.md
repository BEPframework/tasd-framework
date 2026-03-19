[README.md](https://github.com/user-attachments/files/26103067/README.md)
# TASD Unified Framework v1.0

**Toroidal-Attractor Signal Dynamics**

The mathematical unification of the **Ψ_universe attractor** with toroidal-modulated frequency-domain dynamics. Includes the master TASD equation, full Lyapunov stability proof, and real EAST #41195 validation.

---

### Core Features

- Master **TASD equation** (theoretical core)
- Full **Lyapunov stability proof**
- Real **EAST #41195 validation**
- Seamless integration with [PsiFilter v2.0](https://github.com/BEPframework/psi-universe-attractor) and [TDT](https://github.com/BEPframework/toroidal-dynamics-toolkit)

### Quick Start

```bash
python tasd_example.py
```

Or use the framework directly:

```python
from tasd_framework import TASDFramework

tasd = TASDFramework()
tasd.run_tasd_on_real_data()
```

Dependencies: Python 3.x, NumPy, SciPy.

### Related Repositories

- [psi-universe-attractor](https://github.com/BEPframework/psi-universe-attractor) — Ψ_universe attractor filter, validated on real EAST #41195 data
- [tasd-core](https://github.com/BEPframework/tasd-core) — TASD Core Framework (capstone documentation)
- [toroidal-dynamics-toolkit](https://github.com/BEPframework/toroidal-dynamics-toolkit) — Modular toolkit for dynamic toroidal modulation in frequency-domain signal processing
- [q216d-tokamak-simulation](https://github.com/BEPframework/q216d-tokamak-simulation) — Interactive 3D plasma visualization with TASD-enhanced control

### Copyright

Copyright © 2026 Nicolas B. Quiroz, MD. All rights reserved for the original work.

### License

See the [LICENSE](LICENSE) file for details.

### Citation

If you use this framework, please cite:

> **Quiroz, N. B. (2026)**. *TASD Unified Framework v1.0 — Toroidal-Attractor Signal Dynamics*. Zenodo. https://doi.org/10.5281/zenodo.18926748

### Keywords

tokamak · fusion energy · plasma physics · toroidal plasma · magnetic confinement · plasma attractor dynamics · Lyapunov stability
