from pydantic import ValidationError
import json

from hdr_schemata.models.HDRUK import Hdruk212
from hdr_schemata.models.GWDM import Gwdm10
from hdr_schemata.models.SchemaOrg import GoogleRecommendedDataset
from hdr_schemata.models.SchemaOrg import BioSchema


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
        print("here in TestGwdm10")
        print(expected_keys)
        print(list(schema.keys()))

        assert list(schema.keys()) == expected_keys
        assert schema == self.json_schema


class TestGoogleRecommended:
    metadata = get_metadata("SchemaOrg", "GoogleRecommended")
    json_schema = get_schema("SchemaOrg", "GoogleRecommended")

    def test_organization(self):
        from hdr_schemata.models.SchemaOrg.GoogleRecommended import Organization

        assert Organization(**self.metadata["creator"]) != None

    def test_validation(self):
        assert GoogleRecommendedDataset(**self.metadata) != None

    def test_json_schema(self):
        schema = GoogleRecommendedDataset.model_json_schema()
        assert schema == self.json_schema


class TestBioSchema:
    metadata = get_metadata("SchemaOrg", "BioSchema")
    json_schema = get_schema("SchemaOrg", "BioSchema")

    def test_validation(self):
        assert BioSchema(**self.metadata) != None

    def test_json_schema(self):
        schema = BioSchema.model_json_schema()
        assert schema == self.json_schema
