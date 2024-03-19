from typing import Optional
from pydantic import BaseModel, Field

from hdr_schemata.definitions.HDRUK import Semver, Url

from hdr_schemata.annotations import annotations

an = annotations.HDRUK.v2p1p2.revisions


class Revision(BaseModel):
    class Config:
        extra = "forbid"

    version: Semver = Field(..., **an.version.__dict__)
    url: Optional[Url] = Field(..., **an.url.__dict__)
