from typing import Optional
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr
from hdr_schemata.definitions.HDRUK import *


from .annotations import annotations

an = annotations.summary.publisher


class Publisher(BaseModel):

    publisherName: Optional[Name] = Field(..., **an.publisherName.__dict__)

    # note: will need to do something about this in the future
    #      should match a pattern? sha256? integer?
    publisherGatewayId: Optional[constr(min_length=2, max_length=50)] = Field(
        None, **an.publisherGatewayId.__dict__
    )
