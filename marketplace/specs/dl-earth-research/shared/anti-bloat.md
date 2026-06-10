# Anti-Bloat Rules

Research code grows by copying experiments, adding wrappers for one-off work,
and leaving output conventions ambiguous. Prevent bloat by not adding it.

## Rules

- Search before adding a new file or helper.
- Reuse existing loaders, transforms, metrics, plotting helpers, and model blocks.
- Extract common code when two durable scripts share meaningful logic.
- Do not create `*_v2.py`, `*_final.py`, `*_new.py`, or date-suffixed variants.
- Do not add a factory, registry, base class, plugin system, or config class for a one-off script.
- Do not hide unknown behavior with broad fallback branches, swallowed exceptions, or fake success logs.
- Delete superseded code instead of accumulating variants. Git history is the
  archive; follow the cleanup protocol below for what needs asking first.

## Experiment Variants

Bad:

```text
scripts/train.py
scripts/train_v2.py
scripts/train_transformer.py
scripts/train_transformer_final.py
```

Good:

```text
scripts/train.py
configs/exp/unet.yaml
configs/exp/transformer_unet.yaml
configs/exp/transformer_unet_ablation_no_gravity.yaml
```

## Diagnostic Scripts

A small diagnostic script is fine while debugging. If it becomes repeated or
durable, either parameterize one entrypoint or move reusable logic to `src/`.

Bad:

```text
scripts/diagnose_nan.py
scripts/diagnose_nan_v2.py
scripts/diagnose_shapes.py
scripts/diagnose_shapes_final.py
```

Good:

```text
scripts/diagnose_run.py
src/<pkg>/eval/diagnostics.py
```

## Cleanup Protocol

Git history is the safety net: anything committed is recoverable, so deleting
superseded work in the working tree is the default way to prevent bloat.

Delete directly, then list every deletion in the completion report:

- dead code and unused helpers;
- superseded script or config variants (`*_v2.py`, copied experiment scripts);
- rebuildable intermediates (`data/interim/`, `outputs/scratch/`, stale
  smoke-run outputs);
- debug instrumentation that served its purpose.

Ask first only when deletion is irreversible or breaks the experiment record:

- run artifacts under `outputs/` that back reported results;
- `data/manifests/` entries;
- baseline or ablation configs still referenced by reports, papers, or
  comparison tables;
- anything not tracked by git.

Deletion stays scoped to the task:

- Delete only what the current task superseded or replaced, and only after the
  replacement is verified to work.
- "Probably dead" is not "superseded". If nothing in this task replaced it and
  you only suspect it is unused, report it instead of deleting it.
- Repo-wide sweeps and whole-directory removals are a separate cleanup task:
  propose the file list first and wait for confirmation.

When unsure which side something falls on, treat it as experiment record and
ask. Never delete silently: a deletion that does not appear in the completion
report is a bug.

## Completion Report Requirement

When a task adds code, report:

- new files added;
- files deleted and why;
- net new lines if easily available;
- any duplicate or bloat risk noticed;
- why each new durable file is justified.
