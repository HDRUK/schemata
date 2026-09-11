import json
import subprocess
import sys
from pathlib import Path

from pydantic import ValidationError

from hdr_schemata.models.GWDM import Gwdm10, Gwdm22


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


def _gwdm22_model_json_schema_clean_process() -> dict:
    """Build JSON Schema in a fresh interpreter to avoid $defs clashes with other models."""
    root = Path(__file__).resolve().parents[2]
    code = (
        "import json, sys; "
        f"sys.path.insert(0, {str(root)!r}); "
        "from hdr_schemata.models.GWDM.v2_2 import Gwdm22; "
        "print(json.dumps(Gwdm22.model_json_schema()))"
    )
    out = subprocess.check_output(
        [sys.executable, "-c", code],
        cwd=str(root),
        text=True,
    )
    return json.loads(out)


class TestGwdm22:
    metadata = get_metadata("GWDM", "2.2")
    json_schema = get_schema("GWDM", "2.2")

    def test_validation(self):
        assert Gwdm22(**self.metadata) != None

    def test_json_schema(self):
        schema = _gwdm22_model_json_schema_clean_process()
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

    def test_duo_codes_and_patient_recontact_accepted(self):
        metadata = json.loads(json.dumps(self.metadata))
        metadata["accessibility"]["usage"]["duoCodes"] = "DUO:0000042"
        metadata["accessibility"]["usage"]["patientRecontact"] = "Yes"
        assert Gwdm22(**metadata) != None

    def test_dataset_without_new_fields_still_validates(self):
        metadata = json.loads(json.dumps(self.metadata))
        del metadata["accessibility"]["usage"]["duoCodes"]
        del metadata["accessibility"]["usage"]["patientRecontact"]
        assert Gwdm22(**metadata) != None

    def test_rejects_unknown_property_in_usage(self):
        # Usage has additionalProperties: false - confirms a typo'd/unsupported
        # field name fails loudly rather than being silently dropped.
        metadata = json.loads(json.dumps(self.metadata))
        metadata["accessibility"]["usage"]["notARealField"] = "x"
        try:
            Gwdm22(**metadata)
            assert False, "expected ValidationError for an unknown usage property"
        except ValidationError:
            pass
