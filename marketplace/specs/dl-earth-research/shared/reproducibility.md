# Reproducibility

Every claimed result must be traceable to inputs, code, config, environment,
and outputs.

## Run Retention Tiers

Use the lightest tier that preserves the scientific record:

- Scratch: debugging, failed runs, quick hyperparameter probes, and daily
  iteration. Put these in `outputs/scratch/<run_id>/`, a temporary directory,
  or another clearly disposable location. They may be deleted when no longer
  useful. No full manifest or freeze file is required unless the run is
  promoted.
- Smoke: tiny checks that prove the pipeline executes. Record enough command,
  config, metric, or log evidence to debug a failure. No full manifest or
  freeze file is required unless the smoke result is cited or promoted.
- Retained: any run used in a comparison, report, paper, model handoff,
  regression baseline, or result claim. Retained runs must have the full
  manifest, config snapshot, metrics, data manifest/source snapshot, seed, and
  environment freeze.

Promote a scratch or smoke run before citing it: move or copy the selected
artifacts into `outputs/<run_id>/`, add the missing retained-run evidence, and
mark why it is retained.

## Run Manifest

Each retained training, evaluation, prediction, or data-processing run must
write:

```text
outputs/<run_id>/manifest.json
```

or, for data processing that produces data products:

```text
data/manifests/<product>.json
```

Scratch and smoke runs may write lighter records, but they must be promoted to
retained runs before they support a result claim.

## Required Manifest Fields

```json
{
  "run_id": "20260610-142233-unet-swot",
  "created_at": "2026-06-10T14:22:33Z",
  "command": "python scripts/train.py --config configs/exp/unet_swot.yaml",
  "retention": "retained",
  "retention_reason": "comparison table for report",
  "git": {
    "commit": "unknown",
    "dirty": true
  },
  "config_path": "configs/exp/unet_swot.yaml",
  "config_snapshot": "outputs/20260610-142233-unet-swot/config.yaml",
  "seed": 42,
  "environment": {
    "manager": "<uv|conda|venv|...>",
    "name": "<env-name-or-null>",
    "python": "<version>",
    "torch": "<version-or-null>",
    "cuda": "<version-or-null>",
    "freeze": "outputs/20260610-142233-unet-swot/environment.freeze.txt"
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

This is a field template, not a concrete environment recommendation. Actual
run manifests must replace placeholders with real values. Do not invent commit
hashes, metrics, seeds, or environment versions.

## Environment

Each project declares one environment strategy in its own spec or README
(for example: per-project locked env, or a named shared env on a GPU server).
This template does not pick the manager; it requires the contract:

- Every retained run manifest records the environment it ran in, plus a freeze
  snapshot written next to the run artifacts. `freeze` is a path to the
  captured dependency/environment snapshot for this run, not a template-level
  fixed file:

```json
"environment": {
  "manager": "<uv|conda|venv|...>",
  "name": "<env-name>",
  "python": "<version>",
  "torch": "<version>",
  "cuda": "<version-or-null>",
  "freeze": "outputs/<run_id>/environment.freeze.txt"
}
```

- Do not create a freeze file for every scratch run in a sweep. If a scratch or
  smoke run becomes evidence, promote it and capture or copy the environment
  freeze then.
- Shared environments drift; for retained runs, the freeze snapshot is what
  preserves the run.
- For Python, the freeze file can be produced by the selected manager (`pip
  freeze`, `uv pip freeze`, `conda env export`, or equivalent). For
  mixed-language work, point to the equivalent lockfile or environment export
  that makes the run reconstructable.
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

Do not say a model improved, converged, or reproduced a number unless the
supporting run was promoted to retained and:

- metrics exist in `outputs/<run_id>/metrics.json`;
- the evaluated split is recorded;
- the config and seed are recorded;
- the data manifest or source snapshot is recorded;
- the environment freeze is recorded.

If only a smoke test ran, say it was a smoke test.

## Logging Backends

Weights & Biases, SwanLab, TensorBoard, CSV, and console logs are mirrors. The
project-local retained run directory `outputs/<run_id>/` remains the source of
truth.
