from typing import Optional, Union, List
from pydantic import Field, constr, BaseModel

from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.summary.organisation

class Organisation(BaseModel):
    class Config:
        extra = "forbid"

    identifier: Union[constr(min_length=2, max_length=50), int] = Field(
        ..., **an.identifier.__dict__, json_schema_extra={"guidance": an.identifier.guidance}
    )

    name: OneHundredFiftyCharacters = Field(
        ...,
        **an.name.__dict__,
        json_schema_extra={"guidance": an.name.guidance}
    )

    logo: Optional[Url] = Field(
        None,
        **an.logo.__dict__,
    )

    description: Optional[Description] = Field(
        None,
        **an.description.__dict__,
    )

    contactPoint: Union[EmailAddress, List[EmailAddress]] = Field(
        ...,
        **an.contactPoint.__dict__
    )

    memberOf: Optional[MemberOfV2] = Field(
        None,
        **an.memberOf.__dict__,
    )    
