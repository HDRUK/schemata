from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .Organisation import Organisation


class Summary(BaseModel):
    class Config:
        extra = "forbid"

    title: OneHundredFiftyCharacters = Field(
        ...,
        description="Title of the dataset limited to 150 characters. It should provide a short description of the dataset and be unique across the gateway. If your title is not unique, please add a prefix with your organisation name or identifier to differentiate it from other datasets within the Gateway. Please avoid acronyms wherever possible. Good titles should summarise the content of the dataset and if relevant, the region the dataset covers.",
        examples=[["North West London COVID-19 Patient Level Situation Report"]],
        title="Title",
    )
    abstract: Optional[AbstractText] = Field(
        ...,
        description="Provide a clear and brief descriptive signpost for researchers who are searching for data that may be relevant to their research. The abstract should allow the reader to determine the scope of the data collection and accurately summarise its content. The optimal length is one paragraph (limited to 255 characters) and effective abstracts should avoid long sentences and abbreviations where possible",
        examples=[
            "CPRD Aurum contains primary care data contributed by General Practitioner (GP) practices using EMIS Web® including patient registration information and all care events that GPs have chosen to record as part of their usual medical practice."
        ],
        title="Dataset Abstract",
    )
    publisher: Organisation = Field(
        ...,
        description="This is the organisation responsible for running or supporting the data access request process, as well as publishing and maintaining the metadata. In most this will be the same as the HDR UK Organisation (Hub or Alliance Member). However, in some cases this will be different i.e. Tissue Directory are an HDR UK Gateway organisation but coordinate activities across a number of data publishers i.e. Cambridge Blood and Stem Cell Biobank.",
        title="Dataset publisher",
    )
    contactPoint: Optional[EmailAddress] = Field(
        ...,
        description="Please provide a valid email address that can be used to coordinate data access requests with the publisher. Organisations are expected to provide a dedicated email address associated with the data access request process. Notes- An employee's email address can only be provided on a temporary basis and if one is provided an explicit consent must be obtained for this purpose. Gateway Feature: If no contact point is provided in this field, this field will be defaulted to the teams support email provided in the teams setting.",
        examples=["SAILDatabank@swansea.ac.uk"],
        title="Contact Point",
    )
    keywords: Union[Optional[CommaSeparatedValues], List[OneHundredFiftyCharacters]] = (
        Field(
            ...,
            description="Please provide relevant and specific keywords that can improve the SEO of your dataset as a comma separated list. Notes: Onboarding portal will suggest keywords based on title, abstract and description. We are compiling a standardised list of keywords and synonyms across datasets to make filtering easier for users.",
            title="Keywords",
        )
    )
    alternateIdentifiers: Optional[
        Union[Optional[CommaSeparatedValues], List[Optional[ShortDescription]]]
    ] = Field(
        None,
        description="Alternate dataset identifiers or local identifiers",
        title="Alternate dataset identifiers",
    )
    doiName: Optional[Doi] = Field(
        None,
        description="Please provide the DOI for the dataset (Not the DOI for the metadata of the dataset)",
        examples=["10.3399/bjgp17X692645"],
        title="Digital Object Identifier",
    )
