from hdr_schemata.models._shared.v1.Provenance import Provenance as BaseProvenance
from pydantic import Field
from typing import Optional
from .Origin import Origin

from .annotations import annotations

an = annotations.provenance


class Provenance(BaseProvenance):

    origin: Optional[Origin] = Field(
        None, description=an.origin.description, title=an.origin.title
    )