from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.models.GWDM.v1_0 import Usage as BaseUsage

from .Organisation import Organisation

from .annotations import annotations

an = annotations.accessibility.usage


class Usage(BaseUsage):
    resourceCreator: Optional[Organisation] = Field(None, **an.resourceCreator.__dict__)
