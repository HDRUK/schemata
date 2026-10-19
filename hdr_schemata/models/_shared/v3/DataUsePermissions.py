from typing import Optional
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.accessibility.usage.dataUsePermissions


class DataUsePermissions(BaseModel):
    class Config:
        extra = "forbid"

    patientRecontact: Optional[YesNo] = Field(
        "No",
        **an.patientRecontact.__dict__,
        json_schema_extra={"guidance": an.patientRecontact.guidance}
    )
