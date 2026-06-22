from typing import List, Optional

from pydantic import BaseModel, Field

from hdr_schemata.models.GWDM.v2_0.Organisation import Organisation
from hdr_schemata.models.GWDM.v2_0.annotations import annotations as v20_an

an = v20_an.accessibility.usage


class Usage(BaseModel):
    class Config:
        extra = "forbid"

    dataUseLimitation: Optional[List[str]] = Field(
        None,
        title=an.dataUseLimitation.title,
        description=an.dataUseLimitation.description,
    )
    dataUseRequirements: Optional[List[str]] = Field(
        None,
        title=an.dataUseRequirements.title,
        description=an.dataUseRequirements.description,
    )
    resourceCreator: Optional[Organisation] = Field(None, **an.resourceCreator.__dict__)
