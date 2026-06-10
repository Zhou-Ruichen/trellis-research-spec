# Trellis Research Spec

Reusable Trellis spec templates for research projects.

This repository is not a Python project scaffold. It is a ruleset that Trellis
installs into `.trellis/spec/` so AI coding agents follow the same research
engineering conventions across projects.

The templates currently cover:

- `research-core`: language-agnostic research rules for non-DL analysis,
  simulations, traditional ML, data processing, evaluation, and reproducible
  result claims.
- `dl-earth-research`: deep-learning geoscience research with PyTorch-oriented
  training, evaluation, checkpoint, data, and anti-bloat conventions.

`dl-earth-research` targets:

- deep-learning training and evaluation;
- SWOT, altimetry, gravity, bathymetry, and related geoscience data workflows;
- reproducible experiment management;
- anti-bloat rules for research code: superseded variants are deleted (git
  history is the archive), while run artifacts and experiment records are
  protected.

## Scope

- `research-core` is language-agnostic and layout-tolerant. It is the default
  choice for non-DL computational research.
- `dl-earth-research` is Python-first, not Python-only. The layout and style bindings
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

## Template Selection

| Template | Use when | Avoid when |
| --- | --- | --- |
| `research-core` | Non-DL research, simulation, traditional ML, data analysis, reproducible pipelines, existing projects that need research discipline | The project needs DL-specific training/checkpoint/ablation rules |
| `dl-earth-research` | Geoscience projects with deep-learning training, PyTorch evaluation, checkpoints, ablations, or geospatial data workflows | The project is non-DL and only needs generic research reproducibility |

Use the tagged registry for repeatable installs.

For non-DL research:

```sh
trellis init \
  --registry gh:Zhou-Ruichen/trellis-research-spec/marketplace#v0.2.0 \
  --template research-core \
  --claude --codex
```

For deep-learning geoscience research:

```sh
trellis init \
  --registry gh:Zhou-Ruichen/trellis-research-spec/marketplace#v0.2.0 \
  --template dl-earth-research \
  --claude --codex
```

Use the unpinned `main` registry only when you intentionally want the latest
template changes:

```sh
trellis init \
  --registry gh:Zhou-Ruichen/trellis-research-spec/marketplace \
  --template research-core \
  --claude --codex
```

For an existing Trellis project, use `--overwrite` only when replacing a generic
or incorrect spec:

```sh
trellis init \
  --registry gh:Zhou-Ruichen/trellis-research-spec/marketplace#v0.2.0 \
  --template research-core \
  --overwrite \
  --claude --codex
```

## Adopting Into An Existing Project

`--overwrite` replaces the whole `.trellis/spec/` directory. If the project
already has a customized spec (project-specific directory structure, data
contracts, captured learnings), do not overwrite it. Instead:

- Prefer `research-core` for generic adoption.
- Copy only the layout-independent guides (`shared/anti-bloat.md` and
  `shared/reproducibility.md`) into the existing spec layer if full template
  installation would conflict with project-specific structure.
- Keep the project's own documented layout. An established repo's
  `directory-structure.md` or equivalent wins.
- Prepend a short note in copied files mapping template paths to the repo's
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
  --registry gh:Zhou-Ruichen/trellis-research-spec/marketplace#v0.2.0 \
  --template research-core \
  --claude --codex -y
find .trellis/spec -type f | sort
```

## What The Templates Enforce

- `research-core` preserves existing project layout while enforcing retained
  evidence for result claims.
- `dl-earth-research` recommends modern Python layout with importable code
  under `src/<pkg>/`.
- Configs, parameters, or retained commands are the source of truth for run
  knobs.
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
    research-core/
      shared/
      data/
      evaluation/
      guides/
examples/
  project-layout/
```

The marketplace schema follows Trellis `index.json` requirements: a `templates`
array with entries containing string `id`, `type`, `name`, and `path` fields.
