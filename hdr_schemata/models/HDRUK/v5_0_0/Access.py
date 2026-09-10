from typing import List, Optional

from pydantic import BaseModel, Field

from hdr_schemata.definitions.HDRUK import (
    AccessService,
    DeliveryLeadTimeV2,
    Isocountrycode,
    LongDescription,
)


class Access(BaseModel):
    class Config:
        extra = "forbid"

    accessRights: LongDescription = Field(
        ...,
        title="Access Rights",
        description="A URL or description of the conditions under which the dataset can be accessed (dcterms:accessRights).",
    )

    accessServiceCategory: Optional[AccessService] = Field(
        None,
        title="Access Service Category",
        description="Categorisation of the access service type available for this dataset.",
    )

    accessService: Optional[LongDescription] = Field(
        None,
        title="Access Service",
        description="A link or description of the service used to access the dataset (dcat:accessService).",
    )

    accessRequestCost: Optional[LongDescription] = Field(
        None,
        title="Access Request Cost",
        description="Indication of any costs associated with accessing the dataset (healthdcatap:accessRequestCost).",
    )

    deliveryLeadTime: Optional[DeliveryLeadTimeV2] = Field(
        None,
        title="Delivery Lead Time",
        description="Typical time between submitting an access request and receiving data access (healthdcatap:deliveryLeadTime).",
    )

    jurisdiction: Optional[List[Isocountrycode]] = Field(
        None,
        title="Jurisdiction",
        description="ISO 3166-2 country/region code(s) indicating where the data controller is legally registered.",
    )

    dataController: Optional[LongDescription] = Field(
        None,
        title="Data Controller",
        description="Organisation that determines the purposes and means of processing personal data (dpv:hasDataController).",
    )

    dataProcessor: Optional[LongDescription] = Field(
        None,
        title="Data Processor",
        description="Organisation that processes personal data on behalf of the data controller (dpv:hasDataProcessor).",
    )

    legalBasis: Optional[str] = Field(
        None,
        title="Legal Basis",
        description="Legal basis under which personal data in this dataset is processed (dpv:hasLegalBasis). Reference the relevant legislation or DPV concept, e.g. 'GDPR Art.9(2)(j) - scientific research'.",
    )

    applicableLegislation: Optional[str] = Field(
        None,
        title="Applicable Legislation",
        description="Legislation governing the access and use of this dataset (dcatap:applicableLegislation), e.g. 'UK GDPR', 'Health and Social Care (Safety and Quality) Act 2015'.",
    )

    personalData: Optional[str] = Field(
        None,
        title="Personal Data",
        description="Description of the categories of personal data held in the dataset (dpv:hasPersonalData). Reference DPV personal data categories or describe the types of identifiers and sensitive data present.",
    )
