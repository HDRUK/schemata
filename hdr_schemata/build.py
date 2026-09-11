from __future__ import annotations

import argparse
import importlib
import inspect
import json
import subprocess
import sys
from pathlib import Path

from pydantic import BaseModel

REPO_ROOT = Path(__file__).parent.parent
MODELS_DIR = Path(__file__).parent / "models"
DOCS_DIR = REPO_ROOT / "docs"
AVAILABLE_JSON = REPO_ROOT / "available.json"
MKDOCS_YML = REPO_ROOT / "mkdocs.yml"

SCHEMAORG_VERSIONS = ["BioSchema", "default", "GoogleRecommended"]


def _version_str(version_dir_name: str) -> str:
    return version_dir_name[1:].replace("_", ".")


def _version_sort_key(version_str: str) -> tuple:
    try:
        return tuple(int(x) for x in version_str.split("."))
    except ValueError:
        return (0,)


def _write_schema(cls: type[BaseModel], output_path: Path) -> None:
    with open(output_path, "w") as f:
        json.dump(cls.model_json_schema(), f, indent=6)


def _registered_versions(family: str) -> dict:
    family_module = importlib.import_module(f"hdr_schemata.models.{family}")

    seen = {}
    for _, cls in inspect.getmembers(family_module, inspect.isclass):
        if not (isinstance(cls, type) and issubclass(cls, BaseModel)):
            continue
        mod = cls.__module__
        if not mod.startswith(f"hdr_schemata.models.{family}.v"):
            continue
        version_dir = mod.split(".")[-1]
        if version_dir not in seen:
            seen[version_dir] = cls

    return seen


def _build_family(family_dir: Path) -> list:
    family = family_dir.name
    seen = _registered_versions(family)

    versions = []
    for version_dir in sorted(seen, key=lambda d: _version_sort_key(_version_str(d))):
        version_str = _version_str(version_dir)
        output_dir = family_dir / version_str
        output_dir.mkdir(exist_ok=True)
        _write_schema(seen[version_dir], output_dir / "schema.json")
        print(f"  {family}/{version_str}")
        versions.append(version_str)

    return versions


def _build_schemaorg(family_dir: Path) -> list:
    script = family_dir / "create_schemas.py"
    if script.exists():
        subprocess.run([sys.executable, str(script)], cwd=str(family_dir), check=True)
    return SCHEMAORG_VERSIONS


def generate() -> None:
    available = {}

    for family_dir in sorted(MODELS_DIR.iterdir()):
        if not family_dir.is_dir() or family_dir.name.startswith("_"):
            continue
        family = family_dir.name

        if family == "SchemaOrg":
            print("SchemaOrg (named variants)")
            available[family] = _build_schemaorg(family_dir)
        else:
            versions = _build_family(family_dir)
            if versions:
                available[family] = versions

    with open(AVAILABLE_JSON, "w") as f:
        json.dump(available, f, indent=2)
        f.write("\n")

    total = sum(len(v) for v in available.values())
    print(f"\navailable.json written ({total} schemas across {len(available)} families)")

    print("\nGenerating docs...")
    from hdr_schemata.utils.create_markdown import build_docs

    build_docs()


def _generated_paths() -> list:
    paths = [AVAILABLE_JSON, MKDOCS_YML]
    paths.extend(MODELS_DIR.glob("*/*/schema.json"))
    for pattern in ("*/*.md", "*/*.form.json", "*/*.structure.json"):
        paths.extend(DOCS_DIR.glob(pattern))
    return sorted(set(paths))


def _snapshot() -> dict:
    return {path: path.read_bytes() for path in _generated_paths() if path.is_file()}


def _restore(snapshot: dict) -> None:
    for path in _generated_paths():
        if path not in snapshot and path.is_file():
            path.unlink()
    for path, content in snapshot.items():
        if not path.is_file() or path.read_bytes() != content:
            path.write_bytes(content)


def check() -> int:
    before = _snapshot()
    try:
        generate()
        after = _snapshot()

        changed = sorted(
            {path for path in set(before) | set(after) if before.get(path) != after.get(path)}
        )
    finally:
        _restore(before)

    if not changed:
        print("\nUp to date: schemas, available.json, docs and mkdocs.yml all match the models.")
        return 0

    print(f"\nERROR: {len(changed)} generated file(s) are out of date:\n")
    for path in changed:
        print(f"  {path.relative_to(REPO_ROOT)}")
    print(
        "\nRun 'python -m hdr_schemata.build' locally and commit the result.\n"
        "This regenerates every schema.json, available.json, the docs under docs/ "
        "and the mkdocs.yml nav.\n"
        "Requires Python 3.11 with pydantic==2.4.2 — other versions produce different output."
    )
    return 1


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m hdr_schemata.build",
        description="Generate every schema.json, available.json and the documentation.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify the committed output matches the models without changing any files",
    )
    args = parser.parse_args(argv)

    if args.check:
        return check()

    generate()
    return 0


if __name__ == "__main__":
    sys.exit(main())
