from typing import List
from pydantic import Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.accessibility.formatAndStandards

from hdr_schemata.models.HDRUK.v3_0_0.FormatAndStandards import (
    FormatAndStandards as BaseFormatAndStandards,
)


class FormatAndStandards(BaseFormatAndStandards):
    conformsTo: List[StandardisedDataModelsEnumV2] = Field(
        ...,
        **an.conformsTo.__dict__,
        json_schema_extra={"guidance": an.conformsTo.guidance}
    )
