# Guide: Debug NaN, Inf, Divergence, Or OOM

Use a narrow diagnosis before changing model architecture or adding fallback
logic.

## NaN Or Inf

Check in this order:

1. Input data finite values at dataset boundary.
2. Target data finite values and expected range.
3. Normalization mean/std, especially zero or tiny std.
4. Loss inputs and masks.
5. Learning rate and precision.
6. Gradient norm before clipping.
7. First batch forward pass with anomaly detection if needed.

Do not add broad `nan_to_num` or silent loss skipping unless the data policy
explicitly requires it and the behavior is recorded in config.

## OOM

Check in this order:

1. Batch size.
2. Input tile/grid size.
3. Precision setting.
4. Gradient accumulation.
5. Number of workers and prefetching.
6. Model activation memory.
7. Evaluation or prediction retaining tensors on device.

Prefer a smaller smoke config before changing core code.

## Required Debug Output

When adding debug instrumentation, keep it local and removable:

- shape;
- dtype;
- finite-value counts;
- min/max or robust percentiles;
- device;
- batch keys.

If debug code becomes generally useful, move it to `src/<pkg>/eval/diagnostics.py`
and expose it through one script.

