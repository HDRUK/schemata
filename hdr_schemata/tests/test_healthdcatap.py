import copy
import json
from pathlib import Path
import pytest
from pydantic import ValidationError

from hdr_schemata.models.HealthDCATAP import HealthDcatAp8

BASE = Path(__file__).resolve().parent.parent


def get_metadata(model, version):
    return json.loads((BASE / "examples" / model / version / "example.json").read_text())


def get_schema(model, version):
    return json.loads((BASE / "models" / model / version / "schema.json").read_text())


class TestHealthDcatAp8:
    metadata = get_metadata("HealthDCATAP", "8")
    json_schema = get_schema("HealthDCATAP", "8")
    context = json.loads((BASE / "models" / "HealthDCATAP" / "8" / "context.jsonld").read_text())

    def test_validation(self):
        assert HealthDcatAp8(**self.metadata) is not None

    def test_json_schema(self):
        schema = HealthDcatAp8.model_json_schema()
        assert schema == self.json_schema

    def test_example_uses_the_published_context(self):
        assert self.metadata["@context"] == self.context

    def test_dumps_back_to_json_ld_keys(self):
        dumped = HealthDcatAp8(**self.metadata).model_dump(by_alias=True, exclude_none=True, mode="json")
        assert dumped["@type"] == "Dataset"
        assert dumped["@id"] == self.metadata["@id"]

    @pytest.mark.parametrize(
        "field",
        [
            "identifier",
            "description",
            "accessRights",
            "applicableLegislation",
            "datasetType",
            "theme",
            "healthCategory",
            "keyword",
            "contactPoint",
            "publisher",
            "hdab",
            "provenance",
            "hasStructuredData",
            "distribution",
        ],
    )
    def test_non_public_mandatory_fields(self, field):
        metadata = {k: v for k, v in self.metadata.items() if k != field}
        with pytest.raises(ValidationError):
            HealthDcatAp8(**metadata)

    def test_empty_health_category_is_rejected(self):
        metadata = copy.deepcopy(self.metadata)
        metadata["healthCategory"] = []
        with pytest.raises(ValidationError):
            HealthDcatAp8(**metadata)

    def test_public_access_rights_are_rejected(self):
        metadata = copy.deepcopy(self.metadata)
        metadata["accessRights"]["@id"] = (
            "http://publications.europa.eu/resource/authority/access-right/PUBLIC"
        )
        with pytest.raises(ValidationError):
            HealthDcatAp8(**metadata)

    def test_theme_must_include_health(self):
        metadata = copy.deepcopy(self.metadata)
        metadata["theme"] = [
            {"@id": "http://publications.europa.eu/resource/authority/data-theme/ECON", "@type": "Concept"}
        ]
        with pytest.raises(ValidationError):
            HealthDcatAp8(**metadata)

    def test_structured_data_requires_variables(self):
        metadata = copy.deepcopy(self.metadata)
        metadata.pop("hasVariables")
        with pytest.raises(ValidationError):
            HealthDcatAp8(**metadata)

    def test_unstructured_data_is_accepted_without_variables(self):
        metadata = copy.deepcopy(self.metadata)
        metadata.pop("hasVariables")
        metadata["hasStructuredData"] = False
        assert HealthDcatAp8(**metadata).hasVariables is None

    def test_agent_without_contact_is_rejected(self):
        metadata = copy.deepcopy(self.metadata)
        metadata["hdab"]["contact"] = {"@type": "ContactPoint"}
        with pytest.raises(ValidationError):
            HealthDcatAp8(**metadata)

    def test_column_needs_a_description(self):
        metadata = copy.deepcopy(self.metadata)
        metadata["hasVariables"][0]["table"][0]["column"][0].pop("description")
        with pytest.raises(ValidationError):
            HealthDcatAp8(**metadata)

    def test_max_age_below_min_age_is_rejected(self):
        metadata = copy.deepcopy(self.metadata)
        metadata["minTypicalAge"], metadata["maxTypicalAge"] = 60, 18
        with pytest.raises(ValidationError):
            HealthDcatAp8(**metadata)
