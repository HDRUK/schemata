from typing import Optional, List
from pydantic import Field
from hdr_schemata.definitions.HDRUK import *
from .annotations import annotations

an = annotations.accessibility.usage

from hdr_schemata.models._shared.v1.Usage import Usage as BaseUsage

class Usage(BaseUsage):
    duoCodes: Optional[List[DuoCodesEnum]] = Field(
        None,
        **an.duoCodes.__dict__,
        json_schema_extra={"guidance": an.duoCodes.guidance}
    )

    patientRecontact: Optional[YesNo] = Field(
        None,
        **an.patientRecontact.__dict__,
        json_schema_extra={"guidance": an.patientRecontact.guidance}
    )
