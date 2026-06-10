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

Every evaluation run writes:

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

Do not report metrics only in stdout, screenshots, notebooks, or remote logging
dashboards.

## Figures

Use:

```text
outputs/<run_id>/figures/
```

for generated figures tied to a run.

Use:

```text
reports/
```

only for curated figures and tables intended for papers, presentations, or
human-facing reports.

## Prediction Products

Write model predictions under:

```text
outputs/<run_id>/predictions/
```

Prediction products must record:

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

- [ ] Metrics are written to JSON with split and sample count.
- [ ] Figures and predictions are tied to a run ID.
- [ ] Geospatial outputs record coordinate convention, grid definition, and postprocessing.
- [ ] Reports contain curated artifacts, not raw output dumps.
- [ ] New evaluation behavior did not create copied script variants.

