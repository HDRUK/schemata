from __future__ import annotations

import importlib
import inspect
import json
import subprocess
import sys
from pathlib import Path

from pydantic import BaseModel

REPO_ROOT = Path(__file__).parent.parent.parent
MODELS_DIR = Path(__file__).parent.parent / "models"

SCHEMAORG_VERSIONS = ["BioSchema", "default", "GoogleRecommended"]


def _version_str(version_dir_name: str) -> str:
    """v1_0 -> '1.0', v2_1_2 -> '2.1.2'"""
    return version_dir_name[1:].replace("_", ".")


def _version_sort_key(version_str: str) -> tuple:
    try:
        return tuple(int(x) for x in version_str.split("."))
    except ValueError:
        return (0,)


def _generate_schema_isolated(module_path: str, class_name: str, output_path: str) -> None:
    """Generate schema.json in a fresh interpreter — avoids $defs cross-contamination between families."""
    code = (
        "import json, sys; "
        f"sys.path.insert(0, {str(REPO_ROOT)!r}); "
        f"from {module_path} import {class_name}; "
        f"f = open({output_path!r}, 'w'); "
        f"json.dump({class_name}.model_json_schema(), f, indent=6); "
        "f.close()"
    )
    subprocess.run([sys.executable, "-c", code], check=True)


def _build_family(family_dir: Path) -> list:
    family = family_dir.name
    family_module = importlib.import_module(f"hdr_schemata.models.{family}")

    # The family __init__.py is the version registry — collect classes from v* submodules
    seen = {}
    for name, cls in inspect.getmembers(family_module, inspect.isclass):
        if not (isinstance(cls, type) and issubclass(cls, BaseModel)):
            continue
        mod = cls.__module__
        if not mod.startswith(f"hdr_schemata.models.{family}.v"):
            continue
        version_dir = mod.split(".")[-1]
        if version_dir not in seen:
            seen[version_dir] = (name, cls)

    versions = []
    for version_dir in sorted(seen, key=lambda d: _version_sort_key(_version_str(d))):
        class_name, _ = seen[version_dir]
        version_str = _version_str(version_dir)
        output_dir = family_dir / version_str
        output_dir.mkdir(exist_ok=True)
        output_path = str(output_dir / "schema.json")
        module_path = f"hdr_schemata.models.{family}.{version_dir}"
        _generate_schema_isolated(module_path, class_name, output_path)
        print(f"  {family}/{version_str}")
        versions.append(version_str)

    return versions


def _build_schemaorg(family_dir: Path) -> list:
    script = family_dir / "create_schemas.py"
    if script.exists():
        subprocess.run([sys.executable, str(script)], cwd=str(family_dir), check=True)
    return SCHEMAORG_VERSIONS


def build() -> int:
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

    with open(REPO_ROOT / "available.json", "w") as f:
        json.dump(available, f, indent=2)
        f.write("\n")

    total = sum(len(v) for v in available.values())
    print(f"\navailable.json written ({total} schemas across {len(available)} families)")

    print("\nGenerating docs...")
    from hdr_schemata.utils.create_markdown import build_docs
    build_docs()

    return 0


if __name__ == "__main__":
    sys.exit(build())
