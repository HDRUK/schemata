import json

from pydantic import ValidationError

from hdr_schemata.models.GWDM import Gwdm22


def get_metadata(model, version):
    metadata = json.load(open(f"../examples/{model}/{version}/example.json"))
    return metadata


def get_schema(model, version):
    metadata = json.load(open(f"../models/{model}/{version}/schema.json"))
    return metadata


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
