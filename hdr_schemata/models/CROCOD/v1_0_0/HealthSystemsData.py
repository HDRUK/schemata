from typing import List, Optional
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from hdr_schemata.models._shared.v4.EntityReference import EntityReference
from hdr_schemata.models._shared.v4.Learning import Learning

from .annotations import annotations

an = annotations


class HealthSystemsData(BaseModel):
    class Config:
        extra = "forbid"

    usedFor: Optional[List[HealthSystemsDataUse]] = Field(
        None, **an.healthSystemsData.usedFor.__dict__
    )

    participantLocations: Optional[List[ParticipantLocation]] = Field(
        None, **an.healthSystemsData.participantLocations.__dict__
    )

    dataProvidersAppliedTo: Optional[List[EntityReference]] = Field(
        None, **an.healthSystemsData.dataProvidersAppliedTo.__dict__
    )

    datasetsAccessed: Optional[List[EntityReference]] = Field(
        None, **an.healthSystemsData.datasetsAccessed.__dict__
    )

    yearFirstAppliedFor: Optional[Year] = Field(
        None, **an.healthSystemsData.yearFirstAppliedFor.__dict__
    )


class Learnings(BaseModel):
    class Config:
        extra = "forbid"

    recruitment: Optional[Learning] = Field(None, **an.learnings.recruitment.__dict__)

    pharmacovigilance: Optional[Learning] = Field(
        None, **an.learnings.pharmacovigilance.__dict__
    )

    outcomeAscertainment: Optional[Learning] = Field(
        None, **an.learnings.outcomeAscertainment.__dict__
    )

    patientPublicInvolvement: Optional[Learning] = Field(
        None, **an.learnings.patientPublicInvolvement.__dict__
    )

    additionalInsights: Optional[RichText] = Field(
        None, **an.learnings.additionalInsights.__dict__
    )
