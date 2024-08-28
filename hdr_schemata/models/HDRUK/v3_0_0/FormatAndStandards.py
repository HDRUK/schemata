from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.accessibility.formatAndStandards


class FormatAndStandards(BaseModel):
    class Config:
        extra = "forbid"

    vocabularyEncodingScheme: List[ControlledVocabularyEnum] = Field(
        ...,
        **an.vocabularyEncodingScheme.__dict__,
        json_schema_extra={"guidance": an.vocabularyEncodingScheme.guidance}
    )

    conformsTo: List[StandardisedDataModelsEnum] = Field(
        ...,
        **an.conformsTo.__dict__,
        json_schema_extra={"guidance": an.conformsTo.guidance}
    )

    language: List[LanguageEnum] = Field(
        ...,
        **an.language.__dict__,
        json_schema_extra={"guidance": an.language.guidance}
    )

    format: List[Format] = Field(
        ..., **an.format.__dict__, json_schema_extra={"guidance": an.format.guidance}
    )
