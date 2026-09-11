import copy
import json
import subprocess
import sys
from pathlib import Path

from hdr_schemata.models import annotations as annotations_module
from hdr_schemata.models.annotations import (
    annotations,
    dict_to_namespace,
    get_annotations,
    stitch_namespaces,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
MODELS_DIR = Path(annotations_module.__file__).parent.parent
VERSION_ANNOTATION_DIRS = sorted(
    path.parent for path in MODELS_DIR.glob("*/v*/annotations/config.yaml")
)

SNAPSHOT_SCRIPT = """
import importlib, json, sys
from types import SimpleNamespace


def dump(value):
    if isinstance(value, SimpleNamespace):
        return {k: dump(v) for k, v in sorted(vars(value).items())}
    if isinstance(value, list):
        return [dump(v) for v in value]
    return value


for family in sys.argv[1:]:
    importlib.import_module("hdr_schemata.models." + family)

print(
    json.dumps(
        {
            name: dump(module.annotations)
            for name, module in sorted(sys.modules.items())
            if name.startswith("hdr_schemata.models.") and name.endswith(".annotations")
        },
        sort_keys=True,
    )
)
"""


def _snapshot(*families):
    out = subprocess.check_output(
        [sys.executable, "-c", SNAPSHOT_SCRIPT, *families],
        cwd=str(REPO_ROOT),
        text=True,
    )
    return json.loads(out)


def test_version_annotation_dirs_are_discovered():
    names = {path.parent.name for path in VERSION_ANNOTATION_DIRS}
    assert {"v1_0", "v2_1_2", "v4_1_0"} <= names


def test_stitching_does_not_mutate_the_shared_base():
    before = copy.deepcopy(annotations.Common)
    for version_dir in VERSION_ANNOTATION_DIRS:
        stitch_namespaces(annotations.Common, get_annotations(str(version_dir)))
    assert annotations.Common == before


def test_stitching_deep_merges_dicts_and_replaces_lists_and_scalars():
    base = dict_to_namespace(
        {"nested": {"kept": 1, "replaced": 2}, "items": [1, 2], "scalar": "base"}
    )
    update = dict_to_namespace({"nested": {"replaced": 3}, "items": [9], "scalar": "update"})

    stitched = stitch_namespaces(base, update)

    assert stitched.nested == dict_to_namespace({"kept": 1, "replaced": 3})
    assert stitched.items == [9]
    assert stitched.scalar == "update"
    assert base == dict_to_namespace(
        {"nested": {"kept": 1, "replaced": 2}, "items": [1, 2], "scalar": "base"}
    )


def test_annotations_are_independent_of_family_import_order():
    assert _snapshot("CRUK", "GWDM", "HDRUK") == _snapshot("GWDM", "HDRUK", "CRUK")
