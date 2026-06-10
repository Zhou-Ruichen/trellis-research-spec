# Reproducibility

Every claimed result must be traceable to inputs, code, config, environment,
and outputs.

## Run Manifest

Each training, evaluation, prediction, or data-processing run must write:

```text
outputs/<run_id>/manifest.json
```

or, for data processing that produces data products:

```text
data/manifests/<product>.json
```

## Required Manifest Fields

```json
{
  "run_id": "20260610-142233-unet-swot",
  "created_at": "2026-06-10T14:22:33Z",
  "command": "python scripts/train.py --config configs/exp/unet_swot.yaml",
  "git": {
    "commit": "unknown",
    "dirty": true
  },
  "config_path": "configs/exp/unet_swot.yaml",
  "config_snapshot": "outputs/20260610-142233-unet-swot/config.yaml",
  "seed": 42,
  "environment": {
    "python": "3.12",
    "torch": "unknown",
    "cuda": "unknown"
  },
  "data": {
    "manifest": "data/manifests/swot_train_v1.json",
    "splits": "data/manifests/splits_v1.json"
  },
  "outputs": {
    "metrics": "outputs/20260610-142233-unet-swot/metrics.json"
  },
  "assumptions": []
}
```

Use real values when available. Do not invent commit hashes, metrics, seeds, or
environment versions.

## Environment

Each project declares one environment strategy in its own spec or README
(for example: per-project locked env, or a named shared env on a GPU server).
This template does not pick the manager; it requires the contract:

- Every run manifest records the environment it ran in, plus a freeze
  snapshot written next to the run artifacts:

```json
"environment": {
  "manager": "<uv|conda|venv|...>",
  "name": "<env-name>",
  "python": "<version>",
  "torch": "<version>",
  "cuda": "<version-or-null>",
  "freeze": "outputs/<run_id>/requirements.freeze.txt"
}
```

- Shared environments drift; the freeze snapshot is what preserves the run.
- Do not install packages ad hoc into `base` or another project's environment.
  Add new dependencies to this project's dependency file first, then install.

> Fill in after init: this project's environment strategy, env name(s), and
> Python version.

## Seed Rule

Use one project helper for seed setup. It should cover:

- Python `random`;
- NumPy;
- PyTorch CPU;
- PyTorch CUDA when available;
- data-loader worker seeds when applicable.

Deterministic algorithms are useful for debugging but can be slower or unsupported.
Expose them as a config option instead of hardcoding them globally.

## Result Claims

Do not say a model improved, converged, or reproduced a number unless:

- metrics exist in `outputs/<run_id>/metrics.json`;
- the evaluated split is recorded;
- the config and seed are recorded;
- the data manifest or source snapshot is recorded.

If only a smoke test ran, say it was a smoke test.

## Logging Backends

Weights & Biases, SwanLab, TensorBoard, CSV, and console logs are mirrors. The
project-local `outputs/<run_id>/` directory remains the source of truth.

