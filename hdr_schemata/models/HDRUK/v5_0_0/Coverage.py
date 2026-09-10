from typing import List, Optional, Union

from pydantic import BaseModel, Field

from hdr_schemata.definitions.HDRUK import (
    CommaSeparatedValues,
    Description,
    FollowupV2,
    MaterialTypeCategoriesV2,
    Url,
)


class Coverage(BaseModel):
    class Config:
        extra = "forbid"

    spatial: Union[CommaSeparatedValues, List[Url]] = Field(
        ...,
        title="Spatial Coverage",
        description="Geographic area(s) covered by the dataset (dcterms:spatial). Use GeoNames URIs or ISO country codes.",
    )

    typicalAgeRangeMin: Optional[int] = Field(
        None,
        title="Typical Age Range Min",
        description="Minimum age (in years) of individuals represented in the dataset.",
    )

    typicalAgeRangeMax: Optional[int] = Field(
        None,
        title="Typical Age Range Max",
        description="Maximum age (in years) of individuals represented in the dataset.",
    )

    datasetCompleteness: Optional[Url] = Field(
        None,
        title="Dataset Completeness",
        description="URL to a completeness assessment report for this dataset.",
    )

    materialType: Optional[List[MaterialTypeCategoriesV2]] = Field(
        None,
        title="Material Type",
        description="Type(s) of biological material covered by the dataset.",
    )

    followUp: Optional[FollowupV2] = Field(
        "Unknown",
        title="Follow Up",
        description="Typical follow-up period for individuals in the dataset.",
    )

    pathway: Optional[Description] = Field(
        None,
        title="Pathway",
        description="Description of any clinical pathway or care pathway documented in the dataset.",
    )

    populationCoverage: Optional[str] = Field(
        None,
        title="Population Coverage",
        description="Plain-text description of the population represented in the dataset (healthdcatap:populationCoverage). Include demographic scope, inclusion/exclusion criteria, and geographic focus where applicable.",
    )

    numberOfUniqueIndividuals: Optional[int] = Field(
        None,
        title="Number of Unique Individuals",
        description="Count of unique individuals (patients, participants) represented in the dataset (healthdcatap:numberOfUniqueIndividuals).",
        ge=0,
    )

    numberOfRecords: Optional[int] = Field(
        None,
        title="Number of Records",
        description="Total number of rows or records in the dataset (healthdcatap:numberOfRecords). May exceed numberOfUniqueIndividuals for longitudinal datasets.",
        ge=0,
    )
