from typing import List
from pydantic import Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.accessibility.formatAndStandards

from hdr_schemata.models.HDRUK.v3_0_0.FormatAndStandards import (
    FormatAndStandards as BaseFormatAndStandards,
)


_NEW_IN_V2 = [
    r"- [**BNF**](https://www.bnf.org/)",
    r"- [**DDI**](https://ddialliance.org/Specification)",
    r"- [**DCAT**](https://www.w3.org/TR/vocab-dcat-3/)",
]

conformsTo_guidance = an.conformsTo.guidance + "".join(
    r"\n" + bullet for bullet in _NEW_IN_V2
)


class FormatAndStandards(BaseFormatAndStandards):
    conformsTo: List[StandardisedDataModelsEnumV2] = Field(
        ...,
        **{k: v for k, v in an.conformsTo.__dict__.items() if k != "guidance"},
        json_schema_extra={"guidance": conformsTo_guidance}
    )
