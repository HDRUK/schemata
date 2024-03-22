from hdr_schemata.models.GWDM.v1_0 import Summary as BaseSummary
from pydantic import Field
from typing import Optional
from .Organisation import Organisation

from hdr_schemata.definitions.HDRUK import DatasetType

from .annotations import annotations

an = annotations.summary


class Summary(BaseSummary):
    # switch publisher to be an Organisation
    publisher: Optional[Organisation] = Field(
        ...,
        description=an.publisher.description,
        title=an.publisher.title,
    )

    # new field for a summary of the population size
    populationSize: Optional[int] = Field(None, **an.populationSize.__dict__)

    # include a new subType for a dataset to be paired with datasetType
    datasetSubType: Optional[DatasetType] = Field(None, **an.datasetSubType.__dict__)
