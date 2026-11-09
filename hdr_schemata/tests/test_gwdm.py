import copy
import json

from pydantic import ValidationError

from hdr_schemata.models.GWDM import Gwdm10, Gwdm22, Gwdm23


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


class TestGwdm22:
    metadata = get_metadata("GWDM", "2.2")
    json_schema = get_schema("GWDM", "2.2")

    def test_validation(self):
        assert Gwdm22(**self.metadata) != None

    def test_json_schema(self):
        schema = Gwdm22.model_json_schema()
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


class TestGwdm23:
    metadata = get_metadata("GWDM", "2.3")
    json_schema = get_schema("GWDM", "2.3")

    def test_validation(self):
        assert Gwdm23(**self.metadata) != None

    def test_json_schema(self):
        schema = Gwdm23.model_json_schema()
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

    def test_population_is_optional(self):
        metadata = {k: v for k, v in self.metadata.items() if k != "population"}
        assert Gwdm23(**metadata).population is None

    def test_dataset_record_type_defaults_to_dataset(self):
        dataset = Gwdm23(**self.metadata)
        assert dataset.required.recordType.value == "dataset"
        assert dataset.crocod is None


class TestGwdm23CaseStudy:
    metadata = json.load(open("../examples/GWDM/2.3/case_study.json"))

    def test_validation(self):
        assert Gwdm23(**self.metadata).required.recordType.value == "caseStudy"

    def test_case_study_without_crocod_is_rejected(self):
        metadata = {k: v for k, v in self.metadata.items() if k != "crocod"}
        try:
            Gwdm23(**metadata)
            assert False, "expected ValidationError for a case study without crocod"
        except ValidationError:
            pass

    def test_crocod_on_a_dataset_is_rejected(self):
        metadata = copy.deepcopy(self.metadata)
        metadata["required"]["recordType"] = "dataset"
        try:
            Gwdm23(**metadata)
            assert False, "expected ValidationError for crocod on a dataset"
        except ValidationError:
            pass
