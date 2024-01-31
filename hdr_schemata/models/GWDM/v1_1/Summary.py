from hdr_schemata.models.GWDM.v1_0 import Summary as BaseSummary
from pydantic import Field
from typing import Optional
from .Organisation import Organisation

from hdr_schemata.definitions.HDRUK import DatasetType


class Summary(BaseSummary):
    # switch publisher to be an Organisation
    publisher: Optional[Organisation] = Field(
        ...,
        description="Link to details about the publisher of this dataset",
        title="Publisher",
    )

    # new field for a summary of the population size
    populationSize: Optional[int] = Field(
        None,
        description="Summary population size of the cohort",
        title="Population size",
    )

    # include a new subType for a dataset to be paired with datasetType
    datasetSubType: Optional[DatasetType] = Field(
        None,
        description="What us the subtype for this dataset?",
        title="Dataset sub type",
    )
