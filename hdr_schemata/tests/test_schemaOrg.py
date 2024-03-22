from pydantic import ValidationError
import json

from hdr_schemata.models.SchemaOrg import GoogleRecommendedDataset
from hdr_schemata.models.SchemaOrg import BioSchema


def get_metadata(model, version):
    metadata = json.load(open(f"../examples/{model}/{version}/example.json"))
    return metadata


def get_schema(model, version):
    metadata = json.load(open(f"../models/{model}/{version}/schema.json"))
    return metadata


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
