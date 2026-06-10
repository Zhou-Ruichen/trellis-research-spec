# Training Guidelines

Use these rules for model definitions, training loops, config files,
checkpoints, and experiment variants.

## Preferred Stack

- Python package layout under `src/<pkg>/`.
- PyTorch for model code.
- Lightning is acceptable when it is already the project choice.
- YAML config files in `configs/`.
- Optional Hydra/OmegaConf is acceptable, but do not add it to small scripts only
  to look structured.

## Required Training Layout

```text
configs/
  base.yaml
  data/
  model/
  exp/
src/<pkg>/
  data/
  models/
  training/
scripts/
  train.py
```

`scripts/train.py` should be a thin entrypoint:

1. load config;
2. resolve paths;
3. set seed;
4. create datamodule/dataloaders;
5. create model/trainer;
6. write run manifest;
7. train.

Reusable logic belongs under `src/<pkg>/`.

## Config Rule

Configs are the single source of truth for:

- data paths and manifest paths;
- model architecture;
- loss and metrics;
- optimizer and scheduler;
- batch size, epochs, precision, devices, gradient accumulation;
- seed and determinism settings;
- output root and run naming.

Bad:

```python
lr = 3e-4
batch_size = 8
model = UNet(channels=64)
```

Good:

```python
lr = cfg.optimizer.lr
batch_size = cfg.training.batch_size
model = build_model(cfg.model)
```

## Experiment Variants

A new experiment is a config override:

```text
configs/exp/unet_swot.yaml
configs/exp/transformer_unet_swot_gravity.yaml
configs/exp/ablation_no_gravity.yaml
```

Never add:

```text
scripts/train_v2.py
scripts/train_transformer_final.py
src/<pkg>/training/train_old.py
```

## Checkpoints

Write checkpoints under:

```text
outputs/<run_id>/checkpoints/
```

Checkpoint filenames should include epoch and a primary validation metric when
available:

```text
epoch=012-val_rmse=123.456.ckpt
```

Do not store checkpoints in source directories.

## Minimal Smoke Test

Every training project should support a tiny CPU smoke run:

```text
configs/exp/smoke.yaml
```

The smoke config should:

- use a tiny fixture or tiny subset;
- run one epoch or one training step;
- avoid GPU-only assumptions;
- verify loss is finite;
- write a manifest and metrics file.

## Quality Check

- [ ] New experiment added a config, not a copied training script.
- [ ] Training outputs land under `outputs/<run_id>/`.
- [ ] Run manifest records config, seed, code state, environment, and data manifest.
- [ ] One small smoke path exists or was updated when training behavior changed.
- [ ] Model code remains reusable and testable under `src/<pkg>/`.

