from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr
from hdr_schemata.definitions.HDRUK import *


class Revision(BaseModel):

    version: constr(min_length=2,max_length=100) = Field(
        ...,
        title='revision version'
    )

    version: Url = Field(
        ...,
        title='revision url'
    )
