from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.accessibility.formatAndStandards


class FormatAndStandards(BaseModel):
    class Config:
        extra = "forbid"

    vocabularyEncodingScheme: List[ControlledVocabulary] = Field(
        ..., 
        **an.vocabularyEncodingScheme.__dict__, 
        json_schema_extra={"guidance": an.vocabularyEncodingScheme.guidance}
    )

    conformsTo: List[StandardisedDataModels] = Field(
        ..., **an.conformsTo.__dict__, json_schema_extra={"guidance": an.conformsTo.guidance}
    )

    language: Union[Optional[CommaSeparatedValues], List[Language]] = Field(
        ..., **an.language.__dict__, json_schema_extra={"guidance": an.language.guidance}
    )

    format: Union[Optional[CommaSeparatedValues], List[Format]] = Field(
        ..., **an.format.__dict__, json_schema_extra={"guidance": an.format.guidance}
    )
