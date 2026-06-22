from datetime import date, datetime
from typing import Optional, Union
from pydantic import BaseModel, Field


class Distribution(BaseModel):
    class Config:
        extra = "forbid"

    title: Optional[str] = Field(
        None,
        title="Distribution Title",
        description="Display name of the distribution (dct:title).",
    )
    description: Optional[str] = Field(
        None,
        title="Distribution Description",
        description="Human-readable description of the distribution (dct:description).",
    )
    accessUrl: Optional[str] = Field(
        None,
        title="Access URL",
        description="URL to access the distribution (dcat:accessURL).",
    )
    downloadUrl: Optional[str] = Field(
        None,
        title="Download URL",
        description="Direct download URL for the distribution (dcat:downloadURL).",
    )
    mediaType: Optional[str] = Field(
        None,
        title="Media Type",
        description="IANA media type of the distribution, e.g. text/csv (dcat:mediaType).",
    )
    format: Optional[str] = Field(
        None,
        title="Format",
        description="File format label of the distribution (dct:format).",
    )
    byteSize: Optional[int] = Field(
        None,
        title="Byte Size",
        description="Size of the distribution in bytes (dcat:byteSize).",
        ge=0,
    )
    licenseUrl: Optional[str] = Field(
        None,
        title="Licence URL",
        description="Distribution-level licence URI; overrides the dataset-level licence (dct:license).",
    )
    accessService: Optional[str] = Field(
        None,
        title="Access Service",
        description="Service providing access to this distribution (dcat:accessService).",
    )
    issued: Optional[Union[date, datetime]] = Field(
        None,
        title="Issued",
        description="Date the distribution was published (dct:issued).",
    )
    modified: Optional[Union[date, datetime]] = Field(
        None,
        title="Modified",
        description="Date the distribution was last modified (dct:modified).",
    )
