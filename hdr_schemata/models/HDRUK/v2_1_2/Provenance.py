from typing import Optional
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .Origin import Origin
from .Temporal import Temporal

from .annotations import annotations

an = annotations.provenance


class Provenance(BaseModel):
    class Config:
        extra = "forbid"

    origin: Optional[Origin] = Field(
        None, description=an.origin.description, title=an.origin.title
    )
    temporal: Optional[Temporal] = Field(
        None, description=an.temporal.description, title=an.temporal.title
    )
