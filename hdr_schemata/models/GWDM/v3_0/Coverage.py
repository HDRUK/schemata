from typing import Optional

from pydantic import BaseModel, Field

from hdr_schemata.definitions.HDRUK import CommaSeparatedValues, FollowupV2, LongDescription
from hdr_schemata.models.GWDM.v2_0.annotations import annotations as v20_an

an = v20_an.coverage


class Coverage(BaseModel):
    class Config:
        extra = "forbid"

    spatial: Optional[CommaSeparatedValues] = Field(None, **an.spatial.__dict__)
    pathway: Optional[LongDescription] = Field(None, **an.pathway.__dict__)
    followUp: Optional[FollowupV2] = Field(None, **an.followUp.__dict__)
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
        title=an.datasetCompleteness.title,
        description="Completeness description or percentage for the dataset.",
    )
