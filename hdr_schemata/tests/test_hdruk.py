from pydantic import ValidationError
import csv
import json
from hdr_schemata.models.HDRUK import Hdruk212, Hdruk410, Hdruk500
from hdr_schemata.definitions.HDRUK import DuoCodesEnum


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

    def test_patient_recontact_accepts_yes_no(self):
        for value in ["Yes", "No"]:
            metadata = json.loads(json.dumps(self.metadata))
            metadata["accessibility"]["usage"]["dataUsePermissions"] = {
                "patientRecontact": value
            }
            assert Hdruk410(**metadata) != None

    def test_patient_recontact_rejects_invalid_value(self):
        metadata = json.loads(json.dumps(self.metadata))
        metadata["accessibility"]["usage"]["dataUsePermissions"] = {
            "patientRecontact": "Not stated"
        }
        try:
            Hdruk410(**metadata)
            assert False, "expected ValidationError for an invalid patientRecontact value"
        except ValidationError:
            pass

    def test_dataset_without_patient_recontact_still_validates(self):
        metadata = json.loads(json.dumps(self.metadata))
        assert "dataUsePermissions" not in metadata["accessibility"]["usage"]
        assert Hdruk410(**metadata) != None

    def test_patient_recontact_defaults_to_no_when_omitted(self):
        metadata = json.loads(json.dumps(self.metadata))
        metadata["accessibility"]["usage"]["dataUsePermissions"] = {}
        dataset = Hdruk410(**metadata)
        assert dataset.accessibility.usage.dataUsePermissions.patientRecontact == "No"

    def test_duo_codes_accepts_valid_codes(self):
        metadata = json.loads(json.dumps(self.metadata))
        metadata["accessibility"]["usage"]["duoCodes"] = [
            "DUO:0000042",
            "DUO:0000021",
        ]
        assert Hdruk410(**metadata) != None

    def test_duo_codes_rejects_nonexistent_code(self):
        metadata = json.loads(json.dumps(self.metadata))
        metadata["accessibility"]["usage"]["duoCodes"] = ["DUO:9999999"]
        try:
            Hdruk410(**metadata)
            assert False, "expected ValidationError for a nonexistent DUO code"
        except ValidationError:
            pass

    def test_duo_codes_rejects_owl_only_hierarchy_terms(self):
        # DUO:0000032 ("population research") exists in the ontology's class
        # hierarchy (duo.owl) but not in DUO's own separately maintained flat
        # export (duo.csv) - deliberately excluded from the vendored enum,
        # not an oversight, so pin it as a rejected value.
        metadata = json.loads(json.dumps(self.metadata))
        metadata["accessibility"]["usage"]["duoCodes"] = ["DUO:0000032"]
        try:
            Hdruk410(**metadata)
            assert False, "expected ValidationError for an OWL-hierarchy-only DUO term"
        except ValidationError:
            pass

    def test_dataset_without_duo_codes_still_validates(self):
        metadata = json.loads(json.dumps(self.metadata))
        assert "duoCodes" not in metadata["accessibility"]["usage"]
        assert Hdruk410(**metadata) != None


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


def test_duo_codes_enum_matches_vendored_source():
    with open("../definitions/HDRUK/vendor/duo.csv") as f:
        vendored = {row["id"]: row["label"] for row in csv.DictReader(f)}

    vendored_ids = set(vendored)
    enum_ids = {member.value for member in DuoCodesEnum}

    assert enum_ids == vendored_ids, (
        "DuoCodesEnum has drifted from vendor/duo.csv - "
        f"in enum but not vendored: {enum_ids - vendored_ids}, "
        f"in vendored file but not enum: {vendored_ids - enum_ids}"
    )

    drifted = {
        member.value: (member.label, vendored[member.value])
        for member in DuoCodesEnum
        if member.label != vendored[member.value]
    }
    assert not drifted, (
        f"DuoCodesEnum labels have drifted from vendor/duo.csv: {drifted}"
    )
