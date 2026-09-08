from typing import Optional, List
from pydantic import Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations
from .DataUsePermissions import DataUsePermissions

an = annotations.accessibility.usage

from hdr_schemata.models.HDRUK.v3_0_0.Usage import Usage as BaseUsage


class Usage(BaseUsage):
    dataUsePermissions: Optional[DataUsePermissions] = Field(
        None,
        title=an.dataUsePermissions.title,
        description=an.dataUsePermissions.description,
    )

    duoCodes: Optional[List[DuoCodesEnum]] = Field(
        None,
        **an.duoCodes.__dict__,
        json_schema_extra={"guidance": an.duoCodes.guidance}
    )
