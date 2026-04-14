import json
from pathlib import Path

from hdr_schemata.models.CRUK import Cruk100


def get_metadata(model, version):
    base = Path(__file__).resolve().parent.parent
    metadata = json.loads(
        (base / "examples" / model / version / "example.json").read_text()
    )
    return metadata


def get_schema(model, version):
    base = Path(__file__).resolve().parent.parent
    metadata = json.loads((base / "models" / model / version / "schema.json").read_text())
    return metadata


class TestCruk100:
    metadata = get_metadata("CRUK", "1.0.0")
    json_schema = get_schema("CRUK", "1.0.0")

    def test_validation(self):
        assert Cruk100(**self.metadata) is not None

    def test_json_schema(self):
        schema = Cruk100.model_json_schema()
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

