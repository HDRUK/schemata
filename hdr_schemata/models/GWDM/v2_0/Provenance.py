from typing import Optional
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .Origin import Origin
from .Temporal import Temporal

class Provenance(BaseModel):
    class Config:
        extra = 'forbid'

    origin: Optional[Origin] = Field(None)
    temporal: Temporal
