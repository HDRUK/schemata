from datetime import date, datetime
from typing import Optional, Union
from pydantic import BaseModel, Field, conint
from hdr_schemata.definitions.HDRUK import *
from .annotations import annotations

an = annotations.population

class StudyDesign(BaseModel):
    class Config:
        extra = "forbid"

    isLongitudinal: Optional[bool] = Field(None, **an.studyDesign.isLongitudinal.__dict__)
    isFamilyBased: Optional[bool] = Field(None, **an.studyDesign.isFamilyBased.__dict__)
    isClinicalBased: Optional[bool] = Field(None, **an.studyDesign.isClinicalBased.__dict__)

class Wave(BaseModel):
    class Config:
        extra = "forbid"

    waveId: OneHundredFiftyCharacters = Field(..., **an.wave.waveId.__dict__)
    waveType: WaveType = Field(..., **an.wave.waveType.__dict__)
    waveNumber: Optional[conint(ge=1)] = Field(None, **an.wave.waveNumber.__dict__)
    label: Optional[OneHundredFiftyCharacters] = Field(None, **an.wave.label.__dict__)

class Recruitment(BaseModel):
    class Config:
        extra = "forbid"

    status: Optional[RecruitmentStatus] = Field(None, **an.recruitment.status.__dict__)
    startDate: Optional[Union[date, datetime]] = Field(
        None, **an.recruitment.startDate.__dict__
    )

    endDate: Optional[Union[date, datetime]] = Field(
        None, **an.recruitment.endDate.__dict__
    )

    samplingMethod: Optional[Description] = Field(
        None, **an.recruitment.samplingMethod.__dict__
    )

class FollowUpSchedule(BaseModel):
    class Config:
        extra = "forbid"

    frequency: FollowUpFrequency = Field(..., **an.followUpSchedule.frequency.__dict__)
    note: Optional[Description] = Field(
        None, **an.followUpSchedule.note.__dict__
    )

class Eligibility(BaseModel):
    class Config:
        extra = "forbid"

    inclusionCriteria: Optional[Description] = Field(
        None, **an.eligibility.inclusionCriteria.__dict__
    )

    exclusionCriteria: Optional[Description] = Field(
        None, **an.eligibility.exclusionCriteria.__dict__
    )

class Population(BaseModel):
    class Config:
        extra = "forbid"

    studyDesign: Optional[StudyDesign] = Field(
        None, title=an.studyDesign.title, description=an.studyDesign.description
    )

    wave: Optional[Wave] = Field(None, title=an.wave.title, description=an.wave.description)
    recruitment: Optional[Recruitment] = Field(
        None, title=an.recruitment.title, description=an.recruitment.description
    )

    followUpSchedule: Optional[FollowUpSchedule] = Field(
        None, title=an.followUpSchedule.title, description=an.followUpSchedule.description
    )

    eligibility: Optional[Eligibility] = Field(
        None, title=an.eligibility.title, description=an.eligibility.description
    )
