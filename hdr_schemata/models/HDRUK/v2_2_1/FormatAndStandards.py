from typing import Optional, List
from pydantic import Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.accessibility.formatAndStandards

from hdr_schemata.models.HDRUK.v2_2_0 import (
    FormatAndStandards as BaseFormatAndStandards,
)


class FormatAndStandards(BaseFormatAndStandards):
    conformsTo: Optional[List[StandardisedDataModels]] = Field(
        ..., **an.vocabularyEncodingScheme.__dict__
    )
