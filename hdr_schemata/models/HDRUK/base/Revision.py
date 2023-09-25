from typing import Optional
from pydantic import BaseModel, Field

from hdr_schemata.definitions.HDRUK import Semver, Url

class Revision(BaseModel):
    class Config:
        extra = 'forbid'

    version: Semver = Field(..., description='Semantic Version')
    url: Optional[Url] = Field(..., description='URL endpoint to obtain the version')
