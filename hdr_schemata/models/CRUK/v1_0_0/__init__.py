import json
from typing import List, Literal, Optional

from pydantic import BaseModel, Field, constr

from hdr_schemata.definitions.HDRUK import (
    Format,
    OneHundredFiftyCharacters,
    ShortDescription,
    Url,
)
from hdr_schemata.models.HDRUK.v4_0_0 import Hdruk400


class DatasetFilter(BaseModel):
    class Config:
        extra = "forbid"

    id: constr(pattern=r"(\d+_){0,5}\d+") = Field(..., title="Id")
    label: constr(min_length=0, max_length=150) = Field(..., title="Label")
    category: constr(min_length=0, max_length=150) = Field(..., title="Category")
    primaryGroup: Literal["cancer-type", "data-type", "access-type"] = Field(
        ..., title="Primary group"
    )
    description: constr(min_length=0, max_length=150) = Field(..., title="Description")


class DataTable(BaseModel):
    class Config:
        extra = "forbid"

    size: Optional[int] = Field(
        None,
        title="Table size",
        description="Number of Complete Entries.",
        json_schema_extra={
            "guidance": (
                "Provides a measure of the completeness of the data set. A row which includes n/a against "
                "columns that are not relevant or not applicable should still be counted as complete."
            )
        },
    )


class OtherDataType(BaseModel):
    class Config:
        extra = "forbid"

    title: OneHundredFiftyCharacters = Field(
        ...,
        title="Title",
        json_schema_extra={"guidance": "Short descriptive titles"},
        examples=["Mammograms", "Patient recordings"],
    )
    description: ShortDescription = Field(
        ...,
        title="Data description",
        json_schema_extra={"guidance": "A description of the data type."},
        examples=[
            "2D images of both normal and malignant breasts",
            "audio-tapes of oncology consultations",
        ],
    )
    format: Format = Field(
        ...,
        title="Format",
        description="Format drawn from https://www.iana.org/assignments/media-types/media-types.xhtml.",
        json_schema_extra={
            "guidance": (
                "https://www.iana.org/assignments/media-types/media-types.xhtml lists the commonly used "
                "formats for different media (such as video/image/audio) etc. If your format is not "
                "included in the list set out there, please indicate other and specify in the description."
            )
        },
    )


class ProjectGrant(BaseModel):
    pid: Optional[OneHundredFiftyCharacters] = Field(
        None,
        title="Persistent identifier of the study",
    )
    projectGrantName: OneHundredFiftyCharacters = Field(
        ...,
        title="Project Grant Title",
        description=(
            "The Project Grant Title should be unique to the CRUK datahub. "
            "(Add your institute or name if necessary to disambiguate."
        ),
    )
    leadResearcher: OneHundredFiftyCharacters = Field(
        ...,
        title="Lead Researcher",
        examples=["Dr Smith"],
    )
    leadResearchInstitute: OneHundredFiftyCharacters = Field(
        ...,
        title="Lead Research Institute",
        examples=["Sussex University"],
    )
    grantNumber: str = Field(
        ...,
        title="Grant number(s)",
        description="List of CRUK and any other grant numbers.",
        examples=["ABC123"],
        json_schema_extra={"guidance": "Normally specified on the grant acceptance letter"},
    )
    projectGrantStartDate: str = Field(
        ...,
        title="Project Start Date",
        description="Starting date of projectGrant grant.",
        json_schema_extra={
            "guidance": (
                "Date on which the dataset projectGrant starts. This is normally set out in the grant "
                "contract and will be different from the start of any data collection"
            )
        },
    )
    projectGrantEndDate: Optional[str] = Field(
        ...,
        title="Project End Date",
        description="Current end date of project grant.",
        json_schema_extra={
            "guidance": (
                "Date on which the dataset project is currently projected to finish. This is normally set "
                "out in the grant contract and will be different from the end of any data collection"
            )
        },
    )
    projectGrantScope: Optional[constr(min_length=5, max_length=500)] = Field(
        None,
        title="Project Scope",
        description="data and biospecimens expected to result from the grant.",
        examples=["Longitudinal genomic data including somatic mutations"],
        json_schema_extra={
            "guidance": (
                "Short paragraph setting out the types of data / biospecimens likely to result from the "
                "grant and the cancers covered"
            )
        },
    )


class Cruk100(Hdruk400):
    class Config:
        extra = "forbid"

    datasetFilters: Optional[List[DatasetFilter]] = Field(
        None,
        title="Dataset Filters",
    )
    icons: Optional[List[str]] = Field(
        None,
        title="Icons",
        description="Calculated categorization icons added during export.",
    )
    erd: Optional[Url] = Field(
        None,
        title="Entity Relationship Diagram",
        description="Visual representation of data table relationships.",
        json_schema_extra={
            "guidance": (
                "Please upload an image file (max 5MB) showing the relationship between the different tables"
            )
        },
    )
    projectGrants: Optional[List[ProjectGrant]] = Field(
        None,
        title="Associated Project Grants",
    )
    otherDataTypes: Optional[List[OtherDataType]] = Field(
        None,
        title="Other data types",
    )

    @classmethod
    def save_schema(cls, location: str = "./1.0.0/schema.json") -> None:
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)

