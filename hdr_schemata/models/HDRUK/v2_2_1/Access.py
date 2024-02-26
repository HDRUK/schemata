from typing import Optional, List
from pydantic import Field
from hdr_schemata.definitions.HDRUK import AccessService

from hdr_schemata.models.GWDM.v1_1 import Access as BaseAccess


class Access(BaseAccess):
    accessServiceCategory = Optional[List[AccessService]] = Field(
        None,
        description="Where access to data come from: TRE/SED, direct access, open acccess, varies based on project.",
        example="",
        title="Access/governance requirementss",
    )
