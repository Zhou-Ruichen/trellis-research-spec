# Shared Research Guidelines

Applies to every task in this repository. Optimize for reproducibility,
iteration speed, and readable research code.

This spec is stronger than existing messy project history. If old files violate
these rules, treat them as migration candidates, not as patterns to copy.

## Documentation Files

| File | Read when |
| --- | --- |
| [project-layout.md](./project-layout.md) | Creating, moving, or naming files |
| [anti-bloat.md](./anti-bloat.md) | Adding files, variants, scripts, helpers, or abstractions |
| [reproducibility.md](./reproducibility.md) | Running or reporting experiments |
| [python-style.md](./python-style.md) | Writing Python modules |
| [../data/index.md](../data/index.md) | Touching data |
| [../training/index.md](../training/index.md) | Touching training or model code |
| [../evaluation/index.md](../evaluation/index.md) | Touching metrics, predictions, figures, or reports |

## Pre-Development Checklist

- [ ] Can this be expressed as a config change instead of new code?
- [ ] Is there an existing loader, transform, model block, metric, or utility to reuse?
- [ ] Is this exploratory? Keep it in `notebooks/` or a thin `scripts/` entrypoint.
- [ ] Is this durable? Put reusable logic under `src/<pkg>/`.
- [ ] Touching data? Check split, leakage, dtype, shape, coordinates, units, and manifest rules.
- [ ] Touching results? Decide whether each run is scratch, smoke, or
      retained; confirm where retained metrics, figures, config snapshots, and
      run manifests are written.

## Core Rules

- Use `src/<pkg>/` for reusable code. Do not build a pile of top-level scripts.
- Use `configs/` as the single source of truth for experiment knobs.
- A new experiment is a new config override under `configs/exp/`, not a copied training script.
- `data/` is allowed, but it must be structured by lifecycle and documented with manifests.
- `outputs/<run_id>/` is the canonical home for retained run artifacts.
- Scratch and smoke runs stay lightweight and disposable unless promoted.
- `reports/` is only for curated, lightweight figures and tables that are meant to be read.
- Delete code the current task superseded, once the replacement is verified;
  git history is the archive. Suspected-dead code, bulk cleanup, and
  experiment records (`outputs/` artifacts backing results, `data/manifests/`,
  configs still referenced, anything untracked) need asking first. List every
  deletion in the completion report.
- Do not productionize one-off exploration with factories, plugin systems, config classes, or extra CLI layers.

## Quality Check

Before claiming completion:

- [ ] The change follows [project-layout.md](./project-layout.md).
- [ ] No duplicate `*_v2.py`, `*_final.py`, copied experiment script, or backup directory was introduced.
- [ ] New reusable logic lives under `src/<pkg>/`, not in notebooks or ad hoc scripts.
- [ ] Any result claim is backed by a retained run artifact with config, seed,
      environment freeze, data manifest, and metrics.
- [ ] Any data-writing task records what was written, where it came from, and how to rebuild it.
