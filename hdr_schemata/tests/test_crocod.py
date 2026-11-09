import copy
import json
from pathlib import Path
import pytest
from pydantic import ValidationError

from hdr_schemata.models.CROCOD import Crocod100

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

class TestCrocod100:
    metadata = get_metadata("CROCOD", "1.0.0")
    json_schema = get_schema("CROCOD", "1.0.0")

    def test_validation(self):
        assert Crocod100(**self.metadata) is not None

    def test_json_schema(self):
        schema = Crocod100.model_json_schema()
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

    def test_trial_summary_is_required(self):
        metadata = {k: v for k, v in self.metadata.items() if k != "trialSummary"}
        with pytest.raises(ValidationError):
            Crocod100(**metadata)

    def test_end_year_before_start_year_is_rejected(self):
        metadata = copy.deepcopy(self.metadata)
        metadata["trialDesign"]["endYear"] = 2015
        with pytest.raises(ValidationError):
            Crocod100(**metadata)

    def test_participants_must_be_positive(self):
        metadata = copy.deepcopy(self.metadata)
        metadata["trialDesign"]["numberOfParticipants"] = 0
        with pytest.raises(ValidationError):
            Crocod100(**metadata)

    def test_unknown_participant_location_is_rejected(self):
        metadata = copy.deepcopy(self.metadata)
        metadata["healthSystemsData"]["participantLocations"] = ["Atlantis"]
        with pytest.raises(ValidationError):
            Crocod100(**metadata)

    def test_learnings_are_accepted_for_a_declared_data_use(self):
        metadata = copy.deepcopy(self.metadata)
        metadata["learnings"] = {
            "recruitment": {
                "tags": ["Identified eligible participants from screening records"],
                "summary": "Illustrative summary",
                "content": "<p>Illustrative content.</p>",
            }
        }
        assert Crocod100(**metadata).learnings.recruitment.tags

    def test_learnings_for_an_undeclared_data_use_are_rejected(self):
        metadata = copy.deepcopy(self.metadata)
        metadata["healthSystemsData"]["usedFor"] = ["Recruitment"]
        metadata["learnings"] = {"pharmacovigilance": {"summary": "Illustrative summary"}}
        with pytest.raises(ValidationError):
            Crocod100(**metadata)

    def test_gateway_and_non_gateway_references_are_both_accepted(self):
        metadata = copy.deepcopy(self.metadata)
        metadata["healthSystemsData"]["datasetsAccessed"] = [
            {"gatewayId": "b00255bb-4d78-468d-a436-e08f4af23daa", "title": "A Gateway dataset"},
            {"title": "A non-Gateway dataset", "url": "https://example.com/dataset"},
        ]
        assert len(Crocod100(**metadata).healthSystemsData.datasetsAccessed) == 2
