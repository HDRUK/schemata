from typing import Optional
from pydantic import Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.accessibility.usage

from hdr_schemata.models.GWDM.v2_0.Usage import Usage as BaseUsage


class Usage(BaseUsage):
    duoCodes: Optional[CommaSeparatedValues] = Field(
        None, **an.duoCodes.__dict__
    )

    patientRecontact: Optional[CommaSeparatedValues] = Field(
        None, **an.patientRecontact.__dict__
    )
