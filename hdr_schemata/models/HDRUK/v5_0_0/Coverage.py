from typing import Optional

from pydantic import Field

from hdr_schemata.models.HDRUK.v3_0_0.Coverage import Coverage as Coverage300


class Coverage(Coverage300):

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
