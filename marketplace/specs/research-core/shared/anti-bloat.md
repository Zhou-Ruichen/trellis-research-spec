# Anti-Bloat Rules

Research repositories grow by copying experiments, leaving old variants in
place, and turning one-off analysis into framework code. Prevent bloat by not
adding it.

## Rules

- Search before adding a new file or helper.
- Reuse existing loaders, transforms, metrics, plotting helpers, and analysis
  routines.
- Extract common code when two durable scripts share meaningful logic.
- Do not create `*_v2`, `*_final`, `*_new`, or date-suffixed source variants.
- Do not add a factory, registry, base class, plugin system, or config class
  for a one-off script.
- Do not hide unknown behavior with broad fallback branches, swallowed
  exceptions, or fake success logs.
- Delete superseded code instead of accumulating variants. Git history is the
  archive; follow the cleanup protocol below for what needs asking first.

## Variants

Bad:

```text
scripts/analyze.py
scripts/analyze_v2.py
scripts/analyze_final.py
scripts/simulation_new.py
```

Good:

```text
scripts/analyze.py
configs/sensitivity.yaml
configs/baseline.yaml
configs/ablation_without_filter.yaml
```

If a language or project does not use config files, record the parameterized
command in the retained run manifest instead of copying the script.

## Diagnostic Scripts

A small diagnostic script is fine while debugging. If it becomes repeated or
durable, either parameterize one entrypoint or move reusable logic to the
project's source area.

Bad:

```text
scripts/check_data.py
scripts/check_data_v2.py
scripts/debug_bad_case_final.R
```

Good:

```text
scripts/diagnose_run.py
src/project/diagnostics.py
```

## Cleanup Protocol

Git history is the safety net: anything committed is recoverable, so deleting
superseded work in the working tree is the default way to prevent bloat.

Delete directly, then list every deletion in the completion report:

- dead code and unused helpers;
- superseded script or config variants;
- rebuildable intermediates (`data/interim/`, `outputs/scratch/`, stale smoke
  outputs);
- debug instrumentation that served its purpose.

Ask first only when deletion is irreversible or breaks the experiment record:

- retained run artifacts under `outputs/` that back reported results;
- `data/manifests/` entries;
- baseline, ablation, or comparison configs still referenced by reports,
  papers, notebooks, or tables;
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
