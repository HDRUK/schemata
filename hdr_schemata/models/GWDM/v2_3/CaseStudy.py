from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field
from hdr_schemata.definitions.HDRUK import *

from hdr_schemata.models._shared.v4.EntityReference import EntityReference
from hdr_schemata.models._shared.v4.Learning import Learning

from .annotations import annotations

an = annotations.crocod


class TrialDesign(BaseModel):
    class Config:
        extra = "forbid"

    categories: Optional[RichText] = Field(None, **an.trialDesign.categories.__dict__)

    designDescription: Optional[RichText] = Field(
        None, **an.trialDesign.designDescription.__dict__
    )

    registration: Optional[RichText] = Field(None, **an.trialDesign.registration.__dict__)


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


class HealthSystemsData(BaseModel):
    class Config:
        extra = "forbid"

    usedFor: Optional[List[HealthSystemsDataUse]] = Field(
        None, **an.healthSystemsData.usedFor.__dict__
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


class CaseStudy(BaseModel):
    class Config:
        extra = "forbid"

    trialStatus: TrialStatus = Field(..., **an.trialStatus.__dict__)

    therapeuticArea: Optional[RichText] = Field(None, **an.therapeuticArea.__dict__)

    laySummary: Optional[RichText] = Field(None, **an.laySummary.__dict__)

    background: Optional[RichText] = Field(None, **an.background.__dict__)

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
