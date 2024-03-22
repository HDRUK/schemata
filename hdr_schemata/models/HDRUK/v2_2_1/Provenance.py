from hdr_schemata.models.HDRUK.v2_2_0 import Provenance as BaseProvenance
from pydantic import Field
from typing import Optional
from .Origin import Origin


from .annotations import annotations

an = annotations.provenance


class Provenance(BaseProvenance):

    origin: Optional[Origin] = Field(
        None, description=an.origin.description, title=an.origin.title
    )
