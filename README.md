# Trellis Research Spec

Reusable Trellis spec templates for deep-learning research projects.

This repository is not a Python project scaffold. It is a ruleset that Trellis
installs into `.trellis/spec/` so AI coding agents follow the same research
engineering conventions across projects.

The first template, `dl-earth-research`, targets:

- deep-learning training and evaluation;
- SWOT, altimetry, gravity, bathymetry, and related geoscience data workflows;
- reproducible experiment management;
- anti-bloat rules for research code where baselines and ablations must not be
  deleted automatically.

## Use

After this repository is pushed to GitHub:

```sh
trellis init \
  --registry gh:Zhou-Ruichen/trellis-research-spec/marketplace \
  --template dl-earth-research \
  --claude --codex
```

For an existing Trellis project, use `--overwrite` only when replacing a generic
or incorrect spec:

```sh
trellis init \
  --registry gh:Zhou-Ruichen/trellis-research-spec/marketplace \
  --template dl-earth-research \
  --overwrite \
  --claude --codex
```

## Local Validation

Run:

```sh
python3 scripts/validate.py
```

The validator checks:

- Trellis marketplace `index.json` schema;
- template path existence;
- markdown links inside the spec;
- core research requirements;
- ASCII-only paths and contents;
- local `.trellis/spec` installation shape when the `trellis` CLI is installed.

The validator cannot prove remote registry installation until this repository is
published. After publishing, verify with:

```sh
tmpdir="$(mktemp -d)"
cd "$tmpdir"
git init
trellis init \
  --registry gh:Zhou-Ruichen/trellis-research-spec/marketplace \
  --template dl-earth-research \
  --claude --codex -y
find .trellis/spec -type f | sort
```

## What The Template Enforces

- Modern Python layout with importable code under `src/<pkg>/`.
- `configs/` as the single source of truth for experiment knobs.
- `data/` is allowed, but it must be organized by lifecycle and tracked with
  manifests.
- `outputs/<run_id>/` is the source of truth for run artifacts.
- No `train_v2.py`, `*_final.py`, duplicate experiment scripts, or backup
  directories as normal development patterns.
- No automatic deletion of baselines, ablations, or old experiment configs.
  Agents must report cleanup candidates and ask.

## Repository Layout

```text
marketplace/
  index.json
  specs/
    dl-earth-research/
      shared/
      data/
      training/
      evaluation/
      guides/
examples/
  project-layout/
```

The marketplace schema follows Trellis `index.json` requirements: a `templates`
array with entries containing string `id`, `type`, `name`, and `path` fields.
