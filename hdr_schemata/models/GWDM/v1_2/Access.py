from typing import Optional
from pydantic import Field
from hdr_schemata.definitions.HDRUK import CommaSeparatedValues


from hdr_schemata.models.GWDM.v1_1 import Access as BaseAccess


class Access(BaseAccess):
    accessServiceCategory = Optional[CommaSeparatedValues] = Field(
        None,
        description="Where access to data come from: TRE/SED, direct access, open acccess, varies based on project.",
        example="",
        title="Access/governance requirementss",
    )
