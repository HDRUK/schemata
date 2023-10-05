from hdr_schemata.models.GWDM.v1_1 import Summary as BaseSummary
from typing import Optional
from .Organisation import Organisation

class Summary(BaseSummary):

    #switch publisher to be an Organisation
    publisher: Optional[Organisation] = Field(
        ...,
        description="Link to details about the publisher of this dataset",
        title='Publisher',
    )

