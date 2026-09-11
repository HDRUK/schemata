import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
FROZEN = json.loads((REPO_ROOT / "frozen.json").read_text())
AVAILABLE = json.loads((REPO_ROOT / "available.json").read_text())

FROZEN_VERSIONS = [
    (family, version) for family, versions in FROZEN.items() for version in versions
]


def test_frozen_versions_are_still_published():
    missing = [
        (family, version)
        for family, version in FROZEN_VERSIONS
        if version not in AVAILABLE.get(family, [])
    ]
    assert missing == [], (
        "frozen versions must stay in available.json - traser compiles its schema "
        f"registry from it, so a version missing here stops resolving: {missing}"
    )


def test_frozen_versions_keep_their_schema_on_disk():
    missing = [
        (family, version)
        for family, version in FROZEN_VERSIONS
        if not (REPO_ROOT / "hdr_schemata" / "models" / family / version / "schema.json").is_file()
    ]
    assert missing == [], f"frozen versions with no schema.json: {missing}"


def test_frozen_versions_have_no_registered_model():
    import importlib
    import inspect

    from pydantic import BaseModel

    still_built = []
    for family, version in FROZEN_VERSIONS:
        module = importlib.import_module(f"hdr_schemata.models.{family}")
        version_dirs = {
            cls.__module__.split(".")[-1]
            for _, cls in inspect.getmembers(module, inspect.isclass)
            if issubclass(cls, BaseModel)
            and cls.__module__.startswith(f"hdr_schemata.models.{family}.v")
        }
        if "v" + version.replace(".", "_") in version_dirs:
            still_built.append((family, version))

    assert still_built == [], (
        "a frozen version must not also be registered in its family __init__.py, "
        f"or the build would overwrite the frozen schema.json: {still_built}"
    )
