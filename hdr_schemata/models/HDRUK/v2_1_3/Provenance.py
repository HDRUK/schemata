from hdr_schemata.models.HDRUK.v2_1_2 import Provenance as BaseProvenance
from pydantic import Field
from typing import Optional
from .Temporal import Temporal

from hdr_schemata.annotations import annotations

an = annotations.HDRUK.v2p1p3.provenance


class Provenance(BaseProvenance):
    temporal: Optional[Temporal] = Field(
        None, description=an.temporal.description, title=an.temporal.title
    )
