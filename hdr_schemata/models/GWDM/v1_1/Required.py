from hdr_schemata.models.GWDM.v1_0 import Required as BaseRequired
from typing import Optional
from pydantic import Field, constr


from .annotations import annotations

an = annotations.required


class Required(BaseRequired):
    version: constr(
        pattern=r"^\d+\.\d+\.\d+$",
    ) = Field(..., **an.version.__dict__)
