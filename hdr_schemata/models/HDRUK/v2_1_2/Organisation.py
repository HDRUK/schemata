from typing import Optional, Union, List
from pydantic import BaseModel, Field

from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.organisation


class Organisation(BaseModel):
    class Config:
        extra = "forbid"

    identifier: Optional[Url] = Field(None, **an.identifier.__dict__)

    name: OneHundredFiftyCharacters = Field(
        ...,
        **an.name.__dict__,
    )

    logo: Optional[Url] = Field(
        None,
        **an.logo.__dict__,
    )

    description: Optional[Description] = Field(
        None,
        **an.description.__dict__,
    )

    contactPoint: Union[Optional[EmailAddress], List[Optional[EmailAddress]]] = Field(
        ...,
        **an.contactPoint.__dict__,
    )

    memberOf: Optional[MemberOf] = Field(
        None,
        **an.memberOf.__dict__,
    )
