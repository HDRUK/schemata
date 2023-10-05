from typing import Optional
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr
from hdr_schemata.definitions.HDRUK import *


class Publisher(BaseModel):

    publisherName: Optional[Name] = Field(
        ...,
        description="The organisation responsible for running or supporting the data access request process, as well as publishing and maintaining the metadata. In most this will be the same as the HDR UK Organisation (Hub or Alliance Member)/",
        example="SAIL",
        title='Publisher name'
    )

    #note: will need to do something about this in the future
    #      should match a pattern? sha256? integer?
    publisherGatewayId: Optional[constr(min_length=2,max_length=50)] = Field(
        None,
        description="The link to an ID somewhere in the gateway where more information on the publisher can be retrieved.",
        title='Publisher gateway id'
    )
