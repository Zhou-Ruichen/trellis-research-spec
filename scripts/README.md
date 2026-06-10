# Scripts

`validate.py` checks the local marketplace structure:

- `marketplace/index.json` has the fields Trellis expects;
- template paths exist;
- markdown links inside the spec resolve;
- core research requirements are still present.

Run:

```sh
python3 scripts/validate.py
```

