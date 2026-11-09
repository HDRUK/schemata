import json
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, conint, model_validator
from hdr_schemata.definitions.HDRUK import *

from hdr_schemata.models._shared.v4.EntityReference import EntityReference

from .HealthSystemsData import HealthSystemsData, Learnings
from .Trial import Governance, TrialDesign, TrialSummary

from .annotations import annotations as an

# Learnings for these areas only make sense if the trial used health systems data for them.
LEARNING_REQUIRES_USE = {
    "recruitment": HealthSystemsDataUse.RECRUITMENT,
    "pharmacovigilance": HealthSystemsDataUse.PHARMACOVIGILANCE,
    "outcomeAscertainment": HealthSystemsDataUse.OUTCOME_ASCERTAINMENT,
}


class Crocod100(BaseModel):
    class Config:
        extra = "forbid"

    id: Optional[conint(ge=1)] = Field(None, **an.id.__dict__)

    pid: OneHundredFiftyCharacters = Field(..., **an.pid.__dict__)

    version: Semver = Field(..., **an.version.__dict__)

    issued: datetime = Field(..., **an.issued.__dict__)

    modified: datetime = Field(..., **an.modified.__dict__)

    trialSummary: TrialSummary = Field(
        ..., title=an.trialSummary.title, description=an.trialSummary.description
    )

    trialDesign: Optional[TrialDesign] = Field(
        None, title=an.trialDesign.title, description=an.trialDesign.description
    )

    governance: Optional[Governance] = Field(
        None, title=an.governance.title, description=an.governance.description
    )

    healthSystemsData: Optional[HealthSystemsData] = Field(
        None, title=an.healthSystemsData.title, description=an.healthSystemsData.description
    )

    learnings: Optional[Learnings] = Field(
        None, title=an.learnings.title, description=an.learnings.description
    )

    publications: Optional[List[EntityReference]] = Field(None, **an.publications.__dict__)

    readMore: Optional[List[RichText]] = Field(None, **an.readMore.__dict__)

    @model_validator(mode="after")
    def learnings_match_data_use(self):
        if not self.learnings:
            return self
        used = set(self.healthSystemsData.usedFor or []) if self.healthSystemsData else set()
        for area, use in LEARNING_REQUIRES_USE.items():
            if getattr(self.learnings, area) and use not in used:
                raise ValueError(
                    f"learnings.{area} is set but healthSystemsData.usedFor does not include '{use.value}'"
                )
        return self

    @classmethod
    def save_schema(cls, location="./1.0.0/schema.json"):
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
