from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr
from hdr_schemata.definitions.HDRUK import *
from typing import Optional

from .annotations import annotations

an = annotations.revisions


class Revision(BaseModel):

    version: constr(min_length=2, max_length=100) = Field(
        ...,
        **an.version.__dict__,
    )

    url: Optional[Url] = Field(
        ...,
        **an.url.__dict__,
    )
