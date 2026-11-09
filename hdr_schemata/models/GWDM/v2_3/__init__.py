import json
from typing import Optional
from pydantic import Field, model_validator

from hdr_schemata.definitions.HDRUK import RecordType
from hdr_schemata.models.GWDM.v2_2 import Gwdm22

from .CaseStudy import CaseStudy
from .Linkage import Linkage
from .Population import Population
from .Required import Required

from .annotations import annotations as an


class Gwdm23(Gwdm22):
    required: Required = Field(
        ..., description=Gwdm22.model_fields["required"].description,
        title=Gwdm22.model_fields["required"].title,
    )

    linkage: Optional[Linkage] = Field(
        None, description=Gwdm22.model_fields["linkage"].description,
        title=Gwdm22.model_fields["linkage"].title,
    )

    population: Optional[Population] = Field(
        None, description=an.population.description, title=an.population.title
    )

    crocod: Optional[CaseStudy] = Field(
        None, description=an.crocod.description, title=an.crocod.title
    )

    @model_validator(mode="after")
    def crocod_matches_record_type(self):
        is_case_study = self.required.recordType == RecordType.CASE_STUDY
        if is_case_study and self.crocod is None:
            raise ValueError("required.recordType is caseStudy but crocod is missing")
        if not is_case_study and self.crocod is not None:
            raise ValueError("crocod is set but required.recordType is not caseStudy")
        return self

    @classmethod
    def save_schema(cls, location: str = "./2.3/schema.json") -> None:
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
