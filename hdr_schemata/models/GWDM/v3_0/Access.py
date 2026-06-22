from typing import Optional

from pydantic import BaseModel, Field

from hdr_schemata.definitions.HDRUK import (
    CommaSeparatedValues,
    DeliveryLeadTimeV2,
    LongDescription,
)
from hdr_schemata.models.GWDM.v2_0.annotations import annotations as v20_an

an = v20_an.accessibility.access


class Access(BaseModel):
    class Config:
        extra = "forbid"

    accessRights: Optional[CommaSeparatedValues] = Field(
        None, **an.accessRights.__dict__
    )
    accessService: Optional[LongDescription] = Field(None, **an.accessService.__dict__)
    accessRequestCost: Optional[LongDescription] = Field(
        None, **an.accessRequestCost.__dict__
    )
    deliveryLeadTime: Optional[DeliveryLeadTimeV2] = Field(
        None, **an.deliveryLeadTime.__dict__
    )
    jurisdiction: Optional[CommaSeparatedValues] = Field(
        None, **an.jurisdiction.__dict__
    )
    dataController: Optional[LongDescription] = Field(
        None, **an.dataController.__dict__
    )
    dataProcessor: Optional[LongDescription] = Field(
        None, **an.dataProcessor.__dict__
    )
    accessServiceCategory: Optional[CommaSeparatedValues] = Field(
        None, **an.accessServiceCategory.__dict__
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
