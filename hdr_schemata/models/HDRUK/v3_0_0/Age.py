from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK.AgeEnum import AgeEnum

from .annotations import annotations

an = annotations.demographicFrequency.age

class Age(BaseModel):
    bin: AgeEnum = Field(..., **an.bin.__dict__)
    count: int = Field(..., **an.count.__dict__)
