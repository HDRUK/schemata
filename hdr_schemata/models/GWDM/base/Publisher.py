from typing import Optional
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr
from hdr_schemata.definitions.HDRUK import *


class Publisher(BaseModel):

    publisherName: Optional[Name] = Field(
        ...,
        title='Publisher name'
    )

    #note: will need to do something about this in the future
    #      should match a pattern? sha256? integer?
    publisherGatewayId: Optional[constr(min_length=2,max_length=50)] = Field(
        None,
        title='Publisher gateway id'
    )
