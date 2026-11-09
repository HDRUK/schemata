from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.accessibility.access


class Access(BaseModel):
    class Config:
        extra = "forbid"

    accessRights: LongDescription = Field(
        ..., **an.accessRights.__dict__, json_schema_extra={"guidance": an.accessRights.guidance}
    )

    accessServiceCategory: Optional[AccessService] = Field(
        None, 
        **an.accessServiceCategory.__dict__, 
        json_schema_extra={"guidance": an.accessServiceCategory.guidance}
    )

    accessService: Optional[LongDescription] = Field(
        None, **an.accessService.__dict__, json_schema_extra={"guidance": an.accessService.guidance}
    )
    
    accessRequestCost: Optional[LongDescription] = Field(
        None, **an.accessRequestCost.__dict__, json_schema_extra={"guidance": an.accessRequestCost.guidance}
    )
    
    deliveryLeadTime: Optional[DeliveryLeadTimeV2] = Field(
        None, **an.deliveryLeadTime.__dict__, json_schema_extra={"guidance": an.deliveryLeadTime.guidance}
    )

    jurisdiction: Optional[List[Isocountrycode]] = Field(
        None, **an.jurisdiction.__dict__, json_schema_extra={"guidance": an.jurisdiction.guidance}
    )
    
    dataController: Optional[LongDescription] = Field(
        None, **an.dataController.__dict__, json_schema_extra={"guidance": an.dataController.guidance}
    )
    
    dataProcessor: Optional[LongDescription] = Field(
        None, **an.dataProcessor.__dict__, json_schema_extra={"guidance": an.dataProcessor.guidance}
    )
    