from hdr_schemata.models.HDRUK.v2_2_1 import Provenance as BaseProvenance
from pydantic import Field
from typing import Optional
from .Origin import Origin
from .Temporal import Temporal

from .annotations import annotations

an = annotations.provenance


class Provenance(BaseProvenance):

    origin: Optional[Origin] = Field(
        None, description=an.origin.description, title=an.origin.title
    )

    temporal: Temporal = Field(
        None, description=an.temporal.description, title=an.temporal.title
    )