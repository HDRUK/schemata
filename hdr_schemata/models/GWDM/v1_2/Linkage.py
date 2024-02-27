from typing import Optional
from hdr_schemata.models.GWDM.v1_1 import Linkage as BaseLinkage
from pydantic import Field
from hdr_schemata.definitions.HDRUK import CommaSeparatedValues


class Linkage(BaseLinkage):
    syntheticDataWebLink: Optional[CommaSeparatedValues] = Field(
        None,
        description="Links to locations of information and or raw downloads of synthetic data associated with this dataset",
        example="",
        title="Synthetic Data Web Links",
    )
