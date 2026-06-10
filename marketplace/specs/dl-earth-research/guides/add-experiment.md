# Guide: Add An Experiment

Follow this when adding a new model, data setting, ablation, or training run.

## Steps

1. Search existing configs under `configs/`.
2. Create or edit a config override under `configs/exp/`.
3. Reuse the existing training entrypoint.
4. Add or update small tests only if the experiment requires new reusable code.
5. Run the narrowest smoke check that proves the config loads and one step works.
6. Record the expected command in the task response or project notes.

## Do

```text
configs/exp/unet_swot_gravity.yaml
scripts/train.py --config configs/exp/unet_swot_gravity.yaml
```

## Do Not

```text
scripts/train_unet_swot_gravity.py
scripts/train_unet_swot_gravity_final.py
src/<pkg>/training/trainer_v2.py
```

## Required Config Fields

At minimum, an experiment config should resolve:

- seed;
- data manifest path;
- model name and parameters;
- optimizer and scheduler;
- training duration;
- output root or run name;
- logging backend if used.

## Completion Checklist

- [ ] The experiment is represented as config.
- [ ] New code was added only when config could not express the change.
- [ ] The run command is clear.
- [ ] Smoke validation was run or the reason it was not run is stated.

