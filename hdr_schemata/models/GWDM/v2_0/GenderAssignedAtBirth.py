from pydantic import BaseModel, Field
from enum import Enum
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.demographicFrequency.genderAssignedAtBirth

class GenderAssignedAtBirth(BaseModel):
    bin: GenderEnum = Field(..., **an.bin.__dict__)
    count: int = Field(..., **an.count.__dict__)
