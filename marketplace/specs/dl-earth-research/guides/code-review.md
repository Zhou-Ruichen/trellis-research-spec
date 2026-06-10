# Guide: Research Code Review

Use this checklist before considering a change complete.

## Correctness

- [ ] The code addresses the real failure or requested behavior.
- [ ] Data assumptions are explicit.
- [ ] Shape, dtype, device, and coordinate conventions are clear where relevant.
- [ ] Errors fail loudly at boundaries instead of producing fake success.

## Reproducibility

- [ ] Config is the source of truth.
- [ ] Retained run outputs include config snapshot, manifest, seed,
      environment freeze, and metrics.
- [ ] Any result claim is backed by an actual file.
- [ ] Data products have manifests and rebuild instructions.

## Anti-Bloat

- [ ] No copied train/eval/data scripts.
- [ ] No `*_v2.py`, `*_final.py`, or backup source directories.
- [ ] New reusable logic is in `src/<pkg>/`.
- [ ] One-off exploration stayed in `notebooks/` or a thin script.
- [ ] Superseded variants were deleted, not left to accumulate; every deletion
      is listed, and no experiment record (`outputs/`, manifests, configs
      referenced by results) was removed without asking.

## Verification

- [ ] Ran the narrowest meaningful command.
- [ ] If no command was run, the reason is stated.
- [ ] Test scope matches the risk of the change.
