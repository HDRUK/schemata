from typing import Optional, List, Union
from pydantic import BaseModel, Field, constr
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.accessibility.access


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

    dataController: Optional[LongDescription] = Field(None, **an.dataController.__dict__)

    dataProcessor: Optional[LongDescription] = Field(None, **an.dataProcessor.__dict__)

    accessServiceCategory: Optional[CommaSeparatedValues] = Field(
        None, **an.accessServiceCategory.__dict__
    )
