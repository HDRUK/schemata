from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr
from hdr_schemata.definitions.HDRUK import *

from hdr_schemata.annotations import annotations

an = annotations.GWDM.v1p0.required.revisions


class Revision(BaseModel):

    version: constr(min_length=2, max_length=100) = Field(
        ...,
        **an.version.__dict__,
    )

    url: Url = Field(
        ...,
        **an.url.__dict__,
    )
