import copy
import json
from pathlib import Path
import pytest
from pydantic import ValidationError

from hdr_schemata.models.PRUK import Pruk100

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

class TestPruk100:
    metadata = get_metadata("PRUK", "1.0.0")
    json_schema = get_schema("PRUK", "1.0.0")

    def test_validation(self):
        assert Pruk100(**self.metadata) is not None

    def test_json_schema(self):
        schema = Pruk100.model_json_schema()
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

    def test_population_is_required(self):
        metadata = {k: v for k, v in self.metadata.items() if k != "population"}
        with pytest.raises(ValidationError):
            Pruk100(**metadata)

    def test_unknown_follow_up_frequency_is_rejected(self):
        metadata = copy.deepcopy(self.metadata)
        metadata["population"]["followUpSchedule"]["frequency"] = "Sometimes"
        with pytest.raises(ValidationError):
            Pruk100(**metadata)

    def test_wave_of_is_a_single_study(self):
        metadata = copy.deepcopy(self.metadata)
        metadata["linkage"]["waveOf"] = [metadata["linkage"]["waveOf"]]
        with pytest.raises(ValidationError):
            Pruk100(**metadata)
