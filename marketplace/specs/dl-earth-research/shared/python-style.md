# Python Style

Use simple, readable Python that is easy to inspect during research.

## Language

- Code, identifiers, docstrings, comments, filenames, and commit messages are
  written in English.
- The language of prose documents (notes, reports, notebook text) is a
  per-project choice: declare it in this project's spec and stay consistent.

## Project Style

- Put reusable code under `src/<pkg>/`.
- Keep `scripts/*.py` thin: parse config, call package functions, exit.
- Use type hints for public functions and tensor-heavy interfaces when they clarify shape or dtype.
- Keep tensor shape comments close to non-obvious transformations.
- Validate at I/O boundaries: config, files, external APIs, parsed data, and model inputs.
- Avoid broad defensive fallback logic. Unknown data or model states should fail loudly with useful context.

## Imports

Preferred order:

```python
import os
from pathlib import Path

import numpy as np
import torch

from research_project.data.dataset import BathymetryDataset
```

Do not mutate `sys.path` in durable code. Use an editable install or project
package layout instead.

## Paths

Use `pathlib.Path` for filesystem paths. Pass paths through config instead of
hardcoding workstation-specific locations.

Bad:

```python
DATA_ROOT = "/mnt/data2/00-Data"
lr = 3e-4
```

Good:

```python
data_root = Path(cfg.data.root)
lr = cfg.optimizer.lr
```

## Tensor And Array Code

- Be explicit about expected dimensions for non-trivial tensors.
- Check shape, dtype, finite values, coordinate bounds, and NaN rules at dataset boundaries.
- Keep device and dtype ownership obvious. Avoid hidden `.cuda()` calls inside low-level helpers.

Example:

```python
def normalize_grid(x: torch.Tensor, mean: torch.Tensor, std: torch.Tensor) -> torch.Tensor:
    """Normalize bathymetry-like grids.

    Args:
        x: Tensor with shape [batch, channels, height, width].
    """
    return (x - mean[None, :, None, None]) / std[None, :, None, None]
```

## Tests

Minimum meaningful tests:

- config loads;
- dataset returns expected keys, shapes, dtype, and finite values on a tiny fixture;
- one training step runs on CPU with a tiny batch;
- evaluation writes `metrics.json` with the expected schema.

