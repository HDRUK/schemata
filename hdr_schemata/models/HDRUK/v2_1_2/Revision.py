from typing import Optional
from pydantic import BaseModel, Field

from hdr_schemata.definitions.HDRUK import Semver, Url

from .annotations import annotations

an = annotations.revisions


class Revision(BaseModel):
    class Config:
        extra = "forbid"

    version: Semver = Field(..., **an.version.__dict__)
    url: Optional[Url] = Field(..., **an.url.__dict__)
