from typing import Optional, List, Union
from pydantic import BaseModel, Field, constr
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.accessibility.access


class Access(BaseModel):
    class Config:
        extra = "forbid"

    # note: do we want to make this CommaSeparatedValues of URLs?
    #      dont allow a description of the license?
    accessRights: Optional[CommaSeparatedValues] = Field(
        ..., **an.accessRights.__dict__
    )

    # note: do we want to limit these to actual accessibly service objects?
    #      e.g.: Optional[AccessServiceEnum]
    #      options: [SAIL,HIC,DARE,...,OTHER]
    #
    # note: do we want to include something accessServiceType (?)
    #      options: [TRE, SDE, University, SafeHaven, ... ]
    accessService: Optional[LongDescription] = Field(None, **an.accessService.__dict__)

    # note: as above... having a long description seems odd to me...
    #      we could associate this with an Optional[AccessService]
    #      class AccessService(BaseModel):
    #            serviceName: ShortTitle
    #            serviceDescription: LongDescription
    #            cost: 'free'|'paid'|'other'
    #            timeToAcess: DeliveryLeadTime
    accessRequestCost: Optional[LongDescription] = Field(
        None, **an.accessRequestCost.__dict__
    )

    # note: related to above... this is hard to know or guess..
    #      not useful to a researcher as they can tell this is made up...
    #      may remove or class as a 'AccessService'
    deliveryLeadTime: Optional[DeliveryLeadTime] = Field(
        None, **an.deliveryLeadTime.__dict__
    )

    # note: May want to make this a CommaSeparetedListIsoCountryCode
    #       e.g. GB-XXX
    jurisdiction: Optional[CommaSeparatedValues] = Field(
        ..., **an.jurisdiction.__dict__
    )

    # note: this could also be associated with the AccessService?
    #      could the dataController not be the TRE for example?
    #      terminology could be confusing here...
    dataController: Optional[LongDescription] = Field(..., **an.dataController.__dict__)

    # note: as with dataController-- what does this mean?
    #      are these often different?
    dataProcessor: Optional[LongDescription] = Field(None, **an.dataProcessor.__dict__)
