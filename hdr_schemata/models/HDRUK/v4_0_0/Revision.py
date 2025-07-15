from hdr_schemata.models.HDRUK.v3_0_0.Revision import Revision as BaseRevision
from typing import Optional
from pydantic import Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.revisions


class Revision(BaseRevision):

    url: Optional[Url] = Field(None, **an.url.__dict__)
