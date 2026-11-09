from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field, conint, constr, model_validator
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations


class TrialSummary(BaseModel):
    class Config:
        extra = "forbid"

    # Capped at 100 to match GWDM summary.shortTitle, which stores it.
    acronym: constr(min_length=2, max_length=100) = Field(
        ..., **an.trialSummary.acronym.__dict__
    )

    fullTitle: TwoHundredFiftyFiveCharacters = Field(..., **an.trialSummary.fullTitle.__dict__)

    status: TrialStatus = Field(..., **an.trialSummary.status.__dict__)

    therapeuticArea: Optional[RichText] = Field(None, **an.trialSummary.therapeuticArea.__dict__)

    laySummary: Optional[RichText] = Field(None, **an.trialSummary.laySummary.__dict__)

    background: Optional[RichText] = Field(None, **an.trialSummary.background.__dict__)


class TrialDesign(BaseModel):
    class Config:
        extra = "forbid"

    categories: Optional[RichText] = Field(None, **an.trialDesign.categories.__dict__)

    designDescription: Optional[RichText] = Field(
        None, **an.trialDesign.designDescription.__dict__
    )

    registration: Optional[RichText] = Field(None, **an.trialDesign.registration.__dict__)

    startYear: Optional[Year] = Field(None, **an.trialDesign.startYear.__dict__)

    endYear: Optional[Year] = Field(None, **an.trialDesign.endYear.__dict__)

    numberOfParticipants: Optional[conint(ge=1)] = Field(
        None, **an.trialDesign.numberOfParticipants.__dict__
    )

    @model_validator(mode="after")
    def end_not_before_start(self):
        if self.startYear and self.endYear and self.endYear.root < self.startYear.root:
            raise ValueError("endYear cannot be before startYear")
        return self


class Governance(BaseModel):
    class Config:
        extra = "forbid"

    sponsor: Optional[RichText] = Field(None, **an.governance.sponsor.__dict__)

    funder: Optional[RichText] = Field(None, **an.governance.funder.__dict__)

    approvingBody: Optional[RichText] = Field(None, **an.governance.approvingBody.__dict__)

    principalInvestigator: Optional[OneHundredFiftyCharacters] = Field(
        None, **an.governance.principalInvestigator.__dict__
    )

    contactPoints: Optional[List[EmailStr]] = Field(
        None, **an.governance.contactPoints.__dict__
    )
