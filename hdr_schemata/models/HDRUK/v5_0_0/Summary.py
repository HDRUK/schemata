from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, Field

from hdr_schemata.definitions.HDRUK import (
    AbstractText,
    CommaSeparatedValues,
    Doi,
    EmailAddress,
    OneHundredFiftyCharacters,
    ShortDescription,
    ShortTitle,
    Url,
)

from .Creator import Creator
from .Organisation import Organisation


class Summary(BaseModel):
    class Config:
        extra = "forbid"

    title: OneHundredFiftyCharacters = Field(
        ...,
        title="Title",
        description="Full title of the dataset.",
    )

    abstract: AbstractText = Field(
        ...,
        title="Abstract",
        description="Concise description of the dataset, its purpose, and the data it contains.",
    )

    dataCustodian: Organisation = Field(
        ...,
        title="Data Custodian",
        description="The organisation responsible for managing access to this dataset (dcterms:publisher).",
    )

    populationSize: int = Field(
        ...,
        title="Population Size",
        description="Approximate number of unique individuals represented in the dataset.",
    )

    contactPoint: EmailAddress = Field(
        ...,
        title="Contact Point",
        description="Primary email address for enquiries about this dataset (dcat:contactPoint).",
    )

    keywords: Optional[List[OneHundredFiftyCharacters]] = Field(
        None,
        title="Keywords",
        description="Free-text keywords describing the dataset content (dcat:keyword).",
    )

    doiName: Optional[Doi] = Field(
        None,
        title="DOI Name",
        description="Digital Object Identifier for this dataset (dcterms:identifier).",
    )

    datasetAliases: Optional[Union[CommaSeparatedValues, List[ShortDescription]]] = Field(
        None,
        title="Dataset Aliases",
        description="Alternative names or acronyms for the dataset (dcterms:alternative).",
    )

    shortTitle: Optional[ShortTitle] = Field(
        None,
        title="Short Title",
        description="Abbreviated or acronym title for the dataset, used in list/card views (dcterms:alternative).",
    )

    licenseUrl: Optional[Url] = Field(
        None,
        title="Licence URL",
        description="URI of the dataset-level licence (dct:license). Use a recognised licence URI such as https://creativecommons.org/licenses/by/4.0/.",
    )

    landingPage: Optional[Url] = Field(
        None,
        title="Landing Page",
        description="URL of a human-readable landing page for the dataset (dcat:landingPage).",
    )

    creator: Optional[Creator] = Field(
        None,
        title="Creator",
        description="Entity responsible for originally creating the dataset (dct:creator). May differ from the data custodian.",
    )

    theme: Optional[List[AnyUrl]] = Field(
        None,
        title="Theme",
        description="Array of controlled vocabulary concept URIs categorising the dataset by subject area (dcat:theme). Use EuroVoc or NHS Data Dictionary URIs where available.",
    )

    controlledKeywords: Optional[CommaSeparatedValues] = Field(
        None,
        title="Controlled Keywords",
        description="Curated subset of keywords drawn from a controlled vocabulary. Complements free-text keywords.",
    )
