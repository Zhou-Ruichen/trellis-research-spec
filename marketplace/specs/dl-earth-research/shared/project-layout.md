# Project Layout

New projects should use one modern, predictable layout. Existing projects can
migrate toward this shape gradually; do not copy their disorder into new work.

## Required Layout For New Projects

```text
project/
  pyproject.toml
  README.md
  configs/
    base.yaml
    exp/
  data/
    raw/
    interim/
    processed/
    external/
    manifests/
  src/<pkg>/
    data/
    models/
    training/
    eval/
    utils/
  scripts/
  notebooks/
  tests/
  outputs/
  reports/
```

## Directory Contracts

| Path | Contract |
| --- | --- |
| `configs/` | YAML configs. All hyperparameters, data paths, run settings, and feature switches live here. |
| `configs/exp/` | Experiment overrides. Add files here instead of copying train/eval scripts. |
| `data/raw/` | Immutable project-local raw data, symlinks, small samples, or pointers to external data. |
| `data/interim/` | Intermediate outputs from data processing. Rebuildable. |
| `data/processed/` | Model-ready data products. Rebuildable and manifest-backed. |
| `data/external/` | Read-only external datasets or symlinks when a project-local pointer is useful. |
| `data/manifests/` | JSON/YAML records for source, version, checksum, processing parameters, and split definitions. |
| `src/<pkg>/data/` | Dataset, datamodule, transforms, split logic, data validation. |
| `src/<pkg>/models/` | `torch.nn.Module` model definitions and model blocks. |
| `src/<pkg>/training/` | Training loop, LightningModule, optimizer/scheduler/loss builders, checkpoint logic. |
| `src/<pkg>/eval/` | Metrics, prediction writers, evaluation routines, plotting helpers. |
| `src/<pkg>/utils/` | Small shared utilities: seed, logging, config, paths, devices. |
| `scripts/` | Thin command entrypoints only. Business logic belongs in `src/<pkg>/`. |
| `notebooks/` | Exploration and inspection. Stable code must move to `src/<pkg>/`. |
| `tests/` | Smoke tests, data-contract tests, shape tests, and small unit tests. |
| `outputs/<run_id>/` | Complete run artifacts: config snapshot, manifest, metrics, checkpoints, logs, predictions, figures. |
| `reports/` | Selected figures/tables for papers, presentations, and human review. |

## Naming Rules

- Use lower-case ASCII paths with underscores where needed.
- Prefer action-object names: `build_dataset.py`, `train.py`, `evaluate.py`.
- Do not use dates as normal versioning in source paths.
- Do not use non-ASCII filenames for code that agents must modify. Put Chinese notes in markdown if needed.

Bad:

```text
non_ascii_data_script.py
train_v2.py
train_final.py
output/
outputs/
SWOT_seafloor_gitfilter_backup_20251114/
```

Good:

```text
scripts/build_dataset.py
scripts/train.py
configs/exp/unet_geosat.yaml
outputs/20260610-142233-unet-geosat/
archive/2025-11-gitfilter-backup/
```

## Output Rule

Use `outputs/`, not `output/`. A project must not have both.

`outputs/<run_id>/` should contain:

```text
config.yaml
manifest.json
metrics.json
logs/
checkpoints/
predictions/
figures/
```

## Git Rule

Large or generated artifacts should normally be ignored:

```gitignore
data/raw/
data/interim/
data/processed/
data/external/
outputs/
*.ckpt
*.pt
*.pth
*.nc
*.npz
*.tif
*.tiff
```

Commit `data/manifests/`, small fixtures, code, configs, tests, and curated
`reports/` artifacts when they are intentionally part of the project record.
