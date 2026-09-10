from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field

from hdr_schemata.definitions.HDRUK import (
    Doi,
    LongAbstractText,
    LongDescription,
    Pipeline,
    ShortTitle,
    TwoHundredFiftyFiveCharacters,
)

from .Creator import Creator
from .Organisation import Organisation


class Summary(BaseModel):
    class Config:
        extra = "forbid"

    title: TwoHundredFiftyFiveCharacters = Field(
        ...,
        title="Title",
        description="Title of the dataset limited to 150 characters. It should provide a short description of the dataset and be unique across the gateway. If your title is not unique, please add a prefix with your organisation name or identifier to differentiate it from other datasets within the Gateway. Good titles should summarise the content of the dataset and if relevant, the region the dataset covers.",
        examples=[
            "North West London COVID-19 Patient Level Situation Report",
            "Scottish Morbidity Record (SMR)",
        ],
        json_schema_extra={
            "guidance": (
                "- The **title** should provide a short description of the dataset and be **unique** across the gateway.\n"
                "- If your title is not unique, please **add a prefix with your organisation name or identifier** to differentiate it from other datasets within the Gateway.\n"
                "- Good titles should summarise the content of the dataset and if relevant, **the region the dataset covers**."
            )
        },
    )
    shortTitle: Optional[ShortTitle] = Field(
        None,
        title="Short Title",
        description="A shorter descriptive title of the dataset",
        examples=["ONS 2011 Census Wales (CENW)"],
    )
    doiName: Optional[Doi] = Field(
        None,
        title="Digital Object Identifier (DOI) for dataset",
        description="DOI associated to this dataset. Find out more about DOIs here: https://www.doi.org/the-identifier/what-is-a-doi/",
        examples=["10.1093/ije/dyx196"],
    )
    abstract: LongAbstractText = Field(
        ...,
        title="Dataset abstract",
        description="Provide a clear and brief descriptive signpost for researchers who are searching for data that may be relevant to their research. The abstract should allow the reader to determine the scope of the data collection and accurately summarise its content. The optimal length is one paragraph (limited to 255 characters) and effective abstracts should avoid long sentences and abbreviations where possible.",
        examples=[
            "CPRD Aurum contains primary care data contributed by General Practitioner (GP) practices using EMIS Web® including patient registration information and all care events that GPs have chosen to record as part of their usual medical practice."
        ],
    )
    keywords: Optional[List[str]] = Field(
        None,
        title="Keywords",
        description="Please provide a list of relevant and specific keywords that can improve the search engine optimisation (SEO) of your dataset as a comma separated list.",
        examples=["Outpatient Care", "Socioeconomic Deprivation", "Infant Morbidity"],
    )
    controlledKeywords: Optional[List[str]] = Field(
        None,
        title="Controlled Keywords",
        description="Keywords that have been filtered and limited",
    )
    datasetAliases: Optional[List[str]] = Field(
        None,
        title="Dataset Aliases",
        description="Alternative names or acronyms for the dataset.",
    )
    contactPoint: Optional[EmailStr] = Field(
        None,
        title="Contact point",
        description="Please provide a valid email address that can be used to coordinate data access requests.",
        examples=["gateway@hdruk.ac.uk"],
    )
    datasetType: Optional[List[str]] = Field(
        None,
        title="Dataset Type",
        description='Placeholder for dataset type"',
    )
    datasetSubType: Optional[List[str]] = Field(
        None,
        title="Dataset Sub-type",
        description="Placeholder for dataset sub-type",
    )
    description: Optional[LongDescription] = Field(
        None,
        title="Description",
        description="Longer description of the dataset in detail",
    )
    publisher: Optional[Organisation] = Field(
        None,
        title="Dataset publisher",
        description="This is the organisation responsible for running or supporting the data access request process, as well as publishing and maintaining the metadata.",
    )
    populationSize: Optional[int] = Field(
        None,
        title="Dataset population size",
        description="Input the number of people captured within the dataset.",
        examples=[1000],
    )
    inPipeline: Optional[Pipeline] = Field(
        "Not available",
        title="Dataset pipeline status",
        description="Indicate whether this dataset is currently available for Researchers to request access.",
    )
    funders: Optional[List[str]] = Field(
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
