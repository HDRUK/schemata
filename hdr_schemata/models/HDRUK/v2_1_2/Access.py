from typing import Optional, List, Union
from pydantic import BaseModel, Field, constr
from hdr_schemata.definitions.HDRUK import *

from hdr_schemata.annotations import annotations

an = annotations.HDRUK.v2p1p2.accessibility.access


class Access(BaseModel):
    class Config:
        extra = "forbid"

    accessRights: Optional[LongDescription] = Field(..., **an.accessRights.__dict__)

    accessService: Optional[LongDescription] = Field(None, **an.accessService.__dict__)
    accessRequestCost: Optional[
        Union[Optional[LongDescription], List[Optional[Url]]]
    ] = Field(None, **an.accessRequestCost.__dict__)
    deliveryLeadTime: Optional[DeliveryLeadTime] = Field(
        None, **an.deliveryLeadTime.__dict__
    )
    jurisdiction: Union[Optional[CommaSeparatedValues], List[Isocountrycode]] = Field(
        ..., **an.jurisdiction.__dict__
    )
    dataController: Optional[LongDescription] = Field(..., **an.dataController.__dict__)
    dataProcessor: Optional[LongDescription] = Field(None, **an.dataProcessor.__dict__)
