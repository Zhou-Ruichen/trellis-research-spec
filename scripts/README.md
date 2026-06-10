# Scripts

`validate.py` checks the local marketplace structure:

- `marketplace/index.json` has the fields Trellis expects;
- template paths exist;
- markdown links inside the spec resolve;
- core research requirements are still present.
- paths and file contents are ASCII;
- when Trellis is installed, the template can be copied into `.trellis/spec/`
  after `trellis init`.

Run:

```sh
python3 scripts/validate.py
```

The script does not perform a remote `gh:` registry download. That requires the
repository to be published to GitHub first.
