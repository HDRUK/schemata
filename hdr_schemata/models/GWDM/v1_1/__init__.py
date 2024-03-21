from hdr_schemata.models.GWDM import Gwdm10

from hdr_schemata.models.GWDM.v1_0 import *
from .Coverage import Coverage
from .Accessibility import Accessibility
from .Required import Required
from .Summary import Summary
from .TissuesSampleCollection import TissuesSampleCollection
from typing import Optional, List
from pydantic import Field


from .annotations import annotations as an


class Gwdm11(Gwdm10):

    required: Required = Field(
        ..., description=an.required.description, title=an.required.title
    )

    summary: Summary = Field(
        ..., description=an.summary._description, title=an.summary._title
    )

    coverage: Optional[Coverage] = Field(
        None, description=an.coverage.description, title=an.coverage.title
    )

    accessibility: Accessibility = Field(
        None, description=an.accessibility.description, title=an.accessibility.title
    )

    tissuesSampleCollection: Optional[List[TissuesSampleCollection]] = Field(
        None,
        description=an.tissuesSampleCollection.description,
        title=an.tissuesSampleCollection.title,
    )
