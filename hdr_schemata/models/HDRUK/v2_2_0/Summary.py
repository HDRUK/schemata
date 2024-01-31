from typing import Optional
from pydantic import Field
from hdr_schemata.models.HDRUK.v2_1_2.Summary import Summary as BaseSummary
from hdr_schemata.definitions.HDRUK import DatasetType


class Summary(BaseSummary):
    datasetType: Optional[DatasetType] = Field(
        ...,
        description="Placeholder for dataset type",
        examples=[[""]],
        title="Datasetype",
    )

    datasetSubType: Optional[DatasetType] = Field(
        ...,
        description="Placeholder for dataset sub-type",
        examples=[[""]],
        title="Datasetype",
    )

    populationSize: Optional[int] = Field(
        ...,
        description="Summary population size of the cohort",
        title="Population size",
    )
