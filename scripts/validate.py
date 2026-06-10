#!/usr/bin/env python3
"""Validate the local Trellis marketplace structure."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE = ROOT / "marketplace"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_index() -> dict:
    index_path = MARKETPLACE / "index.json"
    if not index_path.exists():
        fail("marketplace/index.json is missing")
    try:
        return json.loads(index_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"marketplace/index.json is invalid JSON: {exc}")


def validate_index() -> None:
    index = load_index()
    templates = index.get("templates")
    if not isinstance(templates, list) or not templates:
        fail("marketplace/index.json must contain a non-empty templates array")

    for template in templates:
        for key in ("id", "type", "name", "path"):
            if not isinstance(template.get(key), str):
                fail(f"template entry must include string {key!r}: {template}")
        if template["type"] != "spec":
            fail(f"unsupported template type {template['type']!r}; expected 'spec'")
        template_path = ROOT / template["path"]
        if not template_path.is_dir():
            fail(f"template path does not exist: {template['path']}")
        if not (template_path / "README.md").is_file():
            fail(f"template path lacks README.md: {template['path']}")


LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+\.md)\)")


def validate_markdown_links() -> None:
    for md_path in (MARKETPLACE / "specs").rglob("*.md"):
        text = md_path.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = match.group(1)
            if "://" in target or target.startswith("#"):
                continue
            resolved = (md_path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                fail(f"{md_path.relative_to(ROOT)} links outside repo: {target}")
            if not resolved.is_file():
                fail(f"{md_path.relative_to(ROOT)} has broken link: {target}")


def validate_required_content() -> None:
    required = {
        "marketplace/specs/dl-earth-research/shared/project-layout.md": [
            "data/raw/",
            "data/interim/",
            "data/processed/",
            "outputs/<run_id>/",
        ],
        "marketplace/specs/dl-earth-research/shared/anti-bloat.md": [
            "Do not delete old experiments",
            "*_v2.py",
            "*_final.py",
        ],
        "marketplace/specs/dl-earth-research/shared/reproducibility.md": [
            "manifest.json",
            "metrics.json",
            "Do not invent",
        ],
        "marketplace/specs/dl-earth-research/data/index.md": [
            "SWOT",
            "Data Lake Rule",
            "Manifest Rule",
        ],
        "marketplace/specs/dl-earth-research/training/index.md": [
            "PyTorch",
            "Lightning",
            "smoke",
        ],
    }
    for rel_path, needles in required.items():
        text = (ROOT / rel_path).read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                fail(f"{rel_path} missing required text: {needle}")


def validate_no_non_ascii() -> None:
    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        rel_path = path.relative_to(ROOT)
        try:
            str(rel_path).encode("ascii")
        except UnicodeEncodeError:
            fail(f"path must be ASCII: {rel_path}")
        if path.is_file():
            data = path.read_bytes()
            try:
                data.decode("ascii")
            except UnicodeDecodeError:
                fail(f"file content must be ASCII: {rel_path}")


def validate_trellis_spec_shape() -> None:
    trellis = shutil.which("trellis")
    if trellis is None:
        print("WARN: trellis not found; skipped install-shape validation", file=sys.stderr)
        return

    template_path = ROOT / "marketplace/specs/dl-earth-research"
    with tempfile.TemporaryDirectory(prefix="trellis-research-spec-") as tmp:
        tmp_path = Path(tmp)
        subprocess.run(
            ["git", "init"],
            cwd=tmp_path,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        subprocess.run(
            [trellis, "init", "--claude", "--codex", "-y"],
            cwd=tmp_path,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        spec_path = tmp_path / ".trellis/spec"
        if spec_path.exists():
            shutil.rmtree(spec_path)
        shutil.copytree(template_path, spec_path)

        expected = [
            "README.md",
            "shared/index.md",
            "shared/project-layout.md",
            "shared/anti-bloat.md",
            "shared/reproducibility.md",
            "shared/python-style.md",
            "data/index.md",
            "training/index.md",
            "evaluation/index.md",
            "guides/add-experiment.md",
            "guides/debug-nan-oom.md",
            "guides/code-review.md",
        ]
        for rel_path in expected:
            if not (spec_path / rel_path).is_file():
                fail(f"Trellis spec-shape validation missing .trellis/spec/{rel_path}")


def main() -> None:
    validate_index()
    validate_markdown_links()
    validate_required_content()
    validate_no_non_ascii()
    validate_trellis_spec_shape()
    print("trellis-research-spec validation passed")


if __name__ == "__main__":
    main()
