from typing import Optional, List, Union
from pydantic import Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.accessibility.formatAndStandards

from hdr_schemata.models.HDRUK.v2_2_1.FormatAndStandards import (
    FormatAndStandards as BaseFormatAndStandards,
)


class FormatAndStandards(BaseFormatAndStandards):
    vocabularyEncodingScheme: Union[
        Optional[CommaSeparatedValues], List[ControlledVocabulary]
    ] = Field(..., **an.vocabularyEncodingScheme.__dict__)

    conformsTo: List[StandardisedDataModels] = Field(
        ..., **an.conformsTo.__dict__
    )

    language: Union[Optional[CommaSeparatedValues], List[Language]] = Field(
        ..., **an.language.__dict__
    )

    format: Union[Optional[CommaSeparatedValues], List[Format]] = Field(
        ..., **an.format.__dict__
    )
