from typing import Optional
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.organisation


class Organisation(BaseModel):
    name: Optional[Name] = Field(None, **an.name.__dict__)

    gatewayId: Optional[constr(min_length=2, max_length=50)] = Field(
        None, **an.gatewayId.__dict__
    )

    rorId: Optional[constr(min_length=9, max_length=9)] = Field(
        None, **an.rorId.__dict__
    )
