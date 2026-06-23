from pydantic import ValidationError
import json
from hdr_schemata.models.HDRUK import Hdruk212, Hdruk500


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


class TestHdruk500:
    metadata = get_metadata("HDRUK", "5.0.0")
    json_schema = get_schema("HDRUK", "5.0.0")

    def test_validation(self):
        assert Hdruk500(**self.metadata) is not None

    def test_jsonld_fields(self):
        model = Hdruk500(**self.metadata)
        assert model.context is not None
        assert "5.0.0.jsonld" in str(model.context)
        assert model.type == "healthdcatap:HealthDataset"

    def test_new_dcat_fields(self):
        model = Hdruk500(**self.metadata)
        assert model.summary.shortTitle is not None
        assert model.summary.licenseUrl is not None
        assert model.summary.landingPage is not None
        assert model.summary.creator is not None
        assert model.summary.theme is not None
        assert len(model.summary.theme) > 0

    def test_healthdcatap_fields(self):
        model = Hdruk500(**self.metadata)
        assert model.coverage.numberOfRecords is not None
        assert model.coverage.numberOfUniqueIndividuals is not None
        assert model.provenance.retentionPeriod is not None
        assert model.accessibility.access.legalBasis is not None

    def test_distributions_and_quality(self):
        model = Hdruk500(**self.metadata)
        assert model.distributions is not None
        assert len(model.distributions) > 0
        assert model.qualityAnnotations is not None
        assert len(model.qualityAnnotations) > 0

    def test_json_schema(self):
        schema = Hdruk500.model_json_schema()
        assert schema == self.json_schema
        # Verify DCAT/JSON-LD fields appear in schema (uses by_alias=True by default)
        assert "@context" in schema["properties"]
        assert "@id" in schema["properties"]
        assert "@type" in schema["properties"]
        assert "distributions" in schema["properties"]
        assert "qualityAnnotations" in schema["properties"]
