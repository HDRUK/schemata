from pydantic import ValidationError
import json

from hdr_schemata.models.GWDM import Gwdm10


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
        schema = Gwdm10.model_json_schema()
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
