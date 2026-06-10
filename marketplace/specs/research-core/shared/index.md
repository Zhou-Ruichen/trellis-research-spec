# Shared Research Core Guidelines

Applies to every task in this repository. Optimize for reproducibility,
iteration speed, readable code, and evidence-backed claims.

## Documentation Files

| File | Read when |
| --- | --- |
| [project-layout.md](./project-layout.md) | Creating, moving, or naming files |
| [anti-bloat.md](./anti-bloat.md) | Adding files, variants, scripts, helpers, or abstractions |
| [reproducibility.md](./reproducibility.md) | Running computations or reporting results |
| [../data/index.md](../data/index.md) | Reading, writing, processing, or validating data |
| [../evaluation/index.md](../evaluation/index.md) | Writing metrics, figures, reports, or comparisons |
| [../guides/index.md](../guides/index.md) | Choosing a task guide |

## Quick Navigation By Task

| Task | Read |
| --- | --- |
| Add a script, notebook, or helper | [anti-bloat.md](./anti-bloat.md) and [project-layout.md](./project-layout.md) |
| Run an experiment, simulation, or analysis | [reproducibility.md](./reproducibility.md) |
| Create or transform data | [../data/index.md](../data/index.md) |
| Report a metric, figure, or comparison | [../evaluation/index.md](../evaluation/index.md) |
| Review a change | [../guides/code-review.md](../guides/code-review.md) |

## Pre-Development Checklist

- [ ] Can this be expressed as a config, parameter, or documented command
      instead of copied code?
- [ ] Is there an existing loader, transform, analysis routine, metric, or
      helper to reuse?
- [ ] Is this exploratory? Keep it in `notebooks/`, scratch output, or a thin
      script.
- [ ] Is this durable? Put reusable logic in the project's existing source
      location.
- [ ] Touching data? Check provenance, schema, split/leakage risk, and manifest
      rules.
- [ ] Touching results? Decide whether each run is scratch, smoke, or retained.

## Core Rules

- Respect the repository's current documented layout. Do not rename a mature
  project into this template shape without a migration task.
- Keep configs, parameters, and commands as explicit sources of truth.
- Use `outputs/<run_id>/` for retained run artifacts.
- Scratch and smoke runs stay lightweight and disposable unless promoted.
- Keep curated human-facing reports separate from raw run outputs.
- Delete code the current task superseded after verification. Ask before
  deleting experiment records, retained outputs, data manifests, or untracked
  files.
- Do not productionize one-off exploration with factories, plugin systems,
  config classes, or broad abstraction layers.

## Quality Check

- [ ] The change follows the repository's documented layout.
- [ ] No duplicate `*_v2`, `*_final`, copied experiment script, or backup
      directory was introduced.
- [ ] Reusable logic lives in the existing source area, not only in notebooks
      or ad hoc scripts.
- [ ] Any result claim is backed by retained evidence with config, command,
      data record, environment, metrics, and assumptions.
- [ ] Any data-writing task records what was written, where it came from, and
      how to rebuild it.
