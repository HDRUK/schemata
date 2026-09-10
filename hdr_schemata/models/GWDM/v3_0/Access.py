from typing import List, Optional

from pydantic import BaseModel, Field

from hdr_schemata.definitions.HDRUK import (
    DeliveryLeadTimeV2,
    LongDescription,
)


class Access(BaseModel):
    class Config:
        extra = "forbid"

    accessRights: Optional[List[str]] = Field(
        None,
        title="Access rights",
        description="Please provide details for the data access rights.",
        examples=["In Progress"],
        json_schema_extra={
            "guidance": (
                "- The URL of a webpage where the data access request process and/or guidance is provided.\n"
                "- If such a resource or the underlying process doesn't exist, please provide \"In Progress\", until both the process and the documentation are ready."
            )
        },
    )
    accessService: Optional[LongDescription] = Field(
        None,
        title="Access service description",
        description="Please provide a brief description of the data access services that are available including: environment that is currently available to researchers; additional consultancy and services; any indication of costs associated. If no environment is currently available, please indicate the current plans and timelines when and how data will be made available to researchers.",
        examples=[
            "https://re-docs.genomicsengland.co.uk/tutorials/",
            "https://publichealthscotland.scot/services/data-research-and-innovation-services/electronic-data-research-and-innovation-service-edris/national-safe-haven-nsh/",
        ],
    )
    accessRequestCost: Optional[LongDescription] = Field(
        None,
        title="Access request cost",
        description="Please provide link(s) to a webpage or description detailing the service or cost model for processing data access requests.",
        json_schema_extra={
            "guidance": "This information should cover the costs and/or services available to different audiences (i.e. academic, commercial, non-UK, etc.). This can be in the form of text or a URL."
        },
    )
    deliveryLeadTime: Optional[DeliveryLeadTimeV2] = Field(
        None,
        title="Time to dataset access",
        description="Please provide an indication of the typical processing times based on the types of requests typically received.",
        json_schema_extra={
            "guidance": (
                "- **Less than 1 week**: Access request process typically processed in less than a week.\n"
                "- **1-2 weeks**: Access request process typically processed in one to two weeks.\n"
                "- **2-4 weeks**: Access request process typically processed in two to four weeks.\n"
                "- **1-2 months**: Access request process typically processed in one to two months.\n"
                "- **2-6 months**: Access request process typically processed in two to six months.\n"
                "- **More than 6 months**: Access request process typically processed in more than six months.\n"
                "- **Variable**: Access request lead time is variable.\n"
                "- **Not applicable**: Access request process duration is not applicable."
            )
        },
    )
    jurisdiction: Optional[List[str]] = Field(
        None,
        title="Jurisdiction",
        description="Please use country code from ISO 3166-1 country codes and the associated ISO 3166-2 for regions, cities, states etc. for the country/state under whose laws the data subjects' data is collected, processed and stored.",
        json_schema_extra={
            "guidance": "A full list of country codes can be found here (alpha-2 column): https://www.iso.org/obp/ui/#search/code/"
        },
    )
    dataController: Optional[LongDescription] = Field(
        None,
        title="Data Controller",
        description="Data Controller means a person/entity who (either alone or jointly or in common with other persons/entities) determines the purposes for which and the way any Data Subject data, specifically personal data or are to be processed.",
        examples=["NHS England"],
    )
    dataProcessor: Optional[LongDescription] = Field(
        None,
        title="Data Processor",
        description="A Data Processor, in relation to any Data Subject data, specifically personal data, means any person/entity (other than an employee of the data controller) who processes the data on behalf of the data controller.",
        examples=["Not Applicable", "SAIL"],
    )
    accessServiceCategory: Optional[List[str]] = Field(
        None,
        title="Access method category",
        description="The method a Researcher will use to access the dataset, if approved.",
        examples=["TRE/SDE"],
        json_schema_extra={
            "guidance": "Select the category which best matches how a Researcher will access the dataset, if approved for access."
        },
    )
    legalBasis: Optional[str] = Field(
        None,
        title="Legal Basis",
        description="Legal basis for processing personal data under this dataset (dpv:hasLegalBasis).",
    )
    personalData: Optional[str] = Field(
        None,
        title="Personal Data",
        description="Type of personal data held in the dataset (dpv:hasPersonalData).",
    )
    applicableLegislation: Optional[str] = Field(
        None,
        title="Applicable Legislation",
        description="Applicable legislation governing the dataset, e.g. GDPR, UK GDPR (dcatap:applicableLegislation).",
    )
