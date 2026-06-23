from datetime import date, datetime
from typing import Optional, Union

from pydantic import BaseModel, Field

from hdr_schemata.definitions.HDRUK import Url


class Distribution(BaseModel):
    class Config:
        extra = "forbid"

    title: Optional[str] = Field(
        None,
        title="Distribution Title",
        description="Display name of this distribution (dct:title).",
    )
    description: Optional[str] = Field(
        None,
        title="Distribution Description",
        description="Human-readable description of this distribution (dct:description).",
    )
    accessUrl: Optional[Url] = Field(
        None,
        title="Access URL",
        description="URL of a resource that gives access to the distribution (dcat:accessURL). May point to a data service or landing page.",
    )
    downloadUrl: Optional[Url] = Field(
        None,
        title="Download URL",
        description="Direct URL to download the distribution file (dcat:downloadURL).",
    )
    mediaType: Optional[str] = Field(
        None,
        title="Media Type",
        description="IANA media type of the distribution, e.g. text/csv, application/json (dcat:mediaType).",
    )
    format: Optional[str] = Field(
        None,
        title="Format",
        description="File format label of the distribution, e.g. CSV, Parquet (dct:format).",
    )
    byteSize: Optional[int] = Field(
        None,
        title="Byte Size",
        description="Size of the distribution in bytes (dcat:byteSize).",
        ge=0,
    )
    licenseUrl: Optional[Url] = Field(
        None,
        title="Licence URL",
        description="Licence URI for this specific distribution; overrides the dataset-level licence if provided (dct:license).",
    )
    accessService: Optional[str] = Field(
        None,
        title="Access Service",
        description="Data service that provides access to this distribution (dcat:accessService).",
    )
    issued: Optional[Union[date, datetime]] = Field(
        None,
        title="Issued",
        description="Date this distribution was first published (dct:issued).",
    )
    modified: Optional[Union[date, datetime]] = Field(
        None,
        title="Modified",
        description="Date this distribution was last modified (dct:modified).",
    )
