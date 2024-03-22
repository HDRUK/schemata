from typing import Optional
from pydantic import Field
from hdr_schemata.models.HDRUK.v2_1_2.Summary import Summary as BaseSummary
from hdr_schemata.definitions.HDRUK import DatasetType

from .annotations import annotations

an = annotations.summary


class Summary(BaseSummary):
    datasetType: Optional[DatasetType] = Field(..., **an.datasetType.__dict__)

    datasetSubType: Optional[DatasetType] = Field(..., **an.datasetSubType.__dict__)

    populationSize: Optional[int] = Field(..., **an.populationSize.__dict__)
