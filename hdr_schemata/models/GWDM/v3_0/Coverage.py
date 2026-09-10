from typing import List, Optional

from pydantic import BaseModel, Field

from hdr_schemata.definitions.HDRUK import FollowupV2, LongDescription


class Coverage(BaseModel):
    class Config:
        extra = "forbid"

    spatial: Optional[List[str]] = Field(
        None,
        title="Geographic coverage",
        description="The geographical area covered by the dataset. It is recommended that links are to entries in one of the recommended standards: For locations in the UK: ONS standards. For locations in other countries: ISO 3166-1 & ISO 3166-2.",
        examples=[
            "United Kingdom",
            "https://www.geonames.org/2635167/united-kingdom-of-great-britain-and-northern-ireland.html",
        ],
    )
    pathway: Optional[LongDescription] = Field(
        None,
        title="Patient pathway description",
        description="Please indicate if the dataset is representative of the patient pathway and any limitations the dataset may have with respect to pathway coverage. This could include if the dataset is from a single speciality or area, a single tier of care, linked across two tiers (e.g. primary and secondary care), or an integrated care record covering the whole patient pathway.",
    )
    followUp: Optional[FollowupV2] = Field(
        None,
        title="Follow-up",
        description="If known, what is the typical time span that a patient appears in the dataset (follow up period). In a prospective cohort study, after baseline information is collected, participants are followed \"longitudinally\" i.e. new information is collected about them for a period of time afterward.",
    )
    minTypicalAge: Optional[int] = Field(
        None,
        title="Minimum Typical Age",
        description="Lower bound of typical participant age in whole years (healthdcatap:minTypicalAge).",
        ge=0,
    )
    maxTypicalAge: Optional[int] = Field(
        None,
        title="Maximum Typical Age",
        description="Upper bound of typical participant age in whole years (healthdcatap:maxTypicalAge).",
        le=150,
    )
    populationCoverage: Optional[str] = Field(
        None,
        title="Population Coverage",
        description="Description of the population covered by the dataset (healthdcatap:populationCoverage).",
    )
    numberOfUniqueIndividuals: Optional[int] = Field(
        None,
        title="Number of Unique Individuals",
        description="Count of unique individuals in the dataset (healthdcatap:numberOfUniqueIndividuals).",
        ge=0,
    )
    numberOfRecords: Optional[int] = Field(
        None,
        title="Number of Records",
        description="Total row/record count in the dataset (healthdcatap:numberOfRecords).",
        ge=0,
    )
    datasetCompleteness: Optional[str] = Field(
        None,
        title="Dataset coverage/completeness/quality",
        description="Completeness description or percentage for the dataset.",
        examples=["https://bhfdatasciencecentre.org/dashboard/"],
    )
