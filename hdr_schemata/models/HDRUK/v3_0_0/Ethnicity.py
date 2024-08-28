from pydantic import BaseModel, Field
from enum import Enum
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.demographicFrequency.ethnicity

class Ethnicity(BaseModel):
    bin: EthnicityEnum = Field(..., **an.bin.__dict__)
    count: int = Field(..., **an.count.__dict__)
