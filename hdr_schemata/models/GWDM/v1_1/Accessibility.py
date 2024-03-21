from typing import Optional
from pydantic import Field
from .Usage import Usage
from hdr_schemata.models.GWDM.v1_0 import Accessibility as BaseAccessibility


from .annotations import annotations

an = annotations.accessibility


class Accessibility(BaseAccessibility):

    usage: Optional[Usage] = Field(
        None,
        description=an.usage.description,
        title=an.usage.title,
    )
