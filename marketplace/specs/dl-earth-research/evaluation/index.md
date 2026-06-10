# Evaluation Guidelines

Use these rules for validation, test evaluation, prediction export, diagnostics,
figures, and report artifacts.

## Evaluation Layout

```text
src/<pkg>/eval/
  metrics.py
  predict.py
  plots.py
  diagnostics.py
scripts/
  evaluate.py
  predict.py
```

Scripts remain thin. Metrics, prediction writing, diagnostics, and plotting
logic live under `src/<pkg>/eval/`.

## Metrics

Retained evaluation runs write:

```text
outputs/<run_id>/metrics.json
```

Recommended schema:

```json
{
  "run_id": "20260610-142233-unet-swot",
  "split": "test",
  "metrics": {
    "rmse": 123.456,
    "mae": 98.765
  },
  "n_samples": 100,
  "data_manifest": "data/manifests/swot_test_v1.json",
  "checkpoint": "outputs/20260610-142233-unet-swot/checkpoints/epoch=012.ckpt",
  "notes": []
}
```

Scratch and smoke evaluation runs may write lighter logs or metrics while
debugging. Promote the run and write the retained metrics file before citing it
in a comparison, report, or result claim.

Do not report retained metrics only in stdout, screenshots, notebooks, or
remote logging dashboards.

## Figures

For retained generated figures tied to a run, use:

```text
outputs/<run_id>/figures/
```

Scratch figures may live under `outputs/scratch/<run_id>/figures/` and may be
deleted unless promoted.

Use:

```text
reports/
```

only for curated figures and tables intended for papers, presentations, or
human-facing reports.

## Prediction Products

For retained runs, write model predictions under:

```text
outputs/<run_id>/predictions/
```

Retained prediction products must record:

- checkpoint path;
- input data manifest;
- prediction format;
- coordinate convention and grid definition when geospatial;
- postprocessing steps.

## Diagnostic Code

One parameterized diagnostic entrypoint is better than many copied scripts.

Good:

```text
scripts/diagnose_run.py
src/<pkg>/eval/diagnostics.py
```

Bad:

```text
scripts/diagnose_run_v2.py
scripts/diagnose_bad_tile_final.py
scripts/evaluate_old_checkpoint.py
```

## Quality Check

- [ ] Retained metrics are written to JSON with split and sample count.
- [ ] Retained figures and predictions are tied to a run ID.
- [ ] Geospatial outputs record coordinate convention, grid definition, and postprocessing.
- [ ] Reports contain curated artifacts, not raw output dumps.
- [ ] New evaluation behavior did not create copied script variants.
