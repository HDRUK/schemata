from typing import Optional
from pydantic import BaseModel, Field
from definitions import *

from Origin import Origin
from Temporal import Temporal

class Provenance(BaseModel):
    class Config:
        extra = 'forbid'

    origin: Optional[Origin] = None
    temporal: Temporal
