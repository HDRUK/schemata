from hdr_schemata.models.GWDM.v1_0 import Required as BaseRequired
from typing import Optional
from pydantic import Field, constr


class Required(BaseRequired):
    version: constr(min_length=3, max_length=4) = Field(
        ...,
        description="Dataset metadata version",
        examples=["1.1.0"],
        title="Dataset Version",
    )
