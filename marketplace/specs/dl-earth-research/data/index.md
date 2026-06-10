# Data Guidelines

Use these rules whenever reading, writing, validating, or transforming data.

The project may keep data under `data/`. The rule is not "no data in repo"; the
rule is "data must have lifecycle, provenance, and rebuild instructions."

## Documentation Files

| File | Read when |
| --- | --- |
| [../shared/project-layout.md](../shared/project-layout.md) | Naming data paths |
| [../shared/reproducibility.md](../shared/reproducibility.md) | Writing manifests and run records |
| [../shared/anti-bloat.md](../shared/anti-bloat.md) | Adding processing scripts or variants |

## General Data Rules

### Data Layout

```text
data/
  raw/
  external/
  interim/
  processed/
  manifests/
```

Use `data/raw/` for immutable local raw inputs or symlinks. Use `data/external/`
for read-only external data roots or symlink targets. Use `data/interim/` for
temporary but rebuildable products. Use `data/processed/` for model-ready
datasets.

### Data Lake Rule

If a project reads from a shared data lake such as `/mnt/data2/00-Data`, treat
that location as read-only by default.

Project code should write to local `data/interim/`, `data/processed/`, or
`outputs/<run_id>/`. Writing back into a shared data lake requires an explicit
data-processing task and a manifest.

### Manifest Rule

Every durable data product needs a manifest in `data/manifests/`.

Required fields:

```json
{
  "name": "swot_bathymetry_train_v1",
  "created_at": "2026-06-10T14:22:33Z",
  "created_by": "python scripts/build_dataset.py --config configs/data/swot.yaml",
  "source_paths": [],
  "source_versions": {},
  "processing_config": "configs/data/swot.yaml",
  "output_paths": [],
  "checksums": {},
  "spatial_bounds": null,
  "temporal_bounds": null,
  "split_policy": "recorded in data/manifests/splits_v1.json",
  "assumptions": []
}
```

Do not invent unavailable fields. Use `null`, an empty list, or a clear
assumption only when the value is truly unknown.

### Boundary Validation

Validate at the point where data enters the project:

- file exists and format is expected;
- coordinate names and units are known;
- longitude convention is explicit (`[-180, 180]` or `[0, 360]`);
- latitude bounds are valid;
- array shapes match config;
- dtype is expected;
- NaN and fill-value handling is explicit;
- train/validation/test splits cannot leak the same track, tile, region, or time range when leakage matters.

## Geoscience Data Rules

### SWOT And Related Data

For SWOT, altimetry, gravity, and bathymetry workflows:

- Record variable names used from `.nc`, `.npz`, `.mat`, `.tif`, or `.csv` files.
- Record resampling, gridding, interpolation, detrending, filtering, and masking parameters.
- Keep geospatial transforms explicit. Do not silently assume coordinate order.
- Preserve enough metadata to rebuild the processed dataset from source data.
- When matching tracks, tiles, ship data, or gridded products, record the join key and tolerance.

## Data Processing Entrypoints

Use one stable entrypoint per durable processing stage:

```text
scripts/build_dataset.py
scripts/validate_dataset.py
scripts/export_product.py
```

Do not create:

```text
scripts/build_dataset_v2.py
scripts/build_dataset_final.py
scripts/1_make_data.py
scripts/2_fix_data.py
```

If the stage changes, update config and manifest, not the script name.

## Quality Check

- [ ] Durable data output has a manifest.
- [ ] Splits are recorded and leakage-checked for the relevant scientific question.
- [ ] Data paths are config-driven, not hardcoded workstation paths.
- [ ] NaN/fill values, units, and coordinate conventions are explicit.
- [ ] Large generated data is ignored by git unless the user explicitly chooses to version a small fixture.
