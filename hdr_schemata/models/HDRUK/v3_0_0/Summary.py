from hdr_schemata.models.HDRUK.v2_2_0 import Summary as BaseSummary
from hdr_schemata.models import remove_fields_from_cls
from typing import Optional
from pydantic import Field
from hdr_schemata.definitions.HDRUK import *

from .Organisation import Organisation

from .annotations import annotations

an = annotations.summary


class Summary(BaseSummary):
    abstract: AbstractText = Field(..., **an.abstract.__dict__)

    dataProvider: Organisation = Field(
        ..., title=an.dataProvider.title, description=an.dataProvider.description
    )

    contactPoint: EmailAddress = Field(..., **an.contactPoint.__dict__)

    doiName: Optional[Doi] = Field(None, **an.doiName.__dict__)

    populationSize: int = Field(..., **an.populationSize.__dict__)


remove_fields_from_cls(Summary, ["publisher", "datasetType", "datasetSubType"])