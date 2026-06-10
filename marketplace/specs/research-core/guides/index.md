# Research Core Guides

Use these guides for common research-code workflows.

## Documentation Files

| Guide | When to read |
| --- | --- |
| [add-run.md](./add-run.md) | Adding a new analysis, simulation, data-processing, or evaluation run |
| [code-review.md](./code-review.md) | Reviewing research-code changes before completion |

## Quick Navigation By Task

| Task | Read |
| --- | --- |
| Add a new run or comparison | [add-run.md](./add-run.md) |
| Process or validate data | [../data/index.md](../data/index.md) |
| Evaluate metrics, figures, or reports | [../evaluation/index.md](../evaluation/index.md) |
| Review for reproducibility and bloat | [code-review.md](./code-review.md) |

## Core Rules Summary

| Rule | Reference |
| --- | --- |
| Use parameters, configs, or retained commands instead of copied scripts | [../shared/anti-bloat.md](../shared/anti-bloat.md) |
| Retained runs need manifest, result files, data/source record, assumptions, and environment freeze | [../shared/reproducibility.md](../shared/reproducibility.md) |
| Scratch and smoke runs stay lightweight unless promoted | [../shared/reproducibility.md](../shared/reproducibility.md) |
| Durable data products need manifests | [../data/index.md](../data/index.md) |
| Reports must point back to retained evidence | [../evaluation/index.md](../evaluation/index.md) |
