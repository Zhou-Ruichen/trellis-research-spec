# Deep Learning Earth Research Spec

This spec is for research repositories that process geoscience data and train
deep-learning models for inversion, prediction, reconstruction, or analysis.

It is intentionally opinionated for new work. Existing messy repositories can
adopt it gradually, but agents should not preserve messy historical layouts as
precedent.

The template is Python-first, not Python-only. Python/PyTorch conventions are
included because they are the expected main stack, while the reproducibility,
anti-bloat, data, and run-manifest contracts apply to mixed-language project
code as well. Add project-local language rules for durable CUDA/C++, Fortran,
Julia, Rust, or shell code when needed.

## Documentation Files

| File | Read when |
| --- | --- |
| [shared/index.md](./shared/index.md) | Before any implementation task |
| [shared/project-layout.md](./shared/project-layout.md) | Creating files or directories |
| [shared/anti-bloat.md](./shared/anti-bloat.md) | Adding files, variants, scripts, or abstractions |
| [shared/reproducibility.md](./shared/reproducibility.md) | Running experiments or reporting results |
| [shared/python-style.md](./shared/python-style.md) | Writing Python modules |
| [data/index.md](./data/index.md) | Reading, writing, processing, or validating data |
| [training/index.md](./training/index.md) | Training, checkpoints, configs, or model code |
| [evaluation/index.md](./evaluation/index.md) | Metrics, figures, predictions, or reports |
| [guides/add-experiment.md](./guides/add-experiment.md) | Adding a new experiment |
| [guides/debug-nan-oom.md](./guides/debug-nan-oom.md) | Debugging NaN, inf, divergence, or OOM |
| [guides/code-review.md](./guides/code-review.md) | Reviewing research-code changes |

## Project Goal

Make new research code easy to run, inspect, compare, and reproduce without
turning exploratory work into over-engineered product code.

## Required Shape For New Projects

```text
project/
  pyproject.toml
  README.md
  configs/
  data/
  src/<pkg>/
  scripts/
  notebooks/
  tests/
  outputs/
  reports/
```

Use this shape for new work unless the user explicitly chooses a narrower
one-off scratch directory.
