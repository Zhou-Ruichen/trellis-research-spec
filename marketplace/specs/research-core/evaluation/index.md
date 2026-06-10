# Evaluation Guidelines

Use these rules for validation, metrics, comparisons, figures, tables,
diagnostics, and report artifacts.

## Evaluation Layout

Keep scripts thin and move reusable evaluation logic to the project's source
area.

Typical structure:

```text
src/ or lib/
  metrics.*
  evaluation.*
  plots.*
scripts/
  evaluate.*
  make_figures.*
```

Existing projects may use different names. Follow their documented ownership
boundaries.

## Metrics

Retained evaluation runs write:

```text
outputs/<run_id>/metrics.json
```

Recommended schema:

```json
{
  "run_id": "20260610-142233-sensitivity",
  "split": "test",
  "metrics": {
    "rmse": 123.456,
    "mae": 98.765
  },
  "n_samples": 100,
  "data_manifest": "data/manifests/test_v1.json",
  "parameters": "outputs/20260610-142233-sensitivity/config.yaml",
  "notes": []
}
```

Scratch and smoke evaluation runs may write lighter logs or metrics while
debugging. Promote the run and write retained metrics before citing it in a
comparison, report, or result claim.

Do not report retained metrics only in stdout, screenshots, notebooks, or
remote logging dashboards.

## Figures And Tables

For retained generated figures and tables tied to a run, use:

```text
outputs/<run_id>/figures/
outputs/<run_id>/tables/
```

Use:

```text
reports/
```

only for curated figures, tables, and summaries intended for papers,
presentations, or human-facing review.

Reports must point back to the retained run, manifest, or data product that
created each result.

## Comparisons

Comparison tables must record:

- compared run IDs or data manifests;
- metric definitions;
- sample set, split, condition, or grouping;
- parameter differences that matter;
- assumptions and exclusions.

Do not compare numbers copied from dashboards, notebooks, or screenshots unless
the underlying retained artifacts are available.

## Diagnostic Code

One parameterized diagnostic entrypoint is better than many copied scripts.

Good:

```text
scripts/diagnose_run.py
src/project/diagnostics.py
```

Bad:

```text
scripts/diagnose_run_v2.py
scripts/evaluate_bad_case_final.py
scripts/check_new_results.py
```

## Quality Check

- [ ] Retained metrics are written to JSON with sample set or split.
- [ ] Retained figures and tables are tied to a run ID or data manifest.
- [ ] Comparison tables record what was compared and how.
- [ ] Reports contain curated artifacts, not raw output dumps.
- [ ] New evaluation behavior did not create copied script variants.
