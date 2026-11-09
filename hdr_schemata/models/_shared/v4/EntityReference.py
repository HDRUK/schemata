from typing import Optional
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.entityReference


class EntityReference(BaseModel):
    class Config:
        extra = "forbid"

    # Text only: an integer/string union breaks under AJV's coerceTypes (null is
    # coerced to 0 then "0"), so numeric Gateway ids are carried as strings.
    gatewayId: Optional[OneHundredFiftyCharacters] = Field(
        None, **an.gatewayId.__dict__
    )

    title: TwoHundredFiftyFiveCharacters = Field(..., **an.title.__dict__)

    url: Optional[Url] = Field(None, **an.url.__dict__)
