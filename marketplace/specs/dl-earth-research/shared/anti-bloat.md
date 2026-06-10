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
- Do not delete old experiments, baselines, ablations, or configs automatically. Report candidates and ask.

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

When you find likely dead code or duplicated old variants:

1. Report the path and why it looks removable or mergeable.
2. Explain whether it may be an experiment record, baseline, or paper artifact.
3. Ask before deleting or collapsing it.

Do not silently remove history from research repositories.

## Completion Report Requirement

When a task adds code, report:

- new files added;
- net new lines if easily available;
- any duplicate or bloat risk noticed;
- why each new durable file is justified.

