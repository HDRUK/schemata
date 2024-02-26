from hdr_schemata.models.GWDM import Gwdm11
from hdr_schemata.models.GWDM.v1_1 import *

from .Accessibility import Accessibility
from .Linkage import Linkage

from typing import Optional, List
from pydantic import Field


class Gwdm12(Gwdm11):
    linkage: Optional[Linkage] = Field(
        None,
        description="Linkage and enrichment.",
        title="Linkage",
    )

    accessibility: Accessibility = Field(
        None,
        description="Accessibility information.",
        title="Accessibility",
    )
