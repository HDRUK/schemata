from typing import Optional, List
from pydantic import Field
from hdr_schemata.definitions.HDRUK import *

from hdr_schemata.models.HDRUK.v2_2_1.Access import Access as BaseAccess


from .annotations import annotations

an = annotations.accessibility.access


class Access(BaseAccess):
    accessRights: LongDescription = Field(..., **an.accessRights.__dict__)

    accessService: Optional[LongDescription] = Field(None, **an.accessService.__dict__)
    
    accessRequestCost: Optional[LongDescription] = Field(None, **an.accessRequestCost.__dict__)
    
    deliveryLeadTime: Optional[DeliveryLeadTimeV2] = Field(
        None, **an.deliveryLeadTime.__dict__
    )

    accessServiceCategory: Optional[AccessService] = Field(
        None, **an.accessServiceCategory.__dict__
    )

    accessMode: Optional[AccessMode] = Field(
        "New project", **an.accessMode.__dict__
    )