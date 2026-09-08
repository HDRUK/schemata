from pydantic import ValidationError
import json
from hdr_schemata.models.HDRUK import Hdruk212, Hdruk410


def get_metadata(model, version):
    metadata = json.load(open(f"../examples/{model}/{version}/example.json"))
    return metadata


def get_schema(model, version):
    metadata = json.load(open(f"../models/{model}/{version}/schema.json"))
    return metadata


class TestHdruk212:
    metadata = get_metadata("HDRUK", "2.1.2")
    json_schema = get_schema("HDRUK", "2.1.2")

    def test_validation(self):
        assert Hdruk212(**self.metadata) != None

    def test_json_schema(self):
        schema = Hdruk212.model_json_schema()
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


class TestHdruk410:
    metadata = get_metadata("HDRUK", "4.1.0")
    json_schema = get_schema("HDRUK", "4.1.0")

    def test_validation(self):
        assert Hdruk410(**self.metadata) != None

    def test_json_schema(self):
        schema = Hdruk410.model_json_schema()
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

    def test_conforms_to_accepts_new_standards(self):
        metadata = json.loads(json.dumps(self.metadata))
        metadata["accessibility"]["formatAndStandards"]["conformsTo"] = [
            "BNF",
            "DDI",
            "DCAT",
        ]
        assert Hdruk410(**metadata) != None

    def test_conforms_to_rejects_invalid_standard(self):
        metadata = json.loads(json.dumps(self.metadata))
        metadata["accessibility"]["formatAndStandards"]["conformsTo"] = [
            "NOT_A_REAL_STANDARD"
        ]
        try:
            Hdruk410(**metadata)
            assert False, "expected ValidationError for an invalid conformsTo value"
        except ValidationError:
            pass

    def test_dataset_without_new_optional_fields_still_validates(self):
        metadata = json.loads(json.dumps(self.metadata))
        metadata["accessibility"]["formatAndStandards"]["conformsTo"] = ["LOCAL"]
        assert Hdruk410(**metadata) != None
