from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

from hdr_schemata.definitions.HDRUK import *
from .Revision import Revision

from .annotations import annotations

an = annotations.required


class Required(BaseModel):
    gatewayId: int = Field(..., description=an.gatewayId.description, title=an.gatewayId.title)

    gatewayPid: constr(min_length=2, max_length=50) = Field(
        ..., description=an.gatewayPid.description, title=an.gatewayPid.title
    )
    issued: datetime = Field(
        ..., description=an.issued.description, title=an.issued.title
    )
    modified: datetime = Field(
        ..., description=an.modified.description, title=an.modified.title
    )
    revisions: List[Revision] = Field(
        ..., description=an.revisions.description, title=an.revisions.title
    )
    version: constr(
        pattern=r"^\d+\.\d+\.\d+$",
    ) = Field(..., **an.version.__dict__)
