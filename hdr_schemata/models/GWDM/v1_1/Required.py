from hdr_schemata.models.GWDM.v1_0 import Required as BaseRequired
from typing import Optional
from pydantic import Field, constr


class Required(BaseRequired):
    version: constr(
        pattern=r"^\d+\.\d+\.\d+$",
    ) = Field(
        ...,
        description="Dataset metadata version",
        examples=["1.1.0"],
        title="Dataset Version",
    )
