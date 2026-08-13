import json
import subprocess
import sys
from pathlib import Path

from hdr_schemata.models.GWDM import Gwdm10


def _gwdm10_model_json_schema_clean_process() -> dict:
    """Build JSON Schema in a fresh interpreter to avoid $defs clashes with other models."""
    root = Path(__file__).resolve().parents[2]
    code = (
        "import json, sys; "
        f"sys.path.insert(0, {str(root)!r}); "
        "from hdr_schemata.models.GWDM.v1_0 import Gwdm10; "
        "print(json.dumps(Gwdm10.model_json_schema()))"
    )
    out = subprocess.check_output(
        [sys.executable, "-c", code],
        cwd=str(root),
        text=True,
    )
    return json.loads(out)


def get_metadata(model, version):
    metadata = json.load(open(f"../examples/{model}/{version}/example.json"))
    return metadata


def get_schema(model, version):
    metadata = json.load(open(f"../models/{model}/{version}/schema.json"))
    return metadata


class TestGwdm10:
    metadata = get_metadata("GWDM", "1.0")
    json_schema = get_schema("GWDM", "1.0")

    def test_validation(self):
        assert Gwdm10(**self.metadata) != None

    def test_json_schema(self):
        schema = _gwdm10_model_json_schema_clean_process()
        expected_keys = [
            "$defs",
            "additionalProperties",
            "properties",
            "required",
            "title",
            "type",
        ]

        assert list(schema.keys()) == expected_keys
        assert schema == self.json_schema
