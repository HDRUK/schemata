from pydantic import Field
from hdr_schemata.definitions.HDRUK import *

from hdr_schemata.models.HDRUK.v2_2_0 import Accessibility as BaseAccessibility
from .Access import Access


class Accessibility(BaseAccessibility):
    access: Access = Field(
        ...,
        description="This section includes information about data access",
        title="Access",
    )
