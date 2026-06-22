from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field

from hdr_schemata.definitions.HDRUK import (
    CommaSeparatedValues,
    Doi,
    LongAbstractText,
    LongDescription,
    Pipeline,
    ShortTitle,
    TwoHundredFiftyFiveCharacters,
)
from hdr_schemata.models.GWDM.v2_0.Organisation import Organisation
from hdr_schemata.models.GWDM.v2_0.annotations import annotations as v20_an

from .Creator import Creator

an = v20_an.summary


class Summary(BaseModel):
    class Config:
        extra = "forbid"

    title: TwoHundredFiftyFiveCharacters = Field(..., **an.title.__dict__)
    shortTitle: Optional[ShortTitle] = Field(None, **an.shortTitle.__dict__)
    doiName: Optional[Doi] = Field(None, **an.doiName.__dict__)
    abstract: LongAbstractText = Field(..., **an.abstract.__dict__)
    keywords: Optional[CommaSeparatedValues] = Field(None, **an.keywords.__dict__)
    controlledKeywords: Optional[CommaSeparatedValues] = Field(
        None, **an.controlledKeywords.__dict__
    )
    contactPoint: Optional[EmailStr] = Field(None, **an.contactPoint.__dict__)
    datasetType: Optional[CommaSeparatedValues] = Field(None, **an.datasetType.__dict__)
    datasetSubType: Optional[CommaSeparatedValues] = Field(
        None, **an.datasetSubType.__dict__
    )
    description: Optional[LongDescription] = Field(None, **an.description.__dict__)
    publisher: Optional[Organisation] = Field(
        None,
        description=an.publisher.description,
        title=an.publisher.title,
    )
    populationSize: Optional[int] = Field(None, **an.populationSize.__dict__)
    inPipeline: Optional[Pipeline] = Field("Not available", **an.inPipeline.__dict__)
    funders: Optional[CommaSeparatedValues] = Field(
        None,
        title="Funded by",
        description="Comma-separated list of funders for this dataset.",
    )
    licenseUrl: Optional[str] = Field(
        None,
        title="Licence URL",
        description="URI of the dataset-level licence (dct:license).",
    )
    landingPage: Optional[str] = Field(
        None,
        title="Landing Page",
        description="URL of a human-readable landing page for the dataset (dcat:landingPage).",
    )
    creator: Optional[Creator] = Field(
        None,
        title="Creator",
        description="Entity responsible for creating the dataset (dct:creator).",
    )
    theme: Optional[List[str]] = Field(
        None,
        title="Theme",
        description="Array of controlled vocabulary URIs categorising the dataset (dcat:theme).",
    )
