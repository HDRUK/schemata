from pydantic import BaseModel, Field
from typing import Optional
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

    temporal: Temporal = Field(
        ..., description=an.temporal.description, title=an.temporal.title
    )
