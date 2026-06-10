# Trellis Research Spec

Reusable Trellis spec templates for deep-learning research projects.

This repository is not a Python project scaffold. It is a ruleset that Trellis
installs into `.trellis/spec/` so AI coding agents follow the same research
engineering conventions across projects.

The first template, `dl-earth-research`, targets:

- deep-learning training and evaluation;
- SWOT, altimetry, gravity, bathymetry, and related geoscience data workflows;
- reproducible experiment management;
- anti-bloat rules for research code: superseded variants are deleted (git
  history is the archive), while run artifacts and experiment records are
  protected.

## Scope

- Python-first, not Python-only. The layout and style bindings
  (`src/<pkg>/`, `pyproject.toml`, `python-style.md`) target Python/PyTorch,
  which is the expected main language. The core contracts -- anti-bloat,
  reproducibility, run manifests, data manifests, environment recording -- are
  language-agnostic and apply to any code in the repo.
- Mixed-language work (CUDA/C++ extensions, Fortran kernels, Julia or Rust
  tooling, shell scripts) follows the same contracts; add a per-language style
  file in the project's own spec when that language carries durable code.
- Designed for new projects. Existing projects with a customized spec should
  follow the adoption section below instead of `--overwrite`.
- Covers code structure, experiment management, data handling, and anti-bloat.
  CI/CD, deployment, and monitoring are intentionally out of scope; add them as
  separate spec layers if a project needs them.

## Use

Use the tagged registry for repeatable installs:

```sh
trellis init \
  --registry gh:Zhou-Ruichen/trellis-research-spec/marketplace#v0.1.0 \
  --template dl-earth-research \
  --claude --codex
```

Use the unpinned `main` registry only when you intentionally want the latest
template changes:

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
  --registry gh:Zhou-Ruichen/trellis-research-spec/marketplace#v0.1.0 \
  --template dl-earth-research \
  --overwrite \
  --claude --codex
```

## Adopting Into An Existing Project

`--overwrite` replaces the whole `.trellis/spec/` directory. If the project
already has a customized spec (project-specific directory structure, data
contracts, captured learnings), do not overwrite it. Instead:

- Copy only the layout-independent guides (`shared/anti-bloat.md` and
  `shared/reproducibility.md`) into the existing spec layer and add them to
  its guidelines index.
- Keep the project's own documented layout: `src/<pkg>/` in this template is
  for new projects; an established repo's `directory-structure.md` wins.
- Prepend a short note in the copied files mapping `src/<pkg>/` to the repo's
  actual module layout.

Reserve `--overwrite` for specs that are still untouched Trellis defaults.

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
  --registry gh:Zhou-Ruichen/trellis-research-spec/marketplace#v0.1.0 \
  --template dl-earth-research \
  --claude --codex -y
find .trellis/spec -type f | sort
```

## What The Template Enforces

- Modern Python layout with importable code under `src/<pkg>/`.
- `configs/` as the single source of truth for experiment knobs.
- `data/` is allowed, but it must be organized by lifecycle and tracked with
  manifests.
- `outputs/<run_id>/` is the source of truth for retained run artifacts;
  scratch and smoke runs stay lightweight and disposable unless promoted.
- No `train_v2.py`, `*_final.py`, duplicate experiment scripts, or backup
  directories as normal development patterns.
- Superseded code variants are deleted by the task that replaces them rather
  than accumulated; git history is the archive. Suspected-dead code, bulk
  cleanup, and run artifacts (`outputs/`, `data/manifests/`, configs still
  referenced by results) require asking first.

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
