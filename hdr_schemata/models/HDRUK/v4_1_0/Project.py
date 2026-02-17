from __future__ import annotations

from datetime import date, datetime
from typing import Optional, Union

from pydantic import BaseModel, Field, constr

from hdr_schemata.definitions.HDRUK import OneHundredFiftyCharacters

from .LineSeparatedValues import LineSeparatedValues


class Project(BaseModel):
    class Config:
        extra = "forbid"

    projectName: Optional[OneHundredFiftyCharacters] = Field(
        None,
        title="Project Title",
        description="May or may not be different to the Dataset Title",
    )

    leadResearcher: Optional[OneHundredFiftyCharacters] = Field(
        None,
        title="Lead Researcher",
        description="",
        examples=["Dr Smith"],
    )

    leadResearchInstitute: Optional[OneHundredFiftyCharacters] = Field(
        None,
        title="Lead Research Institute",
        description="",
        examples=["Sussex University"],
    )

    grantNumbers: Optional[LineSeparatedValues] = Field(
        None,
        title="Grant number(s)",
        description="List of grant numbers separated by a line break",
        examples=["A354t", "ropguadg"],
        json_schema_extra={"guidance": "Normally specified on the grant acceptance letter"},
    )

    projectStartDate: Optional[Union[date, datetime]] = Field(
        None,
        title="Project Start Date",
        description="Starting date of project grant.",
        json_schema_extra={
            "guidance": (
                "Date on which the dataset project starts. This is normally set out in the "
                "grant contract and will be different from the start of any data collection"
            )
        },
    )

    projectEndDate: Optional[Union[date, datetime]] = Field(
        None,
        title="Project End Date",
        description="Current end date of project grant.",
        json_schema_extra={
            "guidance": (
                "Date on which the dataset project is currently projected to finish. This is "
                "normally set out in the grant contract and will be different from the end of "
                "any data collection"
            )
        },
    )

    projectScope: Optional[constr(min_length=5, max_length=500)] = Field(
        None,
        title="Project Scope",
        description="data and biospecimens expected to result from the grant.",
        examples=["Longitudinal genomic data including somatic mutations"],
        json_schema_extra={
            "guidance": (
                "Short paragraph setting out the types of data / biospecimens likely to result "
                "from the grant and the cancers covered"
            )
        },
    )
